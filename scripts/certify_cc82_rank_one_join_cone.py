#!/usr/bin/env python3
"""Certify NF42 join-cone coefficients and exact rank-one equivalences."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c

def inverse2(a):
    d=c.det2(a); assert d[0]>0
    return [[c.div(a[1][1],d),c.div(c.neg(a[0][1]),d)],
            [c.div(c.neg(a[1][0]),d),c.div(a[0][0],d)]]
def cone(k,p,b):
    a=[r[:2] for r in k[:2]]; ai=inverse2(a); r=[k[0][2][0],k[1][2][0]]
    beta=c.mm([[c.iv(x) for x in r]],ai)[0]
    s=c.sub(k[2][2],c.quad(ai,r))
    peff=c.sub(c.iv(p[2]),c.sumiv(c.mul(beta[i],c.iv(p[i])) for i in range(2)))
    denom=c.add(c.iv(b),c.quad(ai,p[:2]))
    updated=c.add(s,c.div(c.mul(peff,peff),denom))
    return updated,s,ai,beta
def controls():
    rows=[]
    for scale in [F(1),F(1,10**18)]:
        k=[[c.iv(x) for x in row] for row in [[2,1,scale],[1,2,scale],[scale,scale,scale**2/6]]]
        p=[F(1,2),F(1,3),scale]
        for multiplier in [F(99,100),F(1),F(101,100)]:
            b=F(74,81)*multiplier
            updated,s,ai,beta=cone(k,p,b); assert s==c.iv(-scale**2/2)
            new=[[c.add(k[i][j],c.iv(p[i]*p[j]/b)) for j in range(3)] for i in range(3)]
            leading=[r[:2] for r in new[:2]]; det=c.det3(new)
            r=[new[0][2][0],new[1][2][0]]
            direct=c.sub(new[2][2],c.quad(inverse2(leading),r))
            assert updated==direct and det==c.mul(c.det2(leading),direct)
            assert (updated[0]>0)==(multiplier<1) and (updated[0]==0)==(multiplier==1)
            # Solve K x=p by the block inverse independently of updating K.
            q=c.quad(ai,p[:2])[0]
            effective=p[2]-sum(beta[i][0]*p[i] for i in range(2))
            invquadratic=q+effective**2/s[0]
            assert det==c.mul(c.det3(k),c.iv(1+invquadratic/b))
            assert (invquadratic+b<0)==(updated[0]>0)
            assert all(new[i][i][0]>0 for i in range(3))
            rows.append(dict(scale=str(scale),denominator_multiplier=str(multiplier),
                exact_updated_margin=str(updated[0]),inverse_quadratic_plus_denominator=str(invquadratic+b)))
    # A frozen old negative witness passes while the new full matrix fails.
    k=[[c.iv(x) for x in row] for row in [[1,0,0],[0,1,0],[0,0,-1]]]
    p=[F(10),F(0),F(2)]; b=F(1)
    assert -1+p[2]**2/b>0
    margin,_,_,_=cone(k,p,b); assert margin[1]<0
    return dict(mixed_crossing_controls=rows,witness_pass_but_full_rank_one_join_fail=True)

def run(root):
    rows=[]
    for parity in ['even','odd']:
        name='RPB108_NF42_'+parity.upper()+'_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json'
        d=c.load(root,name); k=c.matrix(d['conditional_improved_joined_Schur_lower_matrix'])
        a=[r[:2] for r in k[:2]]; ai=inverse2(a)
        border=[[k[0][2]],[k[1][2]]]
        beta=c.mm(c.transpose(border),ai)[0]
        schur=c.sub(k[2][2],c.mm(c.mm(c.transpose(border),ai),border)[0][0])
        assert a[0][0][0]>0 and c.det2(a)[0]>0 and schur[1]<0
        assert c.overlap(schur,c.iv(d['improved_lower_condensed_margin']))
        rows.append(dict(parity=parity,leading_inverse=[[c.pair(x) for x in row] for row in ai],
            signed_border_center=[c.pair(x) for x in beta],negative_baseline_Schur=c.pair(schur),
            required_condensed_credit=c.pair(c.neg(schur)),
            standing_hypothesis=d['background_floor_hypothesis'],actual_new_source_row_certified=False))
    return dict(milestone='CC82',integration_parent='68d23fd4b746f9ae2496433d2ea34af38bd7b65d',
        read_only_source='f2c49f8d2ff95374d3ee2c3b1836ec772e4817dc',parity_checks=rows,
        exact_controls=controls(),simultaneous_six_direction_certificate=False,whole_aperture_positive=False)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    d=run(a.source_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    for row in d['parity_checks']:
        print(row['parity'],'required condensed credit',*[float(F(x)) for x in row['required_condensed_credit']])
