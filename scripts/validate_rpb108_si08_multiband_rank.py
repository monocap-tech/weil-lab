#!/usr/bin/env python3
"""SI08: exact multi-band, physically supported, operator-norm rank certificates.

Reuse SI06's verified signed-original prime enclosures and SI07's validated
digamma lower bound, to rebuild the *entire* unresolved-frequency cover.
Analytic Fourier/Taylor/projection proof is in the SI08 note.
No floating point arithmetic is used to certify any interval or rank.
"""
from fractions import Fraction as F
from math import factorial
from validate_rpb108_si06_negative_band import B, prime_interval
from validate_rpb108_si07_negative_support_cover import (
    END, DEPTH, M, DEN, arch_lower_cell, ceil_fraction
)

# A single positive-frequency cluster [a,b] corresponds to both +/- clusters.
# The zero-extended physical basis vectors are e^(2pi*i*center*x) * x**k on I.
PI_UP = F(22, 7)
TARGET_BITS = (40, 64, 80, 96)


def cover():
    unresolved = []
    good = 0

    def visit(left, right, arch, depth):
        nonlocal good
        center = (left + right) / 2
        lower = arch + prime_interval(center)[0] - M*(right-left)/2
        if lower > 0:
            good += 1
            return
        if depth < DEPTH:
            visit(left, center, arch, depth+1)
            visit(center, right, arch, depth+1)
            return
        height = F(ceil_fraction((-lower)*DEN), DEN)
        assert height >= -lower >= 0
        unresolved.append((left, right, height))

    for j in range(END):
        arch = arch_lower_cell(j)
        visit(F(j), F(j+1), arch, 0)

    unresolved.sort(key=lambda v: v[0])
    assert len(unresolved) == 972 and good == 9261
    assert sum((r-l for l, r, h in unresolved), F(0)) == F(243,16)
    total_mass_upper = 2*sum((h*(r-l) for l, r, h in unresolved), F(0))
    assert total_mass_upper < 38

    clusters = []
    for left, right, height in unresolved:
        if clusters and left == clusters[-1][1]:
            clusters[-1] = (clusters[-1][0], right)
        else:
            clusters.append((left, right))
    assert len(clusters) == 107
    assert sum((r-l for l,r in clusters), F(0)) == F(243,16)
    return clusters, total_mass_upper


def taylor_order(width, bits):
    """Smallest p whose real-phase Taylor remainder is <2^-bits.

    Real phase integral remainder |exp(i*t)-sum(k=0..p-1)(it)^k/k!|
    <= |t|^p/p!. For |xi-center|<=width/2 and |x|<=B,
    |t|<=pi*B*width <= (22/7)*B*width.
    """
    radius = PI_UP*B*width
    bound = F(1)
    for p in range(1, 256):
        bound *= radius / p
        if bound < F(1, 2**bits):
            return p, bound
    raise AssertionError("Taylor budget does not close")


def validate():
    clusters, mass = cover()
    # Full source K_- has its negative-frequency multiplier supported in
    # the union of clusters and their reflected counterparts; integral
    # of m_- is bounded by the SI07 outward rational height budget.
    # Trace = 2B*mass, strictly less than 83 (SI07).
    assert 2*B*mass < 83
    print("SI08 PASS: all intervals and multi-band Taylor error paid")
    print("certified positive-frequency clusters:",len(clusters))
    print("full frequency negative-support cover measure:",
          float(2*sum((r-l for l,r in clusters),F(0))))
    print("certified original m_- integrated mass bound:",float(mass))
    print("certified tr K_- upper:",float(2*B*mass))
    for bits in TARGET_BITS:
        order_pairs=[taylor_order(right-left,bits) for left,right in clusters]
        max_degree=max(p for p,_ in order_pairs)
        # Include BOTH +/- centers (even Fourier multiplier) and retain
        # the original negative odd pole function sinh(x/2) exactly.
        dimension=2*sum(p for p,_ in order_pairs)+1
        eps=F(1,2**bits)
        # || |u><u|-|Pu><Pu| || <= (||u||+||Pu||)||u-Pu||.
        # ||u||=sqrt(2B), ||u-Pu|| <=sqrt(2B)*eps.
        # Consequently ||K_- - Pi_V K_- Pi_V||<=4B*mass*eps.
        err_factor=4*B*mass
        assert err_factor < 2**8
        assert err_factor*eps < F(1,2**(bits-8))
        print("Taylor bits:",bits,
              "rank incl exact odd pole:",dimension,
              "maximum local order:",max_degree,
              "physical operator error <",f"2^-{bits-8}")
        if bits==80:
            assert dimension < 9473, f"SI08 not better than SI06: {dimension}"
    print("SI08: rank/error tradeoff is not full Weil positivity or a 301-rank theorem")


if __name__ == "__main__":
    validate()
