#!/usr/bin/env python3
"""Use the retained successful NF633 producer artifacts and NF632 pi proof.
No new Taylor evaluator or stable-tail dependency. Bind two full nonzero
reference endpoint proofs directly to the actual NF635 indexed bank.
"""
import argparse
import gzip
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path
from emit_nf627_original_moment_bank import filetext
from verify_nf620_physical_key_tables import reduced
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
BANK='WeilDefect.Generated.NF635.Banks'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(d):
    m=json.loads((d/'manifest.json').read_text())
    for x in m['files']:
        assert sha(d/x['file'])==x['sha256']
    return m
def coordinates(path,name,arity):
    t=path.read_text()
    line=next(s for s in t.splitlines() if s.startswith('def '+name+' :'))
    vals=list(map(int,re.findall(r'\((-?\d+):ℚ\)/neutralNF616Q',line)))
    assert len(vals)==arity
    return vals
def main():
    p=argparse.ArgumentParser()
    for k in ('pi','exp','bank','output'): p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    pm,em,bm=map(manifest,(a.pi,a.exp,a.bank))
    assert pm['full'] and len(pm['files'])==127
    assert em['full'] and em['chunk']==32 and len(em['files'])==80
    assert bm['full_values'] and (bm['real_count'],bm['phase_count'])==(5,1276)
    with gzip.open(a.bank/'endpoints.json.gz','rt') as f: b=json.load(f)
    assert b['schema']=='NF635-original-shared-endpoints-v1'
    assert b['scale']=='10^2600'
    assert coordinates(a.pi/'Pi.lean','nf632Pi',2)==list(map(int,b['pi']))
    u=reduced(F(37,32)); assert u==F(87,320)
    ri=next(i for i,(k,v) in enumerate(b['real']) if F(k)==1)
    pi=next(i for i,(k,v) in enumerate(b['phase']) if F(k)==u)
    assert (ri,pi)==(4,986)
    for label,table,i in [('Pole','real',ri),('Phase','phase',pi)]:
        literal=coordinates(a.exp/(label+'Complete.lean'),'nf633'+label+'Endpoint',4)
        assert literal==[int(x) for v in b[table][i][1] for x in v]
    outputs=[]
    def write(name,imports,body):
        d=a.output/(name+'.lean')
        d.write_text(filetext(imports,OPT+body))
        outputs.append({'file':d.name,'sha256':sha(d)})
    body='''theorem nf646PoleKey : decide (neutralNF635ParamRead nf635RealBank.keys 4 = 1)=true := by
  decide +kernel

theorem nf646PoleValue : neutralNF633RectEq (nf635RealBank.read 4) nf633PoleEndpoint=true := by
  decide +kernel

theorem nf646PoleAttached : nf635RealBank.read 4 =
    neutralNF635RealRef (neutralNF635ParamRead nf635RealBank.keys 4) := by
  rw [of_decide_eq_true nf646PoleKey]
  exact (neutralNF633RectEq_sound _ _ nf646PoleValue).trans nf633PoleEndpointEq.symm

#print axioms nf646PoleAttached
'''
    write('PoleAttach',['WeilDefect.Generated.NF633.PoleComplete',BANK],body)
    body='''theorem nf646PiCheck : neutralNF632BallEq nf632Pi nf635Pi=true := by
  decide +kernel

theorem nf646BankPiEq : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=nf635Pi :=
  nf632PiEq.trans (neutralNF632BallEq_sound _ _ nf646PiCheck)

theorem nf646ReducedCheck : decide (neutralNF592Reduced (37/32)=87/320)=true := by
  decide +kernel

theorem nf646PhaseRefEq : neutralNF635PhaseRef nf635Pi (87/320)=nf633PhaseEndpoint := by
  rw [← neutralNF632BallEq_sound _ _ nf646PiCheck,
      ← of_decide_eq_true nf646ReducedCheck]
  exact (neutralNF634PhaseReduced_eq nf632Pi (37/32) neutralNF616Q neutralNF616ExpN).trans
    nf633PhaseEndpointEq

theorem nf646PhaseKey : decide (neutralNF635ParamRead nf635PhaseBank.keys 986 = 87/320)=true := by
  decide +kernel

theorem nf646PhaseValue : neutralNF633RectEq (nf635PhaseBank.read 986) nf633PhaseEndpoint=true := by
  decide +kernel

theorem nf646PhaseAttached : nf635PhaseBank.read 986 =
    neutralNF635PhaseRef nf635Pi (neutralNF635ParamRead nf635PhaseBank.keys 986) := by
  rw [of_decide_eq_true nf646PhaseKey]
  exact (neutralNF633RectEq_sound _ _ nf646PhaseValue).trans nf646PhaseRefEq.symm

#print axioms nf646BankPiEq
#print axioms nf646PhaseAttached
'''
    write('PhaseAttach',['WeilDefect.Generated.NF633.PhaseComplete',BANK],body)
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF646-retained-nonzero-endpoint-pilots-v1',
        'inputs':{k:sha(d/'manifest.json') for k,d in [('pi',a.pi),('exp',a.exp),('bank',a.bank)]},
        'real_slot':ri,'phase_slot':pi,'reduced_parameter':str(u),
        'files':outputs,'scope':'conditional on complete kernel builds; no proof asserted by emitter'},indent=2)+'\n')
    print('NF646 retained pi and two nonzero endpoint literal matches PASS; emitted direct attachment proposals')
if __name__=='__main__': main()
