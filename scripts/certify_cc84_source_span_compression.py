#!/usr/bin/env python3
"""Exact finite source-span compression controls and NF43 inertia check."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc80_defect_response_acceptance as m
import certify_cc81_boundary_response_consumer as c
import certify_cc83_five_source_consumer as parent

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def q(a,x):return dot(x,[dot(row,x) for row in a])
def block(k,p,b):
    e=[r[:2] for r in k[:2]]; ei=m.inv(e); r=[k[0][2],k[1][2]]
    s=k[2][2]-q(ei,r);assert s<0
    pe=[row[:2] for row in p]
    metric=m.add(b,m.mul(m.mul(pe,ei),m.tr(pe)))
    t=[row[2]-dot(row[:2],[dot(v,r) for v in ei]) for row in p]
    mi=m.inv(metric);a=[dot(row,t) for row in mi];theta=dot(t,a)
    full=m.add(k,m.mul(m.mul(m.tr(p),m.inv(b)),p))
    # Reconstruct complete updated condensation independently.
    fe=[row[:2] for row in full[:2]];fr=[full[0][2],full[1][2]]
    full_margin=full[2][2]-q(m.inv(fe),fr)
    assert full_margin==s+theta
    if theta:
        combined=[sum(a[j]*p[j][i] for j in range(len(p))) for i in range(3)]
        denominator=q(b,a);assert denominator>0
        single=m.add(k,[[x*y/denominator for y in combined] for x in combined])
        se=[row[:2] for row in single[:2]];sr=[single[0][2],single[1][2]]
        single_margin=single[2][2]-q(m.inv(se),sr)
        assert single_margin==full_margin
        signed=m.add(b,m.mul(m.mul(p,m.inv(k)),m.tr(p)))
        assert q(signed,a)==theta+theta**2/s
        assert (q(signed,a)<0)==(full_margin>0)
    return s,theta,full_margin,a,full

def controls():
    rows=[]
    transform=m.mat([[1,F(1,3),0],[0,1,F(1,4)],[0,0,1]])
    for scale in [F(1),F(1,10**18)]:
        k0=m.diag([1,1,-scale**2]);p0=m.mat([[1,0,scale],[-1,0,scale]])
        k=m.mul(m.mul(m.tr(transform),k0),transform);p=m.mul(p0,transform)
        for multiplier in [F(99,100),F(1),F(101,100)]:
            b=m.diag([2*multiplier]*2)
            s,theta,margin,a,full=block(k,p,b)
            assert margin==scale**2*(-1+1/multiplier)
            # Each individual row fails the inverse-cone screen.
            ki=m.inv(k);assert all(b[j][j]+q(ki,p[j])>0 for j in range(2))
            assert (margin>0)==(multiplier<1) and (margin==0)==(multiplier==1)
            rows.append(dict(scale=str(scale),denominator_multiplier=str(multiplier),
                exact_batch_and_combination_margin=str(margin),each_individual_column_fails=True,
                optimal_rational_combination=list(map(str,a))))
    # Three-column correlated denominator: no diagonal replacement.
    k=m.mat([[2,1,1],[1,2,1],[1,1,F(1,6)]])
    p=m.mat([[1,0,2],[-1,0,2],[0,1,F(1,3)]])
    b=m.mat([[2,F(1,5),0],[F(1,5),2,F(1,7)],[0,F(1,7),3]])
    assert all(x>0 for x in m.pivots(b));s,theta,margin,a,full=block(k,p,b)
    assert margin>0 and all(x>0 for x in m.pivots(full))
    return dict(two_column_crossings=rows,three_column_signed_metric_control=True,
        combined_column_reproduces_batch_condensed_margin=True)

def run(root):
    rows=[]
    for parity in ['even','odd']:
        d=parent.load(root,'RPB108_NF43_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json')
        k=c.matrix(d['conditional_five_high_joined_Schur_lower_matrix']);s,ei,beta=parent.condensed(k)
        assert s[1]<0 and c.det3(k)[1]<0
        rows.append(dict(parity=parity,certified_inertia='two positive, one negative',
            current_condensed_deficit=c.pair(c.neg(s)),source_floor_hypothesis=d['background_floor_hypothesis']))
    return dict(milestone='CC84',integration_parent='f867b20e04d6783125a8a2ae0870b15ac16a40aa',
        read_only_source='b21b3df8e026db1b8b253325442b6dfaa63f05ef',parity_checks=rows,
        exact_controls=controls(),actual_new_source_span_certified=False,
        simultaneous_six_direction_certificate=False,whole_aperture_positive=False)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF43_root',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    d=run(a.NF43_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    print('CC84 PASS: original inertia and exact batch/one-combination equivalence controls')
