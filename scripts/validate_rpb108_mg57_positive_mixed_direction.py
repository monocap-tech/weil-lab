#!/usr/bin/env python3
"""MG57-MIXED: exact original physical strong-action 24D inertia and
CERTIFIED positive mixed-source direction.

MG56's conservative full24 strong-action lower is negative definite.
MG57's same-cell pole-only change remains negative definite.
But genuine original signed-multiplier [1/8,1/2] physical subpartition
creates a mixed-source direction with an EXACT rational positive lower:

v^T L_MG57 v = 30642918729381 / 250000000000, ||v||²=82.

Since true original S_*=(A_*F)^*(A_*F) >= L_MG57, this certifies
positive strong-action energy on the one-dimensional source subspace
span(v), NOT all 24D, and NOT a global rank-one Loewner bound.
An indefinite conservative lower is NOT an actual negative operator.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
N=24
V=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
def rd(x):
 a=[[Q(z) for z in row] for row in x]
 assert len(a)==N and all(len(row)==N for row in a)
 return a
def inertia(A):
 assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
 M=[r[:] for r in A]
 positive=negative=0
 signs=[]
 for k in range(N):
  p=M[k][k]
  assert p!=0,("no diagonal LDL pivot",k)
  positive+=int(p>0);negative+=int(p<0)
  signs.append(1 if p>0 else -1)
  for i in range(k+1,N):
   for j in range(i,N):
    M[i][j]-=M[i][k]*M[k][j]/p
    M[j][i]=M[i][j]
 assert positive+negative==N
 return positive,negative,signs
def qf(v,A):
 return sum((Q(v[i])*A[i][j]*Q(v[j])
             for i in range(N) for j in range(N)),Q(0))
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg56-json",required=True)
 p.add_argument("--verified-mg57-json",required=True)
 p.add_argument("--output",default="artifacts/mg57_exact_positive_mixed_source_witness.json")
 args=p.parse_args()
 old=json.loads((ROOT/args.verified_mg56_json).read_text())
 new=json.loads((ROOT/args.verified_mg57_json).read_text())
 assert old["status"]=="ORIGINAL_MG56_POLE_CORRECTED_STRONG_ACTION_BAND_24D_LOWER"
 assert new["status"]=="ORIGINAL_MG57_LOCAL_PHYSICAL_MULTIPLIER_POLE_COUPLED_STRONG_LOWER"
 assert old["canonical_W_ODD_NEG"]==new["canonical_W_ODD_NEG"]=="OPEN"
 assert new["original_true_Sstar_ge_MG57_lower"]
 L56=rd(old["exact_band_lower"])
 Lpole=rd(new["samecell_pole_coupled_strong_lower"])
 L57=rd(new["refined_original_true_strong_lower"])
 oldcounts=inertia(L56)
 polecounts=inertia(Lpole)
 refinedcounts=inertia(L57)
 assert oldcounts[:2]==polecounts[:2]==(0,24)
 assert refinedcounts[:2]==(1,23)
 assert L57==rd(new["selected_trace_lower"])
 assert all(L57[i][i]<0 for i in range(N))
 assert len(V)==N and sum(z*z for z in V)==82
 q=qf(V,L57)
 assert q==Q(30642918729381,250000000000)>0
 neg=qf(tuple([1]+[0]*(N-1)),L57)
 assert neg==L57[0][0]<0
 # Positivity of one exact quadratic does NOT grant a 24x24 rank-one
 # Loewner coercivity bound, because cross terms are uncontrolled.
 result={
   "status":"ORIGINAL_MG57_CERTIFIED_POSITIVE_MIXED_STRONG_ACTION_DIRECTION",
   "canonical_W_ODD_NEG":"OPEN",
   "accepted_original_MG56_run_id":39894269994,
   "accepted_original_MG57_run_id":39897754515,
   "true_original_strong_action_second_moment_Sstar_PSD":True,
   "original_true_Sstar_greater_equal_refined_band_lower_FULL24":True,
   "old_MG56_lower_exact_rational_inertia":{"positive":0,"negative":24},
   "pole_only_coupled_lower_exact_rational_inertia":{"positive":0,"negative":24},
   "new_MG57_refined_lower_exact_rational_inertia":{"positive":1,"negative":23},
   "MG57_refined_lower_all_original_coordinate_diagonals_negative":True,
   "MG57_positive_original_mixed_source_vector":[str(x) for x in V],
   "MG57_positive_mixed_source_vector_integer_norm_squared":"82",
   "MG57_positive_original_strong_lower_exact_quadratic":str(q),
   "MG57_positive_original_strong_lower_normalized_constant":str(q/82),
   "MG57_negative_certificate_lower_first_coordinate_quadratic":str(neg),
   "one_dimensional_source_strong_action_coercivity_CERTIFIED":True,
   "full24_original_strong_action_coercivity_NOT_certified":True,
   "GLOBAL_rank_one_Loewner_lower_NOT inferred_from_single_ray":True,
   "negative_conservative_lower_direction_NOT_actual_negative_operator_mode":True,
   "actual_full470_inverse_NOT_proved":True,
   "original_signed_51over56_cap_NOT_proved":True,
   "independent_original_Fourier_form_domain_audit":"OPEN",
   "even_Weil_CC27_RH":"OPEN"
 }
 dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+"\n")
 print("MG57 EXACT MIXED STRONG-ACTION POSITIVITY CERTIFIED",{
    "MG56_inertia":oldcounts[:2],"MG57_inertia":refinedcounts[:2],
    "positive_ray_lower":float(q),
    "unit_source_ray_strong_energy_lower":float(q/82),
    "full24_and_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
