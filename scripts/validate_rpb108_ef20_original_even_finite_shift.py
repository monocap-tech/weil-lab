#!/usr/bin/env python3
"""EF20: exact bounded native 469-even-source FIR annihilator.
Scoped algebra; no signed numerator, energy, Schur or RH certified.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
from validate_rpb108_si10_complement_positivity import protected_inner_cover, protected_outer_band, KAPPA, B
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import WEIGHTS, SHIFTS, ACTIVE
from validate_rpb108_si14_odd_multiband_nogo import cos_sin_pi_multiple

ROOT=Path(__file__).resolve().parents[1]
H=F(1,2048)
R=F(1,100)
N=469

def native():
    outer,lower=protected_outer_band()
    clusters,width,mass,leaves,accepted=protected_inner_cover()
    assert outer==2535 and lower>KAPPA
    assert (len(clusters),leaves,accepted)==(107,973,9261)
    assert width==F(973,32)
    c=[(l+r)/2 for l,r,_ in clusters]
    p=[taylor_order(r-l,9)[0] for l,r,_ in clusters]
    assert len(set(c))==107 and all(F(0)<x<F(896) for x in c)
    assert sum(p)==N and c[0]==F(37,64)
    return c,p

def degree_drop(poly,z,h):
    """Specialize universal identity z[P(x+h)-P(x)] +
    z^-1[P(x-h)-P(x)], lowering polynomial degree by >=1.
    z=2 is algebraic TEST only; actual z_j=exp(i*2*pi*c_j*h).
    """
    out={}
    for k,v in poly.items():
        for j in range(k):
            term=v*comb(k,j)*h**(k-j)*(z+(-1)**(k-j)/z)
            out[j]=out.get(j,F(0))+term
    return {j:v for j,v in out.items() if v}

def annihilation(orders):
    for p in orders:
        assert p>=1
        for d in (0,p-1):
            poly={d:F(1)}
            for _ in range(p):
                poly=degree_drop(poly,F(2),H)
            assert not poly
    assert sum(orders)==469
    return 2*sum(orders)

def geometry_and_jump(centers):
    # Original signed source jump x0=B-ln2 and its parity reflection.
    ll,lh=SHIFTS[2]
    xlo,xhi=B-lh,B-ll
    assert 0<xlo<xhi<B
    spread=N*H
    assert spread==F(469,2048)
    assert xlo>R+spread and xhi+R+spread<B
    # Distinct signed frequency roots e^(+/-2*pi*i*c_j*h):
    # every c_j*h lies strictly inside (0, 1/2).
    assert 2*max(centers)*H<1
    phase=2*B*centers[0]
    assert phase==F(407,320)
    lo,hi=cos_sin_pi_multiple(phase)[1]
    assert hi<0
    wlo,whi=WEIGHTS[2]
    vals=[w*v for w in (wlo,whi) for v in (lo,hi)]
    assert max(vals)<-F(1,4)
    assert set(ACTIVE)=={2,3,4,5,7,8,9}
    return xlo,xhi,spread,min(vals),max(vals)

def fixed_step_original_mixed_jump():
    """The original n=2 arithmetic jump survives at fixed h.

    The FIR extreme T_(-469h) coefficient is +1 and transports
    the true signed jump J to x*=B-ln2+469h. Exact rational
    log/physical edge intervals rule out ALL other collisions.
    Original archimedean pseudolocality remains an analytic premise.
    """
    ll,lh=SHIFTS[2]
    star=(B-lh+N*H,B-ll+N*H)
    assert star[0]<star[1] and star[1]+R+N*H<B
    def separation(a,b):
        if a[1]<b[0]:return b[0]-a[1]
        if b[1]<a[0]:return a[0]-b[1]
        return F(0)
    margin=None
    checked=0
    for k in range(-N,N+1):
        delta=k*H
        for n in sorted(ACTIVE):
            lo,hi=SHIFTS[n]
            right=(B-hi-delta,B-lo-delta)
            if n==2 and k==-N:assert right==star
            else:
                d=separation(star,right)
                assert d>0,("right-edge collision",n,k)
                margin=d if margin is None else min(margin,d)
                checked+=1
            left=(-B+lo-delta,-B+hi-delta)
            d=separation(star,left)
            assert d>0,("left-edge collision",n,k)
            margin=min(margin,d)
            checked+=1
        for endpoint in (B,-B):
            d=separation(star,(endpoint-delta,endpoint-delta))
            assert d>0,("cutoff collision",k,endpoint)
            margin=min(margin,d)
            checked+=1
    assert margin is not None and margin>0
    assert checked==(2*len(ACTIVE)+2)*(2*N+1)-1
    return star,margin,checked


def run():
    data=json.loads((ROOT/"research/obligations.json").read_text())
    o={x["id"]:x for x in data["obligations"]}
    assert data["active_obligation"]=="W-EVEN-FORM"
    assert all(o[x]["status"]=="open" for x in ("W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert "EF20" in o["W-EVEN-FORM"]["evidence"]
    c,p=native()
    multiplicity=annihilation(p)
    assert multiplicity==938
    # Sharp universal bilateral shift support radius: if support is
    # in [-r,r], its Laurent symbol times z^r has degree <=2r.
    # The 107 distinct conjugate root pairs have 938 total multiplicity.
    assert 2*(N-1)<multiplicity==2*N
    xl,xr,s,jlo,jhi=geometry_and_jump(c)
    star,margin,checked=fixed_step_original_mixed_jump()
    print("EF20 original SI10 native positive centers:",len(c),
          "orders:",sum(p),"real frequency root multiplicity:",multiplicity,flush=True)
    print("EF20 fixed exact h:",H,"minimal bilateral radius:",N,
          "physical spread:",float(s),flush=True)
    print("EF20 genuine physical jump neighborhood:",float(xl),float(xr),
          "original signed jump:",float(jlo),float(jhi),flush=True)
    print("EF20 SOURCE ALGEBRA PASS: L_j=T_h+T_-h-2*cos(2*pi*h*c_j)",
          "drops polynomial degree, so product L_j^pj kills all 469",
          "actual even source columns. On interior compact even bumps",
          "the selfadjoint finite shift gives EXACT F469 test without",
          "469D Gram inverse; ||filter||<=4^469.",flush=True)
    print("EF20 SHARP UNIVERSAL FIR ORDER: total distinct root multiplicity",
          "938; no smaller bilateral radius than 469 at this step.",flush=True)
    print("EF20 FIXED-h original signed mixed jump x*:",float(star[0]),float(star[1]),
          "rigorous source/boundary separation:",float(margin),
          "checked:",checked,flush=True)
    print("EF20 CONDITIONAL ORIGINAL MIXED NONZERO:",
          "the true FIR-filtered signed physical gradient retains",
          "isolated J<-1/4 at x*; for some even compact smooth psi",
          "we have q0(e,F_h psi)!=0 at FIXED h.",
          "No explicit signed numerator or normalized Schur.",flush=True)
    print("EF20 OPEN: finite signed mixed original q0(e,f_h),",
          "full q0(f_h,f_h), normalized inverse response, corrected",
          "Schur PSD, analytic form attachment, even/odd/whole Weil, RH.",flush=True)

if __name__=="__main__":
    run()
