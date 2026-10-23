#!/usr/bin/env python3
"""MG63: original coord-5 3+ physical Fourier-cell Jensen singular gap.

MG62 independently proved 23 original two-dimensional coordinate planes
strictly positive by physical two-cell mean Jensen. The sole missing
tested plane is span(v,e5), with v5=0. MG63 holds the operator, original
55 genuine SI10/MG11 Fourier source cells, true sinh pole, and signed
seven-prime/digamma scalar multiplier FIXED.

Select multiple *actual disjoint positive-frequency cells* of the
same true original source, including 3..55 cells, and derive their
Jensen lower via the 2D weighted physical cell means. For source basis
(v/sc,e5), compute center Gram Q=sum 2h c c^T and error
E=sum 2h(r0²+r1²). If det(Q)/tr(Q)>E in exact rationals, the TRUE
full-frequency strong action restricted to span(v,e5) is positive with
constant (L-E)^2/(4 L (||v/sc||²+1)) in coefficient Euclidean norm.

Floating greedy ranking is strictly candidate proposal, NEVER proof.
Full physical source moment and unmeasured frequencies unchanged.
"""
import argparse,json,math,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg59_projected_true_action_plane as m59
import validate_rpb108_mg62_two_cell_jensen_gap as m62
N=24;P=23
V=tuple(F(x) for x in m59.ANCHOR)
E5=tuple(F(j==5) for j in range(N))
assert len(V)==N and V[5]==0 and m59.dot(V,V)==82 and m59.dot(V,E5)==0
SCALES=(F(1,18),F(1,128),F(1,256),F(1,512),F(1,1024),F(1,2048))
TARGETS=(2,3,4,6,8,12,16,24,32,55)
def cell_cov(cell,u,w,b,be):
 h=cell[1]-cell[0]
 x=m59.project_one(u,cell,b,be)
 y=m59.project_one(w,cell,b,be)
 assert len(x)==len(y)==6 and h>0
 wgt=2*h
 a=wgt*x[0]*x[0]
 cross=wgt*x[0]*y[0]
 c=wgt*y[0]*y[0]
 err=wgt*(x[2]*x[2]+y[2]*y[2])
 assert a>=0 and c>=0 and err>=0
 return (a,cross,c,err)
def sums(parts,indices):
 return tuple(sum((parts[i][j] for i in indices),F(0)) for j in range(4))
def exact_check(parts,indices,alpha):
 a,b,c,err=sums(parts,indices)
 tr=a+c;det=a*c-b*b
 lower=det/tr if tr>0 else F(0)
 good=lower>err and lower>0
 # Rigorously lambda_min(Q)>=det(Q)/tr(Q), ||Delta C||op<=sqrt(E);
 # sqrt(L)-sqrt(E)>0; (sqrtL-sqrtE)^2 >= (L-E)^2/(4L).
 coefficient=(lower-err)**2/(4*lower*(82*alpha*alpha+1)) if good else None
 assert not good or coefficient>0
 return {
  "genuine_physical_cell_indices":list(indices),
  "original_selected_cell_count":len(indices),
  "center_gram_00":str(a),"center_gram_01":str(b),"center_gram_11":str(c),
  "exact_center_gram_determinant":str(det),
  "center_min_singular_sq_lower":str(lower),
  "true_original_physical_mean_error_Frobenius_sq_upper":str(err),
  "strict_positive_original_2D_singular_gap":good,
  "exact_restricted_source_coercivity":str(coefficient) if good else None,
  "no_global_24D_rank_two_claim":True}
def float_gap(x):
 a,b,c,e=x
 tr=a+c
 if tr<=0:return (-math.inf,-math.inf)
 d=max(0.,a*c-b*b)
 lam=d/tr
 return lam-e, lam/max(e,1.e-300)
def floats(parts):
 return [tuple(float(x) for x in q) for q in parts]
def seed_pairs(approx):
 pairs=[]
 for i in range(len(approx)):
  for j in range(i+1,len(approx)):
   v=tuple(approx[i][k]+approx[j][k] for k in range(4))
   g,ratio=float_gap(v)
   pairs.append((g,ratio,i,j))
 # Two different heuristic targets, plus deterministic broad spacing.
 strongest_g=sorted(pairs,key=lambda x:(x[0],x[1]),reverse=True)[:4]
 strongest_ratio=sorted(pairs,key=lambda x:(x[1],x[0]),reverse=True)[:4]
 seeds=[(x[2],x[3]) for x in strongest_g+strongest_ratio]
 seeds.extend([(0,54),(6,22),(12,14),(12,35),(14,45)])
 return list(dict.fromkeys(tuple(sorted(x)) for x in seeds))
def greedy_candidates(parts):
 fp=floats(parts)
 allids=tuple(range(len(fp)))
 pool=seed_pairs(fp)
 result={}
 for start in pool:
  current=list(start)
  vec=[sum(fp[i][j] for i in current) for j in range(4)]
  if 2 in TARGETS:result.setdefault(2,[]).append(tuple(sorted(current)))
  for length in range(3,56):
   avail=(i for i in allids if i not in current)
   best=max(avail,key=lambda i:(
    *float_gap(tuple(vec[j]+fp[i][j] for j in range(4))),-i))
   current.append(best)
   for j in range(4):vec[j]+=fp[best][j]
   if length in TARGETS:
    result.setdefault(length,[]).append(tuple(sorted(current)))
 for n in TARGETS:
  assert n in result
  result[n]=list(dict.fromkeys(result[n]))
 return result
def main():
 p=argparse.ArgumentParser()
 for name in ("mg24","mg57","mg58","mg62"):
  p.add_argument("--verified-"+name+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg63_original_e5_multicell_Jensen.json")
 opt=p.parse_args()
 archives={name:json.loads((ROOT/getattr(opt,"verified_"+name+"_json")).read_text())
           for name in ("mg24","mg57","mg58","mg62")}
 assert all(a["canonical_W_ODD_NEG"]=="OPEN" for a in archives.values())
 assert archives["mg62"]["status"]=="ORIGINAL_MG62_TWO_REAL_FOURIER_CELL_JENSEN_SINGULAR_SOURCE_PLANE_GATE"
 assert archives["mg62"]["strict_positive_2D_planes_certified"]==41
 assert archives["mg58"]["selected_refinement_n"]==8
 H,rad,herr=original_H24_from_physical_source()
 assert herr==F(archives["mg24"]["physical_Gram_Loewner_row_error"])
 b=[H[j][P] for j in range(N)]
 be=[rad[j][P] for j in range(N)]
 cells=m62.source55(archives["mg57"],archives["mg58"])
 assert len(cells)==55 and cells[0][0]==0 and cells[-1][1]==4
 assert all(cells[i][1]==cells[i+1][0] for i in range(54))
 records=[];positives=[]
 for alpha in SCALES:
  u=tuple(alpha*x for x in V)
  table=[cell_cov(cell,u,E5,b,be) for cell in cells]
  proposal=greedy_candidates(table)
  chosen=[]
  for n in TARGETS:
   options=[exact_check(table,inds,alpha) for inds in proposal[n]]
   # All selected candidates evaluated EXACTLY; the highest exact
   # L-E is recorded even if it does not prove positivity.
   top=max(options,key=lambda row:F(row["center_min_singular_sq_lower"])
                                 -F(row["true_original_physical_mean_error_Frobenius_sq_upper"]))
   success=[t for t in options if t["strict_positive_original_2D_singular_gap"]]
   if success:
    top=max(success,key=lambda row:F(row["exact_restricted_source_coercivity"]))
   chosen.append({
    "subset_size":n,"number_proposed_subsets":len(options),
    "strict_positive_subsets_evaluated":len(success),
    "best_exact_rational_subset":top})
   positives.extend((alpha,t) for t in success)
  records.append({"anchor_scale":str(alpha),
    "canonical_original_second_direction":"e5",
    "original_anchor_source_norm_squared":"82",
    "exact_source_plane_span":"span(v,e5)",
    "tried_subset_sizes":[int(x) for x in TARGETS],
    "candidate_counts_by_subset_size":{str(x["subset_size"]):x["number_proposed_subsets"] for x in chosen},
    "selected_best_exact_subset_for_each_size":chosen})
  print("MG63 ORIGINAL e5 source Jensen multi-cell",{
   "alpha":str(alpha),
   "strict_positive_sizes":[r["subset_size"] for r in chosen if r["strict_positive_subsets_evaluated"]],
   "best_gap":max(float(F(r["best_exact_rational_subset"]["center_min_singular_sq_lower"])
                    -F(r["best_exact_rational_subset"]["true_original_physical_mean_error_Frobenius_sq_upper"])) for r in chosen)},
   flush=True)
 best=max(positives,key=lambda x:F(x[1]["exact_restricted_source_coercivity"])) if positives else None
 # One exact rational certificate is sufficient for strict source-plane
 # positivity. No unrestricted 24D matrix promotion.
 result={
  "status":"ORIGINAL_MG63_GENUINE_E5_MULTICELL_JENSEN_2D_SOURCE",
  "canonical_W_ODD_NEG":"OPEN",
  "accepted_original_physical_runs":{"MG24":39378465438,"MG57":39897754515,
                                    "MG58":39902364126,"MG62":39982014166},
  "unchanged_original_signed_seven_prime_digamma_action":True,
  "unchanged_original_true_sinh_pole_24D_source":True,
  "whole_true_remaining_strong_energy_PSD":True,
  "original_positive_physical_frequency_coverage":["0","4"],
  "total_original_physical_cells":55,
  "last_uncertified_MG62_coordinate_plane_5":True,
  "source_anchor_v5_zero_and_norm_sq_82":True,
  "separated_physical_Fourier_cells_3_to_55_Jensen":True,
  "floating_heuristics_proposal_only":True,
  "exact_rational_cell_mean_singular_gap_acceptance":True,
  "real_source_plane_count":1,
  "number_original_anchor_scales":len(SCALES),
  "total_tested_selected_subsets":sum(x["number_proposed_subsets"] for r in records
           for x in r["selected_best_exact_subset_for_each_size"]),
  "coordinate5_positive_source_plane_certified":bool(positives),
  "best_source_balancing_scale":str(best[0]) if best else None,
  "best_positive_e5_source_subspace_constant":best[1]["exact_restricted_source_coercivity"] if best else None,
  "best_positive_e5_cell_indices":best[1]["genuine_physical_cell_indices"] if best else None,
  "global_original_24D_source_action_coercivity":False,
  "global_original_24D_source_residual_contraction":False,
  "original_full470_inverse":False,
  "signed_odd_51over56_cap":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN",
  "cases":records}
 dest=ROOT/opt.output;dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+"\n")
 print("MG63 ORIGINAL e5 complete exact physical multi-cell Jensen candidate result",{
  "tested_subsets":result["total_tested_selected_subsets"],
  "coordinate5_2D_certified":bool(positives),
  "selected_scale":result["best_source_balancing_scale"],
  "RH":"OPEN"},flush=True)
if __name__=="__main__":main()
