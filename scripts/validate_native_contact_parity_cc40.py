#!/usr/bin/env python3
"""Reproduce CC40's exact two-mode parity threshold inequalities.

Reads a PINNED copy of NF12's complete signed low4 rational intervals,
not the current head of another branch. Uses Fraction throughout.
This is a finite-dimensional variational diagnostic only.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "notes/data/RPB108_CC40_NATIVE_PARITY_LOW2_INPUT_20261008.json"

def read():
    j = json.loads(DATA.read_text())
    assert j["aperture"] == "53/50"
    assert j["source_commit"] == "33d2b6bbd233d09e8c401b086545d0647b283817"
    g = int(j["grid_denominator"])
    assert g == 10**25
    d = j["source_intervals"]
    assert set(d) == {"0,0", "0,2", "1,1", "1,3", "2,2", "3,3"}
    def iv(k,p):
        a,b = (F(int(v),g) for v in d[k][p])
        assert a<=b
        return a,b
    return d,iv

def add(p,q):
    return (p[0]+q[0],p[1]+q[1])
def neg(p):
    return (-p[1],-p[0])
def sub(p,q):
    return add(p,neg(q))
def mul(p,q):
    a = [x*y for x in p for y in q]
    return min(a),max(a)
def sq(p):
    if p[0]>=0: return (p[0]**2,p[1]**2)
    if p[1]<=0: return (p[1]**2,p[0]**2)
    return F(0),max(p[0]**2,p[1]**2)
def det(a,b,c):
    return sub(mul(a,c),sq(b))
def positive(p):
    assert p[0]>0
def negative(p):
    assert p[1]<0
def lt_scale(a,n,b):
    assert n*a[1] < b[0]

def validate():
    d,iv=read()
    n=0
    def check(q):
        nonlocal n
        assert q
        n+=1
    for k in d:
        terms=add(add(iv(k,"arch"),iv(k,"prime")),iv(k,"poles"))
        native=iv(k,"full")
        check(terms[0] <= native[1] and native[0] <= terms[1])
    H=lambda k: add(iv(k,"arch"),iv(k,"prime"))
    E=det(H("0,0"),H("0,2"),H("2,2"))
    O=det(H("1,1"),H("1,3"),H("3,3"))
    EQ=det(iv("0,0","full"),iv("0,2","full"),iv("2,2","full"))
    OQ=det(iv("1,1","full"),iv("1,3","full"),iv("3,3","full"))
    B=sub(EQ,E)
    for q in (E[1]<0,O[0]>0,EQ[0]>0,OQ[0]>0,B[0]>0,
              iv("0,0","full")[0]>0,iv("2,2","full")[0]>0,
              iv("1,1","full")[0]>0,iv("3,3","full")[0]>0):
        check(q)
    # beta_e+2 = 2 det(Qe)/(det(Qe)-det(He))
    # beta_o-2 = 2 det(Qo)/(det(Ho)-det(Qo))
    # 1 - R_o = det(Qo)/det(Ho)
    check(6000*EQ[1]<B[0])  # 0 < beta_e+2 < 1/3000
    check(151*OQ[1]<O[0])  # 0 < beta_o-2 < 1/75
    check(150*OQ[1]<O[0])  # 149/150 < R_o < 1
    check(OQ[1]<O[0])
    return {
        "stage":"CC40 native contact scalar Ritz",
        "all_passed":True,
        "exact_rational_checks":n,
        "dimension_per_parity":2,
        "even_H_inertia":"1 negative, 1 positive",
        "odd_H_inertia":"2 positive",
        "even_beta_gap":"0 < beta_e^(2)+2 < 1/3000",
        "odd_beta_gap":"0 < beta_o^(2)-2 < 1/75",
        "odd_susceptibility":"149/150 < R_o^(2) < 1",
        "whole_original_aperture106":False,
        "global_contact_excluded":False,
        "lean":False,
    }

if __name__=="__main__":
    print(json.dumps(validate(),indent=2))
