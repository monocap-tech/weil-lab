#!/usr/bin/env python3
"""Read-only candidate analytic + interval certificate of m>=3/1000 on gaps.

Source: pinned PR350 cluster boundaries; original multiplier explicitly stated
in PR346. Mathematical scope: 0..1300 complement of 107 original SM40
clusters, based on Binet first integral, digamma recurrence, complete seven
prime phases, and inherited |m''|<=2145. Uses mpmath.iv for enclosures;
not an independently replayed repository/GitHub certificate.
"""
import json, zipfile, hashlib, time
from fractions import Fraction as F
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
from mpmath import iv

iv.dps=32
LAMBDA=F(1,100);H=F(2145);T=F(1300)
N=16
A=iv.mpf(65)/4
P=iv.pi
PRIMES=[(2*iv.log(iv.mpf(p))/iv.sqrt(iv.mpf(n)),2*P*iv.log(iv.mpf(n)))
        for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]]
CONST=iv.log(P)+1/(2*A)

def dyadic(w):
    sign, mantissa, exponent, bc=w
    v=F((-1 if sign else 1)*mantissa)
    return v*(F(2)**exponent)

def ivp(x):
    return iv.mpf(x.numerator)/x.denominator

def bound(x):
    xx=ivp(x);y=P*xx;ys=y*y;z=A*A+ys
    v=iv.log(z)/2-A/(2*z)-CONST
    for k in range(N):
        ak=iv.mpf(4*k+1)/4
        v-=ak/(ak*ak+ys)
    for coef,phase in PRIMES:
        v-=coef*iv.cos(phase*xx)
    return dyadic(v._mpi_[0])

def main():
    z=zipfile.ZipFile(str(CUSTODY_ROOT / 'pr350-certificate.zip'))
    src=z.read('original_BS_pruned_rank_bound.json')
    assert hashlib.sha256(src).hexdigest()=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
    data=json.loads(src);clusters=data['cluster_witnesses']
    assert len(clusters)==107
    assert F(clusters[0]['lo'])==0 and F(clusters[-1]['hi'])<T
    gaps=[(F(a['hi']),F(b['lo'])) for a,b in zip(clusters,clusters[1:])]
    gaps.append((F(clusters[-1]['hi']),T))
    assert all(l<r for l,r in gaps) and len(gaps)==107
    values={};steps=0;smallest=None;worst=None;depth_max=0
    time_start=time.monotonic()
    def get(q):
        if q not in values:values[q]=bound(q)
        return values[q]
    # Finite bisection, all cutpoints exact rational; no point is discarded
    # based on approximate multiplier values.
    stack=[(l,r,0,k) for k,(l,r) in enumerate(gaps)]
    accepted=[]
    while stack:
        l,r,depth,k=stack.pop()
        assert depth<=32
        b0,b1=get(l),get(r)
        certified=min(b0,b1)-H*(r-l)**2/8
        if certified>LAMBDA:
            steps+=1;depth_max=max(depth,depth_max)
            if smallest is None or certified<smallest:
                smallest=certified;worst=(k,l,r,depth)
            accepted.append((l,r,certified,k,depth))
        else:
            mid=(l+r)/2
            stack.append((mid,r,depth+1,k));stack.append((l,mid,depth+1,k))
        if len(values)%10000==0 and len(values)>0 and len(values)%10000==0:
            pass
    # Confirm complete exact cover of every original gap via concatenation.
    accepted.sort()
    by_gap={k:[] for k in range(len(gaps))}
    for l,r,v,k,depth in accepted:by_gap[k].append((l,r))
    for k,((a,b),arr) in enumerate(zip(gaps,(by_gap[k] for k in range(len(gaps))))):
        assert arr and arr[0][0]==a and arr[-1][1]==b
        for (_,u),(v,_) in zip(arr,arr[1:]):assert u==v
    assert smallest>LAMBDA
    print('GAPS:',len(gaps),'verified segments:',steps,'evaluated endpoints:',len(values),'max depth:',depth_max)
    print('min certified m floor',float(smallest),'gap',worst[0], 'bounds',float(worst[1]),float(worst[2]))
    print('elapsed',round(time.monotonic()-time_start,3),'s')
    report={
     'scope':'107 original SM40 frequency gaps in [0,1300]; positive half-line only; complete other half by evenness',
     'input_sha256':'9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2',
     'analytic_digamma_method':'Binet first integral with 0 <= h(t) <= 1/2, recurrence shift by 16, certified below using interval expression',
     'term_count':N,'interval_backend':'mpmath.iv dps32, not independent native replay',
     'curvature_bound':str(H),'threshold':str(LAMBDA),
     'gaps':len(gaps),'segments_accepted':steps,'unique_endpoint_evaluations':len(values),
     'max_bisection_depth':depth_max,'smallest_accepted_floor':str(smallest),
     'smallest_floor_approx':float(smallest),
     'worst_interval':{'gap':worst[0],'lo':str(worst[1]),'hi':str(worst[2])},
     'full_original_signed_form_certified':False,
     'original_operator_domain_audit':'OPEN',
     'W_ODD_NEG':'OPEN'
    }
    Path(str(CUSTODY_ROOT / 'nf356_gap_001_report.json')).write_text(json.dumps(report,indent=2)+'\n')
    return report
if __name__=='__main__':main()
