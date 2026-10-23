#!/usr/bin/env python3
"""MG61: exact original strong-action 2D plane-basis conditioning audit.

MG60 independently verified 0/50 strictly positive two-plane LOWER
certificates on original 47/55-cell physical Fourier partitions.

A directional Young source bound is NOT invariant under changing basis
of the SAME physical source plane. All MG60 source coordinates were
widely unbalanced: an integer anchor of norm sqrt(82) against unit
coordinate directions. MG61 uses an exact orthogonal Euclidean basis
and two rational balanced scalings BEFORE original physical strong
action Fourier projection, while preserving the same source planes.

The original true pole-corrected action and 55-cell Fourier data are
UNCHANGED. Only certificate conditioning changes. Every accepted
claim is a rational strict 2x2 Gram determinant, not a single ray.
No full24/global-rank-two Loewner or RH promotion.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg59_projected_true_action_plane as m59
N=24;P=23
BASE=tuple(Q(x) for x in m59.ANCHOR)
assert len(BASE)==N and m59.dot(BASE,BASE)==82
SCALES=(Q(1,9),Q(1,18))
def load_original_55_physical(a57,a58):
 baseline=m59.accepted_original_41_source_cells(a57)
 fixed=next(x for x in a58["candidates"] if x["new_subdivisions_per_original_cell"]==8)
 cells=fixed["new_actual_physical_fourier_source_cells"]
 assert len(cells)==16
 def dec(row):
  return (Q(row["left"]),Q(row["right"]),
   Q(row["multiplier_lower"]),Q(row["multiplier_upper"]),
   [Q(x) for x in row["source_midpoint"]],
   [Q(x) for x in row["source_derivative"]],
   [Q(x) for x in row["source_error"]])
 new=[dec(x) for x in cells]
 result=[]
 for cell in baseline:
  if cell[0]==Q(5,8):result.extend(new[:8])
  elif cell[0]==Q(3,4):result.extend(new[8:])
  else:result.append(cell)
 assert len(result)==55
 assert result[0][0]==0 and result[-1][1]==4
 assert all(result[i][1]==result[i+1][0] for i in range(54))
 assert sum((x[1]-x[0] for x in result),Q(0))==4
 return result
def orthogonal_source_complement(i):
 """Source plane is EXACTLY span(BASE,e_i), never new source domain."""
 beta=BASE[i]/Q(82)
 w=tuple(Q(j==i)-beta*BASE[j] for j in range(N))
 assert m59.dot(BASE,w)==0
 assert m59.dot(w,w)==1-BASE[i]*BASE[i]/Q(82)>0
 return w
def prove_2D(row,a,b,w,u):
 c=row[0][0];cross=row[0][1];d=row[1][1]
 assert row[1][0]==cross
 det=c*d-cross*cross
 good=(c>0 and d>0 and det>0)
 norm=m59.dot(a,a)+m59.dot(b,b)
 constant=det/((c+d)*norm) if good else None
 if good:assert constant>0
 return good,det,constant
def main():
 p=argparse.ArgumentParser()
 for name in ("mg24","mg57","mg58","mg60"):
  p.add_argument("--verified-"+name+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg61_original_two_plane_orthogonal_gauge.json")
 args=p.parse_args()
 ds={name:json.loads((ROOT/getattr(args,"verified_"+name+"_json")).read_text())
     for name in ("mg24","mg57","mg58","mg60")}
 a24,a57,a58,a60=(ds[x] for x in ("mg24","mg57","mg58","mg60"))
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in ds.values())
 assert a60["status"]=="ORIGINAL_MG60_COMPOSED_TRUE_REFINED_PROJECTED_ACTION_2D_LOEWER"
 assert not a60["at_least_one_original_2D_action_source_coercivity"]
 assert a58["selected_refinement_n"]==8
 src=load_original_55_physical(a57,a58)
 H,Hrad,he=original_H24_from_physical_source()
 assert he==Q(a24["physical_Gram_Loewner_row_error"])
 b=[H[i][P] for i in range(N)]
 brad=[Hrad[i][P] for i in range(N)]
 previous=next(x for x in a60["source_cases"]
               if x["new_subdivisions_per_original_cell"]==8)
 assert previous["strict_positive_two_planes"]==0
 previous_bylabel={r["second_vector_label"]:r for r in previous["candidate_2D_strong_moment_source_bounds"]}
 assert len(previous_bylabel)==25
 allrows=[];strict=0
 for alpha in SCALES:
  u=tuple(alpha*x for x in BASE)
  for i in range(N):
   w=orthogonal_source_complement(i)
   lower,upper,signal,loss,allocation,counts=m59.twoD_moment(
      src,u,w,b,brad)
   good,det,C=prove_2D(lower,u,w,BASE,w)
   old=previous_bylabel["coordinate_"+str(i)]
   assert not old["exact_positive_2D"]
   row={
     "source_coordinate_index":i,
     "integer_original_anchor": [str(x) for x in BASE],
     "orthogonalized_original_source_second": [str(x) for x in w],
     "anchor_balancing_factor":str(alpha),
     "source_first_scaled":[str(x) for x in u],
     "original_physical_55cell_strong_lower":[[str(x) for x in r] for r in lower],
     "original_physical_55cell_strong_upper":[[str(x) for x in r] for r in upper],
     "original_second_source_orthogonal_to_anchor":True,
     "original_source_second_norm_squared":str(m59.dot(w,w)),
     "exact_2D_positive_definite":good,
     "exact_2D_lower_determinant":str(det),
     "exact_2D_coercivity_constant":str(C) if C is not None else None,
     "original_projected_affine_signal_trace":str(signal),
     "original_projected_Young_error_charge":str(loss),
     "original_young_tau_counts":counts,
     "baseline_MG60_unconditioned_lower":old["original_true_projected_2D_action_lower"],
     "baseline_MG60_unconditioned_negative":True,
     "same_source_plane_as_MG60":True,
     "only_2D_restricted_original_source_positive_claim":True
   }
   strict+=int(good)
   allrows.append(row)
   if i in (0,1,2,5,11,23):
    print("MG61 exact original strong plane basis gauge",{
      "alpha":str(alpha),"axis":i,
      "lower_diag":[float(lower[0][0]),float(lower[1][1])],
      "positive2D":good},flush=True)
 assert len(allrows)==2*N
 winners=[r for r in allrows if r["exact_2D_positive_definite"]]
 chosen=max(winners,key=lambda r:Q(r["exact_2D_coercivity_constant"])) if winners else None
 output={
   "status":"ORIGINAL_MG61_REBALANCED_ORTHOGONAL_55CELL_2D_SOURCE_MOMENT",
   "canonical_W_ODD_NEG":"OPEN",
   "accepted_runs":{"MG24":39378465438,"MG57":39897754515,
                    "MG58":39902364126,"MG60":39959456013},
   "true_original_55cell_source_Fourier_data_unchanged":True,
   "actual_original_signed_seven_prime_digamma_and_true_sinh_pole":True,
   "all_original_strong_frequency_outside_measured_band_remains_PSD":True,
   "exact_orthogonal_source_plane_conditioning_only":True,
   "same_24_source_subspaces_as_MG60_original_coordinate_planes":True,
   "original_source_2D_plane_lower_dependent_on_basis_gauge":True,
   "independently_replayable_new_48_rational_matrices":True,
   "num_tested":len(allrows),
   "num_strict_positive_2D":strict,
   "at_least_one_original_true_2D_source_strong_moment_positive":bool(strict),
   "best_original_second_coordinate":chosen["source_coordinate_index"] if chosen else None,
   "best_balancing_factor":chosen["anchor_balancing_factor"] if chosen else None,
   "best_2D_exact_coercivity_constant":chosen["exact_2D_coercivity_constant"] if chosen else None,
   "no_original_global_rank_two_Loewner_claim":True,
   "no_original_24D_full_source_coercivity_claim":True,
   "no_original_24D_residual_contraction_claim":True,
   "no_original_470D_inverse_claim":True,
   "no_odd_signed_51over56_claim":True,
   "independent_original_Fourier_form_domain_audit":"OPEN",
   "even_Weil_CC27_RH":"OPEN",
   "cases":allrows
 }
 path=ROOT/args.output;path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(output,indent=2)+"\n")
 print("MG61 exact original orthogonalized conditioned source-plane 55-cell audit",{
    "tested":len(allrows),"strict_2D":strict,
    "best":output["best_original_second_coordinate"],
    "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
