#!/usr/bin/env python3
"""PI004 independent exact-rational real-place kernel sanity check.

Checks the coefficient and sign-preserving real-place change of variables at
the rational exponential points exp(u)=q (q perfect square). This is not
a proof of the digamma distribution identity, Masullo's trace theorem, Lean,
or the global spectral dictionary.
"""
from fractions import Fraction as F
from math import isqrt


def k_real_positive(q: int) -> F:
    """Masullo 1/2 real place, with positive/negative g at |g|=q>1."""
    a=isqrt(q)
    assert a*a==q and q>1
    return F(a,2) * (F(1,q-1)+F(1,q+1))


def k_real_negative(q: int) -> F:
    """Same real place at |g|=1/q<1, both real signs included."""
    a=isqrt(q)
    assert a*a==q and q>1
    return F(1,2*a) * (F(q,q-1)+F(q,q+1))


def k_gamma(q: int) -> F:
    """Physical kernel exp(-|u|/2)/(1-exp(-2|u|)) at u=+/-log(q)."""
    a=isqrt(q)
    assert a*a==q and q>1
    return F(1,a)/(F(1)-F(1,q*q))


def main() -> None:
    for q in (4,9,16,25,36,49,64,81):
        krp=k_real_positive(q)
        krn=k_real_negative(q)
        kg=k_gamma(q)
        assert krp==krn==kg, (q,krp,krn,kg)
        assert kg>0
    assert k_real_positive(9)==F(27,80)
    assert k_real_negative(9)==F(27,80)
    assert k_gamma(9)==F(27,80)

    # Exact inverse and symmetry/normalization sanity checks.
    assert F(1,2)*(F(3,8)+F(3,10))==F(27,80)
    assert F(1,3)/(1-F(1,81))==F(27,80)

    # K(u) ~ 1/(2*|u|) as u->0, explaining why h(0)!=0
    # requires a contact/regularization definition, not bare integration.
    print("PI004 exact real-place kernel preflight: PASS")
    print("Both signs of real g, Masullo factor 1/2: retained")
    print("u=+/-log(q) for square q: exact rational real/Gamma kernel match")
    print("u=+/-log(9): exact common weight K=27/80")
    print("NOT CHECKED: full digamma/Fourier proof, paperFT binding, trace, Lean, RH")


if __name__=="__main__":
    main()
