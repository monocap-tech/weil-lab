#!/usr/bin/env python3
"""SI19: exact Jensen minorant for original odd supported signed-positive bands.

The local time-frequency concentration integral itself (not an approximation)
dominates the rank-one projector on its *frequency-averaged* sine feature:
    2 integral_[c-r,c+r] |h_xi><h_xi| dxi >= 4r |g><g|
    g(x)=sin(2*pi*c*x)*sinc(2*pi*r*x), -B<=x<=B.
Consequently NO adverse Taylor operator-norm remainder must be subtracted
from the positive supported scalar floor kappa. Certify source overlaps and
physical Gram by rigorous comparison with SI18's exactly enclosed sine data.
All certificate decisions are exact Fraction comparisons, not floats.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import PI, B
from validate_rpb108_si12_even_supported_inverse import sinh_bounds
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si14_odd_multiband_nogo import certify_positive_window
from validate_rpb108_si18_odd_rank_two_woodbury import (
    CENTERS, RADIUS, DELTAS, gram, signed_odd_overlap,
)

KAPPA=F(1,1000)


def validate():
    # Original signed continuum positivity: both windows are strict.
    signed_first=certify_window()
    signed_second=certify_positive_window(F(73,100),F(79,100))
    assert signed_first>F(7,5)
    assert signed_second>F(1201,1000)
    c1,c2=CENTERS
    assert c1==F(3,10) and c2==F(19,25)
    assert RADIUS==F(1,125)
    assert c1+RADIUS<c2-RADIUS
    assert c1-RADIUS>F(11,50) and c1+RADIUS<F(19,50)
    assert c2-RADIUS>F(73,100) and c2+RADIUS<F(79,100)

    # For any physical odd f, Cauchy-Schwarz gives
    # 2 integral |<f,h_xi>|² dxi
    # >= 4r |<f,g_c>|²,
    # g_c=(2r)^-1 int h_xi dxi
    #     = sin(2*pi*c*x) sinc(2*pi*r*x).
    # Crucially the remainder T_J-4r|g_c><g_c| is POSITIVE,
    # not merely bounded in norm. Therefore the actual supported
    # A_odd >= kappa I + sum 4r*delta_j |g_j><g_j|,
    # with the ORIGINAL kappa=0.001 unchanged.
    gamma1,gamma2=(4*RADIUS*d for d in DELTAS)
    assert gamma1==F(44768,1000000)
    assert gamma2==F(384,10000)

    # sinc u = sin u/u, and 0<=1-sinc u<=u²/6 for |u|<=2*pi*r*B.
    # Therefore ||g_j-h_j||<=theta||h_j|| in L²(I), uniformly
    # for h_j(x)=sin(2*pi*c_j*x). The physical support stays fixed.
    theta=(2*PI[1]*RADIUS*B)**2/6
    assert theta<F(1,1900)
    sblo,sbhi=sinh_bounds(B)
    assert sbhi-B<F(235648,1000000)<F(1,4)
    # SI18 certifies ||h_j||²<133/100; thus ||s||||h_j||<7/12.
    HCAP=F(133,100)
    assert HCAP<F(49,36)
    q_err=theta*F(7,12)
    G_err=(2*theta+theta**2)*HCAP
    assert q_err<F(3,10000)  # <0.0003
    assert G_err<F(14,10000) # <0.0014

    # Regenerate EXACT original signed source overlap and supported Gram
    # via SI18 interval-rational sine/cosine/pi/sinh primitives.
    q1,q2=(signed_odd_overlap(c) for c in CENTERS)
    H11,H22=gram(c1,c1),gram(c2,c2)
    H12=gram(c1,c2)

    # Strict high-precision outward rational enclosures (no decimal fits).
    assert F(54225,100000)<q1[0]<=q1[1]<F(54227,100000)
    assert F(-16620,100000)<q2[0]<=q2[1]<F(-16617,100000)
    assert F(132395,100000)<H11[0]<=H11[1]<F(132398,100000)
    assert F(119237,100000)<H22[0]<=H22[1]<F(119240,100000)
    assert F(-14277,100000)<H12[0]<=H12[1]<F(-14274,100000)

    # Every actual averaged feature G_j satisfies
    # |<s,G_j>-<s,h_j>| <= q_err.
    # |<G_i,G_j>-<h_i,h_j>| <= G_err.
    assert q1[0]-q_err>F(5419,10000)
    assert q1[1]+q_err<F(5426,10000)
    assert q2[0]-q_err>F(-1666,10000)
    assert q2[1]+q_err<F(-1658,10000)
    assert H11[0]-G_err>F(13225,10000)
    assert H11[1]+G_err<F(13254,10000)
    assert H22[0]-G_err>F(11909,10000)
    assert H22[1]+G_err<F(11938,10000)
    assert H12[0]-G_err>F(-1442,10000)
    assert H12[1]+G_err<F(-1413,10000)

    # Exact physical supported reference C0=kappa I+H Gamma H*,
    # H=(G_1,G_2), Gamma=diag(4r delta_j), q=H*s and M=Gamma^-1+Gram/kappa.
    # Woodbury:
    # <s,C0^-1 s> = ||s||²/kappa - q*M^-1*q/kappa².
    # q1>0, q2<0, offdiag b<0 => -2b q1q2 <0,
    # i.e. the mixed term is ADVERSE and must be subtracted.
    q1min=F(5419,10000);q1max=F(5426,10000)
    q2absmin=F(1658,10000);q2absmax=F(1666,10000)
    g11min,g11max=F(13225,10000),F(13254,10000)
    g22min,g22max=F(11909,10000),F(11938,10000)
    babsmin,babsmax=F(1413,10000),F(1442,10000)
    a_min=1/gamma1+g11min/KAPPA
    a_max=1/gamma1+g11max/KAPPA
    d_min=1/gamma2+g22min/KAPPA
    d_max=1/gamma2+g22max/KAPPA
    N_min=(d_min*q1min**2
           -2*(babsmax/KAPPA)*q1max*q2absmax
           +a_min*q2absmin**2)
    assert N_min>0
    # Crucial: determinant is ad-b², NOT ad.
    D_max=a_max*d_max-(babsmin/KAPPA)**2
    assert D_max>0
    correction_min=N_min/D_max/KAPPA**2
    actual_inverse_upper=2*(F(235648,1000000)/KAPPA-correction_min)
    assert F(0)<actual_inverse_upper<F(18,1)
    assert actual_inverse_upper<F(29,1)

    print("SI19 PASS: exact supported Jensen rank-two positive minorant")
    print("FULL signed positive window minima:",float(signed_first),float(signed_second))
    print("Exact Jensen averaging: T_J >= 4r |g><g|, g=sine*sinc")
    print("No adverse full operator remainder; reference floor:",float(KAPPA))
    print("center sine-to-averaged feature norm relative error:",float(theta))
    print("strict original physical overlap error upper:",float(q_err))
    print("strict original physical Gram error upper:",float(G_err))
    print("correct-sign rank-two Woodbury scalar inverse UPPER:",float(actual_inverse_upper))
    print("SI18 certified upper <29; SI19 certified upper <18")
    print("No full original A^-1s, complete negative-frequency BS, Stage I or RH.")


if __name__=="__main__":
    validate()
