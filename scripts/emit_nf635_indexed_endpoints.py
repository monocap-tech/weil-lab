#!/usr/bin/env python3
"""Emit the indexed shared endpoint bank and key-only routing gates.

The full numerical mode computes every unique reference endpoint ONCE.
It emits literal proposals, never an assumption of their equality to
Lean's evaluator. Metadata mode is independent of that expensive work.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from bisect import bisect_left
from fractions import Fraction as F
from emit_nf627_original_moment_bank import filetext, qlit, keylit, scaled
from emit_nf634_shared_endpoint_pilot import inventory
from verify_nf620_physical_key_tables import pi, real_exp, phase_reduced, reduced
from verify_nf622_physical_entry_reassembly import read_shards

BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIndexedEndpoints'
MODULE='WeilDefect.Generated.NF635'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'

def ball(a): return '⟨'+','.join(scaled(x) for x in a)+'⟩'
def rect(a): return '⟨'+','.join(ball(x) for x in a)+'⟩'
def checked_index(keys,q):
    i=bisect_left(keys,q)
    assert i<len(keys) and keys[i]==q
    return i

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--shards',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--full-values',action='store_true')
    a=p.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    data=read_shards(a.root,a.shards)
    assert len(data)==7835 and sum(map(len,data.values()))==37994
    hs,us=inventory(data)
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
            for p in a.shards.rglob('nf621-shard*.json.gz')}
    assert len(hashes)==8
    ordered=sorted(data)
    routes=[]
    for h,f in ordered:
        routes.append([checked_index(hs,h),checked_index(hs,-h),
                       checked_index(us,reduced(f)),checked_index(us,reduced(-f))])
    assert len(routes)==7835 and sum(map(len,routes))==31340
    # Every coordinate in both finite inventories is actually used.
    assert set(i for row in routes for i in row[:2])==set(range(len(hs)))
    assert set(i for row in routes for i in row[2:])==set(range(len(us)))
    files=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(filetext(imports,body))
        files.append({'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    arr=lambda xs:'#[ '+', '.join(map(qlit,xs))+' ]'
    write('Params',[BASE],
          f'def nf635RealKeys : Array ℚ := {arr(hs)}\n\n'+
          f'def nf635PhaseKeys : Array ℚ := {arr(us)}')
    names=[]
    # Key-only coverage: no full row bank or large coordinate reduction.
    for start in range(0,len(ordered),128):
        name=f'Coverage{start//128:03d}'
        names.append(name)
        v='nf635'+name
        ks=',\n  '.join(keylit(k) for k in ordered[start:start+128])
        body=OPT+f'def {v}Keys : List NF616Frequency := [\n  {ks}\n]\n\n'
        body+=f'theorem {v}Check : {v}Keys.all\n'
        body+='    (neutralNF635FrequencyCoverage nf635RealKeys nf635PhaseKeys)=true := by\n  decide +kernel\n\n'
        body+=f'#print axioms {v}Check'
        write(name,[MODULE+'.Params'],body)
    if a.full_values:
        valueimports=[MODULE+'.Params']
        vals={}
        for label,keys,fun in [('Real',hs,real_exp),('Phase',us,phase_reduced)]:
            parts=[]
            for start in range(0,len(keys),16):
                name=f'{label}Values{start//16:03d}'
                v='nf635'+name
                numbers=[fun(q) for q in keys[start:start+16]]
                parts.append(v); valueimports.append(MODULE+'.'+name)
                write(name,[BASE],f'def {v} : Array NF591Rect := #[\n  '+',\n  '.join(map(rect,numbers))+'\n]')
                vals.setdefault(label,[]).extend(numbers)
            vals[label+'Parts']=parts
        body=f'def nf635Pi : NF591Ball := {ball(pi())}\n\n'
        for label in ('Real','Phase'):
            parts=', '.join(vals[label+'Parts'])
            body+=f'def nf635{label}Bank : NF635EndpointBank :=\n'
            body+=f'  ⟨nf635{label}Keys, (#[{parts}] : Array (Array NF591Rect)).foldl (fun a b => a++b) #[]⟩\n\n'
        write('Banks',valueimports,body)
        with gzip.open(a.output/'endpoints.json.gz','wt') as f:
            json.dump({'schema':'NF635-original-shared-endpoints-v1','scale':'10^2600',
                'pi':list(map(str,pi())),
                'real':[[str(k),[[str(x) for x in b] for b in v]] for k,v in zip(hs,vals['Real'])],
                'phase':[[str(k),[[str(x) for x in b] for b in v]] for k,v in zip(us,vals['Phase'])],
                'scope':'untrusted endpoint proposals; exact Lean identity required'},f,separators=(',',':'))
    manifest={'schema':'NF635-indexed-endpoint-proposals-v1','input_sha256':hashes,
              'key_count':len(ordered),'route_count':4*len(ordered),'real_count':len(hs),'phase_count':len(us),
              'full_values':a.full_values,'coverage_chunks':len(names),'files':files}
    (a.output/'routes.json').write_text(json.dumps({'keys':[[str(h),str(f)] for h,f in ordered],
        'routes':routes},separators=(',',':'))+'\n')
    (a.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print('NF635',manifest['route_count'],'exact index routes;',len(names),'coverage chunks; full values=',a.full_values)

if __name__=='__main__': main()
