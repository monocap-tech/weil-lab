#!/usr/bin/env python3
"""GERM-72: third-section self-overlap and fourth exterior return.

New exclusion: 3h-theta < e <= 3h-theta+gamma.
The script inherits the rigorously enclosed six second-section matrices from
the byte-pinned GERM-71 audit, then performs only exact Fraction interval
arithmetic. It certifies the four retyped third-section maps needed in this
strip, three complete fourth-section returns, one rational cone chart, the
fixed arithmetic ordering, and the first newly admitted elliptic word.
No floating-point sign decision, sampled topology, large determinant, or
parent symbolic-suite replay is used.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, "Assertions are part of the verifier; do not use -O."

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "notes/_recurrence71_audit.json"
PARENT_SHA256 = "f837da6405cce7a6aff2f67b381e00d9986dad4e41abf142b970dd21357d132b"
assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == PARENT_SHA256

raw = json.loads(PARENT.read_text())
parent = raw["audit"] if raw.get("format") == "GERM71-AUDIT-WORDS-1" else raw
boxes = parent["rational_audit"]["second_section_maps"]

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __post_init__(self):
        assert self.lo <= self.hi
    def __add__(self, other):
        other = box(other)
        return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + (-box(other))
    def __rsub__(self, other):
        return box(other) - self
    def __mul__(self, other):
        other = box(other)
        vals = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def inv(self):
        assert self.lo > 0 or self.hi < 0
        return I(1/self.hi, 1/self.lo)
    def __truediv__(self, other):
        return self * box(other).inv()

def box(x):
    return x if isinstance(x,I) else I(F(x),F(x))

def parse_interval(pair):
    return I(F(pair[0]), F(pair[1]))

def parse_matrix(m):
    return [[parse_interval(x) for x in row] for row in m]

def exact_matrix(m):
    return [[box(x) for x in row] for row in m]

def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), box(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def product(word, library):
    out = exact_matrix([[1,0],[0,1]])
    for key in word:              # chronological: next map left-multiplies
        out = mm(library[key], out)
    return out

def inv_exact_2(c):
    a,b=c[0]; d,e=c[1]
    det=a*e-b*d
    return [[e/det,-b/det],[-d/det,a/det]]

def determinant(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def show(i, places=10):
    scale=10**places
    def floor(q): return q.numerator*scale//q.denominator
    def ceil(q): return -((-q.numerator*scale)//q.denominator)
    def fmt(n):
        sign="-" if n<0 else ""; n=abs(n)
        return f"{sign}{n//scale}.{n%scale:0{places}d}"
    return [fmt(floor(i.lo)),fmt(ceil(i.hi))]

def show_matrix(m):
    return [[show(x) for x in row] for row in m]

SECOND = {k:parse_matrix(v) for k,v in boxes.items()}

# A single third-section step is itself a complete GERM-71 second-section
# return. Only these four species can occur while epsilon<=gamma.
THIRD_WORDS = {
    "00+": ["00-","00+","00+"],
    "01+": ["01-","11+","11+"],
    "10-": ["11-","11+","11+","10+"],
    "00-": ["00-","00+","00+","00+"],
}
THIRD = {k:product(w,SECOND) for k,w in THIRD_WORDS.items()}

# First returns to H=(alpha,theta).  For w>gamma the return time is 2.
# For w<gamma it is 3; the first target is inside iff w<epsilon.
FOURTH_WORDS = {
    "2out": ["00+","00-"],
    "3out": ["00+","00-","00-"],
    "3in":  ["01+","10-","00-"],
}
FOURTH = {k:product(w,THIRD) for k,w in FOURTH_WORDS.items()}

C = [[F(1),F(1)],[F(3,5),F(1,5)]]
Ci = inv_exact_2(C)
CI, CII = exact_matrix(C), exact_matrix(Ci)

cone = {}
for key,b in FOURTH.items():
    q = mm(mm(CII,b),CI)
    if all(x.hi < 0 for row in q for x in row):
        sign=-1
    else:
        sign=1
    p=[[sign*x for x in row] for row in q]
    assert all(x.lo > 0 for row in p for x in row), (key,show_matrix(p))
    delta=determinant(p)
    assert delta.lo > 0
    fw=min(p[0][0].lo+p[1][0].lo, p[0][1].lo+p[1][1].lo)
    bw=min(p[1][1].lo+p[1][0].lo, p[0][1].lo+p[0][0].lo)/delta.hi
    assert fw > 40 and bw > 40, (key,fw,bw)
    cone[key]={
        "third_section_word":FOURTH_WORDS[key],
        "overall_sign":sign,
        "positive_conjugate":show_matrix(p),
        "determinant_enclosure":show(delta),
        "forward_lower":show(box(fw))[0],
        "backward_lower":show(box(bw))[0],
    }

# Immediately above epsilon=gamma, gamma<w<epsilon is a legal two-step
# return with word 01+,10-.  It is genuinely projectively elliptic.
changed=product(["01+","10-"],THIRD)
tr=changed[0][0]+changed[1][1]
detc=determinant(changed)
disc=tr*tr-4*detc
assert detc.lo>0 and tr.lo>F(-3,2) and tr.hi<F(-7,5)
assert disc.hi<0

# Exact prime-log arithmetic.
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(n,a): return tuple(n*x for x in a)

H=(-4,4,-1)
K=(4,-1,-1)
KAP=sub(K,mul(5,H))
TAU=sub(H,mul(5,KAP))
THETA=sub(KAP,mul(8,TAU))
ALPHA=sub(TAU,mul(3,THETA))
BETA=sub(THETA,ALPHA)
GAMMA=sub(ALPHA,BETA)

assert KAP==(24,-21,4)
assert TAU==(-124,109,-21)
assert THETA==(1016,-893,172)
assert ALPHA==(-3172,2788,-537)
assert BETA==(4188,-3681,709)
assert GAMMA==(-7360,6469,-1246)
assert sub(ALPHA,BETA)==GAMMA
assert sub(THETA,ALPHA)==BETA
assert GAMMA==sub(mul(2,ALPHA),THETA)

def prime_sign(v):
    num=den=1
    for p,e in zip((2,3,5),v):
        if e>=0:num*=p**e
        else: den*=p**(-e)
    return (num>den)-(num<den)

checks={
    "gamma_positive":GAMMA,
    "beta_minus_gamma_positive":sub(BETA,GAMMA),
    "beta_positive":BETA,
    "alpha_minus_beta_positive":sub(ALPHA,BETA),
    "theta_minus_alpha_positive":sub(THETA,ALPHA),
}
assert all(prime_sign(v)>0 for v in checks.values())

# Endpoint: e72=3h-theta+gamma=1759h-338k.
E72=add(sub(mul(3,H),THETA),GAMMA)
assert E72==sub(mul(1759,H),mul(338,K))
L72=add((4,-1,0),E72)     # log(16/3)+e72
assert L72==(-8384,7373,-1421)

out={
  "pass":"SZ-KERNEL-EDGE-GERM-72",
  "standing":"UNRATIFIED",
  "entry_commit":"af8faabfec8952d24ab5ad7c31212f7889958e8f",
  "inherited_formula_scope":"2h<e<=3h",
  "new_exclusion_scope":"3h-theta<e<=3h-theta+gamma",
  "experimental_endpoint":"log(3^7373/(2^8384*5^1421))",
  "parent_audit_sha256":PARENT_SHA256,
  "third_section_words":THIRD_WORDS,
  "fourth_section_words":FOURTH_WORDS,
  "fourth_section_map":"w -> w-gamma mod beta",
  "fourth_section":"alpha<v<theta; coordinate 0<w<beta",
  "exact_order_checks":{k:"PASS" for k in checks},
  "cone_chart":[["1","1"],["3/5","1/5"]],
  "common_forward_backward_factor":"40",
  "cone_certificate":cone,
  "above_scope_word":["01+","10-"],
  "above_scope_trace":show(tr),
  "above_scope_determinant":show(detc),
  "above_scope_discriminant":show(disc),
  "above_scope_status":"PROJECTIVELY ELLIPTIC; CURRENT COMPLETE-RETURN CONE LIBRARY STOPS",
  "sampled_topology_used":False,
  "floating_sign_tests_used":False,
  "old_large_determinants_rerun":False,
  "full_parent_symbolic_suites_rerun":False,
  "canonical_cursor":"SZ-CROSS-COLLAR-3",
  "canonical_effect":"NONE",
}
print(json.dumps(out,indent=2))
