"""V10B37c: rational weighted reserve for the weaker 4^j Legendre envelope.

Conditional on the universal beta identity, finite weighted Taylor
enclosure, coefficient contraction and the uniform Legendre envelope.
No frozen-archive identity or analytic completeness is asserted.
"""
from fractions import Fraction as Q
from math import factorial as f

def B(j,m):
    return Q(f(j)*f(2*m)*f(j+m),f(m)*f(2*j+2*m+1))

def s(j,n):
    return Q(2*j+1,4**j*f(j))*sum(
        (B(j,m)/(8**(2*m)*f(2*m)) for m in range(n)),Q(0))

rho=Q(1,65000)
outer=4**35*rho**10/(1-16*rho)
assert outer<Q(1,10**27)
for n in (16,17):
    eps=Q(2*n+1,8**(2*n)*f(2*n)*2*n)
    assert 0<eps<1
    # Taylor remainder is relative to the positive leading term,
    # hence also relative to the retained positive partial sum.
    for j in range(15,34,2):
        assert s(j,n)>=Q(2*j+1,4**j*f(j))*B(j,0)>0
    # Both numerator and denominator may have two-sided error.
    # If |A-s| <= eps*s and |D-t| <= eps*t then
    # |A/D-s/t| <= 2*eps/(1-eps)*(s/t).
    inner=2*eps/(1-eps)*sum(
        (4**j*s(j,n)/s(15,n) for j in range(15,34,2)),Q(0))
    assert outer+inner<Q(1,10**25)
    print(f'{n} terms: weighted inner {float(inner):.12g}, '
          f'outer {float(outer):.12g}, combined < 1e-25 PASS')
