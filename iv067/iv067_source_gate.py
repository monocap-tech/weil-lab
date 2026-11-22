#!/usr/bin/env python3
"""IV067 reproducible, fail-closed IV066 compiler-receipt acceptance gate.

No Lean success is inferred from static files. The runner must compile in the pinned
repository, remove the old target .olean, collect the actual compiler and axiom
outputs, then call this gate. This utility does not create a PASS receipt on a
missing/failed compiler or on untracked/uncommitted sources.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

TOOLCHAIN = 'leanprover/lean4:v4.34.0'
PARENT = '614ba879f7389fdb620c474adaee273b00eac71c'
LEAN = 'WeilDefect/Arithmetic/IV066OriginalSourcePilot.lean'
AUDIT = 'verification/IV066AxiomAudit.lean'
IV066_GATE = 'iv066/IV066_source_gate.py'
SELF = 'iv067/iv067_source_gate.py'
TARGET = '.lake/build/lib/lean/WeilDefect/Arithmetic/IV066OriginalSourcePilot.olean'
THEOREMS = (
 'iv066_sourceCorrelation_orientation',
 'iv066_original_general_source_summable',
 'iv066_original_general_source_signed',
 'iv066_original_mixed_weilTest_signed',
 'iv066_gamma_literal_native',
 'iv066_native_signed_multiplier',
)
ALLOWED = {'propext', 'Quot.sound', 'Classical.choice'}
# IV069 compiler-guided Real.pi cast correction: source re-pinned; axiom inventory unchanged.
PINNED_IV066 = {
 LEAN: 'be287351931c08bef941199b47240dcb307027abebe3222f55fc49d4f05000b7',
 AUDIT: '424bb2a4b1cc3d86813e33863f8ae4e5bb6c3e0d636190b0507a11ed12c922f8',
 IV066_GATE: '84f705735537fc8ad9c5a2de37dcd418fcfc1659eeffd301e1acb512679ceae4',
}
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


def digest(path: Path) -> str:
 return hashlib.sha256(path.read_bytes()).hexdigest()


def git(root: Path, *args: str, check: bool = True):
 return subprocess.run(['git', *args], cwd=root, check=check,
                       text=True, capture_output=True)


def source_audit(root: Path, require_commit: bool = False):
 assert (root/'lean-toolchain').read_text().strip() == TOOLCHAIN, 'toolchain drift'
 assert 'v4.34.0' in (root/'lakefile.toml').read_text(), 'Mathlib drift'
 head = git(root, 'rev-parse', 'HEAD').stdout.strip()
 assert git(root, 'merge-base', '--is-ancestor', PARENT, head,
            check=False).returncode == 0, 'parent not ancestor'
 for name, expected in SOURCE_BLOBS.items():
  actual = git(root, 'hash-object', name).stdout.strip()
  assert actual == expected, f'original source drift: {name}: {actual}'
 for name, expected in PINNED_IV066.items():
  assert digest(root/name) == expected, f'IV066 pilot/audit changed: {name}'
 if require_commit:
  paths = [*PINNED_IV066, SELF, 'iv067/iv067_compile_one_lane.sh']
  for name in paths:
   git(root, 'ls-files', '--error-unmatch', '--', name)
   # HEAD must actually contain the exact content being compiled, not untracked overlay.
   blob = git(root, 'rev-parse', 'HEAD:'+name).stdout.strip()
   working = git(root, 'hash-object', name).stdout.strip()
   assert blob == working, f'committed/working-tree mismatch: {name}'
  assert not git(root, 'status', '--porcelain', '--', *paths).stdout.strip(), 'uncommitted source or audit files'
 return {'commit':head, 'toolchain':TOOLCHAIN,
         'pinned_original_blobs':SOURCE_BLOBS,
         'pinned_IV066_sha256':PINNED_IV066}


def local_audit(root: Path):
 for name, expected in PINNED_IV066.items():
  assert (root/name).is_file() and digest(root/name) == expected, f'broken IV066 pin {name}'
 lean=(root/LEAN).read_text()
 audit=(root/AUDIT).read_text()
 for th in THEOREMS:
  assert re.search(r'^theorem\s+'+re.escape(th)+r'\b', lean, flags=re.M), f'theorem missing: {th}'
  assert audit.count('#print axioms WeilDefect.'+th+'\n') == 1, f'axiom query missing/duplicate: {th}'
 code=re.sub(r'/\-.*?\-/', '', lean, flags=re.S)  # strip doc/block comments
 code='\n'.join(ln.split('--')[0] for ln in code.splitlines())  # line comments
 assert not re.search(r'\b(sorry|admit|axiom)\b',code,flags=re.I), 'possible proof escape'
 assert (root/SELF).is_file(), 'source gate missing'
 return {'pilot_sha256':digest(root/LEAN),'axiom_source_sha256':digest(root/AUDIT),
         'gate_sha256':digest(root/SELF), 'status':'STATIC PASS; NOT LEAN PASS'}


def parse_axioms(log: str) -> dict:
 """Require exactly one genuine-looking Lean #print axioms response per theorem.

 This parses compiler output, but by itself is not proof that a compiler ran.
 The runner must supply the independently captured file and fresh binary stamp.
 """
 found = {}
 for th in THEOREMS:
  full='WeilDefect.'+th
  entries=[]
  # Lean's two permitted output forms.
  pat=re.compile(r"^'"+re.escape(full)+r"' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)\s*$", re.M)
  for match in pat.finditer(log):
   axioms=({a.strip() for a in match.group(1).split(',') if a.strip()}
           if match.group(1) is not None else set())
   entries.append(axioms)
  assert len(entries)==1, f'missing/duplicate axiom result for {full}: {len(entries)}'
  assert entries[0] <= ALLOWED, f'nonstandard axioms for {full}: {sorted(entries[0]-ALLOWED)}'
  found[th]=sorted(entries[0])
 return found


def receipts(root: Path, axiom_log: Path, build_log: Path, start_stamp: Path):
 source=source_audit(root, require_commit=True)
 local=local_audit(root)
 olean=root/TARGET
 assert olean.is_file() and olean.stat().st_size > 0, 'missing/nonempty olean'
 assert start_stamp.is_file(), 'missing build-start stamp'
 # Stamp is generated before removing stale olean, then before rebuilding it.
 start_ns=int(start_stamp.read_text().strip())
 assert start_ns > 0 and olean.stat().st_mtime_ns >= start_ns, 'stale olean compared with fresh build-start stamp'
 assert build_log.is_file() and build_log.stat().st_size>0, 'empty build log'
 assert axiom_log.is_file() and axiom_log.stat().st_size>0, 'empty axiom log'
 build=build_log.read_text()
 axioms=axiom_log.read_text()
 assert not re.search(r'(?m)^\s*(?:error:|.*: error:)',build), 'Lean build reported error'
 assert not re.search(r'(?m)^\s*(?:error:|.*: error:)',axioms), 'axiom run reported error'
 found=parse_axioms(axioms)
 return {'stage':'IV067','standing':'LEAN COMPILE + STRICT AXIOM AUDIT PASS',
         'source_custody':source,'static_check':local,
         'olean_sha256':digest(olean), 'olean_bytes':olean.stat().st_size,
         'olean_timestamp_ns':olean.stat().st_mtime_ns,
         'start_stamp_ns':start_ns,
         'build_log_sha256':digest(build_log),'axiom_log_sha256':digest(axiom_log),
         'axioms':found}


def main():
 p=argparse.ArgumentParser()
 p.add_argument('--mode',choices=['local','source','receipts'],required=True)
 p.add_argument('--root',type=Path,default=Path('.'))
 p.add_argument('--axiom-log',type=Path)
 p.add_argument('--build-log',type=Path)
 p.add_argument('--start-stamp',type=Path)
 p.add_argument('--output',type=Path)
 a=p.parse_args()
 root=a.root.resolve()
 if a.mode=='local': result=local_audit(root)
 elif a.mode=='source': result=source_audit(root,require_commit=True)
 else:
  assert a.axiom_log is not None and a.build_log is not None and a.start_stamp is not None, 'receipt logs and stamp required'
  result=receipts(root,a.axiom_log,a.build_log,a.start_stamp)
 if a.output:
  a.output.parent.mkdir(parents=True,exist_ok=True)
  a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('IV067',a.mode.upper(),result.get('standing',result.get('status','SOURCE PASS')))
 print('This is a genuine Lean claim ONLY in receipts mode after successful runner invocation.')

if __name__=='__main__':
 try: main()
 except (AssertionError,FileNotFoundError,subprocess.CalledProcessError,ValueError) as err:
  print('IV067 GATE FAIL:',str(err),file=sys.stderr)
  sys.exit(1)
