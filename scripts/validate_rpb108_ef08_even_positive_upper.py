#!/usr/bin/env python3
"""EF08: original signed physical even positive-energy UPPER sharpening.

Certify the complete physically supported original positive quadratic
A_e on EF05's SAME physical even cosine by two rigorous finite rational
sign-aware regions [0,4], [4,128] and a true analytic [128,infinity)
tail, with positive even pole retained. Compare to EF07's entire
original tightened negative-cap lower; never pre-assert its sign.

The global positive energy is NOT approximated by the unsupported
pointwise inverse; Fourier transforms are of the true compactly
supported cosine and ALL frequencies are paid.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B, PI, LN, prime_interval
from validate_rpb108_si14_odd_multiband_nogo import arch_upper
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_ef05_even_cap_obstruction import (
    CENTER, DERIVATIVE, supported_even_fourier, absolute_upper,
    rational_ceil, true_positive_pole_upper
)
from validate_rpb108_ef07_global_even_witness import (
    old_new_global_cap_intervals, original_actual_positive_interval
)

LOW_RIGHT=F(4)
HIGH_RIGHT=F(128)
LOW_SUBDIV=1024
LOW_ARCH_GROUP=64
HIGH_SUBDIV=32
STEP_ROUND=10**6


def signed_original_upper_cells():
    """Whole m, all seven prime-power terms, no sampled sign claim."""
    # arch_upper is a rigorous original signed digamma Euler/Tail upper
    # and the archimedean function increases for xi>=0.
    arch_low=[arch_upper(F(k+1,LOW_ARCH_GROUP))
              for k in range(int(LOW_RIGHT*LOW_ARCH_GROUP))]
    arch_high=[arch_upper(F(k+1))
               for k in range(int(LOW_RIGHT),int(HIGH_RIGHT))]
    original_low=F(0)
    original_mid=F(0)
    cells_low=int(LOW_RIGHT*LOW_SUBDIV)
    for i in range(cells_low):
        l=F(i,LOW_SUBDIV)
        r=F(i+1,LOW_SUBDIV)
        mid=(l+r)/2
        # An original-sign m UPPER on every full 1/1024 cell.
        group=i*LOW_ARCH_GROUP//LOW_SUBDIV
        multiplier=arch_low[group]+prime_interval(mid)[1]+F(69)*(r-l)/2
        multiplier=rational_ceil(max(KAPPA,multiplier))
        amp=supported_even_fourier(mid)
        fbound=rational_ceil(absolute_upper(amp)+DERIVATIVE*(r-l)/2)
        original_low+=2*(r-l)*multiplier*fbound**2

    cells_high=int((HIGH_RIGHT-LOW_RIGHT)*HIGH_SUBDIV)
    for i in range(cells_high):
        l=LOW_RIGHT+F(i,HIGH_SUBDIV)
        r=LOW_RIGHT+F(i+1,HIGH_SUBDIV)
        mid=(l+r)/2
        group=l.numerator//l.denominator-int(LOW_RIGHT)
        # On [4,128] use the integer-right-end original arch upper,
        # paying the ENTIRE original seven-prime signed phase fluctuation.
        multiplier=arch_high[group]+prime_interval(mid)[1]+F(69)*(r-l)/2
        multiplier=rational_ceil(max(KAPPA,multiplier))
        amp=supported_even_fourier(mid)
        # Exact derivative of the physical cosine-transform:
        # |F'| <= 2B/(xi-z) + 1/[pi (xi-z)^2], for xi>=4.
        # This frequency-sensitive bound is much sharper than
        # 2*pi*B^2 and holds for all xi in this entire cell.
        v=l-CENTER
        assert v>3
        deriv=2*B/v+1/(PI[0]*v*v)
        fbound=rational_ceil(absolute_upper(amp)+deriv*(r-l)/2)
        original_mid+=2*(r-l)*multiplier*fbound**2
    return original_low,original_mid,cells_low,cells_high


def whole_infinite_positive_tail():
    """Both signs [128,infinity) analytically with complete log growth.

    From SI15: a(xi)<12+log(1+14xi)<15+log(xi) for xi>=4.
    EF05: |F_z(xi)|² <1/(8xi²). Thus BOTH reflected tails
    < (16+log(T))/(4T), where T=128. log(128)=7 log(2)
    enclosed from above by SI06's rigorous LN[2][1].
    """
    assert HIGH_RIGHT==128 and LN[2][1]<F(7,10)
    tail=(F(16)+7*LN[2][1])/(4*HIGH_RIGHT)
    assert F(0)<tail<F(1,20)
    return tail


def validate():
    low,mid,nlow,nmid=signed_original_upper_cells()
    tail=whole_infinite_positive_tail()
    pole,overlap=true_positive_pole_upper()
    original_positive_upper=low+mid+tail+pole
    cap=old_new_global_cap_intervals()
    prev=original_actual_positive_interval()
    assert cap["new_lower"]>F(8023,10000)
    assert cap["new_upper"]<F(102,100)
    assert original_positive_upper<prev["upper"]
    assert prev["lower"]<original_positive_upper
    assert low>0 and mid>0
    # Primary pass is an improved RIGOROUS UPPER, not an assumed order.
    assert original_positive_upper<F(11,10),(
        "Full signed upper still too coarse",float(original_positive_upper),
        float(low),float(mid),float(tail),float(pole))
    delta_lower=cap["new_lower"]-original_positive_upper
    status="CAP_NO_GO" if delta_lower>0 else "STILL_INCONCLUSIVE"
    print("EF08 complete original signed positive [0,4] UPPER:",
          float(low),"cells",nlow,flush=True)
    print("EF08 complete original signed positive [4,128] UPPER:",
          float(mid),"cells",nmid,flush=True)
    print("EF08 entire original signed positive >=128 tail UPPER:",
          float(tail),flush=True)
    print("EF08 original positive even pole UPPER:",float(pole),flush=True)
    print("EF08 improved WHOLE original A_e positive UPPER:",
          float(original_positive_upper),flush=True)
    print("EF08 previous EF07 original A_e UPPER:",float(prev["upper"]),flush=True)
    print("EF08 EF07 true original supported even refined-cap LOWER:",
          float(cap["new_lower"]),flush=True)
    print("EF08 cap lower minus original positive upper:",
          float(delta_lower),flush=True)
    print("EF08 certified one-vector method classification:",status,flush=True)
    if status=="CAP_NO_GO":
        print("EF08 proves refined EF06 UPPER CAP is not dominated by",
              "actual A_e on this SAME physical even witness; DOES NOT",
              "show actual original signed even Q negative.",flush=True)
    else:
        print("EF08 strict improvement to actual positive upper only;",
              "intervals not separated, do not infer cap feasibility.",
              flush=True)
    print("EF08 PASS: true original A_e full signed integral bounded;",
          "whole even Weil, finite Schur, global bridge and RH OPEN.",
          flush=True)


if __name__=="__main__":
    validate()
