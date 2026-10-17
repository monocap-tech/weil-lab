#!/usr/bin/env python3
"""SM11: original physically supported odd negative-spectrum rank >=17 above kappa.

17 genuine continuous signed seven-prime negative windows, exact rational
whole-interval upper bounds and original physical Jensen Gram Gershgorin.
If PASS, ANY kappa*I + positive rank <=16 minorant (including SM05 C16)
cannot dominate the *entire* original K_freq,o. This is a METHOD no-go,
not evidence for an off-critical zeta zero or for negativity of actual A_o.
"""
from fractions import Fraction as F
from validate_rpb108_sm03_negative_packet_reference_nogo import arch_upper
from validate_rpb108_si06_negative_band import B, PI, prime_interval
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_si21_odd_jensen_four import KAPPA
from validate_rpb108_sm04_negative_packet_rank import CENTERS as SM04_CENTERS, DELTA as SM04_DELTA, RADIUS as SM04_RADIUS

# Reuse all 15 certified SM04 windows. Add two new genuinely separated
# original seven-prime negative continuum windows, not point samples.
EXTRA_CENTERS=(F(20199,100),F(38956,100))
CENTERS=tuple(sorted(SM04_CENTERS+EXTRA_CENTERS))
N=17
RADIUS=F(1,100)
DELTA=F(2,5)
CELLS=4

def abs_up(x):
    assert x[0] <= x[1]
    return max(abs(x[0]),abs(x[1]))

def certify_all_negative_windows():
    assert len(SM04_CENTERS)==15 and len(CENTERS)==N
    assert SM04_DELTA==DELTA and SM04_RADIUS==RADIUS
    assert len(set(CENTERS))==N
    assert all(CENTERS[i+1]-CENTERS[i]>=5 for i in range(N-1))
    assert set(SM04_CENTERS).issubset(CENTERS)
    worst=None
    for center in CENTERS:
        for j in range(CELLS):
            left=center-RADIUS+2*RADIUS*j/CELLS
            right=center-RADIUS+2*RADIUS*(j+1)/CELLS
            mid=(left+right)/2
            # Original seven-prime m=arch+prime. The arch term is
            # monotone for xi>0, so arch_upper(right) is full-cell upper.
            # Signed prime derivative <= 69; exact rational phase source
            # has no sampled-only acceptance.
            upper=arch_upper(right)+prime_interval(mid)[1]+F(69,2)*(right-left)
            assert upper < -DELTA, (
                "Uncertified SM11 full original negative frequency window",
                str(center),j,float(upper))
            worst=upper if worst is None else max(worst,upper)
    return worst

def certify_physical_rank():
    eps=(2*PI[1]*RADIUS*B)**2/6
    assert 0<eps<F(1,100)
    lows=[]
    off_sums=[]
    for i,c in enumerate(CENTERS):
        gc=gram(c,c)
        lows.append((1-eps)**2*gc[0])
        s=F(0)
        for j,d in enumerate(CENTERS):
            if i==j: continue
            gd=gram(c,d)
            s+=abs_up(gd)+4*B*eps
        off_sums.append(s)
    lower=min((a-b for a,b in zip(lows,off_sums)))
    gamma=4*RADIUS*DELTA
    assert gamma==F(2,125)
    # Need only lower >kappa/gamma=.0625, but choose an
    # intentionally stronger safe physical nearly-orthogonal bound.
    assert lower>F(4,5),(
        "17 real odd supported Jensen Gram not certified",
        float(lower),float(max(off_sums)))
    lam=gamma*lower
    assert lam>F(12,1000)>KAPPA
    return lower,lam,eps,min(lows),max(off_sums)

def validate():
    upper=certify_all_negative_windows()
    lower,lam,eps,min_diag,max_off=certify_physical_rank()
    assert upper<-DELTA
    assert N==17
    print("SM11 original whole negative continuum windows:",N,flush=True)
    print("SM11 rational centers:",tuple(str(c) for c in CENTERS),flush=True)
    print("SM11 worst whole-interval original multiplier upper:",float(upper),flush=True)
    print("SM11 actual physical odd sinc-to-center error upper:",float(eps),flush=True)
    print("SM11 actual physical Gram minimum diagonal:",float(min_diag),flush=True)
    print("SM11 physical Gram maximum off-diagonal row upper:",float(max_off),flush=True)
    print("SM11 rigorous 17-mode physical Gram Gershgorin lower:",float(lower),flush=True)
    print("SM11 original K_negative lambda_17 lower:",float(lam),flush=True)
    print("SM11 scalar reference floor kappa:",float(KAPPA),flush=True)
    print("SM11 PASS (SCOPED): every kappa I + PSD rank <=16 "
          "reference FAILS to dominate the original full odd negative "
          "frequency operator, including the retained SM05/SM10 C16; "
          "the ACTUAL A_o is not rank 16 and W-ODD-NEG remains OPEN",flush=True)

if __name__=="__main__":
    validate()
