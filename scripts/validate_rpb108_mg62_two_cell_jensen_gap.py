#!/usr/bin/env python3
"""MG62 original physical strong-action: two-Fourier-cell Jensen singular-gap gate.

Unlike MG61's 2D Young moment lower, directly use Jensen on TWO
distinct exact original physical frequency cells to lower-bound
strong-action energy by the squared TWO measured cell means.

For each genuine original cell I of width h>0, the projected
pole-corrected physical strong-action response y=(y_u,y_w) satisfies
mean(y)_I = c_I+delta_I with |delta_I,i|<=rho_I,i. The shared source
pole-error and multiplier scalar are already combined correctly in
MG59's accepted projected action source interval.

For two cells, Q=sum 2h c c^T, E=sum 2h sum rho_i^2.
Actual two-cell original strong moment >= (sqrt(lambda_min(Q))-sqrt(E))^2 I.
Exact rational lambda_min(Q)>=det(Q)/tr(Q)=L>0.
If L>E, exact rational coercivity >= (L-E)^2/(4L)>0.
This certifies a source-PLANE lower (not a global 24D Loewner matrix).
Heuristic float scores only propose cell pairs: proof is exact rational.
"""
import argparse,json,sys,math
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg59_projected_true_action_plane as m59
N=24;P=23
V=tuple(Q(x) for x in m59.ANCHOR)
def unbox(x):
 return (Q(x["left"]),Q(x["right"]),Q(x["multiplier_lower"]),
  Q(x["multiplier_upper"]),[Q(z) for z in x["source_midpoint"]],
  [Q(z) for z in x["source_derivative"]],
  [Q(z) for z in x["source_error"]])
def source55(a57,a58):
 basic=m59.accepted_original_41_source_cells(a57)
 q=next(z for z in a58["candidates"] if z["new_subdivisions_per_original_cell"]==8)
 cells=[unbox(x) for x in q["new_actual_physical_fourier_source_cells"]]
 assert len(cells)==16
 ans=[]
 for c in basic:
  if c[0]==Q(5,8):ans.extend(cells[:8])
  elif c[0]==Q(3,4):ans.extend(cells[8:])
  else:ans.append(c)
 assert len(ans)==55 and ans[0][0]==0 and ans[-1][1]==4
 assert all(ans[i][1]==ans[i+1][0] for i in range(54))
 return ans
def projected(cells,u,w,b,berr):
 entries=[]
 for cell in cells:
  width=cell[1]-cell[0]
  assert width>0
  a=m59.project_one(u,cell,b,berr)
  c=m59.project_one(w,cell,b,berr)
  assert len(a)==len(c)==6
  y=[a[0],c[0]];r=[a[2],c[2]]
  assert all(x>=0 for x in r)
  entries.append((width,y,r))
 return entries
def asfloat(q):
 try:return float(q)
 except OverflowError:
  if q==0:return 0.
  n,d=q.numerator,q.denominator
  return math.copysign(float("inf"),n) if n.bit_length()-d.bit_length()>1023 else float(n//d)
def pair_exact(entries,i,j,norm):
 cells=[entries[i],entries[j]]
 q00=q01=q11=error=Q(0)
 for h,y,r in cells:
  f=2*h
  q00+=f*y[0]*y[0]
  q01+=f*y[0]*y[1]
  q11+=f*y[1]*y[1]
  error+=f*(r[0]*r[0]+r[1]*r[1])
 determinant=q00*q11-q01*q01
 tr=q00+q11
 lam=determinant/tr if tr>0 else Q(0)
 good=lam>error and lam>0
 own=(lam-error)**2/(4*lam) if good else None
 c=own/norm if good else None
 return {"source_cell_indices":[i,j],
         "original_cell_interval_endpoints":[[str(c[0]),str(c[0]+c[0]*0)] for c in []],
         "center_gram00":str(q00),"center_gram01":str(q01),"center_gram11":str(q11),
         "center_gram_determinant":str(determinant),
         "center_min_singular_squared_lower":str(lam),
         "original_two_cell_mean_error_Frobenius_squared_upper":str(error),
         "exact_positive_2D_singular_gap":good,
         "strict_original_restricted_source_coercivity":str(c) if good else None,
         "not_original_global24_rank2_Loewner":True}
def choose(entries):
 # The float is NEVER used to prove positivity, only to select original
 # physical cell pairs for replay of exact rational singular-gap tests.
 v=[(asfloat(h),[asfloat(x) for x in y],[asfloat(x) for x in r])
    for h,y,r in entries]
 scored=[]
 for i in range(len(v)):
  h1,y1,r1=v[i]
  for j in range(i+1,len(v)):
   h2,y2,r2=v[j]
   a=2*h1*y1[0]**2+2*h2*y2[0]**2
   b=2*h1*y1[0]*y1[1]+2*h2*y2[0]*y2[1]
   c=2*h1*y1[1]**2+2*h2*y2[1]**2
   er=2*h1*(r1[0]**2+r1[1]**2)+2*h2*(r2[0]**2+r2[1]**2)
   if a+c>0 and math.isfinite(a+b+c+er):
    gap=max(0.,a*c-b*b)/(a+c)-er
   else:gap=float("-inf")
   scored.append((gap,i,j))
 scored.sort(reverse=True)
 assert len(scored)==1485
 return [(i,j) for _,i,j in scored[:3]]
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg57","mg58","mg61"):
  p.add_argument("--verified-"+k+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg62_original_two_cell_Jensen_source_plane.json")
 z=p.parse_args()
 a={k:json.loads((ROOT/getattr(z,"verified_"+k+"_json")).read_text())
    for k in ("mg24","mg57","mg58","mg61")}
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in a.values())
 assert a["mg61"]["status"]=="ORIGINAL_MG61_REBALANCED_ORTHOGONAL_55CELL_2D_SOURCE_MOMENT"
 assert a["mg61"]["num_strict_positive_2D"]==0
 assert a["mg58"]["selected_refinement_n"]==8
 H,Rad,e=original_H24_from_physical_source()
 assert e==Q(a["mg24"]["physical_Gram_Loewner_row_error"])
 b=[H[i][P] for i in range(N)]
 brad=[Rad[i][P] for i in range(N)]
 cells=source55(a["mg57"],a["mg58"])
 results=[]
 for alpha in (Q(1,9),Q(1,18)):
  u=tuple(alpha*x for x in V)
  for k in range(N):
   w=tuple(Q(j==k)-Q(V[k])*V[j]/82 for j in range(N))
   assert m59.dot(V,w)==0
   norm=m59.dot(u,u)+m59.dot(w,w)
   entries=projected(cells,u,w,b,brad)
   candidates=choose(entries)
   tests=[]
   for i,j in candidates:
    t=pair_exact(entries,i,j,norm)
    t["original_cell_interval_endpoints"]=[
      [str(cells[idx][0]),str(cells[idx][1])] for idx in (i,j)]
    tests.append(t)
   results.append({"original_coordinate":k,"anchor_scale":str(alpha),
                   "original_second_orthogonal_vector":[str(x) for x in w],
                   "source_plane_coordinate_norm_trace":str(norm),
                   "tested_original_cell_pair_count":3,
                   "positive_two_cell_source_pair_count":sum(x["exact_positive_2D_singular_gap"] for x in tests),
                   "exact_original_Jensen_pair_tests":tests})
   if k in (0,5,11,23):
    print("MG62 original two-cell source Jensen gap",{
      "scale":str(alpha),"axis":k,"success":results[-1]["positive_two_cell_source_pair_count"]},flush=True)
 winners=[(r,test) for r in results for test in r["exact_original_Jensen_pair_tests"]
          if test["exact_positive_2D_singular_gap"]]
 best=max(winners,key=lambda x:Q(x[1]["strict_original_restricted_source_coercivity"])) if winners else None
 output={"status":"ORIGINAL_MG62_TWO_REAL_FOURIER_CELL_JENSEN_SINGULAR_SOURCE_PLANE_GATE",
         "canonical_W_ODD_NEG":"OPEN",
         "accepted_runs":{"MG24":39378465438,"MG57":39897754515,
                          "MG58":39902364126,"MG61":39963056297},
         "genuine_original_full24_pole_corrected_action":True,
         "genuine_original_55_physical_Fourier_cells":True,
         "two_measured_physical_cell_mean_interval_Jensen":True,
         "original_negative_frequency_mirror_factor_two":True,
         "actual_original_strong_energy_remaining_frequency_PSD":True,
         "interval_scalar_multiplier_and_pole_source_shared":True,
         "float_proposal_not_mathematical_acceptance":True,
         "exact_rational_coercivity_acceptance_only":True,
         "tested_original_source_planes":48,
         "tested_genuine_cell_pairs":len(results)*3,
         "strict_positive_2D_planes_certified":sum(r["positive_two_cell_source_pair_count"]>0 for r in results),
         "best_original_source_coordinate":best[0]["original_coordinate"] if best else None,
         "best_original_source_scale":best[0]["anchor_scale"] if best else None,
         "best_exact_original_source_coercivity_constant":best[1]["strict_original_restricted_source_coercivity"] if best else None,
         "no_original_global_24D_rank_two_Loewner":True,
         "no_original_24D_source_residual_contraction":True,
         "no_original_470D_inverse":True,
         "no_original_signed_51over56_odd_cap":True,
         "independent_original_Fourier_form_domain_audit":"OPEN",
         "even_Weil_CC27_RH":"OPEN",
         "results":results}
 path=ROOT/z.output;path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(output,indent=2)+"\n")
 print("MG62 ORIGINAL two physical cell Jensen source-plane exact rational result",{
  "source_planes":48,"pair_tests":len(results)*3,
  "strict_positive_planes":output["strict_positive_2D_planes_certified"],
  "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
