#!/usr/bin/env python3
"""MG37: exact trace infimum for MG36 original measured-band Young family.

This is an EXPLICIT BARRIER DIAGNOSTIC, not a new original-source
Loewner certificate. It consumes the independently accepted complete
original 24D MG36 matrices and per-cell exact-rational diagnostics;
does not recompute any Fourier source integrals.

On every true [4,8] cell, the old valid MG32 directional Young
covariance upper TRACE is
    f(t)=(1+t)P+(1+1/t)E, t>0,
 P=2w (||qv||² + w² ||qd||²/12), E=2w(sum qr)².
The MG36 artifact contains the accepted f(t), t, w, sum qr, so P can
be solved BACK algebraically with exact Fraction and checked P>=0.

For P,E>0, inf_(t>0) f(t)=(sqrt(P)+sqrt(E))². Certified rational
lower/upper sqrt enclosures come from Python's exact integer isqrt,
never floating evidence. For zero factors, the corresponding
one-sided limiting infimum is P+E. Finite rational t candidates
propose achievable Young upper matrices on each cell, but this
TRACE-only artifact does not export those matrices.

The true whole-source missing-frequency complement and original
pole remain fixed as accepted MG36. Even with perfect within-family
Young t optimization and ZERO new export rounding cost, the best
possible complete-frequency upper TRACE is bounded BELOW by
   (accepted complete upper TRACE - accepted band upper TRACE)
     + sum_cells (Young infimum lower).
A lower barrier ABOVE the already accepted MG32 complete upper trace
certifies that adjusting Young t ALONE cannot beat MG32 on TRACE
with fixed original source radii/partition/remainder assumptions.
This does NOT prove a negative operator mode, contraction failure
for unrelated methods, or anything about RH.
"""
import argparse,json,sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
SCALE=10**12

def lower_upper_sqrt_rational(x):
    x=F(x);assert x>=0
    if not x:return F(0),F(0)
    y=isqrt((x.numerator*SCALE*SCALE)//x.denominator)
    lo=F(y,SCALE)
    hi=F(y+1,SCALE)
    assert lo*lo<=x<=hi*hi
    return lo,hi

def exact_young_cost(p,e,t):
    assert p>=0 and e>=0 and t>0
    return (1+t)*p+(1+1/t)*e

def analyze_cell(cell):
    w=F(cell["right"])-F(cell["left"])
    assert w>0 and F(4)<=F(cell["left"])<F(cell["right"])<=F(8)
    tau=F(cell["old_Young_tau"]);assert tau>0
    s=F(cell["radii_l1"]);assert s>=0
    E=2*w*s*s
    actual=F(cell["old_directional_Young_raw_trace"])
    P=(actual-(1+1/tau)*E)/(1+tau)
    assert P>=0 and exact_young_cost(P,E,tau)==actual
    if P and E:
        lo,hi=lower_upper_sqrt_rational(P*E)
        fraclo,frachi=lower_upper_sqrt_rational(E/P)
        proposals=[F(1,1024),F(1,16),F(1,4),F(1,2),F(1),
                   F(2),F(4),F(16),F(256),tau]
        for t in (fraclo,frachi):
            if t>0:proposals.append(t)
        optimum_lo=P+E+2*lo
        optimum_hi=P+E+2*hi
    else:
        optimum_lo=optimum_hi=P+E
        proposals=[tau,F(1,1024),F(1),F(1024),F(10**12)]
    optimum_cost,optimum_t=min(
        ((exact_young_cost(P,E,t),t) for t in proposals if t>0),
        key=lambda q:(q[0],q[1]))
    # The rational SQRT upper may lie above a near-optimal rational\n    # candidate; it bounds the INFIMUM, not each candidate from below.\n    assert optimum_lo<=optimum_hi and optimum_lo<=optimum_cost<=actual
    return {
       "true_original_disjoint_4to8_frequency_cell":[cell["left"],cell["right"]],
       "original_MG36_exported_valid_Young_tau":str(tau),
       "reconstructed_original_joint_affine_P_trace":str(P),
       "reconstructed_original_interval_remainder_E_trace":str(E),
       "original_valid_Young_raw_upper_trace":str(actual),
       "infimum_Young_trace_exact_rational_lower":str(optimum_lo),
       "infimum_Young_trace_exact_rational_upper":str(optimum_hi),
       "best_exact_rational_proposed_tau":str(optimum_t),
       "proposed_certified_Young_upper_raw_trace":str(optimum_cost),
       "certified_raw_upper_trace_reduction_from_tau_choice":str(actual-optimum_cost),
       "attainable_Young_infimum_error_bracket":str(optimum_hi-optimum_lo),
       "floating_numbers_used_in_proof":False,
       "new_complete24_fullmatrix_certified":False
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--verified-mg36-json",required=True)
    ap.add_argument("--output",default="artifacts/mg37_original_exact_young_barrier.json")
    a=ap.parse_args()
    mg36=json.loads((ROOT/a.verified_mg36_json).read_text())
    assert mg36["status"]=="ORIGINAL_MG36_DIRECT_BAND_RESIDUAL_FULL24_MATRIX_GATE"
    assert mg36["canonical_W_ODD_NEG"]=="OPEN"
    assert mg36["verified_MG24_run_id"]==39378465438
    assert mg36["verified_MG29_run_id"]==39440914565
    assert mg36["verified_MG30_run_id"]==39442984941
    assert mg36["verified_MG32_run_id"]==39459624082
    assert mg36["verified_MG33_run_id"]==39462301107
    assert mg36["verified_MG35_run_id"]==39488378664
    assert mg36["new_complete_24D_original_residual_UPPER_matrices_exported"]
    assert mg36["PSD_monotone_full_matrix_original_remainder_reuse"]
    assert not mg36["any_strict_24D_source_residual_contraction"]
    assert len(mg36["scenarios"])==4
    allresults=[]
    for scenario in mg36["scenarios"]:
        info=scenario["original_band_cells"]
        assert info["methods"]=={
             "MG36_row_Gershgorin":0,"MG32_directional_Young":32}
        assert len(info["per_cell"])==32
        cells=[analyze_cell(x) for x in info["per_cell"]]
        oldsum=sum((F(c["original_valid_Young_raw_upper_trace"])
                    for c in cells),F(0))
        lowersum=sum((F(c["infimum_Young_trace_exact_rational_lower"])
                      for c in cells),F(0))
        uppersum=sum((F(c["infimum_Young_trace_exact_rational_upper"])
                      for c in cells),F(0))
        candidatesum=sum((F(c["proposed_certified_Young_upper_raw_trace"])
                          for c in cells),F(0))
        assert oldsum==F(info["original_old_raw_trace"])
        assert oldsum==F(info["new_raw_trace"])
        assert 0<=lowersum<=uppersum and lowersum<=candidatesum<=oldsum
        full=F(scenario["MG36_complete_original_Rupper_trace"])
        band=F(scenario["new_MG36_joint_4to8_upper_trace"])
        baseline=F(scenario["MG32_baseline_complete_upper_trace"])
        rest=full-band
        assert rest>=0 and full>=band
        barrier=rest+lowersum
        proposed_raw=rest+candidatesum
        assert barrier<=proposed_raw<=full
        allresults.append({
           "cutoff_k":scenario["cutoff_k"],
           "original_rational_trial":scenario["source_trial"],
           "original_23adapted_plus_genuine_pole_source":True,
           "all_real_original_frequency_remainder_held_fixed":True,
           "source_Taylor_radii_and_multiplier_cell_intervals_held_fixed":True,
           "old_MG36_full_original_source_residual_upper_trace":str(full),
           "old_MG36_direct_band_upper_trace":str(band),
           "old_MG36_band_raw_Young_trace":str(oldsum),
           "fixed_prefix_plus_remainder_upper_trace":str(rest),
           "MG32_original_prefix_only_complete_upper_trace":str(baseline),
           "unattainable_under_frozen_assumptions_if_barrier_ge_MG32":
                   barrier>=baseline,
           "optimal_all_cell_Young_infimum_lower_trace":str(lowersum),
           "optimal_all_cell_Young_infimum_upper_trace":str(uppersum),
           "best_rational_tau_all_cells_raw_upper_trace":str(candidatesum),
           "MG37_full_source_Young_family_lower_TRACE_barrier":str(barrier),
           "MG37_fixed_export_raw_candidate_TRACE":str(proposed_raw),
           "best_rational_trace_savings_before_export":str(oldsum-candidatesum),
           "all_32_source_cells":[*cells],
           "new_complete24_Gershgorin_margin_proved":False,
           "470D_operator_strong_inverse_not_proved":True})
    assert [(s["cutoff_k"],s["original_rational_trial"]) for s in allresults]==[
       (12,"MG24_scalar_t"),(12,"matrix_ridge_1/10_blend_1/4"),
       (16,"MG24_scalar_t"),(16,"matrix_ridge_1/10_blend_1/4")]
    out={
      "status":"ORIGINAL_MG37_FROZEN_YOUNG_PARAMETER_TRACE_BARRIER_AUDIT",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG36_run_id":39495457084,
      "original_25_SI10_23adapted_plus_sinh_pole_channels":True,
      "same_original_signed_seven_prime_arch_frequency_moments_inherited":True,
      "source_remainder_true_PSD_pole_corrected_full_frequency_inherited":True,
      "all_original_4to8_cells_and_4_trial_cases_audited":True,
      "exact_rational_Young_infimum_sqrt_certificates":True,
      "young_optimizers_only_trace_candidate_not_fullmatrix_certificates":True,
      "complete_24D_matrix_positive_residual_certified":False,
      "original_470D_strong_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "scenarios":allresults,
      "decision":"If exact Young infimum trace floor is still above accepted MG32 baseline, within-family tau tuning cannot reverse the measured-band full trace deficit. Pivot to improving source residual radii, analytic cancellation or the pole-accurate joint error rather than optimizing tau."
    }
    dst=ROOT/a.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG37 original Young barrier:",json.dumps({
      "cases":[{
         "k":s["cutoff_k"],"trial":s["original_rational_trial"],
         "baseline":float(F(s["MG32_original_prefix_only_complete_upper_trace"])),
         "current":float(F(s["old_MG36_full_original_source_residual_upper_trace"])),
         "best_possible_lower":float(F(s["MG37_full_source_Young_family_lower_TRACE_barrier"])),
         "rational_proposal_before_export":float(F(s["MG37_fixed_export_raw_candidate_TRACE"])),
         "barrier_excludes_MG32":s["unattainable_under_frozen_assumptions_if_barrier_ge_MG32"]}
         for s in allresults],"original_470D_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
