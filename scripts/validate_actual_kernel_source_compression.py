#!/usr/bin/env python3
"""Exact raw-positive kernel compression and infinite-support tail controls."""
from fractions import Fraction as F
from itertools import product
import json

def tr(a): return list(map(list,zip(*a)))
def mm(a,b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def neg(a): return [[-x for x in r] for r in a]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def diag(a,b): return [[a,F(0)],[F(0),b]]

def main():
    compressed=different=geometric=0
    for r,(s,t,l),(c,d),h in product((F(1),F(2),F(3)),
        ((F(3),F(4),F(5)),(F(5),F(12),F(13)),(F(8),F(15),F(17))),
        ((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13))),
        (F(-2),F(1),F(3))):
        O=[[c,-d],[d,c]]
        N=mm(O,diag(r,s)); P0=diag(r,l); P=tr(P0)
        L=diag(r*r,l*l); A=diag(F(0),t*t)
        Pi=[[c*c,c*d],[c*d,d*d]]
        R=mm(Pi,N); B=sub(N,R)
        C=neg(mm(mm(P0,diag(1/(r*r),1/(l*l))),tr(R)))
        Delta=sub(L,mm(tr(R),R))
        k=[[h],[F(0)]]; u=neg(mm(R,k)); a=mm(P0,k)
        assert mm(tr(N),N)==diag(r*r,s*s)
        assert sub(L,mm(tr(N),N))==A
        assert mm(P,C)==neg(tr(R))
        assert mm(B,k)==[[F(0)],[F(0)]]
        assert mm(C,u)==a==mm(tr(P),k)
        assert mm(mm(tr(C),C),u)==u
        assert mm(A,k)==mm(Delta,k)==[[F(0)],[F(0)]]
        assert Delta==diag(F(0),l*l)
        assert mm(tr(C),C)==Pi  # contraction; identity only on W.
        assert sum(v[0]**2 for v in a)==sum(v[0]**2 for v in u)
        if Delta!=A: different+=1
        compressed+=1
    q=F(9,25)
    for n in range(1,129):
        coordinates=[F(4,5)*F(3,5)**j for j in range(n)]
        selected=sum(v*v for v in coordinates)
        tail=q**n
        assert selected+tail==1 and tail>0
        assert selected>0  # separating, effective covariance coercive.
        k=F(3,2)
        raw_defect=(1-selected)*k*k
        assert raw_defect==tail*k*k>0
        # With P0=1, the minimal raw compensator is row -coordinates.
        # Its candidate a=C u misses physical adjoint by tail*k.
        candidate_a=selected*k
        assert k-candidate_a==tail*k
        # C*C u=selected*u, so exact finite raw unit gain fails.
        u=[-v*k for v in coordinates]
        assert any(selected*v!=v for v in u)
        # The effective packet and exact rank-one W packet are distinct.
        assert 2*k*k-2*selected*k*k==2*tail*k*k
        if n>1: assert tail<q**(n-1)
        geometric+=1
    print(json.dumps(dict(status="rational_controls_pass",
        compressed_packet_cases=compressed,off_kernel_operator_differences=different,
        infinite_support_prefix_cases=geometric,
        scope="algebra and exact geometric sums; no actual divisor computation"),
        sort_keys=True))

if __name__=="__main__": main()
