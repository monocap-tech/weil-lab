#!/usr/bin/env python3
"""SI22 — exact original-supported odd pole obstruction for SI21's rank-four reference.

Prove that the *reference* C_4 - 2|s><s| is NOT positive, and therefore
C_4 cannot by itself certify the complete negative-frequency BS gate.
No claim that the ORIGINAL A_o - K_o is nonpositive: A_o >= C_4.
All accepting inequalities are exact Fraction computations on certified
physical overlaps and sinh intervals from SI21 / SI12.
"""
from fractions import Fraction as F

from validate_rpb108_si21_odd_jensen_four import (
    B, KAPPA, CENTERS, RADIUS, DELTAS, PI,
    averaged_q_interval, certify_original_window, outward,
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds


def certify():
    # Reverify every original-signed positive-frequency margin.
    # The intervals reflect under xi -> -xi; no frequency-grid inference.
    minima = [certify_original_window(c, delta)
              for c, delta in zip(CENTERS, DELTAS)]
    assert len(CENTERS) == len(DELTAS) == len(minima) == 4
    assert all(value > KAPPA + delta
               for value, delta in zip(minima, DELTAS))

    # On actual physical [-B,B], the original signed odd pole is
    # s(x)=sinh(x/2), with exact ||s||² = sinh(B)-B.
    sinh_lo, sinh_hi = sinh_bounds(B)
    Slo, Shi = sinh_lo - B, sinh_hi - B
    assert F(235, 1000) < Slo < Shi < F(236, 1000)

    # True Jensen feature g_c = mean_{xi in [c-r,c+r]} sin(2pi xi x).
    # SI21's uniform Simpson error, not pointwise h_c replacement:
    tau = (4 * PI[1] * RADIUS * B)**4 / F(2880)
    assert F(0) < tau < F(3, 10**6)
    qerr = F(3, 4) * tau  # ||s|| < 1/2, ||1||_{L2(I)} < 3/2
    q = []
    for c in CENTERS:
        a,b = averaged_q_interval(c)
        q.append(outward((a-qerr, b+qerr)))

    assert all(lo < hi for lo, hi in q)
    # Source-overlap signs are original physical signed projections.
    assert q[0][0] > 0 and q[1][1] < 0
    assert q[2][0] > 0 and q[3][1] < 0

    # Rigorous upper bound on <s,C_4 s>, using ALL four positive
    # reference features, NOT deleting any off-diagonal terms:
    # <s,C_4 s> = kappa*S + sum gamma_i * |<s,g_i>|².
    gammas = [4 * RADIUS * delta for delta in DELTAS]
    q_squared_hi = [max(lo*lo, hi*hi) for lo,hi in q]
    C4_s_hi = KAPPA * Shi + sum((g*x for g,x in zip(gammas, q_squared_hi)), F(0))

    # Pole contributes exactly <s, 2|s><s| s> = 2*S².
    pole_s_lo = 2 * Slo*Slo
    deficit_lo = pole_s_lo - C4_s_hi
    assert C4_s_hi > 0
    assert deficit_lo > F(44,1000)  # >0.044 absolute quadratic deficit

    # Rayleigh-quotient variational characterization of the referenced
    # pole-only Birman-Schwinger operator:
    #
    # || C_4^{-1/2} (2|s><s|) C_4^{-1/2} ||
    # = sup_{f !=0} 2|<s,f>|²/<f,C_4 f>
    # >= 2*S²/<s,C_4 s> >= pole_s_lo / C4_s_hi > 33/20.
    #
    # Since the complete SI11 K_odd >= 2|s><s|, its C4-referenced
    # BS norm is also >33/20. This says NOTHING about original A_odd.
    ratio_lower = pole_s_lo / C4_s_hi
    assert ratio_lower > F(33,20)
    assert ratio_lower < F(2)   # sanity on this specific witness ratio

    # A NEW reference with positive extra contribution Delta >=0 must
    # satisfy <s,Delta s> >=2*S²-<s,C4 s> >0.044 to even avoid this
    # single physical witness obstruction; NOT sufficient for full BS.
    necessary_extra = deficit_lo

    print("SI22 PASS: original physical SI21 rank-four reference obstruction")
    print("SI21 signed window minima:", *(float(m) for m in minima))
    print("source norm squared interval:", float(Slo), float(Shi))
    print("source overlap outward intervals:", [(float(a),float(b)) for a,b in q])
    print("C4 quadratic upper on s:", float(C4_s_hi))
    print("original odd-pole negative quadratic lower on s:", float(pole_s_lo))
    print("strict deficit lower (pole - reference):", float(deficit_lo))
    print("reference-only pole BS norm lower:", float(ratio_lower))
    print("necessary extra positive quadratic <s,Delta s> >",
          float(necessary_extra))
    print("NO original Weil negativity, NO original A^-1 lower, NO full signed BS or RH")


if __name__ == "__main__":
    certify()
