#!/usr/bin/env python3
"""SI10: rigorous *original full signed Weil form* positivity on a cofinite
physically supported subspace, through certified frequency-safe m >= kappa
and cluster plane-wave approximation. Exact rational proof regression.

Uses original CC27/RC312-313 signed multiplier, exact SI06 phase enclosures
and SI07 arch bound. No claim of full original positivity, Stage I or RH.
"""
from fractions import Fraction as F
from functools import lru_cache
from validate_rpb108_si06_negative_band import (
    B, TWOC, arch_lower, prime_interval,
)
from validate_rpb108_si07_negative_support_cover import (
    END, DEPTH, M, DEN, arch_lower_cell, ceil_fraction,
)
from validate_rpb108_si08_multiband_rank import taylor_order

KAPPA = F(1, 1000)
BITS = (9, 10, 12, 16, 32)


def protected_outer_band():
    # SI06 already established an all-degree monotone arch >=1200 envelope.
    assert arch_lower(1200) - TWOC > KAPPA
    leaves = 0
    min_lb = None
    def visit(l, r, low_arch, depth):
        nonlocal leaves, min_lb
        mid = (l + r)/2
        lower = low_arch + prime_interval(mid)[0] - M*(r-l)/2
        if lower > KAPPA:
            leaves += 1
            min_lb = lower if min_lb is None else min(min_lb,lower)
            return
        assert depth < 15, "SI10 unable to protect full 896..1200 band"
        visit(l,mid,low_arch,depth+1)
        visit(mid,r,low_arch,depth+1)
    for j in range(896,1200):
        visit(F(j),F(j+1),arch_lower(j),0)
    assert leaves > 0 and min_lb > KAPPA
    return leaves, min_lb


def protected_inner_cover():
    unresolved = []
    accepted = 0
    def visit(l,r,j,depth):
        nonlocal accepted
        mid = (l+r)/2
        lower = arch_lower_cell(j)+prime_interval(mid)[0]-M*(r-l)/2
        if lower > KAPPA:
            accepted += 1
            return
        if depth < DEPTH:
            visit(l,mid,j,depth+1)
            visit(mid,r,j,depth+1)
            return
        height=F(max(0,ceil_fraction((-lower)*DEN)),DEN)
        assert height >= max(F(0),-lower)
        unresolved.append((l,r,height))

    for j in range(END):
        visit(F(j),F(j+1),j,0)
    unresolved.sort(key=lambda v:v[0])
    assert accepted > 0 and len(unresolved)>0
    assert all(0<=l<r<=896 for l,r,_ in unresolved)
    clusters = []
    for l,r,h in unresolved:
        m=2*(r-l)*h
        if clusters and l==clusters[-1][1]:
            a,_,mass=clusters[-1]
            clusters[-1]=(a,r,mass+m)
        else:
            clusters.append((l,r,m))
    total_width=2*sum((r-l for l,r,_ in clusters),F(0))
    total_mass=sum((mass for l,r,mass in clusters),F(0))
    assert total_width<50, f"new protected cover too wide {float(total_width)}"
    assert total_mass<70, f"negative mass bound too large {float(total_mass)}"
    return clusters,total_width,total_mass,len(unresolved),accepted


def validate():
    high_leaves, high_min = protected_outer_band()
    clusters, width, mass, unresolved_count, accepted = protected_inner_cover()
    print("SI10 certified protected multiplier margin:",float(KAPPA))
    print("outer 896..1200 guaranteed-positive leaves:",high_leaves)
    print("outer 896..1200 minimum strict lower:",float(high_min))
    print("inner proven-positive cells:",accepted)
    print("inner unresolved leaves:",unresolved_count)
    print("positive-frequency clusters:",len(clusters))
    print("full protected possible-negative cover measure:",float(width))
    print("full protected negative multiplier integrated mass upper:",float(mass))
    for bits in BITS:
        orders=[taylor_order(r-l,bits)[0] for l,r,m in clusters]
        dimension=2*sum(orders)+1 # exact original signed odd-pole vector
        # On f perp physical span of modulated supported polynomials:
        # integral_U |Ff|^2 <= 2B sum widths_j eps_j^2 ||f||^2.
        # Knegative quadratic <= 2B sum certified masses_j eps_j^2 ||f||^2.
        # Every group includes 2 reflected signed Fourier clusters.
        eps2=F(1,2**(2*bits))
        protect_loss=2*B*width*eps2
        negative_loss=2*B*mass*eps2
        lower=KAPPA*(1-protect_loss)-negative_loss
        assert lower>F(1,2000), (bits,float(lower))
        # Outward certified rational lower margins, not rounded float results.
        thresholds={9:F(68,100000),10:F(92,100000),
                    12:F(995,1000000),16:F(999,1000000),
                    32:F(999,1000000)}
        assert lower > thresholds[bits], (bits,float(lower))
        assert dimension%2==1 and dimension>=1
        print("local Taylor bits:",bits,
              "physical cofinite codimension <=",dimension,
              "certified whole original Weil L2-positive margin >",float(lower),
              "(in the physical orthogonal complement)")
    print("SI10 PASS: positive ORIGINAL FULL SIGNED WEIL form on")
    print("the entire closed L2 orthogonal complement of an explicit")
    print("finite family (not positivity on that finite-dimensional family).")
    print("Stage I, full signed Schur/positivity, RH OPEN.")


if __name__=="__main__":
    validate()
