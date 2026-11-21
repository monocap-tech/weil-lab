"""Fail-closed UOI governance regression suite. No network or Actions API."""
import copy
import json
import unittest
from pathlib import Path

from uoi_validate import ManifestError, plan, validate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = json.loads((ROOT / "research" / "unified" / "obligations.json").read_text(encoding="utf-8"))


class TestUOI(unittest.TestCase):
    def changed(self):
        return copy.deepcopy(SOURCE)

    def test_valid_13_node_readonly_graph(self):
        nodes = validate(SOURCE)
        self.assertEqual(len(nodes), 13)
        self.assertEqual(SOURCE["authority"]["operational_cursor"], "UOI-INTAKE")

    def test_two_review_ready_but_never_authorized(self):
        result = plan(SOURCE, validate(SOURCE))
        self.assertEqual({x["id"] for x in result["ready_for_review_only"]}, {"UOI-INTAKE", "CI-FANOUT"})
        self.assertEqual(len(result["blocked_by_unpaid_prerequisites"]), 11)
        self.assertIs(result["dispatch_authorized"], False)
        self.assertIs(result["mathematical_promotion_authorized"], False)
        self.assertIs(result["terminal_route_satisfied"], False)

    def test_heavy_remains_review_only_even_when_unblocked(self):
        d = self.changed()
        for o in d["obligations"]:
            if o["id"] == "NF-FRONTIER":
                o["depends_on"] = []
        result = plan(d, validate(d))
        self.assertFalse(result["dispatch_authorized"])
        self.assertTrue(any(x["id"] == "NF-FRONTIER" and
                            x["run_class"] == "heavy_manual"
                            for x in result["ready_for_review_only"]))

    def test_duplicate_id_rejected(self):
        d = self.changed()
        d["obligations"][1]["id"] = "UOI-INTAKE"
        with self.assertRaises(ManifestError):
            validate(d)

    def test_unknown_dependency_rejected(self):
        d = self.changed()
        d["obligations"][2]["depends_on"] = ["NOT-A-NODE"]
        with self.assertRaises(ManifestError):
            validate(d)

    def test_cycle_rejected(self):
        d = self.changed()
        d["obligations"][0]["depends_on"] = ["W-GLOBAL-FORM"]
        with self.assertRaises(ManifestError):
            validate(d)

    def test_unpaid_math_is_blocked(self):
        result = plan(SOURCE, validate(SOURCE))
        self.assertTrue(any(x["id"] == "W-GLOBAL-FORM"
                            for x in result["blocked_by_unpaid_prerequisites"]))

    def test_automatic_dispatch_rejected(self):
        d = self.changed()
        d["authority"]["automatic_dispatch"] = True
        with self.assertRaises(ManifestError):
            validate(d)

    def test_automatic_promotion_rejected(self):
        d = self.changed()
        d["authority"]["automatic_mathematical_promotion"] = True
        with self.assertRaises(ManifestError):
            validate(d)

    def test_hold_cannot_be_waived_by_manifest(self):
        d = self.changed()
        d["authority"]["execution_policy"] = "dispatch"
        with self.assertRaises(ManifestError):
            validate(d)

    def test_historical_odd_cursor_must_be_preserved(self):
        d = self.changed()
        d["authority"]["historical_manifest"] = "removed"
        with self.assertRaises(ManifestError):
            validate(d)

    def test_false_accepted_status_rejected(self):
        d = self.changed()
        d["obligations"][2]["standing"] = "accepted"
        with self.assertRaises(ManifestError):
            validate(d)

    def test_false_evidence_promotion_rejected(self):
        d = self.changed()
        d["obligations"][2]["evidence"][0]["accepts_obligation"] = True
        with self.assertRaises(ManifestError):
            validate(d)

    def test_partial_accepted_receipt_rejected(self):
        d = self.changed()
        d["obligations"][2]["standing"] = "accepted"
        d["obligations"][2]["closure_receipt"] = {
            "source_sha": "0" * 40,
            "artifact_sha256": "0" * 64,
            "independent_audit": "asserted",
        }
        with self.assertRaises(ManifestError):
            validate(d)

    def test_missing_terminal_route_rejected(self):
        d = self.changed()
        d["terminal_routes"] = d["terminal_routes"][:1]
        with self.assertRaises(ManifestError):
            validate(d)

    def test_bad_source_reference_rejected(self):
        d = self.changed()
        d["obligations"][0]["sources"][0] = "https://invalid.invalid/unknown"
        with self.assertRaises(ManifestError):
            validate(d)


if __name__ == "__main__":
    unittest.main()
