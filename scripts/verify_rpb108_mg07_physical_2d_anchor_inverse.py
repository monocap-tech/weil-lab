#!/usr/bin/env python3
"""Exact physical 2D anchor inverse bound from a pinned repaired GH artifact.

This certifies one inverse/coupling term. It does not evaluate the full-form
mixed functionals or certify the remaining finite/infinite Schur.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

JSON_SHA = '264fd853ca006a578d76369ac5bd4588a2097145b829fbba7036693f29b04044'
SOURCE_SHA = '8844685d3e72a3d38f943b084b6e5bc70ef3d09c'

def det2(h):
    return h[0][0]*h[1][1]-h[0][1]*h[1][0]

def psd2(h):
    return h[0][0] >= 0 and h[1][1] >= 0 and h[0][1] == h[1][0] and det2(h) >= 0

def inverse2(h):
    d=det2(h)
    assert h[0][0]>0 and d>0
    return [[h[1][1]/d,-h[0][1]/d],[-h[1][0]/d,h[0][0]/d]]

def subtract(a,b):
    return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]

def verify(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==JSON_SHA
    z=json.loads(raw)
    assert z['status']=='CERTIFIED_TRUE_ORIGINAL_SIGNED_2D_SINE_POLE_POSITIVITY'
    assert z['original_basis']==[['1','4096/3013','near_null'],['1','-1','complement']]
    assert z['positive_high12_form_discarded_as_psd'] is True
    assert z['cross_bound_scope']=='lowband_plus_pole_minus_negative_high_tail'
    assert F(z['lowband_baseline_rounding_upper_payment'])==F(7168,10**9)
    a=F(z['full_signed_A_diagonal_lower'])
    d=F(z['full_signed_D_diagonal_lower'])
    b=F(z['retained_signed_cross_abs_upper'])
    assert z['full_signed_cross_abs_upper']==z['retained_signed_cross_abs_upper']
    assert b>=0 and a*d-b*b==F(z['full_signed_2D_determinant_lower'])>0
    inverse_caps=(F(8000),F(24))
    lower=(1/inverse_caps[0],1/inverse_caps[1])
    x,y=a-lower[0],d-lower[1]
    reserve=x*y-b*b
    assert x>0 and y>0 and reserve>0
    # For every retained anchor matrix T with diagonals >=a,d and
    # |T01|<=b, T>=diag(lower). The omitted positive high form is PSD,
    # so the COMPLETE physical anchor H also >=diag(lower).
    # Inverse order gives H^-1 <= diag(8000,24).
    upper=[[F(8000),F(0)],[F(0),F(24)]]
    diag=[[lower[0],F(0)],[F(0),lower[1]]]
    for sign in (-1,1):
        h=[[a,sign*b],[sign*b,d]]
        assert psd2(subtract(h,diag))
        assert psd2(subtract(upper,inverse2(h)))
        # Arbitrary omitted positive high-frequency mixed term:
        # inverse dominance survives, its offdiagonal is not bounded by b.
        v=(F(100),F(100))
        full=[[h[i][j]+v[i]*v[j] for j in range(2)] for i in range(2)]
        assert abs(full[0][1])>b
        assert psd2(subtract(upper,inverse2(full)))
    # Positive anchor and positive remainder separately do not prove
    # the full block positive: a complete mixed term can overturn it.
    # Synthetic algebra countermodel, never original operator data.
    h=diag
    coupling=F(1,80)
    remainder=F(1)
    exact_schur=remainder-coupling**2/h[0][0]
    assert exact_schur<0
    assert F(7100,24)>295
    assert z['original_global_signed_Wodd']==z['even_CC27_Weil_RH']=='OPEN'
    return dict(status='CERTIFIED_CONDITIONAL_PHYSICAL_2D_ANCHOR_INVERSE_CAP',
                input_run_id=40260136876,input_artifact_id=12623752657,
                input_source_sha=SOURCE_SHA,input_json_sha256=JSON_SHA,
                basis=z['original_basis'],
                retained_diagonal_lowers=[str(a),str(d)],
                retained_cross_abs_upper=str(b),
                physical_anchor_diagonal_lower=list(map(str,lower)),
                diagonal_lower_determinant_reserve=str(reserve),
                complete_physical_anchor_inverse_diagonal_upper=list(map(str,inverse_caps)),
                complete_mixed_schur_penalty='8000*|Q(f,r)|^2 + 24*|Q(g,r)|^2',
                mixed_functionals_must_use_complete_original_form=True,
                original_mixed_functionals_evaluated=False,
                remaining_signed_schur_certified=False,
                SM34_energy_dual_substitution_valid=False,
                inherited_analytic_assumptions_reproved=False,
                whole_original_odd_positivity='OPEN',even_CC27_Weil_RH='OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input',required=True)
    p.add_argument('--output',default='artifacts/mg07_physical_2d_anchor_inverse.json')
    args=p.parse_args()
    result=verify(args.input)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PHYSICAL ANCHOR INVERSE PASS: H^-1 <= diag(8000,24)')
    print('Complete mixed functionals and remaining signed Schur OPEN')
