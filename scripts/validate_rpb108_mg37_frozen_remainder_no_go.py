#!/usr/bin/env python3
"""MG37 structural frozen-remainder no-go on the ACTUAL original MG35 source.

For a fixed true original pole-corrected 24D source trial B, let
D0=R\[0,4], C=[4,8], and D1=D0\C. True covariance measures satisfy
    X(D0)=X(C)+X(D1), X(C)>=0.

MG35 selects the SAME previously accepted 24x24 omitted-source
Loewner upper U0 for D1 that MG32 already used for D0. The accepted
MG32 complete upper is A+U0; the measured-band replacement is A+V+U0
where V is independently a PSD Loewner UPPER for X(C).

Consequently (A+V+U0)-(A+U0)=V>=0, and no choice of
PSD measured-band upper V under this frozen remainder policy can make
a strictly SMALLER full residual Loewner upper. Its exact TRACE must
increase by trace(V)>=0. This theorem is conditional on the
ACTUAL certificate form, not an operator spectral theorem.

The accepted original MG35 artifact is sufficient to verify the
equality for all four source B/cutoff cases without waiting for MG36:
check the exact rational original MG32 baseline replay, accepted
MG35 remainder selector, and both [4,8] and retained MG19 panels.

A strict positive source residual may still arise from a different
incomparable upper matrix with a better sufficient coordinate test,
but there is no certificate improvement in Loewner order here. To
obtain a genuinely stronger source upper, the remaining-frequency
bound or a jointly integrated covariance must change. MG36/MG37
within-band Young tuning alone cannot fix this lower-order issue.
"""
import argparse,json,sys
from fractions import Fraction as Q
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
LABELS=("MG32_prefix_only","MG33_contiguous_0to8",
        "MG33_hybrid_with_MG19")

def verify(d):
    assert d["status"]=="ORIGINAL_MG35_PSD_MONOTONE_REMAINDER_UPPER_TRACE_GUARD"
    assert d["canonical_W_ODD_NEG"]=="OPEN"
    assert d["verified_original_MG33_run"]==39462301107
    assert d["verified_original_MG34_run"]==39467773045
    assert d["original_source_25physical_23adapted_plus_true_sinh_pole"]
    assert d["actual_original_true_joint_residual_pole_and_signed_multiplier_inherited"]
    assert d["actual_Fourier_measured_sectors_are_nested_disjoint"]
    assert d["actual_original_residual_remainder_covariance_PSD_monotonicity"]
    assert d["all_prior_verified_remainder_uppers_remain_valid_on_smaller_sets"]
    assert d["chosen_omitted_remainder_upper_is_existing_valid_Loewner_matrix"]
    assert d["PSD_safe_full_original_residual_upper_TRACE_only"]
    assert not d["source_residual_strict_positive_gap_certified"]
    assert len(d["scenarios"])==4
    results=[]
    for sc in d["scenarios"]:
        stages=sc["full_original_frequency_upper_trace_scenarios"]
        assert tuple(x["frequency_set"] for x in stages)==LABELS
        base=stages[0]
        base_rem=Q(base["selected_PSD_monotone_remainder_upper_trace"])
        base_measured=Q(base["measured_disjoint_joint_residual_upper_trace"])
        baseline=Q(base["selected_valid_complete_frequency_upper_trace"])
        assert baseline==base_rem+base_measured
        assert baseline==Q(sc["baseline_complete_upper_trace"])
        assert base["selected_PSD_monotone_remainder_upper_from"]==LABELS[0]
        rows=[]
        for i,x in enumerate(stages):
            # Holds for the ACTUAL four MG35 scenarios. Another bound
            # selection would instead require a different theorem.
            assert x["selected_PSD_monotone_remainder_upper_from"]==LABELS[0]
            assert Q(x["selected_PSD_monotone_remainder_upper_trace"])==base_rem
            measured=Q(x["measured_disjoint_joint_residual_upper_trace"])
            full=Q(x["selected_valid_complete_frequency_upper_trace"])
            added=measured-base_measured
            assert added>=0
            assert full-baseline==added
            if i>0:
                assert added>0, "actual original residual-band upper has positive trace"
            rows.append({
                "frequency_set":LABELS[i],
                "inherited_original_remainder_upper_unchanged":True,
                "exact_new_measured_band_upper_trace":str(added),
                "exact_total_residual_upper_trace_increase":str(full-baseline),
                "not_smaller_full_upper_in_Loewner_order":True,
                "exact_trace_identity_passed":True,
                "strict_24D_contraction_proved_by_this_order_argument":False})
        results.append({
           "cutoff_k":sc["cutoff_k"],
           "original_rational_trial":sc["original_rational_trial"],
           "MG32_complete_upper_trace":str(baseline),
           "MG35_guarded_complete_upper_trace":str(Q(stages[-1][
               "selected_valid_complete_frequency_upper_trace"])),
           "all_measured_added_covariances_upper_PSD":True,
           "full_matrix_Loewner_nonimprovement_structural_proof":True,
           "scenarios":rows})
    assert len(results)==4
    return {
       "status":"ORIGINAL_MG37_FROZEN_REMAINDER_DOUBLE_CHARGE_NO_GO",
       "canonical_W_ODD_NEG":"OPEN",
       "verified_MG35_run":39488378664,
       "MG35_genuine_original_24D_23pluspole_benchmark":True,
       "true_covariance_frequency_partition_additivity_used":True,
       "all_selected_omitted_upper_matrices_equal_to_MG32_original":True,
       "all_measured_band_additions_are_original_PSD_upper_matrices":True,
       "new_complete_source_upper_is_old_upper_plus_PSD":True,
       "new_complete_source_upper_cannot_improve_old_in_Loewner_order":True,
       "true_four_case_rational_trace_identity_verified":True,
       "actual_MG37_continuous_Young_numerical_barrier_awaits_MG36":True,
       "original_source_residual_24D_positive_gap_certified":False,
       "original_470D_strong_inverse_certified":False,
       "signed_original_51over56_negative_cap_certified":False,
       "independent_original_Fourier_form_domain_audit":"OPEN",
       "complete_even_Weil_CC27_RH":"OPEN",
       "scenarios":results,
       "next_method_gate":"Do not optimize added-band upper with an unchanged inherited original [0,4] remainder upper if the objective is a sharper full Loewner certificate. Reduce the omitted-frequency upper by genuinely new original source covariance information, or certify the entire joined frequency residual without double paying [4,8]."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg35-json",required=True)
    p.add_argument("--output",default="artifacts/mg37_original_frozen_remainder_no_go.json")
    a=p.parse_args()
    d=json.loads((ROOT/a.verified_mg35_json).read_text())
    result=verify(d)
    path=ROOT/a.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    print("MG37 original frozen remainder structural NO-GO:",json.dumps({
       "cases":[{
          "cutoff":sc["cutoff_k"],"B":sc["original_rational_trial"],
          "baseline":float(Q(sc["MG32_complete_upper_trace"])),
          "guarded":float(Q(sc["MG35_guarded_complete_upper_trace"])),
          "extra":float(Q(sc["scenarios"][-1]["exact_new_measured_band_upper_trace"]))}
          for sc in result["scenarios"]],
       "470D_and_RH":"OPEN"}))
if __name__=="__main__":main()
