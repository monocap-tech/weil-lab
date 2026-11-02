#!/usr/bin/env python3
"""NF445: actual original source-correlated R_m and exact Laplace resummation.

The authentic NF424 native positive-frequency endpoint image:
T_m = ∫_0^∞ exp[-(m+1/4)t] u4(B+t/2) dt, m>=1.
This is an EXACT source-linear identity, including the odd sinh pole.
After NF444 leading v/a extraction, R_m is the SAME integral with
u4(B+t/2)-u4(B); no termwise abs over individual generators.
Then the entire residual infinite image family m>=1 is the exact
single correlated integral against
K1(s)=exp(-5s/4)/(1-exp(-s)).
Its t=0 endpoint at x=B is removable via u4(B+t/2)-v=O(t).
We perform independent 4096-bit genuine Arb/Acb source endpoint
derivatives and source-correlated T_m samples. This does NOT yet
certify quantitative infinite-tail integral, D7/D8 or RH.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U
from nf425_original_cell6_chebyshev_existence_exact import source
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
SAMPLES=(1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192)
ORDERS=6
def load(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(x):return arb(str(x))
def enclose(x,digits=75):
 mid,rad,expo=x.mid_rad_10exp(digits)
 fac=F(10)**int(expo)
 return [str((int(mid)-int(rad))*fac),str((int(mid)+int(rad))*fac)]
def I(z):return acb(A(0),z)
def ol(a,b):
 lo,hi=map(F,a);x,y=map(F,b)
 return lo<=y and x<=hi
def result_source(s):
 terms,pole,s0=native_source(s)
 assert len(terms)==273 and s0<F(1,10**700)
 return terms,pole,s0
def calc():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 ap.add_argument('--nf444',default='notes/data/provisional/NF444_original_nearB_resummed_J7_J8_exact_source_custody_index.json')
 ap.add_argument('--precision',type=int,default=4096)
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 ctx.prec=args.precision
 src,sha=load(args.source);seams,ksha=load(args.seams);principal,psha=load(args.principal);parent,parent_sha=load(args.nf444)
 assert sha==SRC and ksha==SEAM and args.precision>=2048
 assert parent['original_nf407_full_246_source_sha256']==sha
 assert parent['original_nf406_seams_sha256']==ksha
 assert principal['original_nf406_seams_sha256']==ksha
 assert src['original_dimension']==242 and len(src['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(src['original_source_critical_sine_frequencies'])==32
 assert all(d['W_ODD_NEG']==d['RH']=='OPEN' for d in (src,seams,principal,parent))
 orig,pole,s0=result_source(src)
 rat,pole2,s02=source(src)
 assert len(rat)==len(orig)==273 and pole==pole2 and s0==s02
 assert sorted((f,k,c) for f,k,c in orig)==sorted((f,k,c) for (f,k),c in rat.items())
 # Each polynomial-exponential source mode as a complex single carrier.
 # Genuine odd source sine/cos carrier convention matched to NF443.
 carriers=[]
 pi=arb.pi()
 end=A(0)
 derivative=[arb(0) for _ in range(ORDERS)]
 for f,k,c in orig:
  lam=acb(A(0),2*pi*A(f))
  alpha=acb(A(0),-A(c)/2) if k%2==0 else acb(A(c)/2)
  eB=(lam*A(B)).exp()
  factor=alpha*eB
  carriers.append((k,factor,lam))
  end+=2*(factor*A(B**k)).real
  for r in range(ORDERS):
   term=acb(0)
   for j in range(min(r,k)+1):
    falling=math.factorial(k)//math.factorial(k-j)
    term+=math.comb(r,j)*falling*A(B**(k-j))*lam**(r-j)
   derivative[r]+=2*(factor*term).real
 end+=A(pole)*(A(B)/2).sinh()
 for r in range(ORDERS):
  derivative[r]+=A(pole)*(A(B)/2).sinh()/(2**r) if r%2==0 else A(pole)*(A(B)/2).cosh()/(2**r)
 assert ol(enclose(end),enclose(derivative[0]))
 # The prior native source u4(B) is computed INDEPENDENTLY.
 u=U(src);direct=u.at(acb(A(B))).real
 assert ol(enclose(direct),enclose(end))
 vp=principal['original_source_u4_endpoint_interval']
 assert ol(enclose(end),vp)
 values=[]
 max_t_width=F(0)
 for m in SAMPLES:
  a=A(F(4*m+1,4))
  v=arb(0)
  for k,factor,lam in carriers:
   inv=1/(acb(a)-lam/2)
   powers=inv
   z=acb(0)
   for j in range(k+1):
    z+=A(F(math.comb(k,j)*math.factorial(j),2**j)*B**(k-j))*powers
    powers*=inv
   v+=2*(factor*z).real
  v+=A(pole)/2*((A(B)/2).exp()/A(m)-(-A(B)/2).exp()/(A(m)+A(F(1,2))))
  R=v-end/a
  # Exact multiple integration by parts yields a source-correlated
  # asymptotic: T_m=sum_{r=0}^{K-1}u^(r)(B)/(2^r a^(r+1))
  # + [1/(2a)^K] int_0^inf exp(-a t)u^(K)(B+t/2)dt.
  # This expansion is NOT a convergent asymptotic certificate
  # at finite m without an independent remainder bound.
  r2=R-derivative[1]/(2*a*a)
  r3=r2-derivative[2]/(4*a*a*a)
  tbound=enclose(v)
  w=F(tbound[1])-F(tbound[0])
  max_t_width=max(max_t_width,w)
  v_lo,v_hi=map(F,tbound)
  scale=max(F(1),abs(v_lo),abs(v_hi))
  assert w<scale*F(1,10**40),('native 4096-bit relative enclosure unexpectedly wide',m)
  values.append({
   'm':m,'a':str(F(4*m+1,4)),
   'original_source_correlated_Tm_arb_interval':tbound,
   'original_source_correlated_Rm_after_uB_over_a_interval':enclose(R),
   'original_Rm_minus_first_derivative_over_2a2_interval':enclose(r2),
   'original_Rm_minus_first_two_derivatives_interval':enclose(r3),
   'scaled_a2_Rm_interval':enclose(R*a*a),
   'scaled_a3_first_derivative_removed_interval':enclose(r2*a*a*a),
   'derivative_1_asymptotic_remainder_not_yet_uniformly_bounded':True
  })
  print('NF445 genuine original source m',m,'T',float(v.mid().real),'R',float(R.mid().real),'a2R',float((R*a*a).mid().real),flush=True)
 # The early source-correlated T_m genuinely have magnitudes up to 10^139;
 # do NOT require tiny absolute width for a huge valid interval.
 # Every m interval above passes strict relative width <1e-40.
 out={
  'pass':'NF445',
  'standing':'SOURCE-NATIVE ACTUAL CORRELATED ORIGINAL R_m AND EXACT LAPLACE INTEGRAL IDENTITY; UNIFORM DECISION QUALITY TAIL, J7/J8 SIGN OPEN',
  'original_nf407_source_sha256':sha,'original_nf406_seams_sha256':ksha,
  'original_nf407_principal_sha256':psha,'original_nf444_parent_custody_sha256':parent_sha,
  'original_full_selected_and_critical_source':246,'original_source_groups':len(orig),
  'original_precision_bits':args.precision,
  'original_source_u4_B_independent_native_interval':enclose(direct),
  'original_source_v_analytic_carrier_interval':enclose(end),
  'original_nf407_u4_B_overlap':True,
  'original_source_derivative_intervals_at_B':{str(i):enclose(v) for i,v in enumerate(derivative)},
  'original_source_M_original_NF444_approx':'1.41812105824581e144',
  'original_native_max_absolute_outward_interval_width':str(max_t_width),
  'original_all_Tm_sample_relative_interval_width_strict_below':'1e-40',
  'original_original_native_T_m_exact_laplace_identity':'Tm=integral_(0,infinity) e^(-(m+1/4)t) u4(B+t/2) dt, for m>=1',
  'original_correlated_R_m_exact_laplace_identity':'Rm=integral_(0,infinity) e^(-(m+1/4)t) [u4(B+t/2)-u4(B)] dt',
  'original_asymptotic_derivative_coefficients':'sum_j u4^(j)(B)/(2^j (m+1/4)^(j+1)), with remainder integral; no uniform remainder yet',
  'original_correlated_kernel_K1':'K1(s)=exp(-5s/4)/(1-exp(-s)) for s>0',
  'original_residual_infinite_image_exact_correlated_integral':'1/2 int_0^infty [u4(B+t/2)-u4(B)] [K1(t+2(B-x))-K1(t+2(B+x))] dt',
  'original_true_B_endpoint_residual_removable':'u4(B+t/2)-u4(B)=O(t), K1(t)=O(1/t), product bounded at t=0',
  'original_source_complete_odd_sinh_m0_pole_stays_separate':True,
  'original_full_source_residual_real_m_samples':values,
  'original_actual_correlated_residual_uniform_bound_certified':False,
  'original_true_J7_signed_integral_certified':False,
  'original_true_J8_signed_integral_certified':False,
  'original_full_NF410_NF404_signed_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2)+'\n')
 print('NF445 source/native 273 authentic source groups, independent u4(B), 14 correlated Tm/Rm values PASS')
 print('NF445 exact Laplace kernel source representation; quantitative residual J7 J8 RH OPEN')
if __name__=='__main__':calc()
