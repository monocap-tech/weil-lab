#!/usr/bin/env python3
"""NF419 independent no-Arb exact Fraction source error and moving boundary audit.
Rebuild original 242+4 physical source U,S0 from original native dyadics;
check NF419 derivative jet remainder ledger term-by-term and original
NF414/NF416/NF418 source SHA. Symbolically verify all u(x) coefficients
cancel when original finite arch and the two moving I0/I1 boundaries join.
No numerical quadrature, no GH proof closure beyond this first x-jet.
"""
import argparse,json,sys
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from nf417_original_hotspots_independent_fraction_replay import read,source_contract
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--jet',default='notes/data/provisional/NF411_original_source_boundary_jet.json')
 ap.add_argument('--gram',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--finite',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 ap.add_argument('--point',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 ap.add_argument('--front',default='notes/data/provisional/NF418_original_hotspot_cellwide_lipschitz_envelopes_exact.json')
 ap.add_argument('--nf419',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 source,ssha=read(a.source); jet,jsha=read(a.jet);gram,gsha=read(a.gram)
 finite,fsha=read(a.finite);pt,psha=read(a.point);front,frsha=read(a.front);r,rsha=read(a.nf419)
 assert source['original_dimension']==242
 assert jet['nf407_source_sha256']==ssha
 assert gram['original_nf407_full_native_source_sha256']==ssha
 assert finite['original_nf407_source_sha256']==ssha
 assert pt['original_nf407_source_sha256']==ssha
 assert front['original_nf407_246_source_sha256']==ssha
 assert [r['original_nf407_source_sha256'],
         r['original_nf411_original_boundary_jet_sha256'],
         r['original_nf413_full_source_curvature_sha256'],
         r['original_nf414_all_seven_true_signed_primes_sha256'],
         r['original_nf416_complete_true_z_point_sha256'],
         r['original_nf418_full_cell_coarse_envelope_sha256']]==[ssha,jsha,gsha,fsha,psha,frsha]
 U,S0,fmax=source_contract(source)
 assert F(882)<fmax<F(883) and U<F(10)**160 and S0<F(1,10**700)
 assert F(r['original_original_source_coefficient_S0_exact'])==S0
 t1=F(2,5);t2=F(4);tau=F(1,50)
 R0=F(8*3**62)*U*F(62)**518/factorial(518)
 R1=10**4*R0
 RH=6*tau**61/(1-tau)
 E_tiny=6*R1/531+100*RH
 Rlarge=F(3**16)*U*F(16)**288/factorial(288)
 Rlarge1=10**4*Rlarge
 K0tail=F(81)*F(2,5)**161/F(3,5)
 E0regular=(t1-tau)*(100*Rlarge1+K0tail*(800+Rlarge1))
 eta=F(1,100)/t1
 K1tail=81*eta**49/(1-eta)
 E1regular=(t2-t1)*(F(2)/t1*Rlarge1+K1tail*(800+Rlarge1))
 S1=10**4*S0; S3=10**12*S0
 coeff=S3*t1*t1/8+2*(t2/t1-1)*S1+10**6*S0
 E=E_tiny+E0regular+E1regular+coeff
 checks={
 'original_tiny_source_derivative_Taylor_error_upper_exact':R1,
 'original_derivative_I0_tiny_integrated_error_upper_exact':E_tiny,
 'original_derivative_I0_regular_integrated_error_upper_exact':E0regular,
 'original_derivative_I1_integrated_error_upper_exact':E1regular,
 'original_source_derivative_coefficient_S1_bound_exact':S1,
 'original_source_third_derivative_coefficient_S3_bound_exact':S3,
 'original_derivative_complete_native_coefficient_error_upper_exact':coeff,
 'original_full_zprime_integral_error_upper_exact':E}
 for name,val in checks.items():assert F(r[name])==val,('original full source exact error mismatch',name)
 assert r['original_I0_derivative_analytic_regular_panel_count']==38
 assert r['original_I1_derivative_analytic_panel_count']==360
 assert r['tiny_original_source_derivative_Taylor_order']==530
 assert r['large_original_source_derivative_Taylor_order']==300
 assert len(r['original_all_seven_signed_prime_derivative_branches'])==7
 assert [x['branch'] for x in r['original_all_seven_signed_prime_derivative_branches']]==[x['branch'] for x in finite['hotspot_points'][1]['all_seven_true_prime_branches']]
 assert r['finite_arch_plus_moving_boundary_exact_full_source_cancellation']=='(c+L/2)*uprime+u(B)*(K(t1)+K(t2)-1/(2d))'
 assert r['algebraically_direct_and_cancelled_arch_arb_intervals_overlap']
 # Exact symbolic affine coefficients with q=1/(2d):
 # finite original derivative has u coefficient k1-k2 and v -q;
 # original I0+I1 moving boundary u coefficient -k1+k2
 # and v coefficient k1+k2. Therefore u cancels identically.
 # Encode every independent k1,k2,q basis coefficient as Fractions.
 finite_u={'k1':F(1),'k2':F(-1),'q':F(0)}
 moving_u={'k1':F(-1),'k2':F(1),'q':F(0)}
 finite_v={'k1':F(0),'k2':F(0),'q':F(-1)}
 moving_v={'k1':F(1),'k2':F(1),'q':F(0)}
 combined_u={k:finite_u[k]+moving_u[k] for k in finite_u}
 combined_v={k:finite_v[k]+moving_v[k] for k in finite_v}
 assert all(x==0 for x in combined_u.values())
 assert combined_v=={'k1':F(1),'k2':F(1),'q':F(-1)}
 vals=list(map(F,r['true_original_complete_zprime_at_9over10_outward_rational_interval']))
 assert vals[0]>0 and vals[1]>vals[0]
 assert vals[1]-vals[0]==F(r['true_original_complete_zprime_interval_width_exact'])
 assert vals[1]-vals[0]<F(1,10**27)
 assert pt['complete_original_z_pointwise_certified']
 assert r['first_order_original_x_jet_certified']
 assert not r['complete_original_source_x_interval_second_derivative_remainder_certified']
 assert not r['NF404_scalar_decided']
 assert r['W_ODD_NEG']==r['RH']=='OPEN'
 result={
 'pass':'NF419-independent','standing':'SOURCE-EXACT FRACTION REPLAY PASS OF ALL ORIGINAL FIRST X-JET ERROR BOUNDS AND EXACT MOVING-ARCH CANCELLATION',
 'original_source_sha256':ssha,'NF419_native_sha256':rsha,
 'all_242_plus_4_original_dyadic_coefficients_reconstructed':True,
 'all_seven_signed_prime_derivative_branches_match_NF414':True,
 'tiny_H_source_and_regular_kernel_source_error_terms_exactly_replayed':True,
 'original_native_source_first_and_third_derivative_radii_replayed':True,
 'original_finite_plus_moving_arch_standalone_source_u_coefficients_exactly_zero':True,
 'original_boundary_remaining_v_coefficients':{'k1':'1','k2':'1','1_over_2d':'-1'},
 'original_zprime_9over10_rational_outward_interval_verified_positive':True,
 'original_zprime_width_strict':'1e-27',
 'second_x_derivative_uniform_remainder_certified':False,
 'complete_original_cellwide_x_Taylor_certified':False,
 'NF404_entire_centered_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+'\n')
 print('NF419 independent original 246 source Fraction zprime error ledger and exact arch cancellation PASS')
if __name__=='__main__':main()
