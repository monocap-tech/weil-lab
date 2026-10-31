#!/usr/bin/env python3
"""NF430: source-exact sharpened cell6 E2/Chebyshev cutoff, no scalar."""
import argparse, hashlib, json, math, sys
from fractions import Fraction as F
from pathlib import Path
from nf425_original_cell6_chebyshev_existence_exact import source
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);C=F(91,100);H=F(7,100)
def load(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",required=True)
 ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
 ap.add_argument("--parent",default="notes/data/provisional/NF423_original_entire_open_cell6_zthird_native.json")
 ap.add_argument("--nf425",default="scripts/local_replay/nf425_original_cell6_chebyshev_existence_exact.py")
 ap.add_argument("--nf427",default="scripts/local_replay/nf427_original_cell6_chebyshev_series_tail_exact.py")
 ap.add_argument("--nf429",default="scripts/local_replay/nf429_original_cell6_chebyshev_square_router_native.py")
 args=ap.parse_args()
 s,ssha=load(args.source);knots,ksha=load(args.seams);p,psha=load(args.parent)
 assert s["original_dimension"]==242 and len(s["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert len(s["original_source_critical_sine_frequencies"])==32
 assert s["W_ODD_NEG"]==s["RH"]=="OPEN"
 assert p["original_nf407_source_sha256"]==ssha
 assert p["original_nf406_exact_support_seams_sha256"]==ksha
 assert p["true_original_entire_open_cell6_zthird_uniform_strict_upper"]==286758
 assert p["original_all_seven_real_signed_prime_branches_inside_open_cell"]==["post-seam"]*5+["neither"]*2
 k=knots["certified_ordered_knots"]
 assert k[13]["label"]=="-B+log(7)" and k[14]["label"]=="-B+log(8)"
 assert F(21,25)<F(k[13]["low"])<F(k[13]["high"])<F(k[14]["low"])<F(k[14]["high"])<F(49,50)
 coeff,pole,radius=source(s)
 raw=sum((abs(q)*B**j for (f,j),q in coeff.items()),abs(pole))
 assert raw<10**160 and radius<F(1,10**700)
 assert max(j for f,j in coeff)<=13 and max(f for f,j in coeff)<883
 assert C+F(5,4)*H==F(399,400) and F(3,4)*H==F(21,400)
 assert B-F(399,400)>F(1,10)
 assert F(1,4)-F(1,16)==F(3,16)
 assert F(1)+10000*(1+F(16,3))+F(4000,9999)<64000
 assert 1+1/(2*(B-F(399,400)))<6
 assert math.factorial(13)*8**13<10**24 and 3**13<10**7
 # Same NF425 source-frequency Cauchy/psi/image proof. Replacing
 # pi<4 by pi<22/7 reduces source complex oscillation exponent.
 # Include all five prime-translated source factors: Re shift <3B.
 exponent=(2*F(22,7)*883+F(1,8))*F(21,400)+3*B/8
 assert exponent<293
 # e<3; all remaining original NF425 transfer triangle costs 1e190.
 assert 10**190*3**293<10**330
 count=1265
 tail=F(4*10**330,2**count)
 assert tail<F(1,10**50)
 assert F(4*10**330,2**(count-1))>=F(1,10**50)
 image=F(36,2000)*10**160*F(3,8)**480
 source_error=(10**12+20)*radius
 assert image+source_error<F(1,10**45)
 residual=tail+image+source_error
 assert residual<F(2,10**45)
 sha={key:hashlib.sha256(Path(path).read_bytes()).hexdigest() for key,path in
      [("NF425_script",args.nf425),("NF427_script",args.nf427),("NF429_script",args.nf429)]}
 out={"pass":"NF430","standing":"SOURCE-EXACT SHARPENED ORIGINAL CELL6 1265-MODE SERIES CUTOFF; SIGNED INTEGRAL OPEN",
      "original_nf407_sha256":ssha,"original_nf406_sha256":ksha,"original_nf423_sha256":psha,
      "original_parent_scripts_sha256":sha,"active_obligation":"W-ODD-NEG",
      "original_cell6":"(log(7)-11/10,log(8)-11/10)",
      "original_selected_plus_critical_generators":246,
      "original_prime_post_seam":[2,3,4,5,7],"original_prime_neither":[8,9],
      "sharper_oscillation_exponent_rational":str(exponent),
      "original_fixed_cell6_Bernstein_E2_upper":"1e330",
      "Chebyshev_series_modes_required":count,"modes_eliminated":1500-count,
      "already_certified_NF428_modes":256,"remaining_source_coefficient_modes":count-256,
      "series_tail_rational":str(tail),"original_2048_image_tail_rational":str(image),
      "original_source_ball_error_rational":str(source_error),"full_cell6_uniform_remainder_rational":str(residual),
      "full_cell6_uniform_error_strict_less_than":"2e-45",
      "NF428_original_signed_p_moments_available":1500,"NF429_original_dx_moments_available":2999,
      "new_quadratic_dx_moments_needed":2*count-1,
      "all_1265_original_coefficients_certified":False,
      "true_original_cell6_integral_certified":False,
      "NF404_signed_scalar_decided":False,"W_ODD_NEG":"OPEN","RH":"OPEN"}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+"\n")
 print("NF430 original E2<1e330, series n>=1265 tail <1e-50, 1009 modes OPEN")
if __name__=="__main__": main()
