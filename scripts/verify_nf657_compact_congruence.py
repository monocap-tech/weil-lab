#!/usr/bin/env python3
"""Independent exact integer checker for NF657's compact congruence certificate.

No dependency on the certificate producer or LDL library. The checker
enforces exact original-entry inclusion, strict transformed diagonal
dominance and a 10^-60 quadratic bound. Lean H membership/transfer remain
separate obligations.
"""
import argparse
import gzip
import hashlib
import io
import json
import sys
import zipfile
from pathlib import Path

sys.set_int_max_str_digits(0)
Q=10**2600
S=10**64

def sha(b):
    return hashlib.sha256(b).hexdigest()

def check(certificate,source):
    w=json.loads(certificate.read_text())
    I=list(range(14))+[241]
    n=len(I)
    assert w['schema']=='NF657-original-15-source-compact-congruence-v1'
    assert w['indices']==I and w['S']=='10^64' and w['Q']=='10^2600'
    K=[[int(x) for x in row] for row in w['K_scaled']]
    C=[[int(x) for x in row] for row in w['H_center_scaled']]
    R=[[int(x) for x in row] for row in w['H_radius_scaled']]
    assert all(len(a)==n and all(len(row)==n for row in a) for a in (K,C,R))
    assert all(K[i][j]==(S if i==j else 0) for i in range(n) for j in range(i,n))
    assert all(C[i][j]==C[j][i] and R[i][j]==R[j][i]>=0
               for i in range(n) for j in range(n))
    assert sha(source.read_bytes())==w['source_archive_sha256']
    with zipfile.ZipFile(source) as z:
        meta=json.loads(z.read('nf631-widening.json'))
        raw=z.read('nf631-widened-entries.jsonl.gz')
        assert sha(raw)==meta['widened_entry_sha256']==w['widened_entry_sha256']
        assert meta['original_entry_sha256']==w['original_entry_sha256']
        indices={x:i for i,x in enumerate(I)}
        count=0
        with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:
            h=json.loads(next(f))
            assert h['scale']=='10^2600'
            assert h['original_entry_sha256']==meta['original_entry_sha256']
            for i,line in enumerate(f):
                if i not in indices:continue
                d=json.loads(line)
                assert d['row']==i
                for j in I:
                    if j>i:continue
                    m,r=map(int,d['H_lower'][j])
                    assert r>=0
                    a,b=indices[i],indices[j]
                    lo,hi=C[a][b]-R[a][b],C[a][b]+R[a][b]
                    assert lo*Q <= (m-r)*S and (m+r)*S <= hi*Q,(i,j,'source enclosure')
                    count+=1
    assert count==120
    # Independent four-index expression, not the producer's matrix
    # multiplication. This is an exact signed integer calculation.
    BC=[[0]*n for _ in range(n)]
    BR=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mid=rad=0
            for p in range(n):
                for q in range(n):
                    coeff=K[i][p]*K[j][q]
                    mid+=coeff*C[p][q]
                    rad+=abs(coeff)*R[p][q]
            BC[i][j]=mid
            BR[i][j]=rad
    assert all(BC[i][j]==BC[j][i] and BR[i][j]==BR[j][i]>=0
               for i in range(n) for j in range(n))
    margins=[]
    for i in range(n):
        d=BC[i][i]-BR[i][i]-sum(
            abs(BC[i][j])+BR[i][j] for j in range(n) if i!=j)
        assert d==int(w['dominance_margin_scaled_numerator'][i]) and d>0,(i,'dominance')
        margins.append(d)
    normsq=sum(x*x for row in K for x in row)
    assert normsq==int(w['K_norm_sq_scaled_numerator'])
    gap=min(margins)*10**60-S*normsq
    assert gap==int(w['coercivity_integer_margin']) and gap>0
    assert w['coercivity_bound']=='1/10^60'
    print('NF657 PASS: 120 source entries, 225 transformed bounds, 15 diagonal-dominance margins')
    print('NF657 external 10^-60 conditional quadratic coercivity PASS')
    print('NF657 actual analytic H inclusion and formal Lean positivity transfer are separate')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('certificate',type=Path)
    p.add_argument('source',type=Path)
    a=p.parse_args()
    check(a.certificate,a.source)
