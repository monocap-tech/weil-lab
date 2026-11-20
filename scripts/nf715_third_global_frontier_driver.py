#!/usr/bin/env python3
"""NF715: third authenticated original global matrix and vector gate batches.

The new certificates depend on the complete NF708 -> NF713 matrix audit chain
and NF709 -> NF714 vector audit chain. Identical source hashes, source manifest
digests, accepted local receipts, and strictly standard Lean axioms are required.
The newly emitted declarations are NOT accepted until the NF715 Lean jobs pass.
"""
import argparse
import json
import re
from pathlib import Path

from nf708_global_matrix_attachment_driver import (
    ALLOWED, manifest as matrix_manifest, sha, theorem_names
)
from emit_nf709_original_global_vector_attachments import (
    COMMON as VECTOR_COMMON, check_manifest as vector_manifest, row_names
)

M_START, M_END = 16, 24
V_START, V_END = 32, 48
MC = theorem_names(0)
M_FIRST = theorem_names(8)
M_SECOND = theorem_names(16)
M_NEW = MC + [
    f"nf704Col{i:03d}{s}" for i in range(M_START, M_END)
    for s in ("DGate", "DProjection", "HD", "A")
]
V_FIRST = list(VECTOR_COMMON) + [
    n for i in range(16) for n in row_names(i)
]
V_SECOND = list(VECTOR_COMMON) + [
    n for i in range(16, 32) for n in row_names(i)
]
V_NEW = list(VECTOR_COMMON) + [
    n for i in range(V_START, V_END) for n in row_names(i)
]
assert (len(M_FIRST), len(M_SECOND), len(M_NEW)) == (35, 67, 35)
assert len(set(M_SECOND + M_NEW)) == 99
assert (len(V_FIRST), len(V_SECOND), len(V_NEW)) == (230, 230, 230)
assert len(set(V_FIRST + V_SECOND + V_NEW)) == 678


def one(root, filename):
    paths = sorted(root.rglob(filename))
    assert len(paths) == 1, (root, filename, paths)
    return paths[0]


def read(path):
    return json.loads(path.read_text())


def audit_axioms(cert, names):
    assert set(cert["axioms"]) == set(names), (
        sorted(set(names)-set(cert["axioms"])), sorted(set(cert["axioms"])-set(names)))
    assert all(set(v) <= ALLOWED for v in cert["axioms"].values())


def build_binding_matrix(a):
    p1 = one(a.prior_first, "manifest.json")
    p2 = one(a.prior_second, "manifest.json")
    f1 = one(a.prior_first, "nf708-complete-audit.json")
    f2 = one(a.prior_second, "nf713-complete-audit.json")
    m1, m2, m3 = (
        matrix_manifest(p1.parent), matrix_manifest(p2.parent),
        matrix_manifest(a.output)
    )
    c1, c2 = read(f1), read(f2)
    b = read(Path("nf708-binding.json"))
    assert (m1["schema"], m2["schema"], m3["schema"]) == (
        "NF704-global-matrix-projection-proposals-v1",)*3
    assert [m1["columns"], m2["columns"], m3["columns"]] == [8, 16, M_END]
    assert [m1["global_gate_targets"], m2["global_gate_targets"],
            m3["global_gate_targets"]] == [16, 32, 2*M_END]
    assert (m1["audit_theorems"], m2["audit_theorems"],
            m3["audit_theorems"]) == (M_FIRST, M_SECOND, theorem_names(M_END))
    assert [len(m1["files"]), len(m2["files"]), len(m3["files"])] == [9, 17, 25]
    assert b["columns"] == M_END and b["theorems"] == theorem_names(M_END)
    assert b["attachment_manifest_sha256"] == sha(a.output/"manifest.json")

    assert c1["schema"] == "NF708-first-original-global-matrix-attachment-v1"
    assert c1["columns"] == 8 and c1["theorems"] == M_FIRST
    assert c1["attachment_manifest_sha256"] == sha(p1)
    audit_axioms(c1, M_FIRST)
    assert c2["schema"] == "NF713-second-original-global-matrix-attachment-v1"
    assert (c2["first"], c2["end"]) == (8, 16)
    assert c2["audit_theorems"] == MC + [
        f"nf704Col{i:03d}{s}" for i in range(8,16)
        for s in ("DGate","DProjection","HD","A")
    ]
    assert c2["new_global_gates"] == 16
    assert c2["new_attachment_manifest_sha256"] == sha(p2)
    assert c2["old_attachment_manifest_sha256"] == sha(p1)
    assert c2["old_audit_sha256"] == sha(f1)
    audit_axioms(c2, c2["audit_theorems"])
    assert c2["source_manifests"] == c1["source_manifests"] == b["source_manifests"]
    assert c2["accepted_source_audits"] == c1["accepted_audits"] == b["accepted_audits"]
    for m in (m1, m2, m3):
        assert m["input_manifest_sha256"] == b["source_manifests"]["inputs"]
        assert m["cache_manifest_sha256"] == b["source_manifests"]["cache"]
        assert m["frontier_manifest_sha256"] == b["source_manifests"]["frontier"]
    # New source must preserve all 17 previously certified modules byte-for-byte.
    previous_sources = {f["file"]: f["sha256"] for f in m2["files"]}
    first_sources = {f["file"]: f["sha256"] for f in m1["files"]}
    current_sources = {f["file"]: f["sha256"] for f in m3["files"]}
    assert set(first_sources) <= set(previous_sources) <= set(current_sources)
    assert all(first_sources[k] == previous_sources[k] == current_sources[k]
               for k in first_sources)
    assert all(previous_sources[k] == current_sources[k] for k in previous_sources)
    assert {f["file"]: f["sha256"] for f in c2["source_files"]} == {
        k: current_sources[k] for k in ["Common.lean"] + [
            f"Col{i:03d}.lean" for i in range(8,16)]}
    expected = {
        "schema": "NF715-third-original-global-matrix-attachment-v1",
        "first": M_START, "end": M_END, "new_global_gates": 2*(M_END-M_START),
        "new_declarations": 4*(M_END-M_START),
        "shared_declarations": MC,
        "audit_theorems": M_NEW,
        "first_accepted_audit_sha256": sha(f1),
        "second_accepted_audit_sha256": sha(f2),
        "first_source_manifest_sha256": sha(p1),
        "second_source_manifest_sha256": sha(p2),
        "new_attachment_manifest_sha256": sha(a.output/"manifest.json"),
        "accepted_original_source_manifests": b["source_manifests"],
        "accepted_source_audits": b["accepted_audits"],
        "prior_17_files_preserved": previous_sources,
        "new_source_files": {
            k: current_sources[k] for k in ["Common.lean"] + [
                f"Col{i:03d}.lean" for i in range(M_START, M_END)]
        },
        "scope": "Original HD row 0 and A column 0 for columns 16..23 only; full matrix and global Weil positivity remain open."
    }
    return expected


def build_binding_vector(a):
    p1 = one(a.prior_first, "manifest.json")
    p2 = one(a.prior_second, "manifest.json")
    f1 = one(a.prior_first, "nf709-complete-audit.json")
    f2 = one(a.prior_second, "nf714-complete-audit.json")
    m1, m2, m3 = (
        vector_manifest(p1.parent), vector_manifest(p2.parent),
        vector_manifest(a.output)
    )
    c1, c2 = read(f1), read(f2)
    assert m1["schema"] == m2["schema"] == m3["schema"] == (
        "NF709-global-original-vector-attachments-v1")
    assert [(m["first"], m["count"], m["rows"]) for m in (m1,m2,m3)] == [
        (0,16,list(range(16))), (16,16,list(range(16,32))),
        (V_START,16,list(range(V_START,V_END)))]
    assert [m1["theorems"],m2["theorems"],m3["theorems"]] == [
        V_FIRST,V_SECOND,V_NEW]
    assert [len(m["files"]) for m in (m1,m2,m3)] == [17,17,17]
    assert c1["schema"] == "NF709-first-global-original-vector-audit-v1"
    assert c1["rows"] == list(range(16))
    assert c1["manifest_sha256"] == sha(p1)
    audit_axioms(c1,V_FIRST)
    assert c2["schema"] == "NF714-second-original-global-vector-attachment-v1"
    assert (c2["first"], c2["end"]) == (16,32)
    assert c2["audit_theorems"] == V_SECOND
    assert c2["prior_accepted_audit_sha256"] == sha(f1)
    assert c2["prior_source_manifest_sha256"] == sha(p1)
    assert c2["current_source_manifest_sha256"] == sha(p2)
    audit_axioms(c2,V_SECOND)
    assert c1["source_manifests"] == m1["source_manifests"] == (
        m2["source_manifests"]) == m3["source_manifests"]
    assert c1["accepted_audits"] == m1["accepted_audits"] == (
        m2["accepted_audits"]) == m3["accepted_audits"]
    assert c2["accepted_original_source_manifests"] == m3["source_manifests"]
    assert c2["accepted_source_audits"] == m3["accepted_audits"]
    shared = [m1["files"][0],m2["files"][0],m3["files"][0]]
    assert all(f["file"] == "Common.lean" for f in shared)
    assert len({f["sha256"] for f in shared}) == 1
    assert c2["old_common_source_sha256"] == shared[0]["sha256"]
    assert c2["new_common_source_sha256"] == shared[1]["sha256"]
    assert {f["file"] for f in m3["files"]} == {
        "Common.lean"} | {f"Row{i:03d}.lean" for i in range(V_START,V_END)}
    expected = {
        "schema": "NF715-third-original-global-vector-attachment-v1",
        "first": V_START, "end": V_END,
        "new_global_vector_gates": V_END-V_START,
        "new_declarations": 14*(V_END-V_START),
        "shared_declarations": list(VECTOR_COMMON),
        "audit_theorems": V_NEW,
        "first_accepted_audit_sha256": sha(f1),
        "second_accepted_audit_sha256": sha(f2),
        "first_source_manifest_sha256": sha(p1),
        "second_source_manifest_sha256": sha(p2),
        "new_source_manifest_sha256": sha(a.output/"manifest.json"),
        "accepted_original_source_manifests": m3["source_manifests"],
        "accepted_source_audits": m3["accepted_audits"],
        "old_shared_source_sha256": shared[0]["sha256"],
        "new_shared_source_sha256": shared[2]["sha256"],
        "scope": "Original global vector rows 32..47 only; remaining 194 rows and full cache closure remain open."
    }
    return expected


def axioms_from_log(filename, names):
    log = Path(filename).read_text()
    expected = set(names)
    found = {}
    for n, x in re.findall(
            r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if n in expected:
            assert n not in found
            found[n] = [v.strip() for v in x.split(",") if v.strip()]
    for n in re.findall(
            r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if n in expected:
            assert n not in found
            found[n] = []
    assert set(found) == expected, (
        sorted(expected-set(found)), sorted(set(found)-expected))
    assert all(set(v) <= ALLOWED for v in found.values())
    return found


def main():
    p = argparse.ArgumentParser()
    p.add_argument("kind", choices=("matrix", "vector"))
    p.add_argument("stage", choices=("prepare", "axiom-file", "verify"))
    p.add_argument("--prior-first", type=Path)
    p.add_argument("--prior-second", type=Path)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    if a.kind == "matrix":
        a.prior_first = a.prior_first or Path("nf715-matrix-first")
        a.prior_second = a.prior_second or Path("nf715-matrix-second")
        a.output = a.output or Path("WeilDefect/Generated/NF704Frontier")
        binding = build_binding_matrix(a)
        bindpath = Path("nf715-matrix-binding.json")
        names = M_NEW
    else:
        a.prior_first = a.prior_first or Path("nf715-vector-first")
        a.prior_second = a.prior_second or Path("nf715-vector-second")
        a.output = a.output or Path("WeilDefect/Generated/NF709")
        binding = build_binding_vector(a)
        bindpath = Path("nf715-vector-binding.json")
        names = V_NEW
    if a.stage == "prepare":
        bindpath.write_text(json.dumps(binding,indent=2,sort_keys=True)+"\n")
        print(f"NF715 {a.kind} source-bound accepted audit chain verified; "
              f"{len(names)} new-batch declarations proposed")
        return
    assert read(bindpath) == binding
    if a.stage == "axiom-file":
        if a.kind == "matrix":
            imports = ["import WeilDefect.Generated.NF704Frontier.Common"] + [
                f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}"
                for i in range(M_START, M_END)]
        else:
            imports = [f"import WeilDefect.Generated.NF709.Row{i:03d}"
                       for i in range(V_START,V_END)]
        path = Path(f"nf715{a.kind.title()}Audit.lean")
        path.write_text("\n".join(imports + [
            f"#print axioms WeilDefect.{n}" for n in names])+"\n")
        print(f"NF715 {a.kind} strict axiom audit source: {len(names)} declarations")
        return
    logpath = f"nf715-{a.kind}-axioms.log"
    binding["axioms"] = axioms_from_log(logpath,names)
    if a.kind == "matrix":
        binding["cumulative_original_global_matrix_gates"] = 2*M_END
        binding["unique_cumulative_declarations"] = len(
            set(M_SECOND + M_NEW))
    else:
        binding["cumulative_original_global_vector_gates"] = V_END
        binding["unique_cumulative_declarations"] = len(
            set(V_FIRST + V_SECOND + V_NEW))
    path = Path(f"nf715-{a.kind}-complete-audit.json")
    path.write_text(json.dumps(binding,indent=2,sort_keys=True)+"\n")
    print(f"NF715 {a.kind.upper()} original global gates accepted; "
          f"cumulative {binding.get('cumulative_original_global_matrix_gates',binding.get('cumulative_original_global_vector_gates'))} LEAN PASS")


if __name__ == "__main__":
    main()
