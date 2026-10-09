#!/usr/bin/env python3
"""NF18 original signed mixed E112 -> e112/e113 rational witness audit.
114 native complete source entries, all four signed channels present.
No full F112 inverse/Gram or whole supported-domain positivity claim.
"""
import argparse,gzip,hashlib,json
from fractions import Fraction as F

E112_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
BOUNDARY_SHA='da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'
WITNESS_SHA='b3e23133db4562c1b28816e922f9c085899818399dcfcee74a323b4f6da10d5c'

def read(p):
    with (gzip.open(p,'rb') if str(p).endswith('.gz') else open(p,'rb')) as h:
        raw=h.read()
    return raw,json.loads(raw)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):
    return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def sqr(a):
    x,y=a
    if x>=0:return x*x,y*y
    if y<=0:return y*y,x*x
    return F(0),max(x*x,y*y)
def div(a,b):
    assert b[0]>0
    return a[0]/b[1],a[1]/b[0]
def I(record):return tuple(map(F,record['full']))

def verify(old_path,columns_path,witness_path):
    raw,d=read(old_path);rr,c=read(columns_path);ww,w=read(witness_path)
    assert hashlib.sha256(raw).hexdigest()==E112_SHA
    assert hashlib.sha256(rr).hexdigest()==BOUNDARY_SHA
    assert hashlib.sha256(ww).hexdigest()==WITNESS_SHA
    assert c['parent_sha256']==E112_SHA and c['aperture']=='53/50'
    assert c['new_columns']==[112,113] and len(c['original_full_source'])==114
    D=d['complete_form']; C=c['original_full_source'];den=F(w['coefficient_denominator'])
    assert len(D)==3192 and w['parent_source']==E112_SHA
    for k,lower in (('110,112',F(2,5)),('111,113',F(1,2))):
        assert I(C[k])[0]>lower
    assert F(1,4)>F(207,1000)*F(9,10**39)
    result=[]
    for name,j in (('even',112),('odd',113)):
        part=w['witnesses'][name]
        ix=part['indices'];x=[F(int(v))/den for v in part['numerators']]
        assert ix==list(range(0 if name=='even' else 1,112,2))
        assert len(ix)==len(x)==56
        norm=sum(t*t for t in x)
        assert F(999,1000)<norm<F(1001,1000)
        old=(F(0),F(0))
        for k,i in enumerate(ix):
            for l in range(k,len(ix)):
                j0=ix[l]
                old=add(old,scale(I(D[f'{min(i,j0)},{max(i,j0)}']),
                                      (2 if k!=l else 1)*x[k]*x[l]))
        mixed=(F(0),F(0))
        for i,t in zip(ix,x):mixed=add(mixed,scale(I(C[f'{i},{j}']),t))
        high=I(C[f'{j},{j}']);assert high[0]>3
        response=div(sqr(mixed),high)
        ratio=div(response,old)
        remaining=add(old,scale(response,F(-1)))
        assert old[0]>0 and remaining[0]>0
        if name=='even':
            assert F(3,1000)<ratio[0]<ratio[1]<F(4,1000)
            bound=['3/1000','4/1000']
        else:
            assert F(16,1000)<ratio[0]<ratio[1]<F(17,1000)
            bound=['16/1000','17/1000']
        result.append(dict(parity=name,outward_degree=j,
            certified_relative_reaction_bracket=bound,
            old_Rayleigh_midpoint_display=float(sum(old)/(2*norm)),
            mixed_original_pairing_midpoint_display=float(sum(mixed)/2),
            incoming_one_mode_response_display=float(sum(response)/(2*norm)),
            remaining_two_plane_positive=True))
    return dict(status='PASS',aperture='53/50',original_E112_sha=E112_SHA,
        complete_boundary_source_sha=BOUNDARY_SHA,witness_sha=WITNESS_SHA,
        full_original_boundary_entries=114,
        lower_bound_on_mixed_physical_norm='1/2',
        crude_absolute_Schur_norm_threshold_fails=True,
        parity_witness_results=result,
        complete_F112_inverse_Gram_certified=False,
        full_corrected_E112_Schur=False,whole_original_aperture_positive=False,
        RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('original_e112_json_gz')
    p.add_argument('complete_boundary_columns_json_gz')
    p.add_argument('critical_rational_witness_json')
    a=p.parse_args()
    print(json.dumps(verify(a.original_e112_json_gz,
            a.complete_boundary_columns_json_gz,
            a.critical_rational_witness_json),indent=2))
