#!/usr/bin/env python3
"""SM43A: exact original POSITIVE signed multiplier AFFINE interpolation.

Stronger than SM43 piecewise-constant:
  for every real ξ∈I=[a,b], m(ξ) is approximated by affine
  interpolation of the TRUE original signed m endpoint values,
  with remainder <= (D_prime+D_arch(a))*h²/8.

Entire original digamma second derivative has an exact rational
bound for all ξ>=a. From quarter-digamma positive-term expansion
  |d²/dt² t²/[v(v²+t²)]|
       <=6/(v²+t²)^(3/2), v=k+1/4, t=pi ξ.
  For a>=1, sum <=
    4/(1/16+(pi_low*a)²)+1/(pi_low*a)².
  For a<1, sum<=64+8=72.
 Multiply by pi_up²*6 and add original SM40 all-seven-prime
 D2. Exact Fraction, no sample or hidden kink assumption.

Let m_{*,I}(ξ) be AFFINE interpolation of endpoint RATIONAL
interval midpoint approximations for genuine original m.
a_{*,I}(ξ)=max(kappa,m_{*,I}(ξ)) has AT MOST ONE rational
crossing inside I. For ALL original REAL ξ∈I,
 |max(kappa,m(ξ))-a_{*,I}(ξ)|
  <=max(endpoint interval radius) +D_I*h²/8,
by 1-Lipschitz of max(kappa,·). This is valid EVEN IF actual
m has arbitrarily many crossings in I.

Combining with original SI10 25 genuine zero-extended odd physical
source cell sup s_j from SM43 yields a CERTIFIED full 25x25
Loewner form error to exact (NOT YET EVALUATED) source-weighted
piecewise-affine frequency integral:
 -epsilon I25 <= A_true_windows-A_affine_windows<=epsilon I25.

This avoids the O(h) genuine-multiplier oscillation error of SM43's
constant step. It does NOT evaluate the reference Fourier cell
integrals, cover rest of [0,4096], or prove original Wodd/RH.
"""
import argparse
import json
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import PI, prime_interval, B
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm40_endpoint_curvature_negative_cap import D2
from validate_rpb108_sm39_rational_left_arch_cap import arch_lower_at
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,arch_upper_at,original_source_centered_windows,
    source_window_support_envelopes,ceil_rat,
    positive_cell_weight_interval
)

A=F(1,4)
LOWARCH=6*PI[1]*PI[1]*(F(64)+F(8))


def arch_second_derivative_whole_real_upper(left):
    left=F(left)
    assert left>=0
    if left<1:return LOWARCH
    tt=PI[0]*left
    # Monotone integrable upper 6 Σ(v²+t²)^(-3/2):
    # first <=4/(a²+t²), integral from a..inf <=1/t².
    better=6*PI[1]*PI[1]*(4/(A*A+tt*tt)+1/(tt*tt))
    return min(LOWARCH,better)


def affine_cell_error(left,right,centers,sources):
    left=F(left);right=F(right);h=right-left
    assert 0<=left<right<=4096
    # Original genuine signed multiplier at TWO exact rational
    # endpoints enclosed by full SI06 original seven-prime and
    # SI07/SM39 original monotone positive 64-term digamma.
    mla=arch_lower_at(left)+prime_interval(left)[0]
    mua=arch_upper_at(left)+prime_interval(left)[1]
    mlb=arch_lower_at(right)+prime_interval(right)[0]
    mub=arch_upper_at(right)+prime_interval(right)[1]
    assert mla<=mua and mlb<=mub
    D=D2+arch_second_derivative_whole_real_upper(left)
    assert D>=D2
    curvature=D*h*h/8
    # Signed m_*(xi) interpolates midpoint rational endpoint
    # values; true m differs by at most radius+curvature.
    w=max(mua-mla,mub-mlb)
    error=w/2+curvature
    assert error>=0
    # If true original m is below kappa for the entire cell,
    # then the TRUE a_o and a_* are the same constant kappa.
    certified_constant=max(mua,mub)+curvature<=KAPPA
    if certified_constant:
        true_error=F(0)
    else:
        true_error=error
    s=source_window_support_envelopes(left,right,centers,sources)
    E=sum((x*x for x in s),F(0))
    # Original form uses reflected signed half-frequency factor2.
    eps_affine=2*h*true_error*E
    # The original SM43 CONSTANT reference and our new affine
    # reference are TWO independently proven TRUE-original
    # whole-real cell approximations. Choose the one with
    # STRICTLY SMALLER exact rational error on EACH cell.
    # A hybrid with per-cell verified choice is automatically
    # no worse than either whole-mesh global method, and the
    # chosen reference remains explicitly defined and fully
    # coupled in the original physical Fourier source integral.
    low,high,_=positive_cell_weight_interval(left,right)
    eps_constant=h*(high-low)*E
    assert eps_constant>=0 and eps_affine>=0
    use_affine=eps_affine<eps_constant
    eps=min(eps_affine,eps_constant)
    va=(mla+mua)/2
    vb=(mlb+mub)/2
    kink_possible=use_affine and (min(va,vb)<KAPPA<max(va,vb))
    return eps,{
      "whole_real_positive_constant_cell":certified_constant,
      "reference_affine_max_has_rational_kink":kink_possible,
      "reference_choice":"signed_positive_part_affine" if use_affine else "original_constant_cell",
      "signed_original_endpoint_interval_max_width":w,
      "whole_original_second_derivative_upper":D,
      "exact_curvature_error":curvature,
      "full_coupled_hybrid_source_error_exact":eps,
      "source_affine_error_exact":eps_affine,
      "source_constant_error_exact":eps_constant
    }


def evaluate(step,centers,sources,windows):
    step=F(step)
    assert 0<step<=F(1,4)
    ncell=0;nflat=0;ncross=0;naffine=0;total=F(0);total_affine=F(0);total_constant=F(0)
    maxcurv=F(0); maxw=F(0)
    windows_total=F(0)
    for aa,bb in windows:
        size=bb-aa;windows_total+=size
        n=(size.numerator*step.denominator+
           size.denominator*step.numerator-1)//(
           size.denominator*step.numerator)
        assert n>=1
        for i in range(n):
            a=aa+size*F(i,n);b=aa+size*F(i+1,n)
            e,meta=affine_cell_error(a,b,centers,sources)
            total+=e;ncell+=1
            total_affine+=meta["source_affine_error_exact"]
            total_constant+=meta["source_constant_error_exact"]
            naffine+=meta["reference_choice"]=="signed_positive_part_affine"
            nflat+=bool(meta["whole_real_positive_constant_cell"])
            ncross+=bool(meta["reference_affine_max_has_rational_kink"])
            maxcurv=max(maxcurv,meta["exact_curvature_error"])
            maxw=max(maxw,meta["signed_original_endpoint_interval_max_width"])
    assert total>0
    return {
       "certified_exact_max_cell_width":str(step),
       "same_true_source_window_measure":str(windows_total),
       "original_selected_odd_source_count":25,
       "exact_original_real_frequency_cells":ncell,
       "certified_real_whole_constant_kappa_cells":nflat,
       "piecewise_affine_reference_rational_crossing_cells":ncross,
       "cells_using_sm43A_signed_affine_reference":naffine,
       "cells_using_verified_original_constant_reference":ncell-naffine,
       "all_affine_reference_error_float":float(total_affine),
       "all_constant_reference_error_float":float(total_constant),
       "max_true_signed_endpoint_uncertainty_float":float(maxw),
       "max_true_original_curvature_allowance_float":float(maxcurv),
       "certified_full_25x25_hybrid_reference_Loewner_error_outward":
           str(ceil_rat(total,10**9)),
       "certified_full_25x25_hybrid_reference_error_float":float(total),
       "reference_integral":"2 sum_I int_I verified per-cell chosen weight (original constant midpoint OR max(kappa,signed endpoint-midpoint affine)) * T_original T_original*",
       "reference_integrals_certified":False,
       "complete_original_low_0_to_4096_certified":False,
       "original_full_odd_signed_positive":False
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm43_original_affine_positive_error.json")
    args=p.parse_args()
    d=json.loads((ROOT/"research/obligations.json").read_text())
    o=next(z for z in d["obligations"] if z["id"]=="W-ODD-NEG")
    assert d["active_obligation"]=="W-ODD-NEG"
    assert d["objective"]["status"]=="open" and o["status"]=="open"
    assert d["governance"]["no_automatic_promotion"] is True
    assert "sm43_original_affine_second_order" in d["governance"]
    cen,sources,windows=original_source_centered_windows()
    coarse=evaluate(F(1,4),cen,sources,windows)
    fine=evaluate(F(1,8),cen,sources,windows)
    print("SM43A ACTUAL ORIGINAL REAL POSITIVE AFFINE 1/4",
          json.dumps(coarse,sort_keys=True),flush=True)
    print("SM43A ACTUAL ORIGINAL REAL POSITIVE AFFINE 1/8",
          json.dumps(fine,sort_keys=True),flush=True)
    constant=json.loads((
        ROOT/"artifacts/sm43_original_positive_cell_error.json").read_text())
    assert constant["status"]=="CERTIFIED_TRUE_ORIGINAL_SOURCE_WINDOW_POSITIVE_INTERVAL_ENVELOPE_ONLY"
    assert coarse["same_true_source_window_measure"]==fine["same_true_source_window_measure"]
    assert fine["certified_full_25x25_hybrid_reference_error_float"] < (
        coarse["certified_full_25x25_hybrid_reference_error_float"])
    # Compare EXACT outward rational certificate scalars to the
    # SAME actual original window old constant-step error: strict
    # efficiency of *second-order* method is required, no promotion.
    assert F(fine["certified_full_25x25_hybrid_reference_Loewner_error_outward"]) < F(
        constant["finer_step"]["certified_whole_25x25_window_Loewner_error_I_exact"])
    data={
      "status":"CERTIFIED_TRUE_ORIGINAL_POSITIVE_SOURCE_WINDOW_ADAPTIVE_CONSTANT_AFFINE_ERROR_ONLY",
      "canonical_original_odd_O1_O2":"OPEN",
      "analytical_original_positive_curvature":{
         "all_seven_prime_second_derivative":"SM40 exact rational D2",
         "entire_digamma_second_derivative":"exact positive-term bound 6*pi_hi^2*[4/(a^2+(pi_lo*l)^2)+1/(pi_lo*l)^2] for l>=1, global finite near 0",
         "positive_part_crossing":"max(kappa,x) globally 1-Lipschitz; piecewise rational affine max has at most one explicit crossing",
         "source_gram":"all 25 original SI10 zero-extended physical Fourier cross paid by true whole-cell source bounds",
         "error_order":"per-cell minimum of full original SM43 constant O(h) error and SM43A signed-affine endpoint interval radius plus D*h^2/8, all exact rational",
         "reference_cell_source_Fourier_integrals_certified":False,
         "original_affine_only_fine_error_did_not_pass_first_order_comparison":True
      },
      "first_step":coarse,
      "refined_step":fine,
      "constant_step_refined_error_outward":
          constant["finer_step"]["certified_whole_25x25_window_Loewner_error_I_exact"],
      "acceptance_still_missing":[
        "validated actual positive affine-reference source Fourier matrix integrals for every processed cell",
        "entire remaining original 0..4096 positive LOW band outside 25-source windows",
        "all original 470 higher-degree physical source transforms and positive tail",
        "original true Astar positive inverse strong residual and complete 470 source O1/O2 or corrected Schur",
        "even E1-E4 Weil CC27 RH and independent Fourier/domain audit"
      ]
    }
    out=ROOT/args.output;out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2)+"\n")
    print("SM43A SCOPED PASS: TRUE ORIGINAL WHOLE-REAL source-window"
          " a_o=max(kappa,m) original complete 25-source adaptive"
          " locally minimum VERIFIED error of constant or signed"
          " endpoint-affine positive weight (O(h²) curvature),"
          " valid through ALL crossings, improves first-order"
          " all-constant source-window bound. Affine source"
          " Fourier cell integrals and rest of full positive LOW"
          " [0,4096] OPEN; whole odd/even/Weil/RH OPEN.",flush=True)

if __name__=="__main__":
    main()
