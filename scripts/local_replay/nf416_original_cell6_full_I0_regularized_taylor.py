#!/usr/bin/env python3
"""NF416: certified complete original physical I0 at x=9/10, plus original z point.

No ordinary Gauss. Correlated 242+4 original source Taylor at actual rational
x/t panel centers. Entire t=0 singularity removed analytically by
H(t)=t*K(t) and the even second-difference Taylor coefficients.
Source/kernel analytic tails and all original 4096-bit coefficient radii
paid with exact rational inequalities. Same original NF370 u4, NF407 7 primes.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import acb,arb,ctx
from nf415_original_cell6_I1_validated_acb import read,native_source,U,A,C
from nf415_original_cell6_I1_correlated_taylor_native import enclosed
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10); X=F(9,10); T=F(2,5)
TAU=F(1,50); STEP=F(1,100); RHO=STEP/2;RHO_S=RHO/2
NS_TINY=530;NH=60;NS=300;NK=160
def frac_interval_add(x,y):
 return [F(x[0])+F(y[0]),F(x[1])+F(y[1])]
def original_jets(s0,grouped,pole,pi,N):
 """Full original source derivatives / n! at exact rational s0, outward Arb."""
 result=[arb(0) for _ in range(N+1)]
 for f,terms in grouped:
  degree=max(k for k,v in terms)
  even=[F(0)]*(degree+1);odd=[F(0)]*(degree+1)
  for k,v in terms:
   arr=even if k%2==0 else odd
   for j in range(k+1):
    arr[j]+=v*math.comb(k,j)*s0**(k-j)
  poly=[acb(A(even[j]),A(odd[j])) for j in range(degree+1)]
  iw=acb(arb(0),2*pi*A(f))
  ew=[(iw*C(s0)).exp()]
  for n in range(1,N+1):ew.append(ew[-1]*iw/n)
  for n in range(N+1):
   val=acb(0)
   for j in range(min(degree,n)+1):val+=poly[j]*ew[n-j]
   result[n]+=val.imag
 sh=(C(s0)/2).sinh().real;ch=(C(s0)/2).cosh().real
 factor=arb(1)
 for n in range(N+1):
  if n:factor=factor/(2*n)
  result[n]+=A(pole)*(sh if n%2==0 else ch)*factor
 return result
def H_series_at_zero():
 """EXACT rational quotient exp(-t/4) / ((1-exp(-t))/t)."""
 a=[F((-1)**n,4**n*math.factorial(n)) for n in range(NH+1)]
 d=[F((-1)**n,math.factorial(n+1)) for n in range(NH+1)]
 q=[a[0]]
 for n in range(1,NH+1):
  q.append(a[n]-sum((d[j]*q[n-j] for j in range(1,n+1)),F(0)))
 assert q[0]==1
 return q
def K_series_at(t0):
 r=(-A(t0)).exp();v=(-A(t0)/4).exp()
 num=[v];den=[arb(1)-r]
 for n in range(1,NK+1):
  num.append(num[-1]*A(F(-1,4))/n)
  den.append(-r*A(F((-1)**n,math.factorial(n))))
 q=[num[0]/den[0]]
 for n in range(1,NK+1):
  q.append((num[n]-sum((den[j]*q[n-j] for j in range(1,n+1)),arb(0)))/den[0])
 return q
def tiny_analytic_integral(grouped,pole,pi,ux):
 # Entire source Taylor at original x, not at arbitrary other object.
 u=original_jets(X,grouped,pole,pi,NS_TINY)
 assert not (u[0]<ux or u[0]>ux),("source identity x mismatch",str(u[0])[:130],str(ux)[:130])
 h=H_series_at_zero()
 # D_tu=-sum_even>=2 u_n*(t/2)^n, and K=H/t.
 # Every polynomial coefficient integrated exactly 0<=t<=TAU.
 result=arb(0);powers=[arb(1)]
 for n in range(NS_TINY+NH+1):powers.append(powers[-1]*A(TAU))
 for n in range(2,NS_TINY+1,2):
  factor=-u[n]/(2**n)
  for j,q in enumerate(h):
   result+=factor*A(q)*powers[n+j]/(n+j)
 return result
def large_panel(t0,grouped,pole,pi,ux):
 # Original symmetric u(x +/-t/2) must be present: no I1 substitution.
 plus=original_jets(X+t0/2,grouped,pole,pi,NS)
 minus=original_jets(X-t0/2,grouped,pole,pi,NS)
 D=[]
 powplus=arb(1);powminus=arb(1)
 for n in range(NS+1):
  if n:
   powplus/=2
   powminus/=(-2)
  d=(ux if n==0 else arb(0))-(plus[n]*powplus+minus[n]*powminus)/2
  D.append(d)
 K=K_series_at(t0)
 rho=A(RHO);rp=[arb(1)]
 for n in range(NS+NK+1):rp.append(rp[-1]*rho)
 acc=arb(0)
 for n in range(0,NS+NK+1,2):
  lower=max(0,n-NS);upper=min(NK,n)
  c=sum((K[j]*D[n-j] for j in range(lower,upper+1)),arb(0))
  acc+=c*(2*rp[n+1]/(n+1))
 return acc
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 p.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 p.add_argument('--nf415',default='notes/data/provisional/NF415_original_cell6_I1_correlated_taylor_native.json')
 p.add_argument('--output',required=True)
 p.add_argument('--precision',type=int,default=1024)
 args=p.parse_args()
 source,source_sha=read(args.source)
 nf413,csha=read(args.nf413);nf414,ssha=read(args.nf414);nf415,isha=read(args.nf415)
 assert nf413['original_nf407_full_native_source_sha256']==source_sha
 assert nf414['original_nf407_source_sha256']==source_sha
 assert nf415['original_nf407_source_sha256']==source_sha
 assert nf413['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert nf415['original_cell6_I1_source_rigorous']
 assert [x['cell'] for x in nf414['hotspot_points']]==[3,6,7]
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (source,nf413,nf414,nf415))
 ctx.prec=args.precision
 terms,pole,S0=native_source(source)
 groups={}
 for f,k,v in terms:groups.setdefault(f,[]).append((k,v))
 grouped=sorted(groups.items())
 assert len(terms)>=240 and max(k for f,vs in grouped for k,v in vs)<=13
 fmax=max(f for f,vs in grouped)
 assert fmax==F(112013,128) or fmax==F(8829140625,10000000) or (F(882)<fmax<F(883))
 assert max(F(7)*abs(f)*TAU/2 for f,vs in grouped)<62
 assert max(F(7)*abs(f)*RHO_S for f,vs in grouped)<16
 Uraw=sum((abs(v)*B**k for f,k,v in terms),abs(pole))
 assert Uraw<F(10)**160
 # Pure source tails of full original u at x +/- t/2:
 # finite monomial degree max13, |omega*delta_s|<62 for t<=.02,
 # e^62<3^62. For real t each Taylor remainder has extra
 # (t/TAU)^(NS_TINY+1), enabling division by t at the removable origin.
 Msmall=NS_TINY-13+1
 Rs=F(8*3**62)*Uraw*F(62)**Msmall/math.factorial(Msmall)
 assert Rs<F(1,10**60)
 # |H|<6 on complex |t|<=1. Use |exp(-t/4)|<3/2 and
 # |(1-exp(-t))/t|>1/4 from e<11/4.
 RH=F(6)*TAU**(NH+1)/(1-TAU)
 assert RH<F(1,10**100)
 # Both u-translations have source Taylor tails <=Rs(t/TAU)^(N+1);
 # integral |H*Derror/t| ≤6 Rs/(N+1), plus ∫|Herror D/t|
 # ≤ TAU*6*RH by NF413 ||u''||2<256 and |D/t|<6 on t<=.02.
 E_small=F(6)*Rs/(NS_TINY+1)+TAU*F(6)*RH
 assert E_small<F(1,10**60)
 # Large original t in [.02,.4], 38 identical rational panels.
 Mlarge=NS-13+1
 Rsource=F(3**16)*Uraw*F(16)**Mlarge/math.factorial(Mlarge)
 assert Rsource<F(1,10**42)
 # For each center>=.025, disk |dt|<t0/2 has Re t>=1/80,
 # K complex modulus <81. Fixed half-step/radius <=2/5.
 rk=F(81)*F(2,5)**(NK+1)/F(3,5)
 assert rk<F(1,10**60)
 # Entire original source |u4|<513 from NF413 second derivative and NF411
 # endpoint data, so |D_tu|<1026, padded as 1030.
 # Real |K|<=2/t<=100 for t>=.02.
 E_large=(T-TAU)*(F(100)*Rsource+rk*(F(1030)+Rsource))
 assert E_large<F(1,10**39)
 # The original coefficient-native true source difference has second
 # derivative uniform S2; unlike S0, this is legitimate at t=0:
 # |δD_t|<=S2*t²/8; ∫K<∫2/t gives S2*T²/8.
 S2=F(nf413['native_second_derivative_source_coefficient_radii_uniform_exact'])
 assert S2<F(1,10**735)
 coeffcharge=S2*T*T/8
 src=U(source);ux=src.at(C(X)).real
 pi=arb.pi()
 small=tiny_analytic_integral(grouped,pole,pi,ux)
 panels=int((T-TAU)/STEP);assert panels==38
 acc=arb(0)
 for j in range(panels):
  t0=TAU+(F(2*j+1)*RHO)
  acc+=large_panel(t0,grouped,pole,pi,ux)
  if j%10==9 or j==panels-1:
   print('NF416 original source I0 large panels',j+1,'/',panels,flush=True)
 integrated=small+acc
 E=E_small+E_large+coeffcharge
 raw=enclosed(integrated,95)
 I0=[F(raw[0])-E,F(raw[1])+E]
 assert I0[1]-I0[0]<F(1,10**12)
 finite=nf414['hotspot_points'][1]['original_z_finite_known_part_source_paid_rational_interval']
 I1=nf415['true_original_cell6_I1_rational_outward_interval']
 zlo=F(finite[0])+F(I1[0])+I0[0]
 zhi=F(finite[1])+F(I1[1])+I0[1]
 assert zhi-zlo<F(1,10**12)
 out={
 'pass':'NF416',
 'standing':'CERTIFIED ACTUAL COMPLETE ORIGINAL z(9/10) POINTWISE VIA 246-SOURCE FULL I0+I1 AND NF414 SEVEN SIGNED PRIMES; CELLWISE AND NF404 OPEN',
 'original_nf407_source_sha256':source_sha,
 'original_nf413_native_full_curvature_sha256':csha,
 'original_nf414_original_finite_seven_primes_sha256':ssha,
 'original_nf415_full_I1_sha256':isha,
 'original_242_selected_and_4_critical_source_preserved':True,
 'original_physical_support_B':'11/10',
 'original_physical_cell':6,'original_physical_x':'9/10',
 'original_I0_t_interval':['0','2/5'],
 'original_zero_singularity_removed_by_H_t_equals_tK_t':True,
 'entire_original_source_symmetric_plus_and_minus_translation_preserved':True,
 'exact_rational_tiny_t_interval':['0','1/50'],
 'tiny_t_source_Taylor_degree':NS_TINY,
 'tiny_t_analytic_H_Taylor_degree':NH,
 'original_source_all_selected_frequencies_max_exact':str(fmax),
 'original_tiny_t_source_remainder_upper_exact':str(Rs),
 'original_tiny_t_H_remainder_upper_exact':str(RH),
 'original_tiny_t_integrated_truncation_upper_exact':str(E_small),
 'source_taylor_degree_large':NS,
 'kernel_taylor_degree_large':NK,
 'large_panel_count':panels,'original_large_t_interval':['1/50','2/5'],
 'original_large_t_source_taylor_remainder_upper_exact':str(Rsource),
 'original_large_t_kernel_taylor_remainder_upper_exact':str(rk),
 'original_large_t_integrated_truncation_upper_exact':str(E_large),
 'original_full_native_4096bit_source_second_derivative_coefficient_radius_S2':str(S2),
 'original_I0_native_source_error_paid_exact':str(coeffcharge),
 'original_I0_total_truncation_and_source_error_upper_exact':str(E),
 'original_I0_full_0_to_2over5_rational_outward_interval':[str(v) for v in I0],
 'original_I0_interval_width_exact':str(I0[1]-I0[0]),
 'original_true_full_z_cell6_at_x9over10_outward_interval':[str(zlo),str(zhi)],
 'original_true_full_z_cell6_pointwise_width_exact':str(zhi-zlo),
 'complete_original_z_pointwise_certified':True,
 'complete_original_z_on_full_cell6_certified':False,
 'complete_original_z_cells_3_and_7_certified':False,
 'signed_original_principal_z_cross_certified':False,
 'original_complete_centered_scalar_certified':False,
 'NF404_acceptance_gate_decided':False,
 'original_J242_perp_lowband':'OPEN',
 'original_operator_domain':'OPEN',
 'original_infinite_inverse':'OPEN',
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF416 fully original source I0',str(integrated)[:160],flush=True)
 print('NF416 original source I0 width',str(I0[1]-I0[0])[:90],flush=True)
 print('NF416 TRUE ORIGINAL z(9/10) POINTWISE ENCLOSED; full cell/centered norm OPEN',flush=True)
if __name__=='__main__':main()
