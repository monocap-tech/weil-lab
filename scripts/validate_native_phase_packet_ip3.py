#!/usr/bin/env python3
"""IP3: exact-rational quotient/packet controls. NOT actual zeta computation."""
from fractions import Fraction as F

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(a,x): return [dot(r,x) for r in a]
def sub(a,b): return [x-y for x,y in zip(a,b)]

checks = 0
# Nontrivial positive source M: outgoing shell not canonical coordinate shell.
M = [[F(2),F(1)],[F(1),F(2)]]
Minv = [[F(2,3),F(-1,3)],[F(-1,3),F(2,3)]]
j = [F(0),F(1)]
u = mv(Minv,j)
assert u == [F(-1,3),F(2,3)]; checks+=1
assert dot(u,mv(M,[F(1),F(0)])) == 0; checks+=1
assert dot(j,u) == F(2,3); checks+=1
w=[F(-1,2),F(1)]
assert dot(w,mv(M,[F(1),F(0)])) == 0; checks+=1
assert dot(w,mv(M,w)) == F(3,2); checks+=1
assert dot(j,w)**2/dot(w,mv(M,w)) == F(2,3); checks+=1
for alpha in [F(0),F(1),F(-3,4),F(11,7)]:
    old=[alpha,F(0)]
    d=sub(u,old)
    assert dot(d,mv(M,d)) == F(2,3)+F(2)*alpha*alpha
    checks+=1
    err = sub(j,mv(M,old))
    assert dot(err,mv(Minv,err)) == F(2,3)+F(2)*alpha*alpha
    checks+=1

# Original-style complete negative analysis, one old generalized eigenvector.
a=F(3,4); lam=a*a; delta=1-lam
j_signed=[F(0),-lam]
assert lam == F(9,16) and delta==F(7,16); checks+=1
assert dot(j_signed,j_signed)==F(81,256); checks+=1
assert dot(j_signed,j_signed)/lam==F(9,16); checks+=1
assert (dot(j_signed,j_signed)/lam)/delta == F(9,7); checks+=1

# Unobserved shell-tail, positive metric, full inverse.
M3=[[F(1),F(0),F(1,2)],[F(0),F(1),F(1,2)],[F(1,2),F(1,2),F(1)]]
Mi3=[[F(3,2),F(1,2),F(-1)],[F(1,2),F(3,2),F(-1)],[F(-1),F(-1),F(2)]]
j3=[F(0),F(1),F(1)]; z=[F(0),F(1),F(0)]
assert dot(z,mv(M3,[F(1),F(0),F(0)]))==0; checks+=1
lower=dot(z,mv(M3,z)); full=dot(j3,mv(Mi3,j3))
assert lower==F(1) and full==F(3,2); checks+=1
res=sub(j3,mv(M3,z))
assert res==[F(0),F(0),F(1,2)]; checks+=1
assert dot(res,mv(Mi3,res)) == F(1,2); checks+=1
assert lower+dot(res,mv(Mi3,res)) == full; checks+=1
assert lower <= full <= lower+F(4)*dot(res,res); checks+=1

print(f'RPB108 IP3 exact rational controls: {checks} passed')
