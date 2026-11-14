#!/usr/bin/env python3
"""NF506 exact rational regression for exterior support-liberation identity.
Finite-dimensional controls only, not original Weil-source admissibility.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(A,b):
    n=len(b)
    T=[list(A[i])+[b[i]] for i in range(n)]
    for c in range(n):
        pivot=next((r for r in range(c,n) if T[r][c]),None)
        assert pivot is not None
        T[c],T[pivot]=T[pivot],T[c]
        d=T[c][c]
        T[c]=[v/d for v in T[c]]
        for r in range(n):
            if r != c:
                f=T[r][c]
                T[r]=[a-f*v for a,v in zip(T[r],T[c])]
    return [row[-1] for row in T]


def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))


def check_case(n,deleted,theta):
    # Two independent selected columns, mimicking original analytical J.
    j=[[F(1),F(i+1,4)] for i in range(n)]
    w=[F(i*i-3*i+7, 2*i+3) for i in range(n)]
    # Shift W by an arbitrary selected-space vector: quotient invariant.
    w=[w[i]+theta[0]*j[i][0]+theta[1]*j[i][1] for i in range(n)]
    O=list(range(n));O2=[i for i in O if i not in deleted]
    def gram(A):return [[sum((j[k][i]*j[k][h] for k in A),F(0)) for h in range(2)] for i in range(2)]
    def rhs(A):return [sum((j[k][i]*w[k] for k in A),F(0)) for i in range(2)]
    def energy(A):return sum((w[k]*w[k] for k in A),F(0))
    G=gram(O);G2=gram(O2)
    a=solve(G,rhs(O));a2=solve(G2,rhs(O2))
    r=[w[i]-dot(j[i],a) for i in O]
    before=energy(O)-dot(rhs(O),a)
    after=energy(O2)-dot(rhs(O2),a2)
    k=[sum((j[t][i]*r[t] for t in deleted),F(0)) for i in range(2)]
    first=sum((r[t]**2 for t in deleted),F(0))
    second=dot(k,solve(G2,k))
    assert before-after==first+second
    assert before>=after>=0 and first>=0 and second>=0
    return 1


def main():
    count=0
    for n in (5,6,7):
        for num in (1,2):
            for D in combinations(range(n),num):
                for theta in ((F(0),F(0)),(F(7,13),F(-11,3)),(F(10**17),F(-10**13))):
                    count+=check_case(n,D,theta)
    print('NF506 exact support-liberation identity controls PASS:',count)
    print('No authentic Weil range/domain or global sign inferred')


if __name__=='__main__':main()
