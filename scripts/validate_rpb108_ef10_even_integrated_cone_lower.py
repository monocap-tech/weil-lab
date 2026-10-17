#!/usr/bin/env python3
"""EF10: analytic cell-integrated original even conservative cap lower.

Retain exactly EF09 original supported cosine, 256 EF06 low cap cells,
121 original mid cap cells, positive weights, and 788 high leaves.
No signed operator is changed. Instead of taking the smallest
Lipschitz amplitude on EVERY cell as the cell's amplitude, integrate
the proved cone |F(xi)| >= max(0, a - D*abs(xi-mid)) exactly.

A strict cap > EF08's whole actual A_e UPPER is a no-go for the
CONSERVATIVE EF06 refined cap only, never original Weil negativity.
"""
from fractions import Fraction as F

from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_ef05_even_cap_obstruction import (
    DERIVATIVE, supported_even_fourier, absolute_lower, rational_floor,
)
from validate_rpb108_ef06_local_even_signed_cap import improve_original_leaf
from validate_rpb108_ef09_even_cap_lower_refinement import (
    EF08_CERTIFIED_AE_UPPER, LOW_SPLITS, MID_SPLITS
)

# Outward DOWN rounding after analytical integration, at most
# 2960 * 1e-12 absolute loss to the entire cap lower.
DEN=10**12
OLD_EF09_CAP_LOWER=F(8724438013,10**10)


def down12(q):
    assert q>=0
    z=q*DEN
    return F(z.numerator//z.denominator,DEN)


def exact_integrated_cone_lower(a, halfwidth, D):
    """Integral of the squared certified triangular amplitude cone.

    2 * integral_(0..halfwidth) max(0,a-Dt)^2 dt.
    The absolute |F| cone is valid on BOTH halves of the cell.
    All arithmetic is exact rational; D is an outward upper
    derivative from the original physical compact-support transform.
    """
    assert a>=0 and halfwidth>0 and D>0
    if a>=D*halfwidth:
        total=2*(a*a*halfwidth-a*D*halfwidth*halfwidth
                 +D*D*halfwidth**3/3)
    else:
        total=F(2)*a**3/(3*D)
    # The triangular integral is at least the constant-floor
    # rectangle computed using the same midpoint amplitude floor.
    constant=max(F(0),a-D*halfwidth)
    assert total>=2*halfwidth*constant**2
    return total


def whole_cap_lower():
    clusters,width,mass,old_mass=full_upper_leaves()
    assert len(clusters)==107 and old_mass==F(1204033883,32000000)
    low=mid=F(0)
    mass_new=F(0)
    source_leaves=low_cells=mid_cells=far_cells=subcells=0
    for cluster in clusters:
        for l,r,h in cluster:
            source_leaves+=1
            original=h+KAPPA
            assert original>=0 and 0<=l<r
            refined=improve_original_leaf(l,r,h) if r<=1 else [(l,r,original)]
            for a,b,w in refined:
                assert a>=l and b<=r and a<b and w>=0
                mass_new+=2*(b-a)*w
                if a>=4:
                    # Existing original full cap remains present.
                    # Its contribution to a lower bound is >=0.
                    far_cells+=1
                    continue
                assert b<=4
                splits=LOW_SPLITS if b<=1 else MID_SPLITS
                ds=(b-a)/splits
                for k in range(splits):
                    left=a+ds*k
                    right=left+ds
                    center=(left+right)/2
                    # Round amplitude DOWN, derivative UP.
                    amp=rational_floor(absolute_lower(supported_even_fourier(center)))
                    assert amp>=0
                    integral=exact_integrated_cone_lower(amp,ds/2,DERIVATIVE)
                    # Multiply by 2 for the reflected negative-frequency
                    # interval of this real even physical cosine.
                    charge=down12(2*w*integral)
                    if b<=1:
                        low+=charge
                    else:
                        mid+=charge
                    subcells+=1
                if b<=1:
                    low_cells+=1
                else:
                    mid_cells+=1
    assert source_leaves==973 and low_cells==256
    assert mid_cells==121 and far_cells==788
    assert subcells==256*LOW_SPLITS+121*MID_SPLITS==2960
    assert abs(mass_new-F(2960374846875,10**11))<F(1,10**7)
    return low,mid,low+mid,subcells


def validate():
    low,mid,total,n=whole_cap_lower()
    # A stronger bound than EF09 should follow from analytical
    # integration, not simply from adding more midpoint samples.
    assert total>OLD_EF09_CAP_LOWER,(
        "Analytic integral unexpectedly not sharper",
        float(total),float(OLD_EF09_CAP_LOWER))
    margin=total-EF08_CERTIFIED_AE_UPPER
    method="CAP_METHOD_NO_GO" if margin>0 else "STILL_INCONCLUSIVE"
    print("EF10 exact triangular-cone original cap lower [0,1]:",
          float(low),flush=True)
    print("EF10 exact triangular-cone original cap lower [1,4]:",
          float(mid),flush=True)
    print("EF10 original full conservative cap LOWER (infinite high lower zero):",
          float(total),flush=True)
    print("EF10 full physical cosine Fourier subcells:",n,flush=True)
    print("EF10 prior EF09 certified full cap lower >",
          float(OLD_EF09_CAP_LOWER),flush=True)
    print("EF10 separately certified EF08 original positive A_e upper <",
          float(EF08_CERTIFIED_AE_UPPER),flush=True)
    print("EF10 rigorous cap-minus-positive LOWER >",
          float(margin),flush=True)
    print("EF10 comparison:",method,flush=True)
    if margin>0:
        print("EF10 conclusion: EF06/EF07 conservative cap is NOT",
              "dominated by actual original A_e on this SAME physical",
              "even cosine; this is method-class no-go only.",
              "Original K_true,e may be far below the cap. W-EVEN-FORM",
              "and RH OPEN.",flush=True)
    else:
        print("EF10 conclusion: cap comparison still unresolved;",
              "no feasibility and no actual signed negativity.",
              "W-EVEN-FORM and RH OPEN.",flush=True)
    print("EF10 PASS: original signed even/whole Weil, global bridge,",
          "Lean full certificate and RH OPEN.",flush=True)


if __name__=="__main__":
    validate()
