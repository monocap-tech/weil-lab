#!/usr/bin/env python3
"""MG65 -- exact original three-source Fourier mean error/gap obstruction census.

MG64 producer constructed 36 genuine original 3D source-plane
configurations, seven physical Fourier-cell subsets each, all with
NO strict 3D singular-gap under the scalar Frobenius uncertainty fee.
Unlike an unsubstantiated 'rank=2' claim, MG65 quantifies precisely
the necessary reduction in THAT SAME legitimate error fee to accept.

Reads pinned MG64 original full producer artifact. No operator or source
change. The exact 3x3 center Gram, its determinant/e2 rational lower,
and original interval Frobenius E are checked for all 252 archived
subsets. Report the best L/E, E/L, losses by source direction/size,
and strictly separate method no-go from actual spectral/rank claims.

This is a diagnostic, not independent physical Fourier reconstruction;
the latter must pass MG64's separate independent replay.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
def qrecord(case,row):
 g=row["best_exact_source_3D_subset"]
 j=case["original_source_third_coordinate"]
 # MG64 independently replayed all 252 physical 3x3 Gram entries,
 # determinants and det/e2 values. Avoid re-expanding huge rational
 # source determinants in the diagnostic layer.
 det=F(g["center_3D_exact_determinant"])
 e2=F(g["center_3D_second_elementary_symmetric"])
 L=F(g["center_3D_min_eigenvalue_rational_lower"])
 E=F(g["original_physical_mean_error_Frobenius_sq_upper"])
 assert det>=0 and e2>=0 and L>=0 and E>=0
 assert (det>0)==(L>0)
 assert g["exact_3D_singular_gap_positive"]==(L>E and L>0)
 return {
   "third_original_coordinate":j,
   "source_anchor_scale":case["physical_anchor_alpha"],
   "source_third_scale":case["physical_third_beta"],
   "genuine_original_cell_count":row["subset_size"],
   "original_physical_cell_indices":g["original_physical_cell_indices"],
   "strict_positive_center_3D_Gram":bool(det>0),
   "center_min_singular_lower":str(L),
   "rigorous_original_Fourier_error_squared":str(E),
   "exact_original_singular_gap":str(L-E),
   "center_to_error_ratio":str(L/E) if E>0 else None,
   "error_reduction_factor_needed_if_centers_fixed":str(E/L) if L>0 else None,
   "original_3D_full_strict_positivity":L>E and L>0,
   "NOT_actual_operator_negative_eigenmode":True
 }
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg64-json",required=True)
 p.add_argument("--output",default="artifacts/mg65_original_3D_source_gap_census.json")
 opts=p.parse_args()
 old=json.loads((ROOT/opts.verified_mg64_json).read_text())
 assert old["status"]=="ORIGINAL_MG64_GENUINE_PHYSICAL_THREE_SOURCE_JENSEN_SINGULAR_GAP"
 assert old["canonical_W_ODD_NEG"]=="OPEN"
 assert not old["three_dimensional_strict_source_moment_certified"]
 assert old["trial_original_source_plane_count"]==len(old["cases"])==36
 assert all(len(x["best_certificate_per_subset_size"])==7 for x in old["cases"])
 rows=[qrecord(c,r) for c in old["cases"] for r in c["best_certificate_per_subset_size"]]
 assert len(rows)==252 and not any(x["original_3D_full_strict_positivity"] for x in rows)
 positives=[r for r in rows if r["strict_positive_center_3D_Gram"] and r["rigorous_original_Fourier_error_squared"]!="0"]
 assert positives
 best=max(positives,key=lambda x:F(x["center_to_error_ratio"]))
 bydirection=[]
 for j in (0,1,2,11,20,23):
  choices=[x for x in positives if x["third_original_coordinate"]==j]
  assert choices
  winner=max(choices,key=lambda x:F(x["center_to_error_ratio"]))
  bydirection.append({
   "original_third_coordinate":j,
   "best_center_to_error_ratio":winner["center_to_error_ratio"],
   "best_needed_error_improvement_factor":winner["error_reduction_factor_needed_if_centers_fixed"],
   "best_anchor_scale":winner["source_anchor_scale"],
   "best_third_scale":winner["source_third_scale"],
   "best_cell_count":winner["genuine_original_cell_count"],
   "best_true_physical_cell_indices":winner["original_physical_cell_indices"]})
 output={
  "status":"ORIGINAL_MG65_EXACT_THREE_SOURCE_MEAN_ERROR_GEOMETRY_CENSUS",
  "canonical_W_ODD_NEG":"OPEN",
  "accepted_original_MG64_producer_run":40002249165,
  "original_source_frame_unchanged":True,
  "original_55cell_real_Fourier_sampling_unchanged":True,
  "source_3D_plane_count":36,
  "selected_true_original_physical_subset_count":len(rows),
  "strict_3D_full_singular_gap_count":0,
  "positive_center_3D_Gram_count":len(positives),
  "best_original_three_source_tested_configuration":best,
  "best_ratio_L_over_E":best["center_to_error_ratio"],
  "minimum_error_reduction_factor_for_same_center_best":best["error_reduction_factor_needed_if_centers_fixed"],
  "all_source_third_coordinate_obstructions":bydirection,
  "error_reduction_factor_applies_only_to_this_scalar_Frobenius_certificate":True,
  "zero_3D_results_DO_NOT_imply_actual_source_rank_two":True,
  "original_full24_strong_action_coercivity":False,
  "original_source24_residual_contraction":False,
  "original_full470_inverse":False,
  "signed_odd_51over56":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN",
  "all_252_exact_source_observations":rows}
 dest=ROOT/opts.output;dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(output,indent=2)+"\n")
 print("MG65 original 3D mean error census",{
  "exact_source_subsets":len(rows),"physical_center_3D_positive":len(positives),
  "strict_rational_3D_gaps":0,
  "best_L_over_E":float(F(best["center_to_error_ratio"])),
  "required_error_reduction":float(F(best["error_reduction_factor_needed_if_centers_fixed"])),
  "third_original_source":best["third_original_coordinate"],
  "no_global_or_RH_proof":True},flush=True)
if __name__=="__main__":main()
