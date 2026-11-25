#!/usr/bin/env python3
"""F08-071 independent exact original IV023 native supported-smoothing custody.

This verifier deliberately fails closed until the original F08-068 producer
is genuinely kernel-PASS and its immutable ZIP digest is pinned.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

NAMES = {"f08_068_supportedWindow_eq", "f08_068_smoothedDomain_mem", "f08_068_weightedSmoothing_tendsto"}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ORIGINAL_IV023 = "614ba879f7389fdb620c474adaee273b00eac71c"
ORIGINAL_DOMAIN_BLOB = "2bf19165fce3a0cfa6e4d782d68caab268aaf82b"
SOURCE_BLOB = "c30f57a1d581c9a8be44ecd9dfccd5ea2e9f6e43"
PRODUCER_COMMIT = "de2838bb5d970cfe2b4dacfbee43a6b26bfd1c2f"
PRODUCER_RUN = 45619047774
ARTIFACT_ID = 15024761732
ARTIFACT_SHA256 = "f388255329c74d5af7c86f6df9df3aa7d1a9c6703eda4fecf3c6eb64fe5624dc"
SOURCE_PATH = "WeilDefect/Generated/F08/OriginalSupportedSmoothingReceiver.lean"
BUILD_PATH = "f08-068-build.log"
AXIOMS_PATH = "f08-068-axioms.log"


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def git_blob(b):
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def read_axioms(log):
    pattern = re.compile(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]"
        r"|'WeilDefect\.(\w+)' does not depend on any axioms", re.S
    )
    found = {}
    for m in pattern.finditer(log):
        name = m[1] or m[3]
        assert name not in found, ("duplicate theorem report", name)
        found[name] = ({x.strip() for x in m[2].split(",") if x.strip()}
                       if m[2] is not None else set())
    assert not pattern.sub("", log).strip(), "unexpected original axiom log content"
    assert set(found) == NAMES, ("missing or additional theorem reports", found)
    assert all(ax <= ALLOWED for ax in found.values()), ("nonstandard axiom", found)
    return found


def unique_file(z, suffix):
    hits = [name for name in z.namelist()
            if name == suffix or name.endswith("/" + suffix)]
    assert len(hits) == 1, ("missing or ambiguous ZIP entry", suffix, hits)
    return z.read(hits[0])


def verify(archive, metadata):
    assert ARTIFACT_ID is not None and ARTIFACT_SHA256 is not None, (
        "NO ACCEPTANCE: true original producer artifact ID and digest not pinned")
    d = json.loads(Path(metadata).read_text())
    assert d == {
        "producer_commit": PRODUCER_COMMIT, "producer_run": PRODUCER_RUN,
        "artifact_id": ARTIFACT_ID, "sha256": ARTIFACT_SHA256,
        "producer_success": True, "direct_compiler_and_axioms_success": True
    }, ("untrusted producer metadata", d)
    raw = Path(archive).read_bytes()
    assert sha256(raw) == ARTIFACT_SHA256, "mismatched complete original ZIP"
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        assert len(names) == 18 and len(names) == len(set(names))
        assert z.testzip() is None
        assert all(not p.startswith("/") and ".." not in Path(p).parts for p in names)
        src = unique_file(z, SOURCE_PATH)
        for name, blob in {
            'OriginalWeightedMollifierMultiplier.lean': '2a8199ff817f59d1437fa173518a588cbbd467b9',
            'OriginalWindowMollifierFourier.lean': '606d324ca9fcfd53d059efe1b57d1b0e30349476',
            'OriginalWindowConvolutionSupport.lean': '6badab7f17605d3131ee414282683d390c6f1964',
            'OriginalNormalizedMollifier.lean': 'b1f53459762df682f6d1d358aae9c82b5396c5a7',
            'OriginalMollifierFourierLimit.lean': '7b91eda87ce5a0d7691fdc643865e72fb153287c',
            'ActualMollifierWeightedDCT.lean': 'f1969dede41f0d799788411420c0cb2a63c5e53a',
            'ExplicitShrinkingPhysicalMollifier.lean': 'b767da47b302734c9b1de0bd0fde38b727c84b20',
            'OriginalSmoothedWindow.lean': 'efe3260cbd8798ad7192142c1e656f31a6729d13',
            'OriginalSmoothedWindowNativeFourier.lean': 'f7f769dd120810645a6bed9fa3ef379c94986a77',
            'NativeFrequencyScalingMeasure.lean': 'eecfe2a849fa79aa13810ede85e9ba625eba7777',
            'NativeL2PushforwardNorm.lean': '4da65f9b9df7cae6ea30a4a7f25d3e6c1606c294',
            'NativeFrequencyDilation.lean': '5c260b69f464f5793e095f9b5448c90f7984617f',
            'OriginalNativeL2SquareIntegral.lean': '16a7053b3a1ea6f0e0f91a89de6e40a91987cd92',
            'OriginalFormDomainEnergyReceiver.lean': '9423bc10b0db9d07078299bdedbe60b585fede7d',
            'OriginalWindowNativeWeightedSmoothing.lean': 'b0712d54ff2c5a3c3c5496f5c007559abf946bf3',
        }.items():
            assert git_blob(unique_file(z, 'WeilDefect/Generated/F08/' + name)) == blob
        build = unique_file(z, BUILD_PATH).decode()
        axioms = unique_file(z, AXIOMS_PATH).decode()
    assert git_blob(src) == SOURCE_BLOB, "wrong original Git source blob"
    assert not re.search(rb"\b(sorry|admit|unsafe)\b", src)
    for name in NAMES:
        assert name.encode() in src, ("missing literal declaration", name)
    assert "Built WeilDefect.Generated.F08.OriginalSupportedSmoothingReceiver" in build
    assert "Build completed successfully (9047 jobs)." in build
    assert not re.search(r"(^|\n)[^\n]*error:", build, re.I)
    found = read_axioms(axioms)
    return {
        "schema": "F08-071-independent-supported-smoothing-custody-v1",
        "pinned_original_research_commit": ORIGINAL_IV023,
        "pinned_original_canonical_domain_blob": ORIGINAL_DOMAIN_BLOB,
        "producer_head": PRODUCER_COMMIT,
        "producer_run": PRODUCER_RUN,
        "artifact_id": ARTIFACT_ID,
        "artifact_zip_sha256": ARTIFACT_SHA256,
        "candidate_source_blob": SOURCE_BLOB,
        "named_declarations_exact_axioms": {n: sorted(found[n]) for n in sorted(found)},
        "strict_ordinary_only_axioms": True,
        "verified_producer_gate": "F08-068",
        "weighted_coordinate_receiver_verified": False,
        "supported_weighted_smoothing_verified": True,
        "source_Weil_mixed_form_identity_proved": False,
        "fixed_support_log_form_core_proved": False,
        "F42_positive_proved": False,
        "RH_proved": False,
    }


def selftest():
    good = "\n".join(
        "'WeilDefect.%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
        % n for n in sorted(NAMES)
    )
    assert set(read_axioms(good)) == NAMES
    mutants = [
        good.replace("propext", "sorryAx"),
        good.replace("f08_068_supportedWindow_eq", "wrong_decl"),
        good + "\n" + good.splitlines()[0],
        good + "\nerror: kernel failed",
    ]
    for mutant in mutants:
        try:
            read_axioms(mutant)
        except AssertionError:
            pass
        else:
            raise AssertionError("invalid evidence accepted")
    assert ARTIFACT_ID == 15024761732 and ARTIFACT_SHA256 is not None
    print("F08-071 auditor selftest PASS 4/4 mutated reports rejected")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--archive", type=Path)
    ap.add_argument("--producer-metadata", type=Path)
    ap.add_argument("--out", type=Path)
    ns = ap.parse_args()
    if ns.selftest:
        selftest()
        return
    assert ns.archive is not None and ns.producer_metadata is not None and ns.out is not None
    receipt = verify(ns.archive, ns.producer_metadata)
    ns.out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("F08-071 original ZIP/SHA/source/3 named axioms independent PASS")


if __name__ == "__main__":
    main()
