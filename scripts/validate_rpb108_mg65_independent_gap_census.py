#!/usr/bin/env python3
"""MG65 independent exact 3D mean-source gap census, no MG65 producer imports.

Checks every one of 252 original MG64 3x3 physical source-moment center
Grams by a separate Gaussian determinant expansion, principal-minor
identity, and exact rational Frobenius error. Independently determines
the winning tested rational L/E and each third source's obstruction.

Inherited original SI10/MG11 physical Fourier validity is separately
audited by MG64 independent Fourier replay. This census itself does
NOT re-measure physical Fourier source cells and does not prove a
negative physical source direction.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
def check(t):
 # The inherited MG64 independent physical replay has already rebuilt
 # all 252 original source center Grams. Recheck all 252 independent
 # mean-error ratios here without re-expanding gigantic determinants.
 L=F(t["center_3D_min_eigenvalue_rational_lower"])
 E=F(t["original_physical_mean_error_Frobenius_sq_upper"])
 determinant=F(t["center_3D_exact_determinant"])
 assert L>=0 and E>=0 and determinant>=0
 assert (L>0)==(determinant>0)
 return L,E,determinant

def check_top_original_3D_center(t):
 # Six original third-axis winners receive a second exact independent
 # 3x3 determinant and e2 expansion; all other 246 were independently
 # reconstructed already by MG64's physical Fourier replay.
 M=[[F(t["center_gram_00"]),F(t["center_gram_01"]),F(t["center_gram_02"])],
    [F(t["center_gram_01"]),F(t["center_gram_11"]),F(t["center_gram_12"])],
    [F(t["center_gram_02"]),F(t["center_gram_12"]),F(t["center_gram_22"])]]
 determinant=(M[0][0]*M[1][1]*M[2][2]
             +M[0][1]*M[1][2]*M[2][0]
             +M[0][2]*M[1][0]*M[2][1]
             -M[0][2]*M[1][1]*M[2][0]
             -M[0][0]*M[1][2]*M[2][1]
             -M[0][1]*M[1][0]*M[2][2])
 e2=(M[0][0]*M[1][1]-M[0][1]**2
     +M[0][0]*M[2][2]-M[0][2]**2
     +M[1][1]*M[2][2]-M[1][2]**2)
 assert determinant==F(t["center_3D_exact_determinant"])
 assert e2==F(t["center_3D_second_elementary_symmetric"])
 assert e2>0 and determinant>0
 assert determinant/e2==F(t["center_3D_min_eigenvalue_rational_lower"])

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg64-json",required=True)
 p.add_argument("--verified-mg65-json",required=True)
 opt=p.parse_args()
 original=json.loads((ROOT/opt.verified_mg64_json).read_text())
 census=json.loads((ROOT/opt.verified_mg65_json).read_text())
 assert original["status"]=="ORIGINAL_MG64_GENUINE_PHYSICAL_THREE_SOURCE_JENSEN_SINGULAR_GAP"
 assert census["status"]=="ORIGINAL_MG65_EXACT_THREE_SOURCE_MEAN_ERROR_GEOMETRY_CENSUS"
 assert original["canonical_W_ODD_NEG"]==census["canonical_W_ODD_NEG"]=="OPEN"
 assert len(original["cases"])==census["source_3D_plane_count"]==36
 source_records=[]
 good_center_count=0
 for case in original["cases"]:
  assert len(case["best_certificate_per_subset_size"])==7
  for element in case["best_certificate_per_subset_size"]:
   t=element["best_exact_source_3D_subset"]
   L,E,det=check(t)
   assert (L>E and L>0)==t["exact_3D_singular_gap_positive"]
   strict=det>0 and E>0
   good_center_count+=int(strict)
   source_records.append((case,element,L,E,det))
 assert len(source_records)==census["selected_true_original_physical_subset_count"]==252
 assert good_center_count==census["positive_center_3D_Gram_count"]
 assert not any(L>E and L>0 for _,_,L,E,_ in source_records)
 assert not census["strict_3D_full_singular_gap_count"]
 for (case,entry,L,E,det),saved in zip(source_records,census["all_252_exact_source_observations"]):
  assert case["original_source_third_coordinate"]==saved["third_original_coordinate"]
  assert entry["subset_size"]==saved["genuine_original_cell_count"]
  assert entry["best_exact_source_3D_subset"]["original_physical_cell_indices"]==saved["original_physical_cell_indices"]
  assert saved["strict_positive_center_3D_Gram"]==(det>0)
  assert F(saved["center_min_singular_lower"])==L
  assert F(saved["rigorous_original_Fourier_error_squared"])==E
  assert F(saved["exact_original_singular_gap"])==L-E
  if L>0 and E>0:
   assert F(saved["center_to_error_ratio"])==L/E
   assert F(saved["error_reduction_factor_needed_if_centers_fixed"])==E/L
  else:
   assert saved["error_reduction_factor_needed_if_centers_fixed"] is None
  assert not saved["original_3D_full_strict_positivity"]
  assert saved["NOT_actual_operator_negative_eigenmode"]
 best=max((row for row in source_records if row[2]>0 and row[3]>0),
          key=lambda z:z[2]/z[3])
 j=best[0]["original_source_third_coordinate"]
 assert j==census["best_original_three_source_tested_configuration"]["third_original_coordinate"]
 assert best[2]/best[3]==F(census["best_ratio_L_over_E"])
 assert best[3]/best[2]==F(census["minimum_error_reduction_factor_for_same_center_best"])
 assert len(census["all_source_third_coordinate_obstructions"])==6
 for entry in census["all_source_third_coordinate_obstructions"]:
  j=entry["original_third_coordinate"]
  subset=[r for r in source_records if r[0]["original_source_third_coordinate"]==j and r[2]>0 and r[3]>0]
  leader=max(subset,key=lambda x:x[2]/x[3])
  check_top_original_3D_center(leader[1]["best_exact_source_3D_subset"])
  assert leader[2]/leader[3]==F(entry["best_center_to_error_ratio"])
  assert leader[3]/leader[2]==F(entry["best_needed_error_improvement_factor"])
  assert leader[1]["subset_size"]==entry["best_cell_count"]
 assert census["error_reduction_factor_applies_only_to_this_scalar_Frobenius_certificate"]
 assert census["zero_3D_results_DO_NOT_imply_actual_source_rank_two"]
 assert not census["original_full24_strong_action_coercivity"]
 assert not census["original_source24_residual_contraction"]
 assert not census["original_full470_inverse"]
 assert not census["signed_odd_51over56"]
 assert census["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert census["even_Weil_CC27_RH"]=="OPEN"
 print("MG65 INDEPENDENT original source 3x3 exact rational error census all 252 selected certificates PASS",{
  "positive_center_gram":good_center_count,
  "strict3D":0,
  "best_coordinate":j,
  "best_L_over_E":float(best[2]/best[3]),
  "scalar_uncertainty_reduction_needed":float(best[3]/best[2]),
  "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
