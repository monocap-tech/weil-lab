#!/usr/bin/env python3
"""NF714: continue actual original global vector gates from accepted rows 0..15.

Verify NF709's standard-axiom 230-theorem kernel audit, all original source
manifest digests and every certified old source before admitting rows 16..31.
The new vector gates are only considered proved after an independent Lean
kernel + strict 230-theorem audit.
"""
import argparse
import json
import re
from pathlib import Path
from emit_nf709_original_global_vector_attachments import (
    ALLOWED, COMMON, row_names, sha, check_manifest
)

START = 16
END = 32
OLD = list(COMMON) + [name for i in range(START) for name in row_names(i)]
NEW = list(COMMON) + [name for i in range(START, END) for name in row_names(i)]
assert len(OLD) == len(NEW) == 230
assert len(set(OLD + NEW)) == 454


def unique(root, name):
    candidates = sorted(root.rglob(name))
    assert len(candidates) == 1, (root, name, candidates)
    return candidates[0]


def accepted_prior(folder):
    previous_manifest = unique(folder, "manifest.json")
    assert previous_manifest.parent.name == "NF709"
    previous_dir = previous_manifest.parent
    previous = check_manifest(previous_dir)
    cert_file = unique(folder, "nf709-complete-audit.json")
    cert = json.loads(cert_file.read_text())
    assert previous["schema"] == "NF709-global-original-vector-attachments-v1"
    assert (previous["first"], previous["count"], previous["rows"]) == (
        0, START, list(range(START)))
    assert previous["theorems"] == OLD
    assert len(previous["files"]) == 17
    assert cert["schema"] == "NF709-first-global-original-vector-audit-v1"
    assert cert["rows"] == list(range(START))
    assert cert["manifest_sha256"] == sha(previous_manifest)
    assert cert["source_manifests"] == previous["source_manifests"]
    assert cert["accepted_audits"] == previous["accepted_audits"]
    assert set(cert["axioms"]) == set(OLD)
    assert all(set(a) <= ALLOWED for a in cert["axioms"].values())
    return previous, cert, previous_dir, cert_file, previous_manifest


def bind(a):
    current_dir = a.output
    current = check_manifest(current_dir)
    old, audit, old_dir, audit_file, old_manifest_file = accepted_prior(a.prior)
    assert current["schema"] == "NF709-global-original-vector-attachments-v1"
    assert (current["first"], current["count"], current["rows"]) == (
        START, END-START, list(range(START, END)))
    assert current["theorems"] == NEW
    assert len(current["files"]) == 17
    assert current["source_manifests"] == old["source_manifests"]
    assert current["accepted_audits"] == old["accepted_audits"]
    assert sha(current_dir / "Common.lean") == sha(old_dir / "Common.lean")
    assert {f["file"] for f in old["files"]} == {
        "Common.lean"} | {f"Row{i:03d}.lean" for i in range(START)}
    assert {f["file"] for f in current["files"]} == {
        "Common.lean"} | {f"Row{i:03d}.lean" for i in range(START, END)}
    binding = {
        "schema": "NF714-second-original-global-vector-attachment-v1",
        "first": START, "end": END,
        "new_global_vector_gates": END-START,
        "new_declarations": 14*(END-START),
        "shared_declarations": list(COMMON),
        "audit_theorems": NEW,
        "prior_accepted_audit_sha256": sha(audit_file),
        "prior_source_manifest_sha256": sha(old_manifest_file),
        "current_source_manifest_sha256": sha(current_dir / "manifest.json"),
        "accepted_original_source_manifests": current["source_manifests"],
        "accepted_source_audits": current["accepted_audits"],
        "old_common_source_sha256": sha(old_dir / "Common.lean"),
        "new_common_source_sha256": sha(current_dir / "Common.lean"),
        "scope": "Original global vector gates for rows 16..31; remaining 210 rows, full HD/A cache, physical entries and payment closure open."
    }
    if a.stage == "prepare":
        Path("nf714-binding.json").write_text(json.dumps(binding, indent=2) + "\n")
        print("NF714 authenticated exact NF709 230-theorem acceptance and identical common source; 16 new original vector gates proposed")
    else:
        assert json.loads(Path("nf714-binding.json").read_text()) == binding
    return binding


def prepare_axioms():
    imports = [f"import WeilDefect.Generated.NF709.Row{i:03d}"
               for i in range(START, END)]
    prints = [f"#print axioms WeilDefect.{n}" for n in NEW]
    Path("nf714Audit.lean").write_text("\n".join(imports+prints)+"\n")
    print("NF714 strict audit file ready: 224 new and 6 shared theorem declarations")


def verify_log(a, binding):
    log = Path("nf714-axioms.log").read_text()
    expected = set(NEW)
    observed = {}
    for n, raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if n in expected:
            assert n not in observed
            observed[n] = [z.strip() for z in raw.split(",") if z.strip()]
    for n in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if n in expected:
            assert n not in observed
            observed[n] = []
    assert set(observed) == expected, (
        sorted(expected - set(observed)), sorted(set(observed) - expected))
    assert all(set(z) <= ALLOWED for z in observed.values())
    binding["axioms"] = observed
    binding["cumulative_global_vector_gates"] = END
    binding["unique_cumulative_theorems"] = len(set(OLD + NEW))
    Path("nf714-complete-audit.json").write_text(
        json.dumps(binding, indent=2) + "\n")
    print("NF714 16 additional original global vector gates, 224 new declarations, cumulative 32 vector gates / 454 unique theorem declarations LEAN PASS")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("prepare", "axiom-file", "verify"))
    p.add_argument("--prior", type=Path, default=Path("nf714-prior"))
    p.add_argument("--output", type=Path,
                   default=Path("WeilDefect/Generated/NF709"))
    a = p.parse_args()
    binding = bind(a)
    if a.stage == "axiom-file":
        prepare_axioms()
    if a.stage == "verify":
        verify_log(a, binding)


if __name__ == "__main__":
    main()
