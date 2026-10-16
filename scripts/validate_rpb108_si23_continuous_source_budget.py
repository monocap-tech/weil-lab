#!/usr/bin/env python3
"""SI23: continuous positive-frequency recovery of SI22's original s-witness deficit.

Uses the complete certified SI13 original signed interval [0.22,0.38] but
only the TWO pieces NOT occupied by SI21's first Jensen window.
The added positive operator is an actual continuous-frequency integral,
NOT an extra rank-one midpoint approximation. On the original supported
odd pole vector s, certify C23-K_pole is strictly positive.

This is a one-input quadratic test, NOT whole-operator positivity, a
Birman-Schwinger norm upper, global Weil positivity, Stage I, or RH.
All accepting inequalities are exact Fraction calculations.
"""
from fractions import Fraction as F

from validate_rpb108_si21_odd_jensen_four import (
    B, KAPPA, PI, CENTERS, DELTAS, RADIUS,
    certify_original_window, averaged_q_interval, outward,
)
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si18_odd_rank_two_woodbury import signed_odd_overlap
from validate_rpb108_si12_even_supported_inverse import sinh_bounds, cosh_bounds

# Outer subintervals of SI13 [.22,.38], away from SI21 [.28,.32].
# The positive operator increment is delta * 2 int_{outer}
#     |sin(2pi xi x)><sin(2pi xi x)| dxi
# on the actual odd, physically supported Hilbert space.
OUTER = ((F(11, 50), F(7, 25)), (F(8, 25), F(19, 50)))
OUTER_DELTA = F(1399, 1000)


def bounds_square(q):
    lo, hi = q
    if lo <= 0 <= hi:
        return F(0), max(lo*lo, hi*hi)
    return min(lo*lo, hi*hi), max(lo*lo, hi*hi)


def certify():
    assert OUTER == ((F(22,100), F(28,100)),
                     (F(32,100), F(38,100)))
    assert CENTERS[0]-RADIUS == OUTER[0][1]
    assert CENTERS[0]+RADIUS == OUTER[1][0]
    assert F(0) < OUTER[0][0] < OUTER[0][1] < OUTER[1][0] < OUTER[1][1]
    assert all(CENTERS[i]-RADIUS > OUTER[1][1] for i in range(1,4))

    # SI13 is an all-frequency proof on [.22,.38], not a grid sample.
    m_outer_min = certify_window()
    assert m_outer_min > KAPPA + OUTER_DELTA == F(7,5)

    # Keep all original SI21 positive minorants, with no energy overlaps.
    m_jensen = [certify_original_window(c, d)
                for c,d in zip(CENTERS, DELTAS)]
    assert len(m_jensen) == 4
    assert all(m > KAPPA + d for m,d in zip(m_jensen, DELTAS))

    sinh_B_lo, sinh_B_hi = sinh_bounds(B)
    Slo, Shi = sinh_B_lo-B, sinh_B_hi-B
    assert F(235,1000) < Slo < Shi < F(236,1000)

    # Rigorous bound |d/dxi <s,h_xi>| <= 2pi int |x s(x)| dx
    # = 2pi(4B*cosh(B/2)-8*sinh(B/2)) < 3 (SI13).
    s_half_lo, _ = sinh_bounds(B/2)
    _, c_half_hi = cosh_bounds(B/2)
    derivative_hi = 2*PI[1]*(4*B*c_half_hi-8*s_half_lo)
    assert 0 < derivative_hi < F(3)

    # TRUE continuous-frequency source energy. The midpoint amplitudes
    # and all between-midpoint values are bounded using SI18's rigorous
    # original analytic supported sine-overlap enclosure and Lipschitz.
    extras = []
    for left,right in OUTER:
        center = (left+right)/2
        halfwidth = (right-left)/2
        qlo,qhi = signed_odd_overlap(center)
        amp_lower = qlo-derivative_hi*halfwidth
        assert qlo > F(1,2)  # holds at both .25 and .35 centers
        assert amp_lower > F(43,100)
        # On every frequency in outer subinterval, q(xi)>=amp_lower>0.
        extras.append((center, amp_lower,
                       2*OUTER_DELTA*(right-left)*amp_lower*amp_lower))
    increment_lower = sum((item[2] for item in extras), F(0))
    assert increment_lower > F(63,1000)

    # SI21 four original true averaged-frequency Jensen vectors.
    tau = (4*PI[1]*RADIUS*B)**4/F(2880)
    assert F(0) < tau < F(3,10**6)
    qerr = F(3,4)*tau
    true_q = []
    for c in CENTERS:
        lo,hi = averaged_q_interval(c)
        true_q.append(outward((lo-qerr,hi+qerr)))
    assert true_q[0][0]>0 and true_q[1][1]<0
    assert true_q[2][0]>0 and true_q[3][1]<0
    gammas = [4*RADIUS*d for d in DELTAS]

    # C4 is EXACT rank-four Jensen reference. Its quadratic is computed
    # through rigorous signed true-average physical source intervals.
    C4_lo = KAPPA*Slo + sum(
        (gamma*bounds_square(q)[0]
         for gamma,q in zip(gammas,true_q)), F(0))
    C4_hi = KAPPA*Shi + sum(
        (gamma*bounds_square(q)[1]
         for gamma,q in zip(gammas,true_q)), F(0))
    pole_lo, pole_hi = 2*Slo*Slo, 2*Shi*Shi
    deficit_lower = pole_lo-C4_hi
    assert deficit_lower > F(44,1000)  # SI22 obstruction rechecked

    # C23=C4+delta*T_outer on the true supported odd space:
    # positive LOEWNER minorant A_odd >= C23 >= C4 >= kappa I.
    #
    # Only assert positivity of the physical s quadratic, not
    # (C23-K_pole)>=0 as an operator.
    C23_source_lo = C4_lo + increment_lower
    surplus_lo = C23_source_lo - pole_hi
    assert surplus_lo > F(18,1000)
    assert increment_lower > deficit_lower

    # The s-input Rayleigh quotient drops below 1, but this is NOT
    # the supremum BS norm: the maximizing input need not be s.
    s_rayleigh_hi = pole_hi / C23_source_lo
    assert 0 < s_rayleigh_hi < F(9,10)

    print("SI23 PASS: continuous original positive-frequency source budget closes SI22 s-witness obstruction")
    print("SI13 strict signed all-frequency m lower on full [.22,.38]:", float(m_outer_min))
    print("outer half-open frequency portions:",[(float(a),float(b)) for a,b in OUTER])
    print("retained original positive margin delta:",float(OUTER_DELTA))
    print("source-frequency derivative upper:",float(derivative_hi))
    print("physical midpoint amplitudes lower:",[(float(c),float(a)) for c,a,_ in extras])
    print("extra TRUE continuous-frequency positive source quadratic LOWER:",float(increment_lower))
    print("SI22 rank-four source reference lower/upper:",float(C4_lo),float(C4_hi))
    print("original pole quadratic lower/upper:",float(pole_lo),float(pole_hi))
    print("SI22 original deficit lower:",float(deficit_lower))
    print("SI23 augmented reference source quadratic LOWER:",float(C23_source_lo))
    print("augmented reference s-source surplus strict LOWER:",float(surplus_lo))
    print("s-witness Rayleigh quotient UPPER (not full BS norm):",float(s_rayleigh_hi))
    print("NO C23 whole odd positivity, NO C23 inverse norm upper, NO full signed BS/Stage I/RH")


if __name__ == "__main__":
    certify()
