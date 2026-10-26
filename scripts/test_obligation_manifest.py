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

    def test_historical_case_sensitive_command_paths_valid(self):
        # These four preexisting scripts genuinely exist on the
        # case-sensitive repository; none should be silently skipped.
        _, checks = gov.verify(self.base)
        by_id = {x["id"]:x for x in checks}
        names = (
            "SM36-original-numerical-feasibility-only",
            "SM38-original-leafwise-odd-fourier-diagnostic",
            "SM52C-original-two-source-L2-coercivity",
            "SM54-original-signed-pole-adaptive-disjoint-3source",
        )
        for name in names:
            self.assertIn(name, by_id)
            self.assertEqual(by_id[name]["argv"][0], "python3")

    def test_untrusted_bare_validation_filename_rejected(self):
        self.invalid(lambda d: d["active_checks"][0].update(
            argv=["python3","scripts/sm99_unapproved_executable.py"]))

    def test_case_sensitive_path_traversal_rejected(self):
        self.invalid(lambda d: d["active_checks"][0].update(
            argv=["python3","scripts/../scripts/sm36_original_odd_numerical_pilot.py"]))

    def test_unknown_replay_cadence_rejected(self):
        self.invalid(lambda d: d["active_checks"][0].update(cadence="infinite"))

    def test_unrecognized_role_rejected(self):
        # Historical evidence categories are preserved separately as
        # scope_role; the declared role is always one of the three
        # schema-recognized classifications, and invalid labels fail.
        self.invalid(lambda d: d["active_checks"][0].update(role="method-obstruction"))

    def test_scoped_historical_roles_preserve_limited_interpretation(self):
        scoped=[c for c in self.base["active_checks"] if "scope_role" in c]
        self.assertGreaterEqual(len(scoped), 30)
        self.assertTrue(all(c["role"]=="verification" and
                            isinstance(c["scope_role"],str) and
                            c["scope_role"] and c["interpretation"]
                            for c in scoped))

    def test_no_per_update_replay_rejected(self):
        self.invalid(lambda d: [c.update(cadence="on-demand") for c in d["active_checks"]])

    def test_missing_evidence_rejected(self):
        self.invalid(lambda d: d["obligations"][0]["evidence"].append("UNPROVED"))


if __name__ == "__main__":
    unittest.main()
