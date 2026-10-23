#!/usr/bin/env python3
"""MG60 INDEPENDENT replay of original MG58+MG59 COMPOSED source construction.

Never imports MG60 producer. Recreates all genuine MG58 original
positive physical Fourier subcells using a separate accepted MG58
independent original-source generator; reconstructs the full 41-cell
MG57 baseline through MG59's independent verifier; then computes all
50 2x2 projected true pole-corrected action covariance enclosures
using MG59's separately authored exact Young accumulator.

Each claimed positive 2D lower needs strict rational determinant and
explicit norm constant, while any negative instance is no physical
negative mode. This is restricted original source, NOT full24.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg58_independent_adaptive_2D_replay import generator_cells
from validate_rpb108_mg59_independent_projected_plane import build_cells,replay,qf,dot
N=24;P=23
def reconstructed_cells(a57,n):
 baseline=build_cells(a57)
 new=generator_cells(n)
 assert len(new)==2*n
 cells=[]
 for x in baseline:
  if x[0]==Q(5,8):cells.extend(new[:n])
  elif x[0]==Q(3,4):cells.extend(new[n:])
  else:cells.append(x)
 assert len(cells)==41+2*(n-1)
 assert cells[0][0]==0 and cells[-1][1]==4
 assert sum((x[1]-x[0] for x in cells),Q(0))==4
 assert all(cells[k][1]==cells[k+1][0] for k in range(len(cells)-1))
 return cells,new
def exact_gram(L,row):
 a=L[0][0];b=L[0][1];c=L[1][1]
 assert L[1][0]==b
 determinant=a*c-b*b
 assert determinant==Q(row["exact_2D_determinant"])
 positive=a>0 and c>0 and determinant>0
 assert positive==row["exact_positive_2D"]
 assert row["full24_global_rank_two_Loewner_NOT_proved"]
 if positive:
  u=[Q(z) for z in row["first_original_source_coefficients"]]
  v=[Q(z) for z in row["second_original_source_coefficients"]]
  norms=dot(u,u)+dot(v,v)
  assert norms>0
  const=determinant/((a+c)*norms)
  assert const>0
  assert const==Q(row["exact_2D_restricted_coefficient_norm_lower"])
 else:
  assert row["exact_2D_restricted_coefficient_norm_lower"] is None
 return positive
def main():
 p=argparse.ArgumentParser()
 for x in ("mg24","mg57","mg58","mg59","mg60"):
  p.add_argument("--verified-"+x+"-json",required=True)
 args=p.parse_args()
 data={x:json.loads((ROOT/getattr(args,"verified_"+x+"_json")).read_text())
       for x in ("mg24","mg57","mg58","mg59","mg60")}
 a24,a57,a58,a59,a60=[data[x] for x in ("mg24","mg57","mg58","mg59","mg60")]
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in data.values())
 assert a60["status"]=="ORIGINAL_MG60_COMPOSED_TRUE_REFINED_PROJECTED_ACTION_2D_LOEWER"
 assert a60["all_50_projected_two_plane_rational_moments"]
 assert a60["original_MG58_two_physical_partitions_47_and_55_cells"]
 assert a60["original_MG59_project_before_multiplier_and_pole_absolute"]
 assert len(a60["source_cases"])==2
 assert a58["status"]=="ORIGINAL_MG58_TRUE_FOURIER_ADAPTIVE_2D_STRONG_SUBSPACE"
 assert a59["status"]=="ORIGINAL_MG59_TRUE_ACTION_PREPROJECTED_TWO_PLANE_LOEWER"
 assert a58["selected_conservative_positive_index"]==1
 assert a59["strict_positive_original_2D_subspaces"]==0
 physical,prad,herr=original_H24_from_physical_source()
 assert herr==Q(a24["physical_Gram_Loewner_row_error"])
 b=[physical[i][P] for i in range(N)]
 berr=[prad[i][P] for i in range(N)]
 baseline=build_cells(a57)
 assert len(baseline)==41
 labels=[("coordinate_"+str(i),tuple(int(j==i) for j in range(N)))
         for i in range(N)]
 alternate=(-33,-2,-23,21,22,2,11,23,14,24,24,15,11,-22,-25,22,2,21,22,25,25,14,-25,-23)
 anchor=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
 labels.append(("second_MG57_integer_ray",alternate))
 assert len(labels)==25 and sum(x*x for x in anchor)==82
 successes=0;best=None
 for case,upstream,n in zip(a60["source_cases"],a58["candidates"],(4,8)):
  assert case["new_subdivisions_per_original_cell"]==n
  assert upstream["new_subdivisions_per_original_cell"]==n
  cells,new=reconstructed_cells(a57,n)
  assert case["original_source_cell_count"]==len(cells)
  assert case["all_original_physical_cells_contiguous"]
  assert len(case["candidate_2D_strong_moment_source_bounds"])==25
  for source,arch in zip(new,case["selected_true_physical_original_new_source_cells"]):
   assert [str(z) for z in source[:4]]==[arch[k] for k in (
    "left","right","multiplier_lower","multiplier_upper")]
   assert [str(z) for z in source[4]]==arch["source_midpoint"]
   assert [str(z) for z in source[5]]==arch["source_derivative"]
   assert [str(z) for z in source[6]]==arch["source_error"]
  localpositive=[]
  for (name,v),row in zip(labels,case["candidate_2D_strong_moment_source_bounds"]):
   assert row["second_vector_label"]==name
   assert [str(x) for x in anchor]==row["first_original_source_coefficients"]
   assert [str(x) for x in v]==row["second_original_source_coefficients"]
   lo,hi,sig,pen,counts=replay(cells,anchor,v,b,berr)
   assert [[str(x) for x in z] for z in lo]==row["original_true_projected_2D_action_lower"]
   assert [[str(x) for x in z] for z in hi]==row["original_true_projected_2D_action_upper"]
   assert str(sig)==row["original_2D_signal_trace"]
   assert str(pen)==row["original_2D_Young_error"]
   assert counts==row["original_young_tau_counts"]
   yes=exact_gram(lo,row)
   if yes:
    localpositive.append(row)
    successes+=1
    constant=Q(row["exact_2D_restricted_coefficient_norm_lower"])
    if best is None or constant>best[0]:
     best=(constant,n,name)
   assert row["full24_global_rank_two_Loewner_NOT_proved"]
  assert case["strict_positive_two_planes"]==len(localpositive)
  if localpositive:
   top=max(localpositive,key=lambda x:Q(x["exact_2D_restricted_coefficient_norm_lower"]))
   assert case["best_certified_original_2D_label"]==top["second_vector_label"]
   assert Q(case["best_restricted_source_coercivity"])==Q(
      top["exact_2D_restricted_coefficient_norm_lower"])
  else:
   assert case["best_certified_original_2D_label"] is None
   assert case["best_restricted_source_coercivity"] is None
  assert case["original_full24_conservative_index_still_only_one"]
 assert successes==a60["num_total_2D_planes_certified"]
 assert bool(successes)==a60["at_least_one_original_2D_action_source_coercivity"]
 if best:
  assert a60["best_positive_plane_subdivision_n"]==best[1]
  assert a60["best_positive_plane_label"]==best[2]
  assert Q(a60["best_positive_2D_restricted_constant"])==best[0]
 else:
  assert a60["best_positive_plane_subdivision_n"] is None
  assert a60["best_positive_plane_label"] is None
  assert a60["best_positive_2D_restricted_constant"] is None
 assert not a60["full_original_24D_strong_action_coercivity_CERTIFIED"]
 assert not a60["full_original_24D_residual_source_contraction_CERTIFIED"]
 assert not a60["full_original_470D_inverse_CERTIFIED"]
 assert not a60["signed_odd_51over56_CAP_CERTIFIED"]
 assert a60["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert a60["even_Weil_CC27_RH"]=="OPEN"
 print("MG60 INDEPENDENT 50 original physical Fourier source projected 2D matrices exact PASS",{
  "physical_partitions":[47,55],"tested_planes":50,
  "positive2D_planes":successes,
  "best_exact_constant":str(best[0]) if best else None,
  "original_full24_and_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
