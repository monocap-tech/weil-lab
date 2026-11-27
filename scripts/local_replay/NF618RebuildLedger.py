#!/usr/bin/env python3
"""Reconstruct the NF618 cumulative ledger for custody analysis only.

The output is never admitted unless its SHA-256 equals the original receipt.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROVISIONAL = ROOT / "notes/provisional"
EXPECTED_PARENT = "6a396e811890b8d1df7d9fc23855a34cf0ec465a3092b795b2647ca9b949adfd"
EXPECTED_ORIGINAL = "40e54496bec49119e252079345147a97ec25db8bb54a640647dc9c9d2b8fd24d"
EXPECTED_CALIBRATION = "6a396e811890b8d1df7d9fc23855a34cf0ec465a3092b795b2647ca9b949adfd"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def advance(parent, report):
    ledger = json.loads(parent)
    slots = ledger["slots"]
    assert len(slots) == 7835 and all(item["index"] == i for i, item in enumerate(slots))
    assert len({item["batch"] for item in report}) == len(report)
    for item in report:
        number = item["batch"]
        label = f"batch{number:02}"
        assert item["native_acceptance"] == "PASS" and item["checkpoint_gate"] == "PASS"
        assert len(item["slots"]) == item["tables"] == len(set(item["slots"]))
        assert sum(slots[index]["rows"] for index in item["slots"]) == item["rows"]
        for stem in ("source", "evidence", "checkpoint"):
            ledger["archives"][f"nf618-{label}-{stem}"] = item[f"{stem}_sha256"]
        ledger["groups"].append({
            "group": label,
            "run": item["producer_run"],
            "tables": item["tables"],
            "rows": item["rows"],
            "audit_targets": item["audit_targets"],
            "manifest_sha256": item["manifest_sha256"],
            "evidence_sha256": item["evidence_sha256"],
        })
        for index in item["slots"]:
            slot = slots[index]
            assert slot["certified_group"] is None and slot["scheduled_batch"] == number
            slot["certified_group"] = label
        ledger["certified_tables"] += item["tables"]
        ledger["certified_rows"] += item["rows"]
        ledger["residual_tables"] -= item["tables"]
        ledger["residual_rows"] -= item["rows"]
    assert ledger["certified_tables"] + ledger["residual_tables"] == 7835
    assert ledger["certified_rows"] + ledger["residual_rows"] == 37994
    return (json.dumps(ledger, indent=2) + "\n").encode()


def main():
    historical = (PROVISIONAL / "NF618CertifiedSlotLedgerBatch16.json").read_bytes()
    previous = (PROVISIONAL / "NF618CertifiedSlotLedgerBatch20.json").read_bytes()
    report1720 = json.loads((PROVISIONAL / "NF618Batch17-20Admission.json").read_bytes())
    report2124 = json.loads((PROVISIONAL / "NF618Batch21-24Admission.json").read_bytes())
    calibrated = advance(historical, report1720)
    assert calibrated == previous and sha(calibrated) == EXPECTED_CALIBRATION
    assert sha(previous) == EXPECTED_PARENT
    candidate = advance(previous, report2124)
    path = PROVISIONAL / "NF618CertifiedSlotLedgerBatch24.unadmitted.json"
    path.write_bytes(candidate)
    digest = sha(candidate)
    result = {"calibration": "PASS (Batch16 -> Batch20 byte-identical)",
              "candidate_bytes": len(candidate), "candidate_sha256": digest,
              "expected_original_sha256": EXPECTED_ORIGINAL,
              "admission": "PASS" if digest == EXPECTED_ORIGINAL else "REJECTED: original SHA-256 mismatch"}
    print(json.dumps(result, indent=2))
    if digest == EXPECTED_ORIGINAL:
        sys.exit(0)
    sys.exit(2)


if __name__ == "__main__":
    main()
