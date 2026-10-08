"""Fixed odd frame source, with exact batched translation interval sums.

Same original odd source, truncations140/180 and gamma56 as CC17. Grid400
and coefficient150 are explicitly paid. Batching clears rational input
denominators and sums interval endpoints as integers before one rounding.
"""
from functools import lru_cache
from fractions import Fraction as F
from math import comb,lcm,factorial
import certify_native_coupled_trial_cc3 as original
from certify_native_rich_action_cc14 import I,D,sqrt_rational,mid
from native_terminal_odd_source_cc17 import CODE,controls as odd_controls

@lru_cache(None)
def rational_composition(p,shift,scale):return tuple(original.compose(p,shift,scale))

def compose_batched(p,shift,scale=F(1)):
 # Interval powers enclose the same true shift for every coefficient.
 if not isinstance(shift,I):return list(rational_composition(tuple(p),shift,scale))
 powers=[I(1)]
 for _ in range(len(p)-1):powers.append(powers[-1]*shift)
 den=lcm(*(x.denominator for x in p));coeff=[int(x*den) for x in p]
 endpoints=[(int(x.lo*I.grid),int(x.hi*I.grid)) for x in powers]
 out=[]
 for k in range(len(p)):
  lo=hi=0
  for n in range(k,len(p)):
   c=coeff[n]*comb(n,k);a,b=endpoints[n-k]
   lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
  out.append(I(F(lo,den*I.grid),F(hi,den*I.grid))*scale**k)
 return out

scope={**original.__dict__,'fast_left':__import__('native_rich_action_fast_source_cc14').fast_left,'compose':compose_batched}
scope['bernoulli']=lru_cache(None)(scope['bernoulli'])
atan=scope['atan']
scope['atan']=lru_cache(None)(atan)
FRAME_CODE=CODE.replace('def odd_source(', 'def frame_source(',1).replace('grid=10**250','grid=10**150')
assert FRAME_CODE!=CODE
exec(compile(FRAME_CODE,__file__,'exec'),scope)
frame_source=scope['frame_source']

def frame_error(p,M0,M1,regs,constant_radius):
 degree=len(p)-1
 assert I.grid==10**400 and 0< M0<100 and degree<=143 and len(regs)==13 and max(map(len,regs))<1000
 assert sum(map(abs,p),F(0))<=M0*8**degree and M1<=143*144*M0
 # The original finite-order operation bound is retained; all integer
 # batched endpoint sums reduce rounding, and no input error is removed.
 operations=10**30*M0*16**degree/I.grid
 rounding=F(1000,10**150)
 N,K=140,180
 ce=F(23,10)*(D/2)**(N+1)/factorial(N+1);cb=4*(D/3)**(2*K+2)/(1-(D/3)**2)
 he=ce/(N+1)+cb/(2*K+2);ae=ce/(N+2)+cb/(2*K+3)
 pole=2*(D/4)**(N+1)/factorial(N+1)
 # A common scalar constant uncertainty multiplies the physical p.
 # The coefficient floor and EVERY nonconstant fixed-grid operation are
 # paid separately. The whole original gamma/log interval remains.
 uniform=2*M0*he+2*M1*ae+100*D*M0*pole+M0*constant_radius+operations+rounding
 return sqrt_rational(D).hi*uniform

def controls():
 count=odd_controls()
 for degree in (1,3,7,13):
  p=[F((-1)**j*(j+1),j+2) for j in range(degree+1)]
  for a,b in [(F(-2,7),F(-2,7)),(F(1,3),F(1,3)+F(1,10**70))]:
   actual=compose_batched(p,I(a,b));naive=original.compose(p,I(a,b))
   for x,y in zip(actual,naive):assert max(x.lo,y.lo)<=min(x.hi,y.hi);count+=1
   for z in (a,b):
    exact=original.compose(p,z)
    for x,y in zip(actual,exact):assert x.lo<=y<=x.hi;count+=1
 return count

if __name__=='__main__':
 import time
 I.grid=10**400;start=time.monotonic();print({'controls':controls()})
 n=113;nz=mid(sqrt_rational(F(2*n+1)/D));p=[nz*x for x in original.shifted_legendre(n)[n]]
 regs,e,pi,geom=frame_source(p,nz,nz*n*(n+1))
 from native_rich_action_source_error_cc14 import constant_radius
 er=frame_error(p,nz,nz*n*(n+1),regs,constant_radius(pi))
 print({'degree':n,'seconds':time.monotonic()-start,'physical_error':float(er),'regular_degree':max(map(len,regs))-1})
