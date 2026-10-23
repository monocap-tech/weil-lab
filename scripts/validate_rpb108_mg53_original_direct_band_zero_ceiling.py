#!/usr/bin/env python3
"""MG53 — exact restricted-method direct-band zero-ceiling diagnostic.

MG52's full original complete-frequency valid residual upper is
 U52 = U_[0,4] + U_[4,8] + U_rem(|xi|>8).
Both direct-source covariance UPPERS must be PSD, since they dominate
an integral of original physical R*R >= 0. Consider the deliberately
NONVALID hypothetical U_[4,8]=0, or both measured bands =0.

If the source lower Hlo-U_rem is negative on a fixed exact rational
witness, NO further sharpening of ONLY U_[4,8] can close the 24D
source gate for that fixed B and U_rem: any genuine direct original
source residual Uvalid >= 0, so Hlo-(U_rem+Uvalid) <= Hlo-U_rem.

This does not rule out a different B, changes in remaining frequencies
or a new joint architecture. Zeroed sources are NOT valid upper bounds.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import deserialize,original_H24_from_physical_source
from validate_rpb108_mg25_robust_source_aware_residual import Id,T,sub,plus,mul,psd,gersh_lower
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
N=24
def m(x):
 a=deserialize(x)
 assert len(a)==N and all(len(z)==N for z in a)
 return a
def enc(a):return [[str(x) for x in r] for r in a]
def qf(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def tr(a):return sum((a[i][i] for i in range(N)),Q(0))
def sign(a):
 kind,witness=classify_ideal(a)
 assert kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH","POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
 if kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  v=[Q(x) for x in witness["rational_vector"]]
  assert qf(v,a)==Q(witness["exact_negative_quadratic"])<0
 return kind,witness

def audit(m24,m46,m47,m50,m52):
 Hmid,Hrad,Herr=original_H24_from_physical_source()
 assert Herr==Q(m24["physical_Gram_Loewner_row_error"])
 Hlo=sub(Hmid,mul(Herr,Id(N)))
 results=[]
 for s46,s47,s50,s52 in zip(m46["scenarios"],m47["scenarios"],
                            m50["cases"],m52["cases"]):
  mesh,k=s52["mesh_cells"],s52["cutoff_k"]
  assert (mesh,k)==(s46["mesh_cells"],s46["cutoff_k"])==(s47["mesh_cells"],s47["cutoff_k"])==(s50["mesh_cells"],s50["cutoff_k"])
  U52=m(s52["MG52_best_original_whole_24D_upper"])
  band4to8=m(s52["MG52_samecell_new_4to8_upper"])
  direct0to4=m(s46["original_MG32_direct_band_24D_upper"])
  oldnewband=m(s50["actual_4to8_original_direct_24D_upper"])
  assert direct0to4==sub(m(s50["actual_0to8_original_direct_24D_upper"]),oldnewband)
  assert sub(oldnewband,band4to8)==m(s52["PSD_direct_upper_reduction"])
  assert U52==sub(m(s50["best_new_whole_24D_upper"]),
                 m(s52["PSD_direct_upper_reduction"]))
  # Every TRUE source covariance itself is PSD. The accepted cell-wise
  # Young uppers are individually positive and independently generated.
  assert psd(direct0to4) and psd(band4to8)
  # EXACT additive algebra; remaining original frequencies and pole
  # charge unchanged and still paid by the FIXED accepted architecture.
  rest=sub(U52,plus(direct0to4,band4to8))
  no_new_band=plus(rest,direct0to4)
  no_direct=rest
  assert plus(no_new_band,band4to8)==U52
  assert plus(no_direct,plus(direct0to4,band4to8))==U52
  certified= sub(Hlo,U52)
  optimistic_new= sub(Hlo,no_new_band)
  optimistic_both=sub(Hlo,no_direct)
  ray=[Q(x) for x in s47["selected_exact_inertia_witness"]["rational_vector"]]
  assert len(ray)==N and any(ray)
  oldMG43=sub(Hlo,m(s47["selected_complete_24D_source_upper"]))
  oldray=qf(ray,oldMG43)
  assert oldray==Q(s47["selected_exact_inertia_witness"]["exact_negative_quadratic"])<0
  actual=qf(ray,certified)
  newgain=qf(ray,band4to8)
  oldgain=qf(ray,direct0to4)
  assert newgain>=0 and oldgain>=0
  ceiling_new=qf(ray,optimistic_new)
  ceiling_both=qf(ray,optimistic_both)
  assert actual+newgain==ceiling_new
  assert ceiling_new+oldgain==ceiling_both
  kind_new,wit_new=sign(optimistic_new)
  kind_both,wit_both=sign(optimistic_both)
  restricted_no_go_new=(ceiling_new<0)
  restricted_no_go_both=(ceiling_both<0)
  # If known genuine MG43 rational witness is negative for the
  # zero-direct upper ceiling, fixed remainder cannot be repaired
  # by any PSD direct covariance upper, no matter how clever.
  if restricted_no_go_new:
    assert kind_new=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
  if restricted_no_go_both:
    assert kind_both=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
  casestr=(str(mesh)+"/k"+str(k))
  output={
   "mesh_cells":mesh,"cutoff_k":k,
   "original_24D_genuine_source_response_B":s52["original_response_B"],
   "full_original_H_lower":enc(Hlo),
   "accepted_MG52_complete_upper":enc(U52),
   "MG52_true_direct_4to8_upper":enc(band4to8),
   "accepted_MG32_true_direct_0to4_upper":enc(direct0to4),
   "fixed_8to_infinity_remaining_upper":enc(rest),
   "zero_only_4to8_counterfactual_24D_source_lower_NOT_CERTIFICATE":enc(optimistic_new),
   "zero_both_measured_counterfactual_24D_source_lower_NOT_CERTIFICATE":enc(optimistic_both),
   "actual_valid_MG52_lower_Gersh":str(gersh_lower(certified)),
   "actual_valid_MG52_negative_MG43_source_ray":str(actual),
   "MG43_accepted_negative_ray":str(oldray),
   "exact_rational_MG43_witness":[str(x) for x in ray],
   "direct_4to8_ray_upper_charge":str(newgain),
   "direct_0to4_ray_upper_charge":str(oldgain),
   "same_ray_counterfactual_new_band_ZERO_ceiling":str(ceiling_new),
   "same_ray_counterfactual_both_bands_ZERO_ceiling":str(ceiling_both),
   "zero_4to8_counterfactual_full24_inertia":kind_new,
   "zero_4to8_counterfactual_full24_inertia_witness":wit_new,
   "zero_both_counterfactual_full24_inertia":kind_both,
   "zero_both_counterfactual_full24_inertia_witness":wit_both,
   "direct_new_band_repair_max_fraction_of_ray_deficit":str(
      newgain/(-actual)) if actual<0 else None,
   "both_direct_bands_repair_max_fraction_of_ray_deficit":str(
      (newgain+oldgain)/(-actual)) if actual<0 else None,
   "restricted_fixed_MG52_remainder_direct_4to8_ONLY_cannot_certify_24D":
      restricted_no_go_new,
   "restricted_fixed_MG52_remainder_either_direct_band_ONLY_cannot_certify_24D":
      restricted_no_go_both,
   "genuine_direct_residual_is_PSD":True,
   "counterfactual_zeroed_band_is_NOT_a_valid_source_upper":True,
   "no_original_operator_negative_eigenmode_claim":True,
   "no_new_full_source_24D_contraction":True
  }
  print("MG53 original strict fixed-remainder bound",casestr,{
     "MG52_ray":float(actual),
     "band4to8_upper_ray":float(newgain),
     "zero4to8_ray":float(ceiling_new),
     "zero0to8_ray":float(ceiling_both),
     "cannot_close_4to8_only":restricted_no_go_new,
     "cannot_close_direct0to8_only":restricted_no_go_both},
     flush=True)
  results.append(output)
 return results
def main():
 p=argparse.ArgumentParser()
 for key in ("mg24","mg46","mg47","mg50","mg52"):
  p.add_argument("--verified-"+key+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg53_original_direct_band_zero_ceiling.json")
 args=p.parse_args()
 read=lambda key:json.loads((ROOT/getattr(args,"verified_"+key+"_json")).read_text())
 z24,z46,z47,z50,z52=(read(x) for x in ("mg24","mg46","mg47","mg50","mg52"))
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in (z24,z46,z47,z50,z52))
 assert z52["status"]=="ORIGINAL_MG52_COUPLED_4TO8_MULTIPLIER_VECTOR_CANCELLATION_24D"
 cases=audit(z24,z46,z47,z50,z52)
 report={
   "status":"ORIGINAL_MG53_FIXED_SOURCE_DIRECT_BAND_ZERO_CEILING",
   "canonical_W_ODD_NEG":"OPEN",
   "accepted_input_runs":{"MG24":39378465438,"MG46":39638393721,
      "MG47":39663431182,"MG50":39727680095,"MG52":39813976498},
   "all_original_four_scenarios_replayed_exact":True,
   "all_direct_original_covariances_PSD":True,
   "hypothetical_zero_upper_is_NOT_a_valid_operator_certificate":True,
   "new_mathematical_obstruction_only_fixed_MG52_remnant_and_B":True,
   "new_original_Fourier_measurements":False,
   "new_actual_original_24D_source_contraction":False,
   "full_original_470D_inverse":False,
   "original_odd_signed_51over56":False,
   "independent_original_Fourier_form_domain_audit":"OPEN",
   "even_Weil_CC27_RH":"OPEN",
   "cases":cases}
 dst=ROOT/args.output;dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(report,indent=2)+"\n")
 print("MG53 four-case exact fixed-original direct-band ceiling diagnostic",{
   "all4_4to8_only_restricted_no_go":all(x["restricted_fixed_MG52_remainder_direct_4to8_ONLY_cannot_certify_24D"] for x in cases),
   "all4_0to8_only_restricted_no_go":all(x["restricted_fixed_MG52_remainder_either_direct_band_ONLY_cannot_certify_24D"] for x in cases),
   "470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
