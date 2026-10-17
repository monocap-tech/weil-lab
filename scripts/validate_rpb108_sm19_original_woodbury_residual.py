#!/usr/bin/env python3
"""SM19: two-dimensional rational Woodbury and residual prototype only."""
from fractions import Fraction as F

def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return [list(col) for col in zip(*a)]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(a,c): return [[c*x for x in r] for r in a]
def spd(a):
    return a[0][0]>0 and a[0][1]==a[1][0] and a[0][0]*a[1][1]>a[0][1]**2
def inv(a):
    assert spd(a)
    d=a[0][0]*a[1][1]-a[0][1]**2
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]

I=[[F(1),F(0)],[F(0),F(1)]]
G=[[F(1)],[F(0)]]
s=[[F(1,4)],[F(0)]]
gamma=F(2)
C=add(I,sc(mul(G,tr(G)),gamma))
B=sub(C,sc(mul(s,tr(s)),2))
K=1/gamma+mul(tr(G),G)[0][0]
q=mul(tr(G),s)[0][0]
alpha=1-2*(mul(tr(s),s)[0][0]-q*q/K)
assert alpha==F(23,24) and spd(sub(B,sc(I,alpha)))
Ci=sub(I,sc(mul(G,tr(G)),1/K))
z0=mul(Ci,s)
Bi=add(Ci,sc(mul(z0,tr(z0)),2/alpha))
assert Bi==inv(B)

A=[[F(4),F(1,3)],[F(1,3),F(2)]]
Y=[[F(1,4),F(0)],[F(0),F(1,2)]]
assert spd(sub(A,B))
E=sub(I,mul(A,Y))
H=sub(add(Y,tr(Y)),mul(mul(tr(Y),A),Y))
D=mul(tr(E),E)
R=mul(tr(G),E)
t=mul(tr(E),s)
z=sub(t,sc(mul(tr(R),[[q]]),1/K))
low_data=sub(D,sc(mul(tr(R),R),1/K))
err=add(low_data,sc(mul(z,tr(z)),2/alpha))
assert err==mul(mul(tr(E),Bi),E)
real=inv(A)
ref=add(H,err)
scalar=add(H,sc(D,1/alpha))
assert real==add(H,mul(mul(tr(E),real),E))
assert spd(sub(ref,real)) and spd(sub(scalar,ref))
print("SM19 PASS: exact coupled finite-data reference improvement")
print("alpha",alpha,"residual",E,"gap",sub(scalar,ref))
print("Original 890-source data and W-ODD-NEG remain OPEN.")
