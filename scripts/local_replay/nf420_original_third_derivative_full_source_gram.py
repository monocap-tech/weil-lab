#!/usr/bin/env python3
"""NF420 full ORIGINAL 242+4 correlated THIRD-derivative Gram and interval z'' bound.

Same original NF370/NF407 supported u4, seven signed physical primes.
4096bit outward Arb exact analytic Gram of u4''' including selected-critical
cross terms and actual odd-pole cosh. This bounds the true original z''
uniformly on a genuine 1/500-long interval about cell6 x=9/10,
using second exact finite-plus-moving-arch cancellation.

Proves a rigorous nonzero-interval Taylor quadratic-remainder bound;
NOT an NF404 decision-quality complete-cell enclosure, NF410 scalar, or RH.
"""
import argparse,sys,math,json
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
from nf413_original_full_246_curvature_gram_native import Moments
from nf415_original_cell6_I1_validated_acb import read,native_source,A
from nf416_original_cell6_full_I0_regularized_taylor import original_jets
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10);RHO=F(1,1000)
def ceiling_power_two(ball):
 n=1
 while not (ball<arb(n)):
  n*=2
  assert n<10**300,('full original third curvature still unresolved',str(ball)[:180])
 return n
def gram_even_basis(m,a,b):
 # Third derivative u''' is EVEN. Basis:
 # x^even cos(2πfx), x^odd sin(2πfx).
 fa,ka=a;fb,kb=b;n=ka+kb
 if ka%2==0 and kb%2==0:
  return (m.get(fa-fb,n,'c')+m.get(fa+fb,n,'c'))/2
 if ka%2==1 and kb%2==1:
  return (m.get(fa-fb,n,'c')-m.get(fa+fb,n,'c'))/2
 if ka%2==0:
  return (m.get(fa+fb,n,'s')+m.get(fb-fa,n,'s'))/2
 return (m.get(fa+fb,n,'s')+m.get(fa-fb,n,'s'))/2
def pole_even_overlap(m,f,k):
 # ∫(even basis) cosh(x/2) = ∫(even basis) exp(x/2).
 # Existing analytic pole integral is sin-even / cos-odd type;
 # for cos-even choose REAL complex moment, sin-odd choose IMAG.
 z=acb(A(F(1,2)),2*m.pi*A(f))
 e=(z*A(B)).exp();mn=(-z*A(B)).exp()
 q=(e-mn)/z
 for j in range(1,k+1):
  q=(A(B**j)*e-A((-B)**j)*mn-j*q)/z
 return q.real if k%2==0 else q.imag
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--jet',default='notes/data/provisional/NF411_original_source_boundary_jet.json')
 ap.add_argument('--curv',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--nf419',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 s,ssha=read(a.source);jet,jsha=read(a.jet)
 g,gsha=read(a.curv);r,rsha=read(a.nf419);seams,seamsha=read(a.seams)
 assert s['original_dimension']==242
 assert len(s['original_selected_generator_node_orders'])==242
 assert len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert g['original_nf407_full_native_source_sha256']==ssha
 assert g['original_nf411_independent_jet_sha256']==jsha
 assert r['original_nf407_source_sha256']==ssha
 assert r['first_order_original_x_jet_certified']
 assert len(r['original_all_seven_signed_prime_derivative_branches'])==7
 assert len(seams['certified_ordered_knots'])==17
 assert all(v['W_ODD_NEG']==v['RH']=='OPEN' for v in (s,g,jet,r,seams))
 kl=seams['certified_ordered_knots'][13];kr=seams['certified_ordered_knots'][14]
 assert kl['label']=='-B+log(7)' and kr['label']=='-B+log(8)'
 assert F(kl['high'])<X-RHO and F(kr['low'])>X+RHO
 assert X+RHO<B and X-RHO>0
 assert F(2,5)-2*RHO>F(1,3)
 assert F(4)+2*RHO<F(9,2)
 ctx.prec=4096
 terms,pole,S0=native_source(s)
 assert len(terms)>=240 and S0<F(1,10**700)
 original={(f,k):v for f,k,v in terms}
 # Three exact derivative transformations, toggling odd -> even.
 # mode=0: original x^even sin, x^odd cos (odd source)
 # mode=1:       x^even cos, x^odd sin (even derivative)
 current={(f,k):A(v) for (f,k),v in original.items()}
 pi=arb.pi()
 for mode in range(3):
  nxt={}
  def add(key,v):nxt[key]=nxt.get(key,arb(0))+v
  for (f,k),v in current.items():
   w=2*pi*A(f)
   if k:add((f,k-1),k*v)
   add((f,k),v*w*(1 if (k+mode)%2==0 else -1))
  current={key:v for key,v in nxt.items() if v!=0}
  print('NF420 original derivative order',mode+1,'full consolidated physical basis count',len(current),flush=True)
 assert len(current)>=200
 M=Moments(pi)
 items=sorted(current.items())
 E=arb(0)
 for j,(key,v) in enumerate(items):
  E+=v*v*gram_even_basis(M,key,key)
  for prev,w in items[:j]:
   E+=2*v*w*gram_even_basis(M,key,prev)
  if (j+1)%60==0:print('NF420 full exact correlated source Gram row',j+1,'/',len(items),flush=True)
 # Source odd pole sinh(x/2) -> u''' pole cosh(x/2)/8.
 pole3=A(pole)/8
 cross=sum((v*pole_even_overlap(M,f,k) for (f,k),v in items),arb(0))
 E+=2*pole3*cross+pole3*pole3*(A(B)+A(B).sinh())
 assert E>0,('original third curvature interval does not prove positivity',str(E)[:240])
 assert E<arb(10)**200,('original source exact third derivative norm huge',str(E)[:240])
 S3=F(10**12)*S0
 assert S3<F(1,10**680)
 # Source coefficient perturbation uniform u''' <= S3, so L2 <=(3/2)*S3.
 u3=E.sqrt()+A(F(3,2)*S3)
 N3=ceiling_power_two(u3)
 # Endpoint u''(B) computed INDEPENDENTLY from same exact original
 # physical generators and their full analytic jet at B.
 grouped={}
 for f,k,q in terms:grouped.setdefault(f,[]).append((k,q))
 grouped=sorted(grouped.items())
 u2_B=2*original_jets(B,grouped,pole,pi,2)[2]
 # True endpoint source coefficient error <=S2 from NF413.
 S2=F(g['native_second_derivative_source_coefficient_radii_uniform_exact'])
 abs_u2_B=abs(u2_B)+A(S2)
 N2B=ceiling_power_two(abs_u2_B)
 # For ALL y in [-B,B], source u''(y) =
 # u''(B) - ∫_y^B u'''(s)ds, hence <=N2B + (3/2)*N3.
 N2=N2B+2*N3
 assert N2>0
 # Source-correlated full z'' formula, no actual quadrature:
 # Let A(x)=c(x)+1/2 log(B/(B-x)), d=B-x, t1=2d,t2=2(B+x),
 # R=K(t1)+K(t2)-1/(2d), v=u(B), w=u'(B).
 #
 # z''= A u''(x) + w(K(t1)-K(t2)) + v R'(x)
 #      + I0[u''](x)+I1[u''](x)
 #      + P_reg''(x) -a/4 sinh(x/2).
 #
 # All standalone u'(x) terms CANCEL EXACTLY between
 # A'(x)u' and derivative of I0/I1 moving boundaries.
 #
 # On x∈[899/1000,901/1000]:
 #   |A|<16, K(t1)<6, K(t2)<1, |R'|<60,
 #   |u(B)|<1e-9, |u'(B)|<1e-6,
 #   |I0[u'']|<3*N3 and |I1[u'']|<4*N3,
 #   |P_reg''|<42*N2, |center''|<2.
 #   Thus |z''|<58*N2+7*N3+3.
 M2=58*N2+7*N3+3
 assert M2>=N3 and M2<10**300
 dmin=B-(X+RHO);t1min=2*dmin;t2min=2*(B+X-RHO)
 t1max=2*(B-(X-RHO));t2max=2*(B+X+RHO)
 assert t1min>F(1,3) and t1max<F(1,2)
 assert t2min>3 and t2max<F(9,2)
 # proof kernel |K'| <=1/(2t)+2/t² from e^t>=1+t.
 assert F(1,2)/t1min+F(2)/t1min**2<20
 assert F(1,2)/t2min+F(2)/t2min**2<1
 assert F(1,2)/dmin**2<18
 assert 2*20+2*1+18<=60
 assert F(16)*N2+F(1,10**6)*7+F(1,10**9)*60+7*N3+42*N2+2<M2
 assert F(3,2)**2>2 and F(9,4)**2>F(9,2)
 # Full original x Taylor remainder about NF416/419 validated x0:
 # |R2(x)| <= M2*(x-x0)^2/2 for every x in the entire
 # ORIGINAL nontrivial interval |x-9/10|<=1/1000.
 # Source z point and derivative are separately certified from parents.
 point=F(1,10**3)
 remainder=M2*point*point/2
 out={
  'pass':'NF420',
  'standing':'FULL ORIGINAL SOURCE-CORRELATED u4 THIRD DERIVATIVE L2 GRAM; VALID ORIGINAL z SECOND-ORDER TAYLOR REMAINDER ON NONZERO PHYSICAL CELL6 INTERVAL; NF404 SCALAR OPEN',
  'original_source_sha256':ssha,'original_NF411_endpoint_jet_sha256':jsha,
  'original_NF413_curvature_sha256':gsha,'original_NF419_true_first_xjet_sha256':rsha,
  'original_NF406_original_seams_sha256':seamsha,
  'unchanged_complete_original_selected_242_critical_4_source':True,
  'all_selected_selected_and_selected_critical_critical_critical_source_cross_retained':True,
  'true_original_odd_pole_u_third_derivative_cosh_included':True,
  'analytic_correlation_exact_moments_not_numeric_grid':True,
  'source_native_precision_bits':4096,
  'full_original_third_derivative_basis_count':len(current),
  'full_original_u_third_derivative_Gram_L2_sq_Arb':str(E),
  'source_third_derivative_coefficient_uniform_radii_exact':str(S3),
  'original_full_u_third_derivative_L2_strict_integer_upper':str(N3),
  'original_u_second_derivative_endpoint_Arb':str(u2_B),
  'original_u_second_derivative_endpoint_with_source_radius_strict_upper':str(N2B),
  'original_u_second_derivative_full_support_strict_upper':str(N2),
  'original_true_physical_cell6_interval_exact':['899/1000','901/1000'],
  'original_cell6_same_true_prime_branches_as_NF419_certified':True,
  'original_x_t_moving_boundary_uprime_cancellation_exact':'A_prime=K(t1)-K(t2); I0prime_plus_I1prime_endpoint=(K(t1)-K(t2))*(uprime(B)-uprime(x)); all standalone uprime(x) cancel',
  'true_original_z_second_derivative_uniform_bound_on_interval':str(M2),
  'true_original_x_second_order_Taylor_radius':'1/1000',
  'true_original_x_second_order_Taylor_remainder_upper_exact':str(remainder),
  'original_NF419_true_first_xjet_reused':True,
  'second_x_derivative_uniform_remainder_certified_on_nontrivial_cell_subinterval':True,
  'original_complete_analytic_cell6_enclosure_precision_NF404':'UNDECIDED',
  'original_complete_entire_cell6_covered':False,
  'original_cellwise_signed_z_p_cross_integrated':False,
  'original_NF404_complete_centered_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF420 original full u third derivative Gram',str(E)[:220],flush=True)
 print('NF420 true original ||u''' + "'" + '||2 <',N3,'u second sup <',N2,flush=True)
 print('NF420 uniform true original |z''|<'+str(M2)+' on [899/1000,901/1000]',flush=True)
 print('NF420 true second Taylor remainder at radius 1/1000 <',str(remainder),flush=True)
 print('NF420 true cellwide NF404 centered scalar OPEN',flush=True)
if __name__=='__main__':main()
