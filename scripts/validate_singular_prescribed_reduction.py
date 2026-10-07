#!/usr/bin/env python3
"""Exact singular prescribed covariance/physical-padding controls."""
from fractions import Fraction as F
from itertools import product
import json

def tr(a): return [list(v) for v in zip(*a)]
def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(a,b,sign=1):
    return [[x+sign*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,s): return [[s*x for x in row] for row in a]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def zero(n,m): return [[F(0) for j in range(m)] for i in range(n)]
def sq(v): return sum(row[0]**2 for row in v)

def main():
    count=padding=0
    for (c,s),r,t,zeta,v in product(
        ((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13))),
        (F(1,2),F(1),F(2)),(F(1),F(2),F(3)),
        (F(0),F(1,2),F(2)),(F(-2),F(0),F(3))):
        P=[[r*c,r*s,F(0)],[F(0),F(0),t],[F(0),F(0),F(0)]]
        R=[[r,F(0),F(0)],[F(0),F(0),F(0)]]
        C=[[-c,-zeta*s],[-s,zeta*c],[F(0),F(0)]]
        A=[[F(0),F(0),F(0)],[F(0),t*t,F(0)],[F(0),F(0),F(0)]]
        G=add(A,mul(tr(R),R))
        Gplus=[[1/(r*r),F(0),F(0)],[F(0),1/(t*t),F(0)],[F(0),F(0),F(0)]]
        Hproj=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(0)]]
        U=[[c,s,F(0)],[F(0),F(0),F(1)]]
        Lproj=mul(tr(U),U)
        Pred=[[r,F(0)],[F(0),t],[F(0),F(0)]]
        Cred=[[-F(1),F(0)],[F(0),F(0)]]
        assert mul(P,tr(P))==G
        assert mul(P,C)==scale(tr(R),-1)
        assert mul(G,Gplus)==Hproj
        assert mul(mul(tr(P),Gplus),P)==Lproj
        assert mul(U,tr(U))==eye(2)
        assert mul(Pred,U)==P
        assert mul(U,C)==Cred
        assert add(mul(Pred,tr(Pred)),mul(tr(R),R),-1)==A
        k=[[F(1)],[F(0)],[v]]; u=[[-r],[F(0)]]
        a=mul(C,u)
        assert a==mul(tr(P),k)
        assert mul(mul(tr(C),C),u)==u
        Z=mul(add(eye(3),Lproj,-1),C)
        assert mul(Z,u)==zero(3,1)
        assert mul(U,a)==mul(Cred,u)==mul(tr(Pred),k)
        assert mul(mul(tr(Cred),Cred),u)==u
        assert mul(A,k)==zero(3,1)
        assert mul(R,k)==scale(u,-1)
        kinv=scale(mul(mul(Gplus,tr(R)),u),-1)
        assert kinv==mul(Hproj,k)
        assert (kinv==k)==(v==0)
        assert sq(a)==sq(u)==sq(mul(U,a))
        if v:
            assert kinv!=k and mul(A,add(k,kinv,-1))==zero(3,1)
            padding+=1
        count+=1
    print(json.dumps(dict(status="rational_controls_pass",
        singular_covariance_cases=count, physical_projection_changes=padding,
        scope="algebra only; named actual covariance and row identities unproved"),
        sort_keys=True))
if __name__=="__main__":
    main()
