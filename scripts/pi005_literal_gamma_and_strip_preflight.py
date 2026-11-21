#!/usr/bin/env python3
"""PI005 exact-rational domain/normalization preflight and optional source pins.

Not a Lean theorem, and not an independent verification of Masullo's trace
formula. The source-binding mode refuses missing/wrong Git blob inputs.
Usage:
  python scripts/pi005_literal_gamma_and_strip_preflight.py
  python scripts/pi005_literal_gamma_and_strip_preflight.py --source-files \
     PATH_TO_ZETA23_DEFS PATH_TO_ZETA23_EXPLICIT_FORMULA PATH_TO_ORIGINAL_IV011
"""
import argparse
import hashlib
from fractions import Fraction as Q
from pathlib import Path


SOURCE_SHA = (
    "8024700cbfefb54d763b487afa84c03fef58a550",
    "11119489556113fd419d7b6fb45ccbaa2e493e2a",
    "14d8f01ce34f764900eccc68399d7323b4f4a25c",
)
SOURCE_PATTERNS = (
    ("def paperFT", "Complex.exp (Complex.I * z * (u : ℂ))"),
    ("def gammaBracket", "Complex.digamma (1 / 4 + I * r / 2)", "Real.log π",
     "theorem paperFT_ofReal_eq_fourier"),
    ("def neutralIV011OriginalMixedArch", "Zeta23.paperFT k r",
     "Zeta23.EF.gammaBracket r", "def neutralIV011OriginalMixedPrime",
     "def neutralIV011OriginalMixedPole"),
)


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()


def verify_source_files(paths: list[str]) -> None:
    if len(paths) != 3:
        raise ValueError("source-binding mode requires all three source files")
    for path, expected_sha, fragments in zip(paths, SOURCE_SHA, SOURCE_PATTERNS):
        raw = Path(path).read_bytes()
        actual = git_blob_sha(raw)
        if actual != expected_sha:
            raise AssertionError(f"{path}: Git blob mismatch {actual} != {expected_sha}")
        source = raw.decode("utf-8")
        for needle in fragments:
            if needle not in source:
                raise AssertionError(f"{path}: missing literal source fragment {needle!r}")
    print("PI005 SOURCE-BINDING PREFLIGHT: three exact Git blobs verified")
    print("NOTE: this still does NOT prove the real-place Fourier identity in Lean")


def rational_sanity() -> None:
    half=Q(1,2)
    # In the specified a=1/2 spectral width, all interior 0<Re rho<1
    # give centered real parts in the open interval (-1/2, 1/2).
    for numerator in range(1,1000):
        beta=Q(numerator,1000)
        assert abs(beta-half) < half
    assert not abs(Q(0)-half) < half
    assert not abs(Q(1)-half) < half
    assert not abs(Q(1,4)-half) < Q(1,5)
    # These are sample checks of the simple rational inequality, NOT a
    # computational proof that all zeta zeros lie inside the critical strip.

    # Original PI003 support centers; a genuine n9 interaction can coexist
    # with a zero-at-origin correlation and Masullo's norm-one test gate.
    left, right, rad=-Q(1099,1000), Q(1099,1000), Q(1,2000)
    assert (left+rad) < (right-rad)
    assert (right-left)==Q(1099,500)

    # One signed negative real-place / positive real-place normalization:
    # same K(log 9) value for both directions, with coefficient 1/2.
    q=Q(9)
    k_plus=Q(3,2)*(1/(q-1)+1/(q+1))
    k_minus=Q(1,6)*(q/(q-1)+q/(q+1))
    kernel=Q(1,3)/(1-Q(1,81))
    assert k_plus==k_minus==kernel==Q(27,80)
    assert Q(2,5)-150*Q(1,500)==Q(1,10)
    print("PI005 rational convention/strip preflight: PASS")
    print("Masullo a=1/2: critical-strip points are included; boundary excluded")
    print("Real-place test kernel K(+/- log 9)=27/80")
    print("Literal source SHA verification: NOT RUN unless --source-files supplied")


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-files",nargs=3,metavar=("DEFS","EF","IV011"))
    args=parser.parse_args()
    rational_sanity()
    if args.source_files:
        verify_source_files(args.source_files)


if __name__=="__main__":
    main()
