#!/usr/bin/env python3
"""Exact-Fraction replay of a pinned accepted native physical Schur witness.

This independently checks the final normalization arithmetic, not the
transcendental physical Gram construction. That construction is retained
with its separate accepted GitHub source/run custody.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

NATIVE_COMMIT='ab41a96861c9e5d0623807e40d53482985d143bc'
NATIVE_RUN=40385192745
NATIVE_ARTIFACT=12679609974
ARCHIVE_SHA256='243d40e1fc7d7ce349a0c16c809f06eea0593cd91635d6966241e4f5f478cf33'
JSON_SHA256='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'

def dyadic(x):
    m,e=int(x[0]),int(x[1])
    return F(m*(2**max(e,0)),2**max(-e,0))
def transpose(m):return list(map(list,zip(*m)))
def mm(a,b):
    columns=transpose(b)
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in columns] for row in a]

def run(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==JSON_SHA256
    z=json.loads(raw)
    assert z['status']=='CERTIFIED_FULL_ORIGINAL_J470_SI29_L2_QUOTIENT_NORMALIZATION'
    assert z['working_precision_bits']==4096
    assert z['full_original_source_count']==470 and z['actual_feature_count']==14
    assert len(z['full_physical_projection_coefficient_balls'])==470
    assert all(len(r)==14 for r in z['full_physical_projection_coefficient_balls'])
    C=[[dyadic(v) for v in row] for row in z['exact_dyadic_feature_transform']]
    midpoint=[[dyadic(v[0]) for v in row] for row in z['physical_Schur_balls']]
    radius=[[dyadic(v[1]) for v in row] for row in z['physical_Schur_balls']]
    assert len(C)==len(midpoint)==len(radius)==14
    assert all(len(row)==14 for row in C+midpoint+radius)
    assert all(v>=0 for row in radius for v in row)
    assert midpoint==transpose(midpoint) and radius==transpose(radius)
    absolute=[[abs(v) for v in row] for row in C]
    center=mm(mm(transpose(C),midpoint),C)
    error=mm(mm(transpose(absolute),radius),absolute)
    rows=[sum((abs(center[i][j]-int(i==j))+error[i][j] for j in range(14)),F(0))
          for i in range(14)]
    # Original true S is symmetric. This exact row-sum bound controls
    # ||Cstar S C-I||_2 uniformly over its full dyadic interval enclosure.
    assert max(rows)<F(1,10**24)<F(1,100)
    assert z['normalized_physical_Schur_lower']=='99/100'
    assert z['normalized_physical_Schur_upper']=='101/100'
    floor=F(99,100)*F(33621,10**9)
    assert F(z['normalized_Astar_energy_Schur_lower'])==floor
    assert z['physical_full_J_projection_computed'] is True
    for key in ('full_J_Astar_energy_projection_computed','Astar_energy_condition_number_certified',
                'normalized_forcing_entries_computed','inverse_response_value_certified'):
        assert z[key] is False
    assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_analytic_domain_review']=='OPEN'
    return dict(status='EXACT_RATIONAL_REPLAY_OF_ACCEPTED_FULL_J_PHYSICAL_NORMALIZATION',
        native_commit=NATIVE_COMMIT,native_run=NATIVE_RUN,native_artifact=NATIVE_ARTIFACT,
        native_archive_sha256=ARCHIVE_SHA256,native_json_sha256=JSON_SHA256,
        exact_rational_row_error_upper=list(map(str,rows)),
        uniform_row_error_ceiling='1/'+str(10**24),
        normalized_physical_Gram_lower='99/100',normalized_physical_Gram_upper='101/100',
        conditional_original_Astar_energy_Schur_lower=str(floor),
        native_Gram_construction_independently_recomputed_here=False,
        normalized_forcing_computed=False,inverse_response_value_certified=False,
        inherited_original_analytic_domain_review='OPEN',W_ODD_NEG='OPEN',even_CC27_Weil_RH='OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--certificate',required=True)
    p.add_argument('--output',default='artifacts/si29_L2_exact_dyadic_replay.json')
    args=p.parse_args()
    z=run(args.certificate)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(z,indent=2)+'\n')
    print('EXACT RATIONAL SI29 NORMALIZATION PASS: dyadic interval row error <1e-24')
    print('Same full J470 quotient; physical Gram [0.99,1.01] and conditional energy floor',z['conditional_original_Astar_energy_Schur_lower'])
    print('Actual Astar matrix, matched forcing and inverse response remain OPEN')
