#!/usr/bin/env python3
"""NF713: authenticated second original global HD/A attachment batch, indices 8..15.

The earlier NF708 (indices 0..7) kernel certificate is mandatory input.
Only the new 32 source-specific declarations are new: the three common
projection declarations are reprinted and checked to prevent source drift.
"""
import argparse
import json
import re
from pathlib import Path

from nf708_global_matrix_attachment_driver import (
    ALLOWED, manifest, sha, theorem_names
)

START, END = 8, 16
COMMON = theorem_names(0)
OLD = theorem_names(START)
NEW = COMMON + [
    f"nf704Col{i:03d}{suffix}"
    for i in range(START, END)
    for suffix in ("DGate", "DProjection", "HD", "A")
]
assert len(COMMON) == 3 and len(OLD) == 35 and len(NEW) == 35
assert len(set(OLD + NEW)) == 67


def exactly_one(root, filename):
    found = sorted(root.rglob(filename))
    assert len(found) == 1, (root, filename, found)
    return found[0]


def old_certificate(root, proposed, binding):
    cert = exactly_one(root, "nf708-complete-audit.json")
    prior_file = exactly_one(root, "manifest.json")
    prior = prior_file.parent
    audit = json.loads(cert.read_text())
    pm = manifest(prior)
    assert pm["schema"] == "NF704-global-matrix-projection-proposals-v1"
    assert pm["columns"] == START and pm["global_gate_targets"] == 2 * START
    assert pm["audit_theorems"] == OLD
    assert audit["schema"] == "NF708-first-original-global-matrix-attachment-v1"
    assert audit["columns"] == START
    assert audit["theorems"] == OLD and set(audit["axioms"]) == set(OLD)
    assert all(set(v) <= ALLOWED for v in audit["axioms"].values())
    assert audit["attachment_manifest_sha256"] == sha(prior_file)
    assert pm["input_manifest_sha256"] == binding["source_manifests"]["inputs"]
    assert pm["cache_manifest_sha256"] == binding["source_manifests"]["cache"]
    assert pm["frontier_manifest_sha256"] == binding["source_manifests"]["frontier"]
    assert audit["source_manifests"] == binding["source_manifests"]
    assert audit["accepted_audits"] == binding["accepted_audits"]
    assert proposed["columns"] == END
    assert proposed["audit_theorems"] == theorem_names(END)
    assert proposed["global_gate_targets"] == 2 * END
    assert len(proposed["audit_theorems"]) == 67
    for f in pm["files"]:
        assert sha(prior / f["file"]) == f["sha256"]
        assert sha(Path("WeilDefect/Generated/NF704Frontier") / f["file"]) == f["sha256"], f
    return audit, cert, prior_file


def verify_binding(a):
    output = a.output
    m = manifest(output)
    b = json.loads(Path("nf708-binding.json").read_text())
    assert b["columns"] == END
    assert b["theorems"] == theorem_names(END)
    assert b["attachment_manifest_sha256"] == sha(output / "manifest.json")
    assert m["input_manifest_sha256"] == b["source_manifests"]["inputs"]
    assert m["cache_manifest_sha256"] == b["source_manifests"]["cache"]
    assert m["frontier_manifest_sha256"] == b["source_manifests"]["frontier"]
    previous, old_audit_file, old_manifest_file = old_certificate(a.prior, m, b)
    expected = {
        "schema": "NF713-second-original-global-matrix-attachment-v1",
        "first": START,
        "end": END,
        "new_global_gates": 2 * (END-START),
        "new_declarations": 4 * (END-START),
        "shared_declarations": COMMON,
        "audit_theorems": NEW,
        "old_audit_sha256": sha(old_audit_file),
        "old_attachment_manifest_sha256": sha(old_manifest_file),
        "new_attachment_manifest_sha256": sha(output / "manifest.json"),
        "source_manifests": b["source_manifests"],
        "accepted_source_audits": b["accepted_audits"],
        "source_files": [
            {"file":x["file"], "sha256":x["sha256"]}
            for x in m["files"] if x["file"]=="Common.lean"
            or x["file"] in {f"Col{i:03d}.lean" for i in range(START, END)}
        ],
        "scope": "Only original HD row zero and A column zero, indices 8..15. All other global matrix identities remain open."
    }
    assert len(expected["source_files"]) == 9
    if a.stage == "prepare":
        Path("nf713-binding.json").write_text(
            json.dumps(expected, indent=2, sort_keys=True) + "\n")
        print("NF713 prior 35-theorem kernel audit and all nine previously certified sources authenticated; 16 new global matrix gate candidates")
        return expected
    stored = json.loads(Path("nf713-binding.json").read_text())
    assert stored == expected
    return expected


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("prepare", "axiom-file", "verify"))
    p.add_argument("--prior", type=Path, default=Path("nf713-prior"))
    p.add_argument("--output", type=Path, default=Path("WeilDefect/Generated/NF704Frontier"))
    a = p.parse_args()
    binding = verify_binding(a)
    if a.stage == "prepare":
        return
    if a.stage == "axiom-file":
        imports = ["import WeilDefect.Generated.NF704Frontier.Common"] + [
            f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}"
            for i in range(START, END)
        ]
        Path("nf713Audit.lean").write_text("\n".join(
            imports + [f"#print axioms WeilDefect.{n}" for n in NEW]
        ) + "\n")
        print("NF713 prepared exact 35-theorem strict audit: 32 new and 3 shared")
        return
    log = Path("nf713-axioms.log").read_text()
    found = {}
    for n, x in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if n in NEW:
            assert n not in found, n
            found[n] = [v.strip() for v in x.split(",") if v.strip()]
    for n in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if n in NEW:
            assert n not in found, n
            found[n] = []
    assert set(found) == set(NEW), (sorted(set(NEW)-set(found)), sorted(set(found)-set(NEW)))
    assert all(set(v) <= ALLOWED for v in found.values())
    binding["axioms"] = found
    binding["unique_cumulative_declarations"] = len(set(OLD+NEW))
    binding["cumulative_global_gates"] = 2*END
    Path("nf713-complete-audit.json").write_text(
        json.dumps(binding, indent=2, sort_keys=True) + "\n")
    print("NF713 new 16 actual global HD/A gates, 32 new declarations, cumulative 32 matrix gates / 67 declarations LEAN PASS")


if __name__ == "__main__":
    main()
