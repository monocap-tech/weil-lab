#!/usr/bin/env python3
"""RPB108 IP4: exact rational source-shell tests; no actual zeta eigenvector."""
from fractions import Fraction as F

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(m,x): return [dot(row,x) for row in m]
def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b): return [a[i]-b[i] for i in range(len(a))]
checks=0
M=[[F(1),F(1,2),F(0)],[F(1,2),F(1),F(0)],[F(0),F(0),F(1)]]
Mi=[[F(4,3),-F(2,3),F(0)],[-F(2,3),F(4,3),F(0)],[F(0),F(0),F(1)]]
I=[[F(int(i==j)) for j in range(3)] for i in range(3)]
assert matmul(M,Mi)==I; checks+=1
assert matmul(Mi,M)==I; checks+=1
n=[F(3,4)]*3
h=[F(1),F(0),F(0)]
lam=dot(n,h)**2/dot(h,mv(M,h))
delta=1-lam
assert lam==F(9,16) and delta==F(7,16); checks+=1
# Full forced original source row Q(h,.)-delta<Mh,.>
j=sub([lam*v for v in mv(M,h)],[dot(n,h)*v for v in n])
assert j==[F(0),-F(9,32),-F(9,16)]; checks+=1
assert dot(j,h)==0; checks+=1
z2=[-F(1,2),F(1),F(0)]
z3=[F(0),F(0),F(1)]
assert dot(z2,mv(M,h))==0; checks+=1
assert dot(z3,mv(M,h))==0; checks+=1
assert dot(z2,mv(M,z2))==F(3,4); checks+=1
assert dot(z3,mv(M,z3))==F(1); checks+=1
assert dot(z2,mv(M,z3))==0; checks+=1
assert dot(j,z2)==-F(9,32); checks+=1
assert dot(j,z3)==-F(9,16); checks+=1
right=dot(j,z2)**2/dot(z2,mv(M,z2))
left=dot(j,z3)**2/dot(z3,mv(M,z3))
full=dot(j,mv(Mi,j))
assert right==F(27,256); checks+=1
assert left==F(81,256); checks+=1
assert right+left==F(27,64); checks+=1
assert full==right+left; checks+=1
assert full/lam==F(3,4); checks+=1
assert (full/lam)/delta==F(12,7); checks+=1
q=[[M[i][k]-n[i]*n[k] for k in range(3)] for i in range(3)]
assert dot(h,mv(q,h))==delta; checks+=1
assert dot([F(1)]*3,mv(q,[F(1)]*3))==-F(17,16); checks+=1
# Supremum of finite outgoing dual energy: both sides needed.
assert right<full and left<full; checks+=1
print(f"RPB108 IP4 exact rational controls: {checks} passed")
