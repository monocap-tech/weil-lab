#!/usr/bin/env python3
"""SI13: rigorous positive original Fourier window improves the ODD supported
A^{-1} inverse response. All source/margin decisions exact Fraction only.

The original full signed CC27/RC312-313 m is imported through SI06's
prime_interval; no unsupported whole-line reciprocal used.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import (
    PI, B, YFAC, CONST_UP, prime_interval, log_rational_bounds,
)
from validate_rpb108_si12_even_supported_inverse import (
    sinh_bounds, cosh_bounds,
)

KAPPA=F(1,1000)
DELTA=F(1)
LOW=F(11,50)   # 0.22
HIGH=F(19,50)  # 0.38
CENTER=F(3,10) # 0.30
CELLS=128
K=128


def arch_lower(x):
    """Exact arch lower at positive rational x, monotonic for larger xi."""
    a=F(1,4)
    y=YFAC*x
    partial=sum((y*y/((k+a)*((k+a)**2+y*y)) for k in range(K)),F(0))
    # Positive decreasing Euler digamma series, integral-tail lower bound.
    tail=log_rational_bounds(1+(y/(K+a))**2)[0]/2
    return partial+tail-CONST_UP


def certify_window():
    global_min=None
    for i in range(CELLS):
        left=LOW+(HIGH-LOW)*i/CELLS
        right=LOW+(HIGH-LOW)*(i+1)/CELLS
        mid=(left+right)/2
        # Entire interval: monotone arch + full signed prime-midpoint enclosure
        # and exact global original prime-derivative bound |p'|<69.
        m_lo=arch_lower(left)+prime_interval(mid)[0]-F(69,2)*(right-left)
        assert m_lo>KAPPA+DELTA, (
            "SI13 positive-window gap not established",i,float(m_lo)
        )
        global_min=m_lo if global_min is None else min(global_min,m_lo)
    return global_min


def validate():
    m_min=certify_window()
    assert m_min>F(101,100)  # certified m>1.01 on both +/- bands

    # Original s(x)=sinh(x/2), odd and supported in [-B,B].
    # At xi_0=3/10, k=2*pi*xi_0=3*pi/5, kB=33*pi/50,
    # angle theta=4*pi/25: sin(kB)=cos(theta),
    # cos(kB)=-sin(theta).
    # |hat(s)(xi_0)| =
    # 2*[cosh(B/2)*cos(theta)/2+
    #    k*sinh(B/2)*sin(theta)]/[1/4+k^2].
    pilo,pihi=PI
    theta_lo=F(4,25)*pilo
    theta_hi=F(4,25)*pihi
    cos_theta_lo=1-theta_hi**2/2
    sin_theta_lo=theta_lo-theta_hi**3/6
    assert 0<sin_theta_lo<1 and 0<cos_theta_lo<1

    s_lo,s_hi=sinh_bounds(B/2)
    c_lo,c_hi=cosh_bounds(B/2)
    k_lo=F(3,5)*pilo
    k_hi=F(3,5)*pihi
    fourier_center_lo=(
        2*(c_lo*cos_theta_lo/2+k_lo*s_lo*sin_theta_lo)/
        (F(1,4)+k_hi*k_hi)
    )
    assert fourier_center_lo>F(54,100)

    # Lipschitz bound in physical frequency:
    # ||d_xi hat(s)||_infty <=2*pi*integral_I |x*s(x)|dx
    # =2*pi*(4*B*cosh(B/2)-8*sinh(B/2)) <3.
    derivative_hi=2*pihi*(4*B*c_hi-8*s_lo)
    assert 0<derivative_hi<3

    # Both J+=[.22,.38], J-=-J+; even multiplier.
    # Use |hat(s)(xi)|>0.54-3*0.08=0.30 throughout.
    radius=(HIGH-LOW)/2
    amp_lower=F(54,100)-3*radius
    assert radius==F(2,25) and amp_lower==F(3,10)
    assert fourier_center_lo-derivative_hi*radius>amp_lower
    two_sided_fourier_mass_lo=2*(HIGH-LOW)*amp_lower**2
    assert two_sided_fourier_mass_lo==F(36,1250) # 0.0288

    # Real original positive A>=kappa I+delta Q_J, Q_J compressed
    # whole-line frequency interval projection, 0<=Q_J<=I.
    # By inverse operator monotonicity then scalar convex chord:
    # A^-1 <= (kappa I+delta Q_J)^-1
    #      <= kappa^-1 I
    #          -delta/[kappa(kappa+delta)] Q_J.
    # Exact rank-one original negative odd pole's BS norm:
    # lambda_pole=2<s,A^-1 s>.
    sB_lo,sB_hi=sinh_bounds(B)
    s_norm_hi=sB_hi-B
    scalar_only_upper=2*s_norm_hi/KAPPA
    gain_lower=2*DELTA/(KAPPA*(KAPPA+DELTA))*two_sided_fourier_mass_lo
    improved_upper=scalar_only_upper-gain_lower
    assert F(471,1)<scalar_only_upper<F(472,1)
    assert gain_lower>F(57,1)
    assert F(0)<improved_upper<F(414,1)
    assert improved_upper<scalar_only_upper

    # A positive window of m is not a standalone proof of K pole
    # absorption: even improved bound >> required BS threshold 1.
    assert improved_upper>1
    print("SI13 PASS: rigorously positive original signed Fourier window on both +/- bands")
    print("whole-window signed m(xi) strict lower:",float(m_min))
    print("positive window J+: [",float(LOW),",",float(HIGH),"]")
    print("rigorous original odd Fourier center amplitude lower:",float(fourier_center_lo))
    print("rigorous odd physical Fourier derivative upper:",float(derivative_hi))
    print("two-sided Fourier odd-mass strict lower:",float(two_sided_fourier_mass_lo))
    print("scalar-only original odd-pole BS upper:",float(scalar_only_upper))
    print("new supported odd-pole BS strict upper:",float(improved_upper))
    print("certified strict improvement:",float(gain_lower))
    print("NOT an exact inverse response, full finite BS eigenvalue, Stage I or RH.")


if __name__=="__main__":
    validate()
