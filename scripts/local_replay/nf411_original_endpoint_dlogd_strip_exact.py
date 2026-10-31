#!/usr/bin/env python3
"""NF411 exact rational L2 budget for the EXTRACTED endpoint d log(B/d) model ONLY.
This does not upper-bound the complete continuous z or its correlation with p.
"""
import argparse,json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from nf407_original_prime_jump_log_power_exact import ilog,I
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10); DELTA=B/(2**24); M=F(131,10**9)
def read(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
 a.add_argument("--center",default="notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
 a.add_argument("--output",required=True)
 a=a.parse_args()
 jet,sh=read(a.jet);center,ch=read(a.center)
 assert jet["pass"]=="NF411" and jet["source_derivative_strict_negative"]
 assert jet["source_derivative_nonzero_certified"] and jet["original_source_native_radii_paid_for_endpoint_derivative"]
 assert jet["W_ODD_NEG"]==jet["RH"]=="OPEN"
 assert center["W_ODD_NEG"]==center["RH"]=="OPEN"
 gamma2=F(center["exact_source_original_full_complement_power_budget"])
 # Native NF411 code must separately certify -131/10^9 < u4'(B) < -129/10^9.
 # The two physical endpoint strips of width delta use odd reflection:
 # T(B-d)=-u4'(B)/2*d*log(B/d).
 # 2 int_0^delta T(B-d)^2 dd
 #   =u4'(B)^2*delta^3/6*[L^2+2L/3+2/9], L=log(B/delta).
 L=ilog(I(2)).u*24
 assert L<F(17)
 # Loose rational L<17 outward upper, no transcendental numeric quadrature:
 bracket=F(17**2)+F(34,3)+F(2,9)
 upper=M*M*DELTA**3*bracket/6
 assert bracket<F(301)
 assert upper<F(3,10**34)
 assert upper<gamma2/F(10**8)
 out={"pass":"NF411","standing":"EXACT RATIONAL UPPER FOR EXPLICIT ENDPOINT d log d MODEL ONLY; TRUE z AND NORM OPEN",
      "nf411_original_source_jet_sha256":sh,"nf404_center_sha256":ch,
      "endpoint_delta_exact":str(DELTA),"endpoint_true_source_derivative_absolute_upper":"131/1000000000",
      "endpoint_log_true_upper":"17","original_two_endpoint_strips_leading_dlogd_power_upper":str(upper),
      "leading_model_power_below_3e_minus34":True,
      "leading_model_power_below_gamma2_over_1e8":True,
      "full_endpoint_regular_remainder_integrated":False,
      "full_endpoint_p_cross_integrated":False,
      "actual_original_continuous_z_integrated":False,
      "original_nf404_cap_decided":False,"W_ODD_NEG":"OPEN","RH":"OPEN"}
 p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(out,indent=2)+"\n")
 print("NF411 original endpoint leading dlogd model power <3e-34 (model ONLY)")
 print("NF411 full continuous z/cross/centered power UNCOMPUTED")
if __name__=="__main__":main()
