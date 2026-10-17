#!/usr/bin/env python3
"""EF04: explicit rational original signed-negative EVEN Taylor moment cap.

Reuses SM10's exact rational ORIGINAL all-frequency cover and moment
coefficients, but uses physical EVEN cosine-Taylor sources rather than odd
sine sources. Verifies 107 full rational SPD moment blocks and the
all-negative infinite/cross error. The missing true supported inverse
890x890 Loewner gate is NOT evaluated or asserted positive.
"""
from fractions import Fraction as F

from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves, exact_block,
)
from validate_rpb108_si10_complement_positivity import (
    KAPPA, protected_outer_band,
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import B
from validate_rpb108_ef02_even_negative_spectral_rank import even_cosine_gram

BITS=24
TAU=F(1,65536)
DIMENSION=890


def parity_and_cross_regression():
    # cos(2*pi*xi*x)'s kth frequency derivative / k! is:
    # (2*pi*x)^k/k! cos(2*pi*c*x + k*pi/2).
    # For even k: x^k even, cosine even; for odd k: x^k odd,
    # phase-shifted cosine is sine odd, so their product remains even.
    for k in range(64):
        polynomial_parity=(-1)**k
        trig_parity=(-1)**k
        assert polynomial_parity*trig_parity == 1

    # On the ORIGINAL compact physical interval, even cosine sources at
    # different frequencies are NOT orthogonal in general: a rigorous
    # rational interval for a concrete physical cross-Gram example.
    # This is a cross-term regression only; these two illustrative
    # frequencies are not represented as actual EF04 cluster centers.
    cross=even_cosine_gram(F(3,10),F(19,25))
    assert F(11,100) < cross[0] < cross[1] < F(12,100), cross
    # A physical source Gram cannot be treated as block diagonal merely
    # because disjoint frequency-cluster MOMENT coefficients are.
    return cross


def validate():
    ext_count,ext_min=protected_outer_band()
    assert ext_count==2535 and ext_min>KAPPA
    clusters,width,mneg,cap_mass=full_upper_leaves()
    assert len(clusters)==107 and width==F(973,32)
    assert mneg==F(1203060883,32000000)
    assert cap_mass==F(1204033883,32000000)
    assert cap_mass==mneg+KAPPA*width
    assert B==F(11,10) and KAPPA==F(1,1000)
    assert TAU==F(1,65536)

    count=0
    nentries=0
    largest=0
    least_pivot=None
    offdiagonal_nonzero=0
    # Each block C_j is the actual complete rational 2∫w(ξ)
    # (ξ-c_j)^(k+l) dξ. This SAME coefficient block multiplies the
    # physical EVEN sources, not the odd functions used by SM10:
    # u_jk^e(x)=(2*pi*x)^k/k! cos(2*pi*c_j*x+k*pi/2).
    for cluster in clusters:
        local_width=cluster[-1][1]-cluster[0][0]
        p,remainder=taylor_order(local_width,BITS)
        assert F(0)<remainder<F(1,2**BITS)
        c=(cluster[0][0]+cluster[-1][1])/2
        C,center,pivots=exact_block(cluster,p)
        assert c==center and center>=0
        assert C[0][0]==2*sum(
            ((h+KAPPA)*(r-l) for l,r,h in cluster),F(0)
        )
        # Check HANKEL identity for every complete k,l pair, rather
        # than just C00/trace. This does not approximate the moments.
        for k in range(p):
            for l in range(p):
                assert C[k][l]==C[l][k]
                if k+l+1<p:
                    assert C[k][l]==C[k+l][0]
                if l>k and C[k][l]!=0:
                    offdiagonal_nonzero+=1

        count+=p
        largest=max(largest,p)
        nentries+=p*(p+1)//2
        for k,pivot in enumerate(pivots):
            assert pivot>0
            ratio=pivot/C[k][k]
            assert 0<ratio<=1
            least_pivot=ratio if least_pivot is None else min(least_pivot,ratio)

    assert count==DIMENSION and largest<256
    assert nentries>DIMENSION and offdiagonal_nonzero>0

    # The analysis error between the TRUE EVEN continuous original cap
    # R_cap and explicit physical Taylor source R_T is bounded by the
    # complete original signed reflected mass; no frequency subband is
    # dropped. Young pays ALL mixed source/remainder cross terms.
    eps2=2*B*cap_mass*F(1,2**(2*BITS))
    eta=(1+1/TAU)*eps2
    assert eta<F(193,10**10)  # 1.93e-8
    assert eta/KAPPA<F(193,10**7) # 1.93e-5
    assert eta<KAPPA
    positive_floor=KAPPA-eta
    assert positive_floor>0

    # Exact physical even Loewner sufficient condition:
    # B_e=A_e-eta I, U=[u_10^e,...,u_jk^e],
    # D=(1+tau) blockdiag(C_j).
    # Q_e >= B_e-U D U*, and full positivity follows if
    # D^-1-U* B_e^-1 U >= 0. The latter matrix is NOT built by EF04.
    # Any future numerical inverse trial must retain the positive
    # residual E*B_e^-1 E in its correct-sign U*B_e^-1 U upper.
    cross=parity_and_cross_regression()
    print("EF04 original signed all-negative envelope mass:",float(cap_mass),flush=True)
    print("EF04 original supported EVEN physical Taylor sources:",count,flush=True)
    print("EF04 exact complete rational moment blocks:",len(clusters),flush=True)
    print("EF04 exact rational SPD LDL pivots:",count,flush=True)
    print("EF04 distinct rational moment upper entries:",nentries,flush=True)
    print("EF04 maximum local Taylor order:",largest,flush=True)
    print("EF04 nonzero upper triangular moment cross entries:",offdiagonal_nonzero,flush=True)
    print("EF04 minimum exact rational LDL pivot/diagonal:",float(least_pivot),flush=True)
    print("EF04 actual physical even cross-Gram example interval:",
          float(cross[0]),float(cross[1]),flush=True)
    print("EF04 full global analysis error square upper:",float(eps2),flush=True)
    print("EF04 fully cross-paid negative-frequency upper tail eta:",float(eta),flush=True)
    print("EF04 original supported positive B_e uniform floor:",float(positive_floor),flush=True)
    print("EF04 PASS (STRUCTURAL ONLY): K_neg,e <= U[(1+tau)C]U* + eta I",flush=True)
    print("W-EVEN-FORM OPEN: U* B_e^-1 U and finite 890-source Schur",
          "positivity not certified; no full Weil, global bridge or RH.",flush=True)


if __name__=="__main__":
    validate()
