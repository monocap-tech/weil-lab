#!/usr/bin/env python3
"""SI18: exact-rational rank-two odd supported positive Loewner minorant.

Original CC27 / RC312-313 signed 7-prime Fourier multiplier:
two *entire*, certified sign-positive bands, supported sine features,
a rigorous Banach Taylor *operator* remainder in each band,
a strictly positive supported rank-two reference, and a conservative
correct-sign Woodbury inverse bound. Never replaces A^-1 by whole-line 1/a.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import PI, B
from validate_rpb108_si12_even_supported_inverse import sinh_bounds, cosh_bounds
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si14_odd_multiband_nogo import (
    certify_positive_window, cos_sin_pi_multiple,
)

KAPPA=F(1,1000)
CENTERS=(F(3,10), F(19,25))  # 0.30 and 0.76
RADIUS=F(1,125)
DELTAS=(F(1399,1000),F(6,5))  # strict original m>1.4 and >1.201
PI_LO,PI_HI=PI


def add(x,y):
    return (x[0]+y[0],x[1]+y[1])


def neg(x):
    return (-x[1],-x[0])


def sub(x,y):
    return add(x,neg(y))


def mul(x,y):
    a,b=x
    c,d=y
    z=(a*c,a*d,b*c,b*d)
    return (min(z),max(z))


def div(x,y):
    assert y[0]>0 or y[1]<0, "denominator interval contains zero"
    return mul(x,(1/y[1],1/y[0]))


def sin_pi(q):
    return cos_sin_pi_multiple(q)[0]


def signed_odd_overlap(c):
    """Exact integral <s,sin(2 pi c x)> on supported physical interval."""
    slo,shi=sinh_bounds(B/2)
    clo,chi=cosh_bounds(B/2)
    k=(2*PI_LO*c,2*PI_HI*c)
    sinpart,cospart=cos_sin_pi_multiple(2*B*c)
    first=mul((clo/2,chi/2),sinpart)
    second=mul(mul(k,(slo,shi)),cospart)
    numerator=mul((F(2),F(2)),sub(first,second))
    denom=(F(1,4)+k[0]**2,F(1,4)+k[1]**2)
    return div(numerator,denom)


def gram(c,d):
    """Physical exact <sin(2 pi c x),sin(2 pi d x)>."""
    if c==d:
        term_a=(B,B)
    else:
        term_a=div(sin_pi(2*B*(c-d)),(
            2*PI_HI*(c-d) if c-d<0 else 2*PI_LO*(c-d),
            2*PI_LO*(c-d) if c-d<0 else 2*PI_HI*(c-d)
        ))
    term_b=div(sin_pi(2*B*(c+d)),(
        2*PI_LO*(c+d),2*PI_HI*(c+d)
    ))
    return sub(term_a,term_b)


def validate():
    # Two entire certified signed-original positive Fourier neighborhoods.
    orig=certify_window()
    second=certify_positive_window(F(73,100),F(79,100))
    assert orig>F(7,5)
    assert second>F(1201,1000)
    c1,c2=CENTERS
    assert F(11,50)<c1-RADIUS<c1+RADIUS<F(19,50)
    assert F(73,100)<c2-RADIUS<c2+RADIUS<F(79,100)
    assert c1+RADIUS<c2-RADIUS

    # Each symmetric J_i contributes on odd space
    # T_i=2int_(c_i-r)^(c_i+r) |h_xi><h_xi|dxi.
    # With uniform ||F''(xi)||<C for F=|h><h|,
    # ||T_i-4r|h_ci><h_ci||| <= (2/3)r³ C.
    C=F(10,3)*(2*PI_HI)**2 * B**3
    eps=F(2,3)*RADIUS**3*C
    assert 0<eps<F(1,16000)

    kp=KAPPA-sum(DELTAS)*eps
    g1,g2=(4*RADIUS*d for d in DELTAS)
    assert F(8,10000)<kp<KAPPA
    # Original A_odd >= kappa I + sum_i delta_i T_i
    # >= kp I + g1|h1><h1| + g2|h2><h2|.
    # This is a full physical-operator Loewner MINORANT, not sampled.

    q1,q2=(signed_odd_overlap(c) for c in CENTERS)
    G11,G22=gram(c1,c1),gram(c2,c2)
    G12=gram(c1,c2)

    # Every one of these named constraints follows from rational sine,
    # cosine, pi, sinh, cosh Taylor intervals, not float sampling.
    assert F(541,1000)<q1[0]<q1[1]<F(543,1000),q1
    assert F(-167,1000)<q2[0]<q2[1]<F(-165,1000),q2
    assert F(1323,1000)<G11[0]<G11[1]<F(1325,1000),G11
    assert F(1191,1000)<G22[0]<G22[1]<F(1194,1000),G22
    assert F(-144,1000)<G12[0]<G12[1]<F(-141,1000),G12

    # Woodbury for C_o=kp I + H diag(g1,g2) H*, where
    # H=[h1,h2], G_ij=<h_i,h_j>, q_i=<s,h_i>:
    # <s,C_o^-1 s> = ||s||²/kp -
    #       q* (diag(1/g_i)+G/kp)^-1 q / kp².
    #
    # M=[[a,b],[b,d]], with a,d>0 and b<0; q1>0,q2<0.
    # Its positive correction has numerator
    # d*q1²-2*b*q1*q2+a*q2², denominator ad-b².
    # Lower-bound numerator by conservative SIGN-AWARE rational constants;
    # upper-bound determinant by amax*dmax (ignore -b²).
    a_min=1/g1+F(1323,1000)/kp
    a_max=1/g1+F(1325,1000)/kp
    d_min=1/g2+F(1191,1000)/kp
    d_max=1/g2+F(1194,1000)/kp
    b_abs_max=F(144,1000)/kp
    N_min=(d_min*F(541,1000)**2
            -2*b_abs_max*F(543,1000)*F(167,1000)
            +a_min*F(165,1000)**2)
    assert N_min>0
    correction_min=N_min/(a_max*d_max)/kp**2

    slo,shi=sinh_bounds(B)
    S_up=F(235648,1000000)
    assert shi-B<S_up
    response_ub=2*(S_up/kp-correction_min)
    assert F(0)<response_ub<F(29)
    assert response_ub<F(42)

    # Actual M determinant >0 follows from diag(1/g1,1/g2)>0
    # and G a true physical Gram PSD; approximate bound itself checked.
    print("SI18 PASS: original signed rank-two supported odd Woodbury certificate")
    print("signed original whole-band minima:",float(orig),float(second))
    print("centers and symmetric halfwidth:",tuple(float(c) for c in CENTERS),float(RADIUS))
    print("full physical Taylor operator remainder each:",float(eps))
    print("positive reference floor:",float(kp))
    print("rank-two gamma coefficients:",float(g1),float(g2))
    print("exact-rational overlap intervals:",tuple(float(z) for z in q1),tuple(float(z) for z in q2))
    print("exact-rational physical Gram intervals:",
          tuple(float(z) for z in G11),tuple(float(z) for z in G22),
          tuple(float(z) for z in G12))
    print("certified full supported inverse UPPER:",float(response_ub),"<29")
    print("previous SI17 certified upper was <42")
    print("NO exact A^-1s, native full A-residual, coupled original Weil positivity, Stage I or RH.")


if __name__=="__main__":
    validate()
