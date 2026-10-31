#!/usr/bin/env python3
"""NF419: true full original continuous z'(9/10), source-correlated native interval.

Differentiate I0 and I1 on THEIR actual moving physical t domains; simplify
shared boundary before numerical evaluation:
 B_arch=K(t1)*(u(B)-u(x))+K(t2)*(u(x)+u(B)).
All original 242 selected+4 critical source, signed seven real prime shifts,
finite arch multiplier, original NF404 center kept. Source-correlated 530/300
Taylor jets for u' and exact panel moments, rigorous derivative-native radii.
This is a FIRST x-JET at one true point, NOT a cellwide x Taylor norm.
"""
import argparse,math,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import acb,arb,ctx
import nf415_original_cell6_I1_correlated_taylor_native as nf415
import nf416_original_cell6_full_I0_regularized_taylor as nf416
from nf415_original_cell6_I1_validated_acb import read,native_source,U,A,C
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10);T1=F(2,5);T2=F(4)
WEIGHTS={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
POLE=F(6677356497477490213,4611686018427387904)
def K(t):
 return (-t/4).exp()/(1-(-t).exp())
def uj_at(s,groups,pole,pi):
 coeff=nf416.original_jets(s,groups,pole,pi,1)
 return coeff[0],coeff[1]
def tiny_I0_prime(groups,pole,pi):
 # Analytic true original source derivative u'; exactly symmetric x shifts.
 vals=nf416.original_jets(X,groups,pole,pi,nf416.NS_TINY+1)
 H=nf416.H_series_at_zero()
 tau=A(nf416.TAU)
 powers=[arb(1)]
 for n in range(nf416.NS_TINY+nf416.NH+1):powers.append(powers[-1]*tau)
 out=arb(0)
 for n in range(2,nf416.NS_TINY+1,2):
  fac=-vals[n+1]*F(n+1,2**n)
  for j,h in enumerate(H):out+=fac*A(h)*powers[n+j]/(n+j)
 return out
def I0_prime_panel(mid,groups,pole,pi,uxprime):
 # Full source derivative jets for original I0 symmetric shifts.
 N=nf416.NS
 plus=nf416.original_jets(X+mid/2,groups,pole,pi,N+1)
 minus=nf416.original_jets(X-mid/2,groups,pole,pi,N+1)
 diff=[]
 pplus=arb(1);pminus=arb(1)
 for n in range(N+1):
  if n:
   pplus/=2
   pminus/=(-2)
  d=(uxprime if n==0 else arb(0))-(pplus*(n+1)*plus[n+1]+pminus*(n+1)*minus[n+1])/2
  diff.append(d)
 kval=nf416.K_series_at(mid)
 rho=A(nf416.RHO);powers=[arb(1)]
 for n in range(N+nf416.NK+1):powers.append(powers[-1]*rho)
 out=arb(0)
 for n in range(0,N+nf416.NK+1,2):
  coef=sum((kval[j]*diff[n-j] for j in range(max(0,n-N),min(n,nf416.NK)+1)),arb(0))
  out+=coef*2*powers[n+1]/(n+1)
 return out
def I1_prime_panel(mid,groups,pole,pi,uxprime):
 # True one-sided 1/2*[u'(x)-u'(x-t/2)].
 N=nf415.NS
 vals=nf416.original_jets(X-mid/2,groups,pole,pi,N+1)
 diff=[]
 factor=arb(1)
 for n in range(N+1):
  if n:factor/=(-2)
  diff.append(((uxprime if n==0 else arb(0))-(n+1)*vals[n+1]*factor)/2)
 kval=nf415.kernel_jets(mid)
 rho=A(nf415.RHO);powers=[arb(1)]
 for n in range(N+nf415.NK+1):powers.append(powers[-1]*rho)
 out=arb(0)
 for n in range(0,N+nf415.NK+1,2):
  coef=sum((kval[j]*diff[n-j] for j in range(max(0,n-N),min(n,nf415.NK)+1)),arb(0))
  out+=coef*2*powers[n+1]/(n+1)
 return out
def finite_prime_prime_derivative(ux,up,v,groups,pole,pi,nf414):
 x=A(X);d=A(B-X);t1=A(T1);t2=A(T2);piA=arb.pi()
 L=(A(B)/d).log()
 e=(-d/2).exp()
 phi=((d/A(B))*(d/4).cosh()/(d/4).sinh()).log()+2*e.atan()
 q=(-t2/4).exp()
 J2=2*(q.atanh()+q.atan())
 c=(arb(1)/4).digamma()-piA.log()+(J2+phi)/2
 phi_prime=1/d-1/(2*(d/2).sinh())-1/(2*(d/2).cosh())
 c_prime=-K(t2)-phi_prime/2
 finite=(c+L/2)*up+c_prime*ux+(ux-v)/(2*d)
 assert abs(c)<12 and abs(c_prime)<2 and abs(L)<7
 prime=arb(0);entries=[]
 assert len(nf414['all_seven_true_prime_branches'])==7
 for (n,p),entry in zip(WEIGHTS.items(),nf414['all_seven_true_prime_branches']):
  assert n==entry['n']
  h=arb(n).log();weight=arb(p).log()/arb(n).sqrt()
  seam=abs(A(B)-h)
  assert x<seam or x>seam
  if h<A(B) and x<seam:
   pplus=uj_at(X+F(0),groups,pole,pi) if False else nf416.original_jets(arb_to_frac_unused if False else F(0),groups,pole,pi,1) if False else None
   # Evaluate native source derivative directly at exact real Arb
   # center, high accuracy (arbitrary real log n is already outward).
   def source_der_at(y):
    val=arb(0)
    for f,terms in groups:
     w=2*pi*A(f)
     sn=(w*y).sin();co=(w*y).cos()
     for k,cf in terms:
      vcf=A(cf)
      val+=vcf*(k*y**(k-1)*(sn if k%2==0 else co) if k else arb(0))
      val+=vcf*y**k*w*(co if k%2==0 else -sn)
    val+=A(pole)/2*(y/2).cosh()
    return val
   piece=-weight*(source_der_at(x+h)+source_der_at(x-h))
   branch='both'
  elif h>A(B) and x<seam:
   piece=arb(0);branch='neither'
  else:
   def source_der_at(y):
    val=arb(0)
    for f,terms in groups:
     w=2*pi*A(f)
     sn=(w*y).sin();co=(w*y).cos()
     for k,cf in terms:
      vcf=A(cf)
      if k:val+=vcf*k*y**(k-1)*(sn if k%2==0 else co)
      val+=vcf*y**k*w*(co if k%2==0 else -sn)
    val+=A(pole)/2*(y/2).cosh()
    return val
   piece=-weight*source_der_at(x-h)
   branch='post-seam'
  assert branch==entry['branch'],(n,branch,entry['branch'])
  prime+=piece
  entries.append({'n':n,'branch':branch,'native_prime_derivative_arb':str(piece)[:130]})
 center=-A(POLE)*(x/2).cosh()/2
 return finite,prime,center,entries
def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 parser.add_argument('--nf411',default='notes/data/provisional/NF411_original_source_boundary_jet.json')
 parser.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 parser.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 parser.add_argument('--nf416',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 parser.add_argument('--nf418',default='notes/data/provisional/NF418_original_hotspot_cellwide_lipschitz_envelopes_exact.json')
 parser.add_argument('--precision',type=int,default=1024)
 parser.add_argument('--output',required=True)
 args=parser.parse_args()
 src,ssha=read(args.source);bjet,bsha=read(args.nf411)
 gram,gsha=read(args.nf413);finite,fsha=read(args.nf414)
 complete,zsha=read(args.nf416);front,frsha=read(args.nf418)
 assert bjet['nf407_source_sha256']==ssha
 assert gram['original_nf407_full_native_source_sha256']==ssha
 assert finite['original_nf407_source_sha256']==ssha
 assert complete['original_nf407_source_sha256']==ssha
 assert front['original_nf407_246_source_sha256']==ssha
 assert gram['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert complete['complete_original_z_pointwise_certified']
 assert front['whole_original_z_derivative_piecewise_uniform_upper_integer']==30000
 assert all(q['W_ODD_NEG']==q['RH']=='OPEN' for q in (src,bjet,gram,finite,complete,front))
 ctx.prec=args.precision
 terms,pole,S0=native_source(src)
 grouped={}
 for f,k,val in terms:grouped.setdefault(f,[]).append((k,val))
 grouped=sorted(grouped.items())
 assert len(terms)>=240 and max(k for f,vs in grouped for k,v in vs)<=13
 fmax=max(f for f,vs in grouped)
 assert F(882)<fmax<F(883)
 Uraw=sum((abs(v)*F(11,10)**k for f,k,v in terms),abs(pole))
 assert Uraw<F(10)**160 and S0<F(1,10**700)
 # Exact correlation-preserving local Taylor remainder for u'(s):
 # derivative raw coefficient absolute sum <10^4 Uraw, all source
 # frequencies |2pi f|<7f<6200 and k/B<13.
 R0=F(8*3**62)*Uraw*F(62)**518/math.factorial(518)
 R1=F(10**4)*R0
 RH=F(6)*nf416.TAU**61/(1-nf416.TAU)
 E_tiny=F(6)*R1/531+F(100)*RH
 assert E_tiny<F(1,10**50)
 Rlarge=F(3**16)*Uraw*F(16)**288/math.factorial(288)
 R1large=F(10**4)*Rlarge
 K0tail=F(81)*F(2,5)**161/F(3,5)
 E0regular=(T1-nf416.TAU)*(100*R1large+K0tail*(800+R1large))
 assert E0regular<F(1,10**31)
 eta=F(1,100)/T1
 K1tail=F(81)*eta**49/(1-eta)
 E1regular=(T2-T1)*(F(2)/T1*R1large+K1tail*(800+R1large))
 assert E1regular<F(1,10**30)
 # The physical original source coefficient error of u''' is
 # globally bounded by < 10^12 S0, since each basis polynomial has
 # degree<=13 and 2pi*f<6200, and the odd pole derivative <1.
 # Hence the symmetric source derivative error integrates to
 # E_I0_coeff < S3*T1^2/8, no spurious divergent S1/t.
 S1=F(10**4)*S0;S3=F(10**12)*S0
 assert S3<F(1,10**680)
 coeff= S3*T1*T1/8 + 2*(T2/T1-1)*S1 + F(10**6)*S0
 E=E_tiny+E0regular+E1regular+coeff
 assert E<F(1,10**27)
 physical=U(src)
 ux=physical.at(C(X)).real
 v=physical.at(C(B)).real
 jet=nf416.original_jets(X,grouped,pole,arb.pi(),1)
 assert jet[0].overlaps(ux)
 up=jet[1]
 up_original_I0= tiny_I0_prime(grouped,pole,arb.pi())
 I0_panels=int((T1-nf416.TAU)/nf416.STEP)
 assert I0_panels==38
 I0_regular=arb(0)
 for j in range(I0_panels):
  mid=nf416.TAU+(2*j+1)*nf416.RHO
  I0_regular+=I0_prime_panel(mid,grouped,pole,arb.pi(),up)
  if (j+1)%10==0 or j+1==I0_panels:
   print('NF419 correlated derivative original I0 panel',j+1,'/',I0_panels,flush=True)
 I1_panels=int((T2-T1)/nf415.STEP)
 assert I1_panels==360
 I1_regular=arb(0)
 for j in range(I1_panels):
  mid=T1+(2*j+1)*nf415.RHO
  I1_regular+=I1_prime_panel(mid,grouped,pole,arb.pi(),up)
  if (j+1)%60==0 or j+1==I1_panels:
   print('NF419 correlated derivative original I1 panel',j+1,'/',I1_panels,flush=True)
 # Exact moving seam/interface recomposition:
 # I0 boundary -2K(t1)*D(t1),
 # I1 lower +K(t1)*(u(x)-u(x-t1/2)), upper
 # +K(t2)*(u(x)-u(-B)).
 # Using u(B)=v and u(-B)=-v, sum = K(t1)(v-u(x))+K(t2)(u(x)+v).
 k1=K(A(T1));k2=K(A(T2))
 boundary=k1*(v-ux)+k2*(ux+v)
 finite_der,prime_der,center_der,entries=finite_prime_prime_derivative(ux,up,v,grouped,pole,arb.pi(),finite['hotspot_points'][1])
 full=up_original_I0+I0_regular+I1_regular+boundary+finite_der+prime_der+center_der
 raw=nf415.enclosed(full,85)
 lo=F(raw[0])-E;hi=F(raw[1])+E
 assert lo<hi and hi-lo<F(1,10**27)
 # NF418 full original bound deliberately loose but must contain new jet.
 assert lo>-30000 and hi<30000
 output={
 'pass':'NF419','standing':'SOURCE-CORRELATED FIRST TRUE ORIGINAL COMPLETE x-JET zprime(9/10), NOT CELLWIDE z TAYLOR/SCALAR',
 'original_nf407_source_sha256':ssha,
 'original_nf411_original_boundary_jet_sha256':bsha,
 'original_nf413_full_source_curvature_sha256':gsha,
 'original_nf414_all_seven_true_signed_primes_sha256':fsha,
 'original_nf416_complete_true_z_point_sha256':zsha,
 'original_nf418_full_cell_coarse_envelope_sha256':frsha,
 'physical_original_rational_x':'9/10','physical_original_cell':6,
 'original_same_242_selected_and_4_critical':True,
 'original_all_seven_signed_prime_derivative_branches':entries,
 'original_true_I0_derivative_original_bounds':['0','2/5'],
 'original_true_I1_derivative_original_bounds':['2/5','4'],
 'moving_original_I0_I1_boundary_exact_cancellation_formula':'K(t1)*(u(B)-u(x))+K(t2)*(u(x)+u(B))',
 'original_I0_derivative_t0_analytic_H_tK':True,
 'tiny_original_source_derivative_Taylor_order':530,
 'large_original_source_derivative_Taylor_order':300,
 'original_I0_derivative_analytic_regular_panel_count':I0_panels,
 'original_I1_derivative_analytic_panel_count':I1_panels,
 'original_tiny_source_derivative_Taylor_error_upper_exact':str(R1),
 'original_derivative_I0_tiny_integrated_error_upper_exact':str(E_tiny),
 'original_derivative_I0_regular_integrated_error_upper_exact':str(E0regular),
 'original_derivative_I1_integrated_error_upper_exact':str(E1regular),
 'original_original_source_coefficient_S0_exact':str(S0),
 'original_source_derivative_coefficient_S1_bound_exact':str(S1),
 'original_source_third_derivative_coefficient_S3_bound_exact':str(S3),
 'original_derivative_complete_native_coefficient_error_upper_exact':str(coeff),
 'original_full_zprime_integral_error_upper_exact':str(E),
 'true_original_complete_zprime_at_9over10_outward_rational_interval':[str(lo),str(hi)],
 'true_original_complete_zprime_interval_width_exact':str(hi-lo),
 'original_true_zpoint_parent_certified':True,
 'first_order_original_x_jet_certified':True,
 'complete_original_source_x_interval_second_derivative_remainder_certified':False,
 'original_full_cell_x_Taylor_enclosure_certified':False,
 'NF410_signed_cross_certified':False,'NF404_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(output,indent=2)+'\n')
 print('NF419 full original x derivative zprime(9/10)=',str(full)[:160],flush=True)
 print('NF419 certified outward interval width',str(hi-lo)[:90],flush=True)
 print('NF419 first-order x jet certified; second-order whole-cell remainder and NF404 OPEN',flush=True)
if __name__=='__main__':main()
