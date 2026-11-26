#!/usr/bin/env python3
"""Exact rational pilot: partial constraint nullspace, not full-kernel or Schur certificate."""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path

N = 665
a = F(11, 10)
h = 2*a/N
def d(p):
    return [i*p[i] for i in range(1,len(p))]
def add(p,q):
    return [(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
            for i in range(max(len(p),len(q)))]
def integral(p):
    return sum((x/F(i+1) for i,x in enumerate(p)),F(0))
def gram(p,q):
    return sum((x*y/F(i+j+1) for i,x in enumerate(p)
                for j,y in enumerate(q)),F(0))

# b=u^5(1-u)^5, v=b'''-h^2 b'/4 on the unit cell, zero outside.
b = [F(0)]*5 + [F((-1)**j*comb(5,j)) for j in range(6)]
p = b
for j in range(5):
    assert p[0] == sum(p) == 0
    p = d(p)
v = add(d(d(d(b))),[-h*h*x/4 for x in d(b)])
assert integral(v)==0 and v[0]==sum(v)==0
assert d(v)[0]==sum(d(v))==0
# Integration by parts: integral exp(s h u) v =
# ((-s*h)^3-h^2*(-s*h)/4) integral exp(s h u) b.
for s in [F(-1,2),F(1,2)]:
    assert (-s*h)**3-h*h*(-s*h)/4==0
cells=[(-a+j*h,-a+(j+1)*h) for j in range(1,N-1)]
assert len(cells)==663
assert all(-a<l<r<a for l,r in cells)
assert all(cells[j][1]==cells[j+1][0] for j in range(len(cells)-1))
# IV100 packed carrier support is inside [1099/1000-3/4000,1099/1000+3/4000].
collar=(F(1099,1000)-F(3,4000),F(1099,1000)+F(3,4000))
assert cells[-1][1]<collar[0]
m=h*gram(v,v)
e=gram(d(v),d(v))/h
assert m>0 and e>0
result={
 "gate":"IV106-E18A",
 "classification":"exact rational partial-constraint trial pilot; no native or full-kernel certificate",
 "frozen_research":"018f7e59f4129ce521cd3ae86d1afd59d3b64b5f",
 "constraint_source":"25d13ea5fb5fce899121fd61ab5ae54a5b954002",
 "cell_count":N,"cell_width":str(h),"first_cell":1,"last_cell":N-2,
 "bank_size":len(cells),"support_union":[str(cells[0][0]),str(cells[-1][1])],
 "packed_collar":[str(x) for x in collar],
 "polynomial_ascending":[str(x) for x in v],
 "physical_mass_gram":{"structure":"diagonal","diagonal":str(m)},
 "weak_derivative_gram":{"structure":"diagonal","diagonal":str(e)},
 "derivative_mass_ratio":str(e/m),
 "verified_algebra":["boundary jets of b through order 4","cell mean zero","C1 zero extension",
 "exponential-moment IBP factors at +/-1/2 vanish","cell interiors disjoint",
 "packed carrier support separation","positive exact diagonal mass and derivative Gram"],
 "unresolved":["native H1-to-log carrier lift for these piecewise polynomials",
 "actual IV105CResponse row contractions and exact nullspace correction",
 "receiving-sector Riesz representatives and trial approximation",
 "trial Weil and projected residual Gram enclosures","Schur positivity"],
 "note":"Both pole moments are individually zero, stronger than required; this pilot is not claimed dense in the full constraint kernel."
}
if __name__=="__main__":
    expected=json.loads(Path(__file__).with_name("pilot.json").read_text())
    assert result==expected,(result,expected)
    print(json.dumps(result,indent=2))
    print("Exact rational pilot replay PASS")
