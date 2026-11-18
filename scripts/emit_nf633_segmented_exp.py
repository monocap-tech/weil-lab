#!/usr/bin/env python3
"""Propose exact rounded Taylor states for one genuine pole and oscillator phase.
Pilot proofs check literal local transitions only. Full proposals link all
prefixes and the original input (phase attachment needs the NF632 pi proof).
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from verify_nf620_physical_key_tables import Q,N,ZERO,ONE,zmul,zadd,div,exact,mul,pi,reduced
sys.set_int_max_str_digits(0)
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedExp'
MODULE='WeilDefect.Generated.NF633'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'

def ball(a): return f'⟨({a[0]}:ℚ)/neutralNF616Q,({a[1]}:ℚ)/neutralNF616Q⟩'
def rect(a): return '⟨'+','.join(map(ball,a))+'⟩'
def state(a): return '⟨'+','.join(map(rect,a))+'⟩'
def step(s,a,n):
    t,p=s
    u=zmul(t,a)
    return (div(u[0],n+1),div(u[1],n+1)),zadd(p,t)
def states(a):
    s=((ONE,ZERO),(ZERO,ZERO))
    out=[s]
    for n in range(N):
        s=step(s,a,n)
        out.append(s)
    return out

def emit(out,chunk,full):
    assert 0<chunk<N
    out.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        path=out/(name+'.lean')
        path.write_text(''.join('import '+x+'\n' for x in imports)+'\nnamespace WeilDefect\n\n'+OPT+body+'\nend WeilDefect\n')
        files.append({'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    cases={'Pole':(exact(F(11,20)),ZERO),
           'Phase':(ZERO,mul(pi(),exact(reduced(F(37,32))/2)))}
    for label,a in cases.items():
        ss=states(a)
        b=tuple((m,r+1) for m,r in ss[N][1])
        e=zmul(b,b)
        if label=='Phase': e=zmul(e,e)
        inp='nf633'+label+'Arg'
        name=label+'Arg'
        write(name,[BASE],f'def {inp} : NF591Rect := {rect(a)}\n')
        if not full:
            for start in (0,N-chunk):
                v=f'nf633{label}{start:04d}'
                body=f'def {v}Start : NF633ExpState := {state(ss[start])}\n'
                body+=f'def {v}End : NF633ExpState := {state(ss[start+chunk])}\n\n'
                body+=f'theorem {v}Check : neutralNF633StateEq\n'
                body+=f'    (neutralNF633Segment {inp} neutralNF616Q {start} {v}Start {chunk}) {v}End = true := by\n  decide +kernel\n\n#print axioms {v}Check\n'
                write(label+f'Pilot{start:04d}',[MODULE+'.'+name],body)
            continue
        prev=None
        for start in range(0,N,chunk):
            length=min(chunk,N-start)
            name=label+f'Segment{start:04d}'
            v='nf633'+name
            startname='nf633'+prev+'End' if prev else f'{v}Start'
            ph='nf633'+prev+'PrefixEq' if prev else '(by rfl)'
            body='' if prev else f'def {startname} : NF633ExpState := ⟨NF591Rect.one,NF591Rect.zero⟩\n'
            body+=f'def {v}End : NF633ExpState := {state(ss[start+length])}\n\n'
            body+=f'theorem {v}Check : neutralNF633StateEq\n'
            body+=f'    (neutralNF633Segment {inp} neutralNF616Q {start} {startname} {length}) {v}End = true := by\n  decide +kernel\n\n'
            body+=f'theorem {v}PrefixEq : neutralNF633State {inp} neutralNF616Q {start+length}={v}End :=\n'
            body+=f'  neutralNF633Prefix_extend {inp} neutralNF616Q {start} {length} {startname} {v}End {ph} {v}Check\n'
            write(name,[MODULE+'.'+(prev or label+'Arg')],body)
            prev=name
        v='nf633'+prev
        small='nf633'+label+'Small'
        ep='nf633'+label+'Endpoint'
        body=f'def {small} : NF591Rect := {rect(b)}\n'
        body+=f'def {ep} : NF591Rect := {rect(e)}\n\n'
        body+=f'theorem {small}Check : neutralNF633RectEq\n'
        body+=f'    ({v}End.sumState.expand (1/(neutralNF616Q:ℚ))) {small}=true := by\n  decide +kernel\n\n'
        body+=f'theorem {small}Eq : neutralNF593SmallExp {inp} neutralNF616Q neutralNF616ExpN={small} :=\n'
        body+=f'  neutralNF633SmallExp_of_state {inp} neutralNF616Q neutralNF616ExpN {v}End {small} {v}PrefixEq {small}Check\n\n'
        sq=f'({small}.mulQ {small} neutralNF616Q)'
        expr=sq if label=='Pole' else f'({sq}.mulQ {sq} neutralNF616Q)'
        body+=f'theorem {ep}Check : neutralNF633RectEq {expr} {ep}=true := by\n  decide +kernel\n\n'
        imports=[MODULE+'.'+prev]
        if label=='Pole':
            arg=f'NF591Rect.realQ ((1:ℚ)*11/20) neutralNF616Q'
            params='(1:ℚ)'
            thm='neutralNF633RealEndpoint_of_small'
            target='neutralNF621RealEndpoint 1 neutralNF616Q neutralNF616ExpN'
        else:
            imports.append('WeilDefect.Generated.NF632.Pi')
            arg='neutralNF592PhaseArg nf632Pi (37/32) neutralNF616Q'
            params='nf632Pi (37/32)'
            thm='neutralNF633Phase_of_small'
            target='neutralNF593Phase nf632Pi (37/32) neutralNF616Q neutralNF616ExpN'
        body+=f'theorem {inp}Check : neutralNF633RectEq ({arg}) {inp}=true := by\n  decide +kernel\n\n'
        body+=f'theorem {ep}Eq : {target}={ep} := by\n'
        body+=f'  apply {thm} {params} neutralNF616Q neutralNF616ExpN {small} {ep}\n'
        body+=f'  · rw [neutralNF633RectEq_sound _ _ {inp}Check]\n    exact {small}Eq\n  · exact {ep}Check\n\n'
        body+=f'#print axioms {ep}Eq\n'
        write(label+'Complete',imports,body)
    (out/'manifest.json').write_text(json.dumps({'schema':'NF633-exp-state-proposals-v1','full':full,'chunk':chunk,
        'files':files,'scope':'literal local transition proposals; no automatic analytic truth'},indent=2)+'\n')
    print('NF633',len(files),'modules; full=',full)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--chunk',type=int,default=32)
    p.add_argument('--full',action='store_true')
    a=p.parse_args()
    emit(a.output,a.chunk,a.full)
if __name__=='__main__': main()
