#!/usr/bin/env python3
"""PI020 analytic-only, exact-arithmetic prime/pole/contact-null control.

Construct smooth functions on R in the mathematical proof:
  rho >= 0, rho nonzero, rho in Cc∞((0,d)), d < log(10/9)
  phi = rho''' - (1/4)rho'
  a = log(9/4)
  C(u) = ∫phi(x)phi(x-u) dx
  D(u) = C(u+a)+C(u-a).

Facts proved analytically in the companion memo:
  D(0)=0; ∫D=0; ∫D exp(±u/2)=0;
  D(±log p^k)=0 for EVERY prime p and integer k>=1.
Yet A_gamma(D)=-∫D K > 0:
  A_gamma(D)=2 Σ_{n>=1} q^(-lambda_n)
     lambda_n² (lambda_n²-1/4)² R(-lambda_n)R(+lambda_n)
where q=9/4, lambda_n=2n+1/2,
R(z)=∫rho(x)exp(zx)dx>0 for real z.

This script checks exact rational inequalities and polynomial/weight
coefficients, not integrals of smooth functions, not Masullo's
Theorem 13.3.1.1, not the zero side, and not Lean/CI.
"""
from fractions import Fraction as Q

QSHIFT=Q(9,4)
QRADIUS=Q(10,9)
ANCHOR_HALF=Q(1,2)


def lam(n:int)->Q:
    assert n>=0
    return 2*Q(n)+Q(1,2)


def laplace_symbol(z:Q)->Q:
    """S(z)=laplace_symbol(z)*R(z) for phi=∂(∂²-1/4)rho."""
    return -z*(z*z-Q(1,4))


def contact_gamma_weight(n:int)->Q:
    """Coefficient of 2*R(-lambda_n)*R(+lambda_n) in A_gamma(D)."""
    t=lam(n)
    # q^(-(2n+1/2)) = (2/3)*q^(-2n), all rational.
    damping=Q(2,3)*QSHIFT**(-2*n)
    return damping*t*t*(t*t-Q(1,4))**2


def main()->None:
    assert Q(2)<QSHIFT/QRADIUS
    assert QSHIFT*QRADIUS<Q(3)
    assert QSHIFT>QRADIUS
    assert QSHIFT/QRADIUS==Q(81,40)
    assert QSHIFT*QRADIUS==Q(5,2)
    # Because [81/40,5/2] subset (2,3), the two translated
    # support intervals cannot intersect any ±log(integer n>=2).
    print("PRIME-POWER SAMPLE EXCLUSION: exact (2,3) gap PASS")

    # phi has zero total mass (z=0) and zero pole Mellin moments
    # (z=±1/2). This forces the corresponding D moments to zero.
    for z in (Q(0),Q(1,2),Q(-1,2)):
        assert laplace_symbol(z)==0
    print("ZERO CONTACT / ZERO MASS / TWO POLE MOMENTS: symbolic PASS")

    assert contact_gamma_weight(0)==0
    assert contact_gamma_weight(1)==Q(800,27)
    count=0
    for n in range(1,501):
        t=lam(n)
        s_pos=laplace_symbol(t)
        s_neg=laplace_symbol(-t)
        assert s_pos*s_neg == -t*t*(t*t-Q(1,4))**2
        assert s_pos*s_neg<0
        assert contact_gamma_weight(n)>0
        count+=1

    # A(D)=2*Σ_{n>=1} weight_n*R(-t)*R(t)>0;
    # first-term exact bound = (1600/27) R(-5/2) R(5/2).
    assert 2*contact_gamma_weight(1)==Q(1600,27)
    print("STRICT GAMMA PHASE CONTRAST: 500 positive exact coefficients PASS")
    print("FIRST TERM EXACT LOWER BOUND: (1600/27) R(-5/2)R(5/2)")
    print("Critical-line frequency fingerprint: 2cos(a*t)*|S(i*t)|^2")
    print("All unproved source-to-spectral/IV map obligations remain OPEN")
    print("No .lean candidate, no compiler invocation, no Actions request")


if __name__=="__main__":
    main()
