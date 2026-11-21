#!/usr/bin/env python3
"""CP017: exact rational Hardy-Z derivative/curvature sufficiency preflight.

The inequalities below are a CONDITIONAL MATH CERTIFICATE, not numerical
interval arithmetic for zeta and NOT a genuine Lean kernel certificate.

To promote the original first RS numerical zero to canonical ordinal 53,
we still require BOTH genuine analytic proof objects:
  Zeta.hardyZ'(149.5) >= 12/5;
  norm(derivWithin (deriv Zeta.hardyZ) [149.5,150.05353] t) <= 4
      for EVERY t in [149.5,150.05353).
And a genuine root-existence certificate inside (150.05352,150.05353).
Only those lead, by real-v4.35 CP017 Lean source candidate, to exact
HardyZ strict monotonicity and equality with source rank 53.

The optional mpmath screen prints NONRIGOROUS numerical values only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ORIGINAL_ZETA="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
ORIGINAL_MATHLIB="v4.35.0"
ZETA_SOURCES={
 "Zeta/Zeros/HardyZ.lean":"9975442b0c14011c35f4624197d0bf26169c7665",
 "Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean":
   "c2b1da101a580cc91cfb0a43d72d5839fd97265c",
}
MATHLIB_SOURCES={
 "Mathlib/Analysis/Calculus/Deriv/MeanValue.lean":
   "b72f134c66e2fc86a0ac93dd241629881b9e7d1b",
 "Mathlib/Analysis/Calculus/MeanValue.lean":
   "7004c9f6d2bf12928f02be9ee35a814aed17e254",
}
A=F(149500,1000)
B=F(15005353,100000)
LO=F(15005352,100000)
ANCHOR=F(12,5)
CURV=F(4)
EXPECTED_MARGIN=F(4647,25000)


def gitblob(path):
    n=path.stat().st_size
    h=hashlib.sha1(b"blob "+str(n).encode()+b"\0")
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def exact_preflight():
    assert A==F(299,2)
    assert B-A==F(55353,100000)
    assert LO<B and LO>A
    assert ANCHOR-CURV*(B-A)==EXPECTED_MARGIN
    assert EXPECTED_MARGIN>0
    assert CURV < ANCHOR/(B-A)
    assert ANCHOR/(B-A)==F(80000,18451)
    # A looser 5-unit curvature bound is NOT sufficient with same anchor.
    assert ANCHOR-F(5)*(B-A)<0
    # A weaker 2-unit anchor is NOT enough with curvature 4.
    assert F(2)-CURV*(B-A)<0
    # Endpoint derivative anchor and pointwise curvature bounds MUST be
    # supplied by a uniform analytic bound, not merely 81+ sample values.
    print("CP017 EXACT RATIONAL DERIVATIVE CURVATURE SUFFICIENCY: PASS")
    print("  source interval        : [149.5, 150.05353]")
    print("  exact window width     : 55353/100000 = 0.55353")
    print("  assumed Z-prime anchor : 12/5 = 2.4")
    print("  assumed curvature cap  : 4 on ENTIRE [a,b)")
    print("  lower derivative bound : 4647/25000 = 0.18588")
    print("  critical max cap       : 80000/18451 ~ 4.3358")
    print("  fallback C=5, anchor=2 negatives: PASS")
    print("  NO ACTUAL RIGOROUS HardyZ analytic bound certified.")


def genuine_source_pin(zeta,mathlib,receipt):
    sources={}
    for base,pins in ((zeta,ZETA_SOURCES),(mathlib,MATHLIB_SOURCES)):
        for name,sha in pins.items():
            file=base/name
            got=gitblob(file)
            if got!=sha:
                raise ValueError(f"Authentic original Lean source drift {name} got {got}, pinned {sha}")
            sources[name]=file.read_text("utf-8")
    hardy=sources["Zeta/Zeros/HardyZ.lean"]
    for text in (
        "noncomputable def Zeta.hardyZ (t : ℝ)",
        "theorem continuousOn_hardyZ",
        "theorem hardyZ_eq_zero_iff_riemannZeta",
    ):
        if text not in hardy:
            raise ValueError("Original Zeta Hardy-Z API changed: "+text)
    mean=sources["Mathlib/Analysis/Calculus/MeanValue.lean"]
    derivmean=sources["Mathlib/Analysis/Calculus/Deriv/MeanValue.lean"]
    if "theorem norm_image_sub_le_of_norm_deriv_le_segment" not in mean:
        raise ValueError("Original Mathlib curvature-to-Lipschitz theorem absent")
    if "theorem strictMonoOn_of_deriv_pos" not in derivmean:
        raise ValueError("Original Mathlib positivity-to-monotonicity theorem absent")
    rank=sources["Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean"]
    if "theorem riemannZeta.N_gramPoint_eq" not in rank:
        raise ValueError("Original zeta N(g) Turing count theorem absent")
    lean=(ROOT/"cp011_zeta_v435/CP017CurvatureBudget.lean").read_text("utf-8")
    for term in (
        "theorem exact_positive_derivative_margin",
        "theorem uniform_derivative_margin_of_rational_budget",
        "theorem strictMonoOn_original_hardyZ_of_rational_budget",
        "theorem derivative_variation_of_curvature_bound",
        "theorem strictMonoOn_original_hardyZ_of_curvature_bound",
        "theorem refined_narrow_root_is_source_53rd_of_rational_budget",
        "theorem narrowRightLtOriginalGram",
        "∀ t ∈ Ico a b",
        "(hanchor : (12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a)",
        "(hvariation :",
        "norm_image_sub_le_of_norm_deriv_le_segment",
    ):
        if term not in lean:
            raise ValueError("CP017 Lean source missing necessary explicit hypothesis: "+term)
    if "sorry" in lean.split("@[expose] public section")[-1]:
        raise ValueError("New CP017 source contains sorry in theorems")
    output={
      "status":"CP017_PINNED_MATHLIB_HARDYZ_DERIVATIVE_BUDGET_SOURCE_PASS_NOT_KERNEL",
      "original_external_zeta_commit":ORIGINAL_ZETA,
      "original_mathlib_rev":ORIGINAL_MATHLIB,
      "source_genuine_git_blobs":{**ZETA_SOURCES,**MATHLIB_SOURCES},
      "interval":["299/2","15005353/100000"],
      "proposed_narrow_zero":["15005352/100000","15005353/100000"],
      "exact_derivative_anchor_lower":"12/5",
      "UNPROVED_uniform_curvature_upper":"4",
      "UNPROVED_actual_anchor_bound":"12/5",
      "derived_if_hypotheses_hold_positive_derivative_margin":"4647/25000",
      "critical_curvature_threshold":"80000/18451",
      "new_CP017_actual_lean_kernel_accepted":False,
      "CP010_actual_narrow_HardyZ_sign_accepted":False,
      "hardyZ_uniform_derivative_enclosures_accepted":False,
      "original_first_RS_numeric_root_ordinal53_proved":False,
      "Weil_spectral_3x3_equality":False,
    }
    receipt.write_text(json.dumps(output,indent=2)+"\n","utf-8")
    print(output["status"])


def numeric_screen(n=81,dps=50):
    """Exploration only. mpmath derivatives are NOT validated enclosures."""
    import mpmath as mp
    mp.mp.dps=dps
    def to_mpf(x):
        return mp.mpf(x.numerator)/x.denominator
    aa=to_mpf(A)
    bb=to_mpf(B)
    data=[]
    for i in range(n):
        t=aa+(bb-aa)*i/(n-1)
        data.append((t,mp.diff(mp.siegelz,t),mp.diff(mp.siegelz,t,2)))
    m1=min((p[1],p[0]) for p in data)
    m2=max((abs(p[2]),p[0]) for p in data)
    print("NONRIGOROUS NUMERICAL Hardy-Z sample, no certified interval bounds")
    print("  sampled count:",n, "  decimal precision:",dps)
    print("  Z-prime at 149.5:",mp.nstr(data[0][1],25))
    print("  min Z-prime sample:",mp.nstr(m1[0],22), "at",mp.nstr(m1[1],16))
    print("  max abs Z-double-prime sample:",mp.nstr(m2[0],22),
          "at",mp.nstr(m2[1],16))
    print("  This is NOT proof of the two exact rational assumptions.")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--zeta",type=Path)
    p.add_argument("--mathlib",type=Path)
    p.add_argument("--numeric-screen",action="store_true")
    p.add_argument("--sample-count",type=int,default=81)
    p.add_argument("--receipt",type=Path,default=Path("cp017-original-curvature-source-only.json"))
    a=p.parse_args()
    if a.self_test:
        exact_preflight()
    if bool(a.zeta)!=bool(a.mathlib):
        raise SystemExit("NOT_READY: requires BOTH original Zeta and Mathlib v4.35 source roots")
    if a.zeta:
        try:
            genuine_source_pin(a.zeta,a.mathlib,a.receipt)
        except (OSError,AssertionError,ValueError,UnicodeError) as e:
            raise SystemExit(f"NOT_READY: {e}")
    if a.numeric_screen:
        if not 2<=a.sample_count<=2001:
            raise SystemExit("NOT_READY: use 2-2001 numerical samples only")
        numeric_screen(a.sample_count)
    if not (a.self_test or a.zeta or a.numeric_screen):
        p.print_help()


if __name__=="__main__":
    main()
