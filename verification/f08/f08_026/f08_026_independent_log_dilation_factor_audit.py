#!/usr/bin/env python3
"""F08-026: independent nonpromoting original F08-025 source/ZIP/axiom audit.

This deliberately cannot issue an acceptance receipt until the genuine
successful Lean producer ZIP ID and external SHA256 are pinned below.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

NAMES = {
    "f08_025_logDilationFactor_nonneg",
    "f08_025_logDilationFactor_one",
    "f08_025_logDilationFactor_sq_le",
    "f08_025_logDilationFactor_continuousAt_one",
    "f08_025_logDilationFactor_tendsto_one",
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ORIGINAL_IV023 = "614ba879f7389fdb620c474adaee273b00eac71c"
ORIGINAL_WEIGHT_BLOB = "ae932d4f3f7e4d6d06dbd778a5708927172238dc"
ORIGINAL_CANONICAL_BLOB = "2bf19165fce3a0cfa6e4d782d68caab268aaf82b"
DEPENDENCY_GIT_BLOB = "5dce3a647223afbf75ef09f72d90c8afb331ee81"
CANDIDATE_GIT_BLOB = "d208814f79f04a9926c2059d427419e73d6abb4b"
PRODUCER_HEAD = "4c53e94fcfb75c5da3f456580bee71e79019aac1"
PRODUCER_RUN = 45299562850
# Exact immutable successful original-source producer artifact:
ARTIFACT_ID = 14879135556
ARTIFACT_SHA256 = "60984424d6d914fe909887b4cbd07453fbe84ec7bcf1c5d5398367f32e07ab2c"

SOURCES = {
    "WeilDefect/Generated/F08/LogWeightDilation.lean": DEPENDENCY_GIT_BLOB,
    "WeilDefect/Generated/F08/NativeLogDilationFactor.lean": CANDIDATE_GIT_BLOB,
}
LOGS = ("f08-025-build.log", "f08-025-axioms.log")
BUILT_TARGET = "WeilDefect.Generated.F08.NativeLogDilationFactor"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(
        b"blob " + str(len(data)).encode() + b"\0" + data
    ).hexdigest()


def parse_axioms(raw):
    """Parse all named Lean outputs, including wrapped multiline axiom lists."""
    pattern = re.compile(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]"
        r"|'WeilDefect\.(\w+)' does not depend on any axioms",
        re.S,
    )
    found = {}
    for match in pattern.finditer(raw):
        name = match[1] or match[3]
        assert name not in found, ("duplicate axiom report", name)
        axioms = (
            {a.strip() for a in match[2].split(",") if a.strip()}
            if match[2] is not None else set()
        )
        found[name] = axioms
    remainder = pattern.sub("", raw)
    assert not remainder.strip(), ("unexpected compiler/axiom text", remainder)
    assert set(found) == NAMES, ("missing or extra named reports", found)
    assert all(axioms <= ALLOWED for axioms in found.values()), (
        "unsafe or nonstandard axiom", found
    )
    return found


def unique_archive_file(archive, suffix):
    hits = [
        p for p in archive.namelist()
        if p == suffix or p.endswith("/" + suffix)
    ]
    assert len(hits) == 1, ("missing/ambiguous path", suffix, hits)
    return archive.read(hits[0])


def verify(archive_path, producer_metadata):
    assert ARTIFACT_ID is not None and ARTIFACT_SHA256 is not None, (
        "NONPROMOTING: original producer ZIP ID/SHA have not been independently pinned"
    )
    meta = json.loads(Path(producer_metadata).read_text())
    assert meta == {
        "head_sha": PRODUCER_HEAD,
        "run_id": PRODUCER_RUN,
        "artifact_id": ARTIFACT_ID,
        "sha256": ARTIFACT_SHA256,
        "completed_success": True,
        "compiler_job_success": True,
    }, ("producer metadata mismatch", meta)
    raw = Path(archive_path).read_bytes()
    assert sha256(raw) == ARTIFACT_SHA256, "external original ZIP SHA mismatch"
    with zipfile.ZipFile(archive_path) as z:
        members = z.namelist()
        assert len(members) == len(set(members)) and members
        assert z.testzip() is None, "ZIP CRC failure"
        assert all(not p.startswith("/") and ".." not in Path(p).parts for p in members)
        for path, expected in SOURCES.items():
            source = unique_archive_file(z, path)
            assert git_blob(source) == expected, ("Git source blob mismatch", path)
            assert not re.search(rb"\b(sorry|admit|unsafe)\b", source), (
                "unsafe source text", path
            )
        source = unique_archive_file(
            z, "WeilDefect/Generated/F08/NativeLogDilationFactor.lean"
        )
        assert b"import WeilDefect.Generated.F08.LogWeightDilation" in source
        assert b"f08_logarithmicFourierWeight_dilation_uniform" in source
        for name in NAMES:
            assert name.encode() in source, ("missing target", name)
        build = unique_archive_file(z, LOGS[0]).decode("utf-8")
        axioms = unique_archive_file(z, LOGS[1]).decode("utf-8")
    assert "Built " + BUILT_TARGET in build, "no direct compiled source object"
    assert not re.search(r"(^|\n)[^\n]*error:", build, re.I), (
        "compiler errors in producer build"
    )
    found = parse_axioms(axioms)
    return {
        "schema": "F08-026-original-log-dilation-factor-independent-custody-v1",
        "original_source_commit": ORIGINAL_IV023,
        "original_log_weight_git_blob": ORIGINAL_WEIGHT_BLOB,
        "original_log_domain_git_blob": ORIGINAL_CANONICAL_BLOB,
        "candidate_head_sha": PRODUCER_HEAD,
        "producer_run": PRODUCER_RUN,
        "artifact_id": ARTIFACT_ID,
        "outer_zip_sha256": ARTIFACT_SHA256,
        "exact_candidate_git_blob": CANDIDATE_GIT_BLOB,
        "exact_dependency_git_blob": DEPENDENCY_GIT_BLOB,
        "real_compiler_build": True,
        "standard_axioms_only": True,
        "five_named_axioms": {k: sorted(v) for k, v in sorted(found.items())},
        "F08_025_scalar_dilation_factor_accepted": True,
        "F08_025_native_dilation_strong_continuity_proved": False,
        "F08_supported_form_core_dense_proved": False,
        "F08_signed_mixed_Weil_identity_proved": False,
        "F42_unrestricted_positive_proved": False,
        "RH_proved": False,
    }


def selftest():
    good = "\n".join(
        "'WeilDefect.%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
        % name for name in sorted(NAMES)
    )
    assert set(parse_axioms(good)) == NAMES
    mutations = [
        good.replace("propext", "sorryAx"),
        good.replace("f08_025_logDilationFactor_one", "wrong_name"),
        good + "\n" + good.splitlines()[0],
        good + "\nerror: unanticipated Lean compilation error",
    ]
    for bad in mutations:
        try:
            parse_axioms(bad)
        except AssertionError:
            pass
        else:
            raise AssertionError("unsafe mutation accepted")
    print("F08-026 selftest PASS: 4/4 adversarial axiom/log mutants rejected")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--archive", type=Path)
    p.add_argument("--producer-metadata", type=Path)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    if args.selftest:
        selftest()
        return
    assert args.archive and args.producer_metadata and args.out
    result = verify(args.archive, args.producer_metadata)
    args.out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("F08-026 genuine source/ZIP/5-axiom independent audit PASS")


if __name__ == "__main__":
    main()
