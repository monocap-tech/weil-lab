#!/usr/bin/env python3
"""CP-C1(A) nine-probe Hermitian reconstruction: exact rational self-test.

No numerical zeta/Weil source input, Lean kernel receipt, or spectral
completeness is implied. The convention is conjugate-linear first,
linear second: B(u,v) = sum conj(u_i) A_ij v_j.
"""
from fractions import Fraction as Q

ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
I = (Q(0), Q(1))

def z(a=0, b=0):
    return Q(a), Q(b)

def add(x,y):
    return x[0]+y[0],x[1]+y[1]

def mul(x,y):
    return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]

def conj(x):
    return x[0],-x[1]

def basis(i):
    return [ONE if j==i else ZERO for j in range(3)]

def hermitian(diags, upper):
    a=[[ZERO for _ in range(3)] for _ in range(3)]
    for i,d in enumerate(diags):
        a[i][i]=z(d)
    for (i,j),v in upper.items():
        assert 0<=i<j<3
        a[i][j]=v
        a[j][i]=conj(v)
    return a

def energy(a,v):
    acc=ZERO
    for i in range(3):
        for j in range(3):
            acc=add(acc,mul(conj(v[i]),mul(a[i][j],v[j])))
    assert acc[1]==0, 'Hermitian energy must be real'
    return acc[0]

def probes(a):
    d=[energy(a,basis(i)) for i in range(3)]
    p={};s={}
    for i in range(3):
        for j in range(i+1,3):
            ei,ej=basis(i),basis(j)
            p[i,j]=energy(a,[add(ei[k],ej[k]) for k in range(3)])
            s[i,j]=energy(a,[add(ei[k],mul(I,ej[k])) for k in range(3)])
    return d,p,s

def reconstruct(d,p,s):
    a=hermitian(d,{})
    for i in range(3):
        for j in range(i+1,3):
            a[i][j]=z((p[i,j]-d[i]-d[j])/2,
                        -(s[i,j]-d[i]-d[j])/2)
            a[j][i]=conj(a[i][j])
    return a

def residual_frobenius_upper_sq(masses,diag_budget,plus_budget,iplus_budget):
    """Guaranteed upper bound on ||G^-1/2 D G^-1/2||_F^2,
    assuming that the nine stated absolute probe-error budgets are valid.
    NOT an independent certifier of their provenance or correctness.
    """
    assert len(masses)==len(diag_budget)==3
    assert all(x>0 for x in masses)
    assert all(x>=0 for x in diag_budget)
    v=sum((diag_budget[i]/masses[i])**2 for i in range(3))
    for i in range(3):
        for j in range(i+1,3):
            dp=plus_budget[i,j]+diag_budget[i]+diag_budget[j]
            ds=iplus_budget[i,j]+diag_budget[i]+diag_budget[j]
            assert dp>=0 and ds>=0
            # |Re D_ij| <= dp/2, |Im D_ij| <= ds/2.
            v+=2*(dp*dp+ds*ds)/(4*masses[i]*masses[j])
    return v

def main():
    tests=[
        hermitian([Q(5),Q(7),Q(11)],{
            (0,1):z(Q(1),Q(2)),(0,2):z(Q(-3),Q(1,2)),
            (1,2):z(Q(4),Q(-5,3))}),
        hermitian([Q(0),Q(0),Q(0)],{(0,1):z(Q(-7,13))}),
        hermitian([Q(-3,7),Q(0),Q(5)],{
            (0,1):z(0,Q(11,9)),(0,2):z(Q(5,8)),(1,2):z(0,Q(-2,7))})
    ]
    for a in tests:
        d,p,s=probes(a)
        assert reconstruct(d,p,s)==a
    d,p,s=probes(tests[0])
    bad=hermitian(d,{})
    for (i,j) in p:
        # DELIBERATE WRONG-SIGN conjugation control.
        bad[i][j]=z((p[i,j]-d[i]-d[j])/2,(s[i,j]-d[i]-d[j])/2)
        bad[j][i]=conj(bad[i][j])
    assert bad!=tests[0]
    prime=tests[1]
    assert energy(prime,[ONE,ONE,ZERO])==Q(-14,13)
    assert energy(prime,[ONE,z(-1),ZERO])==Q(14,13)
    assert energy(prime,[ONE,I,ZERO])==0
    assert energy(prime,basis(0))==energy(prime,basis(1))==0
    zeros={(0,1):Q(0),(0,2):Q(0),(1,2):Q(0)}
    sq=residual_frobenius_upper_sq(
        [Q(1,2000),Q(1,2000),Q(1,1000)],
        [Q(1,10**9)]*3,
        {(i,j):Q(1,10**9) for i,j in zeros},
        {(i,j):Q(1,10**9) for i,j in zeros})
    assert Q(0)<sq<Q(1,500)**2
    # Dimension lower bound: 3 diagonal + 2*3 complex off-diagonal = 9.
    assert len(d)+len(p)+len(s)==9
    print('CP-C1(A): 9/9 exact-rational Hermitian probes reconstruct 3/3 test matrices')
    print('WRONG-CONJUGATION SIGN negative control: rejected')
    print('PRIME PHASE +/-1/i negative controls: PASS')
    print('MASS-NORMALIZED FROBENIUS ERROR LEMMA sample: PASS, squared upper bound =',sq)
    print('NO LEAN PASS; NO ORIGINAL WEIL/EXPLICIT-FORMULA CERTIFICATE; NO ZERO-ROSTER CERTIFICATE')

if __name__=='__main__':
    main()
