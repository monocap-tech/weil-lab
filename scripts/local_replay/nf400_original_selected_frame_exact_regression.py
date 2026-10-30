#!/usr/bin/env python3
"""NF400 independent exact Fraction regression for complete source column map.

Checks Q forward (reversed application), Qtranspose (ascending application),
signed frame/mixed/pole response, raw Gram transport and physical projection.
Synthetic only; original 242D numeric evidence requires source-native Arb.
"""
from fractions import Fraction as F
from nf397_householder_two_vector_exact_regression import (
    transpose, mv, mm, dot, direct
)

def diag(v):
    return [[v[i] if i==j else F(0) for j in range(len(v))] for i in range(len(v))]

def add(a,b):
    return [x+y for x,y in zip(a,b)]

def scale(a,t):
    return [t*x for x in a]

def forward(x,V):
    y=x[:]
    n=len(y)
    for k in range(len(V)-1,-1,-1):
        v=V[k]
        assert len(v)==n and all(v[i]==0 for i in range(k))
        factor=2*dot(v,y)/dot(v,v)
        y=[y[i]-factor*v[i] for i in range(n)]
    return y

def run(n,r):
    V=[]
    for k in range(r):
        V.append([F(0)]*k +
            [F(1 if i==k else ((i+k)%3)-1, 1+((i+2*k)%3))
             for i in range(k,n)])
    Q=diag([F(1)]*n)
    for v in V:
        den=dot(v,v)
        h=[[F(i==j)-2*v[i]*v[j]/den for j in range(n)] for i in range(n)]
        Q=mm(Q,h)
    alpha=[F(i+1,i+2) for i in range(n)]
    beta=[F(2*i-3,i+3) for i in range(n)]
    assert direct(alpha,V)==mv(transpose(Q),alpha)
    assert forward(alpha,V)==mv(Q,alpha)
    assert forward(beta,V)==mv(Q,beta)
    assert dot(alpha,alpha)==dot(forward(alpha,V),forward(alpha,V))

    M=[[F((i+1)*(j+1)+int(i==j),i+j+3) for j in range(n)] for i in range(n)]
    L=[[F((i+1)*(k+2),i+k+4) for k in range(2)] for i in range(n)]
    f=[F(1,2),-F(2,3)]
    u4s=F(1,7)
    H=diag([F(i+2) for i in range(n)])
    D=diag([F(1,i+1) for i in range(n)])
    N=mm(mm(transpose(D),H),D)
    pole=[F(i==n-1) for i in range(n)]
    # Formula using only direct archived reflection actions, not dense Q.
    d=add(forward(mv(M,direct(alpha,V)),V),mv(transpose(D),mv(L,f)))
    d=add(d,scale(mv(transpose(D),mv(H,pole)),2*u4s))
    # Independent dense formula:
    qdense=mv(Q,mv(M,mv(transpose(Q),alpha)))
    dense=add(add(qdense,mv(transpose(D),mv(L,f))),
              scale(mv(transpose(D),mv(H,pole)),2*u4s))
    assert d==dense
    # H,D,N diagonal in this toy: use exact N^-1 as independent transport.
    n_inv_d=[d[i]/N[i][i] for i in range(n)]
    raw=mv(H,mv(D,n_inv_d))
    assert mv(transpose(D),raw)==d
    z=mv(D,beta)
    direct_signed=dot(direct(alpha,V),mv(M,direct(beta,V)))+dot(z,mv(L,f))
    direct_pole=2*u4s*dot(z,mv(H,pole))
    assert dot(z,raw)==direct_signed+direct_pole
    selected_norm2=dot(d,n_inv_d)
    assert selected_norm2>=0
    print('NF400 exact forward/reverse reflector, 242D formula and Gram transport PASS',n,r)

if __name__=='__main__':
    for n in (2,3,4,5):
        for r in range(1,n+1):
            run(n,r)
