#!/usr/bin/env python3
"""Independent source/ZIP/axiom custody for the two actual F08-005 Lean lemmas.

This source-only verifier does not prove density, the original form identity,
positive operators or RH. It accepts only the original compiler evidence.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

NAMES = {
    "f08_005_log_multiplier_error_pointwise",
    "f08_005_log_multiplier_error_integrable",
    "f08_005_log_multiplier_error_tendsto_zero",
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ORIGINAL_SOURCE_BLOB = "2bf19165fce3a0cfa6e4d782d68caab268aaf82b"
CANDIDATE_SOURCE_BLOB = "2a8199ff817f59d1437fa173518a588cbbd467b9"
PRODUCER_SHA = "4391c564089ff82b1bc6aead906c54acb4eb1b1f"
PRODUCER_RUN = 45220909373
ARTIFACT_ID = 14841811812
ARTIFACT_SHA = "984c3302fc7da41ebfc34fac824ba6054ca22549bc3ff804511c9b44b62482e8"
SOURCE_PATH = "WeilDefect/Generated/F08/WeightedMollifierMultiplier.lean"

def sha256(b): return hashlib.sha256(b).hexdigest()

def git_blob(b):
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def read_axioms(raw):
    found = {}
    for line in raw.splitlines():
        line = line.strip()
        m = re.fullmatch(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", line)
        if m:
            assert m[1] not in found, ("duplicate", m[1])
            found[m[1]] = {x.strip() for x in m[2].split(",") if x.strip()}
            continue
        m = re.fullmatch(r"'WeilDefect\.(\w+)' does not depend on any axioms", line)
        if m:
            assert m[1] not in found, ("duplicate", m[1])
            found[m[1]] = set()
            continue
        assert not line, ("unexpected output", line)
    assert set(found) == NAMES, ("unexpected names", found)
    assert all(s <= ALLOWED for s in found.values()), ("unsafe axioms", found)
    return found

def unique_suffix(z, suffix):
    matches = [x for x in z.namelist() if x == suffix or x.endswith("/" + suffix)]
    assert len(matches) == 1, ("missing / ambiguous artifact path", suffix, matches)
    return z.read(matches[0])

def verify(archive):
    data = Path(archive).read_bytes()
    assert sha256(data) == ARTIFACT_SHA, "ZIP outer digest mismatch"
    with zipfile.ZipFile(archive) as z:
        members = z.namelist()
        assert members and len(members) == len(set(members))
        assert z.testzip() is None
        assert all(not x.startswith("/") and ".." not in Path(x).parts for x in members)
        src = unique_suffix(z, SOURCE_PATH)
        build = unique_suffix(z, "f08-005-build.log").decode()
        axioms = unique_suffix(z, "f08-005-axioms.log").decode()
    assert git_blob(src) == CANDIDATE_SOURCE_BLOB, "source not equal to exact producer PR source"
    assert b"import WeilDefect.Morphology.NeutralCanonicalFormDomain" in src
    assert b"import Mathlib.MeasureTheory.Integral.DominatedConvergence" in src
    assert b"f08_005_log_multiplier_error_pointwise" in src
    assert b"f08_005_log_multiplier_error_integrable" in src
    assert b"f08_005_log_multiplier_error_tendsto_zero" in src
    assert b"sorry" not in src and b"admit" not in src and b"unsafe" not in src
    assert "Built WeilDefect.Generated.F08.WeightedMollifierMultiplier" in build
    assert not re.search(r"(^|\n).*?error:", build, re.I), "compiler errors"
    results = read_axioms(axioms)
    return {
        "schema": "F08-006-original-log-weight-independent-receipt-v1",
        "actual_producer_run": PRODUCER_RUN,
        "actual_producer_source_commit": PRODUCER_SHA,
        "source_original_math_blob_git_sha1": ORIGINAL_SOURCE_BLOB,
        "actual_additive_lean_source_git_sha1": CANDIDATE_SOURCE_BLOB,
        "actual_producer_artifact_id": ARTIFACT_ID,
        "external_zip_sha256": ARTIFACT_SHA,
        "real_lean_built": True,
        "exact_named_axioms": {name: sorted(results[name]) for name in sorted(results)},
        "strict_standard_only_axioms": True,
        "weighted_multiplier_error_lemmas_custodied": 3,
        "actual_physical_mollifier_fourier_identity_proved": False,
        "F08_supported_smooth_core_density_proved": False,
        "F08_original_source_to_native_form_proved": False,
        "F41_original_full_matrix_proved": False,
        "F42_original_global_Weil_positivity_proved": False,
        "RH_proved": False,
    }

def selftest():
    good = "\n".join(
        "'WeilDefect.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % n
        for n in sorted(NAMES))
    assert set(read_axioms(good)) == NAMES
    bad = [
        good.replace("propext", "sorryAx"),
        good.replace("f08_005_log_multiplier_error_integrable", "wrongLemma"),
        good + "\n" + good.splitlines()[0],
        good + "\nerror: compiler failed",
    ]
    for mutant in bad:
        try: read_axioms(mutant)
        except AssertionError: pass
        else: raise AssertionError("unsafe mutation accepted")
    print("F08-006 source-only independent audit selftest PASS 4/4 mutations refused")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--archive", type=Path)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    if args.selftest:
        selftest()
        return
    assert args.archive and args.out
    result = verify(args.archive)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("F08-006 independent original scalar log-weight ZIP/source/axiom audit PASS, no F08 density or RH")

if __name__ == "__main__":
    main()
