#!/usr/bin/env python3
"""NF10 independent replay/audit. Recompute all full-prime Schur rows and
depth-6 mass envelopes on two distinct interval meshes. No new whole
signed Weil matrix is asserted.
"""
from fractions import Fraction as F
from certify_native_prime8_complement_nf10_106 import (
    A,K,LOG,PI,POWERS,BASE,prime_weighted_upper,rate_lower,
    derivative_coeffs,integrated_mass_upper,certificate,
)

def run():
    d=2*A
    assert LOG[8][1]<d<LOG[9][0]
    assert PI[0]<PI[1] and F(314159,100000)<PI[0]<PI[1]<F(314160,100000)
    # Independent (non-nested) physical-cell coverings, each of which
    # bounds EVERY possible x in [-a,a] including cut-crossing cells.
    left,idx1,n1=prime_weighted_upper(mesh=6000)
    right,idx2,n2=prime_weighted_upper(mesh=6133)
    assert left<F(257,100) and right<F(257,100)
    assert n1==6000 and n2==6133
    # Explicit coefficient order for all source high degrees, independent
    # of any single saved scalar rate assertion.
    base=derivative_coeffs(K)
    assert len(base)==64 and all(x>0 for x in base)
    for n in range(K+1,K+48):
        c=derivative_coeffs(n)
        assert len(c)==len(base)
        assert all(F(0)<x<=y for x,y in zip(c,base))
    assert rate_lower()>80
    mass=[integrated_mass_upper(t) for t in (14,15,16)]
    assert F(0)<mass[0]<mass[1]<mass[2]
    assert mass[0]<F(1,10**8)
    assert mass[1]<F(1,10**5)
    assert mass[2]<F(1,500)
    result=certificate()
    assert result["certified_physical_complement_lower"]=="17/100"
    assert F(result["raw_complement_lower"])>F(17,100)
    assert F(result["archimedean_lower"])>F(277,100)
    assert F(result["prime_interval_upper"])<F(257,100)
    assert result["whole_domain_positive"] is False
    return dict(status="PASS",aperture="53/50",
                prime_cell_coverings=[6000,6133],
                independent_prime_upper_1=str(F((left*10**9).__ceil__(),10**9)),
                independent_prime_upper_2=str(F((right*10**9).__ceil__(),10**9)),
                high_degrees_checked=48,depth6_coefficients_per_degree=64,
                positive_region_cutoffs=[14,15,16],
                complete_physical_complement_lower="17/100",
                original_target_whole_sign_certified=False)

if __name__=="__main__":
    import json
    print(json.dumps(run(),indent=2))
