#!/usr/bin/env python3
"""IV024: independent exact arithmetic interaction-graph sentry.

This is deliberately a DIFFERENT, independent finite arithmetic
construction from the Lean original Zeta23 source implementation.
It consumes rational physical support cells and independently tests
possible ±log(n) translations, for every active prime POWER n<10.
No reference to a claimed Lean theorem or numerical positive matrix
is used to decide adjacency.

The exact log brackets come from IV015's rational atanh series with
a mathematically bounded nonnegative tail. Comparison is EXACT
fractions. An uncertain (too wide) log bracket FAILS CLOSED: UNKNOWN,
never silently CLEAR.

Predictions:
  * the original NF543 OLD-left/OLD-right n=9 edge survives;
  * all proposed first and second new cell edges are absent;
  * permutation of cell LABELS preserves the canonical edge graph;
  * a counterfeit cell near a log2-translate creates an n=2 edge;
  * the old support plus both new supports has width 17/2000,
    and the COARSE original signed margin 1/16 only when the
    source-specific true old n9 prime allowance transfers.

This is an INDEPENDENT ARITHMETIC GEOMETRY PREFLIGHT, not a Lean
kernel certificate, a spectral operator construction, an equivalence
between projections, global Weil positivity or RH.
"""
import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

from iv015_frozen_collar_exact_log_gap import log_bracket, abs_lower

OUTPUT=Path("iv024-original-prime-interaction-graph-exact-receipt.json")
CUTOFF=10
B=Q(11,10)
SERIES=96

@dataclass(frozen=True)
class Cell:
    label: str
    center: Q
    radius: Q
    def __post_init__(self):
        assert self.radius>0
        assert -B <= self.center-self.radius
        assert self.center+self.radius <= B
    @property
    def left(self):
        return self.center-self.radius
    @property
    def right(self):
        return self.center+self.radius
    @property
    def key(self):
        return (self.center, self.radius)
    @property
    def width(self):
        return 2*self.radius

CELLS=(
    Cell("old_left", -Q(1099,1000),Q(1,1000)),
    Cell("old_right",Q(1099,1000),Q(1,1000)),
    Cell("new_plus",Q(1,5),Q(1,500)),
    Cell("new_minus",-Q(1,5),Q(1,4000)),
)

@lru_cache(maxsize=None)
def rigorous_log(n):
    return log_bracket(n,SERIES)

def frac(x):
    return f"{x.numerator}/{x.denominator}"

def lower6(x):
    """Certified strict under-approx, NEVER rounded upwards."""
    t=10**6
    return Q((x*t).numerator//(x*t).denominator,t)

def is_prime(n):
    if n<2:return False
    d=2
    while d*d<=n:
        if n%d==0:return False
        d+=1
    return True

def is_prime_power(n):
    """Return truth of the exact elementary criterion Λ(n)≠0."""
    if n<2:return False
    for p in range(2,n+1):
        if not is_prime(p):continue
        k=p
        while k<=n:
            if k==n:return True
            k*=p
    return False

def active():
    return tuple(n for n in range(CUTOFF) if is_prime_power(n))

def abs_upper(lo,hi):
    assert lo<=hi
    return max(abs(lo),abs(hi))

def classify(c1,c2,n,sign):
    """A positive or negative TRUE signed log sample is an edge
    iff its entire rigorous rational log interval is inside the
    physical overlap range. If unresolved, output UNKNOWN."""
    assert sign in (-1,1)
    assert n>=2 and is_prime_power(n)
    lo,hi=rigorous_log(n)
    d=c1.center-c2.center
    if sign==1:
        low,high=d+lo,d+hi
    else:
        low,high=d-hi,d-lo
    r=c1.radius+c2.radius
    lower=abs_lower(low,high)-r
    upper=abs_upper(low,high)-r
    if lower>0:return "CLEAR",lower,upper
    if upper<0:return "OVERLAP",lower,upper
    return "UNKNOWN",lower,upper

def build_graph(cells):
    """The directed signed sample graph; canonical keys use actual
    physical center/radius, never arbitrary cell labels."""
    assert len(cells)>=2
    for i,a in enumerate(cells):
        for j,b in enumerate(cells):
            if i>=j:continue
            assert a.right<b.left or b.right<a.left,("overlapping physical cells",a,b)
    edges=[]
    min_clear=None
    uncertain=[]
    input_digest=hashlib.sha256()
    for a in cells:
        for b in cells:
            for n in active():
                for sign in (-1,1):
                    verdict,lower,upper=classify(a,b,n,sign)
                    item=(a.key,b.key,n,sign)
                    input_digest.update(
                        f"{item}:{verdict}:{frac(lower)}:{frac(upper)};".encode()
                    )
                    if verdict=="UNKNOWN":
                        uncertain.append((a.label,b.label,n,sign))
                    elif verdict=="OVERLAP":
                        edges.append((item,a.label,b.label))
                    elif min_clear is None or lower<min_clear:
                        min_clear=lower
    assert not uncertain,("uncertified original prime overlap classification",uncertain)
    return edges,min_clear,input_digest.hexdigest()

def canonical_edges(edges):
    return frozenset(e[0] for e in edges)

def source_signed_margin(cells):
    width=sum((c.width for c in cells),Q(0))
    # Genuine signed Gamma/two original poles/n9 bound:
    # [11/10 -(67/10)*10*m] - 8*m - 2/5 = 7/10 -75*m
    gamma=Q(11,10)-Q(67,10)*10*width
    poles=8*width
    prime=Q(2,5)
    return width,gamma,poles,prime,gamma-poles-prime

def preflight():
    assert active()==(2,3,4,5,7,8,9)
    assert not is_prime_power(6)
    lo10,hi10=rigorous_log(10)
    assert lo10>2*B, "Actual original n>=10 source cutoff unverified"

    edges,min_clear,digest=build_graph(CELLS)
    assert len(edges)==2,("Expected historical n=9 only",edges)
    for key,left,right in edges:
        a,b,n,sign=key
        assert n==9
        assert {left,right}=={"old_left","old_right"}
        assert sign in (-1,1)
    assert set((x[1],x[2]) for x in edges)=={
        ("old_left","old_right"),("old_right","old_left")
    }
    assert min_clear>Q(0)
    width,gamma,poles,prime,margin=source_signed_margin(CELLS)
    assert (width,gamma,poles,prime,margin)==(
        Q(17,2000),Q(1061,2000),Q(17,250),Q(2,5),Q(1,16)
    )

    # PHYSICAL graph is invariant under permutations of index labels
    # (a mere representation change). It is NOT invariant under moving
    # centers or widening radii; those change the actual source set.
    for ordered in (CELLS[::-1],(CELLS[2],CELLS[0],CELLS[3],CELLS[1])):
        e,mm,_=build_graph(ordered)
        assert canonical_edges(e)==canonical_edges(edges)
        assert mm==min_clear
        assert source_signed_margin(ordered)==(width,gamma,poles,prime,margin)

    # Exactly zero new edges for the selected second cell does NOT
    # mean zero original primes: n=9 old-old edge remains.
    old_only,_,_=build_graph(CELLS[:2])
    assert len(old_only)==2

    # Negative control: put an alternative new cell a rational 693/1000
    # beyond the +1/5 first-new center. A real prime n=2 overlap MUST
    # be detected; hence universal prime-invariance is false.
    counterfeit=Cell("counterfeit_log2",Q(1,5)+Q(693,1000),Q(1,4000))
    fake_cells=CELLS[:3]+(counterfeit,)
    fake_edges,_,_=build_graph(fake_cells)
    assert any(
        n==2 and ("counterfeit_log2" in (left,right))
        for ((_,_,n,_),left,right) in fake_edges
    ),"The original true prime2 shifted-collision negative control failed"

    # Changing ONLY measure can exhaust the sufficient analytic
    # margin while the physical prime graph can remain unchanged.
    widened=CELLS[:3]+(Cell("new_minus_wide", -Q(1,5),Q(1,1000)),)
    wide_edges,_,_=build_graph(widened)
    assert len(wide_edges)==2
    assert source_signed_margin(widened)[-1]<0
    assert margin>0

    receipt={
        "schema":"IV024-finite-original-physical-prime-power-graph-exact-Fraction-v1",
        "original_source_radius":frac(B),
        "original_actual_high_prime_cutoff":CUTOFF,
        "rigorous_rational_log_bracket_terms":SERIES,
        "active_original_prime_power_indices":list(active()),
        "inactive_composite_6_rejected":True,
        "cells":[{"label":c.label,"center":frac(c.center),
                  "radius":frac(c.radius),"width":frac(c.width)}
                 for c in CELLS],
        "rigorously_classified_directed_signed_prime_edges":[
            {"from":left,"to":right,"prime_power":key[2],
             "sign":key[3]}
            for key,left,right in edges
        ],
        "all_new_prime_edges_absent":True,
        "old_original_n9_edges_retained":True,
        "smallest_positive_rigorous_clearance_lower_bound_1e6":frac(lower6(min_clear)),
        "complete_rational_classification_sha256":digest,
        "true_original_physical_measure":frac(width),
        "true_original_signed_Gamma_coarse_floor":frac(gamma),
        "both_original_pole_cost":frac(poles),
        "historical_old_n9_prime_bound_requires_verified_source":frac(prime),
        "conditional_full_four_cell_Weil_margin":frac(margin),
        "cell_label_permutation_graph_invariance":True,
        "negative_control_real_prime2_collision_detected":True,
        "negative_control_four_cell_width_bound_exhausted_without_new_prime_edge":True,
        "critical_missing_hypothesis":
          "Actual original Zeta23 prime-sum/correlation dictionary and smooth Schwartz partition, as Lean source candidates IV009-IV023, MUST compile before the graph can be promoted to a genuine original Weil form preservation law.",
        "independent_spectral_equivalence_proved":False,
        "graph_is_full_Weil_quadratic_form":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    OUTPUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
    print("IV024 EXACT ARITHMETIC PRIME GRAPH PASS: historical old-old n=9 edges ONLY; zero new edges; measure17/2000, coarse original signed margin1/16 CONDITIONAL. No Lean/spectral/RH claims.")
    return receipt

def selftest():
    data=preflight()
    assert data["all_new_prime_edges_absent"]
    assert data["negative_control_real_prime2_collision_detected"]
    assert data["negative_control_four_cell_width_bound_exhausted_without_new_prime_edge"]
    print("IV024 THREE falsifiable preservation/capacity/invariance negative controls PASS.")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("stage",choices=("preflight","selftest"))
    stage=ap.parse_args().stage
    if stage=="preflight":preflight()
    else:selftest()
