#!/usr/bin/env python3
"""Rational sign and cutoff-custody controls; no actual zeta data."""
from fractions import Fraction as F
import json

def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),F(0))
def swap(x):
    return (x[1],x[0])
def project(x,y):
    return tuple((a+b)/2 for a,b in zip(x,swap(y)))+tuple((a+b)/2 for a,b in zip(swap(x),y))
signs=[]
for h,expected in [((F(0),F(1)),F(1)),((F(1),F(0)),F(-1))]:
    g=h+swap(h);jg=g[:2]+tuple(-x for x in g[2:])
    mg=tuple(a*b for a,b in zip((1,2,1,2),g))
    pg=project(mg[:2],mg[2:]);err=tuple(a-b for a,b in zip(mg,pg))
    assert dot(jg,pg)==0
    assert dot(jg,mg)==dot(jg,err)==expected
    signs.append(str(expected))
# Neutral atomic signed measure, including exact cutoff atoms and a zero atom.
atoms=[(F(0),F(-1,2)),(F(1),F(1)),(F(2),F(-1,2))]
assert sum((d for u,d in atoms),F(0))==0
for height in [F(0),F(1,2),F(1),F(3,2),F(2),F(3)]:
    tail=sum((d for u,d in atoms if u>height),F(0))
    tail_integral=sum((d*min(u,height) for u,d in atoms),F(0))
    sharp=sum((u*d for u,d in atoms if u<=height),F(0))
    assert sharp==tail_integral-height*tail
print(json.dumps({"kind":"finite algebraic controls only","graph_error_signs":signs,
 "exact_atom_tail_identity_checks":6,"actual_critical_bound_certified":False},
 indent=2,sort_keys=True))
