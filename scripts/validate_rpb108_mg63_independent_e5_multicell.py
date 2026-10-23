#!/usr/bin/env python3
"""MG63 independent replay: original physical coordinate-5 multiple-cell 2D Jensen.

Does not import MG63 producer, MG62 producer, or its proposal algorithm.
Regenerate all 55 genuine original physical Fourier cells from the
independent MG58 original physical primitive generator plus MG57.
Recompute true pole-column intervals from MG24 and projected source
means/errors via separately authored MG59 independent action_cell.
For EACH archived exact selected source subset of 2..55 cells, verify
full exact rational Gram entries, physical Frobenius uncertainty,
strict determinant/trace gap, positive coefficient-source constant.

Only a strict source-plane restriction is certified, never full24.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg58_independent_adaptive_2D_replay import generator_cells
from validate_rpb108_mg59_independent_projected_plane import build_cells,action_cell,dot
N=24;P=23
ANCHOR=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
def independent55(a57,a58):
 accepted=next(x for x in a58["candidates"] if x["new_subdivisions_per_original_cell"]==8)
 new=generator_cells(8)
 assert len(new)==len(accepted["new_actual_physical_fourier_source_cells"])==16
 for a,b in zip(new,accepted["new_actual_physical_fourier_source_cells"]):
  assert [str(x) for x in a[:4]]==[b["left"],b["right"],b["multiplier_lower"],b["multiplier_upper"]]
  assert [str(x) for x in a[4]]==b["source_midpoint"]
  assert [str(x) for x in a[5]]==b["source_derivative"]
  assert [str(x) for x in a[6]]==b["source_error"]
 old=build_cells(a57)
 full=[]
 for x in old:
  if x[0]==F(5,8):full.extend(new[:8])
  elif x[0]==F(3,4):full.extend(new[8:])
  else:full.append(x)
 assert len(full)==55 and full[0][0]==0 and full[-1][1]==4
 assert all(full[k][1]==full[k+1][0] for k in range(54))
 return full
def make_original_data(physical,u,w,b,berr):
 data=[]
 for source in physical:
  a=action_cell(u,source,b,berr)
  e=action_cell(w,source,b,berr)
  h=source[1]-source[0]
  assert h>0 and a[2]>=0 and e[2]>=0
  factor=2*h
  data.append((
    factor*a[0]**2,
    factor*a[0]*e[0],
    factor*e[0]**2,
    factor*(a[2]**2+e[2]**2)))
 return data
def audit_subset(parts,archive,scale):
 ix=archive["genuine_physical_cell_indices"]
 assert len(ix)==archive["original_selected_cell_count"]
 assert len(ix)>=2 and ix==sorted(ix) and len(set(ix))==len(ix)
 assert all(isinstance(i,int) and 0<=i<55 for i in ix)
 q00=sum((parts[i][0] for i in ix),F(0))
 q01=sum((parts[i][1] for i in ix),F(0))
 q11=sum((parts[i][2] for i in ix),F(0))
 error=sum((parts[i][3] for i in ix),F(0))
 det=q00*q11-q01*q01;tr=q00+q11
 assert q00>=0 and q11>=0 and error>=0
 lower=det/tr if tr>0 else F(0)
 good=lower>error and lower>0
 expected=((lower-error)**2/(4*lower*(82*scale*scale+1)) if good else None)
 for key,val in (("center_gram_00",q00),("center_gram_01",q01),
                 ("center_gram_11",q11),
                 ("exact_center_gram_determinant",det),
                 ("center_min_singular_sq_lower",lower),
                 ("true_original_physical_mean_error_Frobenius_sq_upper",error)):
  assert F(archive[key])==val
 assert archive["strict_positive_original_2D_singular_gap"]==good
 if good:
  assert expected>0
  assert F(archive["exact_restricted_source_coercivity"])==expected
 else:assert archive["exact_restricted_source_coercivity"] is None
 assert archive["no_global_24D_rank_two_claim"]
 return good,expected
def main():
 p=argparse.ArgumentParser()
 for name in ("mg24","mg57","mg58","mg62","mg63"):
  p.add_argument("--verified-"+name+"-json",required=True)
 args=p.parse_args()
 a={k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
    for k in ("mg24","mg57","mg58","mg62","mg63")}
 output=a["mg63"]
 assert output["status"]=="ORIGINAL_MG63_GENUINE_E5_MULTICELL_JENSEN_2D_SOURCE"
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in a.values())
 assert output["last_uncertified_MG62_coordinate_plane_5"]
 assert output["source_anchor_v5_zero_and_norm_sq_82"]
 assert output["exact_rational_cell_mean_singular_gap_acceptance"]
 assert output["floating_heuristics_proposal_only"]
 assert a["mg62"]["strict_positive_2D_planes_certified"]==41
 assert ANCHOR[5]==0 and sum(x*x for x in ANCHOR)==82
 physical=independent55(a["mg57"],a["mg58"])
 hm,hr,herr=original_H24_from_physical_source()
 assert herr==F(a["mg24"]["physical_Gram_Loewner_row_error"])
 b=[hm[k][P] for k in range(N)]
 berr=[hr[k][P] for k in range(N)]
 e5=tuple(F(k==5) for k in range(N))
 scales=(F(1,18),F(1,128),F(1,256),F(1,512),F(1,1024),F(1,2048))
 sizes=(2,3,4,6,8,12,16,24,32,55)
 assert len(output["cases"])==len(scales)==output["number_original_anchor_scales"]
 assert output["total_original_physical_cells"]==55
 positive=0;best=None;sampled=0
 for alpha,case in zip(scales,output["cases"]):
  assert F(case["anchor_scale"])==alpha
  assert case["canonical_original_second_direction"]=="e5"
  assert case["exact_source_plane_span"]=="span(v,e5)"
  assert case["original_anchor_source_norm_squared"]=="82"
  u=[alpha*F(x) for x in ANCHOR]
  assert dot(u,e5)==0 and dot(u,u)==82*alpha*alpha
  parts=make_original_data(physical,u,e5,b,berr)
  rows=case["selected_best_exact_subset_for_each_size"]
  assert len(rows)==len(sizes)
  for n,row in zip(sizes,rows):
   assert row["subset_size"]==n
   assert row["number_proposed_subsets"]>=1
   assert row["number_proposed_subsets"]==case["candidate_counts_by_subset_size"][str(n)]
   test=row["best_exact_rational_subset"]
   success,constant=audit_subset(parts,test,alpha)
   assert len(test["genuine_physical_cell_indices"])==n
   # Selected positive best must itself carry an exact positive gap.
   if row["strict_positive_subsets_evaluated"]>0:
    assert success and constant>0
   if success:
    positive+=1
    if best is None or constant>best[0]:
     best=(constant,alpha,test)
   sampled+=row["number_proposed_subsets"]
 assert sampled==output["total_tested_selected_subsets"]
 assert bool(positive)==output["coordinate5_positive_source_plane_certified"]
 if best:
  assert F(output["best_source_balancing_scale"])==best[1]
  assert F(output["best_positive_e5_source_subspace_constant"])==best[0]
  assert output["best_positive_e5_cell_indices"]==best[2]["genuine_physical_cell_indices"]
 else:
  assert output["best_source_balancing_scale"] is None
  assert output["best_positive_e5_source_subspace_constant"] is None
  assert output["best_positive_e5_cell_indices"] is None
 assert not output["global_original_24D_source_action_coercivity"]
 assert not output["global_original_24D_source_residual_contraction"]
 assert not output["original_full470_inverse"]
 assert not output["signed_odd_51over56_cap"]
 assert output["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert output["even_Weil_CC27_RH"]=="OPEN"
 print("MG63 INDEPENDENT original true 55-cell coordinate5 multiple-cell Jensen exact subset replay PASS",{
  "source_scales":len(scales),"independent_exact_selected_subsets":len(scales)*len(sizes),
  "producer_candidate_count":sampled,
  "positive_recorded_subsets":positive,
  "strict_coordinate5_source2D":bool(positive),
  "RH":"OPEN"},flush=True)
if __name__=="__main__":main()
