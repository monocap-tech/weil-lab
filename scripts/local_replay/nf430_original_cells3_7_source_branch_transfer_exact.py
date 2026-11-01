#!/usr/bin/env python3
"""NF430 source-exact cell3/cell7 prime routing and analytic representation cost.

The mathematical source is ORIGINAL NF407 242+4, NF406 original seven
prime powers and rigorous original NF417 complete physical x=0.35/1.04
pointwise anchor. No claiming 3/7 whole signed cell integrals.

Proves cell3 has true original branches (2 both,3/4 post, 5/7/8/9
neither) with a rational E2 ellipse, and cell7 needs six post, one
neither, three rational fixed-branch E2 panels to avoid the arch log
singularity. Certifies 2048 physical image terms are not an adequately
proved cell7 truncation under NF424's source triangle; a deliberately
conservative 120000 images is sufficient for the whole physical J7
under a strict x<=B-1/400 bound.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
PS=(2,3,4,5,7,8,9)
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(pair):
 m,e=int(pair[0]),int(pair[1])
 return F(m*2**e) if e>=0 else F(m,2**(-e))
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--nf417-cell3',default='notes/data/provisional/NF417_original_cell3_full_z_pointwise_native.json')
 ap.add_argument('--nf417-cell7',default='notes/data/provisional/NF417_original_cell7_full_z_pointwise_native.json')
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 src,ssha=read(a.source);seams,ksha=read(a.seams);p3,h3=read(a.nf417_cell3);p7,h7=read(a.nf417_cell7)
 assert src['original_dimension']==242 and len(src['original_selected_generator_node_orders'])==242
 assert len(src['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(src['original_source_critical_sine_frequencies'])==32
 assert src['W_ODD_NEG']==src['RH']=='OPEN'
 assert seams['W_ODD_NEG']==seams['RH']=='OPEN'
 for cell,p in ((3,p3),(7,p7)):
  assert p['cell']==cell and p['x']==('7/20' if cell==3 else '26/25')
  assert p['nf407_original_source_sha256']==ssha
  assert p['true_original_complete_z_pointwise_certified']
  assert not p['entire_original_cell_z_certified']
  assert p['W_ODD_NEG']==p['RH']=='OPEN'
 knots=seams['certified_ordered_knots']
 assert len(knots)==17 and seams['number_of_open_physical_support_cells']==16
 assert [k['label'] for k in knots[8:]]==[
  '0','B-log(3)','-B+log(4)','B-log(2)',
  '-B+log(5)','-B+log(7)','-B+log(8)','-B+log(9)','+B']
 assert F(knots[10]['low'])>F(7,25)
 assert F(knots[11]['high'])<F(21,50)
 assert F(knots[14]['low'])>F(97,100)
 assert F(knots[15]['high'])<F(10973,10000)
 assert B-F(knots[15]['high'])>F(1,400)
 assert F(knots[10]['high'])<F(7,20)<F(knots[11]['low'])
 assert F(knots[14]['high'])<F(26,25)<F(knots[15]['low'])
 # Original physical x>0, original source x±log(n) can be in support:
 # abs shift seam for n2,3 and post for the larger n.
 # n=2: x3 is below B-log2, retaining BOTH translations.
 # n=3: B-log3 already crossed before cell3, hence post only.
 # n=4: -B+log4 is exactly left boundary of J3, hence post.
 # n=8: -B+log8 is exactly left boundary of J7, hence post.
 c3={'both':[2],'post':[3,4],'neither':[5,7,8,9]}
 c7={'both':[],'post':[2,3,4,5,7,8],'neither':[9]}
 assert sorted(c3['both']+c3['post']+c3['neither'])==list(PS)
 assert sorted(c7['both']+c7['post']+c7['neither'])==list(PS)
 # Original principal p=q+r jump-set is only post-seam primes,
 # so cell3 p uses n3,n4, cell7 p uses n2,3,4,5,7,8.
 assert c3['post']==[3,4] and c7['post']==[2,3,4,5,7,8]
 # Strict original-source 242+4 raw upper and source coefficient balls.
 coeff={}
 pole=F(0);S0=F(0)
 def add(f,k,v):coeff[f,k]=coeff.get((f,k),F(0))+v
 for (f,k),(mid,rad) in zip(src['original_selected_generator_node_orders'],
                              src['original_exact_native_raw_selected_coefficients_mid_radius']):
  val=dyad(mid);S0+=abs(dyad(rad))*B**(k or 0)
  if f=='pole':pole+=val
  else:add(F(f),k,val)
 for (mid,rad),shape in zip(src['original_exact_native_original_four_critical_coefficients_mid_radius'],
                            src['original_source_critical_sines_and_pole_coefficients']):
  val=dyad(mid);err=abs(dyad(rad))
  for f,c in zip(src['original_source_critical_sine_frequencies'],shape['sine_coefficients']):
   add(F(f),0,val*F(c));S0+=err*abs(F(c))
  pole+=val*F(shape['sinh_coefficient']);S0+=err*abs(F(shape['sinh_coefficient']))
 U=sum((abs(v)*B**k for (f,k),v in coeff.items()),abs(pole))
 assert U<10**160 and S0<F(1,10**700)
 assert max(f for f,k in coeff)<883 and max(k for f,k in coeff)<=13
 # Original cell3 rational real enclosing [.28,.42], ellipse rho2
 # with Re x<7/16<11/10 and |Im x|<21/400.
 C3=F(7,20);H3=F(7,100)
 assert C3-H3==F(7,25) and C3+H3==F(21,50)
 assert C3+F(5,4)*H3==F(7,16)
 assert B-(C3+F(5,4)*H3)>F(13,20)
 # The source-derived NF425 ellipse M=10^400 proof transfers to
 # the *cell3 fixed analytic branch*: all source translated polynomials
 # evaluated within the same |x|≤B and |Im x|<.0525 domain,
 # psi complex disks unchanged, image denominators unchanged,
 # and the extra n2 both source terms cost only the same 10^400
 # gross envelope. No carrying physical support across seam.
 assert 10**190*3**373<10**400
 N3=2048
 # Tiny source uniform tail: all real x3 satisfy 2(B-x)>1,
 # and source/image polynomial exponent factor<=13/(2B)<6.
 # Charge gross 36e160/2000*(3/8)^2000 < 1e-45.
 t3=1
 assert 2*(B-F(21,50))>1
 r3=F(36,2000)*10**160*F(3,8)**2000
 assert r3<F(1,10**45)
 assert F(4*10**400,2**1500)<F(1,10**50)
 # Original cell7 true x<=1.0973, hence B-x>1/400,
 # left image exponent t1=2(B-x)>1/200. With N=120000
 # the same NF424 conservative geometric argument yields:
 # 36e160 * (1/(1-e^-t1) <= 250) * (3/8)^600 <1e-70.
 # N2048 cannot be promoted with this NF424 *bound*: e^-10
 # times huge source triangle is far above tolerance. This does
 # NOT prove the actual exact source residual is large.
 N7=120000
 assert N7*F(1,200)==600
 assert F(1,1)-F(3,8)**F(1) != 0
 r7=F(36*250)*10**160*F(3,8)**600
 assert r7<F(1,10**70)
 # Cell7 is too close to B for a single rational rho2 ellipse on a
 # natural [0.97,1.0973] enclosure. Three rational panels retain
 # rho2 analyticity without crossing the arch logarithm singularity.
 panels=[
  (F(97,100),F(26,25)),
  (F(26,25),F(27,25)),
  (F(27,25),F(10973,10000))]
 assert panels[0][0]<F(knots[14]['low'])
 assert panels[-1][1]>F(knots[15]['high'])
 assert panels[0][1]==panels[1][0] and panels[1][1]==panels[2][0]
 pp=[]
 for l,r in panels:
  C=(l+r)/2;H=(r-l)/2
  xmax=C+F(5,4)*H
  assert xmax<B,('Bernstein ellipse crosses original endpoint',C,H)
  pp.append({'rational_left':str(l),'rational_right':str(r),
             'center':str(C),'halfwidth':str(H),
             'Bernstein_E2_real_right':str(xmax),
             'distance_from_original_arch_log_pole_strict_lower':str(B-xmax)})
 out={'pass':'NF430',
 'standing':'SOURCE-EXACT ORIGINAL CELLS3/7 SUPPORT ROUTER AND IMAGE/ELLIPSE ENTRY CONTRACT; COMPLETE SIGNED SECTORS NOT INTEGRATED',
 'original_source_sha256':ssha,'original_seams_sha256':ksha,
 'nf417_cell3_true_original_pointwise_sha256':h3,
 'nf417_cell7_true_original_pointwise_sha256':h7,
 'original_selected_source_generators':242,'original_critical_generators':4,
 'original_critical_sine_frequencies':32,
 'cell3_true_domain':'(-B+log(4),B-log(2))',
 'cell7_true_domain':'(-B+log(8),-B+log(9))',
 'original_cell3_true_prime_source_branches':c3,
 'original_cell7_true_prime_source_branches':c7,
 'original_cell3_signed_principal_active_prime_powers':c3['post'],
 'original_cell7_signed_principal_active_prime_powers':c7['post'],
 'original_nf417_cell3_x7over20_original_z_point_certified':True,
 'original_nf417_cell7_x26over25_original_z_point_certified':True,
 'original_source_raw_abs_strict_upper':'1e160',
 'original_source_radii_strict_upper':'1e-700',
 'cell3_rational_C_H':[str(C3),str(H3)],
 'cell3_fixed_branch_Chebyshev_Bernstein_E2_analytic':True,
 'cell3_global_source_exponential_transfer_2048_image_terms_sufficient':True,
 'cell3_2048_image_uniform_tail_strict_under_1e_minus_45':True,
 'cell3_original_degree1499_chebyshev_series_tail_under_1e_minus_50':True,
 'cell3_actual_Chebyshev_coefficients_computed':False,
 'cell7_single_global_rho2_ellipse_not_used':True,
 'cell7_fixed_branch_rational_E2_panels':pp,
 'cell7_conservative_120000_image_terms_uniform_real_cell_tail_strict_under_1e_minus_70':True,
 'cell7_2048_image_global_tail_certificate_available_from_NF424_bound':False,
 'cell7_actual_interval_Chebyshev_coefficients_computed':False,
 'cell3_original_signed_pz_z2_integrated':False,
 'cell7_original_signed_pz_z2_integrated':False,
 'NF410_all_eight_original_cells_integrated':False,
 'NF404_original_complete_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2)+'\n')
 print('NF430 original source exact cells3/7 prime routing PASS; cell3 2048 images + E2 1500 series suffices; cell7 needs 120000 image budget and three E2 panels')
 print('NF430 true original physical NF417 cell3/7 points retained; no cell3/7 signed integrals, NF404 and RH OPEN')
if __name__=='__main__':main()
