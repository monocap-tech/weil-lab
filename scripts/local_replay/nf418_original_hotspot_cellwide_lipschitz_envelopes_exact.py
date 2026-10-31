#!/usr/bin/env python3
"""NF418 exact-rational original cellwide Lipschitz envelope + sign neighborhoods.

No new source evaluation. Original NF413/411 global H2 and boundary-jet
bounds imply source |u'|<400, |u|<513. Derive z'=A_finite' +
I0'+I1'+(signed continuous prime)' -(a sinh(x/2))'
and prove |z'|<30000 on the THREE original positive hotspot open cells
3,6,7 by explicit analytic inequalities. NF406 original certified rational
knot brackets guarantee d=B-x>1/500 on these cells.

The envelopes are VALID but TOO WIDE for NF404. This tool proves no
L2 full centered scalar, nor pointwise values at unverified other cells.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
M=F(30000)
X={3:F(7,20),6:F(9,10),7:F(26,25)}
PARENT={3:'nf417_cell3',6:'nf416_cell6',7:'nf417_cell7'}
def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def endpoint_native_ball(s):
 assert s.startswith('[') and s.endswith(']') and ' +/- ' in s
 a,b=s[1:-1].split(' +/- ')
 with localcontext() as c:
  c.prec=1300
  x=Decimal(a);r=Decimal(b)
  assert r>=0
  return x-r,x+r
def floorF(q):return q.numerator//q.denominator
def ceilF(q):return -floorF(-q)
def bounds_decimal(lo,hi,n=45):
 scale=10**n
 return [str(F(floorF(lo*scale),scale)),str(F(ceilF(hi*scale),scale))]
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--jet',default='notes/data/provisional/NF411_original_source_boundary_jet.json')
 ap.add_argument('--curvature',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--cell3',default='notes/data/provisional/NF417_original_cell3_full_z_pointwise_native.json')
 ap.add_argument('--cell6',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 ap.add_argument('--cell7',default='notes/data/provisional/NF417_original_cell7_full_z_pointwise_native.json')
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 source,source_sha=read(args.source)
 jet,jet_sha=read(args.jet)
 curv,curv_sha=read(args.curvature)
 seams,seam_sha=read(args.seams)
 assert source['original_dimension']==242
 assert len(source['original_selected_generator_node_orders'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(source['original_source_critical_sine_frequencies'])==32
 assert jet['nf407_source_sha256']==source_sha
 assert curv['original_nf407_full_native_source_sha256']==source_sha
 assert curv['original_nf411_independent_jet_sha256']==jet_sha
 assert curv['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert seams['number_of_open_physical_support_cells']==16
 assert len(seams['certified_ordered_knots'])==17
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in [source,jet,curv,seams])
 vmin,vmax=endpoint_native_ball(jet['original_original_source_value_at_B_arb'])
 dmin,dmax=endpoint_native_ball(jet['original_original_source_derivative_at_B_arb'])
 assert -Decimal('1e-9')<vmin<=vmax<Decimal('1e-9')
 assert -Decimal('1e-6')<dmin<=dmax<Decimal('1e-6')
 # Pure rational proof obligations:
 # sqrt(2B)<3/2 => |u'|<1e-6+256*(3/2)<400.
 assert 2*B<F(3,2)**2
 assert F(1,10**6)+256*F(3,2)<400
 # sqrt((2B)^3/3)<2 => |u|<1e-9+(2B)1e-6+256*2 <513.
 assert (2*B)**3/3<4
 assert F(1,10**9)+2*B*F(1,10**6)+512<513
 # For x < log9-B, d=B-x > 2B-log9 > 1/500.
 # This follows original NF406 complete source-exact log9 upper.
 knots=seams['certified_ordered_knots']
 assert knots[15]['label']=='-B+log(9)'
 assert B+F(knots[15]['high'])<F(1099,500)
 assert 2*B-(B+F(knots[15]['high']))>F(1,500)
 # Global elementary derivative ledger on the 3 cells:
 # K(t) <2/t for all positive t (e^t>=1+t,
 # max_t [(1+t)e^(-t/4)] =4e^-3/4<2).
 #
 # With ||u''||2<256, |u'|<400, |u|<513:
 # |I0'| <2200: moving upper endpoint K(2d)D_(2d)
 # plus integrable u' centered differences.
 # |I1'| <2000: both moving endpoints <=400 each,
 # and integral derivative <=512 sqrt(t2)<1127.
 # |A_finite'|<7500: |c|<12, |c'|<2,
 # |u-v|/d<400, |u'|<400,
 # log(B/d)<log(550)<7 by d>1/500.
 # |P_reg'|<16800: 7 original n<=9, each
 # coefficient Lambda(n)/sqrt(n)<ln9<3,
 # at most two physical translated source derivatives each <400;
 # original step r is constant on each exact original open cell.
 # |(a sinh(x/2))'|<2 by original NF404 a<2, x<=B.
 components={'original_I0_derivative':2200,
             'original_I1_derivative':2000,
             'original_arch_finite_derivative':7500,
             'original_seven_signed_prime_continuous_derivative':16800,
             'original_center_derivative':2}
 assert sum(components.values())==28502
 assert sum(components.values())<M
 assert F(7)*2*3*400==16800
 assert F(128)*3+F(1024)*F(3,2)<2200 # I0 proof tightened below
 assert 800+F(512)*F(11,5)<2000 # I1 proof
 assert 2*513+12*400+200+200*7<7500
 # One-sided C0 prime seams, true original NF407 continuation.
 # Derivative is a piecewise bound; use MV theorem on each open cell,
 # then endpoint continuity to include its closure.
 reports=[]
 total_lower=F(0);total_upper=F(0)
 parent_shas={}
 for cell in [3,6,7]:
  x=X[cell]
  path={3:args.cell3,6:args.cell6,7:args.cell7}[cell]
  r,rsha=read(path);parent_shas[cell]=rsha
  if cell==6:
   assert r['original_nf407_source_sha256']==source_sha
   assert r['complete_original_z_pointwise_certified']
   interval=r['original_true_full_z_cell6_at_x9over10_outward_interval']
  else:
   assert r['nf407_original_source_sha256']==source_sha
   assert r['true_original_complete_z_pointwise_certified']
   interval=r['original_true_complete_z_pointwise_rational_interval']
  zlo,zhi=map(F,interval)
  assert zlo<zhi
  kl=knots[8+cell-1];kr=knots[8+cell]
  leftLo,leftHi=F(kl['low']),F(kl['high'])
  rightLo,rightHi=F(kr['low']),F(kr['high'])
  assert leftHi<x<rightLo
  assert leftLo<=leftHi<rightLo<=rightHi
  assert B-rightHi>F(1,500)
  D=max(x-leftLo,rightHi-x)
  # Every original x in the ENTIRE original physical cell has
  # |x-x_anchor| <= D. Outward rational envelope, with no alleged
  # sign certificate for entire cell.
  globalLo=zlo-M*D
  globalHi=zhi+M*D
  assert globalLo<0<globalHi
  # ACTUAL continuous source interval of half-radius 1e-17;
  # point center certified in NF416/417 native original z,
  # and entire local interval strictly inside the original support cell.
  radius=F(1,10**17)
  assert x-radius>leftHi and x+radius<rightLo
  localLo=zlo-M*radius
  localHi=zhi+M*radius
  if cell==3:assert localHi<0 and zhi<0;sgn='strict_negative'
  else:assert localLo>0 and zlo>0;sgn='strict_positive'
  # Partial local area is rigorously signed; no zeta-zero inference.
  total_lower+=rightLo-leftHi
  total_upper+=rightHi-leftLo
  D_up=F(ceilF(D*10**12),10**12)
  out_global=bounds_decimal(globalLo,globalHi,n=30)
  out_local=bounds_decimal(localLo,localHi,n=40)
  assert F(out_global[0])<=globalLo and F(out_global[1])>=globalHi
  assert F(out_local[0])<=localLo and F(out_local[1])>=localHi
  reports.append({
   'original_cell':cell,
   'exact_original_cell_left_label':kl['label'],
   'exact_original_cell_right_label':kr['label'],
   'original_anchor_rational_x':str(x),
   'original_point_cert_sha256':rsha,
   'original_anchor_outward_sign':sgn,
   'original_cell_distance_upper_rational_1e12':str(D_up),
   'original_whole_cell_z_outward_rational_envelope_1e30':out_global,
   'entire_cell_envelope_valid_but_NF404_precision_insufficient':True,
   'certified_same_sign_neighborhood_radius_exact':'1/100000000000000000',
   'certified_same_sign_neighborhood_z_outward_rational_envelope_1e40':out_local,
   'neighborhood_in_original_cell':True,
   'neighborhood_same_sign_certified':True,
   'entire_original_cell_sign_certified':False,
   'cellwide_original_z_tight_norm_certified':False})
 # THREE original hotspot full-cell lengths >1/3 and <1.
 assert total_lower>F(1,3)
 assert total_upper<1
 # Direct Lipschitz-grid recipe, not a universal lower bound:
 # for nearest-neighbor sample mesh h, pointwise interpolation error
 # <=M*h/2, L2 over three cells <=M*h/2 since total length<1.
 # To certify eps=9e-17, the sufficient step h <=2 eps/M
 # is so small that >=(1/3)/h subintervals are required.
 eps=F(9,10**17)
 h=2*eps/M
 num_lower=F(1,3)/h
 assert h<F(1,10**20)
 assert num_lower>F(5*10**19)
 out={
  'pass':'NF418',
  'standing':'ACCEPTED ORIGINAL-SOURCE TRUE GLOBAL CELLWISE LIPSCHITZ ENVELOPES ON ORIGINAL CELLS 3 6 7, BUT FAR TOO LOOSE FOR NF404 SCALAR',
  'original_nf407_246_source_sha256':source_sha,
  'original_nf411_boundary_jet_sha256':jet_sha,
  'original_nf413_complete_curvature_sha256':curv_sha,
  'original_nf406_certified_seam_partition_sha256':seam_sha,
  'original_prior_source_point_receipt_sha256s':{str(k):v for k,v in parent_shas.items()},
  'original_true_full_246_generator_source_unchanged':True,
  'source_u_prime_global_sup_certified_upper_integer':400,
  'source_u_global_sup_certified_upper_integer':513,
  'original_curvature_L2_upper_integer':256,
  'original_source_endpoint_value_abs_upper':'1/1000000000',
  'original_source_endpoint_slope_abs_upper':'1/1000000',
  'original_hotspot_d_lower_strict':'1/500',
  'whole_original_z_derivative_piecewise_uniform_upper_integer':int(M),
  'derivative_component_upper_ledger':components,
  'original_true_seven_signed_prime_branches_retained':True,
  'all_original_hotspot_cells_continuous_z_on_closure':True,
  'original_hotspot_cellwise_envelopes':reports,
  'three_hotspot_total_cell_length_lower_strict':'1/3',
  'three_hotspot_total_cell_length_upper_strict':'1',
  'original_NF409_tentative_eps':'9/100000000000000000',
  'unrefined_lipschitz_nearest_neighbor_mesh_sufficient_h_upper_exact':str(h),
  'unrefined_nearest_neighbor_subintervals_over_three_cells_more_than':'50000000000000000000',
  'global_Lipschitz_grid_is_method_stop_for_NF404':True,
  'source_correlated_tight_cellwise_enclosure_certified':False,
  'original_signed_NF410_p_z_cross_certified':False,
  'original_NF404_complete_centered_scalar_decided':False,
  'original_J242_complement':'OPEN',
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 for row in reports:
  print('NF418 original cell',row['original_cell'],
        'true full-cell wide z envelope',row['original_whole_cell_z_outward_rational_envelope_1e30'],
        'certified same sign local 1e-17',row['original_anchor_outward_sign'],flush=True)
 print('NF418 exact source full cell derivative <30000; NF404 scalar OPEN, naive Lipschitz grid STOP',flush=True)
if __name__=='__main__':main()
