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
from emit_nf633_segmented_exp import states, step, state, rect, ball
from emit_nf627_original_moment_bank import filetext, qlit
from verify_nf620_physical_key_tables import Q,N,ZERO,ONE,exact,mul,pi,zmul,zadd

sys.set_int_max_str_digits(0)
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEndpointSlotCertificates'
MODULE='WeilDefect.Generated.NF642'
BANK='WeilDefect.Generated.NF635'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

FIXED=((0,2),(0,2))

def compressed_states(arg):
    """Find a fixed jet and check the sufficient all-future divisor bound.
    Return only the required prefix, and exact closed-form terminal state.
    No analytic tail approximation or replacement of the reference N."""
    prod=zmul(FIXED,arg)
    assert all(m==0 and r>0 for m,r in prod)
    threshold=max(r for m,r in prod)
    ss=[((ONE,ZERO),(ZERO,ZERO))]
    while len(ss)-1<N:
        n=len(ss)-1
        if ss[-1][0]==FIXED and n+1>=threshold:
            k=2*(N-n)
            return ss,n,(FIXED,zadd(ss[-1][1],((0,k),(0,k)))),threshold
        ss.append(step(ss[-1],arg,n))
    return ss,N,ss[-1],threshold

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--chunk',type=int,default=32)
    ap.add_argument('--slot',action='append',default=[],help='Real:0 or Phase:123')
    ap.add_argument('--all',action='store_true')
    ap.add_argument('--stable-tail',action='store_true')
    ap.add_argument('--survey',action='store_true',help='audit every retained endpoint with compressed exact recurrence')
    a=ap.parse_args()
    assert 0<a.chunk<=N and (not a.survey or a.stable_tail)
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
    base=BASE if not a.stable_tail else 'WeilDefect.Arithmetic.ActualZetaOriginalPhysicalStableTaylorTail'
    write('PiLiteral',[base],f'def nf642Pi : NF591Ball := {ball(p)}')
    plan=[]
    selected=set(requested)
    for label,entries in tables.items():
        for i,(q,endpoint) in enumerate(entries):
            name=f'{label}{i:04d}'
            plan.append({'bank':label,'index':i,'parameter':str(q),'module':name,
                'segments':ceil(N/a.chunk),'generated':(label,i) in selected})
            if (label,i) not in selected and not a.survey: continue
            v='nf642'+name
            arg=(exact(q*F(11,20)),ZERO) if label=='Real' else (ZERO,mul(p,exact(q/2)))
            if a.stable_tail:
                ss,cutoff,terminal,threshold=compressed_states(arg)
                plan[-1].update(cutoff=cutoff,skipped_terms=N-cutoff,
                    prefix_segments=ceil(cutoff/a.chunk),fixed_product_max_radius=threshold)
            else:
                ss=states(arg); cutoff=N; terminal=ss[N]
            small=tuple((x,r+1) for x,r in terminal[1])
            result=zmul(small,small)
            if label=='Phase': result=zmul(result,result)
            assert result==endpoint, (label,i,'retained endpoint mismatch')
            if (label,i) not in selected: continue
            body=f'def {v}Arg : NF591Rect := {rect(arg)}\n'
            body+=f'def {v}Small : NF591Rect := {rect(small)}\n'
            body+=f'def {v}Value : NF591Rect := {rect(endpoint)}\n'
            body+=f'def {v}State0000 : NF633ExpState := {state(ss[0])}\n\n'
            body+=f'theorem {v}SeedCheck : neutralNF633StateEq (neutralNF633State {v}Arg neutralNF616Q 0) {v}State0000=true := by\n  decide +kernel\n'
            body+=f'theorem {v}Prefix0000 : neutralNF633State {v}Arg neutralNF616Q 0={v}State0000 := neutralNF633StateEq_sound _ _ {v}SeedCheck\n\n'
            for start in range(0,cutoff,a.chunk):
                length=min(a.chunk,cutoff-start); end=start+length
                st=f'{v}State{start:04d}'; en=f'{v}State{end:04d}'
                check=f'{v}Check{end:04d}'; pref=f'{v}Prefix{end:04d}'
                body+=f'def {en} : NF633ExpState := {state(ss[end])}\n'
                body+=f'theorem {check} : neutralNF633StateEq (neutralNF633Segment {v}Arg neutralNF616Q {start} {st} {length}) {en}=true := by\n  decide +kernel\n'
                body+=f'theorem {pref} : neutralNF633State {v}Arg neutralNF616Q {end}={en} :=\n  neutralNF633Prefix_extend {v}Arg neutralNF616Q {start} {length} {st} {en} {v}Prefix{start:04d} {check}\n\n'
            if cutoff<N:
                st=f'{v}State{cutoff:04d}'; en=f'{v}State{N:04d}'
                length=N-cutoff
                body+=f'def {en} : NF633ExpState := {state(terminal)}\n'
                body+=f'theorem {v}FixedCheck : neutralNF633RectEq {st}.jet (neutralNF643Fixed neutralNF616Q)=true := by\n  decide +kernel\n'
                body+=f'theorem {v}StableCheck : neutralNF643StableGate {v}Arg neutralNF616Q {cutoff}=true := by\n  decide +kernel\n'
                body+=f'theorem {v}TailCheck : neutralNF633StateEq (neutralNF643Tail {st} neutralNF616Q {length}) {en}=true := by\n  decide +kernel\n'
                body+=f'theorem {v}Prefix{N:04d} : neutralNF633State {v}Arg neutralNF616Q {N}={en} :=\n  neutralNF643Tail_to_state {v}Arg neutralNF616Q {cutoff} {length} {st} {en} {v}Prefix{cutoff:04d} {v}FixedCheck {v}StableCheck {v}TailCheck\n\n'
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
        'stable_tail':a.stable_tail,'survey':a.survey,'audited_slots':sum('cutoff' in x for x in plan),
        'prefix_segments_audited':sum(x.get('prefix_segments',0) for x in plan),
        'skipped_terms_audited':sum(x.get('skipped_terms',0) for x in plan),
        'files':files,'scope':'untrusted local proof proposals, neither full bank truth nor pi attachment'},indent=2)+'\n')
    print('NF642 planned',len(plan),'slots;',len(selected),'actual endpoint matches and prefix proof proposals')
    if a.stable_tail:
        print('NF643 exact tail survey:',sum('cutoff' in x for x in plan),'slots;',sum(x.get('skipped_terms',0) for x in plan),'terms compressed; prefix segments',sum(x.get('prefix_segments',0) for x in plan),flush=True)
if __name__=='__main__': main()
