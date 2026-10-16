#!/usr/bin/env python3
"""SI14: exact-rational MULTI-window odd supported inverse improvement and
a rigorously excluded-frequency no-go for scalar-chord-only certificates.

All original CC27 signed prime / arch data imported from SI06/12/13.
Rational intervals prove whole-window claims (no grid interpolation).
"""
from fractions import Fraction as F
from math import factorial
from validate_rpb108_si06_negative_band import (
    PI, B, prime_interval, log_rational_bounds, LN,
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds, cosh_bounds
from validate_rpb108_si13_odd_fourier_reference import arch_lower

KAPPA=F(1,1000)
DELTA=F(1)
# 3 disjoint positive windows. Both signs always included.
WINDOWS=(
    (F(11,50),F(19,50),F(3,10),F(54,100)),  # SI13, centre 0.30
    (F(73,100),F(79,100),F(76,100),F(16,100)),
    (F(219,100),F(223,100),F(221,100),F(7,100)),
)
# Guaranteed original signed NEGATIVE window (and its reflection).
BAD=(F(7,100),F(13,100),F(1,10),F(26,100))
CELLS=128
K=128


def cos_sin_pi_multiple(q):
    """Outward exact rational sin(pi*q) and cos(pi*q) on rational q."""
    q=q-2*((q+1)//2)
    assert -1<=q<=1
    mid=(PI[0]+PI[1])/2
    t=q*mid
    sin_t=sum(((-1)**j*t**(2*j+1)/factorial(2*j+1)
               for j in range(20)),F(0))
    cos_t=sum(((-1)**j*t**(2*j)/factorial(2*j)
               for j in range(20)),F(0))
    rem=F(22,7)**40/factorial(40)+abs(q)*(PI[1]-PI[0])/2
    assert 0<rem<F(1,10**20)
    return (sin_t-rem,sin_t+rem),(cos_t-rem,cos_t+rem)


def mul_intervals(x,y):
    a,b=x
    c,d=y
    vals=(a*c,a*d,b*c,b*d)
    return min(vals),max(vals)


def add_intervals(x,y):
    return x[0]+y[0],x[1]+y[1]


def neg_interval(x):
    return -x[1],-x[0]


def abs_fourier_center_lower(xi):
    """Exact analytical original s(x)=sinh(x/2) Fourier transform interval."""
    slo,shi=sinh_bounds(B/2)
    clo,chi=cosh_bounds(B/2)
    q=2*xi*B
    sin_b,cos_b=cos_sin_pi_multiple(q)
    k=(2*PI[0]*xi,2*PI[1]*xi)
    first=mul_intervals((clo/2,chi/2),sin_b)
    second=mul_intervals(mul_intervals(k,(slo,shi)),cos_b)
    num=add_intervals(first,neg_interval(second))
    if num[0]>0:
        absnum=num[0]
    elif num[1]<0:
        absnum=-num[1]
    else:
        raise AssertionError(f"SI14 centre zero-crossing/indeterminate at xi={xi}")
    lower=2*absnum/(F(1,4)+k[1]**2)
    assert lower>0
    return lower


def odd_frequency_derivative_upper():
    """|d_xi hat s| <= 2*pi*int_I |x s(x)| dx, positive rational."""
    slo,shi=sinh_bounds(B/2)
    clo,chi=cosh_bounds(B/2)
    # 4 B cosh(B/2)-8 sinh(B/2) > 0 (actual physical first moment).
    res=2*PI[1]*(4*B*chi-8*slo)
    assert 0<res<3
    return res


def arch_upper(x):
    """Rigorous Euler-digamma upper, including the infinite tail."""
    y=PI[1]*x
    a=F(1,4)
    first=sum((y*y/((k+a)*((k+a)**2+y*y))
               for k in range(K)),F(0))
    # Since g_y(t) decreases, sum_{k>=K} g_y(k)
    # <= integral from K-1 to infinity g_y(t)dt.
    tail=log_rational_bounds(1+(y/(K-1+a))**2)[1]/2
    # psi(1/4)-log pi = -gamma-pi/2-3ln2-ln pi
    # SI06 has independently certified gamma>57/100.
    const_lo=(F(57,100)+PI[0]/2+3*LN[2][0]
              +log_rational_bounds(PI[0])[0])
    return first+tail-const_lo


def certify_positive_window(left,right):
    """Full continuum bound with signed prime derivative <69."""
    lower=None
    for i in range(CELLS):
        l=left+(right-left)*i/CELLS
        r=left+(right-left)*(i+1)/CELLS
        mid=(l+r)/2
        cur=arch_lower(l)+prime_interval(mid)[0]-F(69,2)*(r-l)
        assert cur>KAPPA+DELTA, ("positive-window certificate fails",
                               left,right,i,float(cur))
        lower=cur if lower is None else min(lower,cur)
    return lower


def certify_negative_forbidden_band():
    l,r,mid,_=BAD
    # arch real part increases with |xi|; p' bound <69 pays full
    # midpoint -> endpoint uncertainty on BOTH sides continuously.
    upper=arch_upper(r)+prime_interval(mid)[1]+F(69,2)*(r-l)
    assert upper<0, ("SI14 excluded band not proven negative",float(upper))
    return upper


def validate():
    deriv=odd_frequency_derivative_upper()
    slo,shi=sinh_bounds(B)
    scalar_upper=2*(shi-B)/KAPPA
    assert 471<scalar_upper<472
    total_mass_lower=F(0)
    print("SI14: certified ORIGINAL signed positive windows and ODD Fourier masses")
    for left,right,center,centre_target in WINDOWS:
        assert left<center<right
        minimum=certify_positive_window(left,right)
        centre_amp=abs_fourier_center_lower(center)
        assert centre_amp>centre_target, (
            "odd centre Fourier amplitude gate",center,float(centre_amp))
        halfwidth=max(center-left,right-center)
        # Global moment Lipschitz is rigorous, not sampled interpolation.
        amp=centre_target-3*halfwidth
        assert amp>0
        full_mass=2*(right-left)*amp**2
        assert full_mass>0
        total_mass_lower+=full_mass
        print("J+:",str(left),str(right),
              "signed m strict min:",float(minimum),
              "odd center |Fourier(s)| lower:",float(centre_amp),
              "certified two-sided odd Fourier mass lower:",float(full_mass))

    # Disjoint J+ and reflected J-. Their compressed frequency projection
    # is a SINGLE physical positive contraction 0<=Q_J<=I.
    assert all(WINDOWS[j][1]<WINDOWS[j+1][0]
               for j in range(len(WINDOWS)-1))
    gain=2*DELTA/(KAPPA*(KAPPA+DELTA))*total_mass_lower
    multiband_upper=scalar_upper-gain
    first_window_mass=2*(WINDOWS[0][1]-WINDOWS[0][0]) * F(3,10)**2
    old_gain=2*DELTA/(KAPPA*(KAPPA+DELTA))*first_window_mass
    single_window_upper=scalar_upper-old_gain
    assert single_window_upper<F(414)
    assert multiband_upper<single_window_upper
    assert multiband_upper<F(413), ("multi-window gain weak",float(multiband_upper))
    assert multiband_upper>1

    # No-go: a positive-window-only scalar-chord certificate cannot cover
    # any frequency where original signed m(xi)<kappa. There is a
    # rigorously negative band at +/-[.07,.13] with positive odd Fourier
    # mass, so even an IDEALIZED full discount elsewhere leaves the
    # upper certificate larger than the target 1.
    forbidden_upper=certify_negative_forbidden_band()
    l,r,center,amp0=BAD
    ampcentre=abs_fourier_center_lower(center)
    assert ampcentre>amp0
    forbidden_amp=amp0-3*(r-l)/2
    assert forbidden_amp>0
    forbidden_mass=2*(r-l)*forbidden_amp**2
    obstruction=2*forbidden_mass/KAPPA
    assert obstruction>F(6,1) # >6, so never reaches BS target 1
    # The above is a FLOOR ON THE POSSIBLE SCALAR-CHORD *UPPER
    # CERTIFICATE*, NOT a lower bound on the true <s,A^-1s>.
    assert total_mass_lower<shi-B

    print("all-window odd Fourier mass lower:",float(total_mass_lower))
    print("SI13 single-window certified upper:",float(single_window_upper))
    print("SI14 multiple-window certified upper:",float(multiband_upper))
    print("additional certified improvement:",float(single_window_upper-multiband_upper))
    print("certified original m(xi)<0 over +/-[.07,.13]:",float(forbidden_upper))
    print("forbidden-band original ODD Fourier mass lower:",float(forbidden_mass))
    print("SCALAR-CHORD POSITIVE-WINDOW-ONLY bound cannot fall below:",float(obstruction))
    print("SI14 PASS: actual odd inverse upper improved; no-go for this comparison class")
    print("NO lower bound on actual inverse; no residual Gram, full BS eigenvalue, Stage I or RH.")


if __name__=="__main__":
    validate()
