"""Rebuild only the exact ORIGINAL SM40 step weights; no moment LDL or scout.

SM39's rational-left midpoint candidate is no greater than SM37's integer-left
candidate, so the same final weight is min(parent, SM39 candidate, SM40 candidate).
The independent checker reconstructs all three stages explicitly.
"""
import json,time
from fractions import Fraction as F
from functools import lru_cache
from validate_rpb108_si06_negative_band import PI,WEIGHTS,SHIFTS,YFAC,CONST_UP,prime_interval,log_rational_bounds
from validate_rpb108_si07_negative_support_cover import arch_lower_cell
from validate_rpb108_si08_multiband_rank import taylor_order
D2=8*PI[1]**2*sum((WEIGHTS[n][1]*SHIFTS[n][1]**2 for n in WEIGHTS),F(0))
@lru_cache(None)
def arch(a):
 y=YFAC*a;q=F(1,4)
 return sum((y*y/((k+q)*((k+q)**2+y*y)) for k in range(64)),F(0))+log_rational_bounds(1+(y/F(257,4))**2)[0]/2-CONST_UP

def build(neg):
 out=[];mass=F(0);start=time.monotonic();idx=0
 def weight(low):
  need=max(F(0),F(1,1000)-low);return max(F(1,10**6),F(-(- (need*10**6).numerator//(need*10**6).denominator),10**6))
 for l,r,h in [tuple(map(F,row)) for row in neg['original_leaf_witnesses']]:
  for i in range(4):
   a=l+(r-l)*F(i,4);b=l+(r-l)*F(i+1,4);v=arch(a)
   assert v>=arch_lower_cell(int(a))
   w39=weight(v+prime_interval((a+b)/2)[0]-69*(b-a)/2)
   w40=weight(v+min(prime_interval(a)[0],prime_interval(b)[0])-D2*(b-a)**2/8)
   w=min(h+F(1,1000),w39,w40)
   out.append((a,b,w));mass+=2*(b-a)*w
   if len(out)%500==0:print('Weights',len(out),'seconds',round(time.monotonic()-start,2),flush=True)
   if time.monotonic()-start>60:raise RuntimeError('Bounded 60-second weight cost guard')
 assert len(out)==3892 and mass==F(1073441879,64000000),(len(out),mass)
 return out,mass
