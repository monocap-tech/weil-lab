#!/usr/bin/env python3
"""MG66 -- rigorous original PHYSICAL 3-source sign-covariant error gate.

MG65 independently verified 252 source 3D physical Jensen Grams and
identified the best (strictly failing) scalar Frobenius error bound for
each original third coordinate. MG66 computes an ACTUAL different
mathematical 3x3 uncertainty inequality on those six real physical
source configurations.

True Fourier cell mean error delta_I has component intervals
 |delta_I,j|<=rho_I,j, with the same accepted true pole-corrected
 scalar multiplier/source bounds. For any REAL coefficient z, and
 sign diagonal D=diag(sign z_i), one has
 ||Delta C z||² <= z^T D R D z
 R=sum_I (2 h_I) rho_I rho_I^T.
 True center matrix has Q=C^T C. If the EXACT rational
 H_D=Q-D R D is POSITIVE DEFINITE for every one of the 8 signs
 (four inequivalent up to global minus), then no allowed original
 physical Fourier means can lose a direction.

Explicit exact coefficient-source 3D coercivity bound:
 mu=min_D det(H_D)/e2(H_D)>0,
 k=mu²/[2(trace(Q)+trace(R))*trace(W^T W)]>0.
 This follows from
 ||Cz||²-||DeltaCz||² >= mu ||z||², and
 ||Cz||+||DeltaCz|| <= sqrt(2(trQ+trR))||z||.
 The true strong action outside chosen cells remains PSD.

No claim from a failed conservative inequality that original source
operator has a negative eigenvalue. No rank-three or RH assertion
unless the entire verified exact sign test passes.
"""
import argparse,itertools,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg59_projected_true_action_plane as mg59
import validate_rpb108_mg62_two_cell_jensen_gap as mg62
V=tuple(F(x) for x in mg59.ANCHOR)
N=24;P=23
SIGN_GAUGES=((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1))
def det_and_e2(v):
 a,b,c=v[0]
 _,d,e=v[1]
 _,_,f=v[2]
 p01=a*d-b*b;p02=a*f-c*c;p12=d*f-e*e
 det=a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b
 return (a,p01,p02,p12,det,p01+p02+p12)
def cell_mean_matrices(cells,source,b,berr,selected):
 Qm=[[F(0) for j in range(3)] for i in range(3)]
 Rm=[[F(0) for j in range(3)] for i in range(3)]
 for k in selected:
  cell=cells[k]
  assert F(0)<cell[1]-cell[0]
  factor=2*(cell[1]-cell[0])
  readings=[mg59.project_one(s,cell,b,berr) for s in source]
  centers=[r[0] for r in readings]
  radii=[r[2] for r in readings]
  assert all(r>=0 for r in radii)
  for i in range(3):
   for j in range(3):
    Qm[i][j]+=factor*centers[i]*centers[j]
    Rm[i][j]+=factor*radii[i]*radii[j]
 assert all(Qm[i][j]==Qm[j][i] and Rm[i][j]==Rm[j][i]
            for i in range(3) for j in range(3))
 return Qm,Rm
def encoded(A):return [[str(x) for x in row] for row in A]
def test_sign_gates(Qm,Rm,norm):
 traceq=sum(Qm[i][i] for i in range(3))
 tracer=sum(Rm[i][i] for i in range(3))
 assert traceq>0 and tracer>=0 and norm>0
 cases=[]
 for signs in SIGN_GAUGES:
  H=[[Qm[i][j]-signs[i]*signs[j]*Rm[i][j] for j in range(3)]
     for i in range(3)]
  a,p01,p02,p12,det,e2=det_and_e2(H)
  passes=(a>0 and p01>0 and det>0)
  if passes:assert e2>0
  exactmu=det/e2 if passes else None
  record={
   "source_coefficient_signs":list(signs),
   "exact_difference_3D_Gram":encoded(H),
   "first_principal_minor":str(a),
   "second_leading_principal_minor":str(p01),
   "other_principal_2D_minors":[str(p02),str(p12)],
   "full_exact_3D_determinant":str(det),
   "second_elementary_symmetric":str(e2),
   "strict_exact_rational_three_source_error_domination":passes,
   "positive_min_eigenvalue_rational_lower":str(exactmu) if passes else None}
  cases.append(record)
 positive=all(x["strict_exact_rational_three_source_error_domination"] for x in cases)
 mu=min((F(x["positive_min_eigenvalue_rational_lower"]) for x in cases),
        default=F(0)) if positive else None
 const=mu*mu/(2*(traceq+tracer)*norm) if positive else None
 if positive:assert mu>0 and const>0
 return {
  "original_3D_center_Gram":encoded(Qm),
  "original_3D_mean_error_covariance_upper":encoded(Rm),
  "center_trace":str(traceq),"uncertainty_covariance_trace":str(tracer),
  "original_source_basis_normtrace":str(norm),
  "full_eight_sign_patterns_checked_using_four_global_sign_equivalences":True,
  "all_sign_patterns_strictly_positive":positive,
  "certified_min_3D_QminusDRD_lower":str(mu) if positive else None,
  "certified_original_source_3D_coefficient_norm_coercivity":str(const) if positive else None,
  "four_exact_sign_gates":cases}
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg57","mg58","mg64","mg65"):
  p.add_argument("--verified-"+k+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg66_original_3D_sign_covariance.json")
 z=p.parse_args()
 a={k:json.loads((ROOT/getattr(z,"verified_"+k+"_json")).read_text())
    for k in ("mg24","mg57","mg58","mg64","mg65")}
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in a.values())
 assert a["mg65"]["status"]=="ORIGINAL_MG65_EXACT_THREE_SOURCE_MEAN_ERROR_GEOMETRY_CENSUS"
 assert a["mg65"]["strict_3D_full_singular_gap_count"]==0
 assert a["mg64"]["status"]=="ORIGINAL_MG64_GENUINE_PHYSICAL_THREE_SOURCE_JENSEN_SINGULAR_GAP"
 cells=mg62.source55(a["mg57"],a["mg58"])
 assert len(cells)==55
 H,Rad,err=original_H24_from_physical_source()
 assert err==F(a["mg24"]["physical_Gram_Loewner_row_error"])
 b=[H[k][P] for k in range(N)]
 brad=[Rad[k][P] for k in range(N)]
 rows=[];wins=[]
 assert len(a["mg65"]["all_source_third_coordinate_obstructions"])==6
 for witness in a["mg65"]["all_source_third_coordinate_obstructions"]:
  j=witness["original_third_coordinate"]
  alpha=F(witness["best_anchor_scale"])
  beta=F(witness["best_third_scale"])
  indices=witness["best_true_physical_cell_indices"]
  assert j in (0,1,2,11,20,23)
  assert len(indices)==witness["best_cell_count"]
  assert indices==sorted(set(indices)) and all(0<=i<55 for i in indices)
  W=(
     tuple(alpha*v for v in V),
     tuple(F(k==5) for k in range(N)),
     tuple(beta*F(k==j) for k in range(N)))
  Nsource=sum((mg59.dot(w,w) for w in W),F(0))
  Qm,Rm=cell_mean_matrices(cells,W,b,brad,indices)
  original_scalar_ratio=F(witness["best_center_to_error_ratio"])
  # Compare with prior independently verified center Gram and scalar E.
  earlier=next(x for x in a["mg65"]["all_252_exact_source_observations"]
               if x["third_original_coordinate"]==j
               and x["source_anchor_scale"]==witness["best_anchor_scale"]
               and x["source_third_scale"]==witness["best_third_scale"]
               and x["original_physical_cell_indices"]==indices)
  assert F(earlier["rigorous_original_Fourier_error_squared"])==sum(Rm[k][k] for k in range(3))
  prev=next(c for c in a["mg64"]["cases"]
            if c["original_source_third_coordinate"]==j
            and F(c["physical_anchor_alpha"])==alpha
            and F(c["physical_third_beta"])==beta)
  match=next(c["best_exact_source_3D_subset"]
             for c in prev["best_certificate_per_subset_size"]
             if c["best_exact_source_3D_subset"]["original_physical_cell_indices"]==indices)
  assert encoded(Qm)==[[match["center_gram_00"],match["center_gram_01"],match["center_gram_02"]],
                        [match["center_gram_01"],match["center_gram_11"],match["center_gram_12"]],
                        [match["center_gram_02"],match["center_gram_12"],match["center_gram_22"]]]
  test=test_sign_gates(Qm,Rm,Nsource)
  row={"original_third_source_coordinate":j,
       "original_anchor_scale":str(alpha),"original_third_scale":str(beta),
       "original_selected_physical_source_cell_indices":indices,
       "original_scalar_Frobenius_center_over_error_ratio":str(original_scalar_ratio),
       "unchanged_true_original_pole_and_multiplier_source":True,
       "original_full_unselected_action_frequency_energy_PSD":True,
       "only_restricted_3D_coercivity_not_global24":True,
       **test}
  wins.append(row) if test["all_sign_patterns_strictly_positive"] else None
  rows.append(row)
  print("MG66 original physical directional error-matrix sign gates",{
    "third_source":j,"positive_sign_gates":sum(s["strict_exact_rational_three_source_error_domination"]
       for s in test["four_exact_sign_gates"]),
    "accepted3D":test["all_sign_patterns_strictly_positive"]},flush=True)
 best=max(wins,key=lambda r:F(r["certified_original_source_3D_coefficient_norm_coercivity"])) if wins else None
 output={
  "status":"ORIGINAL_MG66_FULL_SIGN_COVARIANT_DIRECTIONAL_THREE_SOURCE_ERROR_GATES",
  "canonical_W_ODD_NEG":"OPEN",
  "accepted_original_source_runs":{"MG24":39378465438,"MG57":39897754515,
                                   "MG58":39902364126,"MG64":40005133889,
                                   "MG65":40007193988},
  "original_real_55_Fourier_source_cells_and_signed_multiplier_unchanged":True,
  "original_23adapted_plus_actual_sinh_pole_24D_source":True,
  "original_actual_full_frequency_strong_action_positive_tail_retained":True,
  "source_3D_error_sign_covariance_is_sufficient_gate_NOT_operator_change":True,
  "all_global_sign_equivalent_error_cases_tested":True,
  "source_plane_count":len(rows),
  "rational_3D_sign_matrix_count":len(rows)*len(SIGN_GAUGES),
  "certified_original_three_dimensional_source_plane_count":len(wins),
  "rank_at_least_three_on_original_source_frame_CERTIFIED":bool(wins),
  "best_original_3D_third_source":best["original_third_source_coordinate"] if best else None,
  "best_restricted_original_3D_coercivity":best["certified_original_source_3D_coefficient_norm_coercivity"] if best else None,
  "original_full24_source_strong_action_coercivity":False,
  "original_24D_source_residual_contraction":False,
  "original_full470_inverse":False,
  "signed_odd_51over56":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN",
  "cases":rows}
 target=ROOT/z.output;target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(output,indent=2)+"\n")
 print("MG66 ORIGINAL actual source physical directional sign-error 3D result",{
   "tested_genuine_3D_planes":len(rows),"positive":len(wins),
   "fully_checked_sign_matrices":len(rows)*4,"RH":"OPEN"},flush=True)
if __name__=="__main__":main()
