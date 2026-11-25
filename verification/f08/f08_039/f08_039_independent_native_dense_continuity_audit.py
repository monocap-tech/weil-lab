#!/usr/bin/env python3
"""F08-039 independent exact original IV023 native L2 dense-continuity conditional transfer custody.

This verifier deliberately fails closed until the original F08-038 producer
is genuinely kernel-PASS and its immutable ZIP digest is pinned.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

NAMES = {
    "f08_038_nativeL2_tendsto_of_dense_core",
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ORIGINAL_IV023 = "614ba879f7389fdb620c474adaee273b00eac71c"
ORIGINAL_DOMAIN_BLOB = "2bf19165fce3a0cfa6e4d782d68caab268aaf82b"
SOURCE_BLOB = "354922e7ed1727292f9ef41cf9b4f7d20f59a753"
PRODUCER_COMMIT = "a5342035b61dfb86a308404ecbb4e39c26f92187"
PRODUCER_RUN = 45546805418
ARTIFACT_ID = 14992491957
ARTIFACT_SHA256 = "9c3fda6d537d23c5c1e12fdf750ae5e34e39588f0927e0b64b1bacbd9883b2f2"
SOURCE_PATH = "WeilDefect/Generated/F08/NativeL2ContinuityDenseTransfer.lean"
BUILD_PATH = "f08-038-build.log"
AXIOMS_PATH = "f08-038-axioms.log"


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
        assert names and len(names) == len(set(names))
        assert z.testzip() is None
        assert all(not p.startswith("/") and ".." not in Path(p).parts for p in names)
        src = unique_file(z, SOURCE_PATH)
        build = unique_file(z, BUILD_PATH).decode()
        axioms = unique_file(z, AXIOMS_PATH).decode()
        predecessor27 = unique_file(z, "WeilDefect/Generated/F08/NativeFrequencyScalingMeasure.lean")
        predecessor29 = unique_file(z, "WeilDefect/Generated/F08/NativeL2PushforwardNorm.lean")
        predecessor30 = unique_file(z, "WeilDefect/Generated/F08/NativeFrequencyDilation.lean")
        predecessor33 = unique_file(z, "WeilDefect/Generated/F08/NativeFrequencyDilationIsometry.lean")
        predecessor35 = unique_file(z, "WeilDefect/Generated/F08/NativeDilationLinearIsometry.lean")
    assert git_blob(src) == SOURCE_BLOB, "wrong original Git source blob"
    # Validate all five original staged predecessor source blobs, not merely names.
    assert git_blob(predecessor27) == "eecfe2a849fa79aa13810ede85e9ba625eba7777"
    assert git_blob(predecessor29) == "4da65f9b9df7cae6ea30a4a7f25d3e6c1606c294"
    assert git_blob(predecessor30) == "5c260b69f464f5793e095f9b5448c90f7984617f"
    assert git_blob(predecessor33) == "8b4055c065ab7987a01bf55143908d8cd77f0f23"
    assert git_blob(predecessor35) == "7038c5d23cecdef6cc3f6bca1d12548246e65bd7"
    assert b"import WeilDefect.Generated.F08.NativeDilationLinearIsometry" in src
    assert b"f08_030_nativeFrequencyDilation" in src
    assert b"f08_035_nativeFrequencyDilation_approximation_bound" in src
    assert b"Dense s" in src
    assert b"Tendsto" in src
    assert b"Metric.tendsto_nhds" in src
    assert b"open scoped Topology" in src
    assert not re.search(rb"\b(sorry|admit|unsafe)\b", src)
    for name in NAMES:
        assert name.encode() in src, ("missing literal declaration", name)
    assert "Built WeilDefect.Generated.F08.NativeL2ContinuityDenseTransfer" in build
    assert not re.search(r"(^|\n)[^\n]*error:", build, re.I)
    found = read_axioms(axioms)
    return {
        "schema": "F08-039-independent-native-L2-dense-continuity-transfer-custody-v1",
        "pinned_original_research_commit": ORIGINAL_IV023,
        "pinned_original_canonical_domain_blob": ORIGINAL_DOMAIN_BLOB,
        "producer_head": PRODUCER_COMMIT,
        "producer_run": PRODUCER_RUN,
        "artifact_id": ARTIFACT_ID,
        "artifact_zip_sha256": ARTIFACT_SHA256,
        "candidate_source_blob": SOURCE_BLOB,
        "one_declaration_exact_axioms": {n: sorted(found[n]) for n in sorted(found)},
        "strict_ordinary_only_axioms": True,
        "conditional_dense_to_all_native_L2_continuity_accepted": True,
        "source_native_dense_convergence_premise_discharged": False,
        "L2_dilation_strong_continuity_proved": False,
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
        good.replace("f08_038_nativeL2_tendsto_of_dense_core", "wrong_decl"),
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
    assert ARTIFACT_ID == 14992491957 and ARTIFACT_SHA256 is not None
    print("F08-039 auditor selftest PASS 4/4 mutated reports rejected")


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
    print("F08-039 original ZIP/SHA/source/one named axiom independent PASS")


if __name__ == "__main__":
    main()
