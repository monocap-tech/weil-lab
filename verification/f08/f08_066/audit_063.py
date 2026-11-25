#!/usr/bin/env python3
"""F08-066 independent exact original IV023 native weighted-coordinate custody.

This verifier deliberately fails closed until the original F08-063 producer
is genuinely kernel-PASS and its immutable ZIP digest is pinned.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

NAMES = {"f08_063_logCorrection_mul_sqrt", "f08_063_weightedCoordinate_ae", "f08_063_correctedNative_memLp"}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ORIGINAL_IV023 = "614ba879f7389fdb620c474adaee273b00eac71c"
ORIGINAL_DOMAIN_BLOB = "2bf19165fce3a0cfa6e4d782d68caab268aaf82b"
SOURCE_BLOB = "34caef0d68578ac7c3fc15b5f839e148ad0e0a00"
PRODUCER_COMMIT = "ff13379a6850453e707bde8c82693a39e416a71a"
PRODUCER_RUN = 45579504322
ARTIFACT_ID = 15006916503
ARTIFACT_SHA256 = "cb06029380ab6908ccc618ce7290fd3ae6868bc03dcb396858e735e52b46b4a5"
SOURCE_PATH = "WeilDefect/Generated/F08/OriginalWeightedCoordinateIdentity.lean"
BUILD_PATH = "f08-063-build.log"
AXIOMS_PATH = "f08-063-axioms.log"


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
        assert len(names) == 9 and len(names) == len(set(names))
        assert z.testzip() is None
        assert all(not p.startswith("/") and ".." not in Path(p).parts for p in names)
        src = unique_file(z, SOURCE_PATH)
        for name, blob in {
            'LogWeightDilation.lean': '5dce3a647223afbf75ef09f72d90c8afb331ee81',
            'NativeLogDilationFactor.lean': 'd208814f79f04a9926c2059d427419e73d6abb4b',
            'NativeFrequencyScalingMeasure.lean': 'eecfe2a849fa79aa13810ede85e9ba625eba7777',
            'NativeL2PushforwardNorm.lean': '4da65f9b9df7cae6ea30a4a7f25d3e6c1606c294',
            'NativeFrequencyDilation.lean': '5c260b69f464f5793e095f9b5448c90f7984617f',
            'LogDilationFixedVectorCorrection.lean': 'd1c2d9241f58541e23b1975aec610c63eb84b92f',
        }.items():
            assert git_blob(unique_file(z, 'WeilDefect/Generated/F08/' + name)) == blob
        build = unique_file(z, BUILD_PATH).decode()
        axioms = unique_file(z, AXIOMS_PATH).decode()
    assert git_blob(src) == SOURCE_BLOB, "wrong original Git source blob"
    assert not re.search(rb"\b(sorry|admit|unsafe)\b", src)
    for name in NAMES:
        assert name.encode() in src, ("missing literal declaration", name)
    assert "Built WeilDefect.Generated.F08.OriginalWeightedCoordinateIdentity" in build
    assert "Build completed successfully (8995 jobs)." in build
    assert not re.search(r"(^|\n)[^\n]*error:", build, re.I)
    found = read_axioms(axioms)
    return {
        "schema": "F08-066-independent-weighted-coordinate-custody-v1",
        "pinned_original_research_commit": ORIGINAL_IV023,
        "pinned_original_canonical_domain_blob": ORIGINAL_DOMAIN_BLOB,
        "producer_head": PRODUCER_COMMIT,
        "producer_run": PRODUCER_RUN,
        "artifact_id": ARTIFACT_ID,
        "artifact_zip_sha256": ARTIFACT_SHA256,
        "candidate_source_blob": SOURCE_BLOB,
        "named_declarations_exact_axioms": {n: sorted(found[n]) for n in sorted(found)},
        "strict_ordinary_only_axioms": True,
        "verified_producer_gate": "F08-063",
        "weighted_coordinate_receiver_verified": True,
        "weighted_physical_carrier_identity_proved": False,
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
        good.replace("f08_063_logCorrection_mul_sqrt", "wrong_decl"),
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
    assert ARTIFACT_ID == 15006916503 and ARTIFACT_SHA256 is not None
    print("F08-066 auditor selftest PASS 4/4 mutated reports rejected")


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
    print("F08-066 original ZIP/SHA/source/3 named axioms independent PASS")


if __name__ == "__main__":
    main()
