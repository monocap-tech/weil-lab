#!/usr/bin/env python3
"""PI025 ANALYTIC-ONLY exact rational contact/pole/prime gap and Gamma-mode ladder.

Smooth (NOT discrete) theoretical construction: choose rho>=0 nonzero in
Cc-infinity((0,d)) with exp(d)=10/9, a=log(9/4). For m>=1 set
    phi_m = partial * prod_(j=0)^(m-1)(partial^2-lambda_j^2) rho,
    lambda_j=2j+1/2.
This kills the total moment and both pole moments at +/-1/2, plus the
first m physical Gamma Laplace atoms, while the remaining Gamma
response of the separated autocorrelation difference is >0.

All arithmetic in this script is exact fractions. No numerical
integration, zeta zeros, Lean proofs or Actions calls. The positive
R(+lambda)R(-lambda) factors are proved from rho>=0 in the companion
analytic memo, not asserted by this script.
"""
from fractions import Fraction as Q


SHIFT = Q(9,4)
DIAMETER_EXP = Q(10,9)


def lam(j:int)->Q:
    assert j>=0
    return Q(2*j)+Q(1,2)


def polynomial(m:int,z:Q)->Q:
    assert m>=0
    p=-z
    for j in range(m):
        p *= z*z-lam(j)**2
    return p


def gamma_weight(m:int,n:int)->Q:
    assert m>=0 and n>=0
    z=lam(n)
    poly=z*z
    for j in range(m):
        poly *= (z*z-lam(j)**2)**2
    return Q(2,3)*SHIFT**(-2*n)*poly


def test()->None:
    # Exact support separation from EVERY integer n >=2:
    # [a-d,a+d] = [log(81/40),log(5/2)] subset (log2,log3).
    assert Q(2) < SHIFT/DIAMETER_EXP == Q(81,40)
    assert SHIFT * DIAMETER_EXP == Q(5,2) < Q(3)
    assert SHIFT > DIAMETER_EXP

    # Full physical Gamma kernel at a rational square source point.
    expected_K = (Q(2,3)/(1-Q(4,9)**2))
    assert expected_K==Q(54,65)
    assert gamma_weight(1,0)==0
    assert gamma_weight(1,1)==Q(800,27)
    assert 2*gamma_weight(1,1)==Q(1600,27)

    checked=0
    for m in range(1,9):
        assert polynomial(m,Q(0))==0
        assert polynomial(m,Q(1,2))==0
        assert polynomial(m,Q(-1,2))==0

        for n in range(m):
            assert gamma_weight(m,n)==0
        assert gamma_weight(m,m)>0

        for n in range(m,m+35):
            x=lam(n)
            assert polynomial(m,x)*polynomial(m,-x) == (
                -(x*x)*__import__("functools").reduce(
                    lambda acc,j: acc*(x*x-lam(j)**2)**2,range(m),Q(1)))
            assert gamma_weight(m,n)>0
            checked+=1

    # Source Chapter 12 contact, Chapter 13 mass-moment, and both pole
    # values are ZERO on D_m, while all Gamma mode weights n>=m positive.
    print("PI025 ANALYTIC RATIONAL PREFLIGHT: PASS")
    print("q=9/4 exact prime-gap [81/40, 5/2] strictly inside (2,3)")
    print("total and +/-1/2 pole moments formally annulled, m=1..8")
    print(f"{checked} exact strictly positive tail coefficient checks")
    print("first unremoved Gamma response m=1: 1600/27 R(5/2) R(-5/2)")
    print("NO evaluation of Masullo operator, Chapter 13 proof, Lean or RH")


if __name__=="__main__":
    test()
