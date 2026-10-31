#!/usr/bin/env python3
"""NF421: rigorous original 246-generator complete z''(9/10) source jet.

Full original NF407 true I0[u4''] and I1[u4''] analytic t-panel
correlation, exact u4(B), u4'(B), source/prime branch derivatives,
NF420 second exact arch boundary cancellation. Source native radius,
tiny removable t=0, analytic kernel and source tails paid by Fractions.
This numeric second jet must NOT itself claim a uniform x interval.
"""
import argparse,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
import nf415_original_cell6_I1_correlated_taylor_native as nf415
import nf416_original_cell6_full_I0_regularized_taylor as nf416
from nf415_original_cell6_I1_validated_acb import read,native_source,A,C
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10);T1=F(2,5);T2=F(4)
WEIGHTS={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
POLE=F(6677356497477490213,4611686018427387904)
def K(t):
 return (-t/4).exp()/(1-(-t).exp())
def Kprime(t):
 r=(-t).exp()
 return K(t)*(-arb(1)/4-r/(1-r))
def tiny_I0_second(groups,pole,pi):
 vals=nf416.original_jets(X,groups,pole,pi,nf416.NS_TINY+2)
 h=nf416.H_series_at_zero()
 p=[arb(1)]
 for n in range(nf416.NS_TINY+nf416.NH+1):p.append(p[-1]*A(nf416.TAU))
 ret=arb(0)
 for n in range(2,nf416.NS_TINY+1,2):
  fac=-vals[n+2]*(n+2)*(n+1)/(2**n)
  for j,q in enumerate(h):ret+=fac*A(q)*p[n+j]/(n+j)
 return ret
def second_panel_I0(t0,groups,pole,pi,ux2):
 N=nf416.NS
 plus=nf416.original_jets(X+t0/2,groups,pole,pi,N+2)
 minus=nf416.original_jets(X-t0/2,groups,pole,pi,N+2)
 vals=[]
 fplus=arb(1);fminus=arb(1)
 for n in range(N+1):
  if n:fplus/=2;fminus/=(-2)
  vals.append((ux2 if n==0 else arb(0))-(fplus*plus[n+2]+fminus*minus[n+2])*(n+2)*(n+1)/2)
 k=nf416.K_series_at(t0)
 r=A(nf416.RHO);powers=[arb(1)]
 for n in range(N+nf416.NK+1):powers.append(powers[-1]*r)
 ret=arb(0)
 for n in range(0,N+nf416.NK+1,2):
  v=sum((k[j]*vals[n-j] for j in range(max(0,n-N),min(n,nf416.NK)+1)),arb(0))
  ret+=v*2*powers[n+1]/(n+1)
 return ret
def second_panel_I1(t0,groups,pole,pi,ux2):
 N=nf415.NS
 source=nf416.original_jets(X-t0/2,groups,pole,pi,N+2)
 v=[];f=arb(1)
 for n in range(N+1):
  if n:f/=(-2)
  v.append(((ux2 if n==0 else arb(0))-(n+2)*(n+1)*source[n+2]*f)/2)
 k=nf415.kernel_jets(t0)
 r=A(nf415.RHO);powers=[arb(1)]
 for n in range(N+nf415.NK+1):powers.append(powers[-1]*r)
 ret=arb(0)
 for n in range(0,N+nf415.NK+1,2):
  coef=sum((k[j]*v[n-j] for j in range(max(0,n-N),min(n,nf415.NK)+1)),arb(0))
  ret+=2*powers[n+1]*coef/(n+1)
 return ret
def source_second_at(y,groups,pole,pi):
 out=A(pole)/4*(y/2).sinh()
 for f,terms in groups:
  w=2*pi*A(f)
  sn=(w*y).sin();co=(w*y).cos()
  for k,cf in terms:
   a=A(cf)
   trig=sn if k%2==0 else co
   deriv=co if k%2==0 else -sn
   if k>=2:out+=a*k*(k-1)*y**(k-2)*trig
   if k:out+=2*a*k*y**(k-1)*w*deriv
   out-=a*y**k*w*w*trig
 return out
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 ap.add_argument('--nf419',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 ap.add_argument('--nf420',default='notes/data/provisional/NF420_original_cell6_independent_sharpened_Taylor_positive_interval.json')
 ap.add_argument('--output',required=True)
 ap.add_argument('--precision',type=int,default=1024)
 a=ap.parse_args()
 source,sha=read(a.source);gram,gsha=read(a.nf413)
 finite,fsha=read(a.nf414);jet,jsha=read(a.nf419);parent,psha=read(a.nf420)
 assert gram['original_nf407_full_native_source_sha256']==sha
 assert finite['original_nf407_source_sha256']==sha
 assert jet['original_nf407_source_sha256']==sha
 assert parent['original_nf407_source_sha256']==sha
 assert jet['first_order_original_x_jet_certified']
 assert parent['original_true_complete_z_second_x_derivative_uniform_bound']==125457
 assert all(q['W_ODD_NEG']==q['RH']=='OPEN' for q in (source,gram,finite,jet,parent))
 ctx.prec=a.precision
 terms,pole,S0=native_source(source)
 groups={}
 for f,k,v in terms:groups.setdefault(f,[]).append((k,v))
 groups=sorted(groups.items())
 Uraw=sum((abs(v)*B**k for f,k,v in terms),abs(pole))
 assert len(terms)>=240 and Uraw<10**160 and S0<F(1,10**700)
 assert max(f for f,v in groups)<883
 # The analytic source second-derivative term triangle is dominated by
 # (w+13/B)^2 < 10^8 times the original full source Uraw.
 Rsmall=F(8*3**62)*Uraw*F(62)**518/math.factorial(518)
 R2small=10**8*Rsmall
 RH=6*nf416.TAU**61/(1-nf416.TAU)
 # True |D_t u''| <= ||u'''||L2 sqrt(t), so
 # integral (Htail/t)*D <= 2 ||u'''||2 sqrt(tau)*RH.
 # Replace 2*1334*sqrt(0.02)<400 by conservative 1000.
 E0tiny=F(6)*R2small/531+1000*RH
 assert E0tiny<F(1,10**48)
 Rlarge=F(3**16)*Uraw*F(16)**288/math.factorial(288)
 R2large=10**8*Rlarge
 K0tail=F(81)*F(2,5)**161/F(3,5)
 E0large=(T1-nf416.TAU)*(100*R2large+K0tail*(5000+R2large))
 assert E0large<F(1,10**29)
 eta=F(1,100)/T1
 K1tail=F(81)*eta**49/(1-eta)
 E1=(T2-T1)*(F(2)/T1*R2large+K1tail*(5000+R2large))
 assert E1<F(1,10**29)
 S2=F(gram['native_second_derivative_source_coefficient_radii_uniform_exact'])
 S4=10**16*S0
 assert S4<F(1,10**660)
 # t0 symmetric second difference uncertainty for true u'':
 # native δu'''' enters with ≤ S4 t^2/8, K<2/t,
 # while one-sided I1 has δu'' <= S2 and |K|<2/t.
 # Endpoints/cancellations and prime branches paid by 1e10*S0,
 # far above derivative factors but << quadrature tolerance.
 Ecoeff=S4*T1*T1/8+2*(T2/T1-1)*S2+10**10*S0
 E=E0tiny+E0large+E1+Ecoeff
 assert E<F(1,10**26)
 pi=arb.pi()
 jetsX=nf416.original_jets(X,groups,pole,pi,2)
 jetsB=nf416.original_jets(B,groups,pole,pi,1)
 ux2=jetsX[2]*2
 v=jetsB[0];w=jetsB[1]
 I0=tiny_I0_second(groups,pole,pi)
 assert (T1-nf416.TAU)/nf416.STEP==38
 for i in range(38):
  t0=nf416.TAU+(2*i+1)*nf416.RHO
  I0+=second_panel_I0(t0,groups,pole,pi,ux2)
  if (i+1)%10==0 or i==37:print('NF421 original I0 u-second panel',i+1,'/38',flush=True)
 I1=arb(0)
 for i in range(360):
  t0=T1+(2*i+1)*nf415.RHO
  I1+=second_panel_I1(t0,groups,pole,pi,ux2)
  if (i+1)%60==0:print('NF421 original I1 u-second panel',i+1,'/360',flush=True)
 d=A(B-X);x=A(X);t1=A(T1);t2=A(T2)
 e=(-d/2).exp()
 phi=((d/A(B))*(d/4).cosh()/(d/4).sinh()).log()+2*e.atan()
 q=(-t2/4).exp();J=2*(q.atanh()+q.atan())
 c=(arb(1)/4).digamma()-pi.log()+(J+phi)/2
 AA=c+(A(B)/d).log()/2
 Rprime=-2*Kprime(t1)+2*Kprime(t2)-1/(2*d*d)
 arch=AA*ux2+w*(K(t1)-K(t2))+v*Rprime
 assert abs(AA)<16
 prime=arb(0);branches=[]
 originals=finite['hotspot_points'][1]['all_seven_true_prime_branches']
 assert [x['n'] for x in originals]==list(WEIGHTS)
 for (n,p),o in zip(WEIGHTS.items(),originals):
  h=arb(n).log();weight=arb(p).log()/arb(n).sqrt()
  seam=abs(A(B)-h)
  if h<A(B) and x<seam:
   val=-weight*(source_second_at(x+h,groups,pole,pi)+source_second_at(x-h,groups,pole,pi))
   branch='both'
  elif h>A(B) and x<seam:
   val=arb(0);branch='neither'
  else:
   val=-weight*source_second_at(x-h,groups,pole,pi)
   branch='post-seam'
  assert o['branch']==branch,('original signed prime seam mismatch',n,branch,o['branch'])
  prime+=val
  branches.append({'n':n,'branch':branch})
 center=-A(POLE)/4*(x/2).sinh()
 total=I0+I1+arch+prime+center
 raw=nf415.enclosed(total,80)
 lo=F(raw[0])-E;hi=F(raw[1])+E
 assert lo<hi and hi-lo<F(1,10**26)
 assert lo>-125457 and hi<125457
 out={
  'pass':'NF421',
  'standing':'COMPLETE ORIGINAL SOURCE-CORRELATED SECOND x JET zsecond(9/10) TRUE PHYSICAL I0 I1 SEVEN PRIMES; NOT YET LOCALLY UNIFORM',
  'original_source_sha256':sha,
  'original_NF413_source_curvature_sha256':gsha,
  'original_NF414_seven_signed_prime_finite_sha256':fsha,
  'original_NF419_source_first_jet_sha256':jsha,
  'original_NF420_second_order_remainder_parent_sha256':psha,
  'physical_cell':6,'physical_x':'9/10',
  'original_true_complete_242_selected_4_critical_source':True,
  'original_full_I0_u_second_t_bounds':['0','2/5'],
  'original_full_I1_u_second_t_bounds':['2/5','4'],
  'original_full_u_second_I0_t0_analytic_H':True,
  'original_u_second_tiny_order':530,
  'original_u_second_regular_source_order':300,
  'original_u_second_I0_panels':38,
  'original_u_second_I1_panels':360,
  'original_seven_signed_prime_derivative_branches':branches,
  'original_true_moving_double_arch_cancellation_used':True,
  'original_NF404_dyadic_center_second_derivative_used':True,
  'source_raw_triangle_exact':str(Uraw),
  'source_radius_S0_exact':str(S0),
  'source_radius_S2_exact':str(S2),
  'source_radius_S4_upper_exact':str(S4),
  'I0_tiny_derivative_tail_exact':str(E0tiny),
  'I0_regular_derivative_tail_exact':str(E0large),
  'I1_derivative_tail_exact':str(E1),
  'full_original_source_native_coefficient_charge_exact':str(Ecoeff),
  'full_original_second_jet_total_error_exact':str(E),
  'true_original_complete_zsecond_at_x9over10_outward_rational_interval':[str(lo),str(hi)],
  'true_original_complete_zsecond_at_x9over10_width_exact':str(hi-lo),
  'original_true_pointwise_second_x_jet_certified':True,
  'original_zsecond_local_x_uniform_interval_certified':False,
  'original_complete_entire_cell6_z_model_certified':False,
  'original_NF404_entire_scalar_certified':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+'\n')
 print('NF421 true original 246-source complete zsecond(0.9)',str(total)[:200],flush=True)
 print('NF421 second jet width',str(hi-lo)[:80],flush=True)
 print('NF421 pointwise second jet only until complete x third-derivative uniform source parent accepted',flush=True)
if __name__=='__main__':main()
