#!/usr/bin/env python3
"""SI15: first genuine original physically-supported ODD trial inverse response.

Trial y = s/4800, s(x)=sinh(x/2), A=positive supported operator from
original RC312-313/ SI11 protected-multiplier decomposition.
Exact rational full-residual bound, not a projected/Galerkin residual.
This is a valid but weak standalone inverse response certificate and does
NOT outperform SI14's positive-window inverse bound.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import (
    B, PI, LN, TWOC,
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

KAPPA=F(1,1000)
ALPHA=F(1,4800)

def validate():
    # SI06/14 original signed source certified constants. SI14's exact
    # all-window odd Fourier mass lower bound:
    # J1: 2*(0.16)*(0.30)^2 = .0288
    # J2: 2*(0.06)*(0.07)^2 = .000588
    # J3: 2*(0.04)*(0.01)^2 = .000008
    E=2*(F(16,100)*F(3,10)**2
        +F(6,100)*F(7,100)**2
        +F(4,100)*F(1,100)**2)
    assert E == F(29396,1000000)
    assert LN[2][1] < F(7,10)
    assert PI[0]>3 and 4*PI[1]<14
    assert TWOC<F(8)
    assert 4+TWOC<12

    # The original archimedean m upper bound derives from
    # g_y(k) positive decreasing:
    # sum g_y(k) <= g_y(0)+ integral_0∞ g_y <=4+0.5 log(1+(4πξ)^2).
    # psi(1/4)-log π <0; primes add <=2C.
    # Hence a=max(m,kappa) <12+log(1+14|ξ|).
    # Low |ξ|≤1: log(1+14|ξ|)≤log 16 < 4*(7/10).
    low_multiplier=F(74,5)
    assert low_multiplier==12+4*F(7,10)

    # For |ξ| in [2^k,2^(k+1)]:
    # log(1+14|ξ|) < (k+5) log2 <.7(k+5)
    # multiplier <= 31/2+(7/10)k.
    d=F(31,2)
    slope=F(7,10)
    assert d==12+5*slope

    # Original physically zero-extended odd s satisfies, for |ξ|>=1,
    # |hat(Zs)(ξ)| <=2 sinh(B/2)/(π|ξ|) < (2/5)/|ξ|.
    shalf_lo,shalf_hi=sinh_bounds(B/2)
    assert shalf_hi <F(3,5)
    assert 2*shalf_hi/PI[0]<F(2,5)

    # ||s||² = sinh B-B <1/4 (exact outward Taylor enclosures).
    sB_lo,sB_hi=sinh_bounds(B)
    Slo,Shi=sB_lo-B,sB_hi-B
    assert 0<Slo<Shi<F(1,4)

    # Since s is odd and c even, the original even pole annihilates s.
    # The fully-supported operator satisfies
    #   As=Z*F^-1 [a * hat(Zs)] ∈ L²(I).
    # Bound the FULL ||As||² by the whole-line integral. Below |ξ|=1
    # use Plancherel; outside use the exact dyadic 1/ξ² integral.
    #
    # For two-sided band [2^k,2^(k+1)] and reflection:
    # ∫ ξ^-2 dξ=2^-k. Then exact geometric sums
    # Σ 2^-k=2, Σ k2^-k=2, Σ k²2^-k=6.
    low_energy_bound=low_multiplier**2*F(1,4)
    high_energy_bound=F(4,25)*(
         2*d*d+4*d*slope+6*slope*slope
    )
    T=low_energy_bound+high_energy_bound
    assert low_energy_bound==F(1369,25)
    assert high_energy_bound==F(52684,625)
    assert T==F(86909,625)<140
    FULL_NORM_UP=F(140)

    # Original positive frequency windows J1..J3 have m>κ+1 and
    # total *actual* odd Fourier energy >E by SI14. Therefore
    # q=<s,As> ≥ κ ||s||² + E, with strictly certified E>0.
    #
    # y=αs is a GENUINE supported odd trial in Dom A, because aŝ∈L².
    # Its full original residual is R=s-αAs, *not* the projected residual.
    # ||R||²= S-2α q+α² ||As||²
    #       <=(1-2ακ) S-2αE+α²T.
    residual_sq_upper=(1-2*ALPHA*KAPPA)*Shi-2*ALPHA*E+ALPHA**2*FULL_NORM_UP
    assert residual_sq_upper>0
    assert residual_sq_upper < Shi

    # SI11 correct-sign identity, scalar floor ||A^-1||<=1/κ:
    # 2<s,A^-1s>
    # <=4αS-2α²q+(2/κ)||R||²
    # <=2S/κ -4αE/κ +2α²T/κ. The negative term -2α²q
    # is safely dropped. Full residual included.
    improvement=4*ALPHA*E/KAPPA-2*ALPHA**2*FULL_NORM_UP/KAPPA
    assert improvement==F(22219,1800000)>F(123,10000)
    scalar_upper=2*Shi/KAPPA
    odd_upper=scalar_upper-improvement
    assert odd_upper <F(471283,1000) # strict <471.283
    assert odd_upper >F(471,1)
    # SI14's tighter window-comparator upper was <412.562. Thus
    # this first genuine residual certificate is NOT competitive.
    assert odd_upper>F(414,1)

    # An original supported Rayleigh variational LOWER bound (for
    # reference, not a negative Weil direction) follows from
    # Cauchy: <s,A^-1s> ≥ ||s||^4 /<s,As> .
    # Because ||As|| ≤sqrt(140), q ≤||s|| sqrt(140):
    # 2<s,A^-1s> ≥ 2 ||s||³/sqrt(140).
    # Avoid introducing a numerical lower claim here.

    print("SI15 PASS: actual supported odd trial y=(1/4800)s and FULL residual paid")
    print("certified all-frequency ||As||² upper:",float(T),"<140")
    print("certified inherited strict odd protected-window energy:",float(E))
    print("full original supported trial residual² upper:",float(residual_sq_upper))
    print("strict inverse upper improvement over scalar-only:",float(improvement))
    print("new odd supported inverse upper:",float(odd_upper))
    print("relative benchmark: SI14's <412.562 remains MUCH stronger")
    print("SI15 establishes genuine residual custody, not odd-pole absorption")
    print("No original full finite BS eigenvalue, Stage I, F4, Lean or RH claim.")

if __name__=="__main__":
    validate()
