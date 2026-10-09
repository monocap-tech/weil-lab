#!/usr/bin/env python3
"""NON-CERTIFYING NF23 check: stable endpoint logs and transformed
endpoint quadrature; all floating point output remains diagnostic only."""
import sys,math,json
sys.path.insert(0,'scripts')
import diagnose_native_complete_source_low2_nf22_106 as d
from scipy.integrate import quad

def J(t):
 u=math.exp(-t/2)
 return .5*(math.log1p(u)-math.log(-math.expm1(-t/2)))+math.atan(u)

out={}
for j in (0,1):
 total=0.;error=0.
 for idx,(l,u) in enumerate(zip(d.cutpoints,d.cutpoints[1:])):
  mid=(l+u)/2
  selected=[(s*math.log(n),d.weights[n]) for n in d.active for s in (-1,1) if abs(mid+s*math.log(n))<d.a]
  def f(y):
   if idx==0:
    z=(u-l)*y**4;x=-d.a+z;tm=2*d.a-z;tp=z;jac=4*(u-l)*y**3
   elif idx==12:
    z=(u-l)*y**4;x=d.a-z;tm=z;tp=2*d.a-z;jac=4*(u-l)*y**3
   else:x=l+(u-l)*y;tm=d.a-x;tp=d.a+x;jac=u-l
   if y==0 and idx in (0,12):return 0.
   U=d.alpha+J(tm)+J(tp)
   arch=d.C0*U if j==0 else d.C1*(x*U+d.F_regular(tp)-d.F_regular(tm))
   prime=-sum(w*(d.C0 if j==0 else d.C1*(x+t)) for t,w in selected)
   return (arch+prime+d.pole(x,j))**2*jac
  q,e=quad(f,0,1,epsabs=2e-14,epsrel=2e-14,limit=300)
  total+=q;error+=e
 out['even' if j==0 else 'odd']={'source_square':total,'estimated_quadrature_error':error}
print(json.dumps(out,indent=2))
