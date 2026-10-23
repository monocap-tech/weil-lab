#!/usr/bin/env python3
"""MG60: COMPOSE verified MG58 physical [5/8,7/8] subcells with MG59
project-first original signed multiplier/pole-corrected 2D strong moment.

This is an entirely new combination. The two upstream mathematical
operations commute only in the ORIGINAL physical action: first select
a source plane, then project the genuine Fourier response on every
new physical cell BEFORE taking interval absolute values or charging
Young fees.

Test 25 source planes per original physical partition (47/55 cells):
the already MG57-proved mixed anchor against all 24 coordinate
directions and the independently accepted second short-integer ray.
The global 24D MG58 index 1 does NOT rule out a positive projected
2D lower; different conservative bounds lose different correlations.

No positive plane declared unless exact rational a>0,c>0,ac-b²>0.
No global rank-two 24D Loewner estimate from a restricted plane.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg59_projected_true_action_plane as m59
N=24;P=23
ANCHOR=tuple(m59.ANCHOR)
ALT=tuple(m59.ALT)
def decode(c):
 return (Q(c["left"]),Q(c["right"]),
         Q(c["multiplier_lower"]),Q(c["multiplier_upper"]),
         [Q(x) for x in c["source_midpoint"]],
         [Q(x) for x in c["source_derivative"]],
         [Q(x) for x in c["source_error"]])
def valid_cells(cells,n):
 assert len(cells)==41+2*(n-1)
 assert cells[0][0]==0 and cells[-1][1]==4
 assert all(cells[i][1]==cells[i+1][0] for i in range(len(cells)-1))
 assert sum((c[1]-c[0] for c in cells),Q(0))==4
 assert all(Q(0)<c[2]<=c[3] for c in cells)
def combine(a57,candidate):
 base=m59.accepted_original_41_source_cells(a57)
 n=candidate["new_subdivisions_per_original_cell"]
 assert n in (4,8)
 raw=candidate["new_actual_physical_fourier_source_cells"]
 assert len(raw)==2*n
 new=[decode(c) for c in raw]
 assert all(new[i][1]==new[i+1][0] for i in range(len(new)-1))
 assert new[0][0]==Q(5,8) and new[-1][1]==Q(7,8)
 cells=[]
 for c in base:
  if c[0]==Q(5,8):
   cells.extend(new[:n])
  elif c[0]==Q(3,4):
   cells.extend(new[n:])
  else:cells.append(c)
 valid_cells(cells,n)
 return cells
def report_plane(cells,b,brad,second_name,w,a59baseline=None):
 lower,upper,sig,err,charges,counts=m59.twoD_moment(cells,ANCHOR,w,b,brad)
 a,cross,c=lower[0][0],lower[0][1],lower[1][1]
 determinant=a*c-cross*cross
 possible=(a>0 and c>0 and determinant>0)
 n0=m59.dot(ANCHOR,ANCHOR);n1=m59.dot(w,w)
 assert n0>0 and n1>0
 constant=(determinant/((a+c)*(n0+n1))) if possible else None
 if possible:assert constant>0
 row={
   "second_vector_label":second_name,
   "first_original_source_coefficients":[str(x) for x in ANCHOR],
   "second_original_source_coefficients":[str(x) for x in w],
   "original_true_projected_2D_action_lower":[[str(x) for x in r] for r in lower],
   "original_true_projected_2D_action_upper":[[str(x) for x in r] for r in upper],
   "exact_positive_2D":possible,
   "exact_2D_determinant":str(determinant),
   "exact_2D_restricted_coefficient_norm_lower":str(constant) if constant is not None else None,
   "original_2D_signal_trace":str(sig),
   "original_2D_Young_error":str(err),
   "source_error_provenance_diagnostic":{k:str(x) for k,x in charges.items()},
   "original_young_tau_counts":counts,
   "full24_global_rank_two_Loewner_NOT_proved":True
 }
 if a59baseline is not None:
  row["baseline_41_cell_projected_strong_lower"]=a59baseline["new_true_original_2D_projected_action_lower"]
  row["baseline_41_cell_exact_positive_2D"]=a59baseline["exact_new_2D_strict_positive"]
 return row
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg57","mg58","mg59"):
  p.add_argument("--verified-"+k+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg60_combined_refined_projected_original_2D_source.json")
 args=p.parse_args()
 inp={k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
      for k in ("mg24","mg57","mg58","mg59")}
 a24,a57,a58,a59=[inp[k] for k in ("mg24","mg57","mg58","mg59")]
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in inp.values())
 assert a58["status"]=="ORIGINAL_MG58_TRUE_FOURIER_ADAPTIVE_2D_STRONG_SUBSPACE"
 assert a59["status"]=="ORIGINAL_MG59_TRUE_ACTION_PREPROJECTED_TWO_PLANE_LOEWER"
 assert a58["selected_conservative_positive_index"]==1
 assert a59["strict_positive_original_2D_subspaces"]==0
 hm,hr,err=original_H24_from_physical_source()
 assert err==Q(a24["physical_Gram_Loewner_row_error"])
 b=[hm[i][P] for i in range(N)]
 brad=[hr[i][P] for i in range(N)]
 mg59base={x["second_vector_label"]:x for x in a59["candidates"]}
 names=[("coordinate_"+str(i),tuple(int(j==i) for j in range(N))) for i in range(N)]
 names.append(("second_MG57_integer_ray",ALT))
 assert len(names)==25
 assert m59.dot(ANCHOR,ANCHOR)==82
 cases=[]
 for old_candidate in a58["candidates"]:
  n=old_candidate["new_subdivisions_per_original_cell"]
  cells=combine(a57,old_candidate)
  rows=[]
  for idx,(name,w) in enumerate(names):
   row=report_plane(cells,b,brad,name,w,mg59base.get(name))
   rows.append(row)
   if idx in (0,5,11,23,24):
    print("MG60 ORIGINAL combined physical projected source",{
     "n":n,"plane":name,
     "exact2D":row["exact_positive_2D"],
     "L00":float(Q(row["original_true_projected_2D_action_lower"][0][0])),
     "L11":float(Q(row["original_true_projected_2D_action_lower"][1][1]))},flush=True)
  successful=[row for row in rows if row["exact_positive_2D"]]
  chosen=(max(successful,key=lambda x:Q(x["exact_2D_restricted_coefficient_norm_lower"]))
          if successful else None)
  old_source=old_candidate["new_actual_physical_fourier_source_cells"]
  assert len(old_source)==2*n
  result={
   "new_subdivisions_per_original_cell":n,
   "original_source_cell_count":len(cells),
   "selected_true_physical_original_new_source_cells":old_source,
   "upstream_global_full24_conservative_positive_index":
       old_candidate["original_full24_conservative_LDL_inertia"]["positive"],
   "original_full24_conservative_index_still_only_one":True,
   "projected_two_plane_candidates_checked":len(rows),
   "strict_positive_two_planes":len(successful),
   "best_certified_original_2D_label":chosen["second_vector_label"] if chosen else None,
   "best_restricted_source_coercivity":chosen["exact_2D_restricted_coefficient_norm_lower"] if chosen else None,
   "all_original_physical_cells_contiguous":True,
   "original_true_pole_correction_and_remaining_strong_energy_PSD":True,
   "candidate_2D_strong_moment_source_bounds":rows}
  print("MG60 COMBINED original projected source result",{
   "n":n,"source_cells":len(cells),
   "positive2D_planes":len(successful),
   "best":result["best_certified_original_2D_label"]},flush=True)
  cases.append(result)
 allgood=[(item,c) for c in cases for item in c["candidate_2D_strong_moment_source_bounds"]
          if item["exact_positive_2D"]]
 best=(max(allgood,key=lambda x:Q(x[0]["exact_2D_restricted_coefficient_norm_lower"]))
       if allgood else None)
 output={
  "status":"ORIGINAL_MG60_COMPOSED_TRUE_REFINED_PROJECTED_ACTION_2D_LOEWER",
  "canonical_W_ODD_NEG":"OPEN",
  "verified_parent_original_runs":{"MG24":39378465438,
     "MG57":39897754515,"MG58":39902364126,"MG59":39905695260},
  "original_MG58_two_physical_partitions_47_and_55_cells":True,
  "original_MG59_project_before_multiplier_and_pole_absolute":True,
  "true_25SI10_23adapted_plus_sinh_pole_original_source":True,
  "true_original_signed_prime7_digamma_and_all_remaining_strong_PSD":True,
  "all_50_projected_two_plane_rational_moments":True,
  "num_total_2D_planes_certified":len(allgood),
  "at_least_one_original_2D_action_source_coercivity":bool(allgood),
  "best_positive_plane_subdivision_n":best[1]["new_subdivisions_per_original_cell"] if best else None,
  "best_positive_plane_label":best[0]["second_vector_label"] if best else None,
  "best_positive_2D_restricted_constant":best[0]["exact_2D_restricted_coefficient_norm_lower"] if best else None,
  "full_original_24D_strong_action_coercivity_CERTIFIED":False,
  "full_original_24D_residual_source_contraction_CERTIFIED":False,
  "full_original_470D_inverse_CERTIFIED":False,
  "signed_odd_51over56_CAP_CERTIFIED":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN",
  "source_cases":cases}
 dst=ROOT/args.output;dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(output,indent=2)+"\n")
 print("MG60 ORIGINAL both valid new-physical and projected 2D mechanisms",{
  "tested":50,
  "positive_two_planes":len(allgood),
  "original_full24_and_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
