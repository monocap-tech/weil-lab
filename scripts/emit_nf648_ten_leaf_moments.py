#!/usr/bin/env python3
"""Generate exactly ten retained endpoint leaves and three full rational moment proofs.
All numerical data are checked against the immutable NF635 and NF621 inputs.
The generated proofs use the already accepted NF633 and NF634 references,
not the optional tail or integer evaluator. No full bank is imported."""
import argparse
import gzip
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path
from emit_nf633_segmented_exp import states, state, rect
from emit_nf627_original_moment_bank import filetext, qlit, keylit, rowlit
from verify_nf620_physical_key_tables import N, ZERO, exact, mul, pi, reduced, zmul, table
from verify_nf622_physical_entry_reassembly import read_shards
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRationalLocalMoment'
MODULE='WeilDefect.Generated.NF648'
PI='WeilDefect.Generated.NF632.Pi'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
CASES=[('Pole',(F(1),F(0)),1),('Osc',(F(0),F(37,32)),27),('Mixed',(F(1,2),F(37,64)),14)]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(d):
    m=json.loads((d/'manifest.json').read_text())
    for x in m['files']: assert sha(d/x['file'])==x['sha256']
    return m
def main():
    ap=argparse.ArgumentParser()
    for k in ('root','shards','bank','pi','output'): ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--group',choices=[x[0] for x in CASES])
    a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    bm,pm=validate(a.bank),validate(a.pi)
    assert bm['full_values'] and (bm['real_count'],bm['phase_count'])==(5,1276)
    assert pm['full'] and len(pm['files'])==127
    hashes={p.name:sha(p) for p in a.shards.rglob('nf621-shard*.json.gz')}
    assert len(hashes)==8 and hashes==bm['input_sha256']
    rows=read_shards(a.root,a.shards)
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
        name=f'{kind}{i:04d}'; v='nf648'+name
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
    for label,k,count in CASES:
        if a.group and a.group!=label: continue
        h,f=k; data=rows[k]
        assert len(data)==count and table(*k,count-1)==data
        rr=[(q,leaf('Real',q)) for q in (h,-h)]
        pp=[(reduced(q),leaf('Phase',reduced(q),q)) for q in (f,-f)]
        v='nf648'+label
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
        groups.append({'group':label,'rows':count,'real':[l[2] for _,l in rr],'phase':[l[2] for _,l in pp]})
    if not a.group: assert len(leaves)==10 and sum(x['rows'] for x in groups)==42
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF648-ten-leaf-local-moment-proposals-v1',
        'group':a.group,'rows':sum(x['rows'] for x in groups),'groups':groups,'leaf_count':len(leaves),
        'prefix_checks':38*len(leaves),'input_sha256':hashes,'pi_manifest_sha256':sha(a.pi/'manifest.json'),
        'bank_manifest_sha256':sha(a.bank/'manifest.json'),'files':files,
        'scope':'untrusted proof proposals; full kernel truth pending'},indent=2)+'\n')
    print('NF648',len(leaves),'retained-value leaves;',sum(x['rows'] for x in groups),'actual moment rows; generated proofs only')
if __name__=='__main__': main()
