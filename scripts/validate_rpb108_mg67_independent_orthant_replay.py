#!/usr/bin/env python3
"""MG67 independently verify 24 exact original source sign-cone extrema.

No MG67 producer import. For the accepted MG66 true original Fourier
source Q/R, independently re-create all 24 sign-dependent rational
matrices; derive true simplex minima by reducing to (x0,x1,1-x0-x1),
separately from producer's 4x4 KKT Gaussian elimination. Confirm
outward rounding, explicit witnesses, rank-three acceptance gates,
and NO negative physical operator claims from error-envelope failure.
"""
import argparse,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
SCALE=10**14
SIGNS=((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1))
def q(A,x):
 return A[0][0]*x[0]**2+A[1][1]*x[1]**2+A[2][2]*x[2]**2+2*A[0][1]*x[0]*x[1]+2*A[0][2]*x[0]*x[2]+2*A[1][2]*x[1]*x[2]
def simplex_min(A):
 cands=[]
 for i in range(3):
  x=[F(int(i==j)) for j in range(3)]
  cands.append((q(A,x),tuple(x)))
 for i,j in ((0,1),(0,2),(1,2)):
  a,b,c=A[i][i],A[i][j],A[j][j]
  den=a+c-2*b
  if den:
   t=(c-b)/den
   if 0<t<1:
    x=[F(0)]*3;x[i]=t;x[j]=1-t
    cands.append((q(A,x),tuple(x)))
 a,b,c=A[0]
 d,e,f=A[1][1],A[1][2],A[2][2]
 aa=a-2*c+f;bb=b-c-e+f;cc=d-2*e+f
 den=aa*cc-bb*bb
 if den:
  x0=((f-c)*cc-bb*(f-e))/den
  x1=(aa*(f-e)-bb*(f-c))/den
  x2=1-x0-x1
  if min(x0,x1,x2)>0:
   x=(x0,x1,x2);cands.append((q(A,x),x))
 # With singular reduced Hessian any interior stationary extremum
 # occurs on an affine family reaching a boundary equal-value point.
 return min(cands,key=lambda z:z[0])
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg66-json",required=True)
 p.add_argument("--verified-mg67-json",required=True)
 z=p.parse_args()
 a=json.loads((ROOT/z.verified_mg66_json).read_text())
 out=json.loads((ROOT/z.verified_mg67_json).read_text())
 assert a["status"]=="ORIGINAL_MG66_FULL_SIGN_COVARIANT_DIRECTIONAL_THREE_SOURCE_ERROR_GATES"
 assert out["status"]=="ORIGINAL_MG67_EXACT_SOURCE_ORTHANT_QUADRATIC_COPOSITIVE_CENSUS"
 assert a["canonical_W_ODD_NEG"]==out["canonical_W_ODD_NEG"]=="OPEN"
 assert a["source_plane_count"]==out["tested_genuine_original_source_3D_planes"]==6
 assert out["exact_rational_signed_source_cones"]==24
 assert out["outward_rounding_denominator"]==SCALE
 assert out["exact_rational_componentwise_outward_error_enclosure"]
 assert out["four_inequivalent_sign_cones_cover_all_eight_original_sign_patterns"]
 positive=negative=uncertain=certified=0
 for upstream,row in zip(a["cases"],out["cases"]):
  for key in ("original_third_source_coordinate","original_anchor_scale",
              "original_third_scale","original_selected_physical_source_cell_indices"):
   assert upstream[key]==row[key]
  Qm=[[F(t) for t in r] for r in upstream["original_3D_center_Gram"]]
  Rm=[[F(t) for t in r] for r in upstream["original_3D_mean_error_covariance_upper"]]
  localgood=localbad=0
  assert len(row["four_exact_cone_gates"])==4
  for s,gate in zip(SIGNS,row["four_exact_cone_gates"]):
   assert gate["original_source_coefficient_signs"]==list(s)
   exact=[[s[i]*s[j]*Qm[i][j]-Rm[i][j] for j in range(3)] for i in range(3)]
   low=[[F((t*SCALE).__floor__(),SCALE) for t in r] for r in exact]
   hi=[[F((t*SCALE).__ceil__(),SCALE) for t in r] for r in exact]
   assert [[str(t) for t in r] for r in low]==gate["entrywise_lower_orthant_matrix"]
   assert [[str(t) for t in r] for r in hi]==gate["entrywise_upper_orthant_matrix"]
   assert all(low[i][j]<=exact[i][j]<=hi[i][j] for i in range(3) for j in range(3))
   L,v=simplex_min(low);U,w=simplex_min(hi)
   assert L<=U
   for info,matrix,m in ((gate["exact_rational_lower_simplex_min"],low,L),
                          (gate["exact_rational_upper_simplex_min"],hi,U)):
    x=tuple(F(t) for t in info["minimizer"])
    assert len(x)==3 and all(t>=0 for t in x) and sum(x,F(0))==1
    assert F(info["min"])==m and q(matrix,x)==m
   assert q(low,v)==L and q(hi,w)==U
   good=L>0;bad=U<0
   assert good==gate["strict_positive_original_physical_error_cone"]
   assert bad==gate["negative_witness_for_conservative_error_envelope"]
   assert not(good and bad)
   if bad:assert q(exact,w)<0
   assert gate["original_physical_operator_negative_mode"] is False
   localgood+=int(good);localbad+=int(bad)
   positive+=int(good);negative+=int(bad);uncertain+=int(not good and not bad)
  assert localgood==row["strict_physical_source_sign_cones"]
  assert localbad==row["strict_failure_of_conservative_envelope_cones"]
  fully=localgood==4
  assert fully==row["all_four_original_source_sign_cones_positive"]
  if fully:
   mu=min(F(g["exact_rational_lower_simplex_min"]["min"]) for g in row["four_exact_cone_gates"])
   trace=sum(Qm[k][k]+Rm[k][k] for k in range(3))
   norm=F(upstream["original_source_basis_normtrace"])
   assert mu>0 and trace>0 and norm>0
   assert F(row["strict_3D_source_coercivity_if_all_positive"])==mu*mu/(2*trace*norm)
   certified+=1
  else:assert row["strict_3D_source_coercivity_if_all_positive"] is None
 assert positive==out["strict_positive_original_error_source_cones"]
 assert negative==out["strict_negative_witnesses_for_conservative_error_envelope"]
 assert uncertain==out["outward_rounding_inconclusive_source_cones"]
 assert certified==out["certified_original_source_3D_planes"]
 assert bool(certified)==out["physical_original_source_rank_at_least_three_CERTIFIED"]
 assert out["negative_error_envelope_witness_NOT_physical_negative_eigenmode"]
 assert not out["original_full24_source_strong_action_coercivity"]
 assert not out["original_source24_residual_contraction"]
 assert not out["original_full470_inverse"]
 assert not out["signed_odd_51over56"]
 assert out["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert out["even_Weil_CC27_RH"]=="OPEN"
 print("MG67 INDEPENDENT original physical-source rational coefficient-orthant 24 simplex minima PASS",{
  "positive_error_cones":positive,"negative_error_envelope_cones":negative,
  "undetermined_cones":uncertain,"certified_restricted_3D_planes":certified,
  "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
