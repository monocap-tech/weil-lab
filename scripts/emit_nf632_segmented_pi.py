#!/usr/bin/env python3
"""Generate original 2600-digit Machin segments with separate kernel gates.

The producer is untrusted. Full proof uses the reference segment
recurrence and local exact equality checks, not the producer's assertion.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(0)
Q=10**2600
N=2000
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedPi'
MODULE='WeilDefect.Generated.NF632'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'

def ball(m,r):
    return f'⟨({m}:ℚ)/neutralNF616Q,({r}:ℚ)/neutralNF616Q⟩'

def segment(p,start,length):
    m=r=0
    power=p**(2*start+1)
    for n in range(start,start+length):
        numer=Q if n%2==0 else -Q
        a,b=divmod(numer,power*(2*n+1))
        m+=a; r+=int(b!=0)
        power*=p*p
    return m,r

def emit(out,chunk,full):
    assert 0<chunk<=N
    out.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        path=out/(name+'.lean')
        path.write_text(''.join('import '+x+'\n' for x in imports)+
                        '\nnamespace WeilDefect\n\n'+OPT+body+'\nend WeilDefect\n')
        files.append({'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    if not full:
        # Beginning and terminal original segments for both denominators.
        for p in (5,239):
            for start in (0,N-chunk):
                m,r=segment(p,start,chunk)
                name=f'Pilot{p}_{start}'
                v='nf632'+name
                write(name,[BASE],f'def {v} : NF591Ball := {ball(m,r)}\n\n'
                    f'theorem {v}Check : neutralNF632BallEq\n'
                    f'    (neutralNF632AtanSegment (1/{p}) neutralNF616Q {start} {chunk}) {v} = true := by\n'
                    f'  decide +kernel\n\n#print axioms {v}Check\n')
    else:
        last=[]; sums=[]
        for p in (5,239):
            prev=None; total=(0,0)
            for start in range(0,N,chunk):
                length=min(chunk,N-start)
                m,r=segment(p,start,length)
                total=(total[0]+m,total[1]+r)
                name=f'Atan{p}_{start:04d}'
                v='nf632'+name
                pv=('nf632'+prev+'Prefix') if prev else '⟨0,0⟩'
                ph=('nf632'+prev+'PrefixEq') if prev else '(by rfl)'
                imports=[BASE] if not prev else [MODULE+'.'+prev]
                body=f'def {v}Segment : NF591Ball := {ball(m,r)}\n'
                body+=f'def {v}Prefix : NF591Ball := {ball(*total)}\n\n'
                body+=f'theorem {v}SegmentCheck : neutralNF632BallEq\n'
                body+=f'    (neutralNF632AtanSegment (1/{p}) neutralNF616Q {start} {length}) {v}Segment = true := by\n  decide +kernel\n\n'
                body+=f'theorem {v}AddCheck : neutralNF632BallEq\n'
                body+=f'    (NF591Ball.add {pv} {v}Segment) {v}Prefix = true := by\n  decide +kernel\n\n'
                body+=f'theorem {v}PrefixEq : neutralNF592AtanPartial (1/{p}) neutralNF616Q {start+length} = {v}Prefix :=\n'
                body+=f'  neutralNF632AtanPrefix_extend (1/{p}) neutralNF616Q {start} {length}\n'
                body+=f'    {pv} {v}Segment {v}Prefix {ph} {v}SegmentCheck {v}AddCheck\n'
                write(name,imports,body); prev=name
            assert total==segment(p,0,N)
            last.append(prev); sums.append(total)
        a,b=sums
        m=16*a[0]-4*b[0]
        r=16*(a[1]+1)+4*(b[1]+1)+2
        assert r==39942
        v,w=('nf632'+s for s in last)
        body=f'def nf632Pi : NF591Ball := {ball(m,r)}\n\n'
        body+=f'theorem nf632PiCheck : neutralNF632BallEq\n'
        body+=f'    (neutralNF632PiFromPartials {v}Prefix {w}Prefix neutralNF616Q) nf632Pi = true := by\n  decide +kernel\n\n'
        body+='theorem nf632PiEq : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=nf632Pi :=\n'
        body+=f'  neutralNF632Pi_of_partials neutralNF616Q neutralNF616AtanN\n    {v}Prefix {w}Prefix nf632Pi {v}PrefixEq {w}PrefixEq nf632PiCheck\n\n'
        body+='theorem nf632PiSound : nf632Pi.Contains Real.pi := neutralNF632HighPrecisionPi_sound _ nf632PiEq\n\n#print axioms nf632PiEq\n#print axioms nf632PiSound\n'
        write('Pi', [MODULE+'.'+s for s in last],body)
    (out/'manifest.json').write_text(json.dumps({'schema':'NF632-pi-segment-proposals-v1',
        'full':full,'chunk':chunk,'files':files,'scope':'untrusted proposals pending kernel truth'},indent=2)+'\n')
    print('NF632',len(files),'literal proposal modules; full=',full)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--chunk',type=int,default=32)
    p.add_argument('--full',action='store_true')
    a=p.parse_args()
    emit(a.output,a.chunk,a.full)
if __name__=='__main__': main()
