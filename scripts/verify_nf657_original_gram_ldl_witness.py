#!/usr/bin/env python3
"""Independent rational verifier for the NF657 original 15-source LDL witness.

Checks all proposed intervals using exact fractions, without importing
the witness producer. The scope is conditional on the analytic H entries
being inside the original NF631 entry enclosures.
"""
import argparse
import gzip
import hashlib
import io
import json
import sys
import zipfile
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)

def plus(a,b):
    return a[0]+b[0],a[1]+b[1]

def minus(a,b):
    return a[0]-b[1],a[1]-b[0]

def times(a,b):
    vals=[x*y for x in a for y in b]
    return min(vals),max(vals)

def over(a,b):
    assert b[0]>0
    vals=[x/y for x in a for y in b]
    return min(vals),max(vals)

def encloses(outer,inner):
    return outer[0]<=inner[0] and inner[1]<=outer[1]

def verify(witness,archive):
    w=json.loads(witness.read_text())
    assert w['schema']=='NF657-original-physical-15-source-interval-LDL-witness-v1'
    indices=list(range(14))+[241]
    n=len(indices)
    assert w['index']==indices and all(len(w[k])==n for k in ('A','L','K','D'))
    assert w['S']=='10^160' and w['Q']=='10^2600'
    scale=10**160
    Q=10**2600
    with zipfile.ZipFile(archive) as z:
        assert hashlib.sha256(archive.read_bytes()).hexdigest()==w['source_sha256']['archive']
        meta=json.loads(z.read('nf631-widening.json'))
        raw=z.read('nf631-widened-entries.jsonl.gz')
        assert hashlib.sha256(raw).hexdigest()==w['source_sha256']['entries']==meta['widened_entry_sha256']
        assert w['source_sha256']['original_entries']==meta['original_entry_sha256']
        A=[[None]*n for _ in range(n)]
        loc={v:k for k,v in enumerate(indices)}
        with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:
            header=json.loads(next(f))
            assert header['scale']=='10^2600'
            assert header['original_entry_sha256']==meta['original_entry_sha256']
            for i,line in enumerate(f):
                row=json.loads(line)
                if i not in loc:
                    continue
                assert row['row']==i
                for j in indices:
                    if j>i:
                        continue
                    m,r=map(int,row['H_lower'][j])
                    assert r>=0
                    A[loc[i]][loc[j]]=A[loc[j]][loc[i]]=(F(m-r,Q),F(m+r,Q))
    def parse(v):
        assert isinstance(v,list) and len(v)==2
        a,b=map(int,v)
        assert a<=b
        return F(a,scale),F(b,scale)
    AA=[[parse(x) for x in row] for row in w['A']]
    DD=[parse(v) for v in w['D']]
    LL=[[parse(v) if v is not None else None for v in row] for row in w['L']]
    KK=[[parse(v) if v is not None else None for v in row] for row in w['K']]
    for i in range(n):
        for j in range(n):
            assert AA[i][j]==AA[j][i]
            assert A[i][j] is not None and encloses(AA[i][j],A[i][j])
            if i==j:
                assert LL[i][j]==KK[i][j]==(F(1),F(1))
            elif i<j:
                assert LL[i][j] is None and KK[i][j] is None
            else:
                assert LL[i][j] is not None and KK[i][j] is not None
    # These are exact-rational interval inclusions, not the producer's
    # outward fixedpoint floor/ceil operations. Proposals are untrusted.
    for k in range(n):
        v=AA[k][k]
        for j in range(k):
            v=minus(v,times(times(LL[k][j],LL[k][j]),DD[j]))
        assert encloses(DD[k],v) and DD[k][0]>0,(k,'pivot')
        for i in range(k+1,n):
            v=AA[i][k]
            for j in range(k):
                v=minus(v,times(times(LL[i][j],LL[k][j]),DD[j]))
            assert encloses(LL[i][k],over(v,DD[k])),(i,k,'L')
    for i in range(n):
        for j in range(i-1,-1,-1):
            v=(F(0),F(0))
            for k in range(j,i):
                v=plus(v,times(LL[i][k],KK[k][j]))
            assert encloses(KK[i][j],(-v[1],-v[0])),(i,j,'inverse L')
    upper=0
    for i in range(n):
        for j in range(i+1):
            lo,hi=map(int,w['K'][i][j])
            upper+=max(abs(lo),abs(hi))**2
    dmin=min(int(v[0]) for v in w['D'])
    margin=dmin*scale*10**60-upper
    assert upper==int(w['K_frob_sq_bound_scaled'])
    assert dmin==int(w['minimum_d_lower_scaled'])
    assert margin==int(w['coercivity_integer_margin']) and margin>0
    assert w['coercivity_bound']=='1/10^60'
    print('NF657 exact rational witness verification PASS: 120 entries, 15 D, 105 L, 105 K')
    print('NF657 strict 10^-60 conditional coercivity PASS')
    print('NF657 original H inclusion and formal Lean theorem remain OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('witness',type=Path)
    p.add_argument('archive',type=Path)
    a=p.parse_args()
    verify(a.witness,a.archive)
