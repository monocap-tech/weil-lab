#!/usr/bin/env python3
"""Exact rational sanity check of the scalar/rank-one identities on real sample vectors.
Not an audit of the actual IV106 operator, spectrum, or Gram."""
from fractions import Fraction as F
c=F(5003,5000)
lam=c/(c+20)
assert lam==F(5003,105003)
assert (1-lam)*c==20*lam and 1/lam<21
dot=lambda a,b:sum((x*y for x,y in zip(a,b)),F(0))
q=[lam,2*lam,5*lam]
p=list(map(F,[1,2,-1]))
g=list(map(F,[2,-1,3]))
T=lambda a:[x/y for x,y in zip(a,q)]
h=dot(p,T(p))+1/(2*lam)
v=dot(p,T(g))
z=v/h
u=[x-z*y for x,y in zip(T(g),T(p))]
Bu=[qi*ui+2*lam*pi*dot(p,u) for qi,ui,pi in zip(q,u,p)]
assert Bu==g
R=dot(g,T(g))-v*v/h
assert R==dot(g,u)
assert 0<=R<=dot(g,g)/lam<21*dot(g,g)
for t in map(F,[-2,-1,0,1,2]):
    zz=z+t
    r=[gi-zz*pi for gi,pi in zip(g,p)]
    assert dot(r,T(r))+zz*zz/(2*lam)==R+h*t*t
print("exact rational rank-one identities PASS (sample only)")
