#!/usr/bin/env python3
"""IV015 — independent EXACT-RATIONAL nonzero frozen-collar gap certificate.

Certificates use positive rational power-series bounds for the real
logarithm, with exact Fraction arithmetic — no float math, numpy,
black-box mpmath intervals, RH or random sampling.

A geometric gap is NOT a Lean kernel proof. The historical original
NF543 two strict collars, genuine ±log(n) translations and original
literal bounded-window cutoff are checked without moving coefficients.
This checks ALL n=0..N-1, even those with Λ(n)=0, strictly stronger
than the actual IV014 Λ-active requirement. Nonzero Schwartz bump
existence is a separate Lean theorem candidate.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

OUT=Path("iv015-frozen-collar-exact-rational-log-gap.json")
CENTER=Q(1,5)
RADIUS=Q(1,1000)
LEFT=-Q(1099,1000)
RIGHT=Q(1099,1000)
OLD_COLLAR_RADIUS=Q(1,1000)
OLD_WINDOW=Q(11,10)
NEW_WINDOW=Q(11,10)
CUTOFF_N=10
SERIES_TERMS=96


def log_bracket(n, terms=SERIES_TERMS):
    """ln(n) ∈ [s,s+tail], using ln(n)=2 artanh((n-1)/(n+1)).

    For 0 ≤ y<1, tail=2*Σ_{k≥K} y^(2k+1)/(2k+1)
      ≤ 2*y^(2K+1)/(2K+1)/(1-y²).
    All operations and inequalities here are on exact rationals.
    Lean's Real.log 0 is 0 by convention.
    """
    assert isinstance(n,int) and n>=0 and terms>0
    if n==0:
        return Q(0),Q(0)
    y=Q(n-1,n+1)
    assert 0<=y<1
    acc=sum((2*y**(2*k+1)/Q(2*k+1)) for k in range(terms))
    rem=2*y**(2*terms+1)/Q(2*terms+1)/(1-y*y)
    assert rem>=0
    return acc,acc+rem


def abs_lower(lo,hi):
    assert lo<=hi
    if lo>0:
        return lo
    if hi<0:
        return -hi
    return Q(0)


def certified(center=CENTER, radius=RADIUS, oldr=OLD_COLLAR_RADIUS,
              oldw=OLD_WINDOW, neww=NEW_WINDOW, cutoff=CUTOFF_N,
              terms=SERIES_TERMS):
    assert radius>0 and oldr>0
    assert abs(center)+radius<neww
    assert not (LEFT-oldr<center<LEFT+oldr)
    assert not (RIGHT-oldr<center<RIGHT+oldr)
    assert cutoff>=2
    margins={}
    min_margin=None
    for n in range(cutoff):
        lo,hi=log_bracket(n,terms)
        results={}
        for label,oldcenter in (("left",LEFT),("right",RIGHT)):
            d=center-oldcenter
            for sign in (-1,1):
                il,iu=(d-hi,d-lo) if sign==-1 else (d+lo,d+hi)
                margin=abs_lower(il,iu)-(oldr+radius)
                assert margin>0,(
                    "Actual ORIGINAL collar and candidate translate overlap",
                    n,label,sign,str(margin))
                results[f"{label}_{'minus' if sign<0 else 'plus'}"]=margin
                if min_margin is None or margin<min_margin:
                    min_margin=margin
        margins[n]=results
    ln_cut_lo,ln_cut_hi=log_bracket(cutoff,terms)
    cutoff_margin=ln_cut_lo-(oldw+neww)
    assert cutoff_margin>0,("Actual original mixed log-prime cutoff does not hold",str(cutoff_margin))
    assert min_margin>0
    return {
        "min_translated_interval_gap":min_margin,
        "cutoff_log_margin":cutoff_margin,
        "per_shift_margin":margins,
        "cutoff_log_interval":(ln_cut_lo,ln_cut_hi),
    }


def format_q(x):
    return f"{x.numerator}/{x.denominator}"

def preflight():
    obj=certified()
    receipt={
        "schema":"IV015-actual-original-NF543-collar-exact-rational-analytic-gap-v1",
        "exact_fraction_input":{
            "candidate_center":format_q(CENTER),
            "candidate_outer_radius":format_q(RADIUS),
            "original_two_collar_centers":[format_q(LEFT),format_q(RIGHT)],
            "original_each_collar_radius":format_q(OLD_COLLAR_RADIUS),
            "original_old_physical_window_radius":format_q(OLD_WINDOW),
            "candidate_new_window_radius":format_q(NEW_WINDOW),
            "cutoff_N":CUTOFF_N,
            "log_atanh_series_terms":SERIES_TERMS,
        },
        "checking_scope":"All integer n=0,...,9 and BOTH ±log(n) shifts in BOTH frozen literal NF543 physical collars, even zero-von-Mangoldt n. This is stronger than Λ-active separation.",
        "certified_lower_strict_log_gap":format_q(obj["min_translated_interval_gap"]),
        "certified_lower_strict_log_cutoff":format_q(obj["cutoff_log_margin"]),
        "per_n_min_gap":{
            str(n):format_q(min(a.values()))
            for n,a in obj["per_shift_margin"].items()
        },
        "rational_interval_log_proof":"For y=(n-1)/(n+1), ln(n)=2∑ y^(2k+1)/(2k+1), with positive tail bounded by 2*y^(2K+1)/((2K+1)*(1-y^2)); exact integer Fraction operations.",
        "all_original_integer_support_shift_geometric_inequalities_exact_rational_pass":True,
        "original_log_cutoff_exact_rational_pass":True,
        "source_only_numeric_rational_proof_not_Lean_kernel":True,
        "nonzero_new_complex_Schwartz_Lean_theorem_pending":True,
        "new_zeta_diagonal_positivity_proved":False,
        "new_zeta_residual_Schur_inequality_proved":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    raw=json.dumps(receipt,indent=2,sort_keys=True)+"\n"
    OUT.write_text(raw)
    print("IV015 independent exact rational geometric gap PASS (not Lean):",
          "min true ±log old/new collar margin >",
          f"{float(obj['min_translated_interval_gap']):.12f}",
          "; log cutoff margin >",f"{float(obj['cutoff_log_margin']):.12f}",
          "; 0..9 all FOUR collar/shift tests. Nonzero bump formal proof still pending.")
    return receipt


def selftest():
    ref=certified()
    cases=["original_frozen_NF543_two_collars_and_1over5_bump_gap_PASS"]
    try:
        certified(center=RIGHT)
    except AssertionError:
        cases.append("old_collar_center_collision_rejected")
    else:
        raise AssertionError("false new test inside old original collars")
    try:
        certified(center=Q(1,5),radius=Q(1,10))
    except AssertionError:
        cases.append("oversized_bump_collides_with_prime_shift_rejected")
    else:
        raise AssertionError("oversized bump accepted")
    try:
        certified(neww=Q(1,10))
    except AssertionError:
        cases.append("outside_physical_window_rejected")
    else:
        raise AssertionError("outside physical window falsely accepted")
    try:
        certified(cutoff=9)
    except AssertionError:
        cases.append("invalid_prime_cutoff_rejected")
    else:
        raise AssertionError("early source cutoff falsely accepted")
    assert ref["min_translated_interval_gap"]>Q(8,100)
    assert ref["cutoff_log_margin"]>Q(1,10)
    cases.append("strict_rational_lower_margins_verified")
    print("IV015 six source-geometry exact-rational counterfactual tests PASS:",cases)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","selftest"))
    args=p.parse_args()
    if args.stage=="preflight":preflight()
    else:selftest()
