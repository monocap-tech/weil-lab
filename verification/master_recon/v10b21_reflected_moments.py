"""Exact independent comparison of reflected and harmonic log moments.
No floating point, no numerical quadrature, no analytic adoption.
For k=0..512 this checks the two right-endpoint moments used by
the V10B19 polynomial/log Gram generator. The finite bound is a
verification range, not a proof of a universal harmonic identity.
"""
from fractions import Fraction as Q
from math import comb
H=Q(0)
H2=Q(0)
for k in range(513):
    n=k+1
    H+=Q(1,n)
    H2+=Q(1,n*n)
    a=sum((Q((-1)**j*comb(k,j),(j+1)**2) for j in range(n)),Q(0))
    b=sum((Q(2*(-1)**j*comb(k,j),(j+1)**3) for j in range(n)),Q(0))
    assert a==H/n,(k,1)
    assert b==(H*H+H2)/n,(k,2)
print("1026/1026 exact rational reflected/harmonic moment comparisons PASS")
