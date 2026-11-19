#!/usr/bin/env python3
"""NF708: source-bound execution and strict audit of first global matrix gates.

Reuses the NF704 exact receipt transport without treating external arithmetic
or a generated Lean source as kernel acceptance.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

N = 242
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def one(root, name):
    found = sorted(root.rglob(name))
    assert len(found) == 1, (root, name, found)
    return found[0]


def manifest(folder):
    p = folder / "manifest.json"
    data = json.loads(p.read_text())
    for item in data["files"]:
        assert sha(folder / item["file"]) == item["sha256"], (p, item["file"])
    return data


def accepted(receipt, folder, required, field):
    data = json.loads(receipt.read_text())
    assert data["manifest_sha256"] == sha(folder / "manifest.json")
    found = data[field]
    assert set(found) == required, (receipt, len(found), len(required), required - set(found))
    assert all(set(v) <= ALLOWED for v in found.values()), receipt
    return data


def theorem_names(columns):
    names = ["nf704HRow0Gate", "nf704HRow0Projection",
             "nf704HDCol0Projection"]
    for i in range(columns):
        s = f"nf704Col{i:03d}"
        names.extend(s + x for x in ("DGate", "DProjection", "HD", "A"))
    assert len(names) == len(set(names)) == 3 + 4 * columns
    return names


def prepare(a):
    assert 1 <= a.columns <= N
    source = a.receipts
    ins = one(source / "input", "manifest.json").parent
    c = one(source / "cache-proposals", "manifest.json").parent
    f = one(source / "frontier", "manifest.json").parent
    ia = one(source / "input", "nf702-input-complete-audit.json")
    ca = one(source / "cache-audit", "nf703-cache-complete-audit.json")
    fa = one(source / "frontier-audit", "nf681-complete-audit.json")
    sm, cm, fm = manifest(ins), manifest(c), manifest(f)
    assert sm["rows"] == cm["rows"] == N
    assert sm["entries_sha256"] == cm["entry_sha256"] == fm["entry_sha256"]
    assert sm["historical_sha256"] == cm["historical_sha256"] == fm["historical_sha256"]
    assert sm["payment_sha256"] == cm["payment_sha256"] == fm["payment_sha256"]
    assert cm["cache_sha256"] == fm["cache_sha256"]
    assert sm["source_frame_sha256"] == fm["frame_sha256"]
    assert cm["frontier_manifest_sha256"] == sha(f / "manifest.json")
    assert sm["input_modules"] == [f"Rows{i:03d}" for i in range(0, N, 4)]
    assert cm["data_modules"] == [f"Rows{i:03d}" for i in range(0, N, 4)]
    inputs_expected = {"nf702InputH_symm", "nf702OriginalW"} | {
        n for r in sm["projection_rows"] for n in r["theorems"]
    }
    assert len(inputs_expected) == 50
    cache_expected = set(cm["audit_theorems"])
    assert len(cache_expected) == 7
    frontier_expected = {f"nf681Col{i:03d}{suffix}"
                         for i in range(N) for suffix in ("HD", "A")}
    assert len(frontier_expected) == 484
    accepted(ia, ins, inputs_expected, "axioms")
    accepted(ca, c, cache_expected, "axioms")
    accepted(fa, f, frontier_expected, "theorems")
    root = Path("WeilDefect/Generated")
    for origin, stage in ((ins, "NF702Inputs"), (c, "NF703Cache"), (f, "NF681")):
        dst = root / stage
        assert not dst.exists(), (dst, "generated source already exists")
        shutil.copytree(origin, dst)
    a.output.mkdir(parents=True, exist_ok=True)
    cmd = [
        "python", "scripts/emit_nf704_first_global_matrix_attachment.py",
        "--inputs", str(root / "NF702Inputs"),
        "--cache", str(root / "NF703Cache"),
        "--frontier", str(root / "NF681"),
        "--input-audit", str(ia),
        "--cache-audit", str(ca),
        "--frontier-audit", str(fa),
        "--output", str(a.output),
        "--count", str(a.columns),
    ]
    subprocess.run(cmd, check=True)
    m = manifest(a.output)
    names = theorem_names(a.columns)
    assert m["columns"] == a.columns and m["global_gate_targets"] == 2 * a.columns
    assert m["audit_theorems"] == names
    binding = {
        "schema": "NF708-first-original-global-matrix-attachment-v1",
        "columns": a.columns,
        "source_manifests": {name: sha(folder / "manifest.json")
                             for name, folder in (("inputs", ins), ("cache", c), ("frontier", f))},
        "accepted_audits": {name: sha(path)
                            for name, path in (("inputs", ia), ("cache", ca), ("frontier", fa))},
        "attachment_manifest_sha256": sha(a.output / "manifest.json"),
        "theorems": names,
        "scope": "First global HD row-zero and A column-zero projections, not complete cache validity.",
    }
    Path("nf708-binding.json").write_text(json.dumps(binding, indent=2, sort_keys=True) + "\n")
    print(f"NF708 source-bound emitter PASS: {2*a.columns} authentic global HD/A gate candidates; Lean pending")


def prepare_axioms(a):
    m = manifest(a.output)
    assert m["audit_theorems"] == theorem_names(m["columns"])
    names = m["audit_theorems"]
    imports = ["import WeilDefect.Generated.NF704Frontier.Common"] + [
        f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}"
        for i in range(m["columns"])
    ]
    body = imports + [f"#print axioms WeilDefect.{n}" for n in names]
    Path("nf708Audit.lean").write_text("\n".join(body) + "\n")
    print(f"NF708 audit source written for {len(names)} exact theorem names")


def verify_axioms(a):
    m = manifest(a.output)
    names = theorem_names(m["columns"])
    assert m["audit_theorems"] == names
    binding = json.loads(Path("nf708-binding.json").read_text())
    assert binding["theorems"] == names
    assert binding["attachment_manifest_sha256"] == sha(a.output / "manifest.json")
    text = Path("nf708-axioms.log").read_text()
    found = {}
    for n, x in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", text):
        if n in names:
            assert n not in found, n
            found[n] = [v.strip() for v in x.split(",") if v.strip()]
    for n in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms", text):
        if n in names:
            assert n not in found, n
            found[n] = []
    assert set(found) == set(names), (sorted(set(names) - set(found)), sorted(set(found) - set(names)))
    assert all(set(v) <= ALLOWED for v in found.values())
    binding["axioms"] = found
    Path("nf708-complete-audit.json").write_text(json.dumps(binding, indent=2, sort_keys=True) + "\n")
    print(f"NF708 {2*m['columns']} concrete global HD/A gates; {len(names)} declarations LEAN PASS")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("prepare", "axiom-file", "verify"))
    p.add_argument("--receipts", type=Path, default=Path("nf708-receipts"))
    p.add_argument("--output", type=Path, default=Path("WeilDefect/Generated/NF704Frontier"))
    p.add_argument("--columns", type=int, default=8)
    a = p.parse_args()
    {"prepare": prepare, "axiom-file": prepare_axioms, "verify": verify_axioms}[a.stage](a)


if __name__ == "__main__":
    main()
