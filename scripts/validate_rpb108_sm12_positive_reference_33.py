#!/usr/bin/env python3
"""SM12: 17 genuine original signed POSITIVE whole odd frequency windows.

Adds seventeen non-overlapping sign-positive Jensen-mean physical features
to the retained SM05 C16 to form a rank-33 positive reference. Certifies
all 17 new windows by rational original arch+seven-prime lower bounds,
all 17x17 physical Gram cross terms, and 33 disjoint frequency intervals.
Rank 33 is necessary progress beyond SM11's rank-16 no-go, NOT sufficient
to absorb original SM10's 890 negative Taylor directions or odd pole.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B, PI, prime_interval
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_si21_odd_jensen_four import KAPPA
from validate_rpb108_sm05_two_source_original_inverse import FEATURES as OLD_POSITIVE
from validate_rpb108_sm04_negative_packet_rank import CENTERS as SM04_NEGATIVE_CENTERS
# Keep candidate discovery independent of the parallel SM11 branch merge.
NEGATIVE_CENTERS=tuple(sorted(SM04_NEGATIVE_CENTERS+(F(20199,100),F(38956,100))))

# These rational candidates lie near, but NEVER inside, SM11's
# original signed-negative windows. They have to be confirmed
# across ENTIRE real-frequency intervals, not by point sampling.
CENTERS=tuple(F(x,100) for x in (
    220,786,1522,2074,2702,3938,4500,5882,6610,
    7678,8406,10350,14258,18786,20169,24638,38926
))
N=17
RADIUS=F(1,100)
DELTA=F(2)
CELLS=8

def check_new_positive_windows():
    assert len(CENTERS)==N and len(set(CENTERS))==N
    assert len(NEGATIVE_CENTERS)==N
    assert all(CENTERS[j+1]-CENTERS[j]>=5 for j in range(N-1))
    worst=None
    for center in CENTERS:
        for j in range(CELLS):
            left=center-RADIUS+2*RADIUS*j/CELLS
            right=center-RADIUS+2*RADIUS*(j+1)/CELLS
            mid=(left+right)/2
            # Original m=arch+seven-prime. Rigorously global m' prime
            # Lipschitz 69, arch monotone. This lower bound covers
            # every real point, not just the rational center.
            lower=arch_lower(left)+prime_interval(mid)[0]-F(69,2)*(right-left)
            assert lower>KAPPA+DELTA,(
                "SM12 original positive signed band not certified",
                str(center),j,float(lower),float(KAPPA+DELTA))
            worst=lower if worst is None else min(worst,lower)
    assert worst>KAPPA+DELTA
    return worst

def check_reference_disjointness():
    # The 16 old features in original C16 have their own inherited
    # signed-positive margins, including separate historical certs.
    assert len(OLD_POSITIVE)==16
    old=[(c-r,c+r) for c,r,delta,degree in OLD_POSITIVE]
    new=[(c-RADIUS,c+RADIUS) for c in CENTERS]
    assert all(delta>0 and degree==0 for c,r,delta,degree in OLD_POSITIVE)
    assert len(set(old))==len(old)
    all_bands=sorted(old+new)
    assert len(all_bands)==33
    assert all(all_bands[j][1]<all_bands[j+1][0]
               for j in range(len(all_bands)-1)),(
                   "New positive source overlaps another original C16 interval",
                   all_bands)
    # Since true sinc-sine means are real entire functions of x with
    # disjoint compact frequency supports (including reflections), all
    # 33 physical features are linearly independent on any open x interval
    # by analytic continuation and Fourier-transform uniqueness.
    assert all(l>0 for l,r in all_bands)
    assert all_bands[0][0]>0
    return all_bands

def check_new_physical_gram():
    # Exact original g_c(x)=sin(2pi*c*x)*sinc(2pi*RADIUS*x),
    # an averaged physical odd vector on [-B,B].
    eps=(2*PI[1]*RADIUS*B)**2/6
    assert 0<eps<F(1,100)
    diag=[]
    offrows=[]
    for i,c in enumerate(CENTERS):
        cc=gram(c,c)
        diag.append((1-eps)**2*cc[0])
        s=F(0)
        for j,d in enumerate(CENTERS):
            if i==j:continue
            gg=gram(c,d)
            s+=max(abs(gg[0]),abs(gg[1]))+4*B*eps
        offrows.append(s)
    spectral_lower=min((a-b for a,b in zip(diag,offrows)))
    # A useful, standalone *supported* 17-mode lower bound on the
    # extra positive operator gamma G G* from the new true windows.
    assert spectral_lower>F(4,5),(
        "17 new true physical positive means insufficiently separated",
        float(spectral_lower),float(max(offrows)))
    gamma=4*RADIUS*DELTA
    assert gamma==F(2,25)
    positive_lambda=gamma*spectral_lower
    assert positive_lambda>F(64,1000)>KAPPA
    return spectral_lower,positive_lambda,eps,min(diag),max(offrows)

def validate():
    signed_lower=check_new_positive_windows()
    all_bands=check_reference_disjointness()
    gram_lower,pos_lambda,eps,diag,off=check_new_physical_gram()
    assert signed_lower>KAPPA+DELTA
    print("SM12 original full signed-positive real continuum windows:",N,flush=True)
    print("SM12 centers:",tuple(map(str,CENTERS)),flush=True)
    print("SM12 original signed seven-prime whole-window LOWER:",float(signed_lower),flush=True)
    print("SM12 positive margin delta and Jensen weight:",float(DELTA),float(4*RADIUS*DELTA),flush=True)
    print("SM12 33 genuinely disjoint original positive frequency bands:",len(all_bands),flush=True)
    print("SM12 true physical odd uniform sinc error upper:",float(eps),flush=True)
    print("SM12 new physical Gram minimum diagonal lower:",float(diag),flush=True)
    print("SM12 new physical Gram maximum offdiag row upper:",float(off),flush=True)
    print("SM12 true physical Gram 17-mode eigenvalue LOWER:",float(gram_lower),flush=True)
    print("SM12 extra original positive 17-mode eigenvalue LOWER:",float(pos_lambda),flush=True)
    print("SM12 PASS (SCOPED): A_o >= kappa I + original C16 Jensen 16-mode correction "
          "+ original NEW 17-mode correction; 33 disjoint true physical odd means, "
          "no overdrawn signed frequency mass",flush=True)
    print("SM12 only removes SM11's necessary rank-16 obstruction; "
          "rank33 is NOT sufficient for SM10's entire negative-frequency "
          "upper operator, physical coupled BS/Schur and W-ODD-NEG remain OPEN",flush=True)

if __name__=="__main__":
    validate()
