#!/usr/bin/env python3
"""NF13 rigorous native low24/low32 interval sign and alternate-order check.

Input is exact Fraction interval JSON emitted by certify_native_low32_nf13_106.py.
The arithmetic lower bound is exact; mpmath midpoint eigenvalues are NOT used.
"""
import argparse,json,hashlib
from fractions import Fraction as F
from pathlib import Path

def verify(path,alternate=None):
    path=Path(path)
    raw=path.read_bytes();obj=json.loads(raw);D=obj['complete_form'];N=obj['dim']
    if N not in (24,32) or obj['aperture']!='53/50':
        raise ValueError("Wrong target aperture/dimension")
    if (obj['N'],obj['K']) not in ((190,160),(210,180)):
        raise ValueError("Unaudited source truncation orders")
    expected=(N//2)*(N//2+1)
    assert len(D)==expected
    q=[[F(0)]*N for _ in range(N)]
    G=10**36;worst=F(0);width=F(0);components=0
    for key,v in D.items():
        i,j=map(int,key.split(','))
        assert 0<=i<=j<N and (i+j)%2==0
        # Enclose the original signed entry by paying ALL FOUR individual
        # archimedean, prime, Hermitian-pole, and total term intervals.
        for component in ('arch','prime','poles','full'):
            l,h=map(F,v[component]);assert l<=h;components+=1
        lower,upper=map(F,v['full'])
        parts=[tuple(map(F,v[c])) for c in ('arch','prime','poles')]
        assert lower<=sum(x[1] for x in parts)
        assert upper>=sum(x[0] for x in parts)
        midpoint=(lower+upper)/2
        center=F((midpoint*G).__floor__(),G)
        worst=max(worst,abs(center-lower),abs(center-upper))
        width=max(width,upper-lower)
        q[i][j]=q[j][i]=center
    assert all(q[i][j]==0 for i in range(N) for j in range(N) if (i+j)%2)
    operator_error=N*worst
    shift={24:F(1,10**18),32:F(2,10**22)}[N]
    assert operator_error<shift
    pivot_counts={}
    for parity in (0,1):
        idx=list(range(parity,N,2));n=len(idx)
        m=[[q[i][j]-(shift if i==j else 0) for j in idx] for i in idx]
        for k in range(n):
            p=m[k][k]
            if p<=0:raise AssertionError(("nonpositive shifted LDL pivot",N,parity,k,str(p)))
            for i in range(k+1,n):
                for j in range(i,n):
                    m[i][j]=m[j][i]=m[i][j]-m[i][k]*m[k][j]/p
        pivot_counts['even' if parity==0 else 'odd']=n
    checks=None
    if alternate:
        B=json.loads(Path(alternate).read_bytes())
        assert B['aperture']=='53/50' and B['dim']==N
        assert B['complete_form'].keys()==D.keys()
        checks=0
        for key,v in D.items():
            for c in ('arch','prime','poles','full'):
                l,h=map(F,v[c]);l2,h2=map(F,B['complete_form'][key][c])
                assert max(l,l2)<=min(h,h2),(key,c)
                checks+=1
    conservative={24:F(9,10**19),32:F(1,10**22)}[N]
    actual_lower=shift-operator_error
    assert actual_lower>conservative
    return dict(status='PASS',target_aperture='53/50',dimension=N,
      exponent_order=obj['N'],Bernoulli_pairs=obj['K'],
      original_arch_prime_pole_entry_count=components,
      source_archive_sha256=hashlib.sha256(raw).hexdigest(),
      max_native_interval_width=str(width),
      operator_error_upper=str(operator_error),
      shifted_midpoint=str(shift),
      positive_shifted_exact_pivots=pivot_counts,
      actual_finite_lower=str(actual_lower),
      conservative_finite_lower=str(conservative),
      alternative_order_overlap_tests=checks,
      entire_112_native_matrix=False,corrected_full_source_Schur=False,
      whole_aperture_positive=False,Lean_certified=False)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('source_json')
    parser.add_argument('--alternate')
    a=parser.parse_args()
    print(json.dumps(verify(a.source_json,a.alternate),indent=2))
