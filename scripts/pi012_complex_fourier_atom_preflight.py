#!/usr/bin/env python3
"""PI012 exact rational reciprocal closure and finite Gamma-atom reconciliation.

Only exact Fraction algebra is checked. This is NOT an implementation of
complex integration, a Lean kernel run, Masullo's operator trace, or RH.
"""
from fractions import Fraction as Q


def reciprocal(a: Q, b: Q) -> tuple[Q, Q]:
    """Return 1/(a+i*b) as exact real and imaginary rational components."""
    denom=a*a+b*b
    if denom == 0:
        raise ZeroDivisionError("Fourier reciprocal has zero denominator")
    return a/denom, -b/denom


def two_halves(alpha: Q, r: Q) -> tuple[Q, Q]:
    assert alpha>0
    left=reciprocal(alpha, -r)  # positive-u complex half-line
    right=reciprocal(alpha, r)  # negative-u complex half-line
    return left[0]+right[0],left[1]+right[1]


def target(alpha: Q, r: Q) -> Q:
    assert alpha>0
    return 2*alpha/(alpha*alpha+r*r)


def gamma_atom(n: int,r:Q)->Q:
    assert n>=0
    a=Q(n)+Q(1,4)
    return a/(a*a+(r/2)**2)


def run() -> None:
    count=0
    for alpha in [Q(1,2),Q(3,5),Q(1),Q(2),Q(11,3),Q(20)]:
        for r in [Q(-25),Q(-3),Q(-1,5),Q(0),Q(2,11),Q(8)]:
            assert two_halves(alpha,r)==(target(alpha,r),Q(0))
            assert target(alpha,r)>0
            assert target(alpha,-r)==target(alpha,r)
            count+=1
    assert count==36
    for n in range(50):
        alpha=2*Q(n)+Q(1,2)
        for r in [Q(-9),Q(-1),Q(0),Q(2,3),Q(7)]:
            assert two_halves(alpha,r)==(gamma_atom(n,r),Q(0))
            count+=1
    assert count==286
    # Fourier transform linearity for the finite digamma physical kernel:
    # K_N(u)=sum_{n<N} exp(-(2n+1/2)|u|), giving sum of true rational atoms.
    # This is an exact finite algebra check, NOT analytic Fubini certification.
    for N in (0,1,2,3,4,10,25,50):
        for r in [Q(0),Q(1,2),Q(11,3)]:
            finite_freq=sum((target(2*Q(n)+Q(1,2),r) for n in range(N)),Q())
            finite_atoms=sum((gamma_atom(n,r) for n in range(N)),Q())
            assert finite_freq==finite_atoms
    # At alpha=0,r=0 the rational target is undefined: hypothesis essential.
    try:
        reciprocal(Q(0),Q(0))
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Missing denominator guard")

    print("PI012 exact rational Fourier/Gamma preflight: PASS")
    print("286 direct exact reciprocal/gamma checks, plus 24 finite-sum checks")
    print("Positive-alpha nonvanishing and even-frequency symmetry preserved")
    print("No integrals, Lean compiler, operator trace, RH or GRH certified")


if __name__=="__main__":
    run()
