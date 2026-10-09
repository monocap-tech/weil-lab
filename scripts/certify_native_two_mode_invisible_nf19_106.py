#!/usr/bin/env python3
"""NF19 exact-rational original E112 3D low-energy certificate.

The 56x3 rational seeds may be selected numerically, but every result
below is proved using the authenticated original E112 signed rational
interval matrix. Rank(2 measured exterior source forms)<=2 then gives
an existential exact two-boundary-invisible retained vector per parity.
Neither this nor the finite Ritz sign is a whole Weil null.
"""
import argparse,gzip,json,hashlib
from pathlib import Path
from fractions import Fraction as F
OLD_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
SEEDS_SHA='2dca6436bf41d27f906ec02d0f2728b5da63919757136ec6fe5a0aef6b59ee48'

def pivots_positive(M):
    a=[row[:] for row in M];pivots=0
    for k in range(len(a)):
        pivot=a[k][k];assert pivot>0,('Cannot certify three-space',k)
        pivots+=1
        for i in range(k+1,len(a)):
            for j in range(i,len(a)):
                a[i][j]=a[j][i]=a[i][j]-a[i][k]*a[k][j]/pivot
    return pivots

def bound(a,t):
    lo,hi=a
    return (lo*t,hi*t) if t>=0 else (hi*t,lo*t)

def verify(e112,seeds):
    with gzip.open(e112,'rb') as f:raw=f.read()
    assert hashlib.sha256(raw).hexdigest()==OLD_SHA
    seed_raw=Path(seeds).read_bytes()
    assert hashlib.sha256(seed_raw).hexdigest()==SEEDS_SHA
    source=json.loads(raw)['complete_form'];s=json.loads(seed_raw)
    assert s['E112_source_sha256']==OLD_SHA
    den=F(s['denominator']);result=[]
    for name,eps in [('even',F(1,10**20)),('odd',F(1,10**17))]:
        rec=s['parities'][name]
        ix=rec['indices'];V=[[F(int(x))/den for x in row] for row in rec['vectors']]
        assert len(ix)==56 and len(V)==3 and all(len(v)==56 for v in V)
        assert ix==list(range(0 if name=='even' else 1,112,2))
        physical=[[sum((V[i][k]*V[j][k] for k in range(56)),F(0))
                   for j in range(3)] for i in range(3)]
        native=[[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(i,3):
                lo=hi=F(0)
                for a,ia in enumerate(ix):
                    for b,ib in enumerate(ix):
                        t=V[i][a]*V[j][b]
                        if t==0:continue
                        x,y=map(F,source[f'{min(ia,ib)},{max(ia,ib)}']['full'])
                        l,u=bound((x,y),t);lo+=l;hi+=u
                assert lo<=hi
                native[i][j]=native[j][i]=(lo,hi)
        corrected=[[F(0)]*3 for _ in range(3)];max_halfwidth=F(0)
        for i in range(3):
            for j in range(3):
                l,u=native[i][j];corrected[i][j]=eps*physical[i][j]-(l+u)/2
                max_halfwidth=max(max_halfwidth,(u-l)/2)
        operator_error=3*max_halfwidth;shift=eps/10
        assert operator_error<shift/100
        test=[[corrected[i][j]-(shift if i==j else 0) for j in range(3)]
              for i in range(3)]
        assert pivots_positive(test)==3
        # For EVERY nonzero vector in the 3D span, original Q<eps*physical.
        # Since at most two independent high pairings are observed, their
        # common kernel on the 3D subspace has dimension >=1.
        result.append(dict(parity=name,source_dim=3,low_energy_threshold=str(eps),
           positive_exact_pivots=3,source_interval_operator_error=str(operator_error),
           certified_invisible_to_both_high_modes=True,
           original_positive_energy_from_NF17=True,
           invisible_vector_explicitly_computed=False))
    return dict(status='PASS',milestone='NF19',aperture='53/50',
       original_E112_sha256=OLD_SHA,rational_seeds_sha256=SEEDS_SHA,
       results=result,first_two_high_response_lower_frame_claim=False,
       whole_F112_source_response_evaluated=False,
       original_Weil_null_claim=False,whole_aperture_positive=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('original_E112_archive');p.add_argument('rational_seed_json')
    p.add_argument('--output');a=p.parse_args()
    r=json.dumps(verify(a.original_E112_archive,a.rational_seed_json),indent=2)+'\n'
    if a.output:Path(a.output).write_text(r)
    print(r)
