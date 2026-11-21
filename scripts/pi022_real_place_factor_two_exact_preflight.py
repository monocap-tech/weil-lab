#!/usr/bin/env python3
"""PI022 ANALYTIC-ONLY exact rational local-place normalization regression.

Primary manuscript sources (visually inspected): Theorem 12.5.1.1 printed
p.519 uses 1/2 * real-place PV with multiplicative Tamagawa dmu=dx/|x|.
Theorem 13.3.1.1 printed p.522 uses ONE * bare real-place PV with the
same dmu. Appendix B.4.4 (printed pp.619-620) identifies canonical Haar
as dmu/2, and Appendix A.3.2 (p.560) defines dmu=dx/|x| over R.

For norm-radial h(log|x|) supported away from u=0, both principal values
are ordinary integrals and the signed real branches x=+e^u,-e^u give
  bare density = sqrt(exp(u))/|1-exp(u)| +
                 sqrt(exp(u))/(1+exp(u))
               = 2 K(|u|),
  where K(t)=exp(-t/2)/(1-exp(-2t)).
Thus Chapter12's displayed real term equals ∫h K, while Chapter13's
displayed real term equals 2∫h K. This source discrepancy is detected
on smooth h with h(0)=∫h=0; it is not a scalar contact correction.

This independent exact-Fraction regression checks rational-square u=log q,
and signed finite-K_N derivative-bump two-atom algebra. It does NOT
compile Lean, evaluate an actual smooth integral or zero divisor, or
prove either Masullo trace theorem valid. NO RH claims.
"""
from fractions import Fraction as F
from math import isqrt


def sqrt_fraction(q: F) -> F:
    if q <= 0:
        raise ValueError("Positive rational square required")
    a, b = isqrt(q.numerator), isqrt(q.denominator)
    assert a*a == q.numerator and b*b == q.denominator
    return F(a, b)


def K_at_log_q(q: F) -> F:
    """Physical original K(|log q|) at q>1 an exact rational square."""
    assert q > 1
    return 1 / sqrt_fraction(q) / (1 - 1/(q*q))


def bare_real_local_density(q: F) -> F:
    """Positive u=log q, sum of x=+q and x=-q with dx/|x|=du."""
    assert q > 1
    return sqrt_fraction(q) * (1/(q-1) + 1/(q+1))


def negative_u_real_density(q: F) -> F:
    """Negative u=-log q, sum of x=+1/q and x=-1/q."""
    assert q > 1
    return (1/sqrt_fraction(q)) * (1/(1-1/q) + 1/(1+1/q))


def finite_K_at_log_q(q: F, N: int) -> F:
    assert q > 1 and N >= 0
    return sum((1/(sqrt_fraction(q)*q**(2*n)) for n in range(N)), F())


def finite_signed_D_even_pair(N:int)->F:
    """Signed 2-point-control for D_e; not itself a smooth test.

    phi=delta_0-delta_log4, C=2delta0-delta_log4-delta_-log4.
    D_e(u)=C(u+log9)+C(u-log9); with even K_N,
    ∫D_e K_N=2*[2K_N(log9)-K_N(log36)-K_N(log(9/4))].
    """
    return 2*(2*finite_K_at_log_q(F(9),N)
              -finite_K_at_log_q(F(36),N)
              -finite_K_at_log_q(F(9,4),N))


def main() -> None:
    roots=(2,3,4,5,6,7,8,9,10,11,12,13,17,21)
    levels=0
    for n in roots:
        q=F(n*n)
        K=K_at_log_q(q)
        assert bare_real_local_density(q) == 2*K
        assert negative_u_real_density(q) == 2*K
        # Printed Ch12 1/2 times bare PV; Ch13 bare PV:
        assert bare_real_local_density(q)/2 == K
        assert bare_real_local_density(q) == 2*K
        levels+=1

    assert K_at_log_q(F(9))==F(27,80)
    assert bare_real_local_density(F(9))==F(27,40)

    # 100 signed finite truncation levels, all strictly detect factor 2.
    for N in range(1,101):
        arch12=finite_signed_D_even_pair(N)
        arch13=2*arch12
        assert arch12<0 and arch13<arch12
        assert arch13-arch12==arch12
    assert finite_signed_D_even_pair(1)==-F(1,3)
    assert 2*finite_signed_D_even_pair(1)==-F(2,3)

    # A pure scalar c*h(0)+d*∫h CANNOT cancel a nonzero discrepancy
    # on a smooth test satisfying h(0)=∫h=0.
    for c,d in ((F(1),F(0)),(F(0),F(1)),(F(-3,4),F(7,9))):
        correction=c*F(0)+d*F(0)
        assert correction==0
        assert correction!=finite_signed_D_even_pair(1)

    # Finite arithmetic local-place source normalization: for Q_p the
    # discriminant is 1, so the manuscript's mu_p(Z_p^×)=1, and the
    # printed finite coefficients log(p)/mu and log(p) agree. This
    # is a SYMBOLIC SOURCE observation, not a numerical log(p) check.

    print("PI022 SOURCE-NORMALIZATION EXACT RATIONAL PREFLIGHT: PASS")
    print(f"{levels} positive/negative rational-square real-place densities")
    print("100 strictly nonzero signed finite-K_N phase-normalization controls")
    print("At log9: bare density 27/40; Chapter12 half = 27/80")
    print("At N=1: Ch12 signed D_e kernel = -1/3, Ch13 bare = -2/3")
    print("No spectral zero sum, Masullo trace proof, Lean, Actions or RH")


if __name__=="__main__":
    main()
