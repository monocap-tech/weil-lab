#!/usr/bin/env python3
"""MG54 independently reconstructed exact rational two-sided source budget.

Authorially independent of the MG54 producer. Rebuild full original
source Gram, MG32/MG52 direct source covariance upper, MG52 remaining
|xi|>8 upper and the original MG43 negative rational test ray from
pinned archives. Exact LDL proves each block PSD and exact rational
arithmetic checks feasibility-frontier intercepts and invalid
counterfactual 24D negative-witness classifications. No new operator
sign statement, no new physical residual bound.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
N=24
def rd(a):
 z=[[Q(x) for x in row] for row in a]
 assert len(z)==N and all(len(row)==N for row in z)
 return z
def trans(A):return [list(v) for v in zip(*A)]
def scale(k,A):return [[k*x for x in r] for r in A]
def add(A,B):return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]
def sub(A,B):return add(A,scale(-1,B))
def eye():return [[Q(i==j) for j in range(N)] for i in range(N)]
def qf(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def psd(A):
 assert A==trans(A)
 mat=[row[:] for row in A]
 for j in range(N):
  p=mat[j][j]
  assert p>=0
  if p==0:
   assert all(mat[j][i]==0 for i in range(j+1,N))
   continue
  for i in range(j+1,N):
   for k in range(i,N):
    mat[i][k]-=mat[j][i]*mat[j][k]/p
    mat[k][i]=mat[i][k]
 return True
def negative_cert(A,t,wit):
 assert t=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
 v=[Q(x) for x in wit["rational_vector"]]
 assert any(v) and len(v)==N
 assert qf(v,A)==Q(wit["exact_negative_quadratic"])<0
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg46","mg47","mg50","mg52","mg53","mg54"):
  p.add_argument("--verified-"+k+"-json",required=True)
 args=p.parse_args()
 d={k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
    for k in ("mg24","mg46","mg47","mg50","mg52","mg53","mg54")}
 result=d["mg54"]
 assert result["status"]=="ORIGINAL_MG54_TWO_SIDED_FIXED_SOURCE_BUDGET_OBSTRUCTION"
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in d.values())
 hm,hr,he=original_H24_from_physical_source()
 assert he==Q(d["mg24"]["physical_Gram_Loewner_row_error"])
 Hlo=sub(hm,scale(he,eye()))
 seen=0
 for s46,s47,s50,s52,s53,s54 in zip(d["mg46"]["scenarios"],
                                      d["mg47"]["scenarios"],
                                      d["mg50"]["cases"],d["mg52"]["cases"],
                                      d["mg53"]["cases"],result["cases"]):
  mesh,k=s54["mesh_cells"],s54["cutoff_k"]
  assert all((mesh,k)==(r["mesh_cells"],r["cutoff_k"]) for r in (s46,s47,s50,s52,s53))
  D0=rd(s46["original_MG32_direct_band_24D_upper"])
  D1=rd(s52["MG52_samecell_new_4to8_upper"])
  D=add(D0,D1)
  oldD=rd(s50["actual_0to8_original_direct_24D_upper"])
  assert D==sub(oldD,rd(s52["PSD_direct_upper_reduction"]))
  U=rd(s52["MG52_best_original_whole_24D_upper"])
  R=sub(U,D)
  assert R==rd(s53["fixed_8to_infinity_remaining_upper"])
  assert D0==rd(s53["accepted_MG32_true_direct_0to4_upper"])
  assert D1==rd(s53["MG52_true_direct_4to8_upper"])
  assert Hlo==rd(s53["full_original_H_lower"])
  assert rd(s54["fixed_original_B"])==rd(s47["full_original_rational_response_B"])
  assert psd(D0) and psd(D1) and psd(D) and psd(R)
  v=[Q(x) for x in s47["selected_exact_inertia_witness"]["rational_vector"]]
  assert v==[Q(x) for x in s53["exact_rational_MG43_witness"]]
  assert v==[Q(x) for x in s54["original_MG43_accepted_source_rational_ray"]]
  negative_cert(sub(Hlo,rd(s47["selected_complete_24D_source_upper"])),
                "NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                s47["selected_exact_inertia_witness"])
  h=qf(v,Hlo);dx=qf(v,D);rx=qf(v,R)
  assert 0<h<dx and h<rx
  check={
   "source_Gram_Hlo_on_ray":h,
   "source_direct_0to8_upper_on_ray":dx,
   "source_remaining_gt8_upper_on_ray":rx,
   "source_full_upper_on_ray":dx+rx,
   "actual_source_lower_on_ray":h-dx-rx,
   "hypothetical_ZERO_remainder_source_lower_on_ray":h-dx,
   "hypothetical_ZERO_direct_source_lower_on_ray":h-rx,
   "minimum_direct_upper_reduction_at_ZERO_remainder":dx-h,
   "minimum_remaining_upper_reduction_at_ZERO_direct":rx-h,
   "necessary_direct_retention_factor_at_ZERO_remainder":h/dx,
   "necessary_remaining_retention_factor_at_ZERO_direct":h/rx,
   "necessary_equal_both_retention_factor":h/(dx+rx),
   "necessary_equal_both_fraction_reduction":1-h/(dx+rx),
  }
  for key,value in check.items():assert Q(s54[key])==value,key
  assert Q(s54["counterfactual_2D_frontier_intercepts"]["alpha_at_beta_zero"])==h/dx
  assert Q(s54["counterfactual_2D_frontier_intercepts"]["beta_at_alpha_zero"])==h/rx
  assert Q(s53["same_ray_counterfactual_both_bands_ZERO_ceiling"])==h-rx
  assert Q(s53["actual_valid_MG52_negative_MG43_source_ray"])==h-dx-rx
  assert s54["hypothetical_zero_remainder_full24_matrix_classification"]=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
  assert s54["hypothetical_zero_direct_full24_matrix_classification"]=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
  negative_cert(sub(Hlo,D),s54["hypothetical_zero_remainder_full24_matrix_classification"],s54["hypothetical_zero_remainder_full24_matrix_witness"])
  negative_cert(sub(Hlo,R),s54["hypothetical_zero_direct_full24_matrix_classification"],s54["hypothetical_zero_direct_full24_matrix_witness"])
  assert s54["original_direct_and_remaining_full24_rational_PSD"]
  assert s54["all_zero_or_scale_models_NONPHYSICAL_NOT_CERTIFICATES"]
  assert s54["fixed_B_and_other_block_only_no_go"]
  assert s54["alternative_B_and_whole_frequency_joint_bound_NOT_ruled_out"]
  assert s54["no_original_true_operator_negative_direction_claim"]
  seen+=1
 assert seen==4 and result["all_four_cases_exact_rational_two_sided_obstructions"]
 assert result["both_original_full24_source_component_upper_matrices_rational_PSD"]
 assert result["all_counterfactual_scalings_clearly_NOT_valid_operator_uppers"]
 assert not result["any_original_24D_contraction"]
 assert not result["original_470D_inverse"]
 assert not result["original_signed_51over56_odd_cap"]
 assert result["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert result["even_Weil_CC27_RH"]=="OPEN"
 print("MG54 INDEPENDENT exact original two-sided source certificate PSD budget PASS",
       {"cases":seen,"direct_only_and_remainder_only_repair":"PROVED IMPOSSIBLE IN FIXED FAMILY",
        "genuine_original_operator_negative_index":"NOT CLAIMED","RH":"OPEN"},flush=True)
if __name__=="__main__":main()
