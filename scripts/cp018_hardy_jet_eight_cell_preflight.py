#!/usr/bin/env python3
"""CP018 exact eight-cell Hardy-Z curvature budget + analytic-jet provenance.

Real rigor:
- Exact rational interval tiling and all proof-budget arithmetic use
  stdlib Fraction and assertions; no numerical zeta values are trusted.
- The original Hardy-Z definition is matched against frozen original
  source by Git blob SHA. Original published ABS VALUE error theorem
  does NOT certify the derivative errors; never differentiate it.

Exploration only:
- 8 midpoint Z'' samples and analytic complex-jet Z'' cross-check,
  optionally 81-point Z''' sample, use mpmath and are NONRIGOROUS.
- A genuine proof still requires eight validated center enclosures
  |Z''(c_j)|<=7/2, uniform |Z'''|<=12 on [a,b], differentiability,
  original Z'(a)>=12/5, and narrow new zero existence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ORIGINAL="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
MATHLIB_REF="v4.35.0"
ZETA_BLOBS={
    "Zeta/Zeros/HardyZ.lean":"9975442b0c14011c35f4624197d0bf26169c7665",
    "Zeta/Gamma/LogGammaBranch.lean":"f544c4682969d8cefe0b8f489f6ddbaafaba45d5",
    "Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean":"c2b1da101a580cc91cfb0a43d72d5839fd97265c",
}
MATHLIB_BLOBS={
    "Mathlib/Analysis/Calculus/MeanValue.lean":
      "7004c9f6d2bf12928f02be9ee35a814aed17e254",
}
A=F(299,2)
B=F(15005353,100000)
W=B-A
N=8
CENTER_CAP=F(7,2)
THIRD_CAP=F(12)
ANCHOR=F(12,5)
EXPECTED_PAD=F(166059,400000)
EXPECTED_CURV=F(1566059,400000)
EXPECTED_GAP=F(33941,400000)
EXPECTED_DERIV=F(4647,25000)

def gitblob(path:Path)->str:
    n=path.stat().st_size
    h=hashlib.sha1(b"blob "+str(n).encode("ascii")+b"\0")
    with path.open("rb") as stream:
        for chunk in iter(lambda:stream.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()

def centers():
    return tuple(A+F(2*j+1,16)*W for j in range(N))

def exact_test():
    c=centers()
    assert len(c)==8 and len(set(c))==8
    assert A<B and W==F(55353,100000)
    assert all(c[j]==A+W*F(2*j+1,16) for j in range(8))
    for j in range(8):
        L=A+W*F(j,8)
        R=A+W*F(j+1,8)
        assert L<=c[j]<=R and R-L==W/8
        assert c[j]-L==W/16 and R-c[j]==W/16
        assert (R if j==7 else A+W*F(j+1,8)) == A+W*F(j+1,8)
    assert A+W==B
    assert THIRD_CAP*W/16==EXPECTED_PAD
    assert CENTER_CAP+EXPECTED_PAD==EXPECTED_CURV
    assert F(4)-EXPECTED_CURV==EXPECTED_GAP
    assert EXPECTED_GAP>0
    assert EXPECTED_CURV<4
    # The ORIGINAL CP017 bound has a separate exact derivative cushion.
    assert ANCHOR-4*W==EXPECTED_DERIV>0
    # Negative controls: a weaker center cap or much larger D3 cap
    # could break the actual universal curvature conclusion.
    assert F(15,4)+THIRD_CAP*W/16>4
    assert CENTER_CAP+F(15)*W/16>4
    # Exact C3 cap threshold assuming 7/2 midpoint bound.
    assert (F(4)-CENTER_CAP)*16/W==F(800000,55353)
    print("CP018 EXACT 8-CELL RATIONAL COVERAGE/CURVATURE BUDGET: PASS")
    print(f"  interval: [{A}, {B}]  width {W}")
    print("  center ordinates [EXACT]:")
    for i,x in enumerate(c):
        print(f"    {i}: {x} = {float(x):.9f}")
    print(f"  8 center |Z-second| assumptions: {CENTER_CAP}")
    print(f"  one UNPROVED UNIFORM |Z-third| bound: {THIRD_CAP}")
    print(f"  max per-cell third-derivative variation: {EXPECTED_PAD}")
    print(f"  resulting if assumptions hold curvature: {EXPECTED_CURV} = {float(EXPECTED_CURV)}")
    print(f"  strict curvature slack: {EXPECTED_GAP} = {float(EXPECTED_GAP)}")
    print("  NOTE: source derivatives/smoothness/root existence have NOT been certified.")

def true_source_gate(zeta:Path,mathlib:Path,receipt:Path):
    content={}
    for base,pins in ((zeta,ZETA_BLOBS),(mathlib,MATHLIB_BLOBS)):
        for name,sha in pins.items():
            f=base/name
            got=gitblob(f)
            if got!=sha:
                raise ValueError(f"Original upstream SHA mismatch: {name}: {got} vs {sha}")
            content[name]=f.read_text("utf-8")
    hd=content["Zeta/Zeros/HardyZ.lean"]
    for term in (
        "noncomputable def Zeta.hardyZ (t : ℝ)",
        "theorem riemannSiegelTheta_eq_im_logGamma",
        "theorem continuousOn_hardyZ",
        "theorem abs_hardyZRemainderEM_le",
        "theorem hardyZ_eq_zero_iff_riemannZeta",
    ):
        if term not in hd:
            raise ValueError(f"Wrong genuine Zeta hardyZ interface: {term}")
    if "deriv (Zeta.hardyZ" in hd:
        raise ValueError("Unexpected derivative theorem: inspect before classifying")
    gamma=content["Zeta/Gamma/LogGammaBranch.lean"]
    if "theorem hasDerivAt_logGamma" not in gamma:
        raise ValueError("Original logGamma digamma chain theorem absent")
    if "theorem norm_image_sub_le_of_norm_deriv_le" not in (
        content["Mathlib/Analysis/Calculus/MeanValue.lean"]):
        raise ValueError("Mathlib genuine MVT derivative/finite mesh bridge absent")
    lean=(ROOT/"cp011_zeta_v435/CP018EightCell.lean").read_text("utf-8")
    for term in (
        "def center (j : Fin 8)", "theorem center_mem_interval",
        "theorem eight_center_cover",
        "theorem exact_eight_cell_curvature_margin",
        "theorem eight_midpoints_and_third_derivative_imply_curvature",
        "theorem original_hardyZ_strictMono_of_eight_midpoint_certificate",
        "hD2diff", "hD3", "hcenters", "hD1diff",
    ):
        if term not in lean:
            raise ValueError("Missing original CP018 Lean source proof target: "+term)
    if "sorry" in lean.split("@[expose] public section")[-1]:
        raise ValueError("Actual new Lean theorem section has sorry")
    output={
        "status":"CP018_FOUR_ORIGINAL_SOURCE_SHA_AND_EIGHT_CELL_EXACT_LOGIC_PASS_NOT_LEAN",
        "original_zeta_commit":ORIGINAL,
        "original_mathlib_ref":MATHLIB_REF,
        "original_actual_git_blobs":{**ZETA_BLOBS,**MATHLIB_BLOBS},
        "exact_interval":["299/2","15005353/100000"],
        "exact_width":"55353/100000",
        "exact_center_ordinates":[str(x) for x in centers()],
        "centre_second_derivative_bound":"7/2",
        "uniform_third_derivative_bound":"12",
        "exact_curvature_upper_if_analytic_hypotheses":"1566059/400000",
        "strict_curvature_budget_slack":"33941/400000",
        "genuine_original_HardyZ_value_error_is_NOT_derivative_error":True,
        "actual_8_center_derivative_interval_certificates":None,
        "actual_third_derivative_uniform_enclosure":None,
        "actual_source_jet_identity_kernel":None,
        "actual_root53_narrow_sign_certificate":None,
        "new_Lean_kernel_acceptance":False,
        "full_signed_Weil_spectral_dictionary":False,
    }
    receipt.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(output["status"])

def exploratory_numerical(n=81,dps=40):
    """Numerical only. TWO separate formulas cross-check analytic identity."""
    import mpmath as mp
    if n<9 or n>1025 or dps<25 or dps>120:
        raise ValueError("Unsafe sample count/precision")
    mp.mp.dps=dps
    cast=lambda q:mp.mpf(q.numerator)/q.denominator
    aa,bb=cast(A),cast(B)
    ce=centers()
    maxc=mp.mpf(0)
    print("CP018 NONRIGOROUS mpmath center Z-second samples; NOT interval enclosures:")
    for j,c in enumerate(ce):
        t=cast(c)
        val=mp.diff(mp.siegelz,t,2)
        maxc=max(maxc,abs(val))
        w=mp.mpf("0.25")+1j*t/2
        s=mp.mpf("0.5")+1j*t
        theta=mp.im(mp.loggamma(w))-t*mp.log(mp.pi)/2
        t1=mp.re(mp.digamma(w))/2-mp.log(mp.pi)/2
        t2=-mp.im(mp.polygamma(1,w))/4
        z=mp.zeta(s)
        z1=mp.diff(mp.zeta,s)
        z2=mp.diff(mp.zeta,s,2)
        analytic=mp.re(mp.exp(1j*theta)*(
            -(t1*t1)*z-2*t1*z1-z2+1j*t2*z))
        error=abs(val-analytic)
        print(f"  midpoint {j}: {mp.nstr(t,15)} "
              f"Z''≈{mp.nstr(val,18)} jet-mismatch≈{mp.nstr(error,5)} "
              "[NUMERICAL ONLY]")
        if error>mp.mpf("1e-25"):
            raise ValueError("Independent numeric Hardy jet mismatch too large")
    max3=mp.mpf(0)
    for i in range(n):
        x=aa+(bb-aa)*i/(n-1)
        max3=max(max3,abs(mp.diff(mp.siegelz,x,3)))
    dp=mp.diff(mp.siegelz,aa)
    print("  NONRIGOROUS finite midpoint max |Z''|≈",mp.nstr(maxc,22))
    print("  NONRIGOROUS sampled max |Z'''|≈",mp.nstr(max3,22))
    print("  NONRIGOROUS sampled Z'(149.5)≈",mp.nstr(dp,22))
    print("  None of these samples proves a UNIVERSAL derivative bound.")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--self-test",action="store_true")
    parser.add_argument("--zeta",type=Path)
    parser.add_argument("--mathlib",type=Path)
    parser.add_argument("--receipt",type=Path,default=Path("cp018-eight-cell-source-budget.json"))
    parser.add_argument("--numeric-screen",action="store_true")
    parser.add_argument("--sample-count",type=int,default=81)
    parser.add_argument("--dps",type=int,default=40)
    a=parser.parse_args()
    if a.self_test:
        exact_test()
    if bool(a.zeta)!=bool(a.mathlib):
        parser.error("Must provide BOTH original Zeta and Mathlib source directories")
    if a.zeta:
        try:
            true_source_gate(a.zeta,a.mathlib,a.receipt)
        except (ValueError,OSError,UnicodeError) as e:
            raise SystemExit("NOT_READY: "+str(e))
    if a.numeric_screen:
        exploratory_numerical(a.sample_count,a.dps)
    if not (a.self_test or a.zeta or a.numeric_screen):
        parser.print_help()

if __name__=="__main__":
    main()
