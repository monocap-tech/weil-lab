#!/usr/bin/env python3
"""NF397 dependency-free exact-Fraction regression for archived Householder order.

Original archive's Q=H0 H1 ... H(n-1), so Q^T a is computed by
successively left-applying H0,H1,... to a; never construct dense Q in native.
Synthetic exact tests validate the order, vector invariance, and bilinear
pairing with a symmetric transformed signed matrix. This is NOT the original
242-dimensional numerical calculation or an RH/Weil proof.
"""
from fractions import Fraction as F

def transpose(A):
    return [list(x) for x in zip(*A)]
def mv(A,v):
    return [sum((a*b for a,b in zip(row,v)),F(0)) for row in A]
def mm(A,B):
    return [mv(transpose(B),row) for row in A]
def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))
def direct(a,Vs):
    out=a[:]
    n=len(out)
    for k,v in enumerate(Vs):
        assert len(v)==n and all(v[i]==0 for i in range(k))
        den=dot(v,v)
        assert den>0
        coeff=2*dot(v,out)/den
        out=[out[i]-coeff*v[i] for i in range(n)]
    return out

def prove(n,count):
    assert 0<count<=n
    # Rational reflectors with nontrivial overlaps and noncommuting order.
    Vs=[]
    for k in range(count):
        v=[F(0)]*k+[F(1 if i==k else ((i+k)%3)-1, 1+((i+2*k)%3))
                      for i in range(k,n)]
        assert any(v[k:])
        Vs.append(v)
    Q=[[F(i==j) for j in range(n)] for i in range(n)]
    for v in Vs:
        den=dot(v,v)
        H=[[F(i==j)-2*v[i]*v[j]/den for j in range(n)] for i in range(n)]
        Q=mm(Q,H)
    A=[F(2*i-3,2*i+1) for i in range(n)]
    B=[F((-1)**i*(i+1),i+2) for i in range(n)]
    qa=mv(transpose(Q),A)
    qb=mv(transpose(Q),B)
    da=direct(A,Vs)
    db=direct(B,Vs)
    assert da==qa and db==qb, 'Householder Q^T application order failure'
    assert dot(da,da)==dot(A,A)
    assert dot(db,db)==dot(B,B)
    assert dot(da,db)==dot(A,B)
    M=[[F((i+1)*(j+1)+int(i==j),3+i+j) for j in range(n)] for i in range(n)]
    assert dot(qa,mv(M,qb))==dot(da,mv(M,db))
    return n
if __name__=='__main__':
    for n in (2,3,4,5):
        for count in range(1,n+1):
            assert prove(n,count)==n
        print('NF398 EXACT Fraction Qtranspose 2-vector regression PASS with partial archived reflection counts at n=',n)
    print('NF397 algebraic transformation verified; native original 242 moment still OPEN')
