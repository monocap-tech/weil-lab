#!/usr/bin/env python3
"""NF411: native original u4 boundary jet. DOES NOT enclose continuous z."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,sys
from flint import arb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
N7=(2,3,4,5,7,8,9)
def load(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(pair):
 n,e=int(pair[0]),int(pair[1])
 return F(n*2**e) if e>=0 else F(n,2**(-e))
def ab(v):return arb(str(v))
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--native",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 a.add_argument("--principal",default="notes/data/provisional/NF407_original_prime_jump_log_power_exact.json")
 a.add_argument("--radius",default="notes/data/provisional/NF408_original_source_midpoint_action_error_exact.json")
 a.add_argument("--output",required=True)
 a=a.parse_args()
 src,sh=load(a.native);p,ph=load(a.principal);rad,rh=load(a.radius)
 assert len(src["original_selected_generator_node_orders"])==242
 assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert src["original_exported_coefficients_are_4096bit_arb_not_float"]
 assert p["source_all_original_prime_jumps_cancelled_from_z"]
 assert rad["original_nf407_coefficient_native_sha256"]==sh
 D=F(rad["original_native_coefficient_derivative_error_uniform_D"])
 assert 0<D<F(1,10**750)
 assert all(t["W_ODD_NEG"]==t["RH"]=="OPEN" for t in (src,p,rad))
 # Group dyadic 242+4 physical generator coefficients as EXACT rationals,
 # before each sin/cos/exp is enclosed; no independent-source interval blowup.
 groups={};pole=F(0)
 def add(freq,k,value):
  key=(freq,k);groups[key]=groups.get(key,F(0))+value
 for (freq,k),(mid,radius) in zip(src["original_selected_generator_node_orders"],src["original_exact_native_raw_selected_coefficients_mid_radius"]):
  value=dyad(mid)
  if freq=="pole": pole+=value
  else: add(F(freq),k,value)
 for (mid,radius),shape in zip(src["original_exact_native_original_four_critical_coefficients_mid_radius"],src["original_source_critical_sines_and_pole_coefficients"]):
  alpha=dyad(mid)
  for freq,coeff in zip(src["original_source_critical_sine_frequencies"],shape["sine_coefficients"]):
   add(F(freq),0,alpha*F(coeff))
  pole+=alpha*F(shape["sinh_coefficient"])
 ctx.prec=4096
 x=ab(B); pi=arb.pi()
 value=ab(pole)*(x/2).sinh()
 deriv=ab(pole)*(x/2).cosh()/2
 for freq in sorted({f for f,k in groups}):
  sinv,cosv=ab(2*freq*B).sin_cos_pi()
  omega=2*pi*ab(freq)
  for (f,k),coef in groups.items():
   if f!=freq or not coef:continue
   C=ab(coef); power=ab(B**k)
   if k%2==0:
    value+=C*power*sinv
    deriv+=C*ab(k*B**(k-1))*sinv if k else ab(0)
    deriv+=C*power*omega*cosv
   else:
    value+=C*power*cosv
    deriv+=C*ab(k*B**(k-1))*cosv-C*power*omega*sinv
 v_lo,v_hi=map(ab,p["original_source_u4_endpoint_interval"])
 assert not (value<v_lo or value>v_hi),"source-correlation/original endpoint mismatch"
 # Certified rational bracket for the TRUE original derivative, paying NF408 D.
 assert deriv > ab(-F(131,10**9))+ab(D)
 assert deriv < ab(-F(129,10**9))-ab(D)
 pos=bool(deriv>ab(D));neg=bool(deriv<-ab(D))
 assert not(pos and neg)
 rows=[]
 for n,term in zip(N7,p["source_true_original_prime_jump_terms"]):
  assert term["n"]==n
  clo,chi=map(F,term["signed_mangoldt_weight_positive_interval"])
  assert 0<clo<=chi
  rows.append({"prime_power":n,"seam":"abs(B-log(n))",
               "derivative_jump_identity":("+c_n*u4_prime(B)" if n in (2,3) else "-c_n*u4_prime(B)"),
               "c_n_positive_outward":[str(clo),str(chi)]})
 result={"pass":"NF411","standing":"4096-bit original source-correlated boundary jet (conditional on native CI verification); no continuous z interval",
         "nf407_source_sha256":sh,"nf407_principal_sha256":ph,"nf408_source_radius_sha256":rh,
         "original_source_selected_count":242,"original_source_critical_count":4,
         "original_original_source_value_at_B_arb":str(value),"original_original_source_derivative_at_B_arb":str(deriv),
         "native_source_derivative_uncertainty_exact_upper":str(D),
         "source_derivative_strict_positive":pos,"source_derivative_strict_negative":neg,
         "source_derivative_nonzero_certified":pos or neg,
         "all_seven_original_prime_seam_derivative_identities":rows,
         "original_source_native_radii_paid_for_endpoint_derivative":True,
         "original_full_arch_x_t_quadrature_certified":False,
         "original_z_interval_certified":False,"original_full_centered_scalar_certified":False,
         "nf404_cap_decided":False,"W_ODD_NEG":"OPEN","RH":"OPEN"}
 target=Path(a.output);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(result,indent=2)+"\n")
 print("NF411 native u4(B):",value)
 print("NF411 native u4_prime(B):",deriv)
 print("NF411 source true u4_prime(B) sign",("positive" if pos else "negative" if neg else "undecided"))
 print("NF411 original z, full scalar and RH remain OPEN")
if __name__=="__main__":main()
