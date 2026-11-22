#!/usr/bin/env python3
"""Finite UOI042 arithmetic/scope sanity checks; NOT a Lean or asymptotic proof."""
import math
from sympy import primerange

eps=1/4000
for d in range(4,9):
    n=8**d
    lo=math.ceil(n*math.exp(-eps))
    hi=math.floor(n*math.exp(eps))
    ps=list(primerange(lo, hi+1))
    s2=sum(math.log(p)**2/p for p in ps)
    s=math.sqrt(s2)
    qbound_scale=n*(1/math.sqrt(n))**7   # constants omitted; O(N^-5/2)
    assert abs(qbound_scale-n**(-2.5))<1e-12
    w=1/(10000*n)
    delta_d=1/(1000*n)
    assert w<delta_d
    assert eps+w<1/1000
    # Integer-log spacing across the chosen interval:
    for p in ps:
        # logarithmic separation from any other positive integer n:
        sep=min(math.log((p+1)/p), math.log(p/(p-1)))
        assert 4*w<sep
        assert abs(math.log(p/n))+w<1/1000
    print(f'd={d} N={n} primes={len(ps)} sqrt(sum weight²)={s:.9f} '
          f'PNT leading={math.sqrt(2*eps*math.log(n)):.9f} '
          f'low-frequency scale N^-5/2={n**(-2.5):.3e}')
print('Finite checks PASS; asymptotic PNT, digamma and Fourier bounds require the written proof.')