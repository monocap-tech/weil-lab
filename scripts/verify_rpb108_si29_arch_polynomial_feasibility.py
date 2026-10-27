#!/usr/bin/env python3
"""Bounded cost test; stop the fixed-4096-bit global monomial implementation."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import flint
from flint import arb,ctx
FRAME_SHA='87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f'
NATIVE_SHA='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
B=F(11,10)
def dy(x):
 n,e=x.man_exp();return [str(n),int(e)]
def good(K,t):
 n=K+1
 return t.numerator**n*2**80 < factorial(n)*t.denominator**n

def main():
 p=argparse.ArgumentParser();p.add_argument('--certificate',required=True);p.add_argument('--frame-certificate',required=True);p.add_argument('--output',default='artifacts/si29_arch_polynomial_feasibility.json');a=p.parse_args();start=time.monotonic()
 raw=Path(a.certificate).read_bytes();fr=Path(a.frame_certificate).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==NATIVE_SHA and hashlib.sha256(fr).hexdigest()==FRAME_SHA
 z=json.loads(raw);frame=json.loads(fr)
 assert flint.__version__=='0.8.0' and z['working_precision_bits']==4096
 assert frame['physical_Gram_lower']=='99/100' and frame['physical_Gram_upper']=='101/100'
 c=max(F(c) for c,p in z['original_source_nodes'])
 assert any(F(center)==c and order>=1 for center,order in z['original_source_nodes'])
 assert c==F(113013,128) # actual original k=0 sine, not an invented test source
 # Whole normalized-frame pointwise operator error <=1/3 implies raw source
 # error <1/2: ||v|| <=sqrt(2B/(99/100)) <3/2, J_high=Uv.
 assert 2*B/F(99,100)<F(9,4)
 peak_argument=4*B*c
 # Equivalently floor((4Bc+1)/2), with exact rational arithmetic.
 count=int((peak_argument+1)/2)
 lower_degree=2*count-1
 assert count==1942 and lower_degree==3883
 last=F(2*count-1,4)/c;next_peak=F(2*count+1,4)/c
 assert 0<last<=B<next_peak
 # Real-variable Taylor/Lagrange remainder, not a necessary actual degree.
 t=F(44,7)*B*c;lo=0;hi=20000
 while lo<hi:
  mid=(lo+hi)//2
  if good(2*mid+1,t):hi=mid
  else:lo=mid+1
 K=2*lo+1;assert K==16643 and good(K,t) and not good(K-2,t)
 n=(K+1)//2
 # One coefficient in that raw-source polynomial. Independent coefficient
 # interval evaluation at x/B=1 has radius at least this single radius.
 k=2*(int(t)//2)+1;ctx.prec=4096
 omegaB=2*arb.pi()*arb(str(B*c));coef=omegaB**k/factorial(k)
 assert coef.rad()>arb(2)**4700
 result=dict(status='SCOPED_FIXED_4096_GLOBAL_MONOMIAL_IMPLEMENTATION_STOP',
   native_input_sha256=NATIVE_SHA,frame_input_sha256=FRAME_SHA,
   actual_source_frequency=str(c),source_kind='sin(2*pi*c*x)',source_power=0,
   physical_half_width=str(B),normalized_frame_uniform_error_target='1/3',
   raw_source_coefficient_norm_squared_upper=str(2*B/F(99,100)),
   positive_extremum_count=count,total_alternating_extrema=2*count,
   necessary_uniform_polynomial_degree=lower_degree,
   raw_Taylor_Lagrange_target='1/'+str(2**80),angular_argument_rational_upper=str(t),
   first_odd_degree_passing_raw_Lagrange_bound=K,
   normalized_trial_Taylor_remainder_certified=False,
   odd_polynomial_dimension=n,dense_universal_odd_Gram_entries=n*n,
   independent_symmetric_odd_Gram_entries=n*(n+1)//2,
   working_precision_bits=4096,flint_version=flint.__version__,
   tested_Taylor_coefficient_degree=k,coefficient_midpoint_dyadic=dy(coef.mid()),
   coefficient_radius_dyadic=dy(coef.rad()),
   coefficient_radius_strict_lower_power_of_two=4700,
   implementation_ceiling='4096-bit raw Taylor coefficient boxes evaluated independently at x/B=1 cannot certify even unit error',
   conclusion='STOP this fixed-precision global monomial implementation before large matrix assembly; reassess representation and full cost',
   alternative_polynomial_representations_ruled_out=False,
   actual_arch_mixed_matrix_computed=False,full_coupling_route_proved_impossible=False,
   higher_precision_campaign_launched=False,
   W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
 print('SCOPED STOP PASS: necessary degree >=3883; raw Lagrange degree16643; 4096-bit coefficient radius >2^4700; seconds',round(result['elapsed_seconds'],3))
if __name__=='__main__':main()
