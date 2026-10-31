#!/usr/bin/env python3
"""NF406 exact ORIGINAL seven-prime physical support seam partition.

No numerical log/float. Rational arctanh series encloses all log(n);
enumerates all fourteen ±(B-log n) seam locations, plus -B,0,+B.
Output supports future rigorously partitioned signed physical x integral.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);N=128;PRIMES=(2,3,4,5,7,8,9)
def read(p):
 d=Path(p).read_bytes();return json.loads(d),hashlib.sha256(d).hexdigest()
def log_interval(n):
 z=F(n-1,n+1)
 assert 0<z<1
 lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
 rem=2*z**(2*N+1)/F((2*N+1)*(1-z*z))
 hi=lo+rem
 assert 0<lo<hi
 return lo,hi
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--physical',default='notes/data/provisional/NF405_original_compact_physical_kernel_exact.json')
 p.add_argument('--boundary',default='notes/data/provisional/NF406_original_physical_endpoint_log_exact.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 phys,psha=read(a.physical)
 bound,bsha=read(a.boundary)
 assert phys['original_compact_translation_integral_upper']=='22/5'
 assert phys['actual_original_prime_power_shifts']==list(PRIMES)
 assert bound['physical_endpoint_log_subtraction_required'] is True
 assert bound['original_complete_regular_part_and_cross_integrated'] is False
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in (phys,bound))
 x=[dict(label='-B',low=-B,high=-B)]
 x.append(dict(label='0',low=F(0),high=F(0)))
 x.append(dict(label='+B',low=B,high=B))
 shifts=[]
 for n in PRIMES:
  lo,hi=log_interval(n)
  assert F(0)<lo<hi<2*B
  assert hi-lo<F(1,10**20)
  rlo,rhi=B-hi,B-lo
  x.append(dict(label=f'B-log({n})',low=rlo,high=rhi))
  x.append(dict(label=f'-B+log({n})',low=-rhi,high=-rlo))
  shifts.append({'n':n,'log_lower':str(lo),'log_upper':str(hi),
                 'positive_shift_crossing_lower':str(rlo),
                 'positive_shift_crossing_upper':str(rhi),
                 'overlap_length_lower':str(2*B-hi),
                 'overlap_length_upper':str(2*B-lo)})
 x.sort(key=lambda z:z['low']+z['high'])
 assert len(x)==17
 assert all(x[i]['high']<x[i+1]['low'] for i in range(16))
 assert x[0]['label']=='-B' and x[-1]['label']=='+B'
 # closest seams near middle are ±(B-log 3), and nearest original
 # physical support ends are ±(B-log 9), as source exact conditions.
 middle=x[7:10]
 assert [z['label'] for z in middle]==['-B+log(3)','0','B-log(3)']
 assert x[1]['label']=='B-log(9)' and x[-2]['label']=='-B+log(9)'
 n3=next(v for v in shifts if v['n']==3)
 n9=next(v for v in shifts if v['n']==9)
 assert F(1,1000)<F(n3['positive_shift_crossing_lower'])<F(n3['positive_shift_crossing_upper'])<F(2,1000)
 assert F(2,1000)<F(n9['overlap_length_lower'])<F(n9['overlap_length_upper'])<F(3,1000)
 out={
  'pass':'NF406','standing':'EXACT ORIGINAL SEVEN PRIME POWER SIGNED TRANSLATE SUPPORT PARTITION; NO PHYSICAL INTEGRATION',
  'original_nf405_compact_kernel_sha256':psha,
  'original_nf406_endpoint_log_sha256':bsha,
  'original_support_half_width':str(B),
  'exact_log_n_method':'2*sum_{k=0}^{127} z^(2k+1)/(2k+1) < log n < that + 2*z^257/(257*(1-z²)); z=(n-1)/(n+1)',
  'all_exact_intervals_disjoint':True,
  'total_original_support_seam_knots_including_ends_and_zero':len(x),
  'number_of_open_physical_support_cells':len(x)-1,
  'original_prime_power_log_shifts':shifts,
  'certified_ordered_knots':[{'label':r['label'],'low':str(r['low']),'high':str(r['high'])} for r in x],
  'original_3_seam_near_zero_b_minus_log3_bounds':[n3['positive_shift_crossing_lower'],n3['positive_shift_crossing_upper']],
  'original_9_shift_tiny_support_overlap':[n9['overlap_length_lower'],n9['overlap_length_upper']],
  'original_signed_prime_powers_all_retained':True,
  'original_regularized_physical_integrand_piecewise_integrated':False,
  'original_complete_centered_positive_physical_scalar_measured':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF406 exact 17 original knots -> 16 physical prime-seam cells; no floats PASS')
 print('NF406 near-zero n=3 and tiny original n=9 edge overlap accepted')
 print('NF406 complete original centered physical scalar still UNMEASURED')
if __name__=='__main__':main()
