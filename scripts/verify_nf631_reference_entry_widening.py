#!/usr/bin/env python3
"""Pay the difference between NF622 external entries and the Lean reference.

Reference arithmetic follows NF622PairRect: round the two coefficient
rectangles, multiply/round the coefficients, then multiply/round the
moment. All center/radius units are 1/Q. This external check proposes
radii; the actual Lean widening propositions must still be proved.
"""
import argparse
import gzip
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_nf620_physical_key_tables import Q, exact, zmul, zadd, ZERO
from verify_nf622_physical_entry_reassembly import selected, critical, read_shards, moment

sys.set_int_max_str_digits(0)

def reference_entry(data,a,b):
    out=(ZERO,ZERO)
    for h,f,n,c,d in a:
        for j,g,m,e,v in b:
            coeff=zmul((exact(c),exact(d)),(exact(e),exact(v)))
            term=zmul(coeff,moment(data,h+j,f+g,n+m))
            out=zadd(out,term)
    assert abs(out[1][0])<=out[1][1]
    return out[0]

def widen(old,new):
    m,r=map(int,old)
    n,s=map(int,new)
    assert r>=0 and s>=0
    return m,max(r,abs(n-m)+s)

def filehash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def self_test():
    # Independently implement reference ball rounding as rational
    # arithmetic, including the +1 rounding fee for all products.
    def bf(a,b):
        x,u=map(lambda t:F(t,Q),a)
        y,v=map(lambda t:F(t,Q),b)
        m=x*y*Q
        r=(abs(x)*v+abs(y)*u+u*v)*Q
        return m.numerator//m.denominator,-(-r.numerator//r.denominator)+1
    def plus(a,b): return a[0]+b[0],a[1]+b[1]
    def zf(a,b):
        u=bf(a[1],b[1])
        return plus(bf(a[0],b[0]),(-u[0],u[1])),plus(bf(a[0],b[1]),bf(a[1],b[0]))
    for k in range(1,101):
        a=(exact(F(k-51,97)),exact(F(-k,103)))
        b=(exact(F(k,131)),exact(F(31-k,107)))
        assert zmul(a,b)==zf(a,b)
        old=(k-51,k%5); new=(31-k,k%7)
        m,r=widen(old,new)
        assert m==old[0] and r>=old[1] and abs(m-new[0])+new[1]<=r
        assert r==max(old[1],abs(m-new[0])+new[1])
    print('NF631 100 exact rational rounding/widening self-tests PASS')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path)
    p.add_argument('--shards',type=Path)
    p.add_argument('--entries',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--summary',type=Path)
    p.add_argument('--self-test',action='store_true')
    a=p.parse_args()
    if a.self_test:
        self_test(); return
    assert a.root and a.shards and a.entries and a.output and a.summary
    sourcehash=filehash(a.entries)
    data=read_shards(a.root,a.shards)
    S,C=selected(a.root),critical(a.root)
    assert len(S)==242 and len(C)==4
    oldmaxH=oldmaxV=maxH=maxV=changesH=changesV=0
    with gzip.open(a.entries,'rt') as src,gzip.open(a.output,'wt') as dst:
        def emit(o): dst.write(json.dumps(o,separators=(',',':'))+'\n')
        head=json.loads(next(src))
        assert head['schema']=='NF622-original-physical-entry-balls-v1' and head['scale']=='10^2600'
        emit({**head,'evidence':'NF631 external reference-rounding paid widening, not Lean custody',
              'original_entry_sha256':sourcehash})
        for i in range(242):
            row=json.loads(next(src))
            assert row['row']==i and len(row['H_lower'])==i+1 and len(row['V'])==4
            H=[]; V=[]
            for j,x in enumerate(row['H_lower']):
                oldrad=int(x[1]); oldmaxH=max(oldmaxH,oldrad)
                v=widen(x,reference_entry(data,S[i],S[j]))
                maxH=max(maxH,v[1]); changesH+=v[1]>oldrad
                H.append(list(map(str,v)))
            for j,x in enumerate(row['V']):
                oldrad=int(x[1]); oldmaxV=max(oldmaxV,oldrad)
                v=widen(x,reference_entry(data,S[i],C[j]))
                maxV=max(maxV,v[1]); changesV+=v[1]>oldrad
                V.append(list(map(str,v)))
            emit({'row':i,'H_lower':H,'V':V})
            if i%20==0: print('NF631 reference widening row',i,flush=True)
        assert next(src,None) is None
    s={'schema':'NF631-reference-widening-v1','original_entry_sha256':sourcehash,
       'widened_entry_sha256':filehash(a.output),
       'input_sha256':{x.name:filehash(x) for x in a.shards.rglob('nf621-shard*.json.gz')},
       'H_entries':29403,'V_entries':968,'H_radius_changes':changesH,'V_radius_changes':changesV,
       'old_max_H_units':str(oldmaxH),'new_max_H_units':str(maxH),
       'old_max_V_units':str(oldmaxV),'new_max_V_units':str(maxV),
       'scope':'external reference arithmetic only; actual Lean widening truth pending'}
    assert len(s['input_sha256'])==8
    a.summary.write_text(json.dumps(s,indent=2)+'\n')
    print('NF631 widening generated:',changesH,'H and',changesV,'V radii changed',flush=True)

if __name__=='__main__': main()
