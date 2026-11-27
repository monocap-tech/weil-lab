"""V10B40b: finite low-mode deflation budget, no infinite expansion.

All numeric assertions use rational arithmetic. Analytic obligations:
literal Rodrigues projection, finite polynomial span/orthogonality,
the Taylor remainder, and the coarse Legendre envelope.
Frozen-archive coefficient identity is not asserted.
"""
from fractions import Fraction as Q
from math import factorial as f, prod

def df(n):
    return prod(range(1,n+1,2))

def s(j,n):
    return sum((Q(2*j+1,8**(j+2*m)*2**m*f(m)*df(2*j+2*m+1))
                for m in range(n)),Q(0))

n=64
eps=Q(n+1,8**n*f(n)*n)
d=Q(7,8)*Q(31,8**15*df(31))
M=sum((2*j+1)*16**j for j in range(14))
projection=eps*(1+M)/d
assert projection<Q(1,10**100)
# Exact degree-63 Taylor projections, after odd reflection and deflation.
C={j:s(j,(64-j+1)//2) for j in range(15,64,2)}
D=C[15]
# |A15-D| <= 31*4^15*eps, directly from the literal projection.
ed=31*4**15*eps
assert D-ed>=d
norm=sum((4**j*C[j]/D for j in C),Q(0))
denerr=ed/d*norm
assert denerr<Q(1,10**97)
for n in (16,17):
    F={j:s(j,n)/s(15,n) for j in range(15,34,2)}
    diff=sum((4**j*abs(C[j]/D-F.get(j,0)) for j in C),Q(0))
    total=projection+diff+denerr
    assert total<Q(1,10**30)
    assert total<Q(1,10**25)
    print(n,'retained terms: low projection',float(projection),
          'finite comparison',float(diff),'denominator',float(denerr),
          'combined',float(total),'PASS')
