"""Exact convolution evaluation of the ORIGINAL kernel-difference sum.

Only an algebraically identical evaluation is substituted. All source terms,
orders, error allowances, metrics and physical normalizations are unchanged.
"""
from fractions import Fraction as F
from math import factorial,lcm
import hashlib,inspect
import certify_native_coupled_trial_cc3 as original
from certify_native_exact_hankel import convolution_window
def conv(p,q):
 dp=lcm(*(x.denominator for x in p));dq=lcm(*(x.denominator for x in q))
 a=[int(x*dp) for x in p];b=[int(x*dq) for x in q];n=len(a)+len(b)-1
 ap=[max(x,0) for x in a];an=[max(-x,0) for x in a]
 bp=[max(x,0) for x in b];bn=[max(-x,0) for x in b]
 pp=convolution_window(ap,bp,0,n);nn=convolution_window(an,bn,0,n)
 pn=convolution_window(ap,bn,0,n);np=convolution_window(an,bp,0,n)
 return [F(pp[i]+nn[i]-pn[i]-np[i],dp*dq) for i in range(n)]
def fast_left(p,A):
 # For k>=1: f(j,k)=j! (k-1)!/(j+k)! -1/k.
 # For k=0: f(j,0)=-H_j. Both convolutions keep EVERY j,k product.
 first=conv([x*factorial(j) for j,x in enumerate(p)],[F(0)]+[A[k]*factorial(k-1) for k in range(1,len(A))])
 second=conv(p,[F(0)]+[A[k]/k for k in range(1,len(A))])
 out=[first[s]/factorial(s)-second[s] for s in range(len(first))]
 harm=F(0)
 for j,x in enumerate(p):
  if j: harm+=F(1,j)
  out[j]-=A[0]*x*harm
 return out
def controls():
 checks=0
 for n in (1,2,3,7,13):
  for m in (1,2,5,11):
   p=[F((-1)**j*(j+2),j+1) for j in range(n)]
   A=[F((-1)**k*(k+1),k+3) for k in range(m)]
   slow=[F(0)]*(n+m-1)
   for j,c in enumerate(p):
    for k,a in enumerate(A):slow[j+k]+=c*a*original.regular_difference_factor(j,k)
   assert fast_left(p,A)==slow;checks+=1
 return checks
SOURCE=inspect.getsource(original.source)
OLD='''    left=[F(0)]*(len(p)+len(A)-1)
    for j,c in enumerate(p):
        for k,a in enumerate(A):left[j+k]+=c*a*regular_difference_factor(j,k)
'''
assert SOURCE.count(OLD)==1
NEW=SOURCE.replace('def source(', 'def fast_source(',1).replace(OLD,'    left=fast_left(p,A)\n',1)
scope={**original.__dict__,'fast_left':fast_left}
exec(compile(NEW,__file__,'exec'),scope)
fast_source=scope['fast_source']
original_source_function_sha256=hashlib.sha256(SOURCE.encode()).hexdigest()
if __name__=='__main__':print({'exact_full_difference_convolution_controls':controls()})
