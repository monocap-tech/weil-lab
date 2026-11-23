#!/usr/bin/env python3
"""CP-C1(H2) original frozen integral Lean 4.34 strict receipt gate.

Source inventory is NOT a Lean theorem receipt. Run after a genuine H1 kernel pass.
"""
from __future__ import annotations
import argparse,hashlib,json,re
from pathlib import Path

ROOT=Path('WeilDefect/Arithmetic')
SOURCE=ROOT/'CP_C1H2_OriginalFrozenCorrelationIntegrals.lean'
H1=ROOT/'CP_C1H_OriginalPointwisePrimeCorrelation.lean'
FG=ROOT/'CP_C1FG_FrozenTargetAndRadiusGlue.lean'
E=ROOT/'CP_C1E_FrozenFlatSchwartz.lean'
OBJ=Path('.lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1H2_OriginalFrozenCorrelationIntegrals.olean')
H1OBJ=Path('.lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1H_OriginalPointwisePrimeCorrelation.olean')
LOG=Path('cpc1h2-original-kernel-axioms.log')
H1RECEIPT=Path('cpc1h1-original-kernel-receipt.json')
OUT=Path('cpc1h2-original-kernel-receipt.json')
PINS={
 H1:'956fef92e4fd5f78fd637f92311a6e16fc7997ab',
 FG:'befea449e7e166a31d6ee108e732666ebec76487',
 E:'29e68fe77e18d6e7b6b2c46bac6084beb4f18307',
}
NEW=[
 'neutralCPC1H_positiveShift_integral',
 'neutralCPC1H_negativeShift_integral',
 'neutralCPC1HLeft_supportedLC',
 'neutralCPC1HRight_supportedRC',
 'neutralCPC1HLeft_real',
 'neutralCPC1HRight_real',
 'neutralCPC1H_overlap_shift',
 'neutralCPC1H_overlap_as_real',
 'neutralCPC1H_plus_correlation',
 'neutralCPC1H_minus_correlation',
 'neutralCPC1H_prime_phase_unconditional',
 'neutralCPC1H_signed_prime_phase_unconditional',
]
UPSTREAM=['neutralNF600Correlation_eq','neutralNF600Prime_single',
          'neutralCPC1H_positiveShift_pointwise','neutralCPC1H_negativeShift_pointwise']
AXIOMS=UPSTREAM+NEW
GOOD={'propext','Classical.choice','Quot.sound'}
PAT=re.compile(r"'WeilDefect\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|(does not depend on any axioms))",re.S)

def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p:Path)->str:
 b=p.read_bytes()
 return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def preflight():
 s=SOURCE.read_text()
 assert s.startswith('import WeilDefect.Arithmetic.CP_C1H_OriginalPointwisePrimeCorrelation\n')
 found=re.findall(r'(?m)^theorem (neutralCPC1H\w+)\b',s)
 assert found==NEW,('declaration inventory drift',found)
 prints=re.findall(r'(?m)^#print axioms (\w+)\s*$',s)
 assert prints==AXIOMS,('axiom inventory drift',prints)
 assert s.rstrip().endswith('end\nend WeilDefect')
 assert not re.search(r'\b(sorry|admit|sorryAx|native_decide)\b',s)
 assert not re.search(r'(?m)^\s*(?:axiom|constant|opaque|unsafe)\b',s)
 assert Path('lean-toolchain').read_text().strip()=='leanprover/lean4:v4.34.0'
 for p,pin in PINS.items():assert blob(p)==pin,('upstream Lean blob drift',str(p),blob(p),pin)
 print('CP-C1(H2) 12 new original source declarations, 16 axiom print requests and three original source pins PASS; NOT LEAN')
def parse(raw):
 assert not re.search(r'error:|##\[error\]|sorryAx|unsolved goals',raw,re.I)
 found={}
 for name,inside,none in PAT.findall(raw):
  assert name in AXIOMS and name not in found,('unknown/duplicate theorem',name)
  assert bool(inside)!=bool(none)
  axioms=[] if none else [x.strip() for x in inside.split(',') if x.strip()]
  assert len(axioms)==len(set(axioms)) and set(axioms)<=GOOD
  found[name]=axioms
 assert list(found)==AXIOMS,('missing/wrong order axiom reports',list(found))
 return found

def selftest():
 baseline=''.join("info: file.lean:1:0: 'WeilDefect."+name+"' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]\n" for name in AXIOMS)
 assert len(parse(baseline))==len(AXIOMS)
 mutants=[
  baseline.replace('Quot.sound','sorryAx',1),
  baseline.replace('Quot.sound','custom_axiom',1),
  baseline.replace('propext','propext, propext',1),
  baseline+baseline,
  baseline.replace("'WeilDefect."+AXIOMS[0]+"'","'WeilDefect.unknown'",1),
  baseline.replace("'WeilDefect."+AXIOMS[0]+"'","'WeilDefect."+AXIOMS[1]+"'",1),
  baseline.replace(' depends on axioms:', ' error: depends on axioms:', 1),
 ]
 for mutant in mutants:
  try:parse(mutant)
  except AssertionError:pass
  else:raise AssertionError('fake Lean transcript accepted')
 print('CP-C1(H2) seven fail-closed axiom transcript controls PASS; NOT LEAN')
def verify():
 preflight()
 for p in [OBJ,H1OBJ,LOG,H1RECEIPT]:
  assert p.is_file() and p.stat().st_size>0,('missing genuine build artifact',str(p))
 upstream=json.loads(H1RECEIPT.read_text())
 assert upstream['status']=='GENUINE LEAN KERNEL + STANDARD AXIOMS PASS'
 assert upstream['compiled_olean_sha256']==sha(H1OBJ)
 assert upstream['source_sha256']==sha(H1)
 rec={
  'schema':'CP-C1H2-frozen-original-integral-Lean4.34-v1',
  'status':'GENUINE LEAN KERNEL + STANDARD AXIOMS PASS',
  'source_git_blobs':{str(p):pin for p,pin in PINS.items()},
  'source_sha256':sha(SOURCE),
  'compiled_olean_sha256':sha(OBJ),
  'h1_compiled_olean_sha256':sha(H1OBJ),
  'h1_strict_kernel_receipt_sha256':sha(H1RECEIPT),
  'genuine_standard_axioms':parse(LOG.read_text()),
  'physical_original_prime_phase':True,
  'quantitative_prime_interval_Lean':False,
  'full_pole_gamma_Weil_comparison':False,
  'external_spectral_target':False,'RH':False,
 }
 OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
 print('CP-C1(H2) 12 actual frozen source theorem results + 4 upstream strict axiom reports PASS')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('mode',choices=['preflight','selftest','verify'])
 {'preflight':preflight,'selftest':selftest,'verify':verify}[a.parse_args().mode]()
