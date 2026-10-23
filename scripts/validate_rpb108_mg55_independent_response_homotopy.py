#!/usr/bin/env python3
"""MG55 independent original 24D Hilbert-space response homotopy replay.

No MG55 producer import. Reconstruct original physical SI10 source Gram
from the original 25 generators, verify all four archived whole-frequency
MG43 Loewner UPPER matrices use the SAME 24D source and are PSD, then
replay 18 new distinct exact rational changed-B response hulls.
Check strong-action Sstar lower for original pole-corrected operator is
NSD for both k12/k16 and that the true PSD Sstar -> 0 better lower
makes the original endpoint convex upper superior to the archived
negative strong-lower curvature formula. Never assert global B optimum.
"""
import argparse,json,sys
from fractions import Fraction as Q
from itertools import combinations
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
N=24
def rd(a):
 A=[[Q(x) for x in row] for row in a]
 assert len(A)==N and all(len(z)==N for z in A)
 return A
def trans(A):return [list(c) for c in zip(*A)]
def scale(k,A):return [[k*x for x in row] for row in A]
def add(A,B):return [[x+y for x,y in zip(rowa,rowb)] for rowa,rowb in zip(A,B)]
def sub(A,B):return add(A,scale(-1,B))
def mult(A,B):
 Bt=trans(B)
 return [[sum((x*y for x,y in zip(row,col)),Q(0))
          for col in Bt] for row in A]
def sand(S,D):return mult(mult(trans(D),S),D)
def eye():return [[Q(i==j) for j in range(N)] for i in range(N)]
def gersh(A):
 assert A==trans(A)
 return min((A[i][i]-sum((abs(A[i][j]) for j in range(N) if i!=j),Q(0))
             for i in range(N)))
def qf(v,A):
 return sum((v[i]*A[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def exact_psd(A):
 assert A==trans(A)
 mat=[list(x) for x in A]
 for j in range(N):
  d=mat[j][j]
  assert d>=0
  if d==0:
   assert all(mat[j][k]==0 for k in range(j+1,N))
   continue
  for i in range(j+1,N):
   for k in range(i,N):
    mat[i][k]-=mat[j][i]*mat[j][k]/d
    mat[k][i]=mat[i][k]
 return True
def negative_report(A,cls,wit):
 if cls=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  v=[Q(x) for x in wit["rational_vector"]]
  assert len(v)==N and any(v)
  assert qf(v,A)==Q(wit["exact_negative_quadratic"])<0
 elif cls=="POSITIVE_EXACT_RATIONAL_LDL":
  mat=[r[:] for r in A]
  for j in range(N):
   d=mat[j][j]
   assert d>0
   for i in range(j+1,N):
    for k in range(i,N):
     mat[i][k]-=mat[j][i]*mat[j][k]/d
     mat[k][i]=mat[i][k]
 else:assert cls=="INCONCLUSIVE"
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg47","mg55"):
  p.add_argument("--verified-"+k+"-json",required=True)
 arg=p.parse_args()
 d={k:json.loads((ROOT/getattr(arg,"verified_"+k+"_json")).read_text())
    for k in ("mg24","mg47","mg55")}
 a24,a47,mg55=d["mg24"],d["mg47"],d["mg55"]
 assert mg55["status"]=="ORIGINAL_MG55_FULL_FREQUENCY_RESPONSE_HOMOTOPY_24D"
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in d.values())
 assert mg55["all_response_blends_full_source_Loewner_valid"]
 assert mg55["original_all_18_pairwise_rational_response_blends_evaluated"]
 hm,hr,he=original_H24_from_physical_source()
 assert he==Q(a24["physical_Gram_Loewner_row_error"])
 hlo=sub(hm,scale(he,eye()))
 endpoints=[]
 for idx,(base,saved) in enumerate(zip(a47["scenarios"],mg55["original_four_response_endpoints"])):
  assert (base["mesh_cells"],base["cutoff_k"])==(saved["mesh_cells"],saved["cutoff_k"])
  B=rd(base["full_original_rational_response_B"])
  U=rd(base["selected_complete_24D_source_upper"])
  assert B==rd(saved["original_response_B"]) and U==rd(saved["complete_24D_upper"])
  assert hlo==add(U,rd(base["selected_complete_24D_source_lower"]))
  assert exact_psd(U)
  g=gersh(sub(hlo,U))
  assert g==Q(saved["exact_original_Gersh"])
  ray=[Q(x) for x in base["selected_exact_inertia_witness"]["rational_vector"]]
  assert qf(ray,sub(hlo,U))==Q(base["selected_exact_inertia_witness"]["exact_negative_quadratic"])<0
  endpoints.append((B,U,g))
 assert len(endpoints)==4
 # Independent continuum certificate obstruction. By the affine
 # residual identity and PSD strong moment, SUM w_i U_i bounds the
 # ORIGINAL whole operator residual for the changed B(w). If a single
 # accepted rational source ray is negative for ALL four Hlo-U_i,
 # it stays negative under EVERY convex combination (not merely
 # the tested finite set of 18 weights).
 common=[Q(x) for x in a47["scenarios"][0]["selected_exact_inertia_witness"]["rational_vector"]]
 charges=[qf(common,sub(hlo,u)) for _,u,_ in endpoints]
 assert len(common)==N and any(common) and all(z<0 for z in charges)
 assert [str(x) for x in common]==mg55["original_common_negative_exact_rational_source_ray"]
 assert [str(x) for x in charges]==mg55["original_common_negative_exact_source_lower_quadratics"]
 assert mg55["whole_four_endpoint_convex_response_certificate_hull_obstructed"]
 assert mg55["all_nonnegative_barycentric_response_weights_covered_by_affine_identity"]
 L={}
 for k in (12,16):
  source=next(r for r in a24["cases"] if r["cutoff_k"]==k)
  Lo=rd(source["complete_Sstar_lower"])
  assert Lo==trans(Lo)
  minusLo=scale(-1,Lo)
  assert exact_psd(minusLo)
  saved=mg55["archived_MG24_strong_moment_lower_is_negative_semidefinite"][str(k)]
  assert rd(saved["negative_Sstar_lower_matrix"])==minusLo
  assert sum((minusLo[i][i] for i in range(N)),Q(0))==Q(saved["negative_Sstar_lower_trace"])
  L[k]=minusLo
 expected=[(i,j,t) for i,j in combinations(range(4),2)
                   for t in (Q(1,4),Q(1,2),Q(3,4))]
 best=max(g for _,_,g in endpoints)
 assert best==Q(mg55["best_archived_original_Gersh"])
 assert len(expected)==len(mg55["trials"])==18
 improvements=positive=curv_checks=0
 for (i,j,t),row in zip(expected,mg55["trials"]):
  assert row["original_response_endpoint_indices"]==[i,j]
  assert Q(row["theta"])==t
  B0,U0,_=endpoints[i]
  B1,U1,_=endpoints[j]
  Delta=sub(B1,B0)
  B=add(scale(1-t,B0),scale(t,B1))
  U=add(scale(1-t,U0),scale(t,U1))
  M=sub(hlo,U)
  assert B==rd(row["new_changed_original_response_B"])
  assert U==rd(row["new_original_full_frequency_valid_upper"])
  assert M==rd(row["new_original_full_frequency_lower"])
  assert exact_psd(U)
  g=gersh(M)
  assert str(g)==row["new_original_exact_Gersh"]
  assert row["strict_improvement_vs_best_archived"]==(g>best)
  assert Q(row["max_historical_MG43_Gersh"])==best
  negative_report(M,row["inertia_classification"],row["inertia_exact_witness"])
  improvements+=int(g>best)
  positive+=int(row["inertia_classification"]=="POSITIVE_EXACT_RATIONAL_LDL")
  for k in (12,16):
   # Original F-AF B is affine in response B, even with true sinh pole.
   # The true strong moment is nonnegative, while archived lower Lo<=0.
   # Thus the MG24 curvature correction is necessarily a PSD CHARGE.
   P=scale(t*(1-t),sand(L[k],Delta))
   assert exact_psd(P)
   strong=add(U,P)
   assert exact_psd(sub(strong,U))
   details=row["strong_moment_MG24_curvature_penalty"][str(k)]
   assert Q(details["correct_original_curvature_upper_additional_PSD_trace"])==sum(P[a][a] for a in range(N))
   assert Q(details["original_curvature_upper_Gersh"])==gersh(sub(hlo,strong))
   assert gersh(sub(hlo,strong))<=g
   assert details["stored_original_strong_curvature_cannot_tighten_convex_upper"]
   curv_checks+=1
 assert curv_checks==36 and improvements==mg55["strict_full24_Gersh_improvements"]
 assert positive==mg55["new_full24_source_contractions"]
 assert mg55["original_all_36_strong_curvature_sign_tests"]
 assert mg55["finite_grid_only_not_global_B_optimality"]
 assert not mg55["original_470D_inverse"]
 assert not mg55["original_signed_51over56_cap"]
 assert mg55["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert mg55["even_Weil_CC27_RH"]=="OPEN"
 print("MG55 INDEPENDENT original full-frequency changed-response homotopy PASS",
  {"trials":len(expected),"strong_curvature_checks":curv_checks,
   "improved_vs_MG43":improvements,"positive_source_cases":positive,
   "original_470D_and_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
