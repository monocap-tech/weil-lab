#!/usr/bin/env python3
"""Custody and operator-representation algebra; not an exclusion certificate."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1]
m=json.loads((r/'notes/data/RPB108_ACTUAL_LOG_OPERATOR_ATTACHMENT_20261007.json').read_text())
for p in m['internal_sources']:
    b=(r/p['path']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['blob_sha']
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def shift(x,k):return [x[i-k] if 0<=i-k<len(x) else F(0) for i in range(len(x))]
counts={'cutoff_mass_cancellation':0,'compressed_shift_adjoint':0,
    'pole_rank_two_identity':0,'eigenvalue_residual_retained':0}
for j in range(1,65):
    mass,rho,near,tail,dk,lb=map(F,(j,-j,3*j,2*j,j+1,2-j))
    c=mass-rho/2+2*near+2*tail
    rho_b=rho-2*lb
    near_b=near+dk-lb/2;tail_b=tail-dk
    assert mass-rho_b/2+2*near_b+2*tail_b==c
    counts['cutoff_mass_cancellation']+=1
    x=[F(i-j,7) for i in range(9)];y=[F(i+j,11) for i in range(9)]
    k=j%9
    assert dot(shift(x,k),y)==dot(x,shift(y,-k))
    counts['compressed_shift_adjoint']+=1
    # rx,ry stand for positive exp(x/2), exp(y/2).
    rx,ry=F(j+1,j),F(j+2,j+1)
    cx,sx=(rx+1/rx)/2,(rx-1/rx)/2
    cy,sy=(ry+1/ry)/2,(ry-1/ry)/2
    assert rx/ry+ry/rx==2*(cx*cy-sx*sy)
    counts['pole_rank_two_identity']+=1
    mu,h,lh=F(j,13),F(j+1,17),F(2-j,19)
    bh=mu*h-lh/2
    assert lh==2*(mu*h-bh)
    assert lh+2*bh==2*mu*h
    assert 2*mu*h!=0
    counts['eigenvalue_residual_retained']+=1
assert not m['global_arithmetic_gate_closed'] and not m['lean_certified']
print(json.dumps({'verified_internal_pins':len(m['internal_sources']),**counts,
    'scope':'actual all-window operator attachment; signed sharp arithmetic still open'},indent=2))
