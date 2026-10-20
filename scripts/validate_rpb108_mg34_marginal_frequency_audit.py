#!/usr/bin/env python3
"""MG34: exact original marginal-frequency residual cost and PSD-mass-credit gate.

Consume the independently accepted MG33 artifact, never floating
recalculate a physical Fourier integral. For all four original
MG30 trial/cutoff scenarios, decompose each change in the rigorous
FULL-FREQUENCY residual UPPER TRACE into

 delta whole = measured added band residual upper trace
                    + change of unmeasured-frequency upper trace.

On the same B and source basis, separately measure the exact
Gershgorin margin change. The two criteria are not equivalent:
a lower trace can coexist with a WORSE sufficient PSD margin.

MG33's sourcewise Young lower for the new measured physical source
mass need not be PSD; an increased complement upper trace after
shrinking the genuinely omitted region is a METHOD budget defect,
not a negative mass or a negative true operator.

This audit is a necessary MG35 method-selection gate, not a new
spectral theorem, positivity, original 470D inverse, or RH proof.
"""
import argparse,json,sys
from fractions import Fraction as Q
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

ROOT=Path(__file__).resolve().parents[1]
TYPES=("MG32_prefix_only","MG33_contiguous_0to8","MG33_hybrid_with_MG19")
STEP_NAMES=("add_contiguous_4to8","add_disjoint_MG19_after8")

def decompose(x,y,added):
    old=Q(x["upper_trace"])
    new=Q(y["upper_trace"])
    rold=Q(x["remaining_original_frequency_upper_trace"])
    rnew=Q(y["remaining_original_frequency_upper_trace"])
    oc=x["frequency_contributions_upper_trace"]
    nc=y["frequency_contributions_upper_trace"]
    assert "prefix" in oc and oc["prefix"]==nc["prefix"]
    assert Q(x["remaining_fraction_of_total_upper_trace"])==rold/old
    assert Q(y["remaining_fraction_of_total_upper_trace"])==rnew/new
    assert added in nc and added not in oc
    # Every region retained unchanged in the later branch.
    assert all(nc[k]==v for k,v in oc.items())
    newmeasured=Q(nc[added])
    delta_rem=rnew-rold
    delta_total=new-old
    assert delta_total==newmeasured+delta_rem
    g0=Q(x["strict_Gershgorin_margin"])
    g1=Q(y["strict_Gershgorin_margin"])
    delta_g=g1-g0
    return {
       "added_original_frequency_sector":added,
       "added_joint_residual_upper_trace":str(newmeasured),
       "delta_unmeasured_residual_upper_trace":str(delta_rem),
       "delta_complete_residual_upper_trace":str(delta_total),
       "independent_rational_trace_balance_exact":True,
       "remaining_upper_trace_increased_despite_fewer_unmeasured_frequencies":
           delta_rem>0,
       "strict_trace_improvement":delta_total<0,
       "Gershgorin_margin_change":str(delta_g),
       "strict_Gershgorin_improvement":delta_g>0,
       "strict_source_residual_contraction_after_step":g1>0,
       "trace_and_Gershgorin_order_not_equivalent":True,
       "band_measurement_not_a_negative_operator_witness":True}

def analyze(data):
    assert data["status"]=="ORIGINAL_DISJOINT_THREE_SECTOR_JOINT_SOURCE_RESIDUAL_GATE"
    assert data["canonical_W_ODD_NEG"]=="OPEN"
    assert data["verified_MG19_run_id"]==39363425186
    assert data["verified_MG24_run_id"]==39378465438
    assert data["verified_MG29_run_id"]==39440914565
    assert data["verified_MG30_run_id"]==39442984941
    assert data["verified_MG32_run_id"]==39459624082
    assert data["true_original_source_SI10_25physical_23pluspole_dimension24"]
    assert data["all_real_frequency_sectors_disjoint_original_source"]
    assert data["entire_MG32_original_32_cell_baseline_replayed_exactly"]
    assert data["remaining_all_original_frequencies_closed_by_physical_source_mass"]
    assert data["complete_original_SM41_strong_source_high_tails_paid"]
    assert data["MG19_selected_nonoverlapping_panels_after8"]==2
    assert [c["cutoff_k"] for c in data["original_rational_trial_cutoffs"]]==[12,16]
    diag=[]
    for c in data["original_rational_trial_cutoffs"]:
        assert len(c["trials"])==2
        for t in c["trials"]:
            v=t["all_three_rigorous_complete_frequency_variants"]
            assert [x["variant"] for x in v]==list(TYPES)
            a,b,d=v
            assert a["physical_disjoint_frequency_partition"]
            assert b["physical_disjoint_frequency_partition"]
            assert d["physical_disjoint_frequency_partition"]
            assert all(x["complete_original_real_frequency_upper"] for x in v)
            stages=[
                decompose(a,b,"new_band"),
                decompose(b,d,"MG19_panels")]
            assert Q(stages[0]["delta_complete_residual_upper_trace"])+Q(
                   stages[1]["delta_complete_residual_upper_trace"])==(
                   Q(d["upper_trace"])-Q(a["upper_trace"]))
            assert Q(stages[0]["Gershgorin_margin_change"])+Q(
                   stages[1]["Gershgorin_margin_change"])==(
                   Q(d["strict_Gershgorin_margin"])-
                   Q(a["strict_Gershgorin_margin"]))
            assert Q(t["hybrid_upper_trace_over_baseline"])==(
                Q(d["upper_trace"])/Q(a["upper_trace"]))
            assert Q(t["hybrid_Gershgorin_improvement_vs_MG32"])==(
                Q(d["strict_Gershgorin_margin"])-
                Q(a["strict_Gershgorin_margin"]))
            diag.append({
              "cutoff_k":c["cutoff_k"],
              "original_MG30_rational_trial":t["trial_name"],
              "true_original_23pluspole_and_complete_frequency":True,
              "source_Fourier_operator_spectrum_not_classified":True,
              "MG32_baseline_upper_trace":a["upper_trace"],
              "MG32_baseline_Gershgorin_margin":a["strict_Gershgorin_margin"],
              "hybrid_upper_trace":d["upper_trace"],
              "hybrid_Gershgorin_margin":d["strict_Gershgorin_margin"],
              "band_then_nonoverlap_original_site_marginals":stages})
    assert len(diag)==4
    band=[x["band_then_nonoverlap_original_site_marginals"][0] for x in diag]
    sites=[x["band_then_nonoverlap_original_site_marginals"][1] for x in diag]
    out={
      "status":"ORIGINAL_MG33_EXACT_MARGINAL_FREQUENCY_METHOD_DIAGNOSIS",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_original_MG33_run":39462301107,
      "original_MG33_output_artifact_id":12284751583,
      "source_basis_true_25physical_23pluspole":True,
      "all_trial_response_matrices_held_fixed_across_frequency_variants":True,
      "three_original_complete_frequency_source_bounds_compared":True,
      "exact_additive_measured_vs_complement_trace_decomposition":True,
      "Gershgorin_source_metric_acceptance_separate_from_trace":True,
      "strict_24D_source_contraction_in_any_test":any(
          s["strict_source_residual_contraction_after_step"]
          for row in diag for s in row["band_then_nonoverlap_original_site_marginals"]),
      "new_4to8_band_complement_upper_trace_increased_in_all_trials":
          all(s["remaining_upper_trace_increased_despite_fewer_unmeasured_frequencies"]
              for s in band),
      "new_4to8_band_gave_strict_trace_improvement_in_any_trial":
          any(s["strict_trace_improvement"] for s in band),
      "two_MG19_original_nonflat_panels_gave_strict_trace_improvement_in_all_trials":
          all(s["strict_trace_improvement"] for s in sites),
      "two_MG19_panels_gave_Gershgorin_improvement_in_any_trial":
          any(s["strict_Gershgorin_improvement"] for s in sites),
      "next_method_gate":"Reject automatic band extension. Certify a PSD-safe source mass credit (do not subtract an indefinite sourcewise-Young mass lower as though it were positive). Separately reduce joint measured-band residual width before expanding more frequencies; compare Loewner-matrix residual, not just trace.",
      "original_470D_strong_inverse_proved":False,
      "signed_original_51over56_negative_cap_proved":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "original_rational_trial_marginals":diag}
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg33-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg34_original_frequency_marginal_diagnostics.json")
    a=p.parse_args()
    d=json.loads((ROOT/a.verified_mg33_json).read_text())
    out=analyze(d)
    target=ROOT/a.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("MG34 original full-frequency marginal accounting:",json.dumps({
      "four_cases":[{
         "k":x["cutoff_k"],"trial":x["original_MG30_rational_trial"],
         "stages":[{
           "sector":s["added_original_frequency_sector"],
           "new_measured":float(Q(s["added_joint_residual_upper_trace"])),
           "remainder_change":float(Q(s["delta_unmeasured_residual_upper_trace"])),
           "whole_change":float(Q(s["delta_complete_residual_upper_trace"])),
           "Gersh_change":float(Q(s["Gershgorin_margin_change"]))}
           for s in x["band_then_nonoverlap_original_site_marginals"]]}
         for x in out["original_rational_trial_marginals"]],
      "strict":out["strict_24D_source_contraction_in_any_test"],
      "470D_odd_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
