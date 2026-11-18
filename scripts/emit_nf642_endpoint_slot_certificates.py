#!/usr/bin/env python3
"""Attach segmented Taylor proofs to the actual retained NF635 endpoint bank.

Generate a complete slot plan, but only bounded proof pilots by default.
Arbitrary slots or all slots may be generated explicitly. The endpoint
values are the retained proposals, not replacement numerical values.
"""
import argparse
import gzip
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from math import ceil
from emit_nf633_segmented_exp import states, state, rect, ball
from emit_nf627_original_moment_bank import filetext, qlit
from verify_nf620_physical_key_tables import Q,N,ZERO,exact,mul,pi,zmul

sys.set_int_max_str_digits(0)
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEndpointSlotCertificates'
MODULE='WeilDefect.Generated.NF642'
BANK='WeilDefect.Generated.NF635'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--chunk',type=int,default=32)
    ap.add_argument('--slot',action='append',default=[],help='Real:0 or Phase:123')
    ap.add_argument('--all',action='store_true')
    a=ap.parse_args()
    assert 0<a.chunk<=N
    a.output.mkdir(parents=True,exist_ok=True)
    m=json.loads((a.bank/'manifest.json').read_text())
    assert m['schema']=='NF635-indexed-endpoint-proposals-v1' and m['full_values']
    assert (m['key_count'],m['route_count'],m['real_count'],m['phase_count'])==(7835,31340,5,1276)
    for x in m['files']:
        assert sha(a.bank/x['file'])==x['sha256']
    with gzip.open(a.bank/'endpoints.json.gz','rt') as f:
        b=json.load(f)
    assert b['schema']=='NF635-original-shared-endpoints-v1' and b['scale']=='10^2600'
    p=tuple(map(int,b['pi'])); assert p==pi()
    tables={}
    for label,n in [('Real',5),('Phase',1276)]:
        entries=[(F(k),tuple(tuple(map(int,v)) for v in r)) for k,r in b[label.lower()]]
        assert len(entries)==n and [k for k,_ in entries]==sorted(set(k for k,_ in entries))
        tables[label]=entries
    assert [k for k,_ in tables['Real']]==[F(-1),F(-1,2),F(0),F(1,2),F(1)]
    phases=[q for q,_ in tables['Phase']]
    assert F(87,320) in phases
    default=[('Real',i) for i in range(5)]+[('Phase',0),('Phase',phases.index(F(87,320)))]
    requested=([(x.split(':')[0],int(x.split(':')[1])) for x in a.slot] if a.slot else default)
    if a.all:
        assert not a.slot
        requested=[(label,i) for label,entries in tables.items() for i in range(len(entries))]
    assert len(set(requested))==len(requested)
    assert all(label in tables and 0<=i<len(tables[label]) for label,i in requested)
    files=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(filetext(imports,OPT+body))
        files.append({'file':path.name,'sha256':sha(path)})
    write('PiLiteral',[BASE],f'def nf642Pi : NF591Ball := {ball(p)}')
    plan=[]
    selected=set(requested)
    for label,entries in tables.items():
        for i,(q,endpoint) in enumerate(entries):
            name=f'{label}{i:04d}'
            plan.append({'bank':label,'index':i,'parameter':str(q),'module':name,
                'segments':ceil(N/a.chunk),'generated':(label,i) in selected})
            if (label,i) not in selected: continue
            v='nf642'+name
            arg=(exact(q*F(11,20)),ZERO) if label=='Real' else (ZERO,mul(p,exact(q/2)))
            ss=states(arg)
            small=tuple((x,r+1) for x,r in ss[N][1])
            result=zmul(small,small)
            if label=='Phase': result=zmul(result,result)
            assert result==endpoint, (label,i,'retained endpoint mismatch')
            body=f'def {v}Arg : NF591Rect := {rect(arg)}\n'
            body+=f'def {v}Small : NF591Rect := {rect(small)}\n'
            body+=f'def {v}Value : NF591Rect := {rect(endpoint)}\n'
            body+=f'def {v}State0000 : NF633ExpState := {state(ss[0])}\n\n'
            body+=f'theorem {v}SeedCheck : neutralNF633StateEq (neutralNF633State {v}Arg neutralNF616Q 0) {v}State0000=true := by\n  decide +kernel\n'
            body+=f'theorem {v}Prefix0000 : neutralNF633State {v}Arg neutralNF616Q 0={v}State0000 := neutralNF633StateEq_sound _ _ {v}SeedCheck\n\n'
            for start in range(0,N,a.chunk):
                length=min(a.chunk,N-start); end=start+length
                st=f'{v}State{start:04d}'; en=f'{v}State{end:04d}'
                check=f'{v}Check{end:04d}'; pref=f'{v}Prefix{end:04d}'
                body+=f'def {en} : NF633ExpState := {state(ss[end])}\n'
                body+=f'theorem {check} : neutralNF633StateEq (neutralNF633Segment {v}Arg neutralNF616Q {start} {st} {length}) {en}=true := by\n  decide +kernel\n'
                body+=f'theorem {pref} : neutralNF633State {v}Arg neutralNF616Q {end}={en} :=\n  neutralNF633Prefix_extend {v}Arg neutralNF616Q {start} {length} {st} {en} {v}Prefix{start:04d} {check}\n\n'
            if label=='Real':
                expected=f'NF591Rect.realQ (({qlit(q)})*11/20) neutralNF616Q'
                ref=f'neutralNF635RealRef ({qlit(q)})'
                theorem=f'neutralNF642RealSlot ({qlit(q)})'
            else:
                expected=f'neutralNF642PhaseArg nf642Pi ({qlit(q)}) neutralNF616Q'
                ref=f'neutralNF635PhaseRef nf642Pi ({qlit(q)})'
                theorem=f'neutralNF642PhaseSlot nf642Pi ({qlit(q)})'
            sq=f'({v}Small.mulQ {v}Small neutralNF616Q)'
            expr=sq if label=='Real' else f'({sq}.mulQ {sq} neutralNF616Q)'
            body+=f'theorem {v}ArgCheck : neutralNF633RectEq ({expected}) {v}Arg=true := by\n  decide +kernel\n'
            body+=f'theorem {v}SmallCheck : neutralNF633RectEq ({v}State{N:04d}.sumState.expand (1/(neutralNF616Q:ℚ))) {v}Small=true := by\n  decide +kernel\n'
            body+=f'theorem {v}ValueCheck : neutralNF633RectEq {expr} {v}Value=true := by\n  decide +kernel\n'
            body+=f'theorem {v}Eq : {ref}={v}Value :=\n  {theorem} {v}Arg {v}Small {v}Value {v}State{N:04d} {v}ArgCheck {v}Prefix{N:04d} {v}SmallCheck {v}ValueCheck\n\n'
            body+=f'#print axioms {v}Eq\n'
            write(name,[MODULE+'.PiLiteral'],body)
            # This intentionally uses the ACTUAL retained bank slot.
            # Keep the expensive full-bank access separate from the prefix.
            bank=f'nf635{label}Bank'
            ref= 'neutralNF635RealRef' if label=='Real' else '(neutralNF635PhaseRef nf635Pi)'
            body=f'theorem {v}KeyCheck : decide (neutralNF635ParamRead {bank}.keys {i}=({qlit(q)}))=true := by\n  decide +kernel\n'
            body+=f'theorem {v}StoredCheck : neutralNF633RectEq ({bank}.read {i}) {v}Value=true := by\n  decide +kernel\n'
            eq=f'{v}Eq'
            if label=='Phase':
                body+='theorem '+v+'PiEq : nf635Pi=nf642Pi := by rfl\n'
                eq=f'(by rw [{v}PiEq]; exact {v}Eq)'
            body+=f'theorem {v}Attached : {bank}.read {i}={ref} (neutralNF635ParamRead {bank}.keys {i}) :=\n  neutralNF642AttachSlot {bank} {ref} {i} ({qlit(q)}) {v}Value {v}KeyCheck {v}StoredCheck {eq}\n\n'
            body+=f'#print axioms {v}Attached\n'
            write(name+'Attach',[MODULE+'.'+name,BANK+'.Banks'],body)
    (a.output/'plan.json').write_text(json.dumps({'schema':'NF642-endpoint-slot-plan-v1',
        'bank_manifest_sha256':sha(a.bank/'manifest.json'),'endpoint_bytes_sha256':sha(a.bank/'endpoints.json.gz'),
        'slots':plan,'slot_count':len(plan),'generated':len(selected),'segments_all':len(plan)*ceil(N/a.chunk),
        'files':files,'scope':'untrusted local proof proposals, neither full bank truth nor pi attachment'},indent=2)+'\n')
    print('NF642 planned',len(plan),'slots;',len(selected),'actual endpoint matches and prefix proof proposals')
if __name__=='__main__': main()
