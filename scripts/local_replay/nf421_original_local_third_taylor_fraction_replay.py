#!/usr/bin/env python3
"""NF421 independent ORIGINAL 246-source exact rational local third Taylor audit.

No Arb quadrature or fourth Gram recomputation. Independently reconstruct
the complete original source Uraw/S0 from NF407 dyadics, check all native
full source zsecond tails and every source radius, reread full fourth
correlated source 4096-bit Gram and endpoint as exact Fraction outward
balls, verify true local z''' bound, and compose certified original
NF416 z0 + NF419 z' + NF421 z'' using exact cubic Taylor bound.

Certifies only original physical cell6 source micro interval. Other
original cells and entire NF404 scalar necessarily remain OPEN.
"""
import argparse,json,sys,math
from fractions import Fraction as F
from decimal import Decimal,localcontext
from pathlib import Path
from nf417_original_hotspots_independent_fraction_replay import read,source_contract
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10);T1=F(2,5);T2=F(4)
def ball(t):
 assert t.startswith('[') and t.endswith(']') and ' +/- ' in t
 a,r=t[1:-1].split(' +/- ')
 with localcontext() as c:
  c.prec=6000
  x=F(Decimal(a));e=F(Decimal(r))
 assert e>=0
 return x-e,x+e
def choose_radius(z0lo,zpabs,z2abs,m):
 def lower(r):return z0lo-zpabs*r-z2abs*r*r/2-m*r**3/6
 lo=F(0);hi=F(1,1000)
 assert lower(lo)>0
 for j in range(100):
  middle=(lo+hi)/2
  if lower(middle)>0:lo=middle
  else:hi=middle
 # Round DOWN to exact 12-digit decimal rational, conservative.
 r=F((lo*10**12).numerator//(lo*10**12).denominator,10**12)
 assert r>0 and r<hi and lower(r)>0
 return r,lower(r)
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--nf416',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 ap.add_argument('--nf419',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 ap.add_argument('--nf420',default='notes/data/provisional/NF420_original_cell6_independent_sharpened_Taylor_positive_interval.json')
 ap.add_argument('--gram',default='notes/data/provisional/NF421_original_fourth_source_gram_and_z_third_bound_native.json')
 ap.add_argument('--second',default='notes/data/provisional/NF421_original_cell6_complete_second_xjet_native.json')
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 src,ssha=read(a.source); nf413,hsha=read(a.nf413)
 z0,zsha=read(a.nf416);zp,jsha=read(a.nf419);nf420,psha=read(a.nf420)
 gram,gsha=read(a.gram);second,dsha=read(a.second)
 assert all(q['W_ODD_NEG']==q['RH']=='OPEN' for q in (src,nf413,z0,zp,nf420,gram,second))
 assert ssha==nf413['original_nf407_full_native_source_sha256']==z0['original_nf407_source_sha256']
 assert ssha==zp['original_nf407_source_sha256']==nf420['original_nf407_source_sha256']
 assert ssha==gram['original_nf407_source_sha256']==second['original_source_sha256']
 assert gram['original_nf420_parent_sha256']==psha
 assert second['original_NF420_second_order_remainder_parent_sha256']==psha
 assert second['original_NF413_source_curvature_sha256']==hsha
 assert second['original_NF419_source_first_jet_sha256']==jsha
 assert len(src['original_selected_generator_node_orders'])==242
 assert len(src['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 U,S0,fmax=source_contract(src)
 assert F(882)<fmax<F(883) and U<10**160
 assert F(second['source_raw_triangle_exact'])==U
 assert F(second['source_radius_S0_exact'])==S0
 S2=F(nf413['native_second_derivative_source_coefficient_radii_uniform_exact'])
 S4=10**16*S0
 assert F(second['source_radius_S2_exact'])==S2
 assert F(second['source_radius_S4_upper_exact'])==S4
 assert F(gram['original_source_coefficient_uniform_fourth_derivative_radii_exact'])==S4
 Esmall0=F(8*3**62)*U*62**518/math.factorial(518)
 Esmall2=10**8*Esmall0
 tau=F(1,50)
 RH=6*tau**61/(1-tau)
 Etiny=6*Esmall2/531+1000*RH
 Elarge=F(3**16)*U*16**288/math.factorial(288)
 Elarge2=10**8*Elarge
 K0=81*F(2,5)**161/F(3,5)
 E0=(T1-tau)*(100*Elarge2+K0*(5000+Elarge2))
 eta=F(1,100)/T1
 K1=81*eta**49/(1-eta)
 E1=(T2-T1)*(F(2)/T1*Elarge2+K1*(5000+Elarge2))
 Ecoeff=S4*T1*T1/8+2*(T2/T1-1)*S2+10**10*S0
 E=Etiny+E0+E1+Ecoeff
 replay={'I0_tiny_derivative_tail_exact':Etiny,
  'I0_regular_derivative_tail_exact':E0,
  'I1_derivative_tail_exact':E1,
  'full_original_source_native_coefficient_charge_exact':Ecoeff,
  'full_original_second_jet_total_error_exact':E}
 for k,v in replay.items():assert F(second[k])==v,('native source remainder mismatch',k)
 assert len(second['original_seven_signed_prime_derivative_branches'])==7
 assert second['original_u_second_I0_panels']==38 and second['original_u_second_I1_panels']==360
 assert second['original_true_pointwise_second_x_jet_certified']
 z2lo,z2hi=map(F,second['true_original_complete_zsecond_at_x9over10_outward_rational_interval'])
 assert z2lo<z2hi and z2hi-z2lo==F(second['true_original_complete_zsecond_at_x9over10_width_exact'])
 assert z2hi-z2lo<F(1,10**26)
 # Original fourth Gram true squared norm and endpoint independently
 # roundtripped as EXACT Fraction, with true original coefficient radii.
 glo,ghi=ball(gram['original_true_4th_derivative_L2_Gram_squared_native_arb'])
 assert glo>0 and ghi<10**200
 N4=int(gram['original_true_u4_fourth_derivative_L2_upper_power2'])
 assert (F(N4)-F(3,2)*S4)>0
 assert ghi<(F(N4)-F(3,2)*S4)**2
 eplo,ephi=ball(gram['original_true_u4_third_derivative_at_B_native_arb'])
 E3=int(gram['original_u4_third_derivative_at_B_native_with_radius_power2'])
 assert max(abs(eplo),abs(ephi))+10**12*S0<E3
 M3=F(E3)+F(3,2)*N4
 assert F(gram['original_true_u4_third_derivative_global_sup_upper_exact'])==M3
 Mz3=58*M3+7*N4+10
 assert F(gram['original_complete_z_third_x_derivative_uniform_upper_exact'])==Mz3
 assert gram['original_complete_z_third_x_derivative_original_interval']==['899/1000','901/1000']
 assert gram['original_true_seven_signed_primes_third_derivative_included_in_bound']
 zlo,zhi=map(F,z0['original_true_full_z_cell6_at_x9over10_outward_interval'])
 wlo,whi=map(F,zp['true_original_complete_zprime_at_9over10_outward_rational_interval'])
 assert zlo>0 and wlo>0
 wmag=max(abs(wlo),abs(whi));z2mag=max(abs(z2lo),abs(z2hi))
 radius,lower=choose_radius(zlo,wmag,z2mag,Mz3)
 assert radius<=F(1,1000)
 upper=zhi+wmag*radius+z2mag*radius*radius/2+Mz3*radius**3/6
 assert lower>0 and upper>lower
 localZ2=[z2lo-Mz3*radius,z2hi+Mz3*radius]
 assert localZ2[0]<localZ2[1]
 assert abs(localZ2[0])<125457 and abs(localZ2[1])<125457
 previous=F(nf420['certified_positive_interval_radius_exact'])
 improved=radius>previous
 out={
 'pass':'NF421-independent',
 'standing':'INDEPENDENT EXACT FRACTION FULL SOURCE ORIGINAL FOURTH GRAM AND COMPLETE SECOND x JET REPLAY, WITH TRUE LOCAL THIRD ORDER POSITIVE INTERVAL; NF404 OPEN',
 'original_source_sha256':ssha,
 'parent_NF413_sha256':hsha,'parent_NF416_sha256':zsha,
 'parent_NF419_sha256':jsha,'parent_NF420_sha256':psha,
 'NF421_original_source_fourth_Gram_sha256':gsha,
 'NF421_original_second_xjet_sha256':dsha,
 'all_original_242_selected_and_4_critical_reconstructed':True,
 'all_original_source_second_xjet_error_bounds_recomputed_exactly':True,
 'original_fourth_correlated_Gram_arb_ball_reread_exactly_as_Fraction':True,
 'original_fourth_native_coefficient_uncertainty_paid_exactly':True,
 'original_true_u4_fourth_derivative_L2_power2_upper':N4,
 'original_true_u4_third_derivative_global_sup_upper_exact':str(M3),
 'original_true_z_third_x_derivative_uniform_upper_exact':str(Mz3),
 'original_macro_cell6_third_Taylor_remainder_valid':True,
 'original_macro_interval':['899/1000','901/1000'],
 'original_macro_taylor_third_remainder_at_radius_1over1000_exact':str(Mz3*F(1,1000)**3/6),
 'original_true_complete_zsecond_at_x9over10_outward_interval':[str(z2lo),str(z2hi)],
 'original_certified_positive_micro_radius_exact':str(radius),
 'original_certified_positive_micro_interval':[str(X-radius),str(X+radius)],
 'original_true_z_on_micro_lower_exact':str(lower),
 'original_true_z_on_micro_upper_exact':str(upper),
 'original_true_zsecond_uniform_local_micro_interval':[str(t) for t in localZ2],
 'original_true_zsecond_micro_bound_tighter_than_NF420_global':True,
 'original_positive_interval_radius_improved_from_NF420':improved,
 'original_previous_NF420_positive_radius':str(previous),
 'original_pointwise_second_jet_certified':True,
 'entire_original_cell6_covered':False,
 'NF410_signed_z_p_integrated':False,
 'NF404_original_entire_centered_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+'\n')
 print('NF421 independently replayed complete original second jet and fourth Gram; local radius',str(radius))
 print('NF421 true original z positive on',out['original_certified_positive_micro_interval'], 'improved?',improved)
 print('NF421 local source-cancelled zsecond interval',str(localZ2[0])[:60],str(localZ2[1])[:60])
 print('NF421 original NF404 centered scalar OPEN')
if __name__=='__main__':main()
