#!/usr/bin/env python3
"""Generate real original integer Taylor segment trials, with reference states
from the existing exact external replay. No Lean truth asserted by emission."""
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from emit_nf633_segmented_exp import states
from verify_nf620_physical_key_tables import Q,N,ZERO,exact,mul,pi,reduced

BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerTaylor'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'

def ball(a): return f'⟨({a[0]}:ℤ),({a[1]}:ℤ)⟩'
def rect(a): return '⟨'+','.join(map(ball,a))+'⟩'
def state(a): return '⟨'+','.join(map(rect,a))+'⟩'

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--chunk',type=int,default=32)
    a=p.parse_args()
    assert 0<a.chunk<N
    a.output.mkdir(parents=True,exist_ok=True)
    records=[]
    args={'Pole':(exact(F(11,20)),ZERO),
          'Phase':(ZERO,mul(pi(),exact(reduced(F(37,32))/2)))}
    for label,arg in args.items():
        ss=states(arg)
        for start in (0,N-a.chunk):
            name=f'{label}{start:04d}'
            v='nf636'+name
            end=ss[start+a.chunk]
            t,p=end
            # Corrupt one coordinate of the actual terminal state.
            bad=(((t[0][0]+1,t[0][1]),t[1]),p)
            body=f'import {BASE}\n\nnamespace WeilDefect\n\n'+OPT
            body+=f'def {v}Arg : NF636Rect := {rect(arg)}\n'
            body+=f'def {v}Start : NF636State := {state(ss[start])}\n'
            body+=f'def {v}End : NF636State := {state(end)}\n'
            body+=f'def {v}Bad : NF636State := {state(bad)}\n\n'
            body+=f'theorem {v}Check : neutralNF636TransitionCheck {v}Arg neutralNF616Q {start} {a.chunk} {v}Start {v}End=true := by\n  decide +kernel\n\n'
            body+=f'theorem {v}Reject : neutralNF636TransitionCheck {v}Arg neutralNF616Q {start} {a.chunk} {v}Start {v}Bad=false := by\n  decide +kernel\n\n'
            body+=f'#print axioms {v}Check\n#print axioms {v}Reject\n\nend WeilDefect\n'
            path=a.output/(name+'.lean')
            path.write_text(body)
            records.append({'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF636-integer-segment-proposals-v1',
        'chunk':a.chunk,'files':records,'scope':'local transitions only; terminal start states not yet certified'},indent=2)+'\n')
    print('NF636 four real source transitions and four corrupted state rejection proposals')
if __name__=='__main__': main()
