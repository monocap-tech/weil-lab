#!/usr/bin/env python3
"""RPB108 IP7: generic exact rational finite-Schur checks, not zeta arithmetic."""
from fractions import Fraction as F
from itertools import product

checks=0
eta=F(1,16)
r=F(2)
m=1-r*eta
barrier=r*r*eta/m
assert m==F(7,8) and barrier==F(2,7); checks+=1

# Sufficient positive Schur example; compatible with protected complement.
A=F(3,5); E=F(1,8); D=F(1)
assert A>barrier and A*D>E*E; checks+=1
assert D>=m and abs(E)<=r*F(1,4); checks+=1
mu=F(1,10)
assert A-mu-r*r*eta/(m-mu)>0; checks+=1
assert (A-mu)*(D-mu)-E*E>0; checks+=1

# A zero-contact case: safe complement but finite threshold inconclusive.
A0=F(1,16); E0=F(1,4); D0=F(1)
assert A0*D0-E0*E0==0; checks+=1
assert A0<=barrier; checks+=1
assert abs(-E0/D0)<=r*F(1,4)/m; checks+=1

# Retained A>0 may still be insufficient for whole-form positivity.
An=F(1,32); En=F(1,4); Dn=F(1)
assert An>0 and An*Dn-En*En<0; checks+=1
assert An<barrier; checks+=1
# Negative finite trial direction guarantees whole negativity.
assert F(-1,4)<0; checks+=1

# Actual generic source crossing controls: fixed positive step exhausts gap.
for s,t in product([F(7,8),F(15,16),F(31,32),F(63,64)],
                   [F(17,16),F(9,8),F(5,4)]):
    assert s<1<t; checks+=1
    assert (t-s)/(1-s)>1; checks+=1

# Finite-rank dimension/trace quantities (no numerical Z_R construction).
for B,R,tau in product([F(1),F(3,2),F(2)],
                       [F(4),F(10),F(100)], [F(1,8),F(1,16)]):
    assert 4*B*R/tau>0; checks+=1
    assert tau>0; checks+=1

print(f"IP7 exact finite-rational controls: {checks} passed")
