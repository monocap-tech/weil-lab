#!/usr/bin/env python3
"""NF509 independent exact Fraction analytic two-generator leverage test.

This verifies the spatial Gram/trace algebra, not original physical source values.
"""
from fractions import Fraction as F

EXP=(1,3)

def gram(lo,hi):
    return [[F(2)*(hi**(p+q+1)-lo**(p+q+1))/(p+q+1)
             for q in EXP] for p in EXP]

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):return list(map(list,zip(*A)))

def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d>0
    return [[A[1][1]/d,-A[0][1]/d],
            [-A[1][0]/d,A[0][0]/d]]

def tr(A):return sum((A[i][i] for i in range(len(A))),F(0))

def test(m):
    B=F(549,500)
    G=gram(F(0),B)
    D=[[F(1),F(7,13)],[F(0),F(23,17)]]
    GD=mm(transpose(D),mm(G,D))
    inv=inv2(G); invD=inv2(GD)
    tot=totD=F(0)
    for j in range(m):
        A=gram(B*F(j,m),B*F(j+1,m))
        AD=mm(transpose(D),mm(A,D))
        tau=tr(mm(inv,A))
        tauD=tr(mm(invD,AD))
        assert tau==tauD and tau>0
        tot+=tau;totD+=tauD
        assert tau<=2
    assert tot==totD==2
    assert tr(mm(invD,GD))==2
    return m

if __name__=='__main__':
    count=sum(test(m) for m in (8,16,64,128,256))
    assert count==472
    print('NF509 exact Fraction polynomial trace and frame covariance: 472 cells PASS')
    print('Native original 242D physical profiles NOT YET independently measured')
