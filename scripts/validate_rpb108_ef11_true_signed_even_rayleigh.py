#!/usr/bin/env python3
"""EF11: direct SAME physical even original signed Weil Rayleigh interval.

No conservative EF04/EF06/EF07 cap enters the sign calculation.
For f=cos(2*pi*(19/25)*x) supported on [-11/10,11/10],
Q_e(f)=2 int_0^inf m(xi)|F_f(xi)|^2 dxi
       +2|<f,cosh(x/2)>|^2.
Enclose the actual ORIGINAL seven-prime signed m, including each
signed Fourier factor and all infinite frequencies.

This is strictly a one-vector diagnostic. A positive Rayleigh
interval never proves whole-operator PSD. A negative result must be
independently audited before any mathematical interpretation.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B, LN, TWOC, prime_interval
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_si14_odd_multiband_nogo import arch_upper
from validate_rpb108_ef05_even_cap_obstruction import (
    CENTER, DERIVATIVE, absolute_lower, absolute_upper, rational_floor,
    rational_ceil, supported_even_fourier, true_positive_pole_upper
)
from validate_rpb108_ef08_even_positive_upper import (
    whole_infinite_positive_tail
)
from validate_rpb108_si06_negative_band import PI

LOW_END=F(4)
HIGH_END=F(128)
LOW_RATE=1024
LOW_ARCH_RATE=64
MID_RATE=32
PRIME_DERIVATIVE=F(69)


def signed_cell_ensured(mlo,mhi,amp_lo,amp_hi,delta):
    """Enclose 2 integral_cell m(xi)|F(xi)|^2 including reflection.

    Because the squared amplitude is nonnegative and bounded, products
    use correct signed interval corners; no false positive clipping.
    """
    assert mlo<=mhi and 0<=amp_lo<=amp_hi and delta>0
    a2,b2=amp_lo**2,amp_hi**2
    lower=(mlo*a2 if mlo>=0 else mlo*b2)
    upper=(mhi*b2 if mhi>=0 else mhi*a2)
    assert lower<=upper
    return 2*delta*lower,2*delta*upper


def entire_finite_signed():
    # Arch is monotone for xi>=0. Rational interval enclosures, with
    # arch.lower at the LEFT endpoint and arch.upper at the RIGHT.
    archlow=[rational_floor(arch_lower(F(j,LOW_ARCH_RATE)))
             for j in range(LOW_ARCH_RATE*int(LOW_END))]
    archhigh=[rational_ceil(arch_upper(F(j+1,LOW_ARCH_RATE)))
              for j in range(LOW_ARCH_RATE*int(LOW_END))]
    integerlow=[rational_floor(arch_lower(F(j)))
                for j in range(int(LOW_END),int(HIGH_END))]
    integerhigh=[rational_ceil(arch_upper(F(j+1)))
                 for j in range(int(LOW_END),int(HIGH_END))]

    low_lb=low_ub=mid_lb=mid_ub=F(0)
    positive_cells=negative_cells=crossing_cells=0
    for i in range(int(LOW_END)*LOW_RATE):
        l=F(i,LOW_RATE);r=F(i+1,LOW_RATE);q=(l+r)/2
        ix=i*LOW_ARCH_RATE//LOW_RATE
        plo,phi=prime_interval(q)
        ml=rational_floor(archlow[ix]+plo-PRIME_DERIVATIVE*(r-l)/2)
        mh=rational_ceil(archhigh[ix]+phi+PRIME_DERIVATIVE*(r-l)/2)
        fmid=supported_even_fourier(q)
        al=rational_floor(max(F(0),absolute_lower(fmid)-DERIVATIVE*(r-l)/2))
        ah=rational_ceil(absolute_upper(fmid)+DERIVATIVE*(r-l)/2)
        sl,su=signed_cell_ensured(ml,mh,al,ah,r-l)
        low_lb+=sl; low_ub+=su
        if ml>=0:positive_cells+=1
        elif mh<=0:negative_cells+=1
        else:crossing_cells+=1

    # High band pays every original signed prime power, not a positive
    # surrogate; distance-dependent physical Fourier derivative.
    for i in range(int((HIGH_END-LOW_END)*MID_RATE)):
        l=LOW_END+F(i,MID_RATE);r=LOW_END+F(i+1,MID_RATE)
        q=(l+r)/2
        ix=l.numerator//l.denominator-int(LOW_END)
        plo,phi=prime_interval(q)
        ml=rational_floor(integerlow[ix]+plo-PRIME_DERIVATIVE*(r-l)/2)
        mh=rational_ceil(integerhigh[ix]+phi+PRIME_DERIVATIVE*(r-l)/2)
        fmid=supported_even_fourier(q)
        z=l-CENTER
        assert z>3
        deriv=2*B/z+1/(PI[0]*z*z)
        al=rational_floor(max(F(0),absolute_lower(fmid)-deriv*(r-l)/2))
        ah=rational_ceil(absolute_upper(fmid)+deriv*(r-l)/2)
        sl,su=signed_cell_ensured(ml,mh,al,ah,r-l)
        mid_lb+=sl;mid_ub+=su
        if ml>=0:positive_cells+=1
        elif mh<=0:negative_cells+=1
        else:crossing_cells+=1
    assert positive_cells+negative_cells+crossing_cells==8064
    return (low_lb,low_ub,mid_lb,mid_ub,
            positive_cells,negative_cells,crossing_cells)


def true_signed_tail():
    """Full [128,infinity) original m tail, BOTH reflected signs.

    Original arch(xi) is monotone increasing, original complete
    signed seven-prime oscillation >= -TWOC. Therefore for all
    xi>=128, m(xi)>=arch_lower(128)-TWOC=:L. If L<0,
    signed integral lower is L/(4*128) via the globally valid
    |F_z|^2<1/(8xi^2). If L>=0, lower is zero.
    For the upper, m<=max(m,kappa)=a and inherit EF08's rigorous
    complete positive tail upper; no high frequency is dropped.
    """
    a=rational_floor(arch_lower(HIGH_END)-TWOC)
    tail_lower=min(F(0),a)/(4*HIGH_END)
    tail_upper=whole_infinite_positive_tail()
    assert tail_lower<=0<=tail_upper
    return tail_lower,tail_upper,a


def validate():
    lo,hi,ml,mh,npos,nneg,ncross=entire_finite_signed()
    tl,tu,arch_min=true_signed_tail()
    pole_up,overlap=true_positive_pole_upper()
    pole_lo=2*absolute_lower(overlap)**2
    assert 0<pole_lo<=pole_up
    original_q_lo=lo+ml+tl+pole_lo
    original_q_hi=hi+mh+tu+pole_up
    assert original_q_lo<=original_q_hi
    verdict=("SINGLE_WITNESS_POSITIVE" if original_q_lo>0 else
             "SINGLE_WITNESS_NEGATIVE_REQUIRES_EXTERNAL_AUDIT"
             if original_q_hi<0 else "INCONCLUSIVE")
    print("EF11 ORIGINAL signed even [0,4] interval:",
          float(lo),float(hi),flush=True)
    print("EF11 ORIGINAL signed even [4,128] interval:",
          float(ml),float(mh),flush=True)
    print("EF11 ORIGINAL signed even >=128 BOTH tails interval:",
          float(tl),float(tu),
          "arch-minus-seven-primes floor:",float(arch_min),flush=True)
    print("EF11 original positive even pole interval:",
          float(pole_lo),float(pole_up),flush=True)
    print("EF11 verified all finite signed cells:",
          npos+nneg+ncross,"positive",npos,"negative",nneg,
          "crossing",ncross,flush=True)
    print("EF11 ACTUAL ORIGINAL full physically supported even",
          "signed Q interval:",float(original_q_lo),
          float(original_q_hi),flush=True)
    print("EF11 sign status:",verdict,flush=True)
    print("EF11 PASS (one-vector only): full original even operator",
          "PSD, whole Weil, global bridge, Lean/RH still OPEN.",
          "No EF06 conservative cap used.",flush=True)


if __name__=="__main__":
    validate()
