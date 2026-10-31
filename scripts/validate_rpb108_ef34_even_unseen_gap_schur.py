#!/usr/bin/env python3
"""EF34: original even SOURCE-TO-UNOBSERVED GAP signed Schur interface.

Exact original EF18 arithmetic first-source jump x0=B-ln2 is in an
open physical gap of ALL EF28 471 C5 bell pairs. In that same gap the
original signed action of EVERY EF33 bell combination is locally smooth:
- its quarter-digamma action is pseudolocal, as all bells vanish there;
- each seven-prime translated bell is analytic away from its endpoints,
  which are excluded with original certified rational log intervals.

Original physical gradient of the first SI10 source has an isolated
jump J<-1/4 at x0. Therefore for any scalar a the distribution
g_e-a*g_bell has the SAME jump at x0.

Original even monic differential annihilator
L(D)=(D²-1/4)*product_j(D²+(2*pi*c_j)²)^p_j
(order 940) maps even C_c^infty test bumps supported in that gap to
genuine SOURCE-AND-POLE-NEUTRAL even cofinite tests, L2-orthogonal to
the EF28 bell span. Its pairing with g_e-a*g_bell is nonzero for
some such test due to noncancellable delta^(939). Analytic
pseudolocality/source form core is documented, not proved by CI.

Consequently the *original* omitted energy-dual Schur remainder
eta=|| b|_{(span{f*})^{perp_q} in F} ||^2 is STRICTLY POSITIVE,
where F=V469^perp and f* is EF31's source/pole-neutral bell.
Identity S_{e|F}=S_{e|f*}-eta, eta>0, value UNKNOWN.
This is not a negative witness or RH counterexample.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from validate_rpb108_si06_negative_band import B,ACTIVE,ln_bounds
from validate_rpb108_ef18_original_even_signed_shift_jump import source_and_jump
from validate_rpb108_ef19_original_even_annihilator import (
    source_contract,annihilator_algebra
)
from validate_rpb108_ef28_pole_neutral_moment_kernel import (
    original_source_and_geometry,COUNT,R,GRID
)

ROOT=Path(__file__).resolve().parents[1]
DEGREE=940
ALPHA_JET=939

def separate_interval(target_lo,target_hi,edge_lo,edge_hi):
    """Strict rational minimum distance of disjoint closed intervals."""
    assert target_lo<=target_hi and edge_lo<=edge_hi
    if target_lo>edge_hi: return target_lo-edge_hi
    if edge_lo>target_hi: return edge_lo-target_hi
    raise AssertionError(("unresolved original arithmetic/bell endpoint collision",
                          str(target_lo),str(target_hi),
                          str(edge_lo),str(edge_hi)))

def original_gap_geometry():
    r=source_and_jump()
    xlo,xhi=r['xlo'],r['xhi']
    assert r['jump_hi']<-F(1,4)
    assert COUNT==471 and GRID==F(1,512) and R==F(1,8192)
    left=F(208,512)+R
    right=F(209,512)-R
    assert left<xlo<xhi<right and right-left>F(1,1000)
    # Even reflection puts the second gap at negative x0.
    assert -right<-xhi<-xlo<-left
    baseline=min(xlo-left,right-xhi)

    # Entire original seven-prime translations of all true C5 bell
    # boundaries (four per bell pair, both +/-shift) do NOT have an
    # endpoint at the authentic source jump x0.
    gaps=[baseline]
    nearest=None
    for n in sorted(ACTIVE):
        lo,hi=ln_bounds(n,terms=180)
        assert 0<lo<=hi
        for j in range(1,472):
            x=F(j,512)
            for sign in (-1,1):
                c=sign*x
                for e in (-1,1):
                    endpoint=c+e*R
                    for shift in (-1,1):
                        a,b=(endpoint+lo,endpoint+hi) if shift==1 else (
                            endpoint-hi,endpoint-lo)
                        d=separate_interval(xlo,xhi,a,b)
                        gaps.append(d)
                        if nearest is None or d<nearest[0]:
                            nearest=(d,n,j,sign,e,shift)
    # Also isolate x0 from all OTHER source arithmetic jumps.
    for n in sorted(ACTIVE):
        lo,hi=ln_bounds(n,terms=180)
        for kind,a,b in (
            ("right",B-hi,B-lo),("left",-B+lo,-B+hi)):
            if n==2 and kind=="right":
                assert a<=xhi and xlo<=b
                continue
            gaps.append(separate_interval(xlo,xhi,a,b))
    margin=min(gaps)
    assert margin>0
    # Each original jump reflection is separated similarly by evenness.
    eps=min(margin,F(1,100))/4
    assert eps>0 and eps<baseline/2
    print("EF34 ORIGINAL first source jump enclosed",float(xlo),float(xhi),
          "strict physical EF28 support gap",float(left),float(right),flush=True)
    print("EF34 genuine arithmetic jump J interval",
          float(r['jump_lo']),float(r['jump_hi']),
          "other translated C5 endpoints scanned",
          7*471*2*2*2,"minimum outward separation",
          float(margin),"safe even test radius <=",float(eps),
          "closest candidate",nearest,flush=True)
    return r,margin,eps

def true_original_annihilator():
    centers,orders=source_contract()
    native,orders2,xs=original_source_and_geometry()
    assert centers==native and orders==orders2
    assert xs==[F(j,512) for j in range(1,472)]
    n,degree=annihilator_algebra(orders)
    assert n==469 and degree==938
    assert degree+2==DEGREE
    assert DEGREE-1==ALPHA_JET
    # Product factors kill every original even SI10 polynomial sine/
    # cosine source of degree <p_j (EF19); the additional factor
    # D²-1/4 kills the genuine cosh pole exactly.
    assert F(1,2)**2-F(1,4)==0
    # Even monic polynomial in D ensures parity and selfadjointness.
    # A nonzero C_c∞ even bump in the strict x0 gap survives L(D)
    # and remains compact in that gap, hence L2 orthogonal to all bells.
    return degree+2,2*sum(orders)

def exact_residual_schur_toy():
    """Toy only: same finite positive 2D / cofinite floor; opposite full signs.

    NOT the Weil operator, does NOT certify actual eta; illustrates why
    a positive EF33 2D block cannot determine an *unmeasured* eta.
    """
    A=F(31,1000); qf=F(1); b=F(1,100)
    S2=A-b*b/qf
    assert S2>F(1,500)
    qy=F(1)
    outcomes=[]
    for cross in (F(1,100),F(1,5)):
        full=S2-cross*cross/qy
        outcomes.append(full)
    assert outcomes[0]>0 and outcomes[1]<0
    # Both scalar complement blocks (f,y) are positive definite,
    # including original inherited mu=17/25000 as a weaker floor.
    assert qf>F(17,25000) and qy>F(17,25000)
    return S2,outcomes

def validate():
    manifest=json.loads((ROOT/'research/obligations.json').read_text())
    assert manifest['active_obligation']=='W-EVEN-FORM'
    byid={x['id']:x for x in manifest['obligations']}
    assert byid['W-EVEN-FORM']['status']=='open'
    assert byid['W-ODD-NEG']['status']=='open'
    jump,margin,eps=original_gap_geometry()
    degree,original_n=true_original_annihilator()
    S2,outcomes=exact_residual_schur_toy()
    assert degree==940 and original_n==938
    print('EF34 ORIGINAL source+positive pole annihilator L(D) degree',
          degree,'leaves a nonzero signed source jump distribution'
          ' of order delta^(939) after differentiation,'
          ' conditional on arch pseudolocality and core/domain.',flush=True)
    print('EF34 EXACT ORIGINAL information interface:'
          ' W_even restricted e/f* Schur S2>1/500 (EF33 accepted);'
          ' full source-vs-cofinite scalar S_e|F=S2-eta,'
          ' with eta>0 by original gap-jump noncancellation;'
          ' no certified eta numeric bound.',flush=True)
    print('EF34 separate EXACT rational abstract models preserve'
          ' positive restricted S2:',float(S2),'but full signs',
          [float(x) for x in outcomes],
          'toy ONLY, no original negative witness.',flush=True)
    print('EF34 METHOD INFORMATION STOP: EF33 bell-only source data'
          ' cannot substitute for original signed residual on the'
          ' remaining q-orthogonal infinite cofinite sector.'
          ' Original complete 469D Schur and W-EVEN-FORM remain OPEN.',
          flush=True)

if __name__=='__main__':
    validate()
