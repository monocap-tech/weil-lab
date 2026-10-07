#!/usr/bin/env python3
"""Custody and algebraic controls; not a proof of null exclusion or F4."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'notes/data/RPB108_COPOISSON_RANGE_ATTACHMENT_20261007.json').read_text())
for pin in m['internal_sources']:
    b=(root/pin['path']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['blob_sha']
s=F(3,8);epsilon=F(1,16)
assert 2*(F(1,4)+epsilon)==F(5,8)<2*s<F(1)
# Geometric weak tail gives every subcritical polynomial moment, including 3/4.
budgets=0
for n in range(1,65):
    # Fourth powers avoid irrational dyadic factors: height=16^j, mass=16^-j.
    T=F(16**n)
    tail=sum((F(1,16**j) for j in range(n+1,129)),F(0))
    assert T*tail<F(1,15)
    moment=sum((F(8**j,16**j) for j in range(1,n+1)),F(0))
    assert moment==1-F(1,2**n)<1
    budgets+=1
gaps=0
for j in range(1,65):
    lam=F(j,j+1)
    for r in (F(1,4),F(1,2),F(1),F(2),F(4)):
        left,right=lam/r,r*lam
        assert left*right==lam*lam<1
        assert not(left>=1 and right>=1)
        gaps+=1
moments=0
for j in range(1,65):
    # Polynomial factor from integration by parts: central zero order j,
    # but at s=0 the multiplier is (1/2)^j, strictly nonzero.
    assert F(0)**j==0 and F(1,2)**j>0
    moments+=1
assert m['actual_bounded_return_found'] is False
assert m['global_graph_shortened'] is False
assert m['lean_certified'] is False
assert set(m['controls'])=={'actual_positive_eigenmode','artificial_compact_good_rows',
    'finite_actual_restoration','two_row_comparison_contact'}
print(json.dumps({'verified_internal_pins':len(m['internal_sources']),
    'strict_multiplier_budget':True,'weak_tail_moment_checks':budgets,
    'dilation_gap_checks':gaps,'central_vs_pole_moment_checks':moments,
    'scope':'lawful attachment obstruction; sharp-return and F4 unproved'},indent=2))
