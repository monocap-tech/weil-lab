#!/usr/bin/env python3
"""EF07: entire original signed EVEN refined-cap witness interval pilot.

One original physical supported even cosine f=cos(2*pi*19x/25).
Compute rigorously both-sided FULL refined signed-negative-cap Rayleigh
intervals, using all SI10 rational leaves, EF06 exact [0,1] subcells,
and a complete analytic >=4 continuum tail. Independently bound both
sides of the genuine original supported positive energy, including
the rank-one even pole, signed original positive Fourier excess,
and global scalar floor. No invented finite inverse/Schur positivity.

Conditional method decisions are based ONLY on certified interval
separation, not midpoint numerics. Even if the one-vector cap passes,
that is NOT a whole-operator proof.
"""
from fractions import Fraction as F

from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_si06_negative_band import B, PI, prime_interval
from validate_rpb108_si07_negative_support_cover import M, arch_lower_cell
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_ef02_even_negative_spectral_rank import even_cosine_gram
from validate_rpb108_ef05_even_cap_obstruction import (
    CENTER, T, DERIVATIVE, TAIL_UP, supported_even_fourier,
    absolute_lower, absolute_upper, rational_floor, rational_ceil,
    true_positive_pole_upper, actual_positive_low_upper, certified_tail,
)
from validate_rpb108_ef06_local_even_signed_cap import improve_original_leaf

POSITIVE_BINS=64
ARCH_STEPS=8
BOUNDARY=F(4)


def physical_fourier_bounds(l,r):
    """Certified all-continuum amplitude enclosure on interval [l,r]."""
    mid=(l+r)/2
    interval=supported_even_fourier(mid)
    loss=DERIVATIVE*(r-l)/2
    low=max(F(0), absolute_lower(interval)-loss)
    high=absolute_upper(interval)+loss
    return rational_floor(low), rational_ceil(high)


def old_new_global_cap_intervals():
    clusters,width,mass,old_mass=full_upper_leaves()
    assert len(clusters)==107 and old_mass==F(1204033883,32000000)
    old_lo=old_hi=new_lo=new_hi=F(0)
    count_old=count_new=count_far=0
    far_hi=F(0)
    mass_new=F(0)
    bands={}
    for cluster in clusters:
        for l,r,h in cluster:
            original=h+KAPPA
            if r<=F(1):
                refined=improve_original_leaf(l,r,h)
            else:
                refined=[(l,r,original)]
            count_old+=1
            count_new+=len(refined)
            for a,b,w in refined:
                mass_new+=2*(b-a)*w

            if l>=BOUNDARY:
                # EF05 analytic Fourier bound |F(xi)|²<1/(8xi²)
                # for EACH xi>=4. Lower 0 (no sampled phases).
                far_hi += original*(r-l)/(4*l*l)
                count_far+=1
                continue

            assert r<=BOUNDARY
            low,high=physical_fourier_bounds(l,r)
            old_lo+=2*original*(r-l)*low**2
            old_hi+=2*original*(r-l)*high**2
            for a,b,w in refined:
                lo,hi=physical_fourier_bounds(a,b)
                new_lo+=2*w*(b-a)*lo**2
                new_hi+=2*w*(b-a)*hi**2
                key="0-1" if b<=1 else "1-4"
                q=bands.setdefault(key,{"lower":F(0),"upper":F(0),"count":0})
                q["lower"]+=2*w*(b-a)*lo**2
                q["upper"]+=2*w*(b-a)*hi**2
                q["count"]+=1

    assert count_old==973 and count_new==1165 and count_far>0
    assert mass_new<old_mass and far_hi>0
    assert abs(mass_new-F(2960374846875,10**11))<F(1,10**7)
    assert bands["0-1"]["count"]==256
    # Both full cap totals have all high-frequency original leaves in
    # the rigorously integrated upper; no uncharged tail.
    old_upper=old_hi+far_hi
    new_upper=new_hi+far_hi
    assert new_upper<=old_upper and new_lo<=new_upper
    return dict(old_lower=old_lo,old_upper=old_upper,
                new_lower=new_lo,new_upper=new_upper,
                mass_new=mass_new,far_upper=far_hi,
                old_leaves=count_old,new_cells=count_new,
                high_leaves=count_far,bands=bands)


def original_actual_positive_interval():
    """Independently bound actual original positive Fourier operator.

    Lower: kappa||f||² + signed-positive excess on [0,4] using 1/8
    archimedean-group left lower, whole seven-prime interval lower
    and 1/64 signed-prime derivative width. The positive even pole is
    included with BOTH lower and upper bounds. Upper inherits EF05's
    fully paid original signed [0,4] plus analytic full >=4 tail.
    """
    norm=even_cosine_gram(CENTER,CENTER)
    assert norm[0]>0 and norm[1]>norm[0]
    pole_up,overlap=true_positive_pole_upper()
    pole_low=2*absolute_lower(overlap)**2
    assert 0<pole_low<=pole_up<F(17,50)

    arch=[arch_lower_cell(F(j,ARCH_STEPS))
          for j in range(int(BOUNDARY*ARCH_STEPS))]
    excess=F(0)
    certified_positive_cells=0
    for i in range(int(BOUNDARY*POSITIVE_BINS)):
        l=F(i,POSITIVE_BINS)
        r=F(i+1,POSITIVE_BINS)
        mid=(l+r)/2
        aidx=(i*ARCH_STEPS)//POSITIVE_BINS
        mlow=arch[aidx]+prime_interval(mid)[0]-M*(r-l)/2
        signed_gain=rational_floor(max(F(0),mlow-KAPPA))
        if signed_gain:
            lo,_=physical_fourier_bounds(l,r)
            excess+=2*(r-l)*signed_gain*lo**2
            certified_positive_cells+=1

    actual_low=KAPPA*norm[0]+excess+pole_low
    low_freq_upper,_,n=actual_positive_low_upper()
    assert n==256
    whole_tail=certified_tail()
    actual_upper=low_freq_upper+whole_tail+pole_up
    assert actual_low>0 and actual_upper>actual_low
    return dict(lower=actual_low,upper=actual_upper,
                norm_lower=norm[0],norm_upper=norm[1],
                pole_lower=pole_low,pole_upper=pole_up,
                positive_signed_excess_lower=excess,
                positive_cells=certified_positive_cells,
                low_freq_upper=low_freq_upper,
                high_freq_upper=whole_tail)


def validate():
    cap=old_new_global_cap_intervals()
    positive=original_actual_positive_interval()
    # For a single actual supported f, isolate *rigorous* differences.
    lower_gap=cap["new_lower"]-positive["upper"]
    upper_gap=cap["new_upper"]-positive["lower"]
    assert lower_gap<=upper_gap
    # Do NOT assert either order: EF07 is a discriminator, not a
    # pre-written claim that the refined majorant is feasible.
    status=("CAP_NO_GO" if lower_gap>0 else
            "WITNESS_PASSES" if upper_gap<0 else "INCONCLUSIVE")
    assert status in ("CAP_NO_GO","WITNESS_PASSES","INCONCLUSIVE")
    print("EF07 old original cap whole Rayleigh interval:",
          float(cap["old_lower"]),float(cap["old_upper"]),flush=True)
    print("EF07 improved original cap whole Rayleigh interval:",
          float(cap["new_lower"]),float(cap["new_upper"]),flush=True)
    print("EF07 full cap high-frequency signed tail UPPER:",
          float(cap["far_upper"]),flush=True)
    for name,q in cap["bands"].items():
        print("EF07 refined original cap band",name,"cells",q["count"],
              "lower",float(q["lower"]),"upper",float(q["upper"]),flush=True)
    print("EF07 original cap full integrated upper mass:",
          float(cap["mass_new"]),flush=True)
    print("EF07 original positive pole interval:",
          float(positive["pole_lower"]),float(positive["pole_upper"]),flush=True)
    print("EF07 original signed-positive excess lower:",
          float(positive["positive_signed_excess_lower"]),
          "certified cells",positive["positive_cells"],flush=True)
    print("EF07 entire actual original positive energy interval:",
          float(positive["lower"]),float(positive["upper"]),flush=True)
    print("EF07 complete cap-minus-original-positive interval:",
          float(lower_gap),float(upper_gap),flush=True)
    print("EF07 rigorous SAME EVEN WITNESS status:",status,flush=True)
    if status=="CAP_NO_GO":
        print("EF07 result: refined full cap STILL obstructed by this f;",
              "no result against true original even Weil form.",flush=True)
    elif status=="WITNESS_PASSES":
        print("EF07 result: same f satisfies new cap<=actual positive;",
              "other even directions and full Schur UNPROVED.",flush=True)
    else:
        print("EF07 result: certified intervals overlap; do not claim",
              "new cap feasibility or impossibility.",flush=True)
    print("EF07 PASS (SCOPE): all original frequency bands charged;",
          "W-EVEN-FORM, whole Weil, global bridge and RH OPEN.",flush=True)


if __name__=="__main__":
    validate()
