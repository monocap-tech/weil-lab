#!/usr/bin/env python3
"""SM04: certify >=15 full ORIGINAL odd signed-negative directions above kappa.

Method-class spectral rank lower bound, not positivity of the Weil form.
Uses SM03's rigorous original multiplier upper and SI18's exact physical Gram.
"""
from fractions import Fraction as F
from validate_rpb108_sm03_negative_packet_reference_nogo import arch_upper
from validate_rpb108_si06_negative_band import B, PI, prime_interval
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_si21_odd_jensen_four import KAPPA

# Independent true-negative signed windows, rational centers, reflected.
# Greedy nonoverlapping selection from negative minima across original
# signed multiplier. Exact validation certifies each whole interval.
CENTERS=tuple(F(a,100) for a in (
    190,726,1442,2004,2732,3908,4470,5912,6640,7648,
    8376,10380,14288,18756,24668
))
N=15
RADIUS=F(1,100)
DELTA=F(2,5)
CELLS=4

def abs_up(interval):
    assert interval[0]<=interval[1]
    return max(abs(interval[0]),abs(interval[1]))

def original_negative_certificates():
    assert len(CENTERS)==N and len(set(CENTERS))==N
    assert all(CENTERS[j+1]-CENTERS[j]>=5 for j in range(N-1))
    worst=None
    for center in CENTERS:
        lo=center-RADIUS
        hi=center+RADIUS
        band_upper=None
        for i in range(CELLS):
            a=lo+(hi-lo)*i/CELLS
            b=lo+(hi-lo)*(i+1)/CELLS
            mid=(a+b)/2
            # Whole rational subcell: arch monotonic upper evaluated at b;
            # signed full-seven-prime derivative <=69 gives BOTH sides.
            upper=arch_upper(b)+prime_interval(mid)[1]+F(69,2)*(b-a)
            assert upper<-DELTA,(center,i,float(upper))
            band_upper=upper if band_upper is None else max(upper,band_upper)
        worst=band_upper if worst is None else max(worst,band_upper)
    return worst

def physical_odd_gram_lower():
    # True g_c(x)=sin(2*pi*c*x)*sinc(2*pi*r*x) on [-B,B] odd.
    # The full reflected negative signed bands give Kneg >= gamma sum |g><g|.
    eps=(2*PI[1]*RADIUS*B)**2/6
    assert F(0)<eps<F(1,100)
    # Pointwise 1-eps <= sinc <=1, hence diagonal norm
    # ||g_c||² >=(1-eps)^2 ||sin_c||².
    # |<g_i,g_j> - <sin_ci,sin_cj>| <=4B eps
    # from Cauchy with ||f|| <=sqrt(2B) and uniform sinc error.
    diag=[]
    off=[]
    for i,c in enumerate(CENTERS):
        sii=gram(c,c)
        diag.append((1-eps)**2*sii[0])
        offsum=F(0)
        for j,d in enumerate(CENTERS):
            if i==j: continue
            hij=gram(c,d)
            offsum+=abs_up(hij)+4*B*eps
        off.append(offsum)
    gersh=min(x-y for x,y in zip(diag,off))
    gamma=4*RADIUS*DELTA
    # The exact Gram of 15 true odd packets is SPD by Gershgorin.
    # Nonzero eigenvalues of gamma GG* = gamma G*G.
    assert min(diag)>F(1)
    assert gersh>F(9,10),(float(gersh),float(min(diag)),float(max(off)))
    assert gamma==F(2,125)
    assert gamma*gersh>F(14,1000)
    assert gamma*gersh>KAPPA
    return gersh, gamma*gersh,eps,min(diag),max(off)

def validate():
    signed_upper=original_negative_certificates()
    gersh,eigen_floor,eps,diaglo,offmax=physical_odd_gram_lower()
    assert signed_upper<-DELTA
    print("SM04 full-original signed negative windows:",len(CENTERS),flush=True)
    print("SM04 rational centers:",tuple(map(str,CENTERS)),flush=True)
    print("SM04 maximum whole-interval signed multiplier UPPER:",float(signed_upper),flush=True)
    print("SM04 continuous true-odd Jensen packet sinc error UPPER:",float(eps),flush=True)
    print("SM04 min diagonal physical packet Gram LOWER:",float(diaglo),flush=True)
    print("SM04 max offdiag physical packet Gram row UPPER:",float(offmax),flush=True)
    print("SM04 rigorous fifteen-mode Gram eigenvalue LOWER:",float(gersh),flush=True)
    print("SM04 original full negative-frequency lambda_15 LOWER:",float(eigen_floor),flush=True)
    print("SM04 scalar baseline floor kappa:",float(KAPPA),flush=True)
    print("SM04 PASS: every kappa-I plus rank<=14 positive reference fails to dominate the full K_negative on H_odd",flush=True)
    print("Original A_o has additional infinite-rank positive structure; W-ODD-NEG and RH remain OPEN.",flush=True)

if __name__=="__main__":
    validate()
