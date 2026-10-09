#!/usr/bin/env python3
"""NF14: full original E64 native exact rational LDL, error and alternate.
Supply source JSON from certify_native_low48_nf14_106.py; never infer F112
or whole-domain sign from finite E48.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def verify(path,alternate=None):
    path=Path(path);raw=path.read_bytes();d=json.loads(raw)
    assert d['aperture']=='53/50' and d['dim']==64 and d['N']==390 and d['K']==340
    records=d['complete_form'];n=64;assert len(records)==1056
    grid=10**70
    M=[[F(0)]*n for _ in range(n)];err=F(0);checks=0
    for key,v in records.items():
        i,j=map(int,key.split(','));assert 0<=i<=j<n and (i+j)%2==0
        for comp in ('arch','prime','poles','full'):
            lo,hi=map(F,v[comp]);assert lo<=hi;checks+=1
        lo,hi=map(F,v['full'])
        assert lo<=sum(F(v[c][1]) for c in ('arch','prime','poles'))
        assert hi>=sum(F(v[c][0]) for c in ('arch','prime','poles'))
        mid=(lo+hi)/2;m=F((mid*grid).__floor__(),grid)
        M[i][j]=M[j][i]=m;err=max(err,abs(m-lo),abs(m-hi))
    assert all(M[i][j]==0 for i in range(n) for j in range(n) if (i+j)%2)
    assert all(M[i][j]==M[j][i] for i in range(n) for j in range(n))
    op_err=n*err;shift=F(1,10**30)
    assert op_err<F(1,10**52)
    blocks={}
    for parity in (0,1):
        ids=list(range(parity,n,2))
        A=[[M[i][j]-(shift if i==j else 0) for j in ids] for i in ids]
        for k in range(len(ids)):
            pivot=A[k][k]
            assert pivot>0,(parity,k,str(pivot))
            for i in range(k+1,len(ids)):
                for j in range(i,len(ids)):
                    A[i][j]=A[j][i]=A[i][j]-A[i][k]*A[k][j]/pivot
        blocks['even' if parity==0 else 'odd']=len(ids)
    assert shift-op_err>F(9,10**31)
    overlaps=None
    if alternate:
        alt=json.loads(Path(alternate).read_bytes())['complete_form']
        assert alt.keys()==records.keys()
        overlaps=0
        for key,v in records.items():
            for part in ('arch','prime','poles','full'):
                lo,hi=map(F,v[part]);a,b=map(F,alt[key][part])
                assert max(lo,a)<=min(hi,b),(key,part)
                overlaps+=1
    return dict(status='PASS',aperture='53/50',dimension=64,
        complete_original_component_intervals=checks,
        source_sha256=hashlib.sha256(raw).hexdigest(),
        whole_operator_error_upper=str(op_err),
        shifted_midpoint='1/100000000000000000000000000',
        exact_positive_parity_LDL_pivots=blocks,
        full_native_E64_physical_lower='9/1000000000000000000000000000000',
        independently_ordered_interval_intersections=overlaps,
        full_112_native=False,source_action_gram=False,
        corrected_infinite_Schur=False,whole_domain_positive=False,
        RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source_json');p.add_argument('--alternate')
    a=p.parse_args();print(json.dumps(verify(a.source_json,a.alternate),indent=2))
