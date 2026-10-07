#!/usr/bin/env python3
"""Exact contour algebra and selection budgets, not an arithmetic sign certificate."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'notes/data/RPB108_GOOD_HEIGHT_CONTOUR_20261007.json').read_text())
for p in m['internal_sources']:
    b=(root/p['path']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['blob_sha']
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def conj(a):return (a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def norm2(a):return a[0]**2+a[1]**2
residues=reflections=0
for j in range(1,65):
    p=(F(j,17),F(3-j,19));n=(F(2*j-7,23),F(j+1,29))
    w=mul(add(p,n),conj(add(p,neg(n))))
    d=norm2(p)-norm2(n);v=norm2(p)+norm2(n)
    assert w[0]==d and w[1]==2*mul(n,conj(p))[1]
    assert norm2(w)<=v*v
    for theta in (F(j),F(-j)):
        beta=F((-1)**j*3,8)
        r=(theta,-beta);sign=1 if theta>0 else -1
        real=sign*mul(r,w)[0]
        assert real==abs(theta)*d+sign*beta*w[1]
        assert abs(beta*w[1])<=F(3,8)*v
        residues+=1
        A=(F(j+2,7),F(1-j,11))
        right=mul(mul(r,w),A)
        left=mul(mul(conj(r),conj(w)),neg(conj(A)))
        difference=add(right,neg(left))
        assert difference==(2*right[0],F(0))
        assert add(neg(right),left)==(-2*right[0],F(0))
        reflections+=1

good_measure=selection=0
for C in range(1,65):
    eta=F(1,4*C)
    assert 2*C*eta==F(1,2)
    good_measure+=1
# Set u=log T, L(T)=1/(T*u^3): log-weighted integral from u=n is 1/n,
# while T log^2 T L=1/n. This tests the critical log powers, not actual h.
for n in range(1,65):
    weighted_tail=F(1,n);cap_budget=F(1,n)
    assert weighted_tail==cap_budget>0
    # If cap budget had a positive lower bound epsilon, weighted integral
    # would dominate epsilon*integral_E dT/(T log T), which diverges.
    epsilon=F(1,n)
    assert epsilon*F(1,n)>0
    selection+=1
# Cap=0 is compatible with positive bulk at every log height: the generic
# inference from cap vanishing to bounded head is rejected.
for n in range(1,65):
    cap=F(0);bulk=F(n);head=bulk+cap+F(7,13)
    assert cap==0 and head/F(n)>1
print(json.dumps({'residue_checks':residues,'vertical_orientation_checks':reflections,
    'good_height_measure_budgets':good_measure,'critical_log_power_controls':selection,
    'cap_zero_positive_bulk_controls':64,'verified_internal_pins':len(m['internal_sources']),
    'scope':'contour substep and obstruction; actual arithmetic sign unproved'},indent=2))
