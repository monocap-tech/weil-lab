"""Unit regressions for fail-closed obligation selection and replay custody."""
import copy
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("obligation_governance", ROOT / "scripts" / "verify_obligation_manifest.py")
gov = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gov)


class ManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "research" / "obligations.json").read_text())

    def invalid(self, modify):
        data = copy.deepcopy(self.base)
        modify(data)
        with self.assertRaises(gov.GovernanceError):
            gov.verify(data)

    def test_valid(self):
        obj, checks = gov.verify(self.base)
        self.assertEqual(obj["id"], "W-ODD-NEG")
        self.assertGreaterEqual(len(checks), 1)

    def test_closed_frontier_rejected(self):
        self.invalid(lambda d: d.update(active_obligation="W-ODD-POLE"))

    def test_missing_dependency_rejected(self):
        self.invalid(lambda d: d["obligations"][1]["depends_on"].append("MISSING"))

    def test_dependency_cycle_rejected(self):
        def mutate(d):
            d["obligations"][0]["depends_on"].append("W-ODD-NEG")
        self.invalid(mutate)

    def test_unfinished_dependency_rejected(self):
        def mutate(d):
            d["obligations"][0]["status"] = "open"
            d["obligations"][0]["priority"] = 99
        self.invalid(mutate)

    def test_invalid_command_rejected(self):
        self.invalid(lambda d: d["active_checks"][0].update(argv=["bash", "-c", "true"]))

    def test_unknown_replay_cadence_rejected(self):
        self.invalid(lambda d: d["active_checks"][0].update(cadence="infinite"))

    def test_no_per_update_replay_rejected(self):
        self.invalid(lambda d: [c.update(cadence="on-demand") for c in d["active_checks"]])

    def test_missing_evidence_rejected(self):
        self.invalid(lambda d: d["obligations"][0]["evidence"].append("UNPROVED"))


if __name__ == "__main__":
    unittest.main()
