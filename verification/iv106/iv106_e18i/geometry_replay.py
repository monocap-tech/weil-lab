#!/usr/bin/env python3
"""Exact rational buffered geometry for the E18A/B trial bank, not a Lean receipt."""
from fractions import Fraction as F

N=665
a=F(11,10)
h=2*a/N
collar=(F(4393,4000),F(4399,4000))
D=10**12
def log_bounds(n):
    t=F(n-1,n+1)
    s=2*sum((t**(2*j+1)/F(2*j+1) for j in range(80)),F(0))
    hi=s+2*t**161/(161*(1-t*t))
    return F((s*D).__floor__(),D), F((hi*D).__ceil__(),D)
logs={n:log_bounds(n) for n in (2,3,4,5,7,8,9)}
forbidden=[collar]+[(collar[0]-hi,collar[1]-lo) for lo,hi in logs.values()]+[(collar[0]+lo,collar[1]+hi) for lo,hi in logs.values()]
rows={}
for j in range(1,N-1):
    l,r=-a+j*h,-a+(j+1)*h
    d=min([l+a,a-r]+[max(lo-r,l-hi) for lo,hi in forbidden])
    if d>0:
        rows[j]=d
assert len(rows)==654
assert sorted(set(range(1,N-1))-rows.keys())==[35,36,76,177,178,245,332,454,455]
dstar=F(50400028827,133000000000000)
assert min((d,j) for j,d in rows.items())==(dstar,246)
eps=dstar/2
for j in rows:
    l,r=-a+j*h-eps,-a+(j+1)*h+eps
    assert -a<l<r<a
    assert all(max(lo-r,l-hi)>=eps for lo,hi in forbidden)
print("654 cells; common enlargement",eps,"; minimum residual gap",eps)
print("Exact rational buffered geometry PASS")
