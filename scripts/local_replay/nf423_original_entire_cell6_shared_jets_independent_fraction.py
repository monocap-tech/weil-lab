#!/usr/bin/env python3
"""NF423 independent exact Fraction original 246-source jet and full cell audit.

Reconstruct NF407 dyadic source triangle, recompute every shared derivative
native analytic tail and source coefficient charge WITHOUT Arb; verify all
4 same-source z-derivative intervals and predecessor overlap. Audit true
NF406 entire open physical cell6 and full native A-ball exactly as Fraction,
source-parity-correct moving endpoints and signed five-prime bound. Compose
new certified true-positive interval from z,z',z'' and whole cell6 z'''
bound. This does NOT complete full-cell scalar/pz/z² integration.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
from nf417_original_hotspots_independent_fraction_replay import read,source_contract
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10);T1=F(2,5);T2=F(4)
def arb_ball(s):
 assert s.startswith('[') and s.endswith(']') and ' +/- ' in s
 a,b=s[1:-1].split(' +/- ')
 with localcontext() as ctx:
  ctx.prec=8000
  m=F(Decimal(a));r=F(Decimal(b))
 assert r>=0
 return m-r,m+r
def signed_radius(z0,z1,z2,M,upper):
 def bound(r):
  return z0-z1*r-z2*r*r/2-M*r*r*r/6
 lo=F(0);hi=upper
 assert bound(lo)>0
 for _ in range(110):
  mid=(lo+hi)/2
  if bound(mid)>0:lo=mid
  else:hi=mid
 r=F((lo*10**12).numerator//(lo*10**12).denominator,10**12)
 assert r>0 and r<=hi and bound(r)>0
 return r,bound(r)
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 p.add_argument('--nf416',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 p.add_argument('--nf419',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 p.add_argument('--nf421',default='notes/data/provisional/NF421_original_cell6_complete_second_xjet_native.json')
 p.add_argument('--nf421interval',default='notes/data/provisional/NF421_original_local_third_taylor_independent_fraction.json')
 p.add_argument('--transfer',default='notes/data/provisional/NF422_original_all_order_arch_transfer_exact.json')
 p.add_argument('--native',default='notes/data/provisional/NF423_original_shared_response_jets_native.json')
 p.add_argument('--whole',default='notes/data/provisional/NF423_original_entire_open_cell6_zthird_native.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 source,ssha=read(a.source);seams,seamsha=read(a.seams)
 curv,csha=read(a.nf413);z0,zsha=read(a.nf416)
 z1,jsha=read(a.nf419);z2,ksha=read(a.nf421)
 old,oldsha=read(a.nf421interval);trans,tsha=read(a.transfer)
 native,nsha=read(a.native);whole,wsha=read(a.whole)
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (source,seams,curv,z0,z1,z2,old,trans,native,whole))
 assert len(source['original_selected_generator_node_orders'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert ssha==curv['original_nf407_full_native_source_sha256']==native['original_nf407_source_sha256']
 assert ssha==whole['original_nf407_source_sha256']==trans['original_nf407_source_sha256']
 assert seamsha==whole['original_nf406_exact_support_seams_sha256']
 assert native['original_nf422_all_order_transfer_sha256']==tsha
 assert native['original_nf416_complete_point_parent_sha256']==zsha
 assert native['original_nf419_complete_first_jet_parent_sha256']==jsha
 assert native['original_nf421_complete_second_jet_parent_sha256']==ksha
 assert whole['original_NF422_correct_odd_derivative_endpoint_sign']
 assert trans['NF421_original_analytic_third_identity_as_written_needs_correction']
 U,S0,fmax=source_contract(source)
 assert F(882)<fmax<F(883) and U<10**160
 assert F(native['original_source_raw_triangle_exact'])==U
 assert F(native['original_source_coefficient_radius_S0_exact'])==S0
 Rs=F(8*3**62)*U*F(62)**518/math.factorial(518)
 Rr=F(3**16)*U*F(16)**288/math.factorial(288)
 R3s=10**12*Rs;R3r=10**12*Rr
 TAU=F(1,50);STEP=F(1,100)
 RH=6*TAU**61/(1-TAU)
 E0small=6*R3s/531+10**5*RH
 RK0=81*F(2,5)**161/F(3,5)
 E0large=(T1-TAU)*(100*R3r+RK0*(50000+R3r))
 RK1=81*(STEP/T1)**49/(1-STEP/T1)
 E1=(T2-T1)*(5*R3r+RK1*(50000+R3r))
 Ec=(10**20*S0)*T1*T1/8+20*10**12*S0+10**26*S0
 E=E0small+E0large+E1+Ec
 for key,val in {
 'source_derivative_third_t0_tail_exact':R3s,
 'source_derivative_third_regular_tail_exact':R3r,
 'original_zero_t_analytic_source_tail_error_exact':E0small,
 'original_I0_regular_analytic_source_tail_error_exact':E0large,
 'original_I1_regular_analytic_source_tail_error_exact':E1,
 'original_true_source_coefficient_charge_exact':Ec,
 'original_source_shared_response_per_order_integral_error_bound_exact':E}.items():
  assert F(native[key])==val,('original shared source exact analytic tail mismatch',key)
 assert native['full_original_shared_I0_panel_count']==38 and native['full_original_shared_I1_panel_count']==360
 assert native['all_four_original_derivative_orders_computed_simultaneously']==[0,1,2,3]
 vals=[list(map(F,p)) for p in native['original_true_full_response_z_derivatives_0_to_3_source_paid_rational_intervals']]
 assert len(vals)==4 and all(lo<hi for lo,hi in vals)
 earlier=[
 list(map(F,z0['original_true_full_z_cell6_at_x9over10_outward_interval'])),
 list(map(F,z1['true_original_complete_zprime_at_9over10_outward_rational_interval'])),
 list(map(F,z2['true_original_complete_zsecond_at_x9over10_outward_rational_interval']))]
 for i in range(3):assert max(vals[i][0],earlier[i][0])<=min(vals[i][1],earlier[i][1])
 assert vals[3][0]<0 and vals[3][1]<0
 # Entire original NF406 exact knot-defined physical open cell6,
 # not assumed as [.84,.99] or sampled at non-source points.
 knots=seams['certified_ordered_knots']
 assert knots[13]['label']=='-B+log(7)' and knots[14]['label']=='-B+log(8)'
 assert F(21,25)<F(knots[13]['low'])<F(knots[13]['high'])<F(knots[14]['low'])<F(knots[14]['high'])<F(99,100)
 assert whole['original_true_entire_cell_open_exact_description']=='(log(7)-11/10,log(8)-11/10)'
 assert whole['native_interval_evaluated_on_strict_original_cell_superset']==['21/25','99/100']
 aa0,aa1=arb_ball(whole['native_interval_arch_A_ball'])
 assert max(abs(aa0),abs(aa1))<whole['true_analytic_arch_A_absolute_strict_upper']
 assert whole['original_all_seven_real_signed_prime_branches_inside_open_cell']==['post-seam']*5+['neither']*2
 assert whole['true_active_prime_weight_strict_upper']==3
 # Independently verify the actual full-cell R'' bound from exact
 # rational kernel inequalities, not a dependency-collapsed Arb ball.
 def kpp_bound(t):
  return F(2)/t*((F(1,4)+1/t)**2+1/t+1/t**2)
 dmin=B-F(99,100)
 t1min=2*dmin
 t2min=2*(B+F(21,25))
 R2exact=4*kpp_bound(t1min)+4*kpp_bound(t2min)+1/dmin**3
 assert R2exact==F(whole['true_Rsecond_source_kernel_rational_upper_exact'])
 assert R2exact<whole['true_Rsecond_strict_upper']==2600
 assert not whole['true_Rsecond_direct_broad_Arb_interval_used']
 assert whole['true_original_source_u4_third_global_sup_strict']==24580
 assert whole['true_original_source_u4_fourth_L2_strict']==16384
 MA=whole['true_analytic_arch_A_absolute_strict_upper']
 P=whole['true_active_prime_weight_strict_upper']
 endpoint=whole['true_original_zthird_endpoint_and_center_budget_strict']
 M=(MA+P)*24580+7*16384+endpoint
 assert M==whole['true_original_entire_open_cell6_zthird_uniform_strict_upper']
 assert M<1540338 and M>0
 assert vals[3][0]>-M and vals[3][1]<M
 # Signed source-certified cubic Taylor from original complete z,z',z''
 # valid inside the ENTIRE open physical cell6; optimise only near .9.
 z0lo,z0hi=vals[0];z1max=max(abs(t) for t in vals[1]);z2max=max(abs(t) for t in vals[2])
 radius,lower=signed_radius(z0lo,z1max,z2max,F(M),F(1,1000))
 assert radius>F(old['original_certified_positive_micro_radius_exact'])
 assert X-radius>F(knots[13]['high']) and X+radius<F(knots[14]['low'])
 zupper=z0hi+z1max*radius+z2max*radius**2/2+F(M)*radius**3/6
 assert lower>0 and zupper>lower
 # Full-cell *conditional* panel design for the original NF409 9e-17
 # L2 target; error-only bound via sqrt(cell length) <1.
 full_width_upper=F(knots[14]['high'])-F(knots[13]['low'])
 assert full_width_upper<F(1,2)
 r=F(1,10**7)
 error_l2_upper=F(M)*r**3/6 # uses sqrt(length)<1.
 assert error_l2_upper<F(9,10**17)
 panel_count=(full_width_upper/(2*r)).numerator//(full_width_upper/(2*r)).denominator+1
 assert panel_count>100000
 out={
 'pass':'NF423-exact-independent',
 'standing':'SOURCE-EXACT INDEPENDENT FOUR SHARED RESPONSE JETS PLUS ENTIRE ORIGINAL PHYSICAL OPEN CELL6 zTHIRD ENVELOPE AND ENLARGED TRUE z POSITIVE INTERVAL; NF404 OPEN',
 'original_nf407_source_sha256':ssha,'original_nf406_exact_seams_sha256':seamsha,
 'original_nf413_curvature_sha256':csha,
 'original_nf416_complete_z_anchor_sha256':zsha,
 'original_nf419_complete_zprime_anchor_sha256':jsha,
 'original_nf421_complete_zsecond_anchor_sha256':ksha,
 'original_nf421_previous_signed_interval_sha256':oldsha,
 'original_nf422_all_order_arch_transfer_sha256':tsha,
 'original_nf423_shared_four_jet_sha256':nsha,
 'original_nf423_entire_cell6_zthird_sha256':wsha,
 'original_all_242_plus_four_critical_native_dyadic_source_rebuilt':True,
 'original_four_shared_jets_analytic_tails_recomputed_from_exact_source':True,
 'original_z0_z1_z2_overlap_independently_verified':True,
 'original_zthird_anchor_strictly_negative':True,
 'original_full_cell6_knot_seam_branches_checked':True,
 'original_4096bit_A_native_interval_exact_fraction_reread':True,
 'original_true_Rsecond_wide_cell_exact_rational_replay':True,
 'original_full_cell6_third_derivative_uniform_upper':M,
 'original_signed_positive_interval_radius_exact':str(radius),
 'original_signed_positive_interval_exact':[str(X-radius),str(X+radius)],
 'original_full_z_on_signed_interval_lower_exact':str(lower),
 'original_full_z_on_signed_interval_upper_exact':str(zupper),
 'original_positive_radius_strictly_improved_from_NF421':True,
 'original_full_cell6_conditional_Taylor_panel_halfwidth':'1/10000000',
 'original_full_cell6_conditional_panel_count_upper':panel_count,
 'original_full_cell6_conditional_Taylor_only_L2_bound_exact':str(error_l2_upper),
 'original_full_cell6_center_jets_certified':False,
 'original_full_cell6_actual_z_cellwise_enclosure_certified':False,
 'NF410_signed_p_z_z2_full_integrated':False,
 'NF404_complete_original_centered_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF423 independent true original zthird(0.9)<0; full cell6 |zthird|<',M,flush=True)
 print('NF423 certified new original z>0 radius',radius,'positive interval',out['original_signed_positive_interval_exact'],flush=True)
 print('NF423 conditional full cell6 source-jet count',panel_count,'NOT computed',flush=True)
 print('NF423 true original NF404 centered scalar OPEN',flush=True)
if __name__=='__main__':main()
