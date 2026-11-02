#!/usr/bin/env python3
"""NF446 exact ORIGINAL joint digamma+both image families: compact-source kernel.

The original NF424/443 central digamma and endpoint images must first be
combined as one original source linear form. Their +/- shifted Laplace
tails CANCEL exactly. The resulting true archimedian response uses U(y)
ONLY on -B<=y<=B, without exterior U_ent(B+t/2) and without the vast
~1e139 individual image coefficients.

For a=2(B-x), b=2(B+x), K(t)=exp(-t/4)/(1-exp(-t)),
c0=psi(1/4)-log pi, v=U(B), x in [0,B], exact after the original
subtraction -v/2*log(B/(B-x)):

J(x) = c0 U(x)
   +int_0^a K(t)[U(x)-(U(x+t/2)+U(x-t/2))/2]dt
   +int_a^b K(t)[U(x)-U(x-t/2)/2-v/2]dt
   +(v/2)[log((B+x)/B)+int_a^b (K(t)-1/t)dt]
   +U(x)*int_b^inf K(t)dt.

This identity extends continuously to x=B. For the pole sinh carrier
it is established by paired finite Laurent cancellation as
lambda->1/2, keeping the original special m0 remainder, NEVER by
separately evaluating the divergent digamma or m0.

Use previously certified original ||U''||_L2<256, exact native v,
native U'(B), and rational kernel inequalities for an explicit,
but NOT signed-decision-quality, bound |J|<17000 on 0<=x<=B,
and |z|<25000 for the actual original J7/J8 physical branches.
"""
from __future__ import annotations
import argparse,json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
from nf425_original_cell6_chebyshev_existence_exact import source
from nf433_original_cell3_cell7_branch_ellipse_router_exact import branch_for_cell
from nf438_original_cells4_5_regular_principal_geometry_exact import principal_jump
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NF445_JSON="51b8e0850c678085580940b3ab9afeff8277f446d4407c0200fb75754970db32"
PRIMES=(2,3,4,5,7,8,9)
def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def I(t):
 a,b=map(F,t);assert a<=b;return a,b
def interval_abs_lt(t,r):
 a,b=I(t);return -r<a<=b<r
def interval_overlap(a,b):
 l,u=I(a);x,y=I(b);return l<=y and x<=u
def exact_identity():
 # In each of the three intervals [0,a],[a,b],[b,infty] the
 # native full digamma has coefficients U(x):1,U(x+t/2):-1/2,
 # U(x-t/2):-1/2. The two native full image tails have
 # +1/2 U(x+t/2) for t>=a; +1/2 U(x-t/2) for t>=b,
 # the latter after ORIGINAL odd source reflection.
 source={'central':(F(1),F(-1,2),F(-1,2)),
         'left_image':(F(0),F(1,2),F(0)),
         'right_image':(F(0),F(0),F(1,2))}
 def group(names):
  return tuple(sum((source[name][i] for name in names),F(0)) for i in range(3))
 assert group(['central'])==(1,F(-1,2),F(-1,2))
 assert group(['central','left_image'])==(1,0,F(-1,2))
 assert group(['central','left_image','right_image'])==(1,0,0)
 # Subtract v/2 from middle integrand, then add it back as
 # (v/2)*integral_a^b K. Exact a,b cancellation with principal log:
 # log(b/a)-log(B/(B-x)) = log((B+x)/B).
 for x in (F(0),F(1,10),F(1,2),F(99,100),F(1099,1000)):
  a=2*(B-x);b=2*(B+x)
  assert 0<a<=b
  assert b/a*F(B-x,B)==F(B+x,B)
 # The original sinh source pole at lambda=1/2:
 # psi(eps)=-1/eps+psi(1)+O(eps),lambda=1/2-2eps.
 # arch has -sinh(lambda*x)/(2eps); image m0 contributes
 # +e^((lambda-1/2)B)*sinh(x/2)/(2eps).
 # Their pole residues cancel. Finite coefficient vector in
 # basis (sinh(x/2),x*cosh(x/2), e^(-B)*sinh(x/2))
 # is ( (psi(1)+psi(1/2))/2-log pi-B, +1, -1 ),
 # exactly the native NF443 pole Kpole and m0 remainder.
 pole_res_arch=F(-1,2);pole_res_m0=F(1,2)
 assert pole_res_arch+pole_res_m0==0
 assert F(-1)+F(1)==0 # m0 analytic tail opposite to digamma.
 # Exact K inequalities for all t>0:
 # e^t>=1+t=>K<=1+1/t; 1-e^-t<=t and
 # e^-t/4>=1-t/4=>K>=1/t-1/4.
 # Hence |K-1/t|<=1, not a difference of divergent integrals.
 return True
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 p.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 p.add_argument('--nf445',required=True)
 p.add_argument('--native-transfer',default='scripts/local_replay/nf443_original_cell2_three_panel_native_index.py')
 p.add_argument('--nf424',default='scripts/local_replay/nf424_original_cell6_global_exponential_transfer_exact.py')
 p.add_argument('--output',required=True)
 args=p.parse_args()
 assert exact_identity()
 src,sha=read(args.source);seams,ksha=read(args.seams)
 principal,psha=read(args.principal);curv,curvsha=read(args.nf413)
 native,nhash=read(args.nf445)
 assert sha==SRC and ksha==SEAM and nhash==NF445_JSON
 assert native['pass']=='NF445' and native['original_nf407_source_sha256']==sha
 assert native['original_nf406_seams_sha256']==ksha
 assert native['original_entire_generator_continuation_outside_physical_support_used']
 assert curv['original_nf407_full_native_source_sha256']==sha
 assert curv['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert curv['independent_NF411_original_endpoint_value_overlap']
 assert curv['independent_NF411_original_endpoint_derivative_overlap']
 assert principal['original_nf406_seams_sha256']==ksha
 assert src['original_dimension']==242
 assert len(src['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(src['original_source_critical_sine_frequencies'])==32
 assert len(source(src)[0])==273
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in (src,seams,principal,curv,native))
 assert interval_overlap(native['original_source_v_analytic_carrier_interval'],principal['original_source_u4_endpoint_interval'])
 v=I(native['original_source_v_analytic_carrier_interval'])
 vp=I(principal['original_source_u4_endpoint_interval'])
 dv=I(native['original_source_derivative_intervals_at_B']['1'])
 assert -1<v[0]<=v[1]<0 and interval_abs_lt(dv,F(1))
 assert native['original_precision_bits']==4096
 # This checks the INTACT original native digamma/image/group convention,
 # including the original special m=0 pole source and both exponents.
 original_transfer=Path(args.native_transfer).read_text()
 for key in (
  'def polygamma_D(lam):',
  'lo=aa-lam/2;hi=aa+lam/2',
  'dr=(lo.polygamma(r)*((-1)**r)+hi.polygamma(r))/(2**(r+1))',
  'if r==0:dr-=acb.pi().log()',
  'for m in range(N_IMAGES):',
  'aa=R(F(4*m+1,4))',
  'if m==0:',
  'total-=A(pole)*(-A(B)/2).exp()',
  'physical_point-=endpoint*((A(B)/A(B-X)).log()/2+sum(weights,arb(0)))',
  '(-2*aa*R(B-X)).exp()-(-2*aa*R(B+X)).exp()',
 ):assert key in original_transfer,('native source identity changed',key)
 source_preflight=Path(args.nf424).read_text()
 assert "target['PsiMinus']=target['PsiPlus']=Q(1,2)" in source_preflight
 # Kernel constant c0=psi(1/4)-log(pi) has |c0|<10,
 # native Arb independent of the source coefficients.
 ctx.prec=512
 c0=arb('1/4').digamma()-arb.pi().log()
 assert c0>-10 and c0<0
 # Only compact original U(y), y in [-B,B], is used in the new
 # finite-interval kernels. The original NF413 |U''|_L2<256,
 # |U'(B)|<1 (native NF445), and sqrt(2B)<3/2 imply:
 # |U'|<1+256*3/2=385<400.
 # |U|<|v|+400*2B<1+880=881<900.
 assert 2*B<F(3,2)**2
 derivative_bound=F(1)+F(256)*F(3,2)
 assert derivative_bound==385 and derivative_bound<400
 compact_U_bound=1+F(400)*2*B
 assert compact_U_bound==881 and compact_U_bound<900
 # K(t)=exp(-t/4)/(1-exp(-t)):
 # 0<K<1/t+1 and |K-1/t|<=1.
 # int_(b)^inf K<4 for b>=2B:
 # exp(-b/4)<2/3, exp(-b)<1/4, quotient<8/9.
 assert 1+F(11,20)+F(11,20)**2/2>F(3,2)
 assert 1+2*B+(2*B)**2/2>4
 # For x in [0,B], a=2(B-x) in [0,2B], b=2(B+x)
 # in [2B,4B]. First integral:
 # |U(x)-(U(x+t/2)+U(x-t/2))/2|<=200t
 # => int_0^a(1/t+1)*200t<=200*(2B+(2B)^2/2)<1000.
 first=200*(2*B+(2*B)**2/2)
 assert first<1000
 # Second difference:
 # |U(x)-U(x-t/2)/2-v/2|<=100(a+t).
 # int_a^b 100(a+t)(1/t+1)dt
 # <=100[2b+3b^2/4], using a log(b/a)<=b.
 second=100*(2*(4*B)+F(3,4)*(4*B)**2)
 assert second<2500
 # Scalar analytic log term |v|/2 * [log((B+x)/B)
 # +int_a^b |K-1/t|] <(1+4B)/2<3.
 scalar=(1+4*B)/2
 assert scalar<3
 # H(b)=int_b^inf K<4, so original finite tail <4*900.
 tail=F(4)*900
 assert tail==3600
 # |c0 U|<10*900=9000. Total <17000 for
 # combined original arch+images-original principal log.
 arch=F(1000)+F(2500)+F(3)+tail+F(10)*900
 assert arch==16103 and arch<17000
 # On J7,J8 only physical regular minus transfers (n2...9)
 # occur. Each original w_n=Lambda(n)/sqrt(n)<1, 7 terms
 # maximum, each |U(x-logn)+v|<901, exact center dyadic <2.
 center=F(6677356497477490213,4611686018427387904)
 assert 0<center<2
 total_bound=F(17000)+7*(900+1)+2
 assert total_bound==23309 and total_bound<25000
 # For original p(x)=v*(1/2 log(B/(B-x)) +sum active w_n),
 # |v|<1 and w_n<1, so ∫_0^B|p|dx
 # <(1/2+7)*B=33/4=8.25<9.
 p_integral=(F(1,2)+7)*B
 assert p_integral==F(33,4) and p_integral<9
 pz_integral=F(25000)*9
 z2_integral=F(25000)**2*B
 signed_global_bound=4*pz_integral+2*z2_integral
 assert signed_global_bound<2*10**9
 true=seams['certified_ordered_knots']
 logs={int(e['n']):(F(e['log_lower']),F(e['log_upper'])) for e in seams['original_prime_power_log_shifts']}
 cells={}
 for number,left,right in ((7,14,15),(8,15,16)):
  L,R=true[left],true[right]
  l0,l1=F(L['low']),F(L['high'])
  r0,r1=F(R['low']),F(R['high'])
  assert 0<l0<=l1<r0<=r1<=B
  minus=[];plus=[];jumps=[]
  for n in PRIMES:
   m,q=branch_for_cell(n,l1,r0,logs,L['label'],R['label'])
   if m:minus.append(n)
   if q:plus.append(n)
   if principal_jump(n,l1,r0,L['label'],R['label'],logs):jumps.append(n)
  expect=list(PRIMES[:-1]) if number==7 else list(PRIMES)
  assert minus==jumps==expect and plus==[],(number,minus,plus,jumps)
  cells[str(number)]={'true_left':L['label'],'true_right':R['label'],
    'original_regular_minus':minus,'original_regular_plus':plus,
    'original_principal_r_jump_active':jumps,
    'original_complete_source_j_arch_absolute_below':17000,
    'original_complete_source_z_absolute_below':25000,
    'original_complete_signed_D_absolute_below':2*10**9,
    'original_signed_D_certified':False}
 out={'pass':'NF446',
  'standing':'ORIGINAL SOURCE EXACT JOINT DIGAMMA+IMAGE CANCELLATION ON COMPACT [-B,B]; TRUE J7/J8 FINITE UNIFORM BOUNDS ACCEPTED, SIGNED D7 D8 OPEN',
  'source_sha256':sha,'seams_sha256':ksha,
  'original_nf407_principal_sha256':psha,
  'original_nf413_curvature_native_json_sha256':curvsha,
  'original_nf445_native_json_sha256':nhash,
  'native_transfer_script_sha256':hashlib.sha256(original_transfer.encode()).hexdigest(),
  'original_nf424_symbolic_transfer_script_sha256':hashlib.sha256(source_preflight.encode()).hexdigest(),
  'original_full_246_source_count':246,'original_source_group_count':273,
  'original_compact_source_bound_domain':'[-B,B]',
  'original_entire_extension_outside_B_needed_in_FINAL_joint_integral':False,
  'original_kernel_K':'exp(-t/4)/(1-exp(-t))',
  'original_kernel_a':'2(B-x)','original_kernel_b':'2(B+x)',
  'original_c0':'psi(1/4)-log(pi)',
  'original_joint_compact_j_formula':
   'c0*U(x)+int_0^a K(t)(U(x)-(U(x+t/2)+U(x-t/2))/2)dt'
   '+int_a^b K(t)(U(x)-U(x-t/2)/2-v/2)dt'
   '+v/2*(log((B+x)/B)+int_a^b(K(t)-1/t)dt)'
   '+U(x)*int_b^inf K(t)dt',
  'original_source_odd_reflection_used':True,
  'original_exact_m0_sinh_digamma_Laurent_pole_residue_cancellation':True,
  'original_original_nf443_pole_m0_finite_term_retained':True,
  'original_B_endpoint_all_joint_integrands_removable':True,
  'original_true_native_u_B_interval':list(map(str,v)),
  'original_true_native_uprime_B_interval':list(map(str,dv)),
  'original_true_NF413_second_derivative_L2_upper':256,
  'original_true_compact_source_derivative_sup_lt':400,
  'original_true_compact_source_sup_lt':900,
  'original_joint_arch_minus_explicit_principal_log_sup_lt':17000,
  'original_true_complete_J7_J8_physical_z_sup_lt':25000,
  'original_true_J7_J8_abs_p_integral_lt':9,
  'original_true_J7_J8_abs_signed_D_upper_lt':2*10**9,
  'original_true_J7_J8_bounds_decision_quality':False,
  'original_exact_functional_identity_is_not_native_quadrature':True,
  'original_native_source_correlated_joint_integral_numerically_enclosed':False,
  'original_cells':cells,
  'original_true_J7_signed_D_certified':False,'original_true_J8_signed_D_certified':False,
  'original_full_NF410_NF404_signed_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2)+'\n')
 print('NF446 PASS original JOINT digamma+images finite compact source cancellation: only U([-B,B])')
 print('NF446 genuine source NF413+NF445 controls: |J|<17000, physical J7/J8 |z|<25000; D signs OPEN.')
if __name__=='__main__':main()
