#!/usr/bin/env python3
"""SM13: exact physical Jensen-Rayleigh diagnostic of C33 vs original Kneg,o.

This compares the *actual* original, physically supported odd lower
negative-frequency Jensen packets from SM11 against the *actual* SM12
33-feature positive Jensen LOWER REFERENCE, with all thirty-three
signed overlap terms, using exact rational outward sine Gram bounds.

A positive witness margin proves C33 cannot dominate the full Kneg,o.
That would disqualify C33 as a sufficient WHOLE-negative Loewner lower
reference, but says NOTHING negative about the original full A_o.
An inconclusive margin proves neither positivity nor a method no-go.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_si21_odd_jensen_four import KAPPA
from validate_rpb108_sm11_rank17_c16_nogo import (
    CENTERS as NEG_CENTERS, RADIUS as NEG_RADIUS,
    DELTA as NEG_DELTA, certify_all_negative_windows,
)
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as NEW_CENTERS, RADIUS as NEW_RADIUS,
    DELTA as NEW_DELTA, OLD_POSITIVE,
    check_new_positive_windows, check_reference_disjointness,
)

def abs_hi(iv):
    assert iv[0]<=iv[1]
    return max(abs(iv[0]),abs(iv[1]))

def sinc_error(radius):
    # |sinc(2*pi*r*x)-1| <= (2*pi_upper*r*B)^2/6
    # and |sinc|<=1 on all real x, for true Jensen averages.
    e=(2*PI[1]*radius*B)**2/6
    assert F(0)<e<F(1,100)
    return e

def positive_data():
    old=[(c,r,4*r*delta) for c,r,delta,degree in OLD_POSITIVE]
    assert len(old)==16 and all(degree==0 for _,_,_,degree in OLD_POSITIVE)
    new=[(c,NEW_RADIUS,4*NEW_RADIUS*NEW_DELTA) for c in NEW_CENTERS]
    assert len(new)==17 and 4*NEW_RADIUS*NEW_DELTA==F(2,25)
    data=old+new
    assert len(data)==33
    # C33 = kappa I + sum_j gamma_j |g_pos,j><g_pos,j|,
    # with true physical Jensen means (not Fourier point sources).
    return [(c,r,gamma,sinc_error(r)) for c,r,gamma in data]

def physical_single_rayleigh(c,pos):
    """Outward original signed-negative MINUS C33 on true g_neg,c.

    Jensen: Kneg >= (2/125) sum_j |g_neg,j><g_neg,j|.
    A single diagonal term gives true quadratic lower
      <g_neg,c,Kneg g_neg,c> >= (2/125)||g_neg,c||^4.
    Positive reference exact quadratic has ALL 33 overlaps. Each
    true sinc-envelope perturbs an original sine by <=e pointwise;
      |<g_neg,c,g_pos,d>| <= |<h_c,h_d>|
          + 2 B (e_neg+e_pos).
    These are exact rational certified UP bounds, no sampled
    physical-frequency grid or false orthogonality assumption.
    """
    en=sinc_error(NEG_RADIUS)
    nlo,nhi=gram(c,c)
    assert F(0)<nlo<=nhi
    norm_lo=(1-en)**2*nlo
    norm_hi=nhi
    gn=4*NEG_RADIUS*NEG_DELTA
    assert gn==F(2,125)
    negative_lower=gn*norm_lo**2
    positive_upper=KAPPA*norm_hi
    old_terms=F(0)
    new_terms=F(0)
    largest=(F(0),None,None)
    for i,(pc,pr,gamma,ep) in enumerate(pos):
        cross_hi=abs_hi(gram(c,pc))+2*B*(en+ep)
        assert cross_hi>0
        term=gamma*cross_hi**2
        if i<16:old_terms+=term
        else:new_terms+=term
        if term>largest[0]:
            largest=(term,pc,i)
        positive_upper+=term
    assert old_terms>0 and new_terms>0
    return {
        "center":c,
        "negative_lower":negative_lower,
        "positive_upper":positive_upper,
        "margin":negative_lower-positive_upper,
        "old_positive_terms_upper":old_terms,
        "new_positive_terms_upper":new_terms,
        "largest_term":largest,
        "norm_lo":norm_lo,
        "norm_hi":norm_hi,
    }

def validate():
    # Anchor every claimed original negative or positive continuum packet
    # to the exact full-seven-prime ALL-REAL signed interval validators.
    worst_negative_upper=certify_all_negative_windows()
    worst_positive_lower=check_new_positive_windows()
    check_reference_disjointness()
    assert worst_negative_upper<-NEG_DELTA
    assert worst_positive_lower>KAPPA+NEW_DELTA
    data=positive_data()
    results=[]
    for c in NEG_CENTERS:
        record=physical_single_rayleigh(c,data)
        results.append(record)
        print("SM13 original true odd packet",float(c),
              "Kneg quadratic LOWER",float(record["negative_lower"]),
              "C33 quadratic UPPER",float(record["positive_upper"]),
              "signed margin LOWER",float(record["margin"]),
              flush=True)
    assert len(results)==17
    assert len(set(NEG_CENTERS))==17
    strongest=max(results,key=lambda x:x["margin"])
    weakest=min(results,key=lambda x:x["margin"])
    print("SM13 17 true-negative packets checked, complete C33 cross terms:",
          len(results)*len(data),flush=True)
    print("SM13 max witness margin lower",float(strongest["margin"]),
          "at original negative center",str(strongest["center"]),flush=True)
    print("SM13 min margin lower",float(weakest["margin"]),
          "at original negative center",str(weakest["center"]),flush=True)
    print("SM13 winning packet C16 upper contribution",
          float(strongest["old_positive_terms_upper"]),flush=True)
    print("SM13 winning packet new C17 upper contribution",
          float(strongest["new_positive_terms_upper"]),flush=True)
    print("SM13 all-real original negative upper",float(worst_negative_upper),
          "positive lower",float(worst_positive_lower),flush=True)
    if strongest["margin"]>0:
        assert strongest["negative_lower"]>strongest["positive_upper"]
        print("SM13 PASS (SCOPED C33 METHOD NO-GO): there exists a "
              "true physically supported negative Jensen packet f such that "
              "<f,Kneg,o f> > <f,C33 f>; hence the unchanged C33 lower "
              "reference CANNOT dominate the entire original negative "
              "operator, even before the odd pole. The actual A_o may "
              "still dominate; W-ODD-NEG and RH OPEN.",flush=True)
    else:
        print("SM13 PASS (DIAGNOSTIC INCONCLUSIVE): no single diagonal "
              "17-packet Rayleigh obstruction was certified by this "
              "outward method. C33 inverse/891-source positivity is NOT "
              "certified; W-ODD-NEG and RH OPEN.",flush=True)

if __name__=="__main__":
    validate()
