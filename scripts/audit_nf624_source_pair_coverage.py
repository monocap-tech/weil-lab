#!/usr/bin/env python3
"""Audit actual source pair metadata, not moment numerical validity.

The same h,f ordering and bounded search are used by the NF624
Lean index candidate. Every actual pair key/degree is checked,
including the four weighted critical sources and retained pole.
"""
import argparse
import hashlib
import json
from pathlib import Path
from verify_nf620_physical_key_tables import inventory, canonical
from verify_nf622_physical_entry_reassembly import selected, critical

def search(keys,k):
    lo,hi=0,len(keys)
    for _ in range(16):
        if lo>=hi:
            break
        m=(lo+hi)//2
        if keys[m]==k:
            return m
        if keys[m]<k:
            lo=m+1
        else:
            hi=m
    return len(keys)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    schedule=inventory(args.root)
    S,C=selected(args.root),critical(args.root)
    keys=sorted(k for k in schedule if k!=(0,0))
    assert len(keys)==7835
    def check(a,b):
        for h,f,n,_,_ in a:
            for j,g,m,_,_ in b:
                k=canonical(h+j,f+g)
                degree=n+m
                if k==(0,0):
                    assert degree<=schedule[k]
                else:
                    i=search(keys,k)
                    assert i<len(keys) and keys[i]==k and degree<=schedule[k]
    for a in S:
        for b in S:
            check(a,b)
    for a in S:
        for b in C:
            check(a,b)
    hcount=sum(len(a)*len(b) for a in S for b in S)
    vcount=sum(len(a)*len(b) for a in S for b in C)
    assert (hcount,vcount)==(234256,127776)
    out={'schema':'NF624-original-key-metadata-v1',
         'source_pair_checks':{'H':hcount,'V':vcount},
         'ordered_nonzero_keys':[{'h':str(h),'f':str(f),'rows':schedule[h,f]+1} for h,f in keys],
         'zero_key_rows':schedule[(0,0)]+1,
         'source_files':{path:hashlib.sha256((args.root/path).read_bytes()).hexdigest() for path in (
           'WeilDefect/Arithmetic/ActualZetaOriginalJ242ExponentialSignature.lean',
           'WeilDefect/Arithmetic/ActualZetaOriginalNF407FrozenData.lean')},
         'scope':'external exact metadata audit only; not a numerical or Lean proof'}
    args.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('NF624 exact source metadata PASS:',hcount,'H and',vcount,'V pair lookups')
if __name__=='__main__': main()
