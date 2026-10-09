#!/usr/bin/env python3
"""Exact necessary source-credit targets and collective sign controls."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def certify(raw):
    k=F(207,1000);rows=[]
    for b in raw:
        c=json.loads(b);q=list(map(F,c['original_native_energy_Gram'][2][2]));g=list(map(F,c['original_complete_source_Gram'][2][2]))
        assert 0<q[0]<=q[1] and 0<g[0]<=g[1]
        negative_upper=q[1]-g[0]/k;assert negative_upper<0
        required=[g[0]/k-q[1],g[1]/k-q[0]]
        fraction=[1-k*q[1]/g[0],1-k*q[0]/g[1]]
        assert 0<fraction[0]<=fraction[1]<1
        crosses=c['original_complete_source_Gram']
        signs=[]
        for i in range(2):
            a,z=map(F,crosses[i][2]);assert a<=z
            signs.append('positive' if a>0 else 'negative' if z<0 else 'unresolved')
        rows.append(dict(parity=c['parity'],sufficient_probe_value_upper=str(negative_upper),
            necessary_inverse_response_credit_interval=list(map(str,required)),
            necessary_fraction_of_floor_response_credit_interval=list(map(str,fraction)),
            signed_physical_source_cross_signs=signs,scalar_targets_are_not_collective_sufficiency=True))
    # D=I, R=I, floor k0=1/2. S=D-R*R/k0=-I.
    # Delta=[[1+eps,b],[b,1+eps]]; C^-1=2I-Delta.
    # Both Delta and C^-1 are positive, and C>=k0 I.
    # Actual Schur=Delta-I has strictly positive diagonals throughout.
    eps=F(1,100);controls=[]
    for b in [F(99,10000),eps,F(101,10000)]:
        delta_diag=1+eps;cinv_diag=1-eps
        assert delta_diag>b and cinv_diag>b and cinv_diag+b<2
        det=eps**2-b**2
        controls.append(dict(mixed_credit=str(b),exact_actual_Schur_determinant=str(det),
            actual_physical_retained_ground_level=str(eps-b),strict_scalar_credit_targets_pass=True,
            credit_positive_definite=True,high_floor_hypothesis_pass=True))
    # At b=eps the original joint block has null vector (1,-1,-1,1).
    a=1-eps;den=a*a-eps*eps
    C=[[a/den,eps/den],[eps/den,a/den]]
    joint=[[F(1),F(0),F(1),F(0)],[F(0),F(1),F(0),F(1)],
           [F(1),F(0),*C[0]],[F(0),F(1),*C[1]]]
    null=[F(1),F(-1),F(-1),F(1)]
    assert all(sum(v*z for v,z in zip(row,null))==0 for row in joint)
    # C>0 and Schur=[[eps,eps],[eps,eps]]>=0 prove joint>=0.
    assert a>eps and den>0
    levels=[dict(whole_mass_shift=str(s),exact_ground_level=str(s)) for s in [F(1,1000),F(1,10),F(2)]]
    return dict(milestone='CC75',certificate_sha256=[hashlib.sha256(b).hexdigest() for b in raw],
        necessary_probe_targets=rows,exact_collective_credit_crossing_controls=controls,
        positive_whole_mass_controls=levels,full_Weil_nonimplication_claimed=False,
        collective_credit_certified_for_actual_Weil=False,whole_aperture_positive=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('even');p.add_argument('odd');p.add_argument('--output',required=True);a=p.parse_args()
    r=certify([Path(a.even).read_bytes(),Path(a.odd).read_bytes()])
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
