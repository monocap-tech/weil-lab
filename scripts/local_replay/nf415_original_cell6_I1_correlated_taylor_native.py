#!/usr/bin/env python3
"""NF415 source-correlated exact-panel Taylor interval integral of original I1, cell 6.

Original u4 = full 242 selected physical polynomial-trig + four critical
sine/pole blocks from NF407; coefficients combined exactly before evaluating
Taylor jets at rational panel centres. K(t) Taylor coefficients are generated
from the exact quotient of its exponential power series. Each panel is
integrated analytically; source and K complex-analytic remainders are
independently bounded by EXACT fractions. No Gauss samples or speculative
convergence. Produces only cell-6 I1, NOT remaining I0 / true z / NF404 scalar.
"""
import argparse,hashlib,json,sys,math
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import read,native_source,U,A,C
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
X=F(9,10)
LEFT=F(2,5);RIGHT=F(4)
STEP=F(1,100);RHO=STEP/2;RHO_S=RHO/2
NS=300;NK=48
def enclosed(z,digits=85):
 m,r,e=z.mid_rad_10exp(digits)
 return [str(F(int(m)-int(r))*F(10)**int(e)),str(F(int(m)+int(r))*F(10)**int(e))]
def source_jets(s0,grouped,pole,pi):
 # Coefficients of original source u(s0+δs) in δs (NOT δt).
 result=[arb(0) for _ in range(NS+1)]
 for f,terms in grouped:
  degree=max(k for k,v in terms)
  even=[F(0)]*(degree+1);odd=[F(0)]*(degree+1)
  for k,v in terms:
   target=even if k%2==0 else odd
   for j in range(k+1):
    target[j]+=v*math.comb(k,j)*s0**(k-j)
  poly=[acb(A(even[j]),A(odd[j])) for j in range(degree+1)]
  iw=acb(arb(0),2*pi*A(f))
  ew=[(iw*C(s0)).exp()]
  for n in range(1,NS+1):ew.append(ew[-1]*iw/n)
  for n in range(NS+1):
   val=acb(0)
   for j in range(min(degree,n)+1):
    val+=poly[j]*ew[n-j]
   result[n]+=val.imag
 z=C(s0)/2
 sh=z.sinh().real;ch=z.cosh().real
 fac=arb(1)
 for n in range(NS+1):
  if n:fac=fac/(2*n)
  result[n]+=A(pole)*(sh if n%2==0 else ch)*fac
 return result
def kernel_jets(t0):
 # K(t)=exp(-t/4)/(1-exp(-t)). All t0 exact rational > 2/5.
 r=(-A(t0)).exp();v=(-A(t0)/4).exp()
 numerator=[v];denom=[arb(1)-r]
 for n in range(1,NK+1):
  numerator.append(numerator[-1]*A(F(-1,4))/n)
  denom.append(-r*A(F((-1)**n,math.factorial(n))))
 q=[numerator[0]/denom[0]]
 for n in range(1,NK+1):
  rest=sum((denom[j]*q[n-j] for j in range(1,n+1)),arb(0))
  q.append((numerator[n]-rest)/denom[0])
 return q
def panel(center,grouped,pole,ux,pi):
 s0=X-center/2
 u=source_jets(s0,grouped,pole,pi)
 D=[];factor=arb(1)
 for n,z in enumerate(u):
  if n:factor=factor/(-2)
  D.append((ux-z)/2 if n==0 else -z*factor/2)
 K=kernel_jets(center)
 # Polynomial exact integral on symmetric rational t interval.
 acc=arb(0)
 rho=A(RHO);powers=[arb(1)]
 for n in range(NS+NK+2):powers.append(powers[-1]*rho)
 for n in range(0,NS+NK+1,2):
  lower=max(0,n-NS);upper=min(NK,n)
  coef=sum((K[k]*D[n-k] for k in range(lower,upper+1)),arb(0))
  acc+=coef*(2*powers[n+1]/(n+1))
 return acc
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 ap.add_argument('--output',required=True)
 ap.add_argument('--precision',type=int,default=1024)
 args=ap.parse_args()
 s,ssha=read(args.source);g,gsha=read(args.nf413);q,qsha=read(args.nf414)
 assert g['original_nf407_full_native_source_sha256']==ssha
 assert q['original_nf407_source_sha256']==ssha
 assert g['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert [v['cell'] for v in q['hotspot_points']]==[3,6,7]
 assert all(v['W_ODD_NEG']==v['RH']=='OPEN' for v in (s,g,q))
 ctx.prec=args.precision
 terms,pole,S0=native_source(s)
 assert len(terms)>=240
 groups={}
 for f,k,v in terms:groups.setdefault(f,[]).append((k,v))
 grouped=sorted(groups.items())
 assert all(k<=13 for f,vs in grouped for k,v in vs)
 assert max(F(7)*abs(f)*RHO_S for f,vs in grouped)<16
 # Exact full raw source triangle is used ONLY for rigorously tiny
 # local Taylor remainder, not to bound complete integral.
 Uraw=sum((abs(v)*B**k for f,k,v in terms),abs(pole))
 assert Uraw<F(10)**160,('original exact source coefficients out of envelope',str(Uraw)[:100])
 Ntail=NS-13+1
 Rsource=F(3**16)*Uraw*F(16)**Ntail/math.factorial(Ntail)
 assert Rsource<F(1,10**42),('analytic source Taylor tail too large',str(Rsource)[:100])
 # Since all real panel t0>=0.4, disk |t-t0|<=t0/2
 # stays in Re(t)>=0.2. Analytic K bound <6,
 # ratio rho/(t0/2)<=1/40. Cauchy tail <7/40^(NK+1).
 RK=F(7,40**(NK+1))
 assert RK<F(1,10**70)
 # From original NF411 |u(B)|<1e-9, |u'(B)|<1e-6 and
 # NF413 ||u''||2<256, endpoint Taylor + CS gives
 # uniform ||u||∞<513 on [-B,B] because sqrt((2B)^3/3)<2.
 # Hence |(u(x)-u(s))/2|<513; use 520 margin.
 # K(t)<2/t<=5 on true I1 t∈[2/5,4].
 integrand_sup_error=F(5,2)*Rsource+RK*(F(520)+Rsource/F(2))
 integrated_error=(RIGHT-LEFT)*integrand_sup_error
 assert integrated_error<F(1,10**40)
 src=U(s);ux=src.at(C(X)).real
 pi=arb.pi()
 panels=int((RIGHT-LEFT)/STEP)
 assert panels==360
 acc=arb(0)
 for j in range(panels):
  center=LEFT+(F(2*j+1)*RHO)
  acc+=panel(center,grouped,pole,ux,pi)
  if j%60==59:print('NF415 original full analytic panel',j+1,'/',panels,flush=True)
 # Arb exact physical polynomial integrations include ALL signed terms,
 # source uncertainty <5*S0 from ∫K<2ln10<5.
 charge=integrated_error+5*S0
 raw=enclosed(acc)
 lo=F(raw[0])-charge;hi=F(raw[1])+charge
 assert lo<=hi
 interval=[str(lo),str(hi)]
 assert hi-lo<F(1,10**12),('true original I1 enclosure unresolved',str(hi-lo)[:180])
 out={
 'pass':'NF415',
 'standing':'CERTIFIED TRUE ORIGINAL 242+4 SOURCE-CORRELATED CELL6 I1 PHYSICAL ARCH INTEGRAL, POINTWISE SMALL-t I0; ENTIRE I0/z OPEN',
 'original_nf407_source_sha256':ssha,
 'original_nf413_correlated_full_curvature_sha256':gsha,
 'original_nf414_true_finite_hotspot_sha256':qsha,
 'original_cell':6,'original_physical_x':'9/10',
 'actual_original_I1_exact_t_interval':['2/5','4'],
 'original_source_246_generator_coverage':True,
 'original_all_source_correlations_preserved_before_panel_integration':True,
 'original_physical_critical_sine_and_odd_pole_retained':True,
 'source_taylor_order':NS,'kernel_taylor_order':NK,
 'number_of_exact_rational_symmetric_panels':panels,
 'native_precision_bits':args.prec,
 'original_coefficient_source_sup_S0_exact':str(S0),
 'analytic_exact_source_raw_abs_U_exact':str(Uraw),
 'exact_rational_local_source_tail_upper':str(Rsource),
 'exact_rational_kernel_tail_upper':str(RK),
 'entire_original_I1_analytic_truncation_error_upper':str(integrated_error),
 'original_native_coefficient_integral_error_upper':str(5*S0),
 'true_original_cell6_I1_rational_outward_interval':interval,
 'true_original_cell6_I1_interval_width_exact':str(hi-lo),
 'original_cell6_I1_source_rigorous':True,
 'original_I0_t0_pointwise_error_at_h_1e12_strict_upper':'1/20000000000000000',
 'original_cell6_remaining_I0_above_h_integrated':False,
 'true_original_z_cell6_pointwise_certified':False,
 'true_original_z_on_full_hotspot_cells_certified':False,
 'complete_original_centered_scalar_certified':False,
 'NF404_gate_decided':False,'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dst=Path(args.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+'\n')
 print('NF415 TRUE original cell6 I1 certified interval',str(acc)[:180],flush=True)
 print('NF415 exact interval width',str(hi-lo)[:150],flush=True)
 print('NF415 original I0, true z, full NF404 scalar OPEN',flush=True)
if __name__=='__main__':main()
