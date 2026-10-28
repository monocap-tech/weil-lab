#!/usr/bin/env python3
"""Exact rational arithmetic high-frequency positivity gate for PR356.
Uses the mathematical Binet bound externally justified on Re z>0.
No floating calculations are used in the acceptance inequalities.
"""
from fractions import Fraction as F
from math import isqrt

def series_log_ratio(v,terms=48):
    assert v>0
    u=(v-1)/(v+1)
    assert 0<=u<=F(1,3)
    power=u;total=F(0)
    for k in range(terms):
        total+=2*power/(2*k+1)
        power*=u*u
    residual=2*power/((2*terms+1)*(1-u*u))
    assert residual>=0
    return total,total+residual

def log_interval(n):
    assert n>=1 and isinstance(n,F)
    k=n.numerator.bit_length()-n.denominator.bit_length()
    while (F(2)**k)>n:k-=1
    while (F(2)**(k+1))<=n:k+=1
    assert k>=0
    v=n/(F(2)**k)
    assert 1<=v<2
    l2,h2=series_log_ratio(F(2))
    lv,hv=series_log_ratio(v)
    return k*l2+lv,k*h2+hv

peers=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
S_hi=F(0)
for n,p in peers:
    _,lu=log_interval(F(p))
    sqrtlo=F(isqrt(n*10**16),10**8)
    assert sqrtlo>0 and sqrtlo*sqrtlo<=n
    S_hi+=2*lu/sqrtlo
assert S_hi<F(71,10)
l1300,_=log_interval(F(1300))
assert l1300>F(717,100)
# pi>3, hence 2/(3*pi*1300)<2/(9*1300).
min_hi=l1300-F(71,10)-F(2,9*1300)
assert min_hi>F(1,100)
print('High-tail proof: S<7.1, log(1300)>7.17, m(x)>',float(min_hi),'for all x>=1300, given Binet formula')
