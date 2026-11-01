#!/usr/bin/env python3
"""NF433 ORIGINAL positive physical cells 3 and 7, exact seam branches.

Machine-proof exact-rational NF406 topology and Bernstein-ellipse feasibility.
The source-wise 512-mode triangle is a candidate only: actual original
cell3/cell7 source-native coefficient balls, signed p moments and
true-cell finite-image remainder have NOT been independently computed.
Never propagate NF432 true cell6 signed certificate to different cells.
"""
import argparse,hashlib,json,math,sys
from fractions import Fraction as F
from pathlib import Path
from nf425_original_cell6_chebyshev_existence_exact import source
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
PRIMES=(2,3,4,5,7,8,9)
GEOM={3:{"left":10,"right":11,"C":F(347,1000),"H":F(61,1000),"rhos":(F(2),F(3),F(4),F(5))},
      7:{"left":14,"right":15,"C":F(1039,1000),"H":F(60,1000),"rhos":(F(11,10),F(9,8),F(7,6))}}
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def ceil(q):return -((-q.numerator)//q.denominator)
def cheb_source_tail(f,k,c,rho,H):
 v=H*(rho-1/rho)/2
 exponent=(2*F(22,7)*f+F(1,8))*v+1
 # 1e8 arch+two-sided image and up to six original prime translates,
 # with full original k!8^k Cauchy source-mode derivative bound.
 # 4 for Cheb coefficient series summation, paired oscillatory modes.
 return 4*10**8*abs(c)*math.factorial(k)*8**k*3**ceil(exponent)*rho**(-512)
def branch_for_cell(n,left,right,logs):
 # original physical prime action -w_n[u(x-log n)+u(x+log n)]
 # support of u(y) is |y|<B; for 0<x<B, right translates
 # x-log n active iff x>log n-B;
 # x+log n active iff x<B-log n.
 L=logs[n]
 minus_lo=L[0]-B;minus_hi=L[1]-B
 plus_lo=B-L[1];plus_hi=B-L[0]
 if left>minus_hi: minus=True
 elif right<minus_lo:minus=False
 else:raise AssertionError(("minus translate changes inside cell",n))
 if right<plus_lo: plus=True
 elif left>plus_hi:plus=False
 else:raise AssertionError(("plus translate changes inside cell",n))
 return minus,plus
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
 ap.add_argument("--nf405",default="notes/data/provisional/NF405_original_compact_physical_kernel_exact.json")
 ap.add_argument("--nf432",default="scripts/local_replay/nf432_original_cell6_sourcewise_512_tail_exact.py")
 ap.add_argument("--output",required=True)
 args=ap.parse_args()
 s,ssha=read(args.source);seams,ksha=read(args.seams);phys,phsha=read(args.nf405)
 assert s["original_dimension"]==242 and len(s["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert len(s["original_source_critical_sine_frequencies"])==32
 assert s["W_ODD_NEG"]==s["RH"]==seams["W_ODD_NEG"]==seams["RH"]==phys["W_ODD_NEG"]==phys["RH"]=="OPEN"
 assert seams["original_nf405_compact_kernel_sha256"]==phsha
 assert seams["number_of_open_physical_support_cells"]==16
 assert phys["actual_original_prime_power_shifts"]==list(PRIMES)
 assert phys["physical_prime_action"]=="-sum_{n=2,3,4,5,7,8,9} Lambda(n)/sqrt(n)*(u4(x+log(n))+u4(x-log(n)))"
 knots=seams["certified_ordered_knots"]
 assert len(knots)==17
 logs={int(p["n"]):(F(p["log_lower"]),F(p["log_upper"])) for p in seams["original_prime_power_log_shifts"]}
 assert set(logs)==set(PRIMES)
 coeff,pole,S0=source(s)
 assert len(coeff)==273 and S0<F(1,10**700)
 raw=sum((abs(c)*B**k for (f,k),c in coeff.items()),abs(pole))
 assert raw<10**160 and max(k for f,k in coeff)<=13 and max(f for f,k in coeff)<883
 source_pin=hashlib.sha256(Path(args.nf432).read_bytes()).hexdigest()
 result={"pass":"NF433","standing":"ACCEPTED ORIGINAL CELL3/7 SEAM/BRANCH AND ELLIPSE GEOMETRY ROUTER; NO NATIVE RESPONSE OR SIGNED CELL INTEGRALS",
         "original_NF407_source_sha256":ssha,"original_NF406_seams_sha256":ksha,
         "original_NF405_physical_sha256":phsha,"NF432_parent_source_tail_script_sha256":source_pin,
         "original_242_plus_four_source_count":246,"original_frequency_degree_groups":len(coeff),
         "physical_prime_shift_weights":"Lambda(n)/sqrt(n); original both x+logn and x-logn",
         "positive_physical_cells":8,"cells":{},"W_ODD_NEG":"OPEN","RH":"OPEN"}
 for cell,g in GEOM.items():
  i,j=g["left"],g["right"]
  leftlo,leftup=F(knots[i]["low"]),F(knots[i]["high"])
  rightlo,rightup=F(knots[j]["low"]),F(knots[j]["high"])
  assert 0<leftlo<=leftup<rightlo<=rightup<B
  C,H=g["C"],g["H"]
  assert C-H<leftlo and rightup<C+H
  active_minus=[];active_plus=[];neither=[]
  for n in PRIMES:
   minus,plus=branch_for_cell(n,leftup,rightlo,logs)
   if minus:active_minus.append(n)
   if plus:active_plus.append(n)
   if not (minus or plus):neither.append(n)
  assert active_minus==([2,3,4] if cell==3 else [2,3,4,5,7,8])
  assert active_plus==([2] if cell==3 else [])
  assert neither==([5,7,8,9] if cell==3 else [9])
  # Independent validity of each chosen ellipse: left endpoint
  # support x>-B and right endpoint singularity x<B.
  admissible=[]
  for rho in g["rhos"]:
   realmax=C+H*(rho+1/rho)/2
   immax=H*(rho-1/rho)/2
   assert realmax<B and C-H*(rho+1/rho)/2>0
   d=B-realmax
   assert d>0
   admissible.append({"rho":str(rho),"real_upper":str(realmax),"imag_absolute_max":str(immax),
                      "original_endpoint_distance_lower":str(d)})
  # Sourcewise independent ellipse candidate; NO cell-specific
  # native response coefficients yet. Evaluate exact generator triangle
  # to diagnose feasibility of n>=512 source tail, never claim full z.
  bounds={}
  for rho in g["rhos"]:
   tri=sum((cheb_source_tail(f,k,c,rho,H) for (f,k),c in coeff.items()),F(0))
   bounds[str(rho)]=tri
  # Cell3: term-by-term best rho works because all source ellipses
  # contain the same physical fixed cell3 analytic branch. For cell7
  # narrow rho cause low-frequency huge original source overestimate,
  # and genuine near-boundary 2048-image remainder is NOT transferable.
  per_source=sum((min(cheb_source_tail(f,k,c,rho,H) for rho in g["rhos"])
                  for (f,k),c in coeff.items()),F(0))
  if cell==3:
   assert per_source<F(1,10**20)
  else:
   assert per_source>F(1,10**20)
   # True original cell7 endpoint B-log9 has B-x near 0.0028,
   # so the old NF424 real-cell [0.84,.98] image-tail proof does
   # not cover cell7; do not silently transfer it.
   assert rightup>B-F(1,100)
  result["cells"][str(cell)]={
   "physical_cell_number":cell,
   "left_original_seam":knots[i]["label"],"right_original_seam":knots[j]["label"],
   "original_left_exact_rational_interval":[str(leftlo),str(leftup)],
   "original_right_exact_rational_interval":[str(rightlo),str(rightup)],
   "sourcewise_analytic_C":str(C),"sourcewise_analytic_H":str(H),
   "original_minus_translate_active":active_minus,
   "original_plus_translate_active":active_plus,
   "original_neither_translate":neither,
   "number_of_active_translate_terms":len(active_minus)+len(active_plus),
   "ellipses_each_with_strict_B_pole_clearance":admissible,
   "single_rho512_sourcewise_untruncated_generator_triangle":{r:str(v) for r,v in bounds.items()},
   "minimum_sourcewise_512_generator_triangle_exact":str(per_source),
   "sourcewise_finite_model_512_generator_tail_less_than_1e_minus20":per_source<F(1,10**20),
   "NF432_original_cell6_image_remainder_reusable_without_new_proof":False,
   "original_response_coefficient_intervals_certified":0,
   "true_original_signed_pz_z2_integrals_certified":False
  }
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+"\n")
 print("NF433 PASS original NF406 exact positive cell3/7 prime-translate branches and endpoint ellipse geometry")
 for c in ("3","7"):
  a=result["cells"][c]
  print("cell",c,"minus",a["original_minus_translate_active"],"plus",a["original_plus_translate_active"],"neither",a["original_neither_translate"],"sourcewise candidate <1e-20",a["sourcewise_finite_model_512_generator_tail_less_than_1e_minus20"])
 print("Original cell3/7 native coefficients, signed integrals, global NF404 and RH remain OPEN")
if __name__=="__main__":main()
