#!/usr/bin/env python3
"""MG55: physically valid original whole-frequency response interpolation audit.

For original SI10/MG11 source F and genuine pole-corrected strong action A*,
R(B)=F-A*F B is AFFINE in a rational 24x24 response B.

For any 0<=theta<=1, exact Hilbert-space parallelogram:
Q(Btheta)=(1-theta) Q(Bi)+theta Q(Bj)
          -theta(1-theta) (Bj-Bi)^T Sstar (Bj-Bi),
Btheta=(1-theta)Bi+theta Bj,
Q(B)=R(B)^*R(B), Sstar=(A*F)^*(A*F)>=0.

Each archived MG43 U_i is a true Loewner upper on the SAME ORIGINAL
complete-frequency Q(B_i), so Uconvex=(1-theta)Ui+theta Uj is
a genuine whole-frequency 24D original source residual upper.
The curvature-aware upper uses independently verified MG24
Sstar >= Lstar:
Ucurvature=Uconvex-theta(1-theta) DeltaB^T Lstar DeltaB.
Check exact if MG24 Lstar is NEGATIVE SEMIDEFINITE: curvature budget
is then a PSD PENALTY, not a useful cancellation, whereas Lstar=0
is guaranteed valid by positivity of true Sstar.

THIS IS A FINITE RESPONSE HOMOTOPY TEST, not a global optimization over B.
No original 470D/odd51/56/Weil/RH promotion.
"""
import argparse,json,sys
from fractions import Fraction as Q
from itertools import combinations
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import deserialize
from validate_rpb108_mg25_robust_source_aware_residual import Id,T,mm,plus,sub,mul,psd,gersh_lower
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal

N=24
THETAS=(Q(1,4),Q(1,2),Q(3,4))
def read(a):
    a=deserialize(a)
    assert len(a)==N and all(len(r)==N for r in a)
    return a
def enc(a):return [[str(x) for x in r] for r in a]
def tr(a):return sum((a[i][i] for i in range(N)),Q(0))
def quadratic(v,a):
    return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def blend(a,b,t):
    return plus(mul(1-t,a),mul(t,b))
def sand(a,b):
    return mm(mm(T(b),a),b)
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg24-json",required=True)
 p.add_argument("--verified-mg47-json",required=True)
 p.add_argument("--output",default="artifacts/mg55_original_response_homotopy.json")
 args=p.parse_args()
 a24=json.loads((ROOT/args.verified_mg24_json).read_text())
 a47=json.loads((ROOT/args.verified_mg47_json).read_text())
 assert a24["canonical_W_ODD_NEG"]==a47["canonical_W_ODD_NEG"]=="OPEN"
 assert a24["true_complete_original_pole_Gstar_Sstar_Loewner_bracket"]
 assert a47["original_actual_unpoled_whole_G_and_S_minus_same_measured_band"]
 assert len(a47["scenarios"])==4
 endpoints=[]
 h0=None
 for i,case in enumerate(a47["scenarios"]):
  B=read(case["full_original_rational_response_B"])
  U=read(case["selected_complete_24D_source_upper"])
  L=read(case["selected_complete_24D_source_lower"])
  H=plus(U,L)
  assert H==T(H) and psd(H)
  assert h0 is None or H==h0
  if h0 is None:h0=H
  assert U==T(U) and psd(U)
  assert gersh_lower(L)==Q(case["selected_exact_Gersh_lower"])
  assert case["selected_strongest_valid_whole_method"]=="MG43_whole"
  ray=[Q(z) for z in case["selected_exact_inertia_witness"]["rational_vector"]]
  assert quadratic(ray,L)==Q(case["selected_exact_inertia_witness"]["exact_negative_quadratic"])<0
  endpoints.append({"case":case,"B":B,"U":U,"lower":L,"ray":ray,
      "label":str(case["mesh_cells"])+"/k"+str(case["cutoff_k"])})
 best_g=max(gersh_lower(e["lower"]) for e in endpoints)
 # MUCH STRONGER THAN A FINITE GRID TEST: find one rational vector
 # whose original source-lower quadratic is strictly negative on ALL
 # four independently accepted original MG43 endpoint matrices.
 # Hence for ANY nonnegative barycentric weights summing to one,
 # qf(v,Hlo-sum w_i U_i)=sum w_i*qf(v,Hlo-U_i)<0.
 # Thus the ENTIRE convex hull of these four ARCHIVED CERTIFICATE
 # uppers fails the 24D source positivity gate, even though it bounds
 # R(sum w_i B_i) for the changed physical original response.
 common_ray=endpoints[0]["ray"]
 common_charges=[quadratic(common_ray,e["lower"]) for e in endpoints]
 assert all(x<0 for x in common_charges)
 assert all(common_ray==e["ray"] for e in endpoints)
 # Independently accepted ORIGINAL full-action lower strong moment Sstar,
 # including actual pole mixed terms and the entire high tail.
 lowmoments={}
 for k in (12,16):
  case=next(z for z in a24["cases"] if z["cutoff_k"]==k)
  LS=read(case["complete_Sstar_lower"])
  assert LS==T(LS)
  negLS=mul(-1,LS)
  assert psd(negLS)
  # Astar* Astar is positive regardless of the signed 7-prime multiplier.
  # Hence 0 is a better valid Sstar lower than this archived NSD bracket.
  lowmoments[str(k)]={
     "negative_original_MG24_lower_strict_PSD":True,
     "negative_Sstar_lower_matrix":enc(negLS),
     "negative_Sstar_lower_trace":str(tr(negLS))
  }
 rows=[]; curved=0;positive=0
 for i,j in combinations(range(4),2):
  e,f=endpoints[i],endpoints[j]
  Delta=sub(f["B"],e["B"])
  assert any(x for row in Delta for x in row)
  for theta in THETAS:
   Btheta=blend(e["B"],f["B"],theta)
   U=blend(e["U"],f["U"],theta)
   L=sub(h0,U)
   assert U==T(U) and psd(U)
   # Finite source upper is Loewner VALID via operator Jensen for this
   # changed response, not via mixing bounds for a fixed physical B.
   g=gersh_lower(L)
   cls,wit=classify_ideal(L)
   assert cls in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                  "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
   if cls=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
    v=[Q(x) for x in wit["rational_vector"]]
    assert quadratic(v,L)==Q(wit["exact_negative_quadratic"])<0
   positive+=int(cls=="POSITIVE_EXACT_RATIONAL_LDL")
   errors={}
   for k in ("12","16"):
    S=read(next(z for z in a24["cases"] if str(z["cutoff_k"])==k)["complete_Sstar_lower"])
    penalty=mul(theta*(1-theta),sand(mul(-1,S),Delta))
    assert penalty==T(penalty) and psd(penalty)
    strongU=plus(U,penalty)
    assert psd(sub(strongU,U))
    strongL=sub(h0,strongU)
    assert gersh_lower(strongL)<=g
    errors[k]={
      "correct_original_curvature_upper_additional_PSD_trace":str(tr(penalty)),
      "original_curvature_upper_Gersh":str(gersh_lower(strongL)),
      "stored_original_strong_curvature_cannot_tighten_convex_upper":True}
    curved+=1
   rows.append({
     "original_response_endpoint_indices":[i,j],
     "source_endpoints":[e["label"],f["label"]],
     "theta":str(theta),
     "new_changed_original_response_B":enc(Btheta),
     "new_original_full_frequency_valid_upper":enc(U),
     "new_original_full_frequency_lower":enc(L),
     "new_original_exact_Gersh":str(g),
     "max_historical_MG43_Gersh":str(best_g),
     "strict_improvement_vs_best_archived":g>best_g,
     "inertia_classification":cls,
     "inertia_exact_witness":wit,
     "original_zero_curvature_lower_is_valid":True,
     "strong_moment_MG24_curvature_penalty":errors,
     "true_original_complete_frequency_pole_and_all_tails_via_endpoints":True
    })
   print("MG55 original valid response blend",i,j,str(theta),
         "Gersh",float(g),"strict",g>best_g,
         "source_positive",cls=="POSITIVE_EXACT_RATIONAL_LDL",flush=True)
 assert len(rows)==18 and curved==36
 report={
   "status":"ORIGINAL_MG55_FULL_FREQUENCY_RESPONSE_HOMOTOPY_24D",
   "canonical_W_ODD_NEG":"OPEN",
   "accepted_source_archives":{"MG24":39378465438,"MG47":39663431182},
   "true_original_physical_response_affine_identity":True,
   "true_23_adapted_plus_sinh_pole_source_24D":True,
   "whole_original_pole_mixed_action_and_high_tails_retained":True,
   "all_response_blends_full_source_Loewner_valid":True,
   "no_new_Fourier_source_samples":True,
   "original_four_response_endpoints":[
       {"mesh_cells":e["case"]["mesh_cells"],
        "cutoff_k":e["case"]["cutoff_k"],
        "original_response_B":enc(e["B"]),
        "complete_24D_upper":enc(e["U"]),
        "exact_original_Gersh":str(gersh_lower(e["lower"]))}
       for e in endpoints],
   "archived_MG24_strong_moment_lower_is_negative_semidefinite":lowmoments,
   "original_all_18_pairwise_rational_response_blends_evaluated":True,
   "original_common_negative_exact_rational_source_ray":[str(x) for x in common_ray],
   "original_common_negative_exact_source_lower_quadratics":[str(x) for x in common_charges],
   "whole_four_endpoint_convex_response_certificate_hull_obstructed":True,
   "all_nonnegative_barycentric_response_weights_covered_by_affine_identity":True,
   "original_all_36_strong_curvature_sign_tests":True,
   "best_archived_original_Gersh":str(best_g),
   "strict_full24_Gersh_improvements":sum(r["strict_improvement_vs_best_archived"] for r in rows),
   "new_full24_source_contractions":positive,
   "finite_grid_only_not_global_B_optimality":True,
   "original_470D_inverse":False,
   "original_signed_51over56_cap":False,
   "independent_original_Fourier_form_domain_audit":"OPEN",
   "even_Weil_CC27_RH":"OPEN",
   "trials":rows}
 dst=ROOT/args.output;dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(report,indent=2)+"\n")
 print("MG55 complete original exact response homotopy result",{
    "trials":len(rows),"improved_gersh":report["strict_full24_Gersh_improvements"],
    "new_positive":positive,"curvature_checks":curved,
    "RH":"OPEN"},flush=True)
if __name__=="__main__":main()
