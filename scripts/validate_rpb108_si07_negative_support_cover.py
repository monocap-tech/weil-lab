#!/usr/bin/env python3
"""SI07 all-rational adaptive certificate of the negative Fourier set's measure.

Imports SI06's already validated exact signed cos/pi/log interval machinery.
No floating-point sampling is used to accept a positivity interval.
"""
from fractions import Fraction as F
from functools import lru_cache

from validate_rpb108_si06_negative_band import (
    B, PI, LN, K as PARENT_K, CONST_UP, YFAC, prime_interval,
    log_rational_bounds,
)

END = 896
DEPTH = 6
K = 64
M = F(69)
DEN = 10**6


@lru_cache(maxsize=None)
def arch_lower_cell(j):
    """Lower bound valid throughout [j,j+1], including j=0."""
    y = YFAC * j
    a = F(1, 4)
    head = sum(
        (y*y / ((k+a)*((k+a)**2+y*y)) for k in range(K)), F(0)
    )
    # Exact integral lower bound to the positive decreasing digamma tail.
    tail = log_rational_bounds(1 + (y/(K+a))**2)[0] / 2
    return head + tail - CONST_UP


def ceil_fraction(q):
    """Small integer outward upper rounding."""
    return -(-q.numerator // q.denominator)


def validate():
    assert PARENT_K == 128 and K == 64
    assert PI[0] > F(333, 106) and PI[1] < F(22, 7)
    assert LN[2][0] > F(69, 100)
    # Half-band is already certified nonnegative above 896 in SI06.
    measure_upper = F(0)
    neg_integral_positive_half_upper = F(0)
    leaves = 0
    accepted = 0
    discarded = 0
    maxdepth = 0
    min_positive = None
    unverified = []

    def visit(left, right, j, d):
        nonlocal measure_upper, neg_integral_positive_half_upper
        nonlocal leaves, accepted, discarded, maxdepth, min_positive
        midpoint = (left + right) / 2
        lo = arch_lower_cell(j) + prime_interval(midpoint)[0] - M*(right-left)/2
        if lo > 0:
            accepted += 1
            min_positive = lo if min_positive is None else min(min_positive, lo)
            return
        if d < DEPTH:
            visit(left, midpoint, j, d+1)
            visit(midpoint, right, j, d+1)
            return
        leaves += 1
        maxdepth = max(maxdepth, d)
        width = right-left
        measure_upper += width
        # Every value in the unresolved interval has m_-(xi)<=-lo.
        # Round upward in simple decimal units so the accumulated
        # certificate stays efficient to verify and explicitly outward.
        high = F(ceil_fraction((-lo)*DEN), DEN)
        assert high >= -lo >= 0
        neg_integral_positive_half_upper += high * width
        unverified.append((left, right, high))

    for j in range(END):
        visit(F(j), F(j+1), j, 0)

    # By evenness the complete negative set lies in both signed copies.
    total_measure_upper = 2*measure_upper
    total_negative_multiplier_integral_upper = 2*neg_integral_positive_half_upper

    # tr K_- = 2B int m_-; K_- is positive trace-class.
    trace_upper = 2*B*total_negative_multiplier_integral_upper
    assert measure_upper == F(243,16), f"unresolved half-band measure {float(measure_upper)}"
    assert total_measure_upper == F(243,8)
    assert trace_upper < 83, f"trace upper {float(trace_upper)}"
    assert accepted > 0 and leaves > 0
    assert maxdepth == DEPTH
    assert total_negative_multiplier_integral_upper > 0

    # For positive trace-class K_-, lambda_j <= tr(K_-)/j,
    # here j=302. The bound concerns K_- only, not the full Weil form.
    assert trace_upper / 302 < F(83,302)

    # Unresolved components can be grouped without changing coverage.
    unverified.sort(key=lambda z: z[0])
    runs = 0
    last_right = None
    for lo, hi, _ in unverified:
        if last_right != lo:
            runs += 1
        last_right = hi

    print("SI07 PASS: certified negativity support cover on [-896,896]")
    print("SI06 high-frequency positivity inherited: |xi|>=896")
    print("nonnegative intervals certified:",accepted)
    print("unresolved dyadic leaves:",leaves,"depth:",maxdepth)
    print("positive-frequency unresolved components:",runs)
    print("positive-half unresolved measure upper:",float(measure_upper))
    print("full negative-set Lebesgue measure upper:",float(total_measure_upper))
    print("full negative multiplier L1 mass upper:",float(total_negative_multiplier_integral_upper))
    print("physical K_- trace upper:",float(trace_upper))
    print("lambda_302(K_-) upper:",float(trace_upper/302))
    print("no claim of a competitive norm-tail at rank <=301")


if __name__ == "__main__":
    validate()
