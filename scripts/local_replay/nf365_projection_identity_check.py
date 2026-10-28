#!/usr/bin/env python3
"""NF365 exact finite-dimensional counterexample only; not native Weil acceptance."""
from fractions import Fraction as Q
for N in [1, 2, 10, 100, 1000]:
    a, b, c = Q(N*N+2), Q(N), Q(2)
    assert a-1>0 and c-1>0 and (a-1)*(c-1)-b*b==1
    v=b/c
    assert b-c*v==0
    assert (a-b*v,b-c*v)==(Q(N*N,2)+2,Q(0))
    assert v==Q(N,2)
print("PASS NF365: exact energy-projection counterexample (NOT original Weil)")
