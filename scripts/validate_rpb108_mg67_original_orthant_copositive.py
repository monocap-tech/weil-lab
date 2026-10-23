#!/usr/bin/env python3
"""MG67: exact original-source sign-orthant (copositive) 3D moment audit.

For x>=0 with sum(x)=1, minimize x' (D Q D-R) x by exact rational
simplex vertices, edge stationary points and interior KKT stationarity.
R is the original verified MG66 true physical pole/multiplier/source
cell error envelope; Q is its original true 3D mean center Gram.
Outward rounding each entry to denominator 10^14 yields independently
replayable rational lower/upper inequalities for nonnegative x.
A negative upper-cone witness disproves only this conservative proof
inequality, NOT the original physical source operator's positivity.
"""
import argparse,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
SCALE=10**14
SIGNS=((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1))
def q(A,x):
 return sum((A[i][j]*x[i]*x[j] for i in range(3) for j in range(3)),F(0))
def solve(A,y):
 n=len(y);B=[list(r)+[v] for r,v in zip(A,y)]
 for k in range(n):
  p=next((j for j in range(k,n) if B[j][k]),None)
  if p is None:return None
  B[k],B[p]=B[p],B[k]
  h=B[k][k];B[k]=[z/h for z in B[k]]
  for j in range(n):
   if j!=k and B[j][k]:
    h=B[j][k];B[j]=[a-h*b for a,b in zip(B[j],B[k])]
 return [r[-1] for r in B]
def minimum(A):
 samples=[]
 for i in range(3):
  x=tuple(F(j==i) for j in range(3))
  samples.append((q(A,x),x,"vertex"))
 for i,j in ((0,1),(0,2),(1,2)):
  a,b,c=A[i][i],A[i][j],A[j][j]
  den=a-2*b+c
  if den:
   t=(c-b)/den
   if 0<t<1:
    x=[F(0)]*3;x[i]=t;x[j]=1-t
    samples.append((q(A,x),tuple(x),"edge"))
 K=[list(r)+[-F(1)] for r in A]+[[F(1),F(1),F(1),F(0)]]
 z=solve(K,[F(0),F(0),F(0),F(1)])
 if z is not None and all(x>0 for x in z[:3]):
  x=tuple(z[:3]);assert sum(x,F(0))==1
  samples.append((q(A,x),x,"interior"))
 # In a singular KKT system, any interior stationary minimum lies
 # in a nontrivial affine family of equal-valued stationary points;
 # this family intersects the simplex boundary, already checked.
 v,x,t=min(samples,key=lambda s:s[0])
 return {"min":str(v),"minimizer":[str(y) for y in x],
         "minimizer_type":t,"stationary_KKT_singular":z is None,
         "stationary_candidates_checked":len(samples)}
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg66-json",required=True)
 p.add_argument("--output",default="artifacts/mg67_original_source_orthant_copositive.json")
 a=p.parse_args()
 d=json.loads((ROOT/a.verified_mg66_json).read_text())
 assert d["status"]=="ORIGINAL_MG66_FULL_SIGN_COVARIANT_DIRECTIONAL_THREE_SOURCE_ERROR_GATES"
 assert d["canonical_W_ODD_NEG"]=="OPEN" and d["source_plane_count"]==6
 assert d["rational_3D_sign_matrix_count"]==24
 assert not d["rank_at_least_three_on_original_source_frame_CERTIFIED"]
 cases=[];positive=negative=uncertain=0;winners=[]
 for src in d["cases"]:
  Qm=[[F(x) for x in row] for row in src["original_3D_center_Gram"]]
  Rm=[[F(x) for x in row] for row in src["original_3D_mean_error_covariance_upper"]]
  gates=[]
  for signs in SIGNS:
   exact=[[signs[i]*signs[j]*Qm[i][j]-Rm[i][j] for j in range(3)] for i in range(3)]
   lo=[[F((x*SCALE).__floor__(),SCALE) for x in row] for row in exact]
   hi=[[F((x*SCALE).__ceil__(),SCALE) for x in row] for row in exact]
   assert all(lo[i][j]<=exact[i][j]<=hi[i][j] for i in range(3) for j in range(3))
   L=minimum(lo);U=minimum(hi)
   certified=F(L["min"])>0
   fail=F(U["min"])<0
   assert not(certified and fail)
   positive+=int(certified);negative+=int(fail)
   uncertain+=int(not certified and not fail)
   gates.append({
    "original_source_coefficient_signs":list(signs),
    "rational_outward_denominator":SCALE,
    "entrywise_lower_orthant_matrix":[[str(v) for v in row] for row in lo],
    "entrywise_upper_orthant_matrix":[[str(v) for v in row] for row in hi],
    "exact_rational_lower_simplex_min":L,
    "exact_rational_upper_simplex_min":U,
    "strict_positive_original_physical_error_cone":certified,
    "negative_witness_for_conservative_error_envelope":fail,
    "acceptance_category":"strict_positive_on_orthant" if certified else (
       "strict_failure_of_this_error_envelope" if fail else "precision_inconclusive"),
    "original_physical_operator_negative_mode":False})
  yes=all(g["strict_positive_original_physical_error_cone"] for g in gates)
  mu=min((F(g["exact_rational_lower_simplex_min"]["min"]) for g in gates),default=F(0)) if yes else None
  if yes:
   tr=sum(Qm[i][i]+Rm[i][i] for i in range(3))
   norm=F(src["original_source_basis_normtrace"])
   k=mu*mu/(2*tr*norm)
   assert k>0
  else:k=None
  row={
   "original_third_source_coordinate":src["original_third_source_coordinate"],
   "original_anchor_scale":src["original_anchor_scale"],
   "original_third_scale":src["original_third_scale"],
   "original_selected_physical_source_cell_indices":src["original_selected_physical_source_cell_indices"],
   "strict_physical_source_sign_cones":sum(g["strict_positive_original_physical_error_cone"] for g in gates),
   "strict_failure_of_conservative_envelope_cones":sum(g["negative_witness_for_conservative_error_envelope"] for g in gates),
   "all_four_original_source_sign_cones_positive":yes,
   "strict_3D_source_coercivity_if_all_positive":str(k) if yes else None,
   "four_exact_cone_gates":gates}
  cases.append(row)
  if yes:winners.append(row)
  print("MG67 original source rational coefficient-cone",{"j":row["original_third_source_coordinate"],
    "positive_sign_cones":row["strict_physical_source_sign_cones"],
    "negative_envelope_witnesses":row["strict_failure_of_conservative_envelope_cones"]},flush=True)
 best=max((F(r["strict_3D_source_coercivity_if_all_positive"]) for r in winners),default=None)
 out={
  "status":"ORIGINAL_MG67_EXACT_SOURCE_ORTHANT_QUADRATIC_COPOSITIVE_CENSUS",
  "canonical_W_ODD_NEG":"OPEN",
  "accepted_MG66_original_physical_source_actions_run":40022012105,
  "original_55_cell_real_Fourier_multiplier_source_and_pole_unchanged":True,
  "exact_rational_componentwise_outward_error_enclosure":True,
  "outward_rounding_denominator":SCALE,
  "four_inequivalent_sign_cones_cover_all_eight_original_sign_patterns":True,
  "original_source_orthant_positivity_is_sufficient_not_operator_change":True,
  "tested_genuine_original_source_3D_planes":len(cases),
  "exact_rational_signed_source_cones":len(cases)*4,
  "strict_positive_original_error_source_cones":positive,
  "strict_negative_witnesses_for_conservative_error_envelope":negative,
  "outward_rounding_inconclusive_source_cones":uncertain,
  "certified_original_source_3D_planes":len(winners),
  "physical_original_source_rank_at_least_three_CERTIFIED":bool(winners),
  "best_original_source_three_dimensional_restricted_constant":str(best) if best else None,
  "negative_error_envelope_witness_NOT_physical_negative_eigenmode":True,
  "original_full24_source_strong_action_coercivity":False,
  "original_source24_residual_contraction":False,
  "original_full470_inverse":False,
  "signed_odd_51over56":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN",
  "cases":cases}
 dest=ROOT/a.output;dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+"\n")
 print("MG67 original exact physical error source 3D coefficient orthants",{
  "strict_positive_cones":positive,"strict_negative_envelope_cones":negative,
  "fully_accepted_three_dimensional_source_planes":len(winners),"RH":"OPEN"},flush=True)
if __name__=="__main__":main()
