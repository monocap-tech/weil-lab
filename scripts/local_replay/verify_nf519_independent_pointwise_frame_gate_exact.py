#!/usr/bin/env python3
"""NF519 independent exact Fraction original-raw J242 pointwise error audit.

Uses original source raw pointwise generator absolute sum, not primary
Gram-trace Cauchy estimate. No original historical frame or local e_D is
manufactured; all gates remain conditional.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SHA="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
B=Q(549,500)
def read(p):
 z=Path(p).read_bytes();return json.loads(z),hashlib.sha256(z).hexdigest()
def main():
 p=argparse.ArgumentParser()
 for k in ("nf505","nf518","nf519","output"):p.add_argument("--"+k,required=True)
 o=p.parse_args()
 old,sha=read(o.nf505);fit,fs=read(o.nf518);prior,ps=read(o.nf519)
 assert sha==SHA and old["pass"]=="NF504-native"
 assert prior["original_nf505_source_sha256"]==sha
 assert prior["original_nf518_source_sha256"]==fs
 assert prior["pass"]=="NF519-exact-original-selected-frame-perturbation-and-gap-basis-invariance"
 assert old["original_selected_J_dimension"]==242
 assert old["original_original_D_frame_SHA256"]==prior["historical_original_D_frame_sha256"]
 a=list(map(int,fit["original_selected_D_frame_coefficients_exact_rational_candidates_numerators"]))
 den=int(fit["original_selected_D_frame_coefficients_exact_rational_denominator"])
 assert len(a)==242 and den==10**105
 l1=Q(sum(map(abs,a)),den);assert l1<Q(5,10**8)
 # Unlike primary trace+sqrt bound, use physical sup_i |J_i| on O.
 rawsum=sum((B**int(k) for f,k in old["original_source_basis_nodes"] if f!="pole"),Q(0))+Q(3,5)
 assert rawsum<Q(293)
 assert 2*B<Q(3,2)**2
 approxL2=Q(3,2)*Q(293)*Q(5,10**8)*Q(1,10**14)+Q(5,10**83)
 assert approxL2<Q(22,10**20)
 oldres=Q(13,10**12)
 energy=2*oldres*approxL2+approxL2**2
 assert energy<Q(6,10**30)
 betaL2=Q(3,2)*Q(1,10**19)+Q(5,10**83)
 assert betaL2<Q(151,10**21)
 assert 2*oldres*betaL2+betaL2**2<Q(4,10**30)
 r=Q(old["original_original_saturated_exterior_residual_outward"][0])
 gamma=Q(old["original_original_gamma_squared"])
 for name,trial,delta in (
   ("H4094",Q(99,10**29),Q(2,5)),
   ("H4095",Q(99,10**29),Q(1,1000)),
   ("H4094_union_H4095",Q(29,10**28),Q(1,20000))):
  assert r-(trial+energy)/delta>gamma
  assert r-(trial+Q(4,10**30))/delta>gamma
 out={"pass":"NF519-independent-original-raw-pointwise-frame-budget",
   "original_nf505_raw_sha256":sha,"original_nf518_receipt_sha256":fs,
   "primary_NF519_receipt_sha256":ps,
   "original_raw_J242_pointwise_absolute_generator_sum_lt_293":True,
   "independent_original_frame_entrywise_error_CONDITIONAL_le_1e_minus_14_implies_any_cell_e_error_lt_6e_minus_30":True,
   "independent_original_weighted_raw_beta_L1_CONDITIONAL_le_1e_minus_19_implies_any_cell_e_error_lt_4e_minus_30":True,
   "all_three_original_NF517_spectral_gap_plus_trial_energy_NF404_conditional_implications":True,
   "actual_historical_source_D_frame_recovered":False,
   "actual_physical_beta_or_local_eD_certified":False,
   "actual_Fredholm_gap_certified":False,
   "original_NF404_named_patch":"OPEN",
   "Weil_source_image_graph_domain":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
 Path(o.output).write_text(json.dumps(out,indent=2)+"\n")
 print("NF519 independent original raw pointwise exact source gate PASS")
 print("No actual D frame, physical local e_D, kernel gap or RH result")
if __name__=="__main__":main()
