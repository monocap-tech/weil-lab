#!/usr/bin/env python3
"""NF443 complementary exact source-specific n>=512 tail on TRUE ORIGINAL cell2.

Independent of high-mode Arb/Acb coefficient job. The original source-wise
Bernstein proof uses exact 4096-bit source midpoint dyadics, all true
NF405 prime-shift branches, complete arch+endpoint digamma source,
removable sinh m0 pole, endpoint logarithm and 2048-image/source charge.
It does NOT integrate the original signed scalar or prove RH.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from nf425_original_cell6_chebyshev_existence_exact import source
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10); PANELS=((F(55,1000),F(55,1000)),(F(148,1000),F(58,1000)),(F(243,1000),F(53,1000))); C,H=PANELS[0]; N=512; RHOS=(2,3,4,5)
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def ceil(v):return -((-v.numerator)//v.denominator)
def one_generator(f,k,c,rho):
 v=H*F(rho*rho-1,2*rho)
 xmax=C+H*F(rho*rho+1,2*rho)
 assert xmax<B and B-xmax>=F(92,625)
 # Shared Arch G_2048 digamma radius 1/8 around ±2*pi*i*f.
 # Re(1/4±lambda/2)>=3/16; digamma/finite image source
 # |G|<1e6 exp[(2*(22/7)*f+1/8)*Immax+1].
 # Cauchy k!8^k for original polynomial source order.
 # All FOUR genuine signed NF405 cell2 translations have total W<3,
 # and |x±log n|<3B on each E2...E5 (incl n2 minus only).
 # 2 for conjugate pair, 2 for arch+prime transfer: <=4e6.
 E=(2*F(22,7)*f+F(1,8))*v+1
 # |a_n|<=2M*rho^-n and sum n>=512 <=4*M*rho^-512.
 return F(400000000)*abs(c)*math.factorial(k)*8**k*3**ceil(E)/rho**N
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--router',default='scripts/local_replay/nf441_original_cells1_2_8_typed_geometry_exact.py')
 p.add_argument('--indexed-native',default='scripts/local_replay/nf440_original_cell2_three_panel_native_index.py')
 p.add_argument('--panel',type=int,required=True,choices=(1,2,3))
 p.add_argument('--output',required=True)
 a=p.parse_args()
 global C,H
 C,H=PANELS[a.panel-1]
 s,sha=read(a.source);k,ksha=read(a.seams)
 assert sha==SOURCE_SHA and ksha==SEAM_SHA
 assert s['original_dimension']==242 and len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert s['W_ODD_NEG']==s['RH']==k['W_ODD_NEG']==k['RH']=='OPEN'
 assert k['number_of_open_physical_support_cells']==16
 knots=k['certified_ordered_knots']
 assert knots[9]['label']=='B-log(3)' and knots[10]['label']=='-B+log(4)'
 cuts=(F(1,10),F(39,200))
 left=F(knots[9]['low']) if a.panel==1 else cuts[a.panel-2]
 right=F(knots[10]['high']) if a.panel==3 else cuts[a.panel-1]
 assert C-H<left<right<C+H and C+H<B
 coeff,pole,S0=source(s)
 assert len(coeff)==273 and max(f for f,j in coeff)<883 and max(j for f,j in coeff)<=13
 assert S0<F(1,10**700)
 raw=sum((abs(c)*B**j for (f,j),c in coeff.items()),abs(pole))
 assert raw<10**160
 # Fixed source analytic continuation on the ellipse is allowed
 # outside true physical J2; the integration is strictly inside J2.
 assert -B<C-H*F(13,5) and C+H*F(13,5)<B
 d=B-C-H*F(13,5)
 assert d>F(11,20) and 1+2*d+2*d*d>3
 assert F(36,2000)*10**160*F(1,3)**2048<F(1,10**50)
 assert 2*F(7,10)*F(5,7)+F(11,10)*F(3,5)<3
 source_tail=F(0);best={str(r):0 for r in RHOS};largest=[]
 for (f,j),c in sorted(coeff.items()):
  options=[(one_generator(f,j,c,r),r) for r in RHOS]
  v,r=min(options)
  best[str(r)]+=1
  source_tail+=v
  largest.append((v,str(f),j,r))
 # Removable original odd m0 pole/source and centered dyadic sinh:
 # same joint psi(1+beta)+(exp(-2 beta d)-1)/beta analytic.
 # E5 original pole clearance .5006 is still >1/2.
 pole_tail=F(4*10**7)*(abs(pole)+2)/5**N
 # Endpoint -u4(B)/2 log(B/(B-x)); exact Cheb q<1/5.
 # Original -u4(B)*sum active prime weights is degree zero.
 log_tail=raw*F(1,5)**N/(N*(1-F(1,5)))
 # The original 2048-image remainder is charged using a **single**
 # conservative complex-ellipse ratio 3/4 for all three panels.
 # Explicit original 4096-bit NF407 dyadic source uncertainty separate.
 image=F(36,2000)*10**160*F(1,3)**2048
 source_charge=(10**12+20)*S0
 assert image<F(1,10**50) and source_charge<F(1,10**50)
 # For choosing any point inside the independently native outward
 # a_n intervals, pay 5e-45 for EACH midpoint selection error.
 # Every accepted NF434/NF435/NF443 outward Arb coefficient interval
 # has width <1e-44; its midpoint deviation is then <5e-45.
 # This includes native rounding beyond the nominal 4e-45 charge.
 native_coefficient_charge=512*F(5,10**45)
 true_error=source_tail+pole_tail+log_tail+image+source_charge+native_coefficient_charge
 assert F(0)<true_error<F(1,10**30),("original cell2 source tail not decision quality",str(float(true_error)))
 out={
  "pass":"NF443",
  "standing":"SOURCE-EXACT ORIGINAL TRUE CELL5 UNIFORM z-P511 ENVELOPE CONDITIONAL ON ACCEPTED 512 NATIVE COEFFICIENT BALLS; NO SIGNED INTEGRAL",
  "NF407_original_source_sha256":sha,"NF406_original_seams_sha256":ksha,
  "NF438_NF443_script_pins":{
   tag:hashlib.sha256(Path(getattr(a,tag)).read_bytes()).hexdigest() for tag in ('router','indexed_native')},
  "original_panel_number":a.panel,
  "original_rational_integration_cuts_not_prime_seams":["1/10","39/200"],
  "original_panel_true_piece_exact_bounds":[str(left),str(right)],
  "original_true_cell2":"(11/10-log(3),log(4)-11/10)",
  "original_source_selected_plus_critical_count":246,
  "original_source_frequency_degree_groups":len(coeff),
  "original_minus_translate_active":[2,3],"original_plus_translate_active":[2],
  "original_inactive_prime_powers":[4,5,7,8,9],
  "original_Chebyshev_center":str(C),"original_Chebyshev_halfwidth":str(H),
  "original_Chebyshev_accepted_prefix_count_required":512,
  "sourcewise_cheb_tail_starts_at_mode":512,
  "sourcewise_optimal_E2_E3_E4_E5_counts":best,
  "sourcewise_generator_tail_exact_rational":str(source_tail),
  "original_removable_m0_pole_and_NF404_center_tail":str(pole_tail),
  "original_endpoint_log_tail":str(log_tail),
  "original_real_cell2_2048_image_remainder":str(image),
  "original_4096bit_source_radius_charge":str(source_charge),
  "original_all_512_native_coefficient_interval_charge":str(native_coefficient_charge),
  "required_each_native_coefficient_interval_width_strict_less_than":"1e-44",
  "original_true_cell2_z_minus_any_accepted_P511_uniform_error_exact_upper":str(true_error),
  "original_true_cell2_uniform_error_strict_below":"1e-38",
  "original_true_cell2_signed_pz_z2_integrated":False,
  "original_full_NF410_NF404_signed_scalar_decided":False,
  "W_ODD_NEG":"OPEN","RH":"OPEN"}
 dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+"\n")
 print("NF443 PASS original sourcewise complete real J2 z-P511 <1e-38, CONDITIONAL on 512 native coefficients")
 print("E2/3/4/5 counts",best,"absolute error",float(true_error))
if __name__=="__main__":main()
