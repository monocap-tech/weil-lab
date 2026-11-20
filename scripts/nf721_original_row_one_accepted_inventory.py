#!/usr/bin/env python3
"""NF721: exact accepted original second-row certificate inventory.

This *does not* prove new Lean propositions. It checks the complete upstream
standard-axiom certificates for NF715, NF716, NF718 and NF719, their original
source/projection provenance, exact coordinate disjointness and missing gaps.
Only 160 genuine HD row-one and 160 A column-one identities are admitted here.
The NF717 and NF720 intervals are explicitly OPEN until their own final audits.
"""
import argparse
import hashlib
import json
from pathlib import Path

N = 242
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
STAGES = (
    ("nf715", 0, 8, 12),
    ("nf716", 8, 32, 24),
    ("nf718", 64, 128, 64),
    ("nf719", 128, 192, 64),
)
PENDING = ((32, 64, "NF717"), (192, 242, "NF720"))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def one(root, filename):
    found = sorted(root.rglob(filename))
    assert len(found) == 1, (root, filename, found)
    return found[0]


def jfile(p):
    return json.loads(p.read_text())


def audit_axioms(cert, count):
    axioms = cert["axioms"]
    names = cert["audit_theorems"] if "audit_theorems" in cert else list(axioms)
    assert len(names) == len(set(names)) == count
    assert set(axioms) == set(names)
    assert all(isinstance(z, list) and set(z) <= ALLOWED
               for z in axioms.values())
    return set(names)


def source_files(folder):
    manifest_path = folder / "manifest.json"
    m = jfile(manifest_path)
    for item in m["files"]:
        assert sha(folder / item["file"]) == item["sha256"], item
    assert len(m["files"]) == len({item["file"] for item in m["files"]})
    return m, sha(manifest_path)


def analyze(root):
    evidence = {}
    for label, lo, hi, n in STAGES:
        d = root / label
        cert_path = one(d, f"{label}-complete-audit.json")
        cert = jfile(cert_path)
        names = audit_axioms(cert, n)
        record = {
            "stage": label, "coordinates": list(range(lo, hi)),
            "HD_gates": hi-lo, "A_gates": hi-lo,
            "lean_theorem_declarations": n,
            "certificate_sha256": sha(cert_path),
            "theorem_names": sorted(names),
        }
        if label in ("nf715", "nf716"):
            mpath = one(d, "manifest.json")
            manifest, digest = source_files(mpath.parent)
            record["source_manifest_sha256"] = digest
            assert manifest["audit_theorems"] == cert["audit_theorems"]
            assert manifest["source_manifests"] == cert["source_manifests"]
            if label == "nf715":
                assert manifest["schema"] == cert["schema"] == (
                    "NF715-second-original-global-matrix-block-v1")
                assert (cert["row"],cert["column"],cert["first"],cert["end"]) == (
                    1,1,0,8)
                assert cert["actual_global_HD_gates"] == (
                    cert["actual_global_A_gates"]) == 8
                assert cert["attachment_manifest_sha256"] == digest
                assert cert["accepted_audits"] == manifest["accepted_audits"]
                assert len(manifest["files"]) == 2
            else:
                assert manifest["schema"] == (
                    "NF716-second-original-global-matrix-row-continuation-v1")
                assert cert["schema"] == (
                    "NF716-second-original-global-matrix-row-continuation-audit-v1")
                assert (cert["original_index"],cert["first"],cert["end"]) == (
                    1,8,32)
                assert cert["source_manifest_sha256"] == digest
                assert cert["new_HD_gates"] == cert["new_A_gates"] == 24
                assert manifest["blocks"] == [1,2,3]
                assert len(manifest["files"]) == 3
                assert [z["index"] for z in cert["gate_coordinates"]] == list(range(8,32))
                assert all(z["row"] == z["column"] == 1 for z in cert["gate_coordinates"])
                assert manifest["accepted_nf715_manifest_sha256"] == evidence["nf715"]["source_manifest_sha256"]
                assert manifest["accepted_nf715_audit_sha256"] == evidence["nf715"]["certificate_sha256"]
                assert manifest["accepted_source_audits"] == evidence["nf715"]["accepted_source_audits"]
            if label == "nf715":
                record["accepted_source_audits"] = cert["accepted_audits"]
                record["source_manifests"] = cert["source_manifests"]
            else:
                assert cert["source_manifests"] == evidence["nf715"]["source_manifests"]
                assert cert["accepted_source_audits"] == evidence["nf715"]["accepted_source_audits"]
                record["source_manifests"] = cert["source_manifests"]
                record["accepted_source_audits"] = cert["accepted_source_audits"]
        else:
            assert cert["schema"] == (
                f"NF{label[-3:]}-complete-parallel-original-global-row-one-audit-v1")
            assert (cert["index"],cert["first"],cert["end"]) == (1,lo,hi)
            assert cert["coordinates"] == list(range(lo,hi))
            assert cert["global_HD_gates"] == cert["global_A_gates"] == 64
            assert cert["lean_declarations"] == 64
            assert len(cert["shard_audit_sha256"]) == 2
            assert all(isinstance(x,str) and len(x)==64 for x in cert["shard_audit_sha256"])
            assert cert["source_manifests"] == evidence["nf715"]["source_manifests"]
            assert cert["accepted_source_audits"] == evidence["nf715"]["accepted_source_audits"]
            assert cert["accepted_nf715_audit_sha256"] == evidence["nf715"]["certificate_sha256"]
            record["source_manifests"] = cert["source_manifests"]
            record["accepted_source_audits"] = cert["accepted_source_audits"]
            record["shard_audit_sha256"] = cert["shard_audit_sha256"]
        evidence[label] = record

    all_coords = sorted(x for r in evidence.values() for x in r["coordinates"])
    assert len(all_coords) == len(set(all_coords)) == 160
    expected = list(range(0,32)) + list(range(64,192))
    assert all_coords == expected
    missing = [i for i in range(N) if i not in set(all_coords)]
    assert missing == list(range(32,64)) + list(range(192,242))
    assert sum(r["lean_theorem_declarations"] for r in evidence.values()) == 164
    theorem_sets = [set(r["theorem_names"]) for r in evidence.values()]
    assert len(set.union(*theorem_sets)) == 164
    assertion = {
        "schema": "NF721-source-specific-original-global-row-one-accepted-inventory-v1",
        "source": "Accepted source-specific Lean standard-axiom audit artifacts only",
        "original_index": 1,
        "authenticated_accepted_stages": list(evidence),
        "total_accepted_original_HD_row_one_gates": 160,
        "total_accepted_original_A_column_one_gates": 160,
        "total_accepted_gate_identities": 320,
        "accepted_lean_declarations": 164,
        "accepted_coordinates": all_coords,
        "pending_intervals": [
            {"first":a,"end":b,"required_final_audit":stage}
            for a,b,stage in PENDING
        ],
        "unproved_coordinates": missing,
        "full_row_one_certified": False,
        "source_manifests": evidence["nf715"]["source_manifests"],
        "accepted_local_source_audits": evidence["nf715"]["accepted_source_audits"],
        "stage_evidence": evidence,
        "scope": "Precisely 160 genuine original index-one HD and A coordinate pairs accepted. NF717 32 and NF720 50 pairs excluded. This is a source-bound audit inventory, not a new Lean proof of an all-coordinate theorem or any full-cache, payment, Weil-positivity or RH result."
    }
    return assertion


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--inputs", type=Path, default=Path("nf721-audits"))
    p.add_argument("--output", type=Path, default=Path("nf721-accepted-original-row-one-inventory.json"))
    a = p.parse_args()
    cert = analyze(a.inputs)
    a.output.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n")
    print("NF721 authenticated 160 original HD row-one and 160 A column-one global gates / 164 standard-axiom theorem declarations; exact 82-pair NF717/NF720 gap remains OPEN")


if __name__ == "__main__":
    main()
