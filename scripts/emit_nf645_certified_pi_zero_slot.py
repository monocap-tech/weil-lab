#!/usr/bin/env python3
"""Bind the accepted NF632 pi literal and prove the actual NF635 zero real slot.
Independent of the newer segmented exponential and stable-tail modules.
"""
import argparse,gzip,hashlib,json,re
from fractions import Fraction as F
from pathlib import Path
from emit_nf627_original_moment_bank import filetext
from emit_nf633_segmented_exp import rect,ball,states
from verify_nf620_physical_key_tables import Q,N,ZERO,zmul,pi
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalCertifiedPiZeroSlot'
MODULE='WeilDefect.Generated.NF645'
BANK='WeilDefect.Generated.NF635.Banks'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(path):
    m=json.loads((path/'manifest.json').read_text())
    for x in m['files']:
        assert sha(path/x['file'])==x['sha256']
    return m
def main():
    ap=argparse.ArgumentParser()
    for x in ('bank','pi','output'): ap.add_argument('--'+x,type=Path,required=True)
    a=ap.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    b=validate(a.bank); p=validate(a.pi)
    assert b['full_values'] and (b['real_count'],b['phase_count'])==(5,1276)
    assert p['full'] and len(p['files'])==127
    with gzip.open(a.bank/'endpoints.json.gz','rt') as f: retained=json.load(f)
    assert retained['schema']=='NF635-original-shared-endpoints-v1'
    pp=tuple(map(int,retained['pi']))
    assert pp==pi() and pp[1]==39942
    # Compare the retained original certified Pi module literal, not a fresh approximation.
    literal=re.search(r'def nf632Pi : NF591Ball := ⟨\((-?\d+):ℚ\)/neutralNF616Q,\((-?\d+):ℚ\)/neutralNF616Q⟩',(a.pi/'Pi.lean').read_text())
    assert literal and tuple(map(int,literal.groups()))==pp
    files=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(filetext(imports,OPT+body))
        files.append({'file':path.name,'sha256':sha(path)})
    body='''theorem nf645PiLiteralCheck : neutralNF632BallEq nf632Pi nf635Pi=true := by
  decide +kernel

theorem nf645BankPiEq : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=nf635Pi :=
  nf632PiEq.trans (neutralNF632BallEq_sound _ _ nf645PiLiteralCheck)

theorem nf645BankPiSound : nf635Pi.Contains Real.pi := neutralNF632HighPrecisionPi_sound _ nf645BankPiEq

#print axioms nf645BankPiEq
#print axioms nf645BankPiSound
'''
    write('PiAttach',['WeilDefect.Generated.NF632.Pi',BANK],body)
    z=retained['real'][2]
    assert F(z[0])==0
    endpoint=tuple(tuple(map(int,v)) for v in z[1])
    ss=states((ZERO,ZERO))
    partial=ss[2][1]; terminal=ss[N][1]
    assert partial==((Q,3),(0,3))
    expanded=tuple((m,r+2*(N-2)+1) for m,r in partial)
    assert expanded==tuple((m,r+1) for m,r in terminal)
    assert zmul(expanded,expanded)==endpoint
    assert endpoint==((Q,4804),(0,4804))
    body=f'def nf645ZeroPartial2 : NF591Rect := {rect(partial)}\ndef nf645ZeroValue : NF591Rect := {rect(endpoint)}\n\n'
    body+='''theorem nf645ZeroPartialCheck : neutralNF645RectEq
    (neutralNF592ExpPartial NF591Rect.zero neutralNF616Q 2) nf645ZeroPartial2=true := by
  decide +kernel

theorem nf645ZeroSquareCheck : neutralNF645RectEq
    ((nf645ZeroPartial2.expand (2*(1198:ℚ)/neutralNF616Q+1/(neutralNF616Q:ℚ))).mulQ
      (nf645ZeroPartial2.expand (2*(1198:ℚ)/neutralNF616Q+1/(neutralNF616Q:ℚ))) neutralNF616Q)
    nf645ZeroValue=true := by
  decide +kernel

theorem nf645ZeroEq : neutralNF635RealRef 0=nf645ZeroValue :=
  neutralNF645ZeroSlot _ _ nf645ZeroPartialCheck nf645ZeroSquareCheck

#print axioms nf645ZeroEq
'''
    write('Zero',[BASE],body)
    body='''theorem nf645ZeroKeyCheck : decide (neutralNF635ParamRead nf635RealBank.keys 2=0)=true := by
  decide +kernel

theorem nf645ZeroStoredCheck : neutralNF645RectEq (nf635RealBank.read 2) nf645ZeroValue=true := by
  decide +kernel

theorem nf645ZeroAttached : nf635RealBank.read 2=neutralNF635RealRef
    (neutralNF635ParamRead nf635RealBank.keys 2) :=
  neutralNF645Zero_attach _ _ _ nf645ZeroKeyCheck nf645ZeroStoredCheck nf645ZeroEq

#print axioms nf645ZeroAttached
'''
    write('ZeroAttach',[MODULE+'.Zero',BANK],body)
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF645-certified-pi-zero-slot-proposals-v1',
        'pi_manifest_sha256':sha(a.pi/'manifest.json'),'bank_manifest_sha256':sha(a.bank/'manifest.json'),
        'files':files,'scope':'literal attachment proofs pending current-head kernel build'},indent=2)+'\n')
    print('NF645 exact pi literal match and zero endpoint replay PASS; emitted three kernel attachment proposals')
if __name__=='__main__': main()
