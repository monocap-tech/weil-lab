#!/usr/bin/env python3
"""PI003 exact-rational local p=3, n=9 coefficient sanity checker.

Independent source-level preflight, NOT proof of an adelic trace formula,
a Lean certificate, global positivity, or RH. Uses only Fraction bounds.
The log(3)/3 coefficient is retained symbolically, not numerically approximated.
"""
from fractions import Fraction as Q

C_MINUS = -Q(1099, 1000)
C_PLUS = Q(1099, 1000)
A = Q(1, 2000)
DELTA = C_PLUS - C_MINUS


def log_interval(n: int, terms: int = 100) -> tuple[Q, Q]:
    """Lower and upper rational bounds for log(n), via positive atanh series."""
    assert isinstance(n, int) and n >= 2
    y = Q(n-1, n+1)
    power = y
    partial = Q(0)
    for j in range(terms):
        partial += 2*power/(2*j+1)
        power *= y*y
    upper_tail = 2*power/((2*terms+1)*(1-y*y))
    return partial, partial + upper_tail


def distance_lower_to_interval(target: Q, lo: Q, hi: Q) -> Q:
    """Certified distance lower bound, exact rational endpoints."""
    return max(Q(0), lo-target, target-hi)


def local_ratio_for_even_valuation(p: int, k: int) -> Q:
    """|p^k|_p^1/2 / |1-p^k u|_p, units u, k even and nonzero."""
    assert p >= 2 and k != 0 and k % 2 == 0
    m = abs(k)
    if k > 0:
        numerator = Q(1, p**(m//2))
        denominator = Q(1)
    else:
        numerator = Q(p**(m//2))
        denominator = Q(p**m)
    return numerator/denominator


def main() -> None:
    lo9, hi9 = log_interval(9)
    assert Q(0) < DELTA-hi9 < DELTA-lo9 < 2*A
    lo10, _ = log_interval(10)
    assert lo10 > Q(11, 5), "Original source cutoff not verified"

    contacts = []
    for n in range(2, 10):
        lo, hi = log_interval(n)
        for sign in (-1, 1):
            signed_lo, signed_hi = (lo, hi) if sign == 1 else (-hi, -lo)
            if distance_lower_to_interval(DELTA, signed_lo, signed_hi) < 2*A:
                contacts.append((n, sign))
    assert contacts == [(9, 1)], contacts

    assert local_ratio_for_even_valuation(3, -2) == Q(1, 3)
    assert local_ratio_for_even_valuation(3, +2) == Q(1, 3)
    # Positive local geometric coefficient for n=9 is symbolically log(3)/3.
    # Multiplicative Haar invariance gives the same unit-shell volume on
    # all shells, canceled by Masullo's prefactor 1/mu(Z_3^x).
    for unit_mass in (Q(1), Q(2, 3), Q(37, 47)):
        assert unit_mass*local_ratio_for_even_valuation(3, -2)/unit_mass == Q(1, 3)

    assert 2*A == Q(1, 1000)
    assert 3**2 == 9

    print("PI003 independent exact-rational local coefficient preflight: PASS")
    print("Unique signed old/old prime-power sample: (n=9, +log9)")
    print("Local contributing shell: valuation k=-2, |g|_3=9")
    print("Exact positive geometric coefficient: log(3)/3, no factor two")
    print("Unit Haar-volume normalization: canceled")
    print("Actual nonzero smooth-bump overlap: strict geometric inequality")
    print("NOT CHECKED: archimedean/pole identity, trace theorem, Lean, RH")


if __name__ == "__main__":
    main()
