#!/usr/bin/env python3
"""SI17: exact original odd supported ONE-DIRECTION concentration minorant.

SI16 used the odd frequency-concentration TRACE as an inverse chord endpoint.
SI17 instead approximates the *operator* in a narrow positive signed frequency
window by an explicit physical rank-one feature, with the ENTIRE operator-norm
Taylor remainder paid. A supported rank-one inverse gives a strictly smaller
upper bound for the same original odd BS response. No original inverse vector,
native full A-residual, finite full BS matrix, Stage I or RH is claimed.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import PI, B
from validate_rpb108_si12_even_supported_inverse import sinh_bounds, cosh_bounds
from validate_rpb108_si13_odd_fourier_reference import certify_window

KAPPA = F(1, 1000)
DELTA = F(1399, 1000)       # Actual original signed m>7/5 on [.22,.38].
CENTER = F(3, 10)
RADIUS = F(1, 125)         # J± = ±[.292,.308].
LEFT, RIGHT = CENTER-RADIUS, CENTER+RADIUS


def validate():
    # Replay full-original signed seven-prime + arch source on every
    # frequency of the inherited [0.22,0.38] continuum and its reflection.
    source_lower = certify_window()
    assert source_lower > F(7,5)
    assert F(11,50) < LEFT < CENTER < RIGHT < F(19,50)
    pi_lo, pi_hi = PI

    # Original odd physical source: s(x)=sinh(x/2); physically supported.
    # h(x)=sin(2*pi*CENTER*x), x in [-B,B], is an explicit ODD physical
    # feature, not an unphysical Fourier projection of s.
    #
    # |<s,h>|=|hat(Zs)(CENTER)| with original Fourier convention.
    theta_lo,theta_hi=F(4,25)*pi_lo,F(4,25)*pi_hi
    cos_theta_lo=1-theta_hi**2/2
    sin_theta_lo=theta_lo-theta_hi**3/6
    cslo,cshi=cosh_bounds(B/2)
    sslo,sshi=sinh_bounds(B/2)
    k_lo,k_hi=F(3,5)*pi_lo,F(3,5)*pi_hi
    amplitude_lo=(2*(cslo*cos_theta_lo/2+
                     k_lo*sslo*sin_theta_lo)/
                  (F(1,4)+k_hi*k_hi))
    assert amplitude_lo>F(541,1000)
    overlap_lower=F(541,1000)**2

    # ||h||² = B - sin(4*pi*B*CENTER)/(4*pi*CENTER).
    # 4*pi*B*CENTER=(33/25)*pi = pi + (8/25)*pi.
    # Thus ||h||² = B + sin(8*pi/25)/(4*pi*CENTER).
    # Alternating rational sine upper valid for 0<t<1.1:
    # sin(t)<=t-t³/6+t^5/120. Respect outward pi intervals.
    tlo,thi=F(8,25)*pi_lo,F(8,25)*pi_hi
    assert F(0)<tlo<thi<F(11,10)
    sine_upper=thi-tlo**3/6+thi**5/120
    h_norm_sq_upper=B+sine_upper/(4*pi_lo*CENTER)
    assert h_norm_sq_upper<F(133,100)
    H=F(133,100)

    # On H_odd, with h_xi(x)=sin(2*pi*xi*x), the original symmetric
    # supported frequency concentration equals
    # T_J=2∫_(CENTER-RADIUS)^(CENTER+RADIUS) |h_xi><h_xi| dxi.
    # Let F(xi)=|h_xi><h_xi|. Symmetric Taylor integration kills F'(CENTER).
    #
    # sup ||F''|| <= 2||h''|| ||h|| + 2||h'||².
    # ||h||²<=2B,
    # ||h'||²<=(2*pi)^2 (2B³/3),
    # ||h''||²<=(2*pi)^4 (2B^5/5).
    # Since sqrt(5)>2, sup ||F''|| <=(10/3)(2*pi)^2 B³.
    C=F(10,3)*(2*pi_hi)**2*B**3
    eps=F(2,3)*RADIUS**3*C
    # Certified ALL operator directions, not only a trace or pointwise
    # Fourier sample. 0<=T_J but T_J~4r hh* with signed operator error.
    assert F(0)<eps<F(1,16000)

    # Original supported odd positive operator A_odd has:
    # A_odd >= kappa I+delta*T_J
    #       >= (kappa-delta*eps)I + gamma|h><h|,
    # gamma=4*r*delta. This is a genuine Loewner MINORANT of A_odd.
    kp=KAPPA-DELTA*eps
    gamma=4*RADIUS*DELTA
    assert kp>F(9,10000)>0 and gamma>0

    # Sherman-Morrison INVERTS ONLY THE EXPLICIT SUPPORTED REFERENCE,
    # not A_odd or the unrestricted whole-line Fourier multiplier.
    #
    # <s,A_odd^-1 s> <= ||s||²/kp
    # -gamma|<s,h>|²/[kp(kp+gamma||h||²)].
    sblo,sbhi=sinh_bounds(B)
    norm_sq_up=sbhi-B
    assert norm_sq_up<F(235648,1000000)
    norm_cap=F(235648,1000000)
    scalar_term=2*norm_cap/kp
    gain=2*gamma*overlap_lower/(kp*(kp+gamma*H))
    response_upper=scalar_term-gain
    assert F(0)<response_upper<F(42)
    assert gain>F(470)
    assert response_upper<F(78)
    assert F(0)<F(2)*norm_cap/KAPPA-response_upper

    print("SI17 PASS: original supported odd rank-one concentration Loewner certificate")
    print("full original signed m minimum inherited:",float(source_lower))
    print("symmetric signed-positive J+:",float(LEFT),float(RIGHT))
    print("certified |<s,h>| lower:",float(amplitude_lo))
    print("certified ||h||² upper:",float(h_norm_sq_upper))
    print("uniform ODD concentration rank-one operator remainder <:",float(eps))
    print("positive supported reference scalar floor:",float(kp))
    print("one-direction reference coefficient:",float(gamma))
    print("rigorous actual odd-pole BS UPPER:",float(response_upper))
    print("previous SI16 upper was <78; new upper is <42")
    print("NOT full original inverse computation, full Weil positivity, Stage I or RH.")


if __name__=="__main__":
    validate()
