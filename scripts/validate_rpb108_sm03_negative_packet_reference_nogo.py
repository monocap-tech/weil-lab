#!/usr/bin/env python3
"""SM03: exact original signed odd negative packet vs SI29 C14 reference.

Proves impossibility of a *sufficient lower-reference domination method*,
NOT a negative witness for the original Weil form or RH.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import (
    PI,B,LN,WEIGHTS,prime_interval,log_rational_bounds
)
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_si21_odd_jensen_four import KAPPA

C=F(147,40)   # physical odd negative packet center 3.675
RADIUS=F(3,100)
DELTA=F(7,5)  # signed multiplier is <-1.4 throughout
ARCH_TERMS=48
NEG_CELLS=128
POS_CELLS=64

def arch_upper(x):
    """Rigorous original Re psi(1/4+i*pi*x)-log(pi) upper.

    Euler series with decreasing positive tail, using
    sum_{k>=N} f(k+a) <= f(N+a)+ integral_N^infty f(t+a)dt.
    """
    assert x>=0
    y=PI[1]*x
    a=F(1,4)
    partial=sum((y*y/((k+a)*((k+a)**2+y*y))
                 for k in range(ARCH_TERMS)),F(0))
    t=ARCH_TERMS+a
    first=y*y/(t*(t*t+y*y))
    tail=log_rational_bounds(1+(y/t)**2)[1]/2
    H128=sum((F(1,k) for k in range(1,129)),F(0))
    gamma_lo=H128-log_rational_bounds(F(129))[1]
    assert gamma_lo>F(57,100)
    constant_lo=gamma_lo+PI[0]/2+3*LN[2][0]+log_rational_bounds(PI[0])[0]
    return partial+first+tail-constant_lo

def certify_negative_band():
    left,right=C-RADIUS,C+RADIUS
    assert (left,right)==(F(729,200),F(741,200))
    worst=None
    for i in range(NEG_CELLS):
        l=left+(right-left)*i/NEG_CELLS
        r=left+(right-left)*(i+1)/NEG_CELLS
        mid=(l+r)/2
        # Arch is monotone increasing in nonnegative frequency;
        # original signed prime derivative is globally bounded by 69.
        upper=arch_upper(r)+prime_interval(mid)[1]+F(69,2)*(r-l)
        worst=upper if worst is None else max(worst,upper)
        assert upper<-DELTA, (i,float(upper),float(-DELTA))
    return worst

def upper_abs(interval):
    return max(abs(interval[0]),abs(interval[1]))

def old_positive_reference_upper():
    # Exact supported physical odd center Gram. N=||sin(2*pi*C*x)||^2.
    Nlo,Nhi=gram(C,C)
    assert F(1)<Nlo<=Nhi<F(6,5)
    eps=(2*PI[1]*RADIUS*B)**2/6
    assert F(0)<eps<F(1,100)
    # |sinc(2*pi*r*x)-1| <= (2*pi*r*B)^2/6
    normlo=(1-eps)**2*Nlo
    gamma_minus=4*RADIUS*DELTA
    negative_packet_lower=gamma_minus*normlo**2

    positive_upper=KAPPA*Nhi
    derivative=2*PI[1]*B**2
    seen={}
    weights=[]
    for c,r,delta,deg in FEATURES:
        assert deg in (0,1) and r>0 and delta>0
        interval=(c-r,c+r)
        if interval not in seen:
            step=2*r/POS_CELLS
            max_abs=F(0)
            for i in range(POS_CELLS):
                mid=c-r+(i+F(1,2))*step
                hi=upper_abs(gram(C,mid)) + derivative*step/2
                max_abs=max(max_abs,hi)
            seen[interval]=max_abs
        # Use true Jensen mean (factor1) or true normalized first
        # Legendre moment (factor 3 E|u| = 3/2).
        t=F(3,2) if deg else F(1)
        gamma=4*r*delta/(3 if deg else 1)
        v=seen[interval]+2*B*eps
        term=gamma*(t*v)**2
        positive_upper+=term
        weights.append(term)
    assert len(FEATURES)==14 and len(seen)==12
    # Entire positive 14-feature reference, not one cherry-picked term.
    assert positive_upper>0 and negative_packet_lower>positive_upper, (
        "C14 lower-reference obstruction did not certify",
        float(negative_packet_lower), float(positive_upper))
    return negative_packet_lower,positive_upper,eps,Nlo,Nhi,weights

def validate():
    negative_m_upper=certify_negative_band()
    neg,pos,eps,nlo,nhi,weights=old_positive_reference_upper()
    print("SM03 original seven-prime signed multiplier whole-negative-band UPPER:",float(negative_m_upper),flush=True)
    print("SM03 negative interval:",float(C-RADIUS),float(C+RADIUS),"and reflection",flush=True)
    print("SM03 true odd negative Jensen packet Gamma:",float(4*RADIUS*DELTA),flush=True)
    print("SM03 norm center true physical enclosure:",float(nlo),float(nhi),flush=True)
    print("SM03 sinc-to-center uniform error upper:",float(eps),flush=True)
    print("SM03 genuine original negative packet quadratic LOWER:",float(neg),flush=True)
    print("SM03 entire fourteen-feature C14 reference quadratic UPPER:",float(pos),flush=True)
    print("SM03 certified method-class obstruction margin LOWER:",float(neg-pos),flush=True)
    assert neg-pos>F(1,1000)
    print("SM03 PASS: C14-star CANNOT dominate full negative frequency operator",flush=True)
    print("Original A-star negative-frequency inequality W-ODD-NEG still OPEN; RH OPEN",flush=True)

if __name__=="__main__":
    validate()
