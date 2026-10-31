#!/usr/bin/env python3
"""NF432 rigorous source-frequency/order-separated original cell6 Chebyshev tail.

Original NF407 all 242+4 exact source midpoint dyadics, NF406 true cell,
NF423/NF424 source-image and NF431 512 original coefficient interface.
For every original (frequency, degree) source generator choose the best
of four independently valid E_rho discs rho=2,3,4,5 and sum outward
exact rational coefficient-tail envelopes n>=512. NEVER infer decay
from observed adjacent finite coefficients or from a sampled grid.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from pathlib import Path
from fractions import Fraction as F
from nf425_original_cell6_chebyshev_existence_exact import source

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);C=F(91,100);H=F(7,100);N=512
RHOS=(2,3,4,5)

def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def ceil(x):
 return -((-x.numerator)//x.denominator)
def envelope(f,k,c,rho):
 """Complete G_2048 arch plus all five original signed prime translates."""
 v=H*F(rho*rho-1,2*rho)
 xmax=C+H*F(rho*rho+1,2*rho)
 assert xmax<B and B-xmax>=F(1,125)
 # For source lambda discs radius1/8, Re psi args>=3/16,
 # |D|<64002, and both endpoint images together <1024,
 # so |G_2048(x,lambda)|<1e6 exp(E) on E_rho.
 # E bounds frequency oscillation + real lambda disk growth.
 E=(2*F(22,7)*f+F(1,8))*v+F(1)
 assert E>0
 # Cauchy derivatives <= k!8^k*(1e6 exp(E)).
 # Signed five prime translates each |x-log n|<3B, W<3.
 # Real sin/cos paired exponential ≤2 times complex bound.
 # Thus |f_{f,k}| <=4e6 |c| k!8^k exp(E);
 # use e<3 and standard Cheb SERIES tail ≤4 M/rho^N.
 return F(16000000)*abs(c)*math.factorial(k)*8**k*3**ceil(E)/rho**N,ceil(E)
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
 ap.add_argument("--nf423",default="notes/data/provisional/NF423_original_entire_open_cell6_zthird_native.json")
 ap.add_argument("--nf430",default="scripts/local_replay/nf430_original_cell6_sharper_ellipse_series_cutoff_exact.py")
 ap.add_argument("--nf431",default="scripts/local_replay/nf431_original_cell6_correlated_cheb_high_block_native.py")
 ap.add_argument("--output",required=True)
 args=ap.parse_args()
 s,ssha=read(args.source);knots,ksha=read(args.seams);prior,psha=read(args.nf423)
 assert s["original_dimension"]==242 and len(s["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert len(s["original_source_critical_sine_frequencies"])==32
 assert s["W_ODD_NEG"]==s["RH"]=="OPEN"
 assert prior["original_nf407_source_sha256"]==ssha
 assert prior["original_nf406_exact_support_seams_sha256"]==ksha
 assert prior["true_original_entire_open_cell6_zthird_uniform_strict_upper"]==286758
 assert prior["original_all_seven_real_signed_prime_branches_inside_open_cell"]==["post-seam"]*5+["neither"]*2
 assert prior["true_active_prime_weight_strict_upper"]==3
 knots=knots["certified_ordered_knots"]
 assert knots[13]["label"]=="-B+log(7)" and knots[14]["label"]=="-B+log(8)"
 assert F(21,25)<F(knots[13]["low"])<F(knots[13]["high"])<F(knots[14]["low"])<F(knots[14]["high"])<F(49,50)
 coeff,pole,S0=source(s)
 assert len(coeff)>80 and max(k for f,k in coeff)<=13
 assert min(f for f,k in coeff)>0 and max(f for f,k in coeff)<883
 raw=sum((abs(c)*B**k for (f,k),c in coeff.items()),abs(pole))
 assert raw<10**160 and S0<F(1,10**700)
 # Uniform common ellipse geometry, digamma/source-gate conditions:
 assert C+H*F(26,10)==F(273,250) and B-F(273,250)==F(1,125)
 assert F(1,4)-F(1,16)==F(3,16)
 assert F(1)+10000*(1+F(16,3))+F(4000,9999)<64000
 assert 1+F(1)/(2*(B-(C+H*F(26,10))))<64
 assert F(22,7)<4
 assert 3**13<10**7 and math.factorial(13)*8**13<10**24
 # For EVERY frequency/order, use its own best admissible ellipse.
 # All 4 choices bound the SAME coefficient tail on the actual J6.
 source_sum=F(0); by_rho={str(r):0 for r in RHOS}; largest=[]
 for (f,k),c in sorted(coeff.items()):
  opts=[(envelope(f,k,c,r)[0],r,envelope(f,k,c,r)[1]) for r in RHOS]
  bound,r,exp=min(opts)
  source_sum+=bound
  by_rho[str(r)]+=1
  largest.append((bound,str(f),k,r,exp))
 # Original odd sinh pole: at lambda=+/-1/2 join psi(beta)+m0 image
 # as psi(1+beta)+(exp(-2 beta d)-1)/beta, beta=0, giving
 # |G_2048(x,+/-1/2)|<1e6 on rho5, independent of imaginary f.
 # The five genuine shifted primes add <9|pole| and centering <6.
 # Generous common bound, cp and centered source still tracked.
 pole_tail=4*10**7*(abs(pole)+2)*F(1,5)**N
 # Original endpoint log only: Chebyshev coeff for n>=1 is 2q^n/n,
 # q=7/(19+2sqrt78)<1/5. The -u(B)/2 gives coeff <=|u(B)| q^n/n.
 # Original -u(B)*W is constant and has NO n>=1 tail.
 log_tail=raw*F(1,5)**N/(N*(1-F(1,5)))
 image=F(36,2000)*10**160*F(3,8)**480
 source_charge=(10**12+20)*S0
 assert image+source_charge<F(1,10**45)
 tail=source_sum+pole_tail+log_tail
 eps=tail+image+source_charge
 assert eps<F(1,10**20),("source-specific tail exceeds decision-quality cap",str(float(tail)))
 source_pins={}
 for key,path in [("NF430",args.nf430),("NF431",args.nf431)]:
  source_pins[key]=hashlib.sha256(Path(path).read_bytes()).hexdigest()
 largest.sort(reverse=True)
 output={
  "pass":"NF432",
  "standing":"SOURCE-EXACT ORIGINAL COMPLETE CELL6 P511 TRUE-Z UNIFORM TAIL CERTIFIED; SIGNED INTEGRAL CONDITIONAL ON SEPARATE NF431 ARTIFACT CONTRACTION",
  "original_nf407_full_source_sha256":ssha,
  "original_nf406_seams_sha256":ksha,
  "original_nf423_parent_sha256":psha,
  "original_script_sha256":source_pins,
  "original_source_generators":246,
  "original_frequency_degree_groups":len(coeff),
  "original_true_cell6":"(log(7)-11/10,log(8)-11/10)",
  "original_post_seam_primes":[2,3,4,5,7],
  "original_neither_primes":[8,9],
  "original_NF404_center":"6677356497477490213/4611686018427387904",
  "true_source_high_Chebyshev_tail_starts_at_n":N,
  "sourcewise_E2_E3_E4_E5_best_counts":by_rho,
  "sourcewise_exact_rational_high_mode_tail":str(source_sum),
  "source_pole_high_mode_tail":str(pole_tail),
  "source_endpoint_log_high_mode_tail":str(log_tail),
  "original_full_cell6_image_tail":str(image),
  "original_full_cell6_source_ball_charge":str(source_charge),
  "original_true_z_vs_original_P511_uniform_error_exact_rational_upper":str(eps),
  "original_true_z_vs_original_P511_uniform_error_strict_below":"1e-20",
  "original_p511_coefficients_certified_by_NF428_NF431":512,
  "next_753_individual_coefficient_balls_required_for_uniform_accuracy":False,
  "original_full_cell6_signed_integral_evaluated_by_this_script":False,
  "original_NF404_full_scalar_decided":False,
  "W_ODD_NEG":"OPEN","RH":"OPEN"}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(output,indent=2)+"\n")
 print("NF432 PASS source-specific original P511 tail <1e-20; actual signed J6 integral is a separate gate")
 print("source groups",len(coeff),"best rho counts",by_rho,"largest",[(float(x[0]),x[1],x[2],x[3]) for x in largest[:4]])
if __name__=="__main__":
 main()
