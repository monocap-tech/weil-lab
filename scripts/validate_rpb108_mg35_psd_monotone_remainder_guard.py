#!/usr/bin/env python3
"""MG35: exact original 24D PSD-monotone omitted-frequency guard.

This method is deliberately TRACE-scoped. It consumes independent accepted
MG33 source residual bounds; the artifact contains exact rational traces but
NOT the complete 24x24 Rupper matrices.

For original true residual Fourier row r(xi), define
X(D)=integral_D r(xi)^T r(xi) dxi. For any measurable D1 subset D0,
0 <= X(D1) <= X(D0) in the genuine Loewner order, even when a
sourcewise-Young lower mass enclosure L_D is indefinite. Therefore EVERY
certified Loewner upper on X(D0) is a valid upper on X(D1).

For measured C0 subset C1 subset C2 and omitted D_i=R\C_i,
the certified old remainder bounds U_D0, U_D1, U_D2 are ALL
valid for the final omitted D2. Choose the candidate with smallest
exact TRACE (ties deterministic); that selected whole MATRIX is a valid
Loewner upper for omitted covariance, though a trace comparison of two
uppers is NOT their Loewner ordering. Thus the selected remainder UPPER
trace is monotone nonincreasing as more valid options are added.

Using actual MG33 original source-sector *joint R*R upper* matrices:
  U_joint(C1)=U_joint(C0)+U_band
  U_joint(C2)=U_joint(C0)+U_band+U_sites.
All addends are valid whole-real source sector upper Loewner bounds.
For each original fixed MG30 rational B/cutoff, compute exact TRUE
upper TRACE under the monotone omitted envelope, and distinguish its
remaining direct-measurement penalty from complement-credit errors.

No valid strict original source contraction or 470D signed cap can be
inferred from trace-only source data. Never 'PSD clip' an indefinite
Loewner lower without proving the resulting matrix remains <= H_C.
"""
import argparse,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
N=24
LABELS=("MG32_prefix_only","MG33_contiguous_0to8",
        "MG33_hybrid_with_MG19")

def psd_monotonicity_regression():
    """Exact PSD cone regression, including unsafe diagonal clipping.

    H=[[1,1],[1,1]] PSD, A=[[1,0],[0,0]] PSD,
    L=H-A=[[0,1],[1,1]] is a VALID lower of H but INDEFINITE.
    Replacing negative/zero *diagonal* of L by zero is NOT a valid
    Loewner lower. The vector v=[1,-1] annihilates H but its clipped
    diagonal mass is 1, violating the claimed lower inequality.
    Spectral positive-part clipping is also not universally Loewner
    admissible for a noncommuting H/L pair, and is NOT used here.
    """
    H=((F(1),F(1)),(F(1),F(1)))
    L=((F(0),F(1)),(F(1),F(1)))
    A=[[H[i][j]-L[i][j] for j in range(2)] for i in range(2)]
    assert A==[[F(1),F(0)],[F(0),F(0)]]
    assert L[0][0]*L[1][1]-L[0][1]**2 < 0
    v=(F(1),F(-1))
    q=lambda M:sum((v[i]*M[i][j]*v[j]
                     for i in range(2) for j in range(2)),F(0))
    clipped=((F(0),F(0)),(F(0),F(1)))
    assert q(H)==0 and q(clipped)==1
    # Conclude neither diagonal PSD clipping nor L_+ substitution
    # follows from L<=H and H>=0 alone.
    return True

def exact_bound_recombination(prefix_only,band_only,sites_only):
    """Use actual MG33 complete-original-frequency *upper traces*.

    Each inherited omitted-frequency upper matrix is a separately
    accepted bound for its own omitted set, hence also for any
    subsequent subset. Choosing minimum TRACE among these existing
    valid matrix bounds is mathematically allowed; this never means
    they are Loewner ordered by trace.
    """
    variants=(prefix_only,band_only,sites_only)
    assert tuple(x["variant"] for x in variants)==LABELS
    prefix={k:F(v) for k,v in
            prefix_only["frequency_contributions_upper_trace"].items()}
    band={k:F(v) for k,v in
          band_only["frequency_contributions_upper_trace"].items()}
    hybrid={k:F(v) for k,v in
            sites_only["frequency_contributions_upper_trace"].items()}
    assert set(prefix)=={"prefix"}
    assert set(band)=={"prefix","new_band"}
    assert set(hybrid)=={"prefix","new_band","MG19_panels"}
    assert prefix["prefix"]==band["prefix"]==hybrid["prefix"]
    assert band["new_band"]==hybrid["new_band"]
    measured=(prefix["prefix"],band["new_band"],hybrid["MG19_panels"])
    rem=[F(x["remaining_original_frequency_upper_trace"]) for x in variants]
    assert all(x>=0 for x in measured+tuple(rem))
    whole=[F(x["upper_trace"]) for x in variants]
    assert whole==[sum(measured[:j+1],F(0))+rem[j] for j in range(3)]
    assert all(x["complete_original_real_frequency_upper"] for x in variants)
    assert all(x["physical_disjoint_frequency_partition"] for x in variants)
    decisions=[]
    for j in range(3):
        valid_sources=list(range(j+1))
        chosen=min(valid_sources,key=lambda k:(rem[k],k))
        claimed=rem[chosen]+sum(measured[:j+1],F(0))
        original=whole[j]
        assert claimed<=original
        result={
          "frequency_set":LABELS[j],
          "measured_disjoint_joint_residual_upper_trace":str(
               sum(measured[:j+1],F(0))),
          "original_MG33_complete_frequency_upper_trace":str(original),
          "original_MG33_omitted_upper_trace":str(rem[j]),
          "original_valid_omitted_upper_sources":{
              LABELS[k]:str(rem[k]) for k in valid_sources},
          "selected_PSD_monotone_remainder_upper_from":LABELS[chosen],
          "selected_PSD_monotone_remainder_upper_trace":str(rem[chosen]),
          "selected_valid_complete_frequency_upper_trace":str(claimed),
          "rigorously_reduced_original_upper_trace":str(original-claimed),
          "no_partial_470D_spectral_conclusion":True,
          "original_source_B_held_fixed":True,
          "source_trace_not_Loewner_matrix_comparison":True,
          "PSD_frequency_remainder_inclusion_proves_validity":True}
        decisions.append(result)
    assert decisions[0]["selected_valid_complete_frequency_upper_trace"]==str(whole[0])
    assert all(F(decisions[j+1]["selected_PSD_monotone_remainder_upper_trace"])<=
               F(decisions[j]["selected_PSD_monotone_remainder_upper_trace"])
               for j in range(2))
    return decisions,measured,rem

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg33-json",required=True)
    p.add_argument("--verified-mg34-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg35_original_monotone_PSD_remainder_guard.json")
    a=p.parse_args()
    old=json.loads((ROOT/a.verified_mg33_json).read_text())
    audit=json.loads((ROOT/a.verified_mg34_json).read_text())
    assert psd_monotonicity_regression()
    assert old["status"]=="ORIGINAL_DISJOINT_THREE_SECTOR_JOINT_SOURCE_RESIDUAL_GATE"
    assert audit["status"]=="ORIGINAL_MG33_EXACT_MARGINAL_FREQUENCY_METHOD_DIAGNOSIS"
    assert old["canonical_W_ODD_NEG"]==audit["canonical_W_ODD_NEG"]=="OPEN"
    assert audit["verified_original_MG33_run"]==39462301107
    assert audit["original_MG33_output_artifact_id"]==12284751583
    assert old["MG19_selected_nonoverlapping_panels_after8"]==2
    assert old["all_real_frequency_sectors_disjoint_original_source"]
    assert old["remaining_all_original_frequencies_closed_by_physical_source_mass"]
    assert old["complete_original_SM41_strong_source_high_tails_paid"]
    assert len(old["original_rational_trial_cutoffs"])==2
    assert len(audit["original_rational_trial_marginals"])==4
    details=[]
    for scenario in old["original_rational_trial_cutoffs"]:
        assert scenario["cutoff_k"] in (12,16)
        assert len(scenario["trials"])==2
        for trial in scenario["trials"]:
            prev=next(row for row in audit["original_rational_trial_marginals"]
                      if row["cutoff_k"]==scenario["cutoff_k"]
                      and row["original_MG30_rational_trial"]==trial["trial_name"])
            variants=trial["all_three_rigorous_complete_frequency_variants"]
            decisions,measured,rem=exact_bound_recombination(*variants)
            # MG34 independently accepted all exact original trace deltas.
            first,second=prev["band_then_nonoverlap_original_site_marginals"]
            assert F(first["added_joint_residual_upper_trace"])==measured[1]
            assert F(second["added_joint_residual_upper_trace"])==measured[2]
            assert F(first["delta_unmeasured_residual_upper_trace"])==rem[1]-rem[0]
            assert F(second["delta_unmeasured_residual_upper_trace"])==rem[2]-rem[1]
            assert F(decisions[-1]["original_MG33_complete_frequency_upper_trace"])==(
                  F(prev["hybrid_upper_trace"]))
            # For each new band, all earlier full sets provide valid
            # *remainder* bounds by PSD frequency-measure inclusion.
            # This is a trace selection from valid Loewner uppers,
            # NOT evidence that the chosen full bounds are ordered.
            guarded=F(decisions[-1]["selected_valid_complete_frequency_upper_trace"])
            baseline=F(decisions[0]["selected_valid_complete_frequency_upper_trace"])
            details.append({
               "cutoff_k":scenario["cutoff_k"],
               "original_rational_trial":trial["trial_name"],
               "actual_original_true_23pluspole_24D":True,
               "signed_arch_plus_seven_prime_and_pole_preserved_by_inheritance":True,
               "same_exact_original_MG30_response_B_all_variants":True,
               "baseline_complete_upper_trace":str(baseline),
               "guarded_hybrid_complete_upper_trace":str(guarded),
               "guarded_hybrid_over_baseline_trace":str(guarded/baseline),
               "guarded_hybrid_beats_original_hybrid_trace":
                   guarded<F(prev["hybrid_upper_trace"]),
               "guarded_hybrid_beats_original_MG32_prefix_baseline":
                   guarded<baseline,
               "source_residual_gap_certified":False,
               "MG33_exact_full_matrix_Gershgorin_not_recomputed":True,
               "full_original_frequency_upper_trace_scenarios":decisions})
    assert len(details)==4
    out={
       "status":"ORIGINAL_MG35_PSD_MONOTONE_REMAINDER_UPPER_TRACE_GUARD",
       "canonical_W_ODD_NEG":"OPEN",
       "verified_original_MG33_run":39462301107,
       "verified_original_MG34_run":39467773045,
       "original_source_25physical_23adapted_plus_true_sinh_pole":True,
       "actual_original_true_joint_residual_pole_and_signed_multiplier_inherited":True,
       "actual_Fourier_measured_sectors_are_nested_disjoint":True,
       "actual_original_residual_remainder_covariance_PSD_monotonicity":True,
       "all_prior_verified_remainder_uppers_remain_valid_on_smaller_sets":True,
       "chosen_omitted_remainder_upper_is_existing_valid_Loewner_matrix":True,
       "selected_remainder_upper_trace_nonincreasing_with_added_frequency_sectors":True,
       "no_spectral_PSD_clipping_of_indefinite_Loewner_lower":True,
       "exact_2D_invalid_PSD_diagonal_clipping_regression":True,
       "all_four_original_rational_trial_cases_accounted_exactly":True,
       "PSD_safe_full_original_residual_upper_TRACE_only":True,
       "new_full_original_24D_matrix_Loewner_margin_tested":False,
       "source_residual_strict_positive_gap_certified":False,
       "original_470D_strong_inverse_certified":False,
       "signed_original_negative_51over56_cap_certified":False,
       "independent_original_Fourier_form_domain_audit":"OPEN",
       "even_Weil_CC27_RH":"OPEN",
       "scenarios":details,
       "next_method_gate":"Need genuine original PSD full 24D matrix upper selection/congruence and sharper actual [4,8] residual intervals; inherited old omitted residual bound alone cannot beat MG32 baseline after paying positive added-band residual upper."
    }
    target=ROOT/a.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("MG35 original PSD-monotone source remainder:",json.dumps({
      "scenarios":[{
        "k":x["cutoff_k"],"trial":x["original_rational_trial"],
        "baseline":float(F(x["baseline_complete_upper_trace"])),
        "guarded_hybrid":float(F(x["guarded_hybrid_complete_upper_trace"])),
        "hybrid_over_base":float(F(x["guarded_hybrid_over_baseline_trace"])),
        "new_better_than_old_baseline":x["guarded_hybrid_beats_original_MG32_prefix_baseline"]}
        for x in details],
      "full_original_470D_odd_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
