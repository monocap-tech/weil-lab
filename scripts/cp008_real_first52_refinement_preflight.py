#!/usr/bin/env python3
"""CP008 exact first-52 ORIGINAL-source refinement compatibility preflight.

Proposed five-decimal Euler-Maclaurin brackets are numerical CANDIDATES.
Mathematical inclusion, ordering, and CP006 weighted localization error are
checked with Python Fraction. Numeric Hardy Z screening is OPTIONAL mpmath,
NOT rigorous sign verification. The genuine source Zeta v4.35 `build_batch`
must subsequently compile AND pass a strict actual standard-axiom audit.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

from cp006_dyadic_zero_bracket_budget import dyadic_band, localization
from cp005_formal_zero_roster_adapter import E_tail, E_QUAD_ALLOWANCE, EPS_MAX, RADII
from cp007_original_first52_precision_obstruction import parse_original52

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "cp008_zeta_v435/python/out/euler_maclaurin/zeros/zeros_00001.txt"
MANIFEST = STORE.parent / "manifest.json"
LEAN = ROOT / "cp008_zeta_v435/CP008First52.lean"

EXPECT={
    F(1,1000):F(143819,32000000000),
    F(1,500):F(286481,48000000000)
}

def parse_candidate():
    raw=STORE.read_text(encoding="ascii")
    lines=raw.splitlines()
    original=ROOT / "data/cp007_original_euler_maclaurin_first52.txt"
    assert len(lines)==52
    old = original.read_text(encoding="ascii").splitlines()
    assert len(old)==52
    # The upstream source SHA itself is checked through parse_original52().
    old_intervals=parse_original52()
    refined=[]
    for n,(line,old_line,(old_l,old_r)) in enumerate(zip(lines,old,old_intervals),1):
        fields=[x.strip() for x in line.split(",")]
        old_fields=[x.strip() for x in old_line.split(",")]
        assert len(fields)==7 and len(old_fields)==7
        assert fields[0]==str(n)==old_fields[0]
        assert fields[3:]==old_fields[3:],f"Original method cutoffs/parameters changed on row {n}"
        assert all(len(z.partition(".")[2])==5 for z in fields[1:3])
        a,b=map(F,fields[1:3])
        assert old_l<a<b<old_r,f"Candidate {n} is NOT strictly inside its authentic upstream certified bracket"
        assert b-a==F(1,100000),f"Candidate {n} is not the proposed exact width 1e-5"
        if refined:
            assert refined[-1][1]<a,f"Candidate {n} is overlapping or not monotone"
        refined.append((a,b))
    meta=json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert meta["rows"]==52
    assert meta["files"]==[{"file":"zeros_00001.txt","rows":52,"height":"147.42277"}]
    assert meta["params"]["candidate_origin"].endswith("preserved")
    assert refined[0]==(F(1413472,100000),F(1413473,100000))
    assert refined[-1]==(F(14742276,100000),F(14742277,100000))
    lean=LEAN.read_text(encoding="utf-8")
    assert "BatchSpec 52 1413472 100000 14742277 100000 := by" in lean
    assert "build_batch 0 52" in lean
    assert "sorry" not in lean.replace("No all-zero count nor full Weil EF matrix is asserted.","")
    return refined

def rigorous_arithmetic():
    intervals=parse_candidate()
    bands={}
    for a,b in intervals:
        band=dyadic_band(a)
        bands[band]=bands.get(band,F(0))+(b-a)/2
    assert bands=={
        3:F(1,200000), 4:F(3,200000),5:F(1,20000),
        6:F(7,50000),7:F(1,20000)
    }
    for radius in RADII:
        error=localization(radius,bands)
        assert error==EXPECT[radius],f"Exact CP006 candidate localization disagrees at radius={radius}"
        remaining=EPS_MAX-E_tail(radius)-E_QUAD_ALLOWANCE-error
        assert remaining>0
        print(f"r={radius}: exact conditional first52 localization {error} ~= {float(error):.12g}")
        print(f"  Remaining budget for ALL 1747950 other zeros: {remaining} ~= {float(remaining):.12g}")
    print("CP008 SOURCE-SUBSET/EXACT-FRACTION ERROR PREFLIGHT PASS — NO LEAN, ZERO SIGN, OR SPECTRAL CERTIFICATE")

def numeric_screen():
    import mpmath as mp
    mp.mp.dps=75
    candidates=parse_candidate()
    min_abs=None
    for n,(a,b) in enumerate(candidates,1):
        am=mp.mpf(a.numerator)/a.denominator
        bm=mp.mpf(b.numerator)/b.denominator
        root=mp.im(mp.zetazero(n))
        za=mp.siegelz(am)
        zb=mp.siegelz(bm)
        assert am<root<bm and za*zb<0, f"High-precision NUMERIC preflight failed on candidate {n}"
        margin=min(abs(za),abs(zb))
        min_abs=margin if min_abs is None else min(min_abs,margin)
    print(f"CP008 52/52 high-precision NUMERIC Hardy-Z endpoint signs: PASS; min |Z| ~= {mp.nstr(min_abs,14)}")
    print("NOT RIGOROUS: mpmath is not the original Lean Enclosure ball arithmetic; real build_batch required.")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--arithmetic",action="store_true")
    p.add_argument("--numeric-screen",action="store_true")
    args=p.parse_args()
    if args.arithmetic:
        rigorous_arithmetic()
    if args.numeric_screen:
        numeric_screen()
    if not args.arithmetic and not args.numeric_screen:
        p.print_help()

if __name__=="__main__":
    main()
