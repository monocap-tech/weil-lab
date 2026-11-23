#!/usr/bin/env python3
"""Fail-closed H1 source/axiom receipt. No preflight is a Lean pass."""
import hashlib, json, re, sys
from pathlib import Path
S=Path("WeilDefect/Arithmetic/CP_C1H_OriginalPointwisePrimeCorrelation.lean")
L=Path("cpc1h1-original-kernel-axioms.log")
O=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1H_OriginalPointwisePrimeCorrelation.olean")
OUT=Path("cpc1h1-original-kernel-receipt.json")
PINS={
 "WeilDefect/Arithmetic/CP_C1E_FrozenFlatSchwartz.lean":"29e68fe77e18d6e7b6b2c46bac6084beb4f18307",
 "WeilDefect/Arithmetic/CP_C1FG_FrozenTargetAndRadiusGlue.lean":"befea449e7e166a31d6ee108e732666ebec76487",
 "WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean":"5ed0be00fdfefe2f0b21223858c36e3870cda5f7",
 "WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeGeometry.lean":"5dbaf772eaf7e0b5a94c2ebed9cdb5629809be1c",
}
NAMES=["neutralNF600Log9_cross","neutralCPC1H_positiveShift_pointwise","neutralCPC1H_negativeShift_pointwise"]
NEWT=NAMES[1:]
PAT=re.compile(r"'WeilDefect\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|(does not depend on any axioms))",re.S)
GOOD={"propext","Classical.choice","Quot.sound"}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p):
 b=p.read_bytes()
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def preflight():
 s=S.read_text()
 assert s.startswith("import WeilDefect.Arithmetic.CP_C1FG_FrozenTargetAndRadiusGlue\n")
 assert re.findall(r"(?m)^theorem (neutralCPC1H_\w+)",s)==NEWT
 assert re.findall(r"(?m)^#print axioms (\w+)",s)==NAMES
 assert s.rstrip().endswith("end\nend WeilDefect")
 assert not re.search(r"\b(sorryAx|sorry|admit|native_decide)\b",s)
 assert not re.search(r"(?m)^\s*(axiom|opaque|constant|unsafe)\b",s)
 assert "conj v * (L x * conj (R (x + Real.log 9)))" in s
 assert "neutralNF600Log9_cross" in s
 assert Path("lean-toolchain").read_text().strip()=="leanprover/lean4:v4.34.0"
 for fname,pin in PINS.items(): assert blob(Path(fname))==pin,(fname,pin)
 print("CP-C1(H1) source+4 upstream original blob pins PASS; NOT LEAN")
def parse(raw):
 assert not re.search(r"error:|sorryAx|unsolved goals|##\[error\]",raw,re.I)
 found={}
 for name,inside,none in PAT.findall(raw):
  assert name in NAMES and name not in found
  assert bool(inside)!=bool(none)
  axioms=[] if none else [q.strip() for q in inside.split(",") if q.strip()]
  assert len(axioms)==len(set(axioms)) and set(axioms)<=GOOD
  found[name]=axioms
 assert list(found)==NAMES,(list(found),NAMES)
 return found
def selftest():
 base="".join("'WeilDefect."+n+"' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]\n" for n in NAMES)
 parse(base)
 for bad in [base.replace("Quot.sound","sorryAx",1),base.replace("Quot.sound","untrusted.axiom",1),base+base,base.replace(NAMES[1],"missing",1),base.replace("propext","propext, propext",1)]:
  try:parse(bad)
  except AssertionError:pass
  else:raise AssertionError("false receipt passed")
 print("CP-C1(H1) 5 strict negative controls PASS NOT LEAN")
def verify():
 preflight()
 assert O.is_file() and O.stat().st_size>0
 assert L.is_file() and L.stat().st_size>0
 ax=parse(L.read_text())
 rec={"schema":"CP-C1H1-original-NF600-pointwise-Lean4.34-v1","status":"GENUINE LEAN KERNEL + STANDARD AXIOMS PASS","source_git_blobs":PINS,"source_sha256":digest(S),"compiled_olean_sha256":digest(O),"genuine_standard_axioms":ax,"frozen_CP001_integrals_compiled":False,"full_Weil_positive":False,"RH":False}
 OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+"\n")
 print("CP-C1(H1) both pointwise source theorems genuine Lean and standard-only axiom receipts PASS")
if __name__=="__main__":
 {"preflight":preflight,"selftest":selftest,"verify":verify}[sys.argv[1]]()
