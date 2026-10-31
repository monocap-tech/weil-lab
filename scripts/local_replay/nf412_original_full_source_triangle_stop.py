#!/usr/bin/env python3
"""NF412 correction: valid but very loose TRUE full u4'' source-triangle bound.
All original 242 selected plus 4 critical used; nothing is inferred from
NF374 exterior curvature as if it were the missing selected cancellation.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);H=F(1,10**10);EPS=F(9,10**17)
def read(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(v):
 n,e=int(v[0]),int(v[1])
 return F(n*(2**e)) if e>=0 else F(n,2**(-e))
def second_bound(k,f):
 a=7*abs(f)
 return (k*(k-1)*B**(k-2) if k>=2 else 0)+(2*k*a*B**(k-1) if k else 0)+a*a*B**k
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 a.add_argument("--radius",default="notes/data/provisional/NF408_original_source_midpoint_action_error_exact.json")
 a.add_argument("--output",required=True)
 args=a.parse_args()
 s,ssha=read(args.source);r,rsha=read(args.radius)
 assert r["original_nf407_coefficient_native_sha256"]==ssha
 assert len(s["original_selected_generator_node_orders"])==242
 assert len(s["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert s["original_odd_physical_parity_native_reproduced"]
 total=F(0);selected=F(0);critical=F(0)
 for (freq,k),(mid,rad) in zip(s["original_selected_generator_node_orders"],s["original_exact_native_raw_selected_coefficients_mid_radius"]):
  coeff=abs(dyad(mid))+abs(dyad(rad))
  inc=coeff*(F(1,4) if freq=="pole" else second_bound(k,F(freq)))
  selected+=inc
 for (mid,rad),shape in zip(s["original_exact_native_original_four_critical_coefficients_mid_radius"],s["original_source_critical_sines_and_pole_coefficients"]):
  coeff=abs(dyad(mid))+abs(dyad(rad))
  amp=sum((abs(F(v))*second_bound(0,F(f)) for v,f in
           zip(shape["sine_coefficients"],s["original_source_critical_sine_frequencies"])),F(0))
  amp+=abs(F(shape["sinh_coefficient"]))/4
  critical+=coeff*amp
 total=selected+critical
 assert total>0
 # L2(-B,B) <sqrt(2B) sup <=3/2 sup; legitimate after all 246 exact sources.
 full_curv_upper=F(3,2)*total
 # L2 positive half symmetric small-t operator error h²/8*||u''||.
 pos_fee=H*H*full_curv_upper/8
 # Odd extension sqrt 2<3/2, so loose rational full-support fee.
 whole_fee=F(3,2)*pos_fee
 assert whole_fee>EPS
 out={
 "pass":"NF412","standing":"TRUE ORIGINAL FULL 242+4 SOURCE TRIANGLE CURVATURE UPPER (RIGOROUS BUT USELESS); INVALID EARLIER FOUR-CRITICAL MINUS NF374 CURVATURE CERTIFICATE SUPERSEDED",
 "original_nf407_original_full_source_sha256":ssha,
 "original_nf408_source_radius_sha256":rsha,
 "selected_source_generators_included":242,"critical_source_generators_included":4,
 "original_full_source_second_derivative_uniform_triangle_selected_exact":str(selected),
 "original_full_source_second_derivative_uniform_triangle_critical_exact":str(critical),
 "original_full_source_second_derivative_uniform_triangle_exact":str(total),
 "true_original_full_source_second_derivative_L2_triangle_upper_exact":str(full_curv_upper),
 "original_t_cutoff_h_exact":str(H),
 "true_original_small_t_I0_positive_half_L2_triangle_upper_exact":str(pos_fee),
 "true_original_small_t_I0_whole_odd_support_L2_triangle_upper_exact":str(whole_fee),
 "triangle_bound_exceeds_desired_error_tolerance":True,
 "original_source_correlated_246D_curvature_gram_computed":False,
 "nf374_exterior_w4_curvature_substituted_for_missing_242_selected_terms":False,
 "former_NF412_original_correlated_small_t_gram_receipt_acceptance":"INVALIDATED: mixed four-critical Gram with unmatched exterior w4; despite numerical CI PASS it is not a bound on the true full u4",
 "true_small_t_physical_usable_budget_certified":False,
 "original_z_cells_6_3_7_certified":False,"complete_centered_scalar_certified":False,
 "NF404_gate_decided":False,"W_ODD_NEG":"OPEN","RH":"OPEN"}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+"\n")
 print("NF412 legitimate complete original source triangle curvature upper, enormously loose")
 print("NF412 previous critical-only attempt NOT the true source; scalar open")
if __name__=="__main__":main()
