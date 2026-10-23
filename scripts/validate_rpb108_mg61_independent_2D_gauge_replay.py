#!/usr/bin/env python3
"""MG61 INDEPENDENT source basis-gauge audit, original true physical 55-cell action.

Does NOT import MG61 producer. Reconstruct 55 genuine original
physical Fourier source cells from MG57 41-cell baseline and MG58
independent physical source generator, and independently reimplement
the original action 2D projected cell moment through accepted MG59
independent script. Check all 48 exact rational 2x2 Grams, orthogonality,
coercivity, positive/negative classifications and nonpromotion scope.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg58_independent_adaptive_2D_replay import generator_cells
from validate_rpb108_mg59_independent_projected_plane import build_cells,replay,dot
N=24;P=23
ANCHOR=tuple(Q(z) for z in (-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2))
def reconstruct(a57,a58):
 base=build_cells(a57)
 new=generator_cells(8)
 assert len(new)==16
 physical=next(x for x in a58["candidates"] if x["new_subdivisions_per_original_cell"]==8)
 for source,arch in zip(new,physical["new_actual_physical_fourier_source_cells"]):
  assert [str(z) for z in source[:4]]==[
   arch["left"],arch["right"],arch["multiplier_lower"],arch["multiplier_upper"]]
  assert [str(z) for z in source[4]]==arch["source_midpoint"]
  assert [str(z) for z in source[5]]==arch["source_derivative"]
  assert [str(z) for z in source[6]]==arch["source_error"]
 source=[]
 for cell in base:
  if cell[0]==Q(5,8):source.extend(new[:8])
  elif cell[0]==Q(3,4):source.extend(new[8:])
  else:source.append(cell)
 assert len(source)==55 and source[0][0]==0 and source[-1][1]==4
 assert all(source[i][1]==source[i+1][0] for i in range(54))
 return source
def strict2D(L,u,v):
 a=L[0][0];b=L[0][1];c=L[1][1]
 assert L[1][0]==b
 det=a*c-b*b
 good=a>0 and c>0 and det>0
 const=det/((a+c)*(dot(u,u)+dot(v,v))) if good else None
 if good:assert const>0
 return det,good,const
def main():
 p=argparse.ArgumentParser()
 for s in ("mg24","mg57","mg58","mg60","mg61"):
  p.add_argument("--verified-"+s+"-json",required=True)
 args=p.parse_args()
 d={s:json.loads((ROOT/getattr(args,"verified_"+s+"_json")).read_text())
    for s in ("mg24","mg57","mg58","mg60","mg61")}
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in d.values())
 a57,a58,a60,out=d["mg57"],d["mg58"],d["mg60"],d["mg61"]
 assert out["status"]=="ORIGINAL_MG61_REBALANCED_ORTHOGONAL_55CELL_2D_SOURCE_MOMENT"
 assert a60["status"]=="ORIGINAL_MG60_COMPOSED_TRUE_REFINED_PROJECTED_ACTION_2D_LOEWER"
 assert a60["num_total_2D_planes_certified"]==0
 assert a58["selected_refinement_n"]==8
 assert out["num_tested"]==48 and len(out["cases"])==48
 assert dot(ANCHOR,ANCHOR)==82
 h,hrad,herr=original_H24_from_physical_source()
 assert herr==Q(d["mg24"]["physical_Gram_Loewner_row_error"])
 b=[h[i][P] for i in range(N)]
 berr=[hrad[i][P] for i in range(N)]
 source=reconstruct(a57,a58)
 accepted=next(x for x in a60["source_cases"] if x["new_subdivisions_per_original_cell"]==8)
 baseline={x["second_vector_label"]:x for x in accepted["candidate_2D_strong_moment_source_bounds"]}
 assert len(baseline)==25
 count=0;wins=[]
 for alpha in (Q(1,9),Q(1,18)):
  u=[alpha*x for x in ANCHOR]
  for k in range(N):
   row=out["cases"][count]
   assert Q(row["anchor_balancing_factor"])==alpha
   assert row["source_coordinate_index"]==k
   assert [str(x) for x in u]==row["source_first_scaled"]
   beta=ANCHOR[k]/82
   v=[Q(int(i==k))-beta*ANCHOR[i] for i in range(N)]
   assert dot(ANCHOR,v)==0
   assert [str(x) for x in v]==row["orthogonalized_original_source_second"]
   assert dot(v,v)==Q(row["original_source_second_norm_squared"])>0
   assert row["same_source_plane_as_MG60"]
   L,U,sig,fee,counts=replay(source,u,v,b,berr)
   assert [[str(x) for x in a] for a in L]==row["original_physical_55cell_strong_lower"]
   assert [[str(x) for x in a] for a in U]==row["original_physical_55cell_strong_upper"]
   assert str(sig)==row["original_projected_affine_signal_trace"]
   assert str(fee)==row["original_projected_Young_error_charge"]
   assert counts==row["original_young_tau_counts"]
   old=baseline["coordinate_"+str(k)]
   assert not old["exact_positive_2D"]
   assert old["original_true_projected_2D_action_lower"]==row["baseline_MG60_unconditioned_lower"]
   assert row["baseline_MG60_unconditioned_negative"]
   det,good,const=strict2D(L,u,v)
   assert det==Q(row["exact_2D_lower_determinant"])
   assert good==row["exact_2D_positive_definite"]
   if good:
    assert const==Q(row["exact_2D_coercivity_constant"])
    wins.append((const,alpha,k))
   else:assert row["exact_2D_coercivity_constant"] is None
   assert row["only_2D_restricted_original_source_positive_claim"]
   count+=1
 assert count==48==out["num_tested"]
 assert len(wins)==out["num_strict_positive_2D"]
 assert bool(wins)==out["at_least_one_original_true_2D_source_strong_moment_positive"]
 if wins:
  best=max(wins,key=lambda x:x[0])
  assert best[2]==out["best_original_second_coordinate"]
  assert str(best[1])==out["best_balancing_factor"]
  assert best[0]==Q(out["best_2D_exact_coercivity_constant"])
 else:
  assert out["best_original_second_coordinate"] is None
  assert out["best_balancing_factor"] is None
  assert out["best_2D_exact_coercivity_constant"] is None
 assert out["no_original_global_rank_two_Loewner_claim"]
 assert out["no_original_24D_full_source_coercivity_claim"]
 assert out["no_original_24D_residual_contraction_claim"]
 assert out["no_original_470D_inverse_claim"]
 assert out["no_odd_signed_51over56_claim"]
 assert out["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert out["even_Weil_CC27_RH"]=="OPEN"
 print("MG61 INDEPENDENT 55-cell 48 original source gauges exact rational reconstructed PASS",{
  "tested":count,"2D_positive":len(wins),
  "best":(str(best[0]),str(best[1]),best[2]) if wins else None,
  "original_full24_Weil_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
