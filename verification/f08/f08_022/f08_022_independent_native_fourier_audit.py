#!/usr/bin/env python3
"""Independent source/ZIP/axiom custody for the six original source physical-to-native L2 Fourier a.e. lemmas.

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
    "f08_021_original_smoothed_window_native_ae",
    "f08_021_original_smoothed_window_native_integrable",
    "f08_021_original_smoothed_window_native_ae_support",
    "f08_021_original_smoothed_window_native_fourier_ae",
    "f08_021_original_smoothed_window_native_fourier_product_ae",
    "f08_021_explicit_original_smoothed_window_native_fourier_ae",
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ORIGINAL_SOURCE_BLOB = "60453bd214c43feedb0fa64d74a15bd452e48998"
ORIGINAL_LOG_WEIGHT_SOURCE_BLOB = "2bf19165fce3a0cfa6e4d782d68caab268aaf82b"
CANDIDATE_SOURCE_BLOB = "f7f769dd120810645a6bed9fa3ef379c94986a77"
PRODUCER_SHA = "6fc58b60ee13bcabd7b1faa64b40f0d3e0a39fec"
PRODUCER_RUN = 45281337186
ARTIFACT_ID = 14869304303
ARTIFACT_SHA = "f4a63af8914b593cebd81fa95032235049a004927d7d5fe36ad4998fced460b0"
SOURCE_PATH = "WeilDefect/Generated/F08/OriginalSmoothedWindowNativeFourier.lean"

def sha256(b): return hashlib.sha256(b).hexdigest()

def git_blob(b):
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def read_axioms(raw):
    """Strictly parse Lean's single- or multiline pretty-printed named axioms."""
    found = {}
    pattern = re.compile(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]"
        r"|'WeilDefect\.(\w+)' does not depend on any axioms", re.S)
    for match in pattern.finditer(raw):
        name = match[1] or match[3]
        assert name not in found, ("duplicate", name)
        found[name] = (
            {x.strip() for x in match[2].split(",") if x.strip()}
            if match[2] is not None else set())
    remainder = pattern.sub("", raw)
    assert not remainder.strip(), ("unexpected output", remainder)
    assert set(found) == NAMES, ("unexpected names", found)
    assert all(values <= ALLOWED for values in found.values()), ("unsafe axioms", found)
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
        deps = {
            "WeilDefect/Generated/F08/OriginalWeightedMollifierMultiplier.lean": "2a8199ff817f59d1437fa173518a588cbbd467b9",
            "WeilDefect/Generated/F08/OriginalWindowMollifierFourier.lean": "606d324ca9fcfd53d059efe1b57d1b0e30349476",
            "WeilDefect/Generated/F08/OriginalWindowConvolutionSupport.lean": "6badab7f17605d3131ee414282683d390c6f1964",
            "WeilDefect/Generated/F08/OriginalNormalizedMollifier.lean": "b1f53459762df682f6d1d358aae9c82b5396c5a7",
            "WeilDefect/Generated/F08/OriginalMollifierFourierLimit.lean": "7b91eda87ce5a0d7691fdc643865e72fb153287c",
            "WeilDefect/Generated/F08/ActualMollifierWeightedDCT.lean": "f1969dede41f0d799788411420c0cb2a63c5e53a",
            "WeilDefect/Generated/F08/ExplicitShrinkingPhysicalMollifier.lean": "b767da47b302734c9b1de0bd0fde38b727c84b20",
            "WeilDefect/Generated/F08/OriginalSmoothedWindow.lean": "efe3260cbd8798ad7192142c1e656f31a6729d13",
        }
        for path, blob in deps.items():
            data = unique_suffix(z, path)
            assert git_blob(data) == blob, ("original physical/Fourier dependency mismatch", path)
        build = unique_suffix(z, "f08-021-build.log").decode()
        axioms = unique_suffix(z, "f08-021-axioms.log").decode()
    assert git_blob(src) == CANDIDATE_SOURCE_BLOB, "source not equal to exact producer PR source"
    assert b"import WeilDefect.Generated.F08.OriginalSmoothedWindow" in src
    assert b"f08_021_originalSmoothedWindowL2" in src
    assert b"neutralIntegrableL2_fourier_ae" in src
    for name in NAMES:
        assert name.encode() in src, ("declaration absent", name)
    assert b"sorry" not in src and b"admit" not in src and b"unsafe" not in src
    assert "Built WeilDefect.Generated.F08.OriginalSmoothedWindowNativeFourier" in build
    assert not re.search(r"(^|\n).*?error:", build, re.I), "compiler errors"
    results = read_axioms(axioms)
    return {
        "schema": "F08-022-original-native-L2-physical-Fourier-coordinate-independent-receipt-v1",
        "actual_producer_run": PRODUCER_RUN,
        "actual_producer_source_commit": PRODUCER_SHA,
        "source_original_math_blob_git_sha1": ORIGINAL_SOURCE_BLOB,
        "source_original_logarithmic_weight_git_sha1": ORIGINAL_LOG_WEIGHT_SOURCE_BLOB,
        "actual_additive_lean_source_git_sha1": CANDIDATE_SOURCE_BLOB,
        "actual_producer_artifact_id": ARTIFACT_ID,
        "external_zip_sha256": ARTIFACT_SHA,
        "real_lean_built": True,
        "exact_named_axioms": {name: sorted(results[name]) for name in sorted(results)},
        "strict_standard_only_axioms": True,
        "native_real_complex_L2_fourier_bridge_lemmas_custodied": 6,
        "actual_original_physical_to_native_fourier_coordinate_ae": True,
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
        good.replace("f08_021_explicit_original_smoothed_window_native_fourier_ae", "wrongLemma"),
        good + "\n" + good.splitlines()[0],
        good + "\nerror: compiler failed",
    ]
    for mutant in bad:
        try: read_axioms(mutant)
        except AssertionError: pass
        else: raise AssertionError("unsafe mutation accepted")
    print("F08-022 original-native Fourier bridge audit selftest PASS 4/4 adversarial mutations rejected")

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
    print("F08-022 independent original native Fourier coordinate ZIP/source/axiom audit PASS, no F08 density or RH")

if __name__ == "__main__":
    main()
