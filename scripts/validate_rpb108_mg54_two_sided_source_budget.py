#!/usr/bin/env python3
"""MG54 — exact two-sided fixed-source certificate budget obstruction.

Original physical source 24D accepted MG53 decomposes true all-frequency
residual upper U52=D_0to8+R_gt8. The TWO independently valid positive-
semidefinite original source covariance uppers each exceed Hlo on
MG43's previously certified rational witness.

Therefore with the original response B and EITHER one accepted
fixed upper intact, NO optimization of only the other independently
positive semidefinite source upper can yield Hlo-U > 0.

The 2D alpha/beta feasible triangle is a nonphysical mathematical
budget: scaling existing uppers is NOT claimed to preserve Loewner
coverage of the original physical operator.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import deserialize,original_H24_from_physical_source
from validate_rpb108_mg25_robust_source_aware_residual import Id,T,sub,plus,mul
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
N=24
def mat(x):
 a=deserialize(x)
 assert len(a)==N and all(len(row)==N for row in a)
 return a
def ray(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def exact_psd(A):
 """Symmetric pivot-free exact rational LDL PSD (zero pivot requires zero row)."""
 assert A==T(A)
 m=[list(row) for row in A]
 for j in range(N):
  d=m[j][j]
  assert d>=0
  if d==0:
   assert all(m[j][k]==0 for k in range(j+1,N))
   continue
  for i in range(j+1,N):
   for k in range(i,N):
    m[i][k]-=m[j][i]*m[j][k]/d
    m[k][i]=m[i][k]
 return True
def classification(A):
 name,witness=classify_ideal(A)
 assert name in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH","POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
 if name=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  w=[Q(x) for x in witness["rational_vector"]]
  assert ray(w,A)==Q(witness["exact_negative_quadratic"])<0
 return name,witness
def main():
 p=argparse.ArgumentParser()
 for z in ("mg24","mg47","mg52","mg53"):
  p.add_argument("--verified-"+z+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg54_original_two_sided_certificate_budget.json")
 args=p.parse_args()
 load=lambda z:json.loads((ROOT/getattr(args,"verified_"+z+"_json")).read_text())
 a24,a47,a52,a53=[load(z) for z in ("mg24","mg47","mg52","mg53")]
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in (a24,a47,a52,a53))
 assert a53["status"]=="ORIGINAL_MG53_FIXED_SOURCE_DIRECT_BAND_ZERO_CEILING"
 assert a52["status"]=="ORIGINAL_MG52_COUPLED_4TO8_MULTIPLIER_VECTOR_CANCELLATION_24D"
 hm,hr,err=original_H24_from_physical_source()
 assert err==Q(a24["physical_Gram_Loewner_row_error"])
 Hlo=sub(hm,mul(err,Id(N)))
 results=[]
 for s47,s52,s53 in zip(a47["scenarios"],a52["cases"],a53["cases"]):
  mesh,k=s53["mesh_cells"],s53["cutoff_k"]
  assert (mesh,k)==(s47["mesh_cells"],s47["cutoff_k"])==(s52["mesh_cells"],s52["cutoff_k"])
  assert Hlo==mat(s53["full_original_H_lower"])
  D0=mat(s53["accepted_MG32_true_direct_0to4_upper"])
  D1=mat(s53["MG52_true_direct_4to8_upper"])
  D=plus(D0,D1)
  R=mat(s53["fixed_8to_infinity_remaining_upper"])
  U=mat(s53["accepted_MG52_complete_upper"])
  assert plus(D,R)==U
  assert U==mat(s52["MG52_best_original_whole_24D_upper"])
  assert exact_psd(D0) and exact_psd(D1)
  assert exact_psd(D) and exact_psd(R)
  original=[Q(x) for x in s47["selected_exact_inertia_witness"]["rational_vector"]]
  assert [str(x) for x in original]==s53["exact_rational_MG43_witness"]
  assert ray(original,sub(Hlo,mat(s47["selected_complete_24D_source_upper"])))==Q(
    s47["selected_exact_inertia_witness"]["exact_negative_quadratic"])<0
  h=ray(original,Hlo);d=ray(original,D);r=ray(original,R)
  assert h>0 and d>h and r>h
  assert ray(original,sub(Hlo,U))==h-d-r
  assert ray(original,sub(Hlo,D))==h-d<0
  assert ray(original,sub(Hlo,R))==h-r<0
  assert ray(original,sub(Hlo,R))==Q(s53["same_ray_counterfactual_both_bands_ZERO_ceiling"])
  assert ray(original,D)==Q(s53["direct_0to4_ray_upper_charge"])+Q(s53["direct_4to8_ray_upper_charge"])
  # The necessary scalar *counterfactual* feasibility region is
  # alpha*d+beta*r < h; alpha,beta in [0,1]. No such scaling
  # is ever advertised as a valid physical residual estimate.
  ci_D,wi_D=classification(sub(Hlo,D))
  ci_R,wi_R=classification(sub(Hlo,R))
  assert ci_D==ci_R=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
  outcomes={
     "mesh_cells":mesh,"cutoff_k":k,
     "original_MG43_accepted_source_rational_ray":[str(z) for z in original],
     "source_Gram_Hlo_on_ray":str(h),
     "source_direct_0to8_upper_on_ray":str(d),
     "source_remaining_gt8_upper_on_ray":str(r),
     "source_full_upper_on_ray":str(d+r),
     "actual_source_lower_on_ray":str(h-d-r),
     "hypothetical_ZERO_remainder_source_lower_on_ray":str(h-d),
     "hypothetical_ZERO_direct_source_lower_on_ray":str(h-r),
     "minimum_direct_upper_reduction_at_ZERO_remainder":str(d-h),
     "minimum_remaining_upper_reduction_at_ZERO_direct":str(r-h),
     "necessary_direct_retention_factor_at_ZERO_remainder":str(h/d),
     "necessary_remaining_retention_factor_at_ZERO_direct":str(h/r),
     "necessary_equal_both_retention_factor":str(h/(d+r)),
     "necessary_equal_both_fraction_reduction":str(1-h/(d+r)),
     "counterfactual_2D_frontier_intercepts":{
         "alpha_at_beta_zero":str(h/d),"beta_at_alpha_zero":str(h/r)},
     "hypothetical_zero_remainder_full24_matrix_classification":ci_D,
     "hypothetical_zero_remainder_full24_matrix_witness":wi_D,
     "hypothetical_zero_direct_full24_matrix_classification":ci_R,
     "hypothetical_zero_direct_full24_matrix_witness":wi_R,
     "original_direct_and_remaining_full24_rational_PSD":True,
     "fixed_original_B":s53["original_24D_genuine_source_response_B"],
     "all_zero_or_scale_models_NONPHYSICAL_NOT_CERTIFICATES":True,
     "fixed_B_and_other_block_only_no_go":True,
     "alternative_B_and_whole_frequency_joint_bound_NOT_ruled_out":True,
     "no_original_true_operator_negative_direction_claim":True,
  }
  results.append(outcomes)
  print("MG54 source split",mesh,k,{
   "Hlo":float(h),"direct":float(d),"remaining":float(r),
   "both_equal_fraction_must_not_exceed":float(h/(d+r)),
   "direct_only_fix_impossible":h-r<0,
   "remaining_only_fix_impossible":h-d<0},flush=True)
 assert len(results)==4
 report={
   "status":"ORIGINAL_MG54_TWO_SIDED_FIXED_SOURCE_BUDGET_OBSTRUCTION",
   "canonical_W_ODD_NEG":"OPEN",
   "input_runs":{"MG24":39378465438,"MG47":39663431182,
                 "MG52":39813976498,"MG53":39886275002},
   "all_four_cases_exact_rational_two_sided_obstructions":True,
   "both_original_full24_source_component_upper_matrices_rational_PSD":True,
   "no_new_actual_original_Fourier_data":True,
   "all_counterfactual_scalings_clearly_NOT_valid_operator_uppers":True,
   "any_original_24D_contraction":False,
   "original_470D_inverse":False,
   "original_signed_51over56_odd_cap":False,
   "independent_original_Fourier_form_domain_audit":"OPEN",
   "even_Weil_CC27_RH":"OPEN",
   "cases":results
 }
 out=ROOT/args.output;out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(report,indent=2)+"\n")
 print("MG54 four-case two-sided exact source decomposition GENERATED",
      {"cases":len(results),"470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
