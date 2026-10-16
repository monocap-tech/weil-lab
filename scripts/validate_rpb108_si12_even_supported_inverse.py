#!/usr/bin/env python3
"""SI12 original physically supported even-pole inverse-response comparison.

Exact Fraction bounds on the full supported A^{-1} from a *positive operator
minorant*, not a fake whole-line Fourier reciprocal and NOT a certified
approximation to the odd A^{-1} response or finite BS spectrum.

Functional calculus, rank-one resolvent identity, and parity are proved in
notes/RPB108_SI12_EVEN_POLE_SUPPORTED_INVERSE_20261015.md.
"""
from fractions import Fraction as F
from math import factorial

B=F(11,10)
KAPPA=F(1,1000)


def sinh_bounds(x, n=22):
    assert x>0
    low=sum((x**(2*k+1)/factorial(2*k+1) for k in range(n)),F(0))
    first=x**(2*n+1)/factorial(2*n+1)
    ratio=x*x/F((2*n+2)*(2*n+3))
    return low,low+first/(1-ratio)


def cosh_bounds(x,n=22):
    assert x>0
    low=sum((x**(2*k)/factorial(2*k) for k in range(n)),F(0))
    first=x**(2*n)/factorial(2*n)
    ratio=x*x/F((2*n+1)*(2*n+2))
    return low,low+first/(1-ratio)


def validate():
    slow,shi=sinh_bounds(B)
    clo,chi=cosh_bounds(B)
    assert F(12,10)<slow<shi<F(14,10)
    # c(x)=cosh(x/2), s(x)=sinh(x/2), original supported I.
    # Exact inner products:
    # ||c||^2 = B + sinh B
    # ||s||^2 = sinh B - B
    # u0(x)=(2B)^(-1/2)
    # |<u0,c>|^2 = (4/B)*(cosh B - 1)
    c2_lo,c2_hi=B+slow,B+shi
    s2_lo,s2_hi=slow-B,shi-B
    overlap_lo,overlap_hi=4*(clo-1)/B,4*(chi-1)/B

    assert overlap_hi<c2_lo   # strict Cauchy-Schwarz / nonconstant c
    assert overlap_lo>F(243,100)  # >2.43
    assert F(2435,1000)<c2_lo<c2_hi<F(2436,1000)

    # Original positive operator A=A0+2|c><c|, A0>=kappa I,
    # hence supported inverse order A^-1 <= C^-1, C=kappa I+2cc*.
    #
    # For normalized even u0: <u0,A^-1 u0>
    # <= 1/kappa * [1-2|<u0,c>|^2/(kappa+2||c||^2)].
    constant_response_hi=(1-2*overlap_lo/(KAPPA+2*c2_hi))/KAPPA
    constant_response_lo=(1-2*overlap_hi/(KAPPA+2*c2_lo))/KAPPA
    assert F(212,100)<constant_response_lo<constant_response_hi<F(213,100)

    # For normalized exact positive-pole feature e_c=c/||c||:
    pole_response_hi=1/(KAPPA+2*c2_lo)
    pole_response_lo=1/(KAPPA+2*c2_hi)
    assert F(205,1000)<pole_response_lo<pole_response_hi<F(206,1000)

    # Since c is even and s odd, <c,s>=0 exactly.
    # Reference inverse C^-1 s = kappa^-1 s.
    # Thus rank-one even-pole information cannot improve the odd scalar floor.
    assert 2*s2_lo/KAPPA > 470
    assert 2*s2_hi/KAPPA < 472
    assert F(0)<s2_lo<s2_hi<c2_lo

    # The exact rank-one Sherman-Morrison law can be verified in a
    # rational 2x2 physically-supported toy operator but is *not*
    # pretending to compute original A0^-1.
    # D=diag(3,5), c=(1,1). R=D^-1; A=D+2cc*
    invdiag=[F(1,3),F(1,5)]
    t=sum(invdiag)
    denom=1+2*t
    g00=invdiag[0]-2*invdiag[0]**2/denom
    g01=-2*invdiag[0]*invdiag[1]/denom
    g11=invdiag[1]-2*invdiag[1]**2/denom
    a00,a01,a11=F(5),F(2),F(7)
    det=a00*a11-a01*a01
    assert g00==a11/det and g01==-a01/det and g11==a00/det

    print("SI12 PASS: exact supported original positive even-pole inverse Loewner bound")
    print("||c||^2 interval:",float(c2_lo),float(c2_hi))
    print("||s||^2 interval:",float(s2_lo),float(s2_hi))
    print("|<u0,c>|^2 interval:",float(overlap_lo),float(overlap_hi))
    print("<u0,A^-1 u0> strict certified upper:",float(constant_response_hi))
    print("<c/||c||,A^-1 c/||c||> strict upper:",float(pole_response_hi))
    print("odd negative pole / kappa-only scalar BS bound:",float(2*s2_hi/KAPPA))
    print("original signed parity: even rank-one inverse update; odd unaffected")
    print("No original A^-1 application, complete residual, finite BS eigenvalue, or RH claim.")


if __name__=="__main__":
    validate()
