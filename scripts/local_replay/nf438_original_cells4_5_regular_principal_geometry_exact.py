#!/usr/bin/env python3
"""NF438 exact original physical cells 4/5: REGULAR vs PRINCIPAL routing.

NF405 regular u4(x±log n) source active translates are distinct from
NF407 principal r jumps at |B-log n|. Independently check both against
NF406 irrational seams, NF410 original m0 custody, and inspect genuine
sourcewise complex Bernstein geometry. Source triangles are candidates
only; no certified z polynomial or signed integral from this router.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from nf425_original_cell6_chebyshev_existence_exact import source
from nf433_original_cell3_cell7_branch_ellipse_router_exact import branch_for_cell,cheb_source_tail
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);PRIMES=(2,3,4,5,7,8,9)
GEOM={4:(11,12,F(459,1000),F(54,1000),(2,3,4,5)),
      5:(12,13,F(678,1000),F(170,1000),(2,3,4))}
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def load(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def principal_jump(n,lo,hi,left_label,right_label,logs):
 loglo,loghi=logs[n]
 if loghi<B:
  a,b=B-loghi,B-loglo;label=f"B-log({n})"
 else:
  assert loglo>B
  a,b=loglo-B,loghi-B;label=f"-B+log({n})"
 if left_label==label:return True
 if right_label==label:return False
 if lo>b:return True
 if hi<a:return False
 raise AssertionError(("original principal jump crossing inside physical cell",n,label))
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
 ap.add_argument("--nf405",default="notes/data/provisional/NF405_original_compact_physical_kernel_exact.json")
 ap.add_argument("--principal",default="notes/data/provisional/NF407_original_prime_jump_log_power_exact.json")
 ap.add_argument("--nf410",default="notes/data/provisional/NF410_original_signed_taylor_moments.json")
 ap.add_argument("--output",required=True)
 a=ap.parse_args()
 s,sha=load(a.source);seams,ksha=load(a.seams)
 physical,phsha=load(a.nf405);principal,psha=load(a.principal);old,oldsha=load(a.nf410)
 assert sha==SOURCE_SHA and ksha==SEAM_SHA
 assert seams["original_nf405_compact_kernel_sha256"]==phsha
 assert principal["original_nf406_seams_sha256"]==ksha
 assert old["original_nf406_source_sha256"]==ksha
 assert old["original_nf407_source_sha256"]==psha
 assert s["original_dimension"]==242
 assert len(s["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert len(s["original_source_critical_sine_frequencies"])==32
 assert physical["actual_original_prime_power_shifts"]==list(PRIMES)
 assert physical["physical_prime_action"]=="-sum_{n=2,3,4,5,7,8,9} Lambda(n)/sqrt(n)*(u4(x+log(n))+u4(x-log(n)))"
 assert all(x["W_ODD_NEG"]==x["RH"]=="OPEN" for x in (s,seams,physical,principal,old))
 assert principal["source_r_formula"]=="r(x)=u4(B)*sgn(x)*sum_{n=2,3,4,5,7,8,9} [Lambda(n)/sqrt(n)]*1_(|x|>abs(B-log(n)))"
 knots=seams["certified_ordered_knots"]
 logs={int(p["n"]):(F(p["log_lower"]),F(p["log_upper"])) for p in seams["original_prime_power_log_shifts"]}
 assert set(logs)==set(PRIMES) and len(knots)==17
 coeff,pole,S0=source(s)
 assert len(coeff)==273 and S0<F(1,10**700)
 assert max(k for f,k in coeff)<=13 and max(f for f,k in coeff)<883
 raw=sum((abs(c)*B**k for (f,k),c in coeff.items()),abs(pole))
 assert raw<10**160
 result={
  "pass":"NF438",
  "standing":"ORIGINAL CELLS4/5 EXACT REGULAR TRANSLATE AND PRINCIPAL JUMP SUPPORT TYPES + ANALYTIC ELLIPSE FEASIBILITY; TRUE SIGNED CELLS OPEN",
  "original_NF407_source_sha256":sha,"original_NF406_seams_sha256":ksha,
  "original_NF405_physical_source_sha256":phsha,
  "original_NF407_principal_source_sha256":psha,
  "original_NF410_principal_moments_source_sha256":oldsha,
  "original_source_selected_plus_critical":246,
  "original_frequency_order_source_groups":len(coeff),
  "original_principal_formula":"p(x)=u4(B)*(log(B/(B-x))/2+sum_(jump-active n) Lambda(n)/sqrt(n))",
  "original_regular_formula":"z has -sum_(regular-active translate) Lambda(n)/sqrt(n)*u4(x±log(n))",
  "cells":{},"original_complete_NF410_NF404_signed_scalar_decided":False,
  "W_ODD_NEG":"OPEN","RH":"OPEN"}
 for cell,(i,j,C,H,rhos) in GEOM.items():
  left,right=knots[i],knots[j]
  leftlo,leftup=F(left["low"]),F(left["high"])
  rightlo,rightup=F(right["low"]),F(right["high"])
  assert 0<leftlo<=leftup<rightlo<=rightup<B
  assert C-H<leftlo and rightup<C+H
  regular_minus=[];regular_plus=[];neither=[];jumps=[];off=[]
  for n in PRIMES:
   minus,plus=branch_for_cell(n,leftup,rightlo,logs,left["label"],right["label"])
   jump=principal_jump(n,leftup,rightlo,left["label"],right["label"],logs)
   if minus:regular_minus.append(n)
   if plus:regular_plus.append(n)
   if not minus and not plus:neither.append(n)
   (jumps if jump else off).append(n)
  expected=([2,3,4] if cell==4 else [2,3,4,5])
  assert regular_minus==expected and regular_plus==[] and jumps==expected
  assert neither==([5,7,8,9] if cell==4 else [7,8,9])
  assert off==neither
  assert len(old["original_positive_original_physical_cells"])==8
  oldcell=old["original_positive_original_physical_cells"][cell-1]
  assert oldcell["cell"]==cell and oldcell["left_label"]==left["label"] and oldcell["right_label"]==right["label"]
  p0lo,p0hi=map(F,oldcell["signed_original_p_moments_by_degree_0_to_3"][0])
  assert p0lo<=p0hi<0
  ellipses=[]
  for rho in rhos:
   rho=F(rho)
   xmax=C+H*(rho+1/rho)/2
   xmin=C-H*(rho+1/rho)/2
   imax=H*(rho-1/rho)/2
   assert xmin>0 and xmax<B
   ellipses.append({"rho":str(rho),"real_min":str(xmin),"real_max":str(xmax),
                    "imag_max":str(imax),"B_minus_real_max":str(B-xmax)})
  if cell==4:
   assert C==F(459,1000) and H==F(54,1000)
   assert B-(C+H*F(13,5))>F(1,2)
  else:
   assert C==F(678,1000) and H==F(170,1000)
   assert B-(C+H*F(17,8))>F(1,20)
   # E5 would hit B: cannot inherit cell4 ellipse family
   assert C+H*F(13,5)>B
  tail=sum((min(cheb_source_tail(f,k,c,F(r),H) for r in rhos)
            for (f,k),c in coeff.items()),F(0))
  counts={str(r):0 for r in rhos}
  for (f,k),c in coeff.items():
   rr=min(rhos,key=lambda r:cheb_source_tail(f,k,c,F(r),H))
   counts[str(rr)]+=1
  result["cells"][str(cell)]={
   "original_true_seam_left":left["label"],"original_true_seam_right":right["label"],
   "exact_seam_left_interval":[str(leftlo),str(leftup)],
   "exact_seam_right_interval":[str(rightlo),str(rightup)],
   "rational_analytic_C":str(C),"rational_analytic_H":str(H),
   "original_regular_z_active_minus":regular_minus,
   "original_regular_z_active_plus":regular_plus,
   "original_regular_z_inactive":neither,
   "original_principal_r_jump_active":jumps,
   "original_principal_r_jump_inactive":off,
   "original_NF410_original_principal_p0_interval":[str(p0lo),str(p0hi)],
   "sourcewise_admissible_Bernstein_ellipses":ellipses,
   "candidate_sourcewise_generator_n512_tail_rational":str(tail),
   "candidate_sourcewise_optimal_rho_counts":counts,
   "candidate_sourcewise_generator_n512_less_than_1e_minus20":tail<F(1,10**20),
   "original_real_cell_specific_2048_image_remainder_certified":False,
   "original_512_native_z_coefficient_intervals_certified":False,
   "original_true_signed_cell_integral_certified":False
  }
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+"\n")
 for key,v in result["cells"].items():
  tri=F(v["candidate_sourcewise_generator_n512_tail_rational"])
  print("NF438 original cell",key,"regular -",v["original_regular_z_active_minus"],
        "+",v["original_regular_z_active_plus"],"principal jumps",v["original_principal_r_jump_active"],
        "ellipse count",len(v["sourcewise_admissible_Bernstein_ellipses"]),
        "generator only n512 tail",float(tri),flush=True)
 print("NF438 exact original distinct regular-vs-principal branch and source ellipse PASS; true signed integral OPEN",flush=True)
if __name__=="__main__":main()
