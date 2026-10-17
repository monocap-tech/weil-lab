#!/usr/bin/env python3
"""EF02: original even physically supported negative-frequency rank certificate.

Reuses the SM04 complete original seven-prime signed continuum certificates,
but independently constructs the EVEN cosine Gram and 15 true averaged
even Jensen vectors. This is a method-class obstruction only: it cannot
establish negativity or positivity of the original complete even Weil form.
"""
from fractions import Fraction as F

from validate_rpb108_sm04_negative_packet_rank import (
    CENTERS, N, RADIUS, DELTA, original_negative_certificates,
)
from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_si18_odd_rank_two_woodbury import (
    sin_pi, div, add,
)
from validate_rpb108_si21_odd_jensen_four import KAPPA


def abs_up(interval):
    assert interval[0] <= interval[1]
    return max(abs(interval[0]), abs(interval[1]))


def even_cosine_gram(c, d):
    """Exact interval for ∫_-B^B cos(2πcx)cos(2πdx) dx.

    sin[2πB(c-d)]/[2π(c-d)] + sin[2πB(c+d)]/[2π(c+d)].
    c,d positive, and same-center limit of first term is B.
    """
    if c == d:
        first = (B, B)
    else:
        difference = c - d
        denominator = (
            2 * (PI[1] if difference < 0 else PI[0]) * difference,
            2 * (PI[0] if difference < 0 else PI[1]) * difference
        )
        assert (denominator[0] > 0 and denominator[1] > 0) or (denominator[0] < 0 and denominator[1] < 0)
        first = div(sin_pi(2 * B * difference), denominator)
    positive_sum = c + d
    second = div(sin_pi(2 * B * positive_sum),
                 (2 * PI[0] * positive_sum, 2 * PI[1] * positive_sum))
    return add(first, second)


def physical_even_gram_lower():
    # The 15 true even packets are g_j(x)=cos(2π c_j x)
    # sinc(2πρx). Both frequency reflections are charged.
    eps = (2 * PI[1] * RADIUS * B)**2 / 6
    assert F(0) < eps < F(1,100)
    diag = []
    off = []
    for i, c in enumerate(CENTERS):
        gii = even_cosine_gram(c, c)
        assert gii[0] > 0
        diag_lower = (1-eps)**2 * gii[0]
        off_upper = F(0)
        for j, d in enumerate(CENTERS):
            if i == j:
                continue
            gij = even_cosine_gram(c, d)
            off_upper += abs_up(gij) + 4 * B * eps
        diag.append(diag_lower)
        off.append(off_upper)
    gersh = min(a-b for a,b in zip(diag,off))
    gamma = 4 * RADIUS * DELTA
    assert gamma == F(2,125)
    assert N == 15 and len(diag) == N
    assert min(diag) > F(109,100), float(min(diag))
    assert max(off) < F(15,100), float(max(off))
    assert gersh > F(93,100), float(gersh)
    assert gamma * gersh > F(3,200), float(gamma * gersh)
    assert gamma * gersh > KAPPA
    return gersh, gamma*gersh, eps, min(diag), max(off)


def validate():
    signed_upper = original_negative_certificates()
    assert signed_upper < -DELTA
    gersh, floor, eps, diag_min, off_max = physical_even_gram_lower()
    print("EF02 true-original signed-negative entire bands:", N, flush=True)
    print("EF02 original whole-band multiplier upper:",float(signed_upper),flush=True)
    print("EF02 true averaged EVEN Jensen sinc error upper:",float(eps),flush=True)
    print("EF02 exact physical even Gram min diagonal lower:",float(diag_min),flush=True)
    print("EF02 exact physical even Gram max offrow upper:",float(off_max),flush=True)
    print("EF02 fifteen-vector EVEN Gram eigenvalue lower:",float(gersh),flush=True)
    print("EF02 lambda_15(K_freq,even) rigorous lower:",float(floor),flush=True)
    print("EF02 baseline scalar kappa:",float(KAPPA),flush=True)
    print("EF02 PASS: all kappa-I plus rank<=14 positive references fail to dominate original even K_freq",flush=True)
    print("In particular kappa-I + 2|cosh(x/2)><cosh(x/2)| + rank<=13 cannot suffice.",flush=True)
    print("W-EVEN-FORM OPEN: true A0,even has infinite-rank positive structure, not represented by a low-rank reference.",flush=True)


if __name__ == "__main__":
    validate()
