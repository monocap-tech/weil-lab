#!/usr/bin/env python3
"""SM07: original signed multiplier EXCESS defeats scalar-floor-only absorption.

This is a rigorous operator-norm LOWER bound on the *actual remainder*
E=K_neg,o - T_{J,7/5}, not a negative vector for original Weil Q.
Physical odd support and the inherited original seven-prime multiplier.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import PI, B, prime_interval
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_sm03_negative_packet_reference_nogo import (
    C as OLD_CENTER, RADIUS as OLD_RADIUS, DELTA as OLD_DELTA,
    arch_upper
)
from validate_rpb108_si21_odd_jensen_four import KAPPA

# A real subinterval J1 subset [3.645, 3.705] within the original
# signed negative packet whose original multiplier is much more negative
# than the uniform 7/5 contribution already absorbed by SM06.
CENTER=F(73,20)     # 3.65
RADIUS=F(1,200)    # .005; J1=[3.645,3.655]
THRESHOLD=F(2)     # m(xi)< -2 continuously on J1
EXTRA=F(3,5)       # (kappa-m)_+-7/5 >.6 on J1
CELLS=16

def certify_subband():
    assert (CENTER-RADIUS,CENTER+RADIUS)==(F(729,200),F(731,200))
    assert OLD_CENTER-OLD_RADIUS==F(729,200)
    assert CENTER+RADIUS<OLD_CENTER+OLD_RADIUS
    assert OLD_DELTA==F(7,5) and KAPPA==F(1,1000)
    assert THRESHOLD+KAPPA-OLD_DELTA>EXTRA
    worst=None
    for j in range(CELLS):
        lo=CENTER-RADIUS+2*RADIUS*j/CELLS
        hi=CENTER-RADIUS+2*RADIUS*(j+1)/CELLS
        mid=(lo+hi)/2
        # Original arch term increases for xi>=0. Signed seven-prime
        # derivative is globally bounded in absolute value by 69.
        # This upper is for every real xi in the rational subcell.
        upper=arch_upper(hi)+prime_interval(mid)[1]+F(69,2)*(hi-lo)
        worst=upper if worst is None else max(worst,upper)
        assert upper < -THRESHOLD,(j,float(upper))
    return worst

def true_physical_odd_packet_norm():
    # EXACT odd physical continuous-frequency Jensen mean
    # g(x)=sin(2*pi*CENTER*x)*sinc(2*pi*RADIUS*x).
    # The approximation sin_c is used only for a rigorous L2 LOWER:
    # |sinc(z)-1|<=z²/6 for |z|<=2*pi*RADIUS*B.
    eps=(2*PI[1]*RADIUS*B)**2/6
    assert 0<eps<F(1,1000)
    lo,hi=gram(CENTER,CENTER)
    norm_lower=(1-eps)**2*lo
    assert norm_lower>F(1) and hi<F(6,5),(
        "SM07 physical Jensen L2 norm source failed",float(lo),float(hi)
    )
    return norm_lower,eps

def validate():
    multiplier_upper=certify_subband()
    norm_lower,sinc_error=true_physical_odd_packet_norm()
    # On J1, the full original signed negative spectral multiplier
    # r=(kappa-m)_+ is >OLD_DELTA+EXTRA, because m< -2.
    # Hence the residual E=K_neg - T_{J,7/5} satisfies
    # E >= 2*EXTRA int_[J1] |sin(2*pi*xi*x)><sin| dxi
    #   >= 4*RADIUS*EXTRA |g><g| on the true physical odd support.
    gamma=4*RADIUS*EXTRA
    eigen_lower=gamma*norm_lower
    assert gamma==F(3,250)
    assert eigen_lower>F(1,100)
    # SM06's *certified lower coercivity floor* after subtracting the
    # pole and the uniform 7/5 band is >5.6440e-5.
    # That is a positive floor, NOT an upper bound on the true
    # residual positive operator. We disprove only the shortcut:
    #   E <= (5.6440e-5)*I.
    sm06_reported_lower_floor=F(56440,10**9)
    assert sm06_reported_lower_floor==F(5644,10**8)
    assert eigen_lower>100*sm06_reported_lower_floor
    print("SM07 original signed seven-prime WHOLE subband m UPPER:",
          float(multiplier_upper),flush=True)
    print("SM07 true supported odd Jensen norm² LOWER:",
          float(norm_lower),flush=True)
    print("SM07 true mean-to-center sinc error:",float(sinc_error),flush=True)
    print("SM07 original VARIABLE negative-multiplier excess Jensen weight:",
          float(gamma),flush=True)
    print("SM07 original REMAINDER spectral norm LOWER:",float(eigen_lower),flush=True)
    print("SM07 SM06 scalar-only certified floor:",float(sm06_reported_lower_floor),flush=True)
    print("SM07 PASS: actual variable negative continuum excess CANNOT be paid using SM06's reported scalar floor alone",flush=True)
    print("This DOES NOT show E > original A_o-2ss*-uniform band; full signed covariance/inverse remains OPEN",flush=True)

if __name__=="__main__":
    validate()
