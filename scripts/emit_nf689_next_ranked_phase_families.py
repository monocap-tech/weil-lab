#!/usr/bin/env python3
"""Schedule the complete original canonical bank by shared reduced phase.
Emit a chosen exact family batch using established rational leaf proof source.
The complete schedule is external evidence, not a kernel coverage certificate."""
import argparse
import gzip
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path
from emit_nf633_segmented_exp import states, state, rect
from emit_nf627_original_moment_bank import filetext, qlit, keylit, rowlit
from verify_nf620_physical_key_tables import N, ZERO, exact, mul, pi, reduced, zmul, table, inventory
from emit_nf684_second_oscillator_moments import CASES as NF684_CASES
from verify_nf622_physical_entry_reassembly import read_shards
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRationalLocalMoment'
MODULE='WeilDefect.Generated.NF689'
PI='WeilDefect.Generated.NF632.Pi'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
CERTIFIED_NF686_FAMILIES=(F(87,640),F(3,32))
BATCH_SIZE=4
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(d):
    m=json.loads((d/'manifest.json').read_text())
    for x in m['files']: assert sha(d/x['file'])==x['sha256']
    return m
def main():
    ap=argparse.ArgumentParser()
    for k in ('root','shards','bank','pi','output'): ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--family',action='append',type=F,default=[])
    ap.add_argument('--plan-only',action='store_true')
    a=ap.parse_args()
    sig=(a.root/'WeilDefect/Arithmetic/ActualZetaOriginalJ242ExponentialSignature.lean').read_text()
    gs=re.findall(r'\(\((\d+(?:/\d+)?)\s*:\s*ℚ\),\s*(\d+)\)',sig)
    assert gs[:2]==[('37/64','14'),('211/128','9')] and len(gs)==67
    a.output.mkdir(parents=True,exist_ok=True)
    bm,pm=validate(a.bank),validate(a.pi)
    assert bm['full_values'] and (bm['real_count'],bm['phase_count'])==(5,1276)
    assert pm['full'] and len(pm['files'])==127
    hashes={p.name:sha(p) for p in a.shards.rglob('nf621-shard*.json.gz')}
    assert len(hashes)==8 and hashes==bm['input_sha256']
    rows=read_shards(a.root,a.shards)
    schedule=inventory(a.root)
    schedule.pop((F(0),F(0)))
    assert {k:len(v)-1 for k,v in rows.items()}==schedule
    assert len(rows)==7835 and sum(map(len,rows.values()))==37994
    families={}
    for k,data in sorted(rows.items()):
        h,f=k
        families.setdefault(abs(reduced(f)),[]).append((k,len(data)))
    assert len(families)==639
    all_phase={reduced(s*f) for h,f in rows for s in (-1,1)}
    all_real={s*h for h,f in rows for s in (-1,1)}
    assert (len(all_phase),len(all_real))==(1276,5)
    previous={abs(reduced(f)) for _,(h,f),_ in NF684_CASES}
    first_keys={(F(1),F(0)),(F(0),F(37,32)),(F(1,2),F(37,64)),(F(-1,2),F(37,64))}
    first={abs(reduced(f)) for h,f in first_keys}
    ordered=sorted(families,key=lambda q:(-sum(n for k,n in families[q]),q))
    todo=[q for q in ordered if q not in first|previous]
    assert todo[:2]==list(CERTIFIED_NF686_FAMILIES)
    # The first two ranked untouched families were covered by NF686.
    # Select the next four, never silently repeat earlier whole families.
    remaining=todo[2:]
    requested=a.family or remaining[:BATCH_SIZE]
    assert len(requested)==BATCH_SIZE and len(set(requested))==BATCH_SIZE
    assert all(q in remaining for q in requested)
    if not a.family: assert requested==remaining[:BATCH_SIZE]
    plan=[]; allkeys=[]
    for rank,q in enumerate(ordered,1):
        members=families[q]; real=sorted({s*h for (h,f),n in members for s in (-1,1)})
        phases=sorted({reduced(s*f) for (h,f),n in members for s in (-1,1)})
        allkeys.extend(k for k,n in members)
        plan.append({'rank':rank,'abs_phase':str(q),'tables':len(members),'rows':sum(n for k,n in members),'real_parameters':list(map(str,real)),'phase_parameters':list(map(str,phases)),
                     'leaf_family_targeted_before':q in first|previous|set(CERTIFIED_NF686_FAMILIES),'selected':q in requested,
                     'keys':[{'key':list(map(str,k)),'rows':n} for k,n in members]})
    assert len(allkeys)==len(set(allkeys))==7835 and set(allkeys)==set(rows)
    planpath=a.output/'full-phase-plan.json'
    planpath.write_text(json.dumps({'schema':'NF689-full-original-phase-schedule-v1','keys':7835,'rows':37994,'families':639,'real_leaves':5,'phase_leaves':1276,'input_sha256':hashes,'families_ranked_by_rows':plan,'scope':'Exact external schedule reconciliation only; no Lean coverage or table truth.'},indent=2)+'\n')
    cases=[]; targetfamily={}
    for q in requested:
        for k,n in families[q]:
            label=f'Key{len(cases):03d}'
            cases.append((label,k,n));targetfamily[label]=requested.index(q)
    assert len(cases)==sum(len(families[q]) for q in requested)
    assert len({k for _,k,_ in cases})==len(cases)
    assert sum(n for _,_,n in cases)==sum(n for q in requested for _,n in families[q])
    print('NF689 exact complete plan: 639 families, 7835 keys, 37994 rows; selected',len(cases),'tables',sum(n for _,_,n in cases),'rows',flush=True)
    if a.plan_only: return
    with gzip.open(a.bank/'endpoints.json.gz','rt') as f: b=json.load(f)
    assert b['schema']=='NF635-original-shared-endpoints-v1' and b['scale']=='10^2600'
    p=tuple(map(int,b['pi'])); assert p==pi()
    literal=next(x for x in (a.pi/'Pi.lean').read_text().splitlines() if x.startswith('def nf632Pi :'))
    assert list(map(int,re.findall(r'\((-?\d+):ℚ\)/neutralNF616Q',literal)))==list(p)
    R,P=({F(k):(i,tuple(tuple(map(int,z)) for z in v)) for i,(k,v) in enumerate(b[label])}
         for label in ('real','phase'))
    files=[]; leaves={}; groups=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(filetext(imports,OPT+body))
        files.append({'file':path.name,'sha256':sha(path)})
    # Each proof starts exactly at the seed and pays all 1200 terms.
    def leaf(kind,param,original_f=None):
        key=(kind,param)
        if key in leaves: return leaves[key]
        i,value=(R if kind=='Real' else P)[param]
        name=f'{kind}{i:04d}'; v='nf689'+name
        arg=(exact(param*F(11,20)),ZERO) if kind=='Real' else (ZERO,mul(p,exact(param/2)))
        ss=states(arg); small=tuple((m,r+1) for m,r in ss[N][1])
        end=zmul(small,small)
        if kind=='Phase': end=zmul(end,end)
        assert end==value
        body=f'def {v}Arg : NF591Rect := {rect(arg)}\ndef {v}Small : NF591Rect := {rect(small)}\ndef {v}Value : NF591Rect := {rect(value)}\n'
        body+=f'def {v}State0000 : NF633ExpState := {state(ss[0])}\n'
        body+=f'theorem {v}Seed : neutralNF633State {v}Arg neutralNF616Q 0={v}State0000 := by\n  apply neutralNF633StateEq_sound\n  decide +kernel\n\n'
        # Split modules per eight transitions for bounded elaboration and parallelizable group builds.
        prev=name+'Seed'
        write(prev,[BASE,PI],body)
        proof=f'{v}Seed'
        for block in range(0,N,256):
            mod=name+f'Part{block//256:02d}'; body=''
            for start in range(block,min(block+256,N),32):
                endn=min(start+32,N); length=endn-start
                st=f'{v}State{start:04d}'; en=f'{v}State{endn:04d}'
                gate=f'{v}Gate{endn:04d}'; nextproof=f'{v}Prefix{endn:04d}'
                body+=f'def {en} : NF633ExpState := {state(ss[endn])}\n'
                body+=f'theorem {gate} : neutralNF633StateEq (neutralNF633Segment {v}Arg neutralNF616Q {start} {st} {length}) {en}=true := by\n  decide +kernel\n'
                body+=f'theorem {nextproof} : neutralNF633State {v}Arg neutralNF616Q {endn}={en} :=\n  neutralNF633Prefix_extend {v}Arg neutralNF616Q {start} {length} {st} {en} {proof} {gate}\n\n'
                proof=nextproof
            write(mod,[MODULE+'.'+prev],body); prev=mod
        if kind=='Real':
            argexpr=f'NF591Rect.realQ ({qlit(param)}*11/20) neutralNF616Q'
            target=f'neutralNF621RealEndpoint {qlit(param)} neutralNF616Q neutralNF616ExpN'
            apply=f'neutralNF633RealEndpoint_of_small {qlit(param)} neutralNF616Q neutralNF616ExpN {v}Small {v}Value'
        else:
            assert reduced(original_f)==param
            argexpr=f'neutralNF592PhaseArg nf632Pi {qlit(original_f)} neutralNF616Q'
            target=f'neutralNF593Phase nf632Pi {qlit(original_f)} neutralNF616Q neutralNF616ExpN'
            apply=f'neutralNF633Phase_of_small nf632Pi {qlit(original_f)} neutralNF616Q neutralNF616ExpN {v}Small {v}Value'
        sq=f'({v}Small.mulQ {v}Small neutralNF616Q)'
        expr=sq if kind=='Real' else f'({sq}.mulQ {sq} neutralNF616Q)'
        body=f'theorem {v}ArgCheck : neutralNF633RectEq ({argexpr}) {v}Arg=true := by\n  decide +kernel\n'
        body+=f'theorem {v}SmallCheck : neutralNF633RectEq ({v}State{N:04d}.sumState.expand (1/(neutralNF616Q:ℚ))) {v}Small=true := by\n  decide +kernel\n'
        body+=f'theorem {v}ValueCheck : neutralNF633RectEq {expr} {v}Value=true := by\n  decide +kernel\n'
        body+=f'theorem {v}OriginalEq : {target}={v}Value := by\n  apply {apply}\n  · rw [neutralNF633RectEq_sound _ _ {v}ArgCheck]\n    exact neutralNF633SmallExp_of_state {v}Arg neutralNF616Q neutralNF616ExpN {v}State{N:04d} {v}Small {proof} {v}SmallCheck\n  · exact {v}ValueCheck\n'
        if kind=='Phase':
            body+=f'theorem {v}Reduced : neutralNF592Reduced {qlit(original_f)}={qlit(param)} := by\n  decide +kernel\n'
            body+=f'theorem {v}Eq : neutralNF634PhaseReduced nf632Pi {qlit(param)} neutralNF616Q neutralNF616ExpN={v}Value := by\n  rw [← {v}Reduced,neutralNF634PhaseReduced_eq]\n  exact {v}OriginalEq\n'
        else:
            body+=f'theorem {v}Eq : {target}={v}Value := {v}OriginalEq\n'
        body+=f'#print axioms {v}Eq'
        write(name,[MODULE+'.'+prev],body)
        leaves[key]=(name,v,i)
        return leaves[key]
    for label,k,count in cases:
        h,f=k; data=rows[k]
        assert len(data)==count and table(*k,count-1)==data
        rr=[(q,leaf('Real',q)) for q in (h,-h)]
        pp=[(reduced(q),leaf('Phase',reduced(q),q)) for q in (f,-f)]
        v='nf689'+label
        def lookup(s,pairs):
            body=f'def {v}{s} (q : ℚ) : NF591Rect :=\n'
            for key,l in dict(pairs).items(): body+=f'  if q={qlit(key)} then {l[1]}Value else\n'
            return body+'  NF591Rect.zero\n\n'
        body=lookup('R',rr)+lookup('P',pp)
        body+=f'def {v}Table : NF624KeyTable := ⟨{keylit(k)}, #[\n    '+',\n    '.join(map(rowlit,data))+'\n  ]⟩\n\n'
        proofs=[]
        for kind,pairs,exprs in [('R',rr,[v+'Table.key.h','(-'+v+'Table.key.h)']),
                                 ('P',pp,['neutralNF592Reduced '+v+'Table.key.f',
                                          'neutralNF592Reduced (-'+v+'Table.key.f)'])]:
            for j,((q,l),expr) in enumerate(zip(pairs,exprs)):
                n=v+kind+str(j); proofs.append(n+'Eq')
                body+=f'theorem {n}Param : {expr}={qlit(q)} := by\n  decide +kernel\n'
                body+=f'theorem {n}Check : neutralNF633RectEq ({v}{kind} {qlit(q)}) {l[1]}Value=true := by\n  decide +kernel\n'
                ref=(f'neutralNF621RealEndpoint ({expr}) neutralNF616Q neutralNF616ExpN' if kind=='R' else
                     f'neutralNF634PhaseReduced nf632Pi ({expr}) neutralNF616Q neutralNF616ExpN')
                body+=f'theorem {n}Eq : {v}{kind} ({expr})={ref} := by\n  rw [{n}Param]\n  exact (neutralNF633RectEq_sound _ _ {n}Check).trans {l[1]}Eq.symm\n\n'
        body+=f'theorem {v}Check : neutralNF634SharedKeyCheck nf632Pi {v}R {v}P {v}Table=true := by\n  decide +kernel\n\n'
        body+=f'''theorem {v}Moment (n : ℕ) (hn : n < {v}Table.rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) {v}Table.key.value n-
      (neutralNF617MomentRead {v}Table.rows n).value‖ ≤
      (neutralNF617MomentRead {v}Table.rows n).rad :=
  neutralNF648Moment_of_local nf632Pi {v}R {v}P {v}Table nf632PiEq
    {' '.join(proofs)} {v}Check n hn

#print axioms {v}Moment
'''
        imports=sorted({MODULE+'.'+l[0] for _,l in rr+pp})
        write(label,imports,body)
        groups.append({'group':label,'family':targetfamily[label],'key':[str(h),str(f)],'rows':count,'real':[l[2] for _,l in rr],'phase':[l[2] for _,l in pp]})
    assert sum(x['rows'] for x in groups)==sum(n for _,_,n in cases)
    expected_leaves={('Real',s*h) for _,(h,f),n in cases for s in (-1,1)}|{('Phase',reduced(s*f)) for _,(h,f),n in cases for s in (-1,1)}
    assert set(leaves)==expected_leaves
    assert len(groups)==len(cases)
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF689-ranked-phase-family-proposals-v1','full_plan_sha256':sha(planpath),'rows':sum(x['rows'] for x in groups),'groups':groups,'leaf_count':len(leaves),'selected_families':list(map(str,requested)),'previous_nf686_families':list(map(str,CERTIFIED_NF686_FAMILIES)),
        'prefix_checks':38*len(leaves),'input_sha256':hashes,'pi_manifest_sha256':sha(a.pi/'manifest.json'),
        'bank_manifest_sha256':sha(a.bank/'manifest.json'),'files':files,
        'scope':'untrusted proof proposals; full kernel truth pending'},indent=2)+'\n')
    print('NF689',len(leaves),'retained-value leaves;',sum(x['rows'] for x in groups),'actual moment rows; generated proofs only')
if __name__=='__main__': main()
