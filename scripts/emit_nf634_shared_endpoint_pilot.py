#!/usr/bin/env python3
"""Emit shared endpoint inventory and bounded original moment residual pilots.
All generated endpoints are untrusted proposals pending reference equalities.
Pilot checks intentionally omit transcendental evaluation, not its proof debt.
"""
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import emit_bank, filetext, qlit, scaled, MODULE
from verify_nf620_physical_key_tables import pi, real_exp, phase_reduced, reduced, table
from verify_nf622_physical_entry_reassembly import read_shards

BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSharedEndpointCache'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'

def ball(x):
    return '⟨'+','.join(scaled(v) for v in x)+'⟩'

def rect(x):
    return '⟨'+','.join(ball(v) for v in x)+'⟩'

def lookup(name,items):
    body=f'def {name} (q : ℚ) : NF591Rect :=\n'
    for k,v in sorted(items.items()):
        body+=f'  if q = {qlit(k)} then {rect(v)} else\n'
    return body+'  NF591Rect.zero\n\n'

def inventory(data):
    signed=set(data)|{(-h,-f) for h,f in data}|{(F(0),F(0))}
    hs=sorted({h for h,f in signed})
    us=sorted({reduced(f) for h,f in signed})
    assert hs==[F(-1),F(-1,2),F(0),F(1,2),F(1)]
    assert len(signed)==15671 and len(us)==1276
    assert all(-F(1,2)<=u<F(1,2) for u in us)
    return hs,us

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--shards',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--inventory',type=Path,required=True)
    a=p.parse_args()
    data=read_shards(a.root,a.shards)
    assert len(data)==7835 and sum(map(len,data.values()))==37994
    hs,us=inventory(data)
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
            for p in a.shards.rglob('nf621-shard*.json.gz')}
    assert len(hashes)==8
    a.inventory.write_text(json.dumps({'schema':'NF634-shared-endpoint-inventory-v1',
        'keys':len(data),'rows':sum(map(len,data.values())),'signed_keys':15671,
        'real_parameters':[str(x) for x in hs],'reduced_phases':[str(x) for x in us],
        'input_sha256':hashes,'scope':'external inventory; receipt truth not asserted'},indent=2)+'\n')
    keys=[(F(1),F(0)),(F(0),F(37,32))]
    # Each pilot retains the genuine first row, checked independently
    # against the original producer. The omitted rows remain open.
    subset={k:data[k][:1] for k in keys}
    assert all(table(*k,0)==rows for k,rows in subset.items())
    m=emit_bank(subset,a.output,1,hashes)
    hh={v for h,f in keys for v in (h,-h)}
    uu={reduced(v) for h,f in keys for v in (f,-f)}
    R={h:real_exp(h) for h in hh}
    P={u:phase_reduced(u) for u in uu}
    body=f'def nf634PilotPi : NF591Ball := {ball(pi())}\n\n'
    body+=lookup('nf634PilotR',R)+lookup('nf634PilotP',P)
    (a.output/'SharedEndpoints.lean').write_text(filetext([BASE],body))
    for i,k in enumerate(sorted(subset)):
        name=f'Chunk{i:03d}'
        body=OPT+f'theorem nf634{name}Local :\n'
        body+=f'    neutralNF634SharedChunkCheck nf634PilotPi nf634PilotR nf634PilotP nf627{name}=true := by\n'
        body+='  decide +kernel\n\n'
        body+=f'#print axioms nf634{name}Local\n'
        (a.output/f'SharedGate{i:03d}.lean').write_text(filetext(
            [MODULE+'.SharedEndpoints',MODULE+'.'+name],body))
    print('NF634 inventory:',len(hs),'real factors,',len(us),'reduced phases; two actual first-row residual proposals')

if __name__=='__main__': main()
