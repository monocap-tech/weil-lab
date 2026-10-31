#!/usr/bin/env python3
"""NF420 independent exact Fraction/Decimal sharpening of original x remainder.

No Arb, no quadrature, no source replacement. Re-read original 4096bit
outward analytic 246-source third derivative Gram certificate; exact rational
check u4''' L2<1334, hence u4'' sup<2002 and full z''<125457 on the genuine
NF406 original cell6 interval. Compose actual NF416 z(9/10) and NF419
z'(9/10) original rational intervals to certify z>0 on true
[9/10-1/40000000, 9/10+1/40000000].
Only that subinterval sign is promoted, NOT the entire cell or RH.
"""
import argparse,sys,json,hashlib
from fractions import Fraction as F
from decimal import Decimal,localcontext
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10)
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def parse_outward_arb(src):
 assert src[0]=='[' and src[-1]==']' and ' +/- ' in src
 a,b=src[1:-1].split(' +/- ')
 with localcontext() as ctx:
  ctx.prec=5000
  m=F(Decimal(a));r=F(Decimal(b))
 assert r>=0
 return [m-r,m+r]
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--curvature',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--point',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 ap.add_argument('--derivative',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 ap.add_argument('--gram',default='notes/data/provisional/NF420_original_full_third_curvature_and_cell6_Taylor_remainder_native.json')
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 source,sha=read(a.source);seams,seamsha=read(a.seams)
 curv,csha=read(a.curvature);point,psha=read(a.point)
 derivative,dsha=read(a.derivative);gram,gsha=read(a.gram)
 assert len(source['original_selected_generator_node_orders'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert gram['original_source_sha256']==point['original_nf407_source_sha256']==derivative['original_nf407_source_sha256']==sha
 assert gram['original_NF413_curvature_sha256']==csha
 assert gram['original_NF419_true_first_xjet_sha256']==dsha
 assert gram['original_NF406_original_seams_sha256']==seamsha
 assert point['complete_original_z_pointwise_certified']
 assert derivative['first_order_original_x_jet_certified']
 assert gram['second_x_derivative_uniform_remainder_certified_on_nontrivial_cell_subinterval']
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (source,seams,curv,point,derivative,gram))
 # Reconstruct source errors from independent NF417 module,
 # rather than blindly trust scalar S3 metadata.
 from nf417_original_hotspots_independent_fraction_replay import source_contract
 U,S0,fmax=source_contract(source)
 assert F(882)<fmax<F(883)
 S3=F(10**12)*S0
 assert S3==F(gram['source_third_derivative_coefficient_uniform_radii_exact'])
 assert S3<F(1,10**600)
 # 4096bit native source Gram interval, whose bound was already
 # SHA-custodied, is now interpreted by exact decimal-to-Fraction.
 E_lo,E_hi=parse_outward_arb(gram['full_original_u_third_derivative_Gram_L2_sq_Arb'])
 assert E_lo>0
 M3=1334
 assert E_hi<(F(M3)-F(1,1000))**2
 assert F(3,2)*S3<F(1,1000)
 assert E_hi>F(10**6)
 assert int(gram['original_full_u_third_derivative_L2_strict_integer_upper'])>=M3
 # Independent exact native endpoint u''(B) with original S2 radius.
 b_lo,b_hi=parse_outward_arb(gram['original_u_second_derivative_endpoint_Arb'])
 S2=F(curv['native_second_derivative_source_coefficient_radii_uniform_exact'])
 assert max(abs(b_lo),abs(b_hi))+S2<1
 assert 2*B<F(3,2)**2
 M2=1+F(3,2)*M3
 assert M2==2002
 # Same true SOURCE-CORRELATED z'' analytic identity and
 # original seven-prime physical branches as prior native source Gram.
 # Whole actual cell6 open interval [-0.001,+0.001] around x0,
 # finite arch |A|<16, prime second derivatives <42 M2,
 # two I0/I1 curvature pieces <7 M3, endpoint <1.
 MZ=58*M2+7*M3+3
 assert MZ==125457
 assert MZ<int(gram['true_original_z_second_derivative_uniform_bound_on_interval'])
 knots=seams['certified_ordered_knots']
 assert knots[13]['label']=='-B+log(7)' and knots[14]['label']=='-B+log(8)'
 assert F(knots[13]['high'])<F(899,1000) and F(knots[14]['low'])>F(901,1000)
 zlo,zhi=[F(z) for z in point['original_true_full_z_cell6_at_x9over10_outward_interval']]
 wlo,whi=[F(z) for z in derivative['true_original_complete_zprime_at_9over10_outward_rational_interval']]
 assert zlo>0 and wlo>0 and zhi>zlo and whi>wlo
 W=max(abs(wlo),abs(whi))
 coarseR=F(1,1000)
 coarseTaylor=MZ*coarseR**2/2
 assert coarseTaylor<F(1,10)
 # True nonzero signed subinterval, 2.5e-8 radius, uses exact
 # original point/first jet and all original NF420 source remainders.
 rho=F(1,40000000)
 assert rho<coarseR
 narrowR=MZ*rho*rho/2
 narrow_linear=W*rho
 narrowLo=zlo-narrow_linear-narrowR
 narrowHi=zhi+narrow_linear+narrowR
 assert narrowLo>F(0),('original true z sign unresolved',str(narrowLo)[:100])
 assert narrowHi>narrowLo
 assert rho>F(10**9)*F(1,10**17) # >1e9 * previous NF418 radius
 assert zlo-MZ*rho*rho/2-W*rho>0
 out={
  'pass':'NF420-sharpened-independent',
  'standing':'ACCEPTED ORIGINAL SOURCE-CORRELATED UNIFORM SECOND X TAYLOR REMAINDER, CERTIFIED TRUE z>0 ON CELL6 RADIUS 1/40000000; NF404 STILL OPEN',
  'original_nf407_source_sha256':sha,'original_nf406_seam_sha256':seamsha,
  'original_nf413_correlated_curvature_sha256':csha,
  'original_nf416_complete_zpoint_sha256':psha,
  'original_nf419_complete_xprime_sha256':dsha,
  'original_nf420_4096bit_full_source_third_gram_sha256':gsha,
  'original_full_source_242_plus_4_retained':True,
  'original_third_derivative_full_analytic_cross_correlations_from_parent':True,
  'original_arb_ball_bounds_reread_as_exact_Fraction':True,
  'original_Gram_squared_midpoint_true_positive_rechecked':True,
  'original_true_third_derivative_L2_integer_upper':M3,
  'original_true_second_derivative_global_sup_integer_upper':int(M2),
  'original_true_complete_z_second_x_derivative_uniform_bound':int(MZ),
  'original_full_support_cell6_macroscopic_Taylor_interval':['899/1000','901/1000'],
  'original_macroscopic_second_order_Taylor_remainder_at_radius_1over1000_exact':str(coarseTaylor),
  'original_certified_positive_interval_exact':[str(X-rho),str(X+rho)],
  'certified_positive_interval_radius_exact':str(rho),
  'original_full_z_positive_on_ENTIRE_micro_interval':True,
  'original_micro_interval_upper_Taylor_quadratic_error_exact':str(narrowR),
  'original_micro_interval_upper_Taylor_linear_error_exact':str(narrow_linear),
  'original_micro_interval_signed_z_lower_exact':str(narrowLo),
  'original_micro_interval_signed_z_upper_exact':str(narrowHi),
  'NF418_sign_island_radius_original':'1/100000000000000000',
  'NF420_sign_island_radius_expansion_factor_strict_lower':'1000000000',
  'original_complete_full_cell6_covered':False,
  'original_NF410_signed_principal_z_cross_certified':False,
  'original_NF404_complete_centered_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2)+'\n')
 print('NF420 independent exact certified ||u4 third||2 <',M3,'and ||u4 second||sup <',M2)
 print('NF420 original z second x derivative uniformly <',MZ,'on [899/1000,901/1000]')
 print('NF420 original source actual z STRICT POSITIVE on',out['original_certified_positive_interval_exact'])
 print('NF420 positive z min lower exact',str(narrowLo)[:180])
 print('NF420 full scalar NF404 and RH OPEN')
if __name__=='__main__':main()
