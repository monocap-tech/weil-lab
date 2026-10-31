#!/usr/bin/env python3
"""NF407: original endpoint logarithm + ALL seven physical prime-jump primitives.

Exact rational enclosures; unmeasured continuous response/cross not silently
replaced by the singular-principal-part calculation.
"""
import argparse,hashlib,json,math,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
P=(2,3,4,5,7,8,9)
PMAP={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
class I:
 def __init__(self,lo,hi=None):
  self.l=F(lo);self.u=F(hi if hi is not None else lo)
  assert self.l<=self.u
 def __add__(a,b):
  if not isinstance(b,I):b=I(b)
  return I(a.l+b.l,a.u+b.u)
 def __radd__(a,b):return a.__add__(b)
 def __neg__(a):return I(-a.u,-a.l)
 def __sub__(a,b):return a+(-b if isinstance(b,I) else -I(b))
 def __rsub__(a,b):return (-a)+b
 def __mul__(a,b):
  if not isinstance(b,I):b=I(b)
  z=[a.l*b.l,a.l*b.u,a.u*b.l,a.u*b.u]
  return I(min(z),max(z))
 def __rmul__(a,b):return a.__mul__(b)
 def __truediv__(a,b):
  if not isinstance(b,I):b=I(b)
  assert b.l>0 or b.u<0
  return a*I(1/b.u,1/b.l)
 def __repr__(a):return f'I({a.l},{a.u})'
 def out(a):return [str(a.l),str(a.u)]
def square(a):
 if a.l<=0<=a.u:return I(0,max(a.l*a.l,a.u*a.u))
 return I(min(a.l*a.l,a.u*a.u),max(a.l*a.l,a.u*a.u))
def sqrt_int(n,dec=45):
 scale=10**dec
 root=math.isqrt(n*scale*scale)
 return I(F(root,scale),F(root+1,scale))
def atanh_log(q):
 """Exact positive rational log(q) with 144-term arctanh and k*log(2)."""
 assert q>0
 k=0
 z=F(q)
 while z<1:z*=2;k-=1
 while z>=2:z/=2;k+=1
 assert 1<=z<2
 def series(v):
  p=(v-1)/(v+1)
  assert 0<=p<=F(1,3)
  summ=2*sum((p**(2*i+1)/F(2*i+1) for i in range(64)),F(0))
  next_power=p**129
  rem=2*next_power/F(129)/(1-p*p)
  return I(summ,summ+rem)
 base=series(z);l2=series(F(2))
 if k<0:return base+(-(-k*l2))
 return base+k*l2
def compact(a,digits):
 scale=10**digits
 lo=(a.l*scale).__floor__()
 hi=(a.u*scale).__ceil__()
 return I(F(lo,scale),F(hi,scale))
def ilog(q):
 return I(atanh_log(q.l).l,atanh_log(q.u).u)
def mx(a,b):return I(max(a.l,b.l),max(a.u,b.u))
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--boundary',default='notes/data/provisional/NF406_original_physical_endpoint_log_exact.json')
 p.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--output',required=True)
 args=p.parse_args()
 seams,s_sha=read(args.seams)
 boundary,b_sha=read(args.boundary)
 center,c_sha=read(args.center)
 assert seams['all_exact_intervals_disjoint'] is True
 assert seams['number_of_open_physical_support_cells']==16
 assert seams['original_signed_prime_powers_all_retained'] is True
 assert boundary['physical_endpoint_log_subtraction_required'] is True
 assert boundary['original_full_supported_centered_scalar_upper_computed'] is False
 assert center['actual_original_full_supported_centered_scalar_integrated'] is False
 assert all(d['W_ODD_NEG']==d['RH']=='OPEN' for d in (seams,boundary,center))
 v=compact(I(*map(F,boundary['original_u4_endpoint_outward'])),55)
 assert v.u<0
 v2=square(v)
 assert B*v2.l<=F(boundary['original_exact_log_model_squared_norm_lower'])
 assert v2.u>0
 assert B*v2.u>=F(boundary['original_exact_log_model_squared_norm_upper'])
 shift={e['n']:e for e in seams['original_prime_power_log_shifts']}
 logs={n:compact(I(F(shift[n]['log_lower']),F(shift[n]['log_upper'])),36) for n in P}
 cs={n:logs[PMAP[n]]/sqrt_int(n) for n in P}
 x={n:(B-logs[n] if logs[n].u<B else logs[n]-B) for n in P}
 assert all(F(0)<x[n].l<=x[n].u<B for n in P)
 # Source origin: u4(B)=v, u4(-B)=-v. Each translated prime
 # n creates TWO interior support jump sites ±x_n, both with jump
 # v*Lambda(n)/sqrt(n) for orientation x increasing. Thus explicit
 # odd step r_n(x)= v*c_n*sgn(x)*1_(|x|>x_n).
 # This removes all seven prime-translated discontinuities from g-q.
 r_squared=I(0)
 for n in P:
  for m in P:
   r_squared+=2*v2*cs[n]*cs[m]*(B-mx(x[n],x[m]))
 # q(x)=v/2 sgn(x)log(B/(B-|x|)).
 # <q,r>=v² sum_n c_n * integral_(x_n)^B log(B/(B-x))dx
 #      =v² sum_n c_n*d_n*(1+log(B/d_n)).
 qr=I(0);terms=[]
 for n in P:
  d=B-x[n]
  assert d.l>0
  ell=ilog(I(B)/d)
  contribution=v2*cs[n]*d*(1+ell)
  qr+=contribution
  terms.append({'n':n,
    'prime_power_base':PMAP[n],
    'signed_mangoldt_weight_positive_interval':cs[n].out(),
    'positive_jump_location_absolute_interval':x[n].out(),
    'source_jump_amplitude_interval':(v*cs[n]).out(),
    'original_cross_q_r_positive_term_interval':contribution.out()})
 qpower=B*v2
 singular_model_power=qpower+r_squared+2*qr
 assert F(15,10**23)<r_squared.l<r_squared.u<F(13,10**22)
 assert F(38,10**23)<qr.l<qr.u<F(4,10**22)
 assert F(21,10**22)<singular_model_power.l<singular_model_power.u<F(22,10**22)
 # Source lower bound for the nonprincipal continuous remainder:
 # ||z||=||g-q-r|| >= ||q+r||-||g|| is NOT a valid lower since ||g||
 # is unknown; do not invent a lower. The original |P_Jg| lower
 # only bounds ||g||, not ||z||.
 out={
  'pass':'NF407',
  'standing':'SOURCE-EXACT ORIGINAL LOG AND SEVEN PRIME DISCONTINUITY PRINCIPAL MODEL; CONTINUOUS RESPONSE UNMEASURED',
  'original_nf406_seams_sha256':s_sha,
  'original_nf406_boundary_sha256':b_sha,
  'original_nf404_center_sha256':c_sha,
  'original_source_u4_endpoint_interval':v.out(),
  'original_log_model_q_power_interval':qpower.out(),
  'original_prime_jump_model_r_power_interval':r_squared.out(),
  'original_signed_q_r_cross_interval':qr.out(),
  'original_known_q_plus_all_seven_prime_jumps_power_interval':singular_model_power.out(),
  'source_true_original_prime_jump_terms':terms,
  'source_r_formula':'r(x)=u4(B)*sgn(x)*sum_{n=2,3,4,5,7,8,9} [Lambda(n)/sqrt(n)]*1_(|x|>abs(B-log(n)))',
  'source_q_formula':'q(x)=u4(B)/2*sgn(x)*log(B/(B-|x|))',
  'source_all_original_prime_jumps_cancelled_from_z':True,
  'source_regularized_continuous_z_formula':'z(x)=1_I[m(D)u4-a*sinh(x/2)]-q(x)-r(x); z has no endpoint log and no prime support jump',
  'source_exact_qr_cross_formula':'u4(B)^2*sum_n c_n*d_n*(1+log(B/d_n)), d_n=B-abs(B-log n)',
  'source_exact_r_power_formula':'2*u4(B)^2*sum_n,m c_n*c_m*(B-max(x_n,x_m))',
  'source_source_specific_operator_identity_general_domain_review':'OPEN',
  'original_continuous_physical_z_squared_norm_measured':False,
  'original_signed_z_qplusr_cross_measured':False,
  'original_full_supported_centered_scalar_upper_computed':False,
  'original_lowband_upper_computed':False,
  'new_signed_kernel_cells':0,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF407 original q power, 7-jump r power, signed qr cross certified by pure Fractions')
 print('NF407 original known q+r power in (2.1e-21,2.2e-21); remaining z energy/cross OPEN')
if __name__=='__main__':main()
