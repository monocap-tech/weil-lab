#!/usr/bin/env python3
"""PI019 analytic-only: independent zero-MELLIN-moment diagonal witness.

An actual smooth construction: φ=ρ' for nonzero nonnegative ρ∈Cc∞,
then ∫φ=0 and J=∫φ²>0, so every autocorrelation of
s_β=(φ+βφ(.-a))/sqrt(2) has
    h_β(0)=J>0 and ∫h_β(u)du=|∫s_β|²=0.
This is transversal to the main theorem's h(0)=0 test domain.

The source Chapter 13 moment trace formula is a claimed/partly
unfinished manuscript assertion, NOT a verified trace theorem.

Check a separate exact DISCRETE signed two-atom control φ=δ_0−δ_log4:
    C=2δ_0−δ_log4−δ_(-log4)
    I_N=2K_N(log9)−K_N(log36)−K_N(log(9/4))<0 for N>=1.
All values are EXACT fractions because 9,36,9/4 are rational squares.
This discrete model is NOT an admissible smooth spectral test; it merely
checks the strict-sign mechanism visible in the smooth derivative proof.
"""
from fractions import Fraction as Q
from math import isqrt


def rational_sqrt(q: Q) -> Q:
    assert q>0
    a,b=isqrt(q.numerator),isqrt(q.denominator)
    if a*a!=q.numerator or b*b!=q.denominator:
        raise ValueError("The argument must be an exact rational square")
    return Q(a,b)


def finite_kernel_at_log(q: Q,N:int)->Q:
    assert q>1 and N>=0
    root=rational_sqrt(q)
    return sum((Q(1)/(root*q**(2*n)) for n in range(N)),Q())


def signed_zero_mean_shift_pair(N:int)->Q:
    return (2*finite_kernel_at_log(Q(9),N)
      -finite_kernel_at_log(Q(36),N)
      -finite_kernel_at_log(Q(9,4),N))


def main()->None:
    assert signed_zero_mean_shift_pair(0)==0
    assert signed_zero_mean_shift_pair(1)==-Q(1,6)
    checks=0
    for N in range(1,101):
        answer=signed_zero_mean_shift_pair(N)
        assert answer<0
        # Each nth term satisfies
        # 2*9^(-t)-36^(-t)-(9/4)^(-t)
        # = -9^(-t)(2^t-2^(-t))², for t=2n+1/2.
        # The global finite sign is consequently strict.
        checks+=1
    print("PI019 EXACT ZERO-MOMENT SIGN MODEL: PASS")
    print(f"{checks} finite source-K_N signed two-atom controls strictly negative")
    print("N=1 coefficient exactly -1/6; source n=9 offset")
    print("NOT a smooth spectral test or a proof of Masullo Chapter 13")
    print("NOT Lean/Actions, trace-class extension, IV transport, positivity or RH")


if __name__=="__main__":
    main()
