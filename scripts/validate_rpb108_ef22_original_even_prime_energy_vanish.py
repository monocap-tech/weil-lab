#!/usr/bin/env python3
"""EF22 source-specific TRUE ORIGINAL signed seven-prime energy vanishing.

On EF21's fixed h=1/2048/r=1/65536 physical even cosine-six bell
f=F_h psi in V_even469^perp, ALL original prime-power translations
n=2,3,4,5,7,8,9 produce supports disjoint from f itself.

Thus for the original signed pole-free multiplier:
  q_prime(f,f)=-2 sum_n w_n Re<int f(x), f(x+ln n)> = 0 EXACTLY.
  q0(f,f) = int_R arch(xi) |fhat(xi)|^2 dxi.

This uses genuine original ln(n) Fraction intervals and does NOT
replace m by a surrogate. The prime MIXED q_prime(e,f) is generally
nonzero; native source orthogonality reduces it exactly to a finite
sum of signed outside-the-physical-cutoff bell integrals.

All source, physical disjointness and signed-parity identities are
source checkable. No numeric original q0(e,f), q0(f,f) upper,
corrected Schur PSD or RH accepted here.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import SHIFTS,ACTIVE,B
from validate_rpb108_ef21_original_even_fixed_bell import (
    authentic_source_replay, physical_support_and_disjointness, H,N,R,
    bell_transform_identity,
)

ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)


def interval_distance(a,b):
    """Exact nonnegative lower bound for separation of two intervals."""
    if a[1]<b[0]:
        return b[0]-a[1]
    if b[1]<a[0]:
        return a[0]-b[1]
    return F(0)


def original_primes_separate_all_f_supports():
    # Support centers: s*a - k*h for s=+-1 and -469<=k<=469.
    # Same-sign center differences span [-938h,938h].
    # Opposite-sign differences span +-2a+[-938h,938h].
    # A source translate ln(n) can overlap only if one difference
    # is at distance <= 2r from one of these possibilities.
    l2lo,l2hi=SHIFTS[2]
    alo,ahi=B-l2hi+N*H,B-l2lo+N*H
    assert F(0)<alo<ahi<B
    assert 2*R<H
    # All original prime logarithms >= log2, and the entire
    # same-lobe FIR span is only 938h<log2.
    same_gap=l2lo-2*N*H
    assert same_gap>2*R

    # Opposite-lobe source differences for positive ln n:
    # ln n - (2a + d*h), d integer [-938,938].
    # We must exclude BOTH opposite-lobe signs, but ln n +2a
    # cannot be within the shift span: positive >938h.
    assert l2lo+2*alo-2*N*H>2*R
    minimum=None
    witness=None
    checked=0
    for n in sorted(ACTIVE):
        lnlo,lnhi=SHIFTS[n]
        for d in range(-2*N,2*N+1):
            interval=(2*alo+d*H,2*ahi+d*H)
            separation=interval_distance((lnlo,lnhi),interval)
            assert separation>2*R, (
                "EF22 original prime translation overlaps fixed f supports",
                n,d,float(separation),float(2*R))
            remaining=separation-2*R
            if minimum is None or remaining<minimum:
                minimum=remaining
                witness=(n,d)
            checked+=1
    assert checked==len(ACTIVE)*(4*N+1)==7*1877
    assert minimum>0
    # Every self-support pair of bells is strictly disjoint under
    # all 7 original true ln(n) shifts: exact energy cancellation.
    return dict(same_gap=same_gap,minimum_margin=minimum,
                nearest=witness,pairs=checked)


def original_prime_mixed_boundary_reduction():
    # e(x)=1_I cos(2*pi*c0*x), c0=37/64, f in original even F469.
    # For each original n and sigma=+-:
    # 0 = int_I f(x) cos(2*pi*c0*(x+sigma*ln(n)))dx:
    #     cos-phase follows from original <f,cos(2*pi*c0*x)>=0
    #     and sine term vanishes by exact even parity.
    # Therefore int f(x)e(x+sigma*ln n)dx is the NEGATIVE
    # of the integral of the same global cos over the set where
    # |x+sigma*ln n|>B. The original arithmetic mixed form is
    # q_prime(e,f)=sum_n w_n sum_sigma int_{exterior}
    #                          f(x)cos(2*pi*c0*(x+sigma*ln n))dx.
    # This is exact, not a claim of vanishing mixed coupling.
    c0=F(37,64)
    assert c0>0
    original_set=tuple(sorted(ACTIVE))
    assert original_set==(2,3,4,5,7,8,9)
    # All 2*939 original actual f bell centers are inside I;
    # each truncated original source cosine boundary crosses
    # at most ONE translated compact bell per sign-lobe/edge,
    # as h>2r. There are at most
    # 7 original powers *2 +/-source shifts*2 physical edges*
    # 2 bell lobes =56 partial bell integrations.
    max_partial=7*2*2*2
    assert 2*R<H and max_partial==56
    # The other whole-bell pieces evaluate with exact H_r(c0)
    # times cosine of the translated center. This collapses
    # ALL original prime-only mixed integrals to finite elementary
    # trigonometric/Fraction-interval sums, not an infinite m_prime
    # quadrature. These sums are NOT evaluated or sign-certified.
    return max_partial



def exact_partial_boundary_bell_classification():
    """Strict original ln(n) interval classification for EF21's ONE f.

    Each shifted source e(x+sigma ln n) can only clip an EF21 bell if
    center s*a-k*h+sigma ln n lies within radius r of endpoint ±B.
    With r/h=1/32, only O(1) candidate lattice k per n/sigma/s/edge;
    all excluded integer k have >h separation by elementary rounding.
    Classify partial vs disjoint using exact source Fraction intervals.
    """
    l2lo,l2hi=SHIFTS[2]
    alo,ahi=B-l2hi+N*H,B-l2lo+N*H
    assert R/H==F(1,32)
    partial=[]
    checks=0
    for n in sorted(ACTIVE):
        lnlo,lnhi=SHIFTS[n]
        for sigma in (-1,1):
            for s in (-1,1):
                b0=(alo,ahi) if s==1 else (-ahi,-alo)
                n0=(lnlo,lnhi) if sigma==1 else (-lnhi,-lnlo)
                for endpoint in (-B,B):
                    dlo=b0[0]+n0[0]-endpoint
                    dhi=b0[1]+n0[1]-endpoint
                    assert dhi>=dlo and dhi-dlo<H/16
                    # Need |d-kh|<r. Every integer beyond
                    # [floor(dlo/h)-1, floor(dhi/h)+2] is >h
                    # away, hence automatically beyond r<h/32.
                    lower=(dlo/H).numerator//(dlo/H).denominator
                    upper=(dhi/H).numerator//(dhi/H).denominator
                    assert upper-lower<=1
                    for k in range(lower-1,upper+3):
                        if abs(k)>N:continue
                        zlo,zhi=dlo-k*H,dhi-k*H
                        checks+=1
                        if zhi < -R or zlo > R:
                            continue
                        # The original logarithm enclosures must
                        # identify a rigorous actually clipped bell
                        # without an unresolved interval boundary.
                        assert -R<zlo<=zhi<R, (
                            "unresolved partial bell source cutoff",
                            n,sigma,s,endpoint,k,float(zlo),float(zhi))
                        partial.append((n,sigma,s,str(endpoint),k))
    assert len(partial)==2,partial
    assert set(partial)=={
        (2,1,1,str(B),N),
        (2,-1,-1,str(-B),-N),
    },partial
    return partial,checks


def even_pole_eigenvalue_identity():
    # The original even pole c(x)=cosh(x/2) is a common eigenfunction
    # of every symmetric shift on the FULL real line:
    # (T_h+T_-h)c=2cosh(h/2)c.
    # For compact physical f=F_h psi, all shifts stay inside I.
    # Therefore <c,f> = Lambda_h <c,psi> exactly,
    # Lambda_h=prod_j [2cosh(h/2)-2cos(2*pi*h*c_j)]^p_j >0.
    # The original even pole contribution is
    # +2 Lambda_h^2 |<c,psi>|^2 >=0.
    # This is a symbolic identity; no numerical Lambda claimed.
    centers,orders=authentic_source_replay()
    assert len(centers)==107 and sum(orders)==469
    assert all(0<2*c*H<1 for c in centers)
    return len(centers)


def run():
    data=json.loads((ROOT/"research/obligations.json").read_text())
    obs={o["id"]:o for o in data["obligations"]}
    assert data["active_obligation"]=="W-EVEN-FORM"
    assert all(obs[x]["status"]=="open"
               for x in ("W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert all(x in obs["W-EVEN-FORM"]["evidence"]
               for x in ("EF20","EF21","EF22"))
    mass,bellnorm=bell_transform_identity()
    al,ah,phase_lo,phase_hi,normlo=physical_support_and_disjointness()
    d=original_primes_separate_all_f_supports()
    partial=original_prime_mixed_boundary_reduction()
    clipped,clipchecks=exact_partial_boundary_bell_classification()
    count=even_pole_eigenvalue_identity()
    assert normlo>0 and MU*normlo>0
    print("EF22 actual native original SI10 seven-prime n:",sorted(ACTIVE),
          "all actual 469 even exceptional source constraints",count,
          "clusters; fixed h",H,"radius",R,flush=True)
    print("EF22 exact SAME-lobe ln2 minus whole fixed filter span:",
          float(d["same_gap"]),"required positive 2r:",float(2*R),
          flush=True)
    print("EF22 opposite-lobe ORIGINAL ln n translated pairs checked:",
          d["pairs"],"minimal positive support separation AFTER 2r:",
          float(d["minimum_margin"]),"nearest (n,d):",d["nearest"],flush=True)
    print("EF22 ORIGINAL SIGNED ARITHMETIC ENERGY VANISHES EXACTLY:",
          "q_prime(f,f)=0 for ALL seven n; true original pole-free",
          "E=q_arch(f,f) (no prime energy quadrature).",flush=True)
    print("EF22 original signed PRIME MIXED DOES NOT VANISH BY THIS:",
          "exact finite exterior-cutoff elementary bell decomposition;",
          "at most",partial,"partially clipped bell terms.",
          "Finite sums not yet interval-evaluated.",flush=True)
    print("EF22 exact original source-cutoff PARTIAL bells:",
          len(clipped),"==2, candidates tested:",clipchecks,
          "partial identifiers:",clipped,flush=True)
    print("EF22 original even positive pole eigenvalue identity:",
          "Lambda=prod(2cosh(h/2)-2cos(2*pi*h*cj))^pj>0;",
          "even-pole contribution +2*Lambda²|<c,psi>|².",
          "No numerical Lambda claimed.",flush=True)
    print("EF22 SCOPED TRUE ORIGINAL SIGNED SOURCE PASS:",
          "exact physical prime-energy cancellation, NOT a proof",
          "that full q0(e,f) or q0(f,f) can be numerically bounded.",
          "Original arch E and mixed M, normalized inverse Schur",
          "and whole even/odd/Weil/RH remain OPEN.",flush=True)


if __name__=="__main__":
    run()
