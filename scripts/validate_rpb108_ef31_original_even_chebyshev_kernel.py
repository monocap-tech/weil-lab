#!/usr/bin/env python3
"""EF31 exact Chebyshev kernel identity regression; toy arithmetic only.
Original SI10 inventory is separately checked via --source; actual EF29
signed g, delta, and numeric kernel are not evaluated here.
"""
from fractions import Fraction as F
from math import comb
import argparse

def add(a,b):
    p=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): p[i]+=x
    for i,x in enumerate(b): p[i]+=x
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def mul(a,b):
    p=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): p[i+j]+=x*y
    return p

def mean(p):
    return sum((x*F(comb(i,i//2),4**(i//2)) for i,x in enumerate(p) if i%2==0),F(0))

def chebs(n):
    T=[[F(1)],[F(0),F(1)]]
    for _ in range(2,n+1):
        a=mul(T[-1],[F(0),F(2)])
        T.append(add(a,[-v for v in T[-2]]))
    return T[:n+1]

def to_cheb(p):
    p=p[:]; T=chebs(len(p)-1); w=[F(0)]*len(p)
    for k in range(len(p)-1,0,-1):
        w[k]=p[k]/T[k][k]
        p=add(p,[-w[k]*v for v in T[k]])
    w[0]=p[0]
    return w

def evaluate(p,z):
    a=F(0)
    for v in reversed(p): a=a*z+v
    return a

def toy(roots,t):
    n=sum(o for _,o in roots); P=[F(1)]
    for z,o in roots:
        for _ in range(o): P=mul(P,[-z,F(1)])
    U=mul(P,[-t,F(1)]); A=mean(U); B=mean(mul(U,[F(0),F(1)]))
    assert A or B
    R=mul(U,[B,-A]); w=to_cheb(R)
    assert len(w)==n+3 and w[0]==0 and any(w[1:])
    assert mean(R)==0 and evaluate(R,t)==0
    for z,o in roots:
        q=R
        for _ in range(o):
            assert evaluate(q,z)==0
            q=[F(i)*q[i] for i in range(1,len(q))]
    T=chebs(n+2)
    assert all(sum((w[l]*T[l][k] if k<len(T[l]) else F(0)
                    for l in range(n+3)),F(0))==R[k] for k in range(len(R)))
    assert sum((w[l]*evaluate(T[l],t) for l in range(n+3)),F(0))==0
    print('EF31 toy exact Chebyshev polynomial source/pole/null PASS',n)

def native():
    from validate_rpb108_ef28_pole_neutral_moment_kernel import original_source_and_geometry, GRID, COUNT
    from validate_rpb108_ef30_original_even_sampled_rank import native_root_non_aliases
    centers,orders,xs=original_source_and_geometry()
    assert len(centers)==len(orders)==107
    assert sum(orders)==469 and COUNT==471 and GRID==F(1,512)
    assert xs==[(i+1)*GRID for i in range(COUNT)]
    assert native_root_non_aliases(centers)==214
    print('EF31 ORIGINAL SI10 inventory 107/469/471 and 214 distinct roots PASS')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',action='store_true')
    args=parser.parse_args()
    toy([(F(1,3),2),(F(2,5),1)],F(6,5))
    toy([(F(-1,3),1),(F(1,4),1)],F(5,4))
    toy([(F(1,5),1)],F(7,5))
    if args.source: native()
    print('EF31 symbolic kernel regression PASS; actual signed delta OPEN')
