#!/usr/bin/env python3
"""EF01: original signed even packet parity rank and exact error regression.

Reuses the SI10 original complete seven-prime protected cover and SI08
per-cluster Taylor orders; tests the even *reduction*, not the missing
actual even inverse Gram, coupled finite eigenvalue, whole Weil or RH.
"""
from fractions import Fraction as F

from validate_rpb108_si10_complement_positivity import (
    KAPPA, protected_inner_cover, protected_outer_band
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import B


FULL_RANK = {
    9: 939, 10: 1003, 12: 1121, 16: 1367,
    20: 1561, 21: 1631, 24: 1781, 32: 2151,
}
EVEN_RANK_CEILING = {
    9: 469, 10: 501, 12: 560, 16: 683,
    20: 780, 21: 815, 24: 890, 32: 1075,
}


def transpose(a):
    return [list(row) for row in zip(*a)]


def product(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse2(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert det > 0
    return [[a[1][1] / det, -a[0][1] / det],
            [-a[1][0] / det, a[0][0] / det]]


def plus(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[i]))]
            for i in range(len(a))]


def minus(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[i]))]
            for i in range(len(a))]


def scale(k, a):
    return [[k*x for x in row] for row in a]


def model_pole_regression():
    # Finite algebra identity ONLY; not the original even inverse.
    a0 = [[F(2), F(1, 4)], [F(1, 4), F(3)]]
    c = [[F(1)], [F(2, 3)]]
    pole = scale(F(2), product(c, transpose(c)))
    a = plus(a0, pole)
    i0 = inverse2(a0)
    w = product(i0, c)
    denom = F(1) + 2 * product(transpose(c), w)[0][0]
    assert denom > 1
    correction = scale(F(2) / denom, product(w, transpose(w)))
    exact = minus(i0, correction)
    assert exact == inverse2(a)
    assert correction[0][0] > 0
    assert correction[1][1] > 0
    assert correction[0][0]*correction[1][1] == correction[0][1]**2
    print("EF01 model algebra: supported positive-pole inverse correction has correct sign")


def validate():
    outer_count, outer_min = protected_outer_band()
    assert outer_count == 2535 and outer_min > KAPPA

    groups, width, mass, leaves, protected = protected_inner_cover()
    assert len(groups) == 107 and leaves == 973 and protected == 9261
    assert width == F(973, 32)
    assert mass == F(1203060883, 32000000)
    assert B == F(11, 10) and KAPPA == F(1, 1000)
    total_r = mass + KAPPA * width
    assert total_r == F(1204033883, 32000000) < 38

    for bits in FULL_RANK:
        orders = [taylor_order(right-left, bits)[0]
                  for left, right, _ in groups]
        assert all(isinstance(p, int) and p > 0 for p in orders)
        d = sum(orders)
        assert d == EVEN_RANK_CEILING[bits]
        assert 1 + 2*d == FULL_RANK[bits]
        eps = F(1, 2**bits)
        eta = 4 * B * total_r * eps
        cofinite_floor = KAPPA - 2*B*total_r*eps**2
        complement_k = 2*B*total_r*eps**2
        assert cofinite_floor > 0
        assert 0 < complement_k < KAPPA
        assert 0 < eta and eta / KAPPA > 0

        if bits == 9:
            assert d == 469 and cofinite_floor > F(68, 100000)
            assert eta / KAPPA < F(323349, 1000)
        if bits == 20:
            assert d == 780 and eta / KAPPA < F(157886, 10**6)
        if bits == 24:
            assert d == 890 and eta / KAPPA < F(9868, 10**6)
        if bits == 32:
            assert d == 1075 and eta / KAPPA < F(38547, 10**9)

        print("b", bits, "even-rank <=", d, "cofinite-floor >=",
              float(cofinite_floor), "full-negative eta/kappa <=",
              float(eta/KAPPA), flush=True)

    model_pole_regression()
    print("EF01 PASS: even SI10 original signed cofinite rank halved;",
          "whole-negative spectral remainder preserved", flush=True)
    print("W-EVEN-FORM OPEN: full original finite inverse eigenvalue",
          "and cross-coupling not certified", flush=True)


if __name__ == "__main__":
    validate()
