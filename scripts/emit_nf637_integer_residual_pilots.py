#!/usr/bin/env python3
"""Emit integer-only residual gates on genuine original moment rows.
Literal cache inputs still require their separate reference identities."""
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import filetext
from verify_nf620_physical_key_tables import Q, exact, mul, pi, endpoint, real, zmul, zadd, zneg, upper, table
from verify_nf622_physical_entry_reassembly import read_shards

BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerResidual'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def ball(a): return '⟨'+','.join(f'({x}:ℤ)' for x in a)+'⟩'
def rect(a): return '⟨'+','.join(map(ball,a))+'⟩'
def row(a): return '⟨'+','.join(f'({x}:ℤ)' for x in a)+'⟩'

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--shards',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    data=read_shards(a.root,a.shards)
    a.output.mkdir(parents=True,exist_ok=True)
    records=[]
    for label,k in [('Pole',(F(1),F(0))),('Osc',(F(0),F(37,32))),('Mixed',(F(1,2),F(37,64)))]:
        h,f=k
        rows=data[k]
        assert table(h,f,len(rows)-1)==rows
        d=max(abs(h),6*abs(f))
        z=exact(h),mul(pi(),exact(2*f))
        pos,neg=endpoint(h,f),endpoint(-h,-f)
        prefix='nf637'+label
        body=OPT+f'def {prefix}Z : NF636Rect := {rect(z)}\n\n'
        count=0
        for n,(x,y,R) in enumerate(rows):
            B=zadd(zmul(real(F(11,10)**n),pos),zneg(zmul(real(F(-11,10)**n),neg)))
            q=((x,0),(y,0))
            r=zadd(B,zneg(zmul(z,q)))
            prior=0
            v=prefix+str(n)
            if n:
                px,py,pr=rows[n-1]
                r=zadd(r,zneg(zmul(real(n),((px,0),(py,0)))))
                prior=n*pr
            assert d.denominator*(upper(r)+prior)<=d.numerator*R
            # Zero-radius mutation must fail: arithmetic fee is positive.
            assert upper(r)+prior>0
            body+=f'def {v}B : NF636Rect := {rect(B)}\n'
            body+=f'def {v}Row : NF637Row := {row((x,y,R))}\n'
            body+=f'def {v}Bad : NF637Row := {row((x,y,0))}\n'
            if n==0:
                gate=f'neutralNF637BaseGate {v}B {prefix}Z {{row}} neutralNF616Q {d.numerator} {d.denominator}'
            else:
                gate=f'neutralNF637SuccGate {v}B {prefix}Z {{row}} {prefix}{n-1}Row neutralNF616Q {n-1} {d.numerator} {d.denominator}'
            body+=f'theorem {v}Check : {gate.replace("{row}",v+"Row")}=true := by\n  decide +kernel\n'
            body+=f'theorem {v}Reject : {gate.replace("{row}",v+"Bad")}=false := by\n  decide +kernel\n\n'
            count+=1
        body+=f'#print axioms {prefix}0Check\n#print axioms {prefix}{len(rows)-1}Check\n'
        path=a.output/(label+'.lean')
        path.write_text(filetext([BASE],body))
        records.append({'file':path.name,'key':[str(h),str(f)],'rows':count,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in a.shards.rglob('nf621-shard*.json.gz')}
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF637-residual-pilot-proposals-v1','input_sha256':hashes,
        'files':records,'scope':'local fixed-scale residual truth only; cache and row identities remain separate'},indent=2)+'\n')
    print('NF637 emitted',sum(x['rows'] for x in records),'actual moment rows and zero-radius mutations')

if __name__=='__main__': main()
