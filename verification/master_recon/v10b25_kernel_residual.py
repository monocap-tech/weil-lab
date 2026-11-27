"""Exact rational replay of the V10B19 regular-kernel Taylor polynomial.
Analytic premises: exp/sinh power-series identities at 0<=r<=1/2.
No floating point in acceptance checks; no Lean or arithmetic adoption.
"""
from fractions import Fraction as Q
from math import factorial as fac
D=28
r=Q(1,2)
ratio=[]
for j in range(D+2):
    ratio.append(Q(1,2**j*fac(j))-sum((ratio[j-k]/fac(k+1) for k in range(2,j+1,2)),Q(0)))
q=[ratio[j+1]/2 for j in range(D+1)]
d=[Q(1,fac(j+1)) if j%2==0 else Q(0) for j in range(D+1)]
a=[(Q(1,2**(j+1)*fac(j+1))-(Q(1,fac(j+2)) if j%2 else 0))/2 for j in range(D+1)]
res=[Q(0)]*(2*D+1)
for i,x in enumerate(d):
    for j,y in enumerate(q):res[i+j]+=x*y
for j,x in enumerate(a):res[j]-=x
assert all(x==0 for x in res[:D+1])
poly_norm=sum(abs(x)*r**j for j,x in enumerate(q))
finite_res=sum(abs(x)*r**j for j,x in enumerate(res))
# Both analytic tails: coefficient absolute value <=1/(j+1)!, j>=29.
# Since r<=1/2, sum_{j>=29} r^j/(j+1)! <=2^-28/30!.
tail=Q(1,2**28*fac(30))
bound=finite_res+(1+poly_norm)*tail
assert poly_norm<1
assert bound<Q(1,2**28)
assert bound<Q(1,10**22)
print('29/29 low residual coefficients vanish')
print('polynomial norm < 1: PASS')
print('residual enclosure < 10^-22: PASS')
print('original 2^-28 budget: PASS')
print('diagnostic approximate bound:',float(bound))
