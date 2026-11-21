#!/usr/bin/env python3
"""CP006 pinned external Zeta SOURCE blob and theorem-name validation only.

A matching SHA1 git blob verifies source bytes, NOT a compiled Lean proof,
certified zero-to-row correspondence, or arithmetic/spectral equivalence.
"""
import argparse
import hashlib
import json
from pathlib import Path

LOCK = Path(__file__).with_name("cp006_upstream_zeta_source_lock.json")


def gitblob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_lock():
    obj = json.loads(LOCK.read_text(encoding="utf-8"))
    assert obj["repo"] == "smmercuri/zeta"
    assert obj["tag"] == "v1-1e6"
    assert obj["commit"] == "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
    assert obj["upstream_lean"] == "leanprover/lean4:v4.35.0"
    assert obj["original_weil_lab_lean"] == "leanprover/lean4:v4.34.0"
    assert len(obj["files"]) == 7
    assert obj["expected"]["certified_intervals_count"] == 1748002
    assert obj["expected"]["last_interval_right_rational"] == "1000449286/1000"
    return obj


def audit(directory, lock):
    contents = {}
    for path, expected in lock["files"].items():
        raw = (directory / path).read_bytes()
        actual = gitblob(raw)
        if actual != expected:
            raise ValueError(f"source git blob mismatch for {path}: {actual} != {expected}")
        contents[path] = raw.decode("utf-8")
    anchors = {
        "lean-toolchain": ["leanprover/lean4:v4.35.0"],
        "lakefile.toml": ['rev = "v4.35.0"', 'name = "Zeta"'],
        "Zeta/Main.lean": ["theorem riemannHypothesisUpTo_1000449",
                           "theorem simpleZerosUpTo_1000449",
                           "#print axioms Zeta.riemannHypothesisUpTo_1000449"],
        "Zeta/Zeros/Certificates.lean": [
            "def certifiedZeroIntervals : CertifiedZeroIntervals",
            "certifiedZeroIntervals.intervals.length = 1748002",
            "some (Enclosure.sfrac false 1000449286 1000)"],
        "Zeta/Zeros/CountCertificates.lean": [
            "def certifiedZeroCount : CertifiedZeroCount",
            "count := by rw [certifiedZeroIntervals_length]",
            "below := by"],
        "Zeta/Zeros/Count.lean": [
            "structure CertifiedZeroCount extends CertifiedGramBlockSeq, CertifiedZeroIntervals",
            "count : toCertifiedGramBlockSeq.minIdx + 1 = intervals.length"],
        "Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean": [
            "theorem riemannZeta.N_gramPoint_eq",
            "riemannZeta.N (gramPoint Z.minIdx) = Z.intervals.length"]
    }
    for path, texts in anchors.items():
        for s in texts:
            if s not in contents[path]:
                raise ValueError(f"source anchor missing {path}: {s}")
    return len(contents)


def selftest():
    obj = load_lock()
    assert gitblob(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a"
    assert len(obj["files"]) == 7
    print("CP006 source-lock metadata SHA and immutable commit: PASS")
    print("No external Lean kernel build or root data imported in this self-test")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--source-dir",type=Path)
    opts = p.parse_args()
    if opts.self_test:
        selftest()
    if opts.source_dir is not None:
        try:
            n=audit(opts.source_dir,load_lock())
        except (OSError, KeyError, AssertionError, ValueError, UnicodeError) as exc:
            print("NOT_READY:",exc)
            raise SystemExit(2)
        print(f"SOURCE_BLOBS_MATCHED_NOT_KERNEL: {n} files; exact pinned declarations found")
    if not opts.self_test and opts.source_dir is None:
        p.print_help()


if __name__ == "__main__":
    main()
