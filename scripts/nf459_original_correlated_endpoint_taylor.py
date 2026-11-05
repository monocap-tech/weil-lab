#!/usr/bin/env python3
"""NF459 original physical 244D collar via source-correlated Taylor jets."""
from fractions import Fraction as F
from math import comb
from flint import arb,arb_mat
def certify(rows,D,N,V,S,B,delta,phys):
    pi=arb.pi();aa=phys.a
    M=72
    rho=F(1,10**4)
    ratio=delta/rho
    assert ratio==F(1,10**11)
    assert F(111,100)**13<4
    assert all(c<F(883) and k<=13 for c,k in rows if c is not None)
    assert 2*F(22,7)*F(883)*rho<1
    # On |d|=rho every original x^k sin/cos(2pi*c*(B-d))
    # has modulus < 4*e^1 <12; pole and raw n512/513 <3.
    # Exact generous Cauchy envelope M=16 holds for every generator.
    tail=F(16)*ratio**M/(1-ratio)
    assert tail>0
    def coefficients(c,k,exact_raw=None):
        if c is None:
            sb=(aa(B)/2).sinh();cb=(aa(B)/2).cosh()
            step=arb(1);out=[]
            for j in range(M):
                if j:step=step/(2*j)
                out.append((sb if j%2==0 else -cb)*step)
            return out
        A=2*pi*aa(c)
        if exact_raw is not None:
            assert c==F(5*exact_raw,11) and 2*c*B==exact_raw
            sn,co=arb(0),arb((-1)**exact_raw)
        else:sn,co=(A*aa(B)).sin_cos()
        t=[];step=arb(1)
        for j in range(M):
            if j:step=step*A/j
            cosj=(step* (-1)**(j//2)) if j%2==0 else arb(0)
            sinj=(step* (-1)**((j-1)//2)) if j%2 else arb(0)
            t.append(sn*cosj-co*sinj if k%2==0 else co*cosj+sn*sinj)
        out=[]
        for j in range(M):
            z=arb(0)
            for m in range(min(k,j)+1):
                z+=(-1)**m*comb(k,m)*aa(B)**(k-m)*t[j-m]
            out.append(z)
        return out
    raw=arb_mat(242,M)
    for i,row in enumerate(rows):
        c,k=row if row is not None else (None,None)
        vals=coefficients(c,k)
        for n in range(M):raw[i,n]=vals[n]
    transformed=D.transpose()*raw
    extras=[coefficients(F(5*n,11),0,n) for n in (512,513)]
    d=arb(aa(delta/2),aa(delta/2))
    def rational(y):
        m,k=y.man_exp()
        return F(int(m))*F(2)**int(k)
    assert rational(d.lower())<=0 and rational(d.upper())>=delta
    e=[arb(0) for _ in rows]
    u=[arb(0),arb(0)]
    for n in range(M-1,-1,-1):
        for i in range(242): e[i]=e[i]*d+transformed[i,n]
        for j in range(2):u[j]=u[j]*d+extras[j][n]
    C=max(rational(sum((abs(D[i,j]) for i in range(242)),arb(0)).upper()) for j in range(242))
    rem=aa(tail)*aa(C)
    assert rem.upper()<arb("1e-30")
    for i in range(242):e[i]+=arb(0,rem.upper())
    e=arb_mat([[v] for v in e])
    u=arb_mat([[z+arb(0,aa(tail).upper())] for z in u])
    z=N.solve(e,algorithm="lu")
    g=u-V.transpose()*z
    K=(e.transpose()*z)[0,0]+(g.transpose()*S.solve(g,algorithm="lu"))[0,0]
    assert K.lower()>0
    return K,rem,M
