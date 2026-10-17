#!/usr/bin/env python3
"""EF05: rigorous original EVEN cap method-class obstruction.

Certifies with exact outward rational arithmetic that a single genuine
supported even cosine f has <f,K_cap,e f> > <f,A_e f>. Therefore the
conservative EF04 all-negative UPPER cap cannot be dominated by the
true ORIGINAL positive operator, and EF04's sufficient 890-source
Schur condition is FALSE. This says NOTHING about positivity or
negativity of the actual signed Weil Q_e=A_e-K_true,e.

Inherits SI15's globally justified a(xi)<12+log(1+14|xi|)
for the genuine original original-seven-prime positive multiplier.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B, PI, LN, prime_interval, log_rational_bounds
from validate_rpb108_si14_odd_multiband_nogo import (
    arch_upper, cos_sin_pi_multiple,
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds,cosh_bounds
from validate_rpb108_si18_odd_rank_two_woodbury import add,mul,div
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_si07_negative_support_cover import ceil_fraction
from validate_rpb108_si10_complement_positivity import KAPPA

CENTER=F(19,25)
T=F(4)
CELLS_PER_UNIT=64
DERIVATIVE=2*PI[1]*B**2
TAIL_UP=F(35,32)
ROUND_DEN=10**6


def rational_ceil(q):
    """Safe per-cell outward upper to avoid giant Fraction aggregation."""
    return F(ceil_fraction(q*ROUND_DEN),ROUND_DEN)


def rational_floor(q):
    """Safe per-cell outward lower, including nonnegative zero floor."""
    y=q*ROUND_DEN
    return F(y.numerator//y.denominator,ROUND_DEN)


def absolute_upper(interval):
    assert interval[0]<=interval[1]
    return max(abs(interval[0]),abs(interval[1]))


def absolute_lower(interval):
    assert interval[0]<=interval[1]
    return max(F(0),interval[0],-interval[1])


def scalar_sinc_integral(q):
    """Physical Fourier transform of exp(i2pi*q*x) on [-B,B].

    Return rigorous interval sin(2pi B q)/(pi q); continuous value 2B
    when q=0. Our cosine source has an additional factor one half.
    """
    if q==0:
        return (2*B,2*B)
    numerator=cos_sin_pi_multiple(2*B*q)[0]
    u=PI[0]*q
    v=PI[1]*q
    return div(numerator,(min(u,v),max(u,v)))


def supported_even_fourier(xi):
    """Actual f(x)=cos(2pi CENTER x) zero-extended Fourier transform."""
    a=scalar_sinc_integral(xi-CENTER)
    b=scalar_sinc_integral(xi+CENTER)
    return ((a[0]+b[0])/2,(a[1]+b[1])/2)


def true_positive_pole_upper():
    """Original even pole 2|<f,cosh(x/2)>|² exact outward bound.

    The physical symmetric integral is
      2[(sinh(B/2)/2) cos(2pi CENTER B)
        +(2pi CENTER) cosh(B/2) sin(2pi CENTER B)]
      /[(1/2)^2+(2pi CENTER)^2].
    """
    s=sinh_bounds(B/2)
    c=cosh_bounds(B/2)
    sine,cosine=cos_sin_pi_multiple(2*B*CENTER)
    k=(2*PI[0]*CENTER,2*PI[1]*CENTER)
    first=mul((s[0]/2,s[1]/2),cosine)
    second=mul(mul(k,c),sine)
    numerator=mul((F(2),F(2)),add(first,second))
    denominator=(F(1,4)+k[0]**2,F(1,4)+k[1]**2)
    overlap=div(numerator,denominator)
    pole=rational_ceil(2*absolute_upper(overlap)**2)
    assert 0<pole<F(17,50),float(pole) # <0.34
    return pole,overlap


def full_cap_lower():
    """One subset of actual original SI10 signed upper-cap leaves only.

    Uses exact whole-leaf outward derivative remainder, not a sampled
    approximation; ignores every leaf beyond frequency one, safely
    lowering K_cap. Positive and negative reflection both included.
    """
    clusters,W,Mneg,mass=full_upper_leaves()
    assert len(clusters)==107
    assert W==F(973,32) and mass==F(1204033883,32000000)
    total=F(0)
    selected=0
    for cluster in clusters:
        for l,r,h in cluster:
            if r>T/4:
                continue
            center=(l+r)/2
            amp=supported_even_fourier(center)
            amp_lower=max(F(0),absolute_lower(amp)-DERIVATIVE*(r-l)/2)
            # Every physical Fourier amplitude is rounded DOWN before
            # squaring and accumulation, so the finite cap lower stays valid.
            amp_lower=rational_floor(amp_lower)
            total+=2*(h+KAPPA)*(r-l)*amp_lower**2
            selected+=1
    assert selected>0 and total>F(4),float(total)
    return total,selected


def actual_positive_low_upper():
    """Exact all-continuum (not sampled) a=max(m,kappa) upper [0,4].

    Archimedean contribution monotone, bounded at enclosing integer right endpoint;
    whole seven-prime signed cosine upper at midpoint with global
    |p'|<69 remainder; true physically supported Fourier moment
    covered by derivative max 2pi B² at each rational subcell.
    """
    count=int(T)*CELLS_PER_UNIT
    step=F(1,CELLS_PER_UNIT)
    total=F(0)
    highest=F(0)
    # The original archimedean Euler term is monotone on xi>=0.
    # One upper enclosure at each integer RIGHT endpoint pays ALL
    # contained 1/64 rational subcells. Only four expensive exact
    # 48-term rational Euler/digamma enclosures are needed.
    arch_integer_upper=[arch_upper(F(j+1)) for j in range(int(T))]
    for i in range(count):
        l=i*step
        r=(i+1)*step
        mid=(l+r)/2
        m_upper=(arch_integer_upper[i//CELLS_PER_UNIT]
                 +prime_interval(mid)[1]+F(69)*(r-l)/2)
        a_upper=rational_ceil(max(KAPPA,m_upper))
        f_mid=supported_even_fourier(mid)
        f_upper=rational_ceil(absolute_upper(f_mid)+DERIVATIVE*(r-l)/2)
        # Each local multiplier and Fourier factor is rounded UP,
        # retaining the full continuum operator upper inequality.
        total+=2*(r-l)*a_upper*f_upper**2
        highest=max(highest,a_upper)
    assert 0<total<F(2),float(total)
    return total,highest,count


def certified_tail():
    """Entire [4,infinity) original positive frequency continuum.

    Inherit SI15's original global bound
         a(xi) < 12+log(1+14 xi).
    Since xi>=4, <= 15+log xi (log15<3), and
    |hat f(xi)| <= xi/[pi(xi²-CENTER²)].
    (1-CENTER²/4²)^-2 < 9/8, pi>3, so
      |hat f(xi)|² < 1/(8 xi²).
    Include both frequency signs, and log4 <3/2:
       2 ∫_4^inf (15+log xi)/(8 xi²)dx < 35/32.
    """
    assert log_rational_bounds(F(15))[1]<3
    assert 2*LN[2][1]<F(3,2)
    assert PI[0]>3
    ratio=(1-CENTER**2/T**2)
    assert ratio>0 and 1/ratio**2<F(9,8)
    assert T==4 and CENTER==F(19,25)
    assert TAIL_UP==F(35,32)
    return TAIL_UP


def validate():
    assert B==F(11,10) and KAPPA==F(1,1000)
    cap_lower,nleaves=full_cap_lower()
    low,amax,cells=actual_positive_low_upper()
    pole,overlap=true_positive_pole_upper()
    tail=certified_tail()
    A_upper=low+tail+pole
    margin=cap_lower-A_upper
    assert cap_lower>4
    assert A_upper<F(7,2),float(A_upper)
    assert margin>F(1,2),(float(margin),float(cap_lower),float(A_upper))

    # EF04/EF03 exact original whole negative UPPER:
    # K_true,e <= K_cap,e <= (1+tau) U C U* + eta I.
    # For the physical f, K_cap,e(f)>A_e(f) proves the
    # *stronger upper surrogate* cannot be <=A_e.
    # Hence B_e - (1+tau) U C U* is not PSD, and EF04's
    # finite sufficient D^-1-U*B_e^-1 U cannot be PSD.
    # Critically K_true,e may be MUCH SMALLER than K_cap,e.
    print("EF05 original signed global envelope low leaves:",nleaves,flush=True)
    print("EF05 genuine even physical witness center:",str(CENTER),flush=True)
    print("EF05 positive low continuum exact rational cells:",cells,flush=True)
    print("EF05 original A0 frequency[0,4] quadratic UPPER:",float(low),flush=True)
    print("EF05 original A0 frequency>=4 quadratic UPPER:",float(tail),flush=True)
    print("EF05 original positive even pole overlap interval:",
          float(overlap[0]),float(overlap[1]),flush=True)
    print("EF05 positive even pole quadratic UPPER:",float(pole),flush=True)
    print("EF05 entire genuine ORIGINAL positive A_e quadratic UPPER:",float(A_upper),flush=True)
    print("EF05 EF04 original SI10 upper CAP quadratic LOWER:",float(cap_lower),flush=True)
    print("EF05 strict cap minus true-positive Q margin LOWER:",float(margin),flush=True)
    print("EF05 PASS: EF04 complete cap is PROVABLY TOO CONSERVATIVE;",
          "the 890-source sufficient supported Schur gate is impossible.",flush=True)
    print("W-EVEN-FORM OPEN: this is NOT a negative witness",
          "for original K_true or actual Q_e, and does NOT settle RH.",flush=True)


if __name__=="__main__":
    validate()
