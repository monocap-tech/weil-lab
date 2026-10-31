#!/usr/bin/env python3
"""EF19 original signed even cofinite test family without 469D Gram inversion.

For the ACTUAL SI10 b9 469-dimensional even carrier V, construct the
constant-coefficient formal annihilator
    P(D)=prod_j (D^2+(2*pi*c_j)^2)^{p_j}, degree 938.
Then f_epsilon=P(D) Phi_epsilon for smooth real even compactly
supported Phi_epsilon inside (-B,B) lies EXACTLY in V^perp.

Apply to the genuine original signed source gradient
g=P_I m(D)e (e=first actual even source). Its n=2 arithmetic jump
J!=0 at x0=B-ln2 implies P(D)g contains J delta_x0^(937)
and a mirrored even counterpart, giving an explicit family with
lim_epsilon->0 q0(e,f_epsilon)=-J>1/4.

This is a rigorous *existential unnormalized* mixed lower, dependent
on the separately stated standard pseudolocality and original domain
facts. No finite epsilon or normalized original Schur bound is
certified. The exact rational script checks physical source pins,
translation isolation and formal annihilator/JET algebra; it DOES
NOT run order-938 differentiation or certify distributional
pseudolocality analytically.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover, protected_outer_band, KAPPA, B,
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import ACTIVE, SHIFTS
from validate_rpb108_ef18_original_even_signed_shift_jump import source_and_jump

ROOT=Path(__file__).resolve().parents[1]
ORDER_BITS=9
RADIUS=F(1,100)
DEGREE=938
JET_ORDER=937


def source_contract():
    outer,low=protected_outer_band()
    clusters,W,M,leaves,accepted=protected_inner_cover()
    assert outer==2535 and low>KAPPA
    assert (len(clusters),leaves,accepted)==(107,973,9261)
    assert W==F(973,32)
    centers=[(l+r)/2 for l,r,_ in clusters]
    orders=[taylor_order(r-l,ORDER_BITS)[0] for l,r,_ in clusters]
    assert len(centers)==107 and all(c>0 for c in centers)
    assert len(set(centers))==107
    assert sum(orders)==469
    assert 2*sum(orders)==DEGREE
    assert (centers[0],sum(orders))==(F(37,64),469)
    return centers,orders


def gaussian_add(a,b):
    return (a[0]+b[0],a[1]+b[1])


def gaussian_iw(a,w):
    return (-w*a[1],w*a[0])


def polynomial_conjugate_operator(poly,w):
    """Apply (D^2+2*i*w*D) to polynomial in x, exact Z[i].
    This is e^(-i*w*x)(D^2+w^2)e^(i*w*x).
    Each application drops polynomial degree by >=1 regardless of w.
    """
    out={}
    for power,z in poly.items():
        if power>=2:
            a=(power*(power-1)*z[0], power*(power-1)*z[1])
            out[power-2]=gaussian_add(out.get(power-2,(0,0)),a)
        if power>=1:
            a=gaussian_iw(z,2*w*power)
            out[power-1]=gaussian_add(out.get(power-1,(0,0)),a)
    return {k:v for k,v in out.items() if v!=(0,0)}


def annihilator_algebra(orders):
    # Exact integer-Gaussian symbolic analogue. Every authentic p_j
    # parity source with k<p_j is killed by its own 2nd-order factor
    # to p_j power. The argument is independent of numeric real omega.
    count=0
    for p in orders:
        assert p>=1
        poly={p-1:(1,0)}
        for k in range(p):
            poly=polynomial_conjugate_operator(poly,3)
            count+=1
        assert not poly
    assert count==sum(orders)==469
    # P(D) is even and monic; with 107 signed-frequency squared
    # factors the differential order is precisely 938.
    return count,2*count


def isolate_jump():
    entry=source_and_jump() # original SI10 and all prime-phase checks
    xlo,xhi=entry["xlo"],entry["xhi"]
    assert xlo>RADIUS and B-xhi>RADIUS
    assert xhi-xlo<RADIUS
    # Both +x0/-x0 small supported bumps avoid all other
    # arithmetic-shift endpoints, including mirrored counterparts.
    for n in ACTIVE:
        lnlo,lnhi=SHIFTS[n]
        if n!=2:
            # Different right edges B-ln(n).
            assert (lnlo>SHIFTS[2][1]+RADIUS
                    or lnhi<SHIFTS[2][0]-RADIUS)
        # Different left edges -B+ln(n), including at +/-x0.
        assert (SHIFTS[2][0]+lnlo>2*B+RADIUS
                or SHIFTS[2][1]+lnhi<2*B-RADIUS)
    assert entry["jump_hi"]<-F(1,4)
    # The formal even detector Phi_epsilon=(phi_x0+
    # reflected phi_x0)/2 has derivative-jet:
    # at x0: Phi^(937)=+1/2, at -x0: -1/2;
    # derivatives k<937 vanish at BOTH jump points.
    # Even g has mirror jumps J and -J.
    # Pairing with the highest delta^(937) gives -J exactly,
    # and the smooth remainder is o(1) as epsilon->0.
    limit_lo=-entry["jump_hi"]
    limit_hi=-entry["jump_lo"]
    assert limit_lo>F(1,4)
    return entry,limit_lo,limit_hi


def validate():
    custody=json.loads((ROOT/"research/obligations.json").read_text())
    ob={x["id"]:x for x in custody["obligations"]}
    assert custody["active_obligation"]=="W-EVEN-FORM"
    assert ob["W-EVEN-FORM"]["status"]=="open"
    assert ob["W-ODD-NEG"]["status"]=="open"
    assert ob["W-WHOLE-FORM"]["status"]=="open"
    assert "EF18" in ob["W-EVEN-FORM"]["evidence"]
    assert "EF19" in ob["W-EVEN-FORM"]["evidence"]
    c,p=source_contract()
    n,deg=annihilator_algebra(p)
    source,llo,lhi=isolate_jump()
    print("EF19 native actual SI10 original even carrier:",
          len(c),"clusters",n,"orders; real monic annihilator degree",
          deg,flush=True)
    print("EF19 source pin first:",str(c[0]),"boundary phase",
          str(source["phase"]),"jump x0 enclosure",
          float(source["xlo"]),float(source["xhi"]),flush=True)
    print("EF19 original signed first source jump enclosure:",
          float(source["jump_lo"]),float(source["jump_hi"]),flush=True)
    print("EF19 exact signed mixed detector limit -J enclosure:",
          float(llo),float(lhi),">1/4; hence for some sufficiently"
          " small unspecified epsilon, |q0(e,f_epsilon)|>1/8",
          flush=True)
    print("EF19 SOURCE ALGEBRA PASS (conditional analytic):"
          " even compact source annihilator P(D) of order 938"
          " produces an explicit genuine F469 test family,"
          " avoiding finite 469D Gram inversion. Analytic"
          " pseudolocality and unbounded physical form operator"
          " domain must be separately reviewed. No EXPLICIT epsilon,"
          " certified normalized energy, inverse Riesz response,"
          " original complete signed Schur sign, full even/odd Weil"
          " or RH.",flush=True)


if __name__=="__main__":
    validate()
