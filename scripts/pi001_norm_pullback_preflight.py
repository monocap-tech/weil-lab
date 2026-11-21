#!/usr/bin/env python3
"""PI001 independent rational geometry preflight. NOT a Lean or trace-formula certificate.

Checks the physical three-cell layout of IV019/IV020, all signed finite
integer logarithmic shifts 2..9, old/old surviving n=9 interaction,
new/new self-prime clearance, and the norm-one zero-at-origin domain gate.

All logarithms are enclosed by rational atanh series with a geometric
rational remainder bound; no floating point or numerical-oracle logarithms.
"""
from fractions import Fraction as F

OLD_R = F(1, 1000)
NEW_R = F(1, 500)
OLD = {"minus": -F(1099, 1000), "plus": F(1099, 1000)}
NEW_C = F(1, 5)


def log_bounds(n: int, terms: int = 70) -> tuple[F, F]:
    """Rigorous lower/upper bounds on natural log(n), n>=2 integer."""
    assert n >= 2 and terms >= 1
    y = F(n - 1, n + 1)
    y2 = y * y
    power = y
    partial = F(0)
    for k in range(terms):
        partial += 2 * power / (2 * k + 1)
        power *= y2
    # Tail from k=terms: denominators >= 2*terms+1.
    tail = 2 * power / ((2 * terms + 1) * (1 - y2))
    return partial, partial + tail


def dist_from_shift_interval(delta: F, lo: F, hi: F, sign: int) -> F:
    """Certified lower bound on |delta - sign*log(n)|."""
    assert sign in (-1, 1)
    a, b = (lo, hi) if sign == 1 else (-hi, -lo)
    return max(a - delta, delta - b, F(0))


def max_dist_to_interval(delta: F, lo: F, hi: F) -> F:
    """Upper bound on |delta-log(n)| from a rigorous log interval."""
    return max(abs(delta - lo), abs(delta - hi))


def main() -> None:
    bounds = {n: log_bounds(n) for n in range(2, 11)}
    assert bounds[2][0] > 2 * NEW_R
    assert bounds[10][0] > F(11, 5), "Original n>=10 cutoff unverified"

    old_new_min = None
    for old_c in OLD.values():
        delta = NEW_C - old_c
        assert abs(delta) > OLD_R + NEW_R  # h_(s,t)(0)=0 geometrically
        for n in range(2, 10):
            lo, hi = bounds[n]
            for sign in (-1, 1):
                gap = dist_from_shift_interval(delta, lo, hi, sign) - (OLD_R + NEW_R)
                assert gap > 0, (old_c, n, sign, "unexpected old/new interaction")
                old_new_min = gap if old_new_min is None else min(old_new_min, gap)
    assert old_new_min is not None
    assert old_new_min > F(84, 1000), "Unexpected deterioration of mixed prime clearance"

    # Every old-old source/sample interaction is recorded, including n=9.
    collisions = set()
    for a_name, a_c in OLD.items():
        for b_name, b_c in OLD.items():
            delta = b_c - a_c
            for n in range(2, 10):
                lo, hi = bounds[n]
                for sign in (-1, 1):
                    gap = dist_from_shift_interval(delta, lo, hi, sign)
                    if gap < 2 * OLD_R:
                        collisions.add((a_name, b_name, n, sign))
    expected = {
        ("minus", "plus", 9, 1),
        ("plus", "minus", 9, -1),
    }
    assert collisions == expected, (collisions, expected)

    n9_lo, n9_hi = bounds[9]
    assert max_dist_to_interval(OLD["plus"] - OLD["minus"], n9_lo, n9_hi) < 2 * OLD_R

    # The mass-capacity budget is conditional on authentic prime transfer.
    union_measure = 4 * OLD_R + 2 * NEW_R
    assert union_measure == F(1, 125)
    conditional_margin = F(7, 10) - 75 * union_measure
    assert conditional_margin == F(1, 10)
    assert F(2, 5) - 150 * NEW_R == conditional_margin

    print("PI001 EXACT RATIONAL PREFLIGHT: PASS")
    print("Original-old/central-new support overlap at zero: NONE")
    print("Old/new signed n=2..9 prime shift overlaps: NONE")
    print("New/new active prime shift overlap: NONE (log 2 > 2*r)")
    print("Old/old signed integer sample collisions: only the two n=9 directions")
    print("Certified minimum old/new clearance: > 84/1000")
    print("Original n>=10 cutoff: log 10 > 11/5")
    print("Three-cell support-measure bound: 1/125")
    print("Conditional IV019 mass-margin algebra: 1/10")
    print("NOT checked: adelic smoothness, Haar/Mellin, trace formula, Lean, RH")


if __name__ == "__main__":
    main()
