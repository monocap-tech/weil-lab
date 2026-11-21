#!/usr/bin/env python3
"""PI002 rational independent sanity checker.

NOT a formal proof of the Masullo trace formula, adelic smoothness, or RH.
Exact Fraction atanh enclosures certify the single active n=9 old-old
prime-power shift in a two-bump mixed test. Exact rational polynomial-surrogate
moments cross-check the sign/orientation of the reflected Laplace transform.
"""
from fractions import Fraction as Q
from math import comb, factorial

C_MINUS = -Q(1099, 1000)
C_PLUS = Q(1099, 1000)
OLD_BUMP_R = Q(1, 2000)
DELTA = C_PLUS - C_MINUS


def log_enclosure(n: int, terms: int = 100) -> tuple[Q, Q]:
    assert n >= 2 and terms >= 1
    y = Q(n - 1, n + 1)
    sq = y * y
    power = y
    partial = Q()
    for j in range(terms):
        partial += 2 * power / (2*j + 1)
        power *= sq
    tail = 2 * power / ((2*terms + 1)*(1 - sq))
    return partial, partial + tail


def distance_lower_to_interval(x: Q, lo: Q, hi: Q) -> Q:
    return max(lo - x, x - hi, Q())


def unit_ball_moment(k: int, a: Q) -> Q:
    """Integral_{-a}^a v^k (1 - v^2/a^2) dv, 0 if k odd."""
    if k % 2:
        return Q()
    return 4*a**(k+1)/((k+1)*(k+3))


def raw_moment(k: int, center: Q, a: Q) -> Q:
    return sum(
        (Q(comb(k, j)) * center**(k-j) * unit_ball_moment(j, a)
         for j in range(k+1)), Q()
    )


def moment_via_product(k: int) -> Q:
    """kth derivative at z=0 of H_t(z) H_s(-z), two center values."""
    return sum(
        Q(comb(k, j)) * raw_moment(j, C_PLUS, OLD_BUMP_R)
        * (-1)**(k-j) * raw_moment(k-j, C_MINUS, OLD_BUMP_R)
        for j in range(k+1)
    )


def moment_via_center_difference(k: int) -> Q:
    """Separate expansion of (delta+v-w)^k over centered bumps."""
    total = Q()
    for j in range(k+1):
        inner = sum(
            Q(comb(j, l)) * (-1)**(j-l)
            * unit_ball_moment(l, OLD_BUMP_R)
            * unit_ball_moment(j-l, OLD_BUMP_R)
            for l in range(j+1)
        )
        total += Q(comb(k, j))*DELTA**(k-j)*inner
    return total


def main() -> None:
    assert C_MINUS + OLD_BUMP_R < C_PLUS - OLD_BUMP_R
    assert DELTA == Q(1099, 500)

    # Exact n=9 overlap: [log9_lower,log9_upper] is strictly
    # below delta yet within two bump radii of it.
    lo9, hi9 = log_enclosure(9)
    assert 0 < DELTA-hi9 < DELTA-lo9 < 2*OLD_BUMP_R

    # Other signed shifts do not meet these two very narrow old bumps.
    contacts = set()
    for n in range(2, 10):
        lo, hi = log_enclosure(n)
        for sign in [-1, +1]:
            a,b = (lo,hi) if sign==1 else (-hi,-lo)
            if distance_lower_to_interval(DELTA, a,b) < 2*OLD_BUMP_R:
                contacts.add((n,sign))
    assert contacts == {(9,1)}, contacts

    # All n>=10 excluded by physical original window [-1.1,1.1].
    lo10,_=log_enclosure(10)
    assert lo10 > Q(11,5)

    # Under Masullo Appendix A.3.2.1, Q's Tamagawa compact-fiber mass is 1:
    # r1=1,r2=0, h=R=d=1,w=2; hence 2**r1 /w=1.
    fiber_mass = Q(2,2)
    assert fiber_mass == 1

    # Two independent exact expansions of the reflected Laplace product
    # using C0 polynomial surrogates (not the true C-infinity bumps).
    for k in range(0,9):
        assert moment_via_product(k) == moment_via_center_difference(k), k
    assert moment_via_product(0) > 0
    assert moment_via_product(1) == DELTA * moment_via_product(0)

    # Demonstrate that a diagonal test cannot satisfy the norm-one zero gate.
    assert raw_moment(0, C_PLUS, OLD_BUMP_R)>0

    print("PI002 exact rational preflight: PASS")
    print("Masullo Q compact-fiber Haar mass: 1 (using stated number-field constants)")
    print("Old mixed test: h(0)=0 from disjoint physical supports")
    print("Signed n=2..9 old-old contacts: only (+log 9)")
    print("At +log9 actual smooth positive bumps have strictly positive overlap")
    print("Original n>=10: log10>11/5")
    print("Reflected Laplace correlation: exact Taylor derivatives 0..8 agree")
    print("Surrogate moment check is NOT an original smooth-source or trace proof")


if __name__ == "__main__":
    main()
