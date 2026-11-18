#!/usr/bin/env python3
"""Produce a compact 64-digit rational congruence witness for original H.

The preconditioner is untrusted search output from the NF656 interval LDL.
All claims require independent verification by verify_nf657_compact_congruence.py.
"""
import argparse
import gzip
import hashlib
import io
import json
import sys
import tempfile
import zipfile
from pathlib import Path
from verify_nf656_original_physical_gram_interval_ldl import (
    source_matrix, interval_ldl, inverse_lower_frob_bound
)

sys.set_int_max_str_digits(0)
Q=10**2600
S=10**64
INDICES=list(range(14))+[241]
N=len(INDICES)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def ceildiv(x,y):
    return -((-x)//y)

def mm(a,b):
    cols=list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col)) for col in cols] for row in a]

def trans(a):
    return list(map(list,zip(*a)))

def generate(source,output):
    with zipfile.ZipFile(source) as z:
        raw=z.read('nf631-widened-entries.jsonl.gz')
        summary=z.read('nf631-widening.json')
        m=json.loads(summary)
        assert m['schema']=='NF631-reference-widening-v1'
        assert sha(raw)==m['widened_entry_sha256']
    with tempfile.TemporaryDirectory() as work:
        p=Path(work)
        entries=p/'nf631-widened-entries.jsonl.gz'
        manifest=p/'nf631-widening.json'
        entries.write_bytes(raw)
        manifest.write_bytes(summary)
        matrix,originals,meta=source_matrix(entries,manifest)
        pivots,L=interval_ldl(matrix)
        _,K=inverse_lower_frob_bound(L)
    assert len(originals)==120 and all(x[0]>0 for x in pivots)
    factor=10**96
    # Round the interval midpoint to a fixed, untrusted rational K.
    k=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            lo,hi=K[i][j]
            k[i][j]=(lo+hi+factor)//(2*factor)
    assert all(k[i][i]==S for i in range(N))
    M=[[None]*N for _ in range(N)]
    R=[[None]*N for _ in range(N)]
    loc={j:i for i,j in enumerate(INDICES)}
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:
        h=json.loads(next(f))
        assert h['scale']=='10^2600'
        assert h['original_entry_sha256']==meta['original_entry_sha256']
        for i,line in enumerate(f):
            if i not in loc:continue
            row=json.loads(line)
            for j in INDICES:
                if j>i:continue
                mid,rad=map(int,row['H_lower'][j])
                assert rad>=0
                a,b=loc[i],loc[j]
                M[a][b]=M[b][a]=mid
                R[a][b]=R[b][a]=rad
    assert all(x is not None for row in M for x in row)
    c=[[0]*N for _ in range(N)]
    e=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lo=(M[i][j]-R[i][j])*S//Q
            hi=ceildiv((M[i][j]+R[i][j])*S,Q)
            c[i][j]=(lo+hi)//2
            e[i][j]=max(c[i][j]-lo,hi-c[i][j])
    ac=[[abs(x) for x in row] for row in k]
    bc=mm(mm(k,c),trans(k))
    br=mm(mm(ac,e),trans(ac))
    margins=[
        bc[i][i]-br[i][i]-
        sum(abs(bc[i][j])+br[i][j] for j in range(N) if j!=i)
        for i in range(N)
    ]
    kn=sum(x*x for row in k for x in row)
    gap=min(margins)*10**60-S*kn
    assert all(d>0 for d in margins) and gap>0
    cert={
        'schema':'NF657-original-15-source-compact-congruence-v1',
        'indices':INDICES,
        'source_archive_sha256':sha(source.read_bytes()),
        'widened_entry_sha256':meta['widened_entry_sha256'],
        'original_entry_sha256':meta['original_entry_sha256'],
        'S':'10^64','Q':'10^2600',
        'K_scaled':[[str(x) for x in row] for row in k],
        'H_center_scaled':[[str(x) for x in row] for row in c],
        'H_radius_scaled':[[str(x) for x in row] for row in e],
        'dominance_margin_scaled_numerator':[str(x) for x in margins],
        'K_norm_sq_scaled_numerator':str(kn),
        'coercivity_integer_margin':str(gap),
        'coercivity_bound':'1/10^60',
        'scope':'exact external witness; Lean H membership and diagonal-congruence transfer separate'
    }
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(cert,indent=2)+'\n')
    print('NF657 emitted 120 source enclosures, 15 strict dominance margins and 10^-60 gate')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('archive',type=Path)
    p.add_argument('output',type=Path)
    a=p.parse_args()
    generate(a.archive,a.output)
