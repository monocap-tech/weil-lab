"""Exact rational E19D pivot obstruction and alternative geometry.
Conditional analytic attachment to E18O positive exponential series.
No numerical evaluation of the choice-defined IV097 bump is used.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt

k=34
h=F(11,3325)
d=F(3,2000*k)
N=50
left=lambda j:-F(11,10)+j*h
collar_lo=F(4393,4000)
collar_hi=F(4399,4000)
assert collar_lo-(left(34)+h)>2
assert (2*N+F(1,2))*d < F(1,225)
assert sum(F(4**j,factorial(j)) for j in range(8))>50
assert F(52,51)**3/50 < F(1,40)
tail=F(51**3,50**50)*F(40,39)
B=F(1,225)**33+tail
binom_norm_sq=comb(66,33)
assert binom_norm_sq > k*(10**85*B)**2
assert binom_norm_sq > k*(10**86*B)**2
print("exact tail:",tail)
print("exact relative row-difference bound:",B)
print("conditional condition number > 10^86")
print("numerical display of lower bound:",sqrt(binom_norm_sq/k)/float(B))

excluded={35,36,76,177,178,245,332,454,455}
assert all(1<=j<=663 and j not in excluded for j in range(629,664))
assert collar_lo-(left(663)+h)==F(829,532000)
assert collar_hi-left(629)>0
assert 35*h < F(693147180,10**9)
# For a preceding-cell surplus, the Cauchy-Binet coefficient reserve
# uses elementary symmetric functions of reciprocals of X_n > 1.
caps=[comb(k,j+1) for j in range(k)]
assert sum(caps)==2**k-1
assert max(caps)==2333606220
print("near pivot: 630..663; surplus: 629")
print("near pivot gap interval:",collar_lo-(left(663)+h),collar_hi-left(630))
print("coefficient l1 reserve:",sum(caps),"max coefficient:",max(caps))
