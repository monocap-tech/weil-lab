#!/usr/bin/env python3
"""Source custody and exact projection controls, not actual null exclusion."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'notes/data/RPB108_EXTERNAL_TERMINAL_DEFECT_20261007.json').read_text())
for p in m['internal_sources']:
    b=(root/p['path']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['blob_sha']
def inner(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
controls=0
for j in range(1,65):
    # An arbitrary non-coordinate subspace, not a chosen zero source vector.
    v=[F(j),F(1),F(2-j)];norm=inner(v,v)
    def proj(x):return [a*inner(v,x)/norm for a in v]
    def q(x,y):
        px,py=proj(x),proj(y)
        return inner([a-b for a,b in zip(x,px)],[a-b for a,b in zip(y,py)])
    x=[F(j-2),F(3),F(j+1)]
    y=[F(2*j),F(-1),F(5)]
    assert proj(proj(x))==proj(x)
    assert q(v,x)==q(v,y)==0 and q(x,x)>=0
    assert q(x,y)==inner(x,y)-inner(v,x)*inner(v,y)/norm
    # The same vector is a positive eigenvector after a mass shift.
    mu=F(j,7)
    assert q(v,x)+mu*inner(v,x)==mu*inner(v,x)
    controls+=1
coefficients=0
for j in range(1,65):
    c=F(j,11)
    for sigma in (-1,1):
        left,right=sigma*c,c
        assert left*left+right*right==2*c*c>0
        # Dividing by pi gives the proved continuum coefficient 2/pi*c^2.
        coefficients+=1
assert not m['actual_bounded_return_found'] and not m['global_graph_shortened']
assert m['comparison_source']=='continuous Fourier plus finite artificial negative rows'
assert m['actual_transfer_proved'] is False
print(json.dumps({'verified_internal_pins':len(m['internal_sources']),
    'full_mixed_projection_and_mass_shift_checks':controls,
    'balanced_log_coefficient_checks':coefficients,
    'scope':'external terminal-defect permission; actual sharp arithmetic gate open'},indent=2))
