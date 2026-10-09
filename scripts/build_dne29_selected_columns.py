#!/usr/bin/env python3
"""Exact selected NF38 columns from the pinned NF41 frozen base columns."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse,json,hashlib,gzip,base64
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def root(x):
    s=10**160;n=isqrt(x.numerator*s*s//x.denominator);v=F(n+1,s);assert v*v>x;return v
def run(base,trial,packet):
    (b,bh),(t,th),(p,ph)=map(read,(base,trial,packet));assert b['parity']==t['parity']==p['parity'];assert p['fixed_trial_sha256']==th
    cols=b['frozen_joined_polynomial_columns'];ids=t['merged_target_indices'];h=list(map(F,t['exact_moved_target_coefficients']))
    reconstructed={}
    for col,a in zip(cols,h):
        for j,v in zip(col['indices'],map(F,col['coefficients'])):reconstructed[j]=reconstructed.get(j,F(0))+a*v
    assert [reconstructed.get(j,F(0)) for j in ids]==list(map(F,t['merged_target_coefficients']))
    z0=list(map(F,t['old_correction_coefficients']));z1=list(map(F,t['fixed_rational_second_correction_coefficients']));C=[list(map(F,row)) for row in p['selected_rational_joint_functionals']]
    assert sum(a*b for a,b in zip(z0,z1))==0 and all(j>=112 for j in t['correction_indices'])
    selected=[]
    for i,col in enumerate(cols):
        ii=col['indices'];cc=list(map(F,col['coefficients']));assert sum(v*v for v in cc)<=F(p['source_norm_mass_upper'][i])**2
        merged=dict(zip(ii,cc));retained={j:v for j,v in merged.items() if j<112}
        for j,a,bv in zip(t['correction_indices'],z0,z1):merged[j]=merged.get(j,F(0))-C[0][i]*a-C[1][i]*bv
        assert retained=={j:v for j,v in merged.items() if j<112}
        ii=sorted(merged);cc=[merged[j] for j in ii];mass=sum(v*v for v in cc)
        selected.append(dict(indices=ii,coefficients=list(map(str,cc)),exact_mass_squared=str(mass),norm_upper=str(root(mass))))
    return dict(stage='DNE29',parity=b['parity'],base_source_commit=b['source_commit'],input_sha256=[bh,th,ph],
        frame_rule='selected_i=NF41_base_i-z0*C[0,i]-z1*C[1,i]',
        base_witness_polynomial_exactly_matches_NF38_trial=True,retained_components_unchanged=True,columns=selected)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ['base','trial','packet','output']:p.add_argument(k)
    a=p.parse_args();r=run(a.base,a.trial,a.packet);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(r['parity'],'exact selected columns constructed')
