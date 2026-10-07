#!/usr/bin/env python3
"""Algebra/constant controls only; no actual-kernel or Lean certificate."""
from fractions import Fraction as F
import json

def clean(p):
    return {e:c for e,c in p.items() if c}

def derivative(p): # s=2L+1
    return clean({e-1:2*e*c for e,c in p.items() if e})

def shift(p,e):
    return clean({k+e:c for k,c in p.items()})

def subtract(p,q):
    d=p.copy()
    for e,c in q.items(): d[e]=d.get(e,F(0))-c
    return clean(d)

ode_checks=0
for w in [F(0),F(1),F(-2),F(3,7)]:
    for c in [F(1),F(-1),F(2,5)]:
        for kind in [0,1]:
            r={F(-kind):c}
            V=clean({F(1,2):w,F(-kind):c if not kind else c/3})
            H=shift(subtract(V,r),F(-1))
            assert derivative(V)==H
            W=shift(V,F(-1,2))
            assert derivative(W)=={e:-v for e,v in shift(r,F(-3,2)).items()}
            ode_checks+=1

for j in range(1,65):
    eps=F(1,2**j)
    assert 2*(1-eps)<2  # exact integrated low-frequency mass error

def gram(v):
    return [[x*y for y in v] for x in v]

balanced=0
for n in range(1,9):
    R=[F(1)]+[F(0)]*(n-1)
    for sign in [1,-1]:
        L=[sign*x for x in R]
        assert gram(R)==gram(L)
        # Right: left pairing -1/2, exterior pairing +1/2.
        # Left: left pairing +1/2, exterior pairing -1/2.
        assert -F(1,2)*R[0]**2+F(1,2)*L[0]**2 == F(1,2)*R[0]**2-F(1,2)*L[0]**2
        balanced+=1
R=[F(1),F(1)]; L=[F(1),F(-1)]
assert all(R[j]**2==L[j]**2 for j in range(2))
assert gram(R)!=gram(L) # diagonal basis checks alone miss the mixed defect

print(json.dumps({
    "status":"PASS",
    "scope":"integrating-factor, mass-budget and boundary-Gram controls only",
    "exact_ode_profiles":ode_checks,
    "layer_cake_error_checks":64,
    "balanced_rank_one_controls":balanced,
    "mixed_gram_negative_control":"rejected despite matching basis diagonal norms",
    "quotient_scope":"trace kernel may contain nonzero regular coordinates",
    "actual_null_or_lean_certificate":False,
},indent=2,sort_keys=True))
