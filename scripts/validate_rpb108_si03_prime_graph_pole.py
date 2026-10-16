#!/usr/bin/env python3
"""SI03: exact rational enclosures for finite shift-graph norm and pole absorption."""
from fractions import Fraction as F
from math import isqrt, factorial

B = F(11, 10)
ACTIVE = (2, 3, 4, 5, 7, 8, 9)
PRIME = {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2, 9: 3}
LENGTH = {2: 4, 3: 3, 4: 2, 5: 2, 7: 2, 8: 2, 9: 2}


def log_bounds(p, terms=140):
    """atanh series, outward rational remainder for ln(p), p>1."""
    t = F(p - 1, p + 1)
    power = t
    lo = F(0)
    for k in range(terms):
        lo += 2 * power / F(2 * k + 1)
        power *= t * t
    remainder = 2 * power / (F(2 * terms + 1) * (1 - t * t))
    return lo, lo + remainder


def sqrt_bounds(n, places=55):
    """Rational integer-square-root floor and ceiling."""
    scale = 10**places
    root = isqrt(n * scale * scale)
    lo = F(root, scale)
    hi = lo if root * root == n * scale * scale else F(root + 1, scale)
    assert lo * lo <= n <= hi * hi
    return lo, hi


def sinh_bounds(x, terms=24):
    """Positive Taylor partial sum and geometric-ratio remainder."""
    lo = sum(
        (x ** (2*k+1) / factorial(2*k+1) for k in range(terms)), F(0)
    )
    first = x ** (2 * terms + 1) / factorial(2 * terms + 1)
    ratio = x*x / F((2*terms+2) * (2*terms+3))
    assert 0 < ratio < 1
    return lo, lo + first / (1-ratio)


def path_poly(L):
    """Characteristic polynomial of length-L path adjacency."""
    q0 = [F(1)]
    if L == 0:
        return q0
    q1 = [F(0), F(1)]
    for _ in range(2, L+1):
        xq = [F(0)] + q1
        prev = q0 + [F(0)] * (len(xq) - len(q0))
        q0, q1 = q1, [u-v for u,v in zip(xq, prev)]
    return q1


def validate():
    lb = {p: log_bounds(p) for p in (2, 3, 5, 7)}
    logs = {
        n: tuple(k*v for v in lb[PRIME[n]])
        for n, k in ((2,1), (3,1), (4,2), (5,1),
                     (7,1), (8,3), (9,2))
    }
    # The exact geometric regimes determining the maximal fiber path length.
    assert B/2 < logs[2][0] and logs[2][1] < 2*B/3
    assert 2*B/3 < logs[3][0] and logs[3][1] < B
    for n in ACTIVE[2:]:
        assert B < logs[n][0] and logs[n][1] < 2*B

    w = {}
    for n in ACTIVE:
        llog, ulog = lb[PRIME[n]]
        srlo, srhi = sqrt_bounds(n)
        w[n] = (llog/srhi, ulog/srlo)

    rt2 = sqrt_bounds(2)
    rt5 = sqrt_bounds(5)
    factor = {
        2: ((1+rt5[0])/2, (1+rt5[1])/2),
        3: rt2,
        4: (F(1), F(1)), 5: (F(1), F(1)),
        7: (F(1), F(1)), 8: (F(1), F(1)), 9: (F(1), F(1)),
    }
    Mlo = sum((w[n][0]*factor[n][0] for n in ACTIVE), F(0))
    Mhi = sum((w[n][1]*factor[n][1] for n in ACTIVE), F(0))
    Clo = sum((w[n][0] for n in ACTIVE), F(0))
    Chi = sum((w[n][1] for n in ACTIVE), F(0))
    gaplo, gaphi = 2*Clo-Mhi, 2*Chi-Mlo
    slo, shi = sinh_bounds(B)
    polemax = 2*(shi-B)
    lower = gaplo-polemax

    assert Mlo <= Mhi < F(410315,100000)
    assert gaplo > F(297185,100000)
    assert lower > F(25005,10000)
    assert gaplo <= gaphi
    assert all(LENGTH[n] == (4 if n==2 else 3 if n==3 else 2)
               for n in ACTIVE)

    # Three path characteristic polynomials, in increasing degree order:
    # x^2-1, x(x^2-2), (x^2-x-1)(x^2+x-1).
    assert path_poly(2) == [-1,0,1]
    assert path_poly(3) == [0,-2,0,1]
    assert path_poly(4) == [1,0,-3,0,1]

    print("SI03 PASS: rational 7-prime path lengths, gap, signed-pole absorption")
    for name, low, high in (
        ("prime norm upper M", Mlo, Mhi),
        ("prime scalar 2C", 2*Clo, 2*Chi),
        ("prime Dirichlet gap", gaplo, gaphi),
        ("gap after signed odd pole", lower, gaphi-2*(slo-B)),
    ):
        print(f"{name}: [{float(low):.13f}, {float(high):.13f}]")
    print("shift-path lengths:", LENGTH)


if __name__ == "__main__":
    validate()
