#!/usr/bin/env python3
"""MG57 independent reverse exact LDL strong-source mixed sign replay.

No MG57 mixed-inertia producer import. Reverse diagonal Gaussian
congruences certify 1 positive +23 negative of conservative 24D
physical corrected-action lower. Two independently simple integer
source vectors explicitly show rigorously POSITIVE source strong
action energy; a negative coordinate of conservative lower only
establishes weakness of the global lower, NOT a physical negative mode.

Does not promote 1D ray to a full matrix rank-one Loewner lower.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
N=24
V2=(-33,-2,-23,21,22,2,11,23,14,24,24,15,11,-22,-25,22,2,21,22,25,25,14,-25,-23)
def mat(rows):
 a=[[Q(x) for x in r] for r in rows]
 assert len(a)==N and all(len(r)==N for r in a)
 return a
def quadratic(v,A):
 return sum((v[i]*A[i][j]*v[j] for j in range(N) for i in range(N)),Q(0))
def reverse_inertia(a):
 assert all(a[i][j]==a[j][i] for i in range(N) for j in range(N))
 M=[r[:] for r in a];pos=neg=0
 for k in range(N-1,-1,-1):
  pivot=M[k][k]
  assert pivot!=0
  pos+=int(pivot>0);neg+=int(pivot<0)
  for i in range(k):
   factor=M[i][k]/pivot
   for j in range(i,k):
    M[i][j]-=factor*M[k][j]
    M[j][i]=M[i][j]
 return (pos,neg)
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg56-json",required=True)
 p.add_argument("--verified-mg57-json",required=True)
 p.add_argument("--verified-mg57-mixed-json",required=True)
 args=p.parse_args()
 read=lambda x:json.loads((ROOT/x).read_text())
 old,mg57,report=[read(getattr(args,"verified_"+name+"_json"))
                    for name in ("mg56","mg57","mg57_mixed")]
 assert report["status"]=="ORIGINAL_MG57_CERTIFIED_POSITIVE_MIXED_STRONG_ACTION_DIRECTION"
 assert old["canonical_W_ODD_NEG"]==mg57["canonical_W_ODD_NEG"]==report["canonical_W_ODD_NEG"]=="OPEN"
 L=mat(mg57["refined_original_true_strong_lower"])
 assert L==mat(mg57["selected_trace_lower"])
 assert reverse_inertia(L)==(1,23)
 assert reverse_inertia(mat(old["exact_band_lower"]))==(0,24)
 assert reverse_inertia(mat(mg57["samecell_pole_coupled_strong_lower"]))==(0,24)
 assert all(L[i][i]<0 for i in range(N))
 v=[Q(x) for x in report["MG57_positive_original_mixed_source_vector"]]
 assert len(v)==N and any(v)
 norm=sum(z*z for z in v)
 assert norm==82==Q(report["MG57_positive_mixed_source_vector_integer_norm_squared"])
 q=quadratic(v,L)
 assert q==Q(report["MG57_positive_original_strong_lower_exact_quadratic"])>0
 assert q/norm==Q(report["MG57_positive_original_strong_lower_normalized_constant"])
 # A second much different INTEGER certificate, independently rounded
 # from the physical new action-moment matrix with positive quadratic.
 assert len(V2)==N and sum(z*z for z in V2)==10017
 q2=quadratic(V2,L)
 assert q2>0
 e=[Q(1)]+[Q(0)]*(N-1)
 assert quadratic(e,L)==Q(report["MG57_negative_certificate_lower_first_coordinate_quadratic"])<0
 assert report["one_dimensional_source_strong_action_coercivity_CERTIFIED"]
 assert report["full24_original_strong_action_coercivity_NOT_certified"]
 assert report["GLOBAL_rank_one_Loewner_lower_NOT_inferred_from_single_ray"]
 assert report["negative_conservative_lower_direction_NOT_actual_negative_operator_mode"]
 assert report["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert report["even_Weil_CC27_RH"]=="OPEN"
 print("MG57 INDEPENDENT exact reverse LDL + TWO integer strict positive original mixed-source energy witnesses PASS",{
  "exact_24D_conservative_lower_inertia":(1,23),
  "first_unit_ray_energy_lower":float(q/norm),
  "second_ray_energy_lower":float(q2/sum(z*z for z in V2)),
  "full24_coercivity":"OPEN",
  "physical_negative_operator_mode":"NOT CLAIMED",
  "RH":"OPEN"},flush=True)
if __name__=="__main__":main()
