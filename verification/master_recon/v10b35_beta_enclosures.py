"""Exact centered beta moments and normalized coefficient truncation bounds.
Analytic input: exponential Taylor series and integration on [0,1].
This checker does not claim native attachment to the frozen archive.
"""
from fractions import Fraction as Q
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def beta(j,m):
    # Integral z^j(1-z)^j(2z-1)^(2m), by independent polynomial integration.
    return sum((Q((-1)**(i+k)*comb(j,i)*comb(2*m,k)*2**k,
                  j+i+k+1) for i in range(j+1) for k in range(2*m+1)), Q(0))

def df(n):
    return 1 if n<=0 else n*df(n-2)

def coefficient(j,n):
    # Rodrigues with a=1/4, b=-1/8. Centered even Taylor series.
    pref=Q(2*j+1,4**j*factorial(j))
    terms=[pref*beta(j,m)/ (8**(2*m)*factorial(2*m)) for m in range(n+1)]
    for m,t in enumerate(terms):
        assert t==Q(2*j+1,8**(j+2*m)*2**m*factorial(m)*df(2*j+2*m+1))
        assert t>0
    # First omitted term and a decreasing upper bound for all following ratios.
    r=Q(1,128*(n+1)*(2*j+2*n+3))
    s=sum(terms[:-1],Q(0))
    return s,terms[-1]/(1-r)

for n in (16,17):
    bounds={j:coefficient(j,n) for j in range(15,34,2)}
    assert all(e<=s*Q(1,10**73) for s,e in bounds.values())
    den,ed=bounds[15]
    total=Q(0)
    for j,(s,e) in bounds.items():
        c=s/den
        lo=s/(den+ed); hi=(s+e)/den
        if j==15:
            lo=hi=Q(1)
        assert c-lo<=c*Q(1,10**73) and hi-c<=c*Q(1,10**73)
        total+=max(c-lo,hi-c)
    tail=Q(1,65000)**10/(1-Q(1,65000))
    assert total+tail<Q(1,10**25)
    print(f'{n} retained terms: 10 coefficient enclosures PASS; inner error < 1e-73 relative; combined l1 reserve < 1e-25')
print('180 distinct exact beta moments checked; analytic and frozen archive attachment outstanding')
