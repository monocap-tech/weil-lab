#!/usr/bin/env python3
"""NF720: final bounded, source-authenticated original HD/A row-one blocks 24..30.

Two independent bounded jobs certify coordinates 192..223 and 224..241, including the final Fin 2 packed block.
Neither depends on provisional NF716, NF717 or NF718 proof results; each
independently replays the accepted NF715 source and its kernel-axiom receipt
from the same immutable NF702, NF703, NF700 proposals and audits.

The aggregate stage refuses gaps, overlaps, source drift or missing/extra
axiom entries, and only runs after both shard jobs finish successfully.
"""
import argparse
import json
import re
from pathlib import Path

from emit_nf630_original_literal_payments import filetext
from nf716_second_global_matrix_row_continuation import (
    ALLOWED, WIDTH, OPTIONS, generated_block, reproduce_nf715,
    source_manifest, sha
)

STAGE = "nf720"
MODULE = "WeilDefect.Generated.NF720"
SHARDS = ((24, 28), (28, 31))
SUFFIXES = (
    "DGate", "DProjection", "HDTargetGate", "HDTargetProjection",
    "ATargetGate", "ATargetProjection", "GlobalHD", "GlobalA"
)
FIRST_COORD, LAST_COORD = 192, 242


def expected_names(first, end):
    return [
        f"nf720Block{block:03d}{suffix}"
        for block in range(first, end)
        for suffix in SUFFIXES
    ]


def expected_coordinates(first, end):
    return list(range(WIDTH * first, min(WIDTH * end, 242)))


def shard_range(first, end):
    assert (first, end) in SHARDS, (first, end)
    return range(first, end)


def preflight(a):
    blocks = shard_range(a.first_block, a.end_block)
    rows = []
    for block in blocks:
        src = generated_block(block, stage=STAGE,
                              lower=a.first_block, upper=a.end_block)
        names = expected_names(block, block + 1)
        assert len(names) == 8
        assert len(src.split("theorem ")) == 9
        assert all("theorem " + n in src for n in names)
        assert f"nf700Block{block:03d}HDAllCoordinates j" in src
        assert f"nf700Block{block:03d}AAllCoordinates j" in src
        assert f"⟨{block * WIDTH} + j.val, by omega⟩" in src
        rows.extend(range(WIDTH*block, min(WIDTH*(block+1),242)))
    assert rows == expected_coordinates(a.first_block, a.end_block)
    print(f"NF720 bounded shard {a.first_block}–{a.end_block}: exact {len(rows)}-coordinate HD/A inventory PASS ({2*len(rows)} conditional gates)")


def prepare(a):
    preflight(a)
    original, baseline, nf715_receipt = reproduce_nf715(a)
    packed = source_manifest(Path("WeilDefect/Generated/NF700"))
    assert packed["schema"] == "NF700-original-packed-second-matrix-frontier-v1"
    assert packed["H_source_row"] == packed["HD_source_column"] == 1
    assert packed["HD_exact_external"] == packed["A_exact_external"] == 242
    assert len(packed["blocks"]) == 31
    assert len(packed["files"]) == 32
    assert baseline["row"] == baseline["column"] == 1
    assert baseline["first"] == 0 and baseline["end"] == 8
    assert baseline["actual_global_HD_gates"] == baseline["actual_global_A_gates"] == 8
    a.output.mkdir(parents=True, exist_ok=True)
    files, names, coordinates = [], [], []
    for block in shard_range(a.first_block, a.end_block):
        b = packed["blocks"][block]
        assert b["module"] == f"Block{block:03d}"
        assert (b["start"], b["stop"], b["width"]) == (
            block * WIDTH, min((block+1)*WIDTH, 242),
            min(WIDTH, 242 - block*WIDTH))
        assert {f"nf700Block{block:03d}HDAllCoordinates",
                f"nf700Block{block:03d}AAllCoordinates"} <= set(b["theorems"])
        generated = generated_block(
            block, stage=STAGE, lower=a.first_block, upper=a.end_block)
        ns = expected_names(block, block+1)
        generated += "\n".join(f"#print axioms {n}" for n in ns) + "\n"
        path = a.output / f"Block{block:03d}.lean"
        path.write_text(filetext([
            "WeilDefect.Generated.NF715.Common",
            f"WeilDefect.Generated.NF700.Block{block:03d}",
        ], OPTIONS + generated))
        files.append({"file": path.name, "sha256": sha(path)})
        names.extend(ns)
        coordinates.extend(range(block*WIDTH, min((block+1)*WIDTH, 242)))
    assert len(names) == len(set(names)) == 8*(a.end_block-a.first_block)
    assert coordinates == expected_coordinates(a.first_block, a.end_block)
    m = {
        "schema": "NF720-parallel-original-global-row-one-shard-v1",
        "original_index": 1, "first_block": a.first_block,
        "end_block": a.end_block,
        "blocks": list(shard_range(a.first_block, a.end_block)),
        "first": WIDTH*a.first_block, "end": min(WIDTH*a.end_block, 242),
        "coordinates": coordinates,
        "new_HD_gates": len(coordinates),
        "new_A_gates": len(coordinates),
        "audit_theorems": names, "files": files,
        "accepted_nf715_manifest_sha256": sha(original/"manifest.json"),
        "accepted_nf715_audit_sha256": sha(nf715_receipt),
        "nf700_packed_manifest_sha256":
            sha(Path("WeilDefect/Generated/NF700/manifest.json")),
        "source_manifests": baseline["source_manifests"],
        "accepted_source_audits": baseline["accepted_audits"],
        "scope": (
            "Exact index-one original HD/A matrix products on one of two"
            " bounded source-bound shards; separate final aggregate required."
            " Does not assert full global matrix or global Weil positivity."
        ),
    }
    (a.output/"manifest.json").write_text(json.dumps(m, indent=2)+"\n")
    print(f"NF720 original index-one source-bound shard {a.first_block}–{a.end_block}: {2*len(coordinates)} authentic global product candidates; Lean pending")


def audit_file(a):
    m = source_manifest(a.output)
    assert m["schema"] == "NF720-parallel-original-global-row-one-shard-v1"
    assert (m["first_block"], m["end_block"]) == (a.first_block, a.end_block)
    names = expected_names(a.first_block, a.end_block)
    assert m["audit_theorems"] == names
    imports = [f"import {MODULE}.Block{block:03d}"
               for block in shard_range(a.first_block, a.end_block)]
    Path("nf720Audit.lean").write_text(
        "\n".join(imports + [f"#print axioms WeilDefect.{n}" for n in names])+"\n")


def verify(a):
    m = source_manifest(a.output)
    assert m["schema"] == "NF720-parallel-original-global-row-one-shard-v1"
    assert (m["first_block"], m["end_block"]) == (a.first_block, a.end_block)
    assert m["audit_theorems"] == expected_names(a.first_block, a.end_block)
    assert m["coordinates"] == expected_coordinates(a.first_block, a.end_block)
    assert m["new_HD_gates"] == m["new_A_gates"] == len(m["coordinates"])
    log = Path("nf720-axioms.log").read_text()
    expected = set(m["audit_theorems"])
    found = {}
    for n, raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if n in expected:
            assert n not in found, n
            found[n] = [z.strip() for z in raw.split(",") if z.strip()]
    for n in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if n in expected:
            assert n not in found, n
            found[n] = []
    assert set(found) == expected, (
        sorted(expected-set(found)), sorted(set(found)-expected))
    assert len(found) == 8*(a.end_block-a.first_block)
    assert all(set(v) <= ALLOWED for v in found.values())
    audit = {
        "schema": "NF720-parallel-original-global-row-one-shard-audit-v1",
        "manifest_sha256": sha(a.output/"manifest.json"),
        "original_index": 1,
        "first_block": a.first_block, "end_block": a.end_block,
        "coordinates": m["coordinates"],
        "audit_theorems": m["audit_theorems"],
        "source_manifests": m["source_manifests"],
        "accepted_source_audits": m["accepted_source_audits"],
        "accepted_nf715_manifest_sha256": m["accepted_nf715_manifest_sha256"],
        "accepted_nf715_audit_sha256": m["accepted_nf715_audit_sha256"],
        "nf700_packed_manifest_sha256": m["nf700_packed_manifest_sha256"],
        "axioms": found,
        "scope": "32 HD and 32 A actual original global gates accepted in this bounded shard only.",
    }
    Path("nf720-shard-audit.json").write_text(
        json.dumps(audit, indent=2, sort_keys=True)+"\n")
    print(f"NF720 bounded original row-one shard {a.first_block}–{a.end_block}: {2*len(m['coordinates'])} global gates, {len(found)} declarations LEAN PASS")


def aggregate(a):
    expected_range = SHARDS
    matched = list(a.audits.rglob("nf720-shard-audit.json"))
    assert len(matched) == len(expected_range), matched
    audits = []
    for path in matched:
        audit = json.loads(path.read_text())
        manifest_dir = path.parent/"WeilDefect/Generated/NF720"
        manifest_path = manifest_dir/"manifest.json"
        m = source_manifest(manifest_dir)
        assert audit["schema"] == "NF720-parallel-original-global-row-one-shard-audit-v1"
        assert m["schema"] == "NF720-parallel-original-global-row-one-shard-v1"
        assert audit["manifest_sha256"] == sha(manifest_path)
        assert audit["first_block"] == m["first_block"]
        assert audit["end_block"] == m["end_block"]
        assert audit["coordinates"] == m["coordinates"]
        assert audit["audit_theorems"] == m["audit_theorems"]
        for key in ("source_manifests", "accepted_source_audits",
                    "accepted_nf715_manifest_sha256",
                    "accepted_nf715_audit_sha256",
                    "nf700_packed_manifest_sha256"):
            assert audit[key] == m[key]
        assert set(audit["axioms"]) == set(m["audit_theorems"])
        assert all(set(v) <= ALLOWED for v in audit["axioms"].values())
        assert m["new_HD_gates"] == m["new_A_gates"] == len(m["coordinates"])
        assert len(m["files"]) == m["end_block"]-m["first_block"]
        audits.append((audit, m, manifest_path))
    audits.sort(key=lambda record: record[0]["first_block"])
    assert [(item[0]["first_block"], item[0]["end_block"])
            for item in audits] == list(expected_range)
    combined_names, combined_coords, found = [], [], {}
    for audit, m, path in audits:
        assert m["audit_theorems"] == expected_names(m["first_block"], m["end_block"])
        assert m["coordinates"] == expected_coordinates(m["first_block"], m["end_block"])
        combined_names.extend(audit["audit_theorems"])
        combined_coords.extend(audit["coordinates"])
        for name, axioms in audit["axioms"].items():
            assert name not in found, name
            found[name] = axioms
    assert combined_coords == list(range(FIRST_COORD, LAST_COORD))
    assert len(found) == len(combined_names) == 56
    assert set(combined_names) == set(found)
    for key in ("source_manifests", "accepted_source_audits",
                "accepted_nf715_manifest_sha256", "accepted_nf715_audit_sha256",
                "nf700_packed_manifest_sha256"):
        assert all(item[0][key] == audits[0][0][key] for item in audits)
    result = {
        "schema": "NF720-complete-parallel-original-global-row-one-audit-v1",
        "index": 1, "first": FIRST_COORD, "end": LAST_COORD,
        "coordinates": combined_coords, "global_HD_gates": 50,
        "global_A_gates": 50,
        "lean_declarations": 56,
        "shard_audit_sha256": [
            sha(manifest_path.parents[3]/"nf720-shard-audit.json")
            for _, _, manifest_path in audits
        ],
        "accepted_nf715_audit_sha256": audits[0][0]["accepted_nf715_audit_sha256"],
        "source_manifests": audits[0][0]["source_manifests"],
        "accepted_source_audits": audits[0][0]["accepted_source_audits"],
        "axioms": found,
        "scope": "100 genuine original index-one global matrix gates for coordinates 192..241 only. Combined prior index-one batches close this row/column only after their independent audits pass; complete cache and global positivity remain open.",
    }
    Path("nf720-complete-audit.json").write_text(
        json.dumps(result, indent=2, sort_keys=True)+"\n")
    print("NF720 two strict independent kernel-accepted shards: 100 original global matrix HD/A gates, 56 unique declarations LEAN PASS")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("preflight", "prepare", "axiom-file", "verify", "aggregate"))
    p.add_argument("--first-block", type=int, default=24)
    p.add_argument("--end-block", type=int, default=28)
    p.add_argument("--receipts", type=Path, default=Path("nf720-receipts"))
    p.add_argument("--prior", type=Path, default=Path("nf720-prior"))
    p.add_argument("--output", type=Path, default=Path("WeilDefect/Generated/NF720"))
    p.add_argument("--audits", type=Path, default=Path("nf720-audits"))
    a = p.parse_args()
    if a.stage == "aggregate":
        aggregate(a)
    else:
        {"preflight": preflight, "prepare": prepare,
         "axiom-file": audit_file, "verify": verify}[a.stage](a)


if __name__ == "__main__":
    main()
