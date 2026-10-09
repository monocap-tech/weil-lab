#!/usr/bin/env python3
"""NF17 exact original E112 native interval and shifted parity sign audit.
Requires complete generated E112 source and authenticated E96 prefix.
Finite E112 result ONLY; no corrected infinite F112 Schur asserted.
"""
from fractions import Fraction as F
import gzip,json,hashlib,argparse,time
def load(path):
    with gzip.open(path,'rb') if path.endswith('.gz') else open(path,'rb') as h:
        raw=h.read()
    return raw,json.loads(raw)
def validate(e112,e96):
    t=time.monotonic();raw,d=load(e112);oldraw,old=load(e96)
    oldsha=hashlib.sha256(oldraw).hexdigest()
    assert oldsha=='aff17c786d41287f077680f412e4b2c14d59fdebacbaf11272d23033aee6e3ac'
    assert d['aperture']=='53/50' and d['dim']==112 and d['N']==720 and d['K']==620
    assert old['aperture']=='53/50' and old['dim']==96
    D=d['complete_form'];prior=old['complete_form']
    assert len(D)==3192 and len(prior)==2352
    assert all(D[k]==v for k,v in prior.items())
    n=112;M=[[F(0)]*n for _ in range(n)]
    g=10**100;error=F(0);width=F(0);checks=0
    for name,parts in D.items():
        i,j=map(int,name.split(','));assert 0<=i<=j<n and (i+j)%2==0
        assert set(parts)=={'arch','prime','poles','full'}
        for kind in ('arch','prime','poles','full'):
            a,b=map(F,parts[kind]);assert a<=b;checks+=1
        lo,hi=map(F,parts['full'])
        assert lo<=sum(F(parts[k][1]) for k in ('arch','prime','poles'))
        assert hi>=sum(F(parts[k][0]) for k in ('arch','prime','poles'))
        middle=(lo+hi)/2;center=F((middle*g).__floor__(),g)
        error=max(error,abs(center-lo),abs(center-hi))
        width=max(width,hi-lo);M[i][j]=M[j][i]=center
    assert checks==12768
    assert all(M[i][j]==0 for i in range(n) for j in range(n) if (i+j)%2)
    op_error=n*error
    # Test shifts from stronger to weaker; any failed test is inconclusive.
    selected=None;counts=None
    for power in (38,40,42,44,46,48,50,52,55,58,60):
        shift=F(1,10**power)
        if shift<=op_error:continue
        passes={};ok=True
        for parity in (0,1):
            ix=list(range(parity,n,2));m=len(ix)
            A=[[M[i][j]-(shift if i==j else 0) for j in ix] for i in ix]
            count=0
            for k in range(m):
                pivot=A[k][k]
                if pivot<=0:ok=False;break
                count+=1
                for i in range(k+1,m):
                    for j in range(i,m):
                        A[i][j]=A[j][i]=A[i][j]-A[i][k]*A[k][j]/pivot
            passes['even' if parity==0 else 'odd']=count
            if not ok:break
        if ok:
            selected=shift;counts=passes;break
    status='PASS finite E112 sign' if selected is not None else 'INCONCLUSIVE finite E112 sign'
    return dict(status=status,aperture='53/50',dimension=n,
        E112_source_sha256=hashlib.sha256(raw).hexdigest(),
        E96_prefix_sha256=oldsha,complete_original_signed_entries=3192,
        new_complete_signed_entries=840,all_component_interval_checks=checks,
        maximum_source_interval_width=str(width),
        whole_matrix_operator_error=str(op_error),
        tested_positive_shift=str(selected) if selected else None,
        exact_positive_parity_pivots=counts,
        certified_finite_L2_lower=str(selected-op_error) if selected else None,
        whole_original_aperture_positive=False,corrected_infinite_F112_Schur=False,
        original_positive_source_action_Gram=False,Lean_certified=False,
        validation_seconds=round(time.monotonic()-t,3))
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('e112');a.add_argument('e96')
    args=a.parse_args()
    print(json.dumps(validate(args.e112,args.e96),indent=2))
