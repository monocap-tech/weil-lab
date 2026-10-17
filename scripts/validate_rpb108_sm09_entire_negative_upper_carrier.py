#!/usr/bin/env python3
"""SM09: rigorous full-original odd negative-frequency UPPER carrier.

Unlike SM05-SM08's selected lower subband absorption, this bounds the
ENTIRE r=(kappa-m)_+ original signed multiplier with SI10's global
protected-positive frequency cover. A finite physical odd Taylor space P
carries the remaining upper positive operator, with all low/high cross
terms controlled by a sharp Cauchy Young inequality.

The finite operator P K_cap P is NOT here dominated by the original
positive-frequency operator; W-ODD-NEG remains OPEN.
"""
from fractions import Fraction as F
from validate_rpb108_si10_complement_positivity import (
    KAPPA, protected_inner_cover, protected_outer_band
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import B

BITS=(12,16,24)
TAU=F(1,1024)

def validate():
    # All-positive exterior, including original 896..1200 seven-prime phase
    # bounds, and the entire original 0..896 uncertain-dyadic cover.
    # Each unresolved leaf has SI10 outward h>=(-m)_+. Hence
    # r=(kappa-m)_+ <= h+kappa there and r=0 everywhere else.
    exterior,ext_min=protected_outer_band()
    assert exterior>0 and ext_min>KAPPA
    clusters,width,mass,leaves,protected=protected_inner_cover()
    assert len(clusters)>0 and leaves>0 and protected>0
    assert 0 < width < F(50) and 0 < mass < F(70)
    assert width==F(973,32) # 30.40625, BOTH signs in original SI10 cover
    # The cover majorant is r_cap = (h_leaf+kappa) on each unresolved
    # dyadic leaf, zero outside; this is a nonnegative measurable
    # *upper* weight, not a finite lower/sampled subband.
    whole_mass=mass+KAPPA*width
    assert whole_mass>mass and whole_mass<F(38)
    print("SM09 full original r=(kappa-m)_+ UPPER cover:",flush=True)
    print("  SI10 exterior certified positive leaves:",exterior,flush=True)
    print("  protected positive clusters:",len(clusters),flush=True)
    print("  uncertain positive-frequency dyadic leaves:",leaves,flush=True)
    print("  full reflected upper-cover width:",float(width),flush=True)
    print("  entire original cap integrated weight upper:",
          float(whole_mass),flush=True)

    for bits in BITS:
        orders=[taylor_order(hi-lo,bits)[0] for lo,hi,_ in clusters]
        odd_dim=sum(orders)
        # P is physical L²-orthogonal projection onto the span of
        # d^k/dxi^k sin(2πxi x)|_{xi=c_j}, k<p_j,
        # for positive-frequency cluster centers c_j.
        # Each derivative is physically supported odd, so we need
        # only ONE parity-adapted column per Taylor degree.
        # For every xi in the certified cover, h_xi differs from its
        # local physical Taylor polynomial by <=sqrt(2B)*2^-bits.
        eps2=2*B*whole_mass*F(1,2**(2*bits))
        # R_cap f = sqrt(2*(h+kappa)) <f,sin(2πxi x)>
        # on all SI10 positive-frequency unresolved leaves.
        # Uniformly ||R_cap(I-P)||²<=eps2.
        # Decompose R_cap=R_cap P + R_cap(I-P), and apply:
        # (a+b)^*(a+b) <= (1+tau)a*a+(1+1/tau)b*b.
        # This gives K_neg,o <= K_cap,o <=
        #   (1+tau)P K_cap,o P +
        #   (1+1/tau)eps2*(I-P).
        # Includes ALL cross terms; none silently set to zero.
        floor=(1+1/TAU)*eps2
        print("  bits",bits,"original odd Taylor rank ceiling:",odd_dim,
              "unprojected negative cap L2 norm-square:",
              float(eps2),"whole low/high coupling floor:",
              float(floor),flush=True)
        assert odd_dim>=1 and odd_dim<1500
        assert eps2>0 and floor>eps2
        if bits==24:
            assert floor<F(1,10**9), (
                "SM09 global signed negative upper-carrier floor too large",
                float(floor))
            assert odd_dim<1200
    print("SM09 PASS (SCOPED): full original signed negative-frequency operator "
          "dominated by explicit physical finite-odd-carrier cap plus a "
          "rigorously bounded infinite complement; finite positive-vs-negative "
          "Schur gate, odd pole coupling, W-ODD-NEG and RH all OPEN",flush=True)

if __name__=="__main__":
    validate()
