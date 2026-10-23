#!/usr/bin/env python3
"""MG53 independent original fixed-remnant direct-only impossibility replay.

No import of MG53 producer. Rebuild complete original Gram lower and
real physical MG32/MG52 direct source uppers from independently accepted
archived matrices. Verify PSD by exact rational symmetric LDL (allow zero
pivots only with a zero remaining row), then calculate exact counterfactual
zero-direct original source lower on the original MG43 rational witness.
No zero-band variant is a valid physical operator upper!
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
N=24
def rd(x):
 z=[[Q(v) for v in row] for row in x]
 assert len(z)==N and all(len(row)==N for row in z)
 return z
def transpose(a):return [list(col) for col in zip(*a)]
def plus(a,b):return [[u+v for u,v in zip(row1,row2)] for row1,row2 in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
def sub(a,b):return plus(a,scale(-1,b))
def ident():return [[Q(i==j) for j in range(N)] for i in range(N)]
def quadratic(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def trace(a):return sum((a[i][i] for i in range(N)),Q(0))
def verify_psd(A):
 A=[row[:] for row in A]
 assert A==transpose(A)
 for k in range(N):
  d=A[k][k]
  if d==0:
   assert all(A[k][j]==0 for j in range(k+1,N))
   continue
  assert d>0
  for i in range(k+1,N):
   for j in range(i,N):
    A[i][j]-=A[k][i]*A[k][j]/d
    A[j][i]=A[i][j]
 return True
def verify_exact_negative_report(a,typ,info):
 if typ=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  w=[Q(x) for x in info["rational_vector"]]
  assert len(w)==N and any(w)
  assert quadratic(w,a)==Q(info["exact_negative_quadratic"])<0
 elif typ=="POSITIVE_EXACT_RATIONAL_LDL":
  mat=[r[:] for r in a]
  for k in range(N):
   d=mat[k][k]
   assert d>0
   for i in range(k+1,N):
    for j in range(i,N):
     mat[i][j]-=mat[k][i]*mat[k][j]/d
     mat[j][i]=mat[i][j]
 else:
  assert typ=="INCONCLUSIVE"
def run(d):
 obj=d["mg53"]
 assert obj["status"]=="ORIGINAL_MG53_FIXED_SOURCE_DIRECT_BAND_ZERO_CEILING"
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in d.values())
 hm,hr,he=original_H24_from_physical_source()
 assert he==Q(d["mg24"]["physical_Gram_Loewner_row_error"])
 Hlo=sub(hm,scale(he,ident()))
 num=0;zero_new=0;zero_both=0
 for s46,s47,s50,s52,s53 in zip(d["mg46"]["scenarios"],d["mg47"]["scenarios"],
                         d["mg50"]["cases"],d["mg52"]["cases"],obj["cases"]):
  mesh,k=s53["mesh_cells"],s53["cutoff_k"]
  assert (mesh,k)==(s46["mesh_cells"],s46["cutoff_k"])==(s47["mesh_cells"],s47["cutoff_k"])==(s50["mesh_cells"],s50["cutoff_k"])==(s52["mesh_cells"],s52["cutoff_k"])
  assert rd(s53["original_24D_genuine_source_response_B"])==rd(s47["full_original_rational_response_B"])
  assert rd(s53["full_original_H_lower"])==Hlo
  whole=rd(s52["MG52_best_original_whole_24D_upper"])
  assert whole==rd(s53["accepted_MG52_complete_upper"])
  direct0=rd(s46["original_MG32_direct_band_24D_upper"])
  direct8=rd(s52["MG52_samecell_new_4to8_upper"])
  assert direct0==rd(s53["accepted_MG32_true_direct_0to4_upper"])
  assert direct8==rd(s53["MG52_true_direct_4to8_upper"])
  assert verify_psd(direct0) and verify_psd(direct8)
  assert direct0==sub(rd(s50["actual_0to8_original_direct_24D_upper"]),
                       rd(s50["actual_4to8_original_direct_24D_upper"]))
  assert direct8==sub(rd(s50["actual_4to8_original_direct_24D_upper"]),
                       rd(s52["PSD_direct_upper_reduction"]))
  rest=sub(sub(whole,direct0),direct8)
  assert rest==rd(s53["fixed_8to_infinity_remaining_upper"])
  assert plus(plus(rest,direct0),direct8)==whole
  lower=sub(Hlo,whole)
  optimistic_new=plus(lower,direct8)
  optimistic_both=plus(optimistic_new,direct0)
  assert optimistic_new==rd(s53["zero_only_4to8_counterfactual_24D_source_lower_NOT_CERTIFICATE"])
  assert optimistic_both==rd(s53["zero_both_measured_counterfactual_24D_source_lower_NOT_CERTIFICATE"])
  ray=[Q(x) for x in s47["selected_exact_inertia_witness"]["rational_vector"]]
  assert [str(x) for x in ray]==s53["exact_rational_MG43_witness"]
  mg43=sub(Hlo,rd(s47["selected_complete_24D_source_upper"]))
  assert str(quadratic(ray,mg43))==s53["MG43_accepted_negative_ray"]
  assert str(quadratic(ray,lower))==s53["actual_valid_MG52_negative_MG43_source_ray"]
  e8=quadratic(ray,direct8);e0=quadratic(ray,direct0)
  assert e8>=0 and e0>=0
  assert str(e8)==s53["direct_4to8_ray_upper_charge"]
  assert str(e0)==s53["direct_0to4_ray_upper_charge"]
  ceil8=quadratic(ray,optimistic_new)
  ceilBoth=quadratic(ray,optimistic_both)
  assert str(ceil8)==s53["same_ray_counterfactual_new_band_ZERO_ceiling"]
  assert str(ceilBoth)==s53["same_ray_counterfactual_both_bands_ZERO_ceiling"]
  assert ceil8==quadratic(ray,lower)+e8
  assert ceilBoth==ceil8+e0
  nogo_new=ceil8<0;nogo_both=ceilBoth<0
  assert s53["restricted_fixed_MG52_remainder_direct_4to8_ONLY_cannot_certify_24D"]==nogo_new
  assert s53["restricted_fixed_MG52_remainder_either_direct_band_ONLY_cannot_certify_24D"]==nogo_both
  verify_exact_negative_report(optimistic_new,s53["zero_4to8_counterfactual_full24_inertia"],s53["zero_4to8_counterfactual_full24_inertia_witness"])
  verify_exact_negative_report(optimistic_both,s53["zero_both_counterfactual_full24_inertia"],s53["zero_both_counterfactual_full24_inertia_witness"])
  assert s53["counterfactual_zeroed_band_is_NOT_a_valid_source_upper"]
  assert s53["genuine_direct_residual_is_PSD"]
  assert s53["no_original_operator_negative_eigenmode_claim"]
  if quadratic(ray,lower)<0:
   assert str(e8/(-quadratic(ray,lower)))==s53["direct_new_band_repair_max_fraction_of_ray_deficit"]
   assert str((e8+e0)/(-quadratic(ray,lower)))==s53["both_direct_bands_repair_max_fraction_of_ray_deficit"]
  num+=1;zero_new+=int(nogo_new);zero_both+=int(nogo_both)
 assert num==4
 assert obj["all_original_four_scenarios_replayed_exact"]
 assert obj["all_direct_original_covariances_PSD"]
 assert obj["hypothetical_zero_upper_is_NOT_a_valid_operator_certificate"]
 assert obj["new_mathematical_obstruction_only_fixed_MG52_remnant_and_B"]
 assert not obj["new_actual_original_24D_source_contraction"]
 assert not obj["full_original_470D_inverse"]
 assert not obj["original_odd_signed_51over56"]
 assert obj["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert obj["even_Weil_CC27_RH"]=="OPEN"
 print("MG53 INDEPENDENT exact rational fixed-remainder zero-direct ceiling replay PASS",{
   "cases":num,"negative_with_zero_4to8":zero_new,
   "negative_with_zero_both_direct_bands":zero_both,
   "physical_operator_negative_index":"NOT_CLAIMED",
   "RH":"OPEN"},flush=True)
def main():
 p=argparse.ArgumentParser()
 for name in ("mg24","mg46","mg47","mg50","mg52","mg53"):
  p.add_argument("--verified-"+name+"-json",required=True)
 arg=p.parse_args()
 d={n:json.loads((ROOT/getattr(arg,"verified_"+n+"_json")).read_text()) for n in ("mg24","mg46","mg47","mg50","mg52","mg53")}
 run(d)
if __name__=="__main__":main()
