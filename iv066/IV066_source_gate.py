#!/usr/bin/env python3
"""IV066 source/receipt preflight; never confuses local static PASS with Lean PASS.

Usage:
  python iv066/IV066_source_gate.py --mode local --root .
  python iv066/IV066_source_gate.py --mode source --root .
  python iv066/IV066_source_gate.py --mode receipts --root . --axiom-log /tmp/IV066_axioms.log
The source mode requires the original pinned repository checkout.
"""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path

PINNED_GIT_HEAD = '614ba879f7389fdb620c474adaee273b00eac71c'
PINNED_TOOLCHAIN = 'leanprover/lean4:v4.34.0'
SOURCE_BLOBS = {
 'WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean': '0034976fe2f1e5fa9d411108736160542eb94293',
 'WeilDefect/External/Zeta23/Theorems/Thm_Zeta23_WeilEF_EF_lit_zeta.lean': 'b3a9159178cefd7f3817bbe6e2a19b52414e1566',
 'WeilDefect/Arithmetic/ActualZetaLiteralFormula.lean': 'b52b130605be6b564e31bb91afb0f47d24009451',
 'WeilDefect/Arithmetic/ActualZetaPrimeTransport.lean': 'f27b56c4ec5eca8739e2ccf1e44057b037ad1724',
 'WeilDefect/Arithmetic/ActualZetaArchimedeanCoordinates.lean': 'cc5041cda1d1cf91ef30c6319dbe0a9c264b4871',
 'WeilDefect/Arithmetic/ActualZetaNativeWeilForm.lean': '961b6742782fa3f808ac9b70cfadfc0790c8fc32',
 'WeilDefect/Morphology/NeutralLogPoleSourceAttachment.lean': '331ad94a02336a124eb6c17e3ee94480694a8c5c',
 'WeilDefect/Morphology/NeutralWeilMultiplier.lean': '4c24084c8a058cbb6685d54bc8226b746cabc413',
}
LEAN_PATH='WeilDefect/Arithmetic/IV066OriginalSourcePilot.lean'
AXIOM_PATH='verification/IV066AxiomAudit.lean'
THEOREMS = (
 'iv066_sourceCorrelation_orientation',
 'iv066_original_general_source_summable',
 'iv066_original_general_source_signed',
 'iv066_original_mixed_weilTest_signed',
 'iv066_gamma_literal_native',
 'iv066_native_signed_multiplier',
)
ALLOWED_AXIOMS = {'propext','Quot.sound','Classical.choice'}

def sha256(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args,root):
 p=subprocess.run(['git',*args],cwd=root,check=True,text=True,capture_output=True)
 return p.stdout.strip()

def local(root):
 script=root/LEAN_PATH
 audit=root/AXIOM_PATH
 assert script.is_file() and audit.is_file(), 'missing Lean source/audit'
 t=script.read_text()
 for theorem in THEOREMS:
  assert re.search(r'(?m)^theorem\s+'+re.escape(theorem)+r'\b',t),f'missing {theorem}'
  assert f'#print axioms WeilDefect.{theorem}' in audit.read_text()
 assert not re.search(r'(?m)^\s*(?:sorry|admit|axiom)\b',t), 'inadmissible Lean proof escape'
 assert 'Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam' in t, 'missing actual upstream imported theorem'
 assert 'Zeta23.EF.weilTest g f' in t, 'lost mixed orientation'
 assert 'neutralActualZetaGammaBracket_native' in t
 print('IV066 LOCAL STATIC PREFLIGHT PASS; NOT A LEAN KERNEL RESULT')
 print('IV066 Lean source SHA256:', sha256(script))
 print('IV066 axiom source SHA256:', sha256(audit))
 return {'lean_sha256':sha256(script),'axiom_sha256':sha256(audit)}

def source(root):
 assert (root/'lean-toolchain').read_text().strip()==PINNED_TOOLCHAIN
 assert 'v4.34.0' in (root/'lakefile.toml').read_text()
 for path,digest in SOURCE_BLOBS.items():
  actual=git('hash-object',path,root=root)
  assert actual==digest, f'upstream source mismatch {path}: {actual} != {digest}'
 commit=git('rev-parse','HEAD',root=root)
 ancestor=subprocess.run(['git','merge-base','--is-ancestor',PINNED_GIT_HEAD,commit],cwd=root)
 assert ancestor.returncode==0, 'the pinned original IV023 commit is not an ancestor of this checkout'
 print('IV066 PINNED-SOURCE PREFLIGHT PASS; NOT A LEAN KERNEL RESULT')
 return {'git_commit':commit,'verified_blobs':SOURCE_BLOBS}

def receipts(root,axiom_log):
 source_file=root/LEAN_PATH
 assert source_file.is_file()
 olen=root/'.lake/build/lib/lean/WeilDefect/Arithmetic/IV066OriginalSourcePilot.olean'
 assert olen.exists() and olen.stat().st_size>0, f'nonempty .olean absent: {olen}'
 log=Path(axiom_log).read_text()
 found={}
 for theorem in THEOREMS:
  fullname='WeilDefect.'+theorem
  pat=rf"'{re.escape(fullname)}' depends on axioms: \[([^\]]*)\]"
  match=re.search(pat,log)
  if match:
   axioms={x.strip() for x in match.group(1).split(',') if x.strip()}
  else:
   assert re.search(rf"'{re.escape(fullname)}' does not depend on any axioms",log),f'missing axioms result: {fullname}'
   axioms=set()
  assert axioms<=ALLOWED_AXIOMS, f'NONSTANDARD AXIOMS for {theorem}: {axioms-ALLOWED_AXIOMS}'
  found[theorem]=sorted(axioms)
 return {'stage':'IV066','standing':'LEAN PASSED WITH STRICT AXIOM AUDIT',
         'commit_sha':git('rev-parse','HEAD',root=root),
         'source_sha256':sha256(source_file),
         'olean_size':olen.stat().st_size,'olean_sha256':sha256(olen),
         'axiom_log_sha256':sha256(Path(axiom_log)),
         'axiom_results':found}

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--mode',choices=['local','source','receipts'],required=True)
 ap.add_argument('--root',type=Path,default=Path('.'))
 ap.add_argument('--axiom-log')
 ap.add_argument('--output',type=Path)
 args=ap.parse_args()
 root=args.root.resolve()
 if args.mode=='local':result=local(root)
 elif args.mode=='source':result=source(root)
 else:
  assert args.axiom_log,'--axiom-log required for receipts'
  result=receipts(root,args.axiom_log)
  print('IV066 STRICT LEAN/KERNEL AUDIT PASS')
 if args.output:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')

if __name__=='__main__':main()
