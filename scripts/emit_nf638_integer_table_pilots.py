#!/usr/bin/env python3
"""Emit complete integer-table gates on audited original moment shards.

The local gate computes all boundary rectangles itself from the three
proposed cache rectangles. Cache equality to the transcendental reference
remains an explicit hypothesis of the analytic attachment theorem.
"""
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import filetext, keylit
from verify_nf620_physical_key_tables import Q, exact, mul, pi, endpoint
from verify_nf622_physical_entry_reassembly import read_shards

BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerTableClosure'
MODULE='WeilDefect.Generated.NF638'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def tup(xs): return '⟨'+','.join(xs)+'⟩'
def integers(xs): return tup(f'({v}:ℤ)' for v in xs)
def rect(x): return tup(integers(b) for b in x)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--shards',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    data=read_shards(a.root,a.shards)
    a.output.mkdir(parents=True,exist_ok=True)
    records=[]
    names=[]
    for label,k in [('Pole',(F(1),F(0))),('Osc',(F(0),F(37,32))),('Mixed',(F(1,2),F(37,64)))]:
        h,f=k; rows=data[k]; delta=max(abs(h),6*abs(f))
        z=exact(h),mul(pi(),exact(2*f))
        cache=tup(rect(v) for v in (z,endpoint(h,f),endpoint(-h,-f)))
        v='nf638'+label
        params=f'{keylit(k)}, {delta.numerator}, {delta.denominator}, {cache},'
        literal='#[\n    '+',\n    '.join(map(integers,rows))+'\n  ]'
        body=OPT+f'def {v} : NF638Table := ⟨{params}\n  {literal}⟩\n\n'
        body+=f'theorem {v}Check : {v}.check neutralNF616Q neutralNF616ExpN=true := by\n  decide +kernel\n\n'
        body+=f'def {v}Bad : NF638Table := {{ {v} with e := 0 }}\n'
        body+=f'theorem {v}Reject : {v}Bad.check neutralNF616Q neutralNF616ExpN=false := by\n  decide +kernel\n\n'
        body+=f'#print axioms {v}Check\n#print axioms {v}Reject'
        path=a.output/(label+'.lean')
        path.write_text(filetext([BASE],body))
        names.append(v)
        records.append({'file':path.name,'rows':len(rows),'key':[str(h),str(f)],'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    body=OPT+'def nf638PilotTables : List NF638Table := ['+', '.join(names)+']\n\n'
    body+='theorem nf638PilotChecks : nf638PilotTables.all (fun t => t.check neutralNF616Q neutralNF616ExpN)=true := by\n'
    body+='  simp only [nf638PilotTables,List.all_cons,List.all_nil,'+', '.join(v+'Check' for v in names)+',Bool.true_and]\n\n'
    body+='''theorem nf638PilotChunk (p : NF591Ball)
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hc : ∀ t ∈ nf638PilotTables, t.cache.denote neutralNF616Q=
      neutralNF621Cache p t.key neutralNF616Q neutralNF616ExpN) :
    neutralNF628ChunkCheck (neutralNF638Chunk nf638PilotTables)=true :=
  neutralNF638Chunk_of_checks nf638PilotTables p hpi hc nf638PilotChecks

#print axioms nf638PilotChunk
'''
    path=a.output/'Join.lean'
    path.write_text(filetext([MODULE+'.'+x[5:] for x in names],body))
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in a.shards.rglob('nf621-shard*.json.gz')}
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF638-integer-table-pilots-v1',
        'input_sha256':hashes,'files':records,'join_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'scope':'local complete table checks; cache equalities are explicit assumptions'},indent=2)+'\n')
    print('NF638 three complete original table gates,',sum(x['rows'] for x in records),'rows; cache inputs untrusted')
if __name__=='__main__': main()
