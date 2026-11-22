#!/usr/bin/env python3
"""CP-C1(F/G) original frozen-source kernel custody; source preflight != Lean."""
import argparse, hashlib, json, re
from pathlib import Path

ROOT=Path("WeilDefect/Arithmetic")
SRC=ROOT/"CP_C1FG_FrozenTargetAndRadiusGlue.lean"
E=ROOT/"CP_C1E_FrozenFlatSchwartz.lean"
D=ROOT/"CP_C1D_OriginalNineProbeCompatibility.lean"
OBJ=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1FG_FrozenTargetAndRadiusGlue.olean")
EOBJ=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1E_FrozenFlatSchwartz.olean")
ERECEIPT=Path("cpc1e-original-kernel-receipt.json")
LOG=Path("cpc1fg-original-kernel-axioms.log")
OUT=Path("cpc1fg-original-kernel-receipt.json")
BLOBS={
 E:"29e68fe77e18d6e7b6b2c46bac6084beb4f18307",
 D:"3e6feabb5fc139f79f208d0c87e6db1d3e008ad2",
}
NEW=[
 "neutralCPC1F_frozenDivisor_eq_target_of_nine_readings",
 "neutralCPC1G_frozenOldPair_same",
 "neutralCPC1G_frozenFourOldReadings_same",
 "neutralCPC1G_frozenOriginalOldBlock_same",
 "neutralCPC1G_frozenDivisorOldBlock_same",
]
ORIGINAL=[
 "neutralCPC1EFrozenOriginal_matrix_eq_completeDivisor",
 "neutralCPC1D_original_eq_target_of_nine_phase_readings",
]
ALL=ORIGINAL+NEW
PAT=re.compile(r"'WeilDefect\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|(does not depend on any axioms))",re.S)
GOOD={"propext","Classical.choice","Quot.sound"}
def blob(p):
 b=p.read_bytes()
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def preflight():
 s=SRC.read_text()
 assert re.findall(r"(?m)^theorem (neutralCPC1[FG]_\w+)\b",s)==NEW
 assert re.findall(r"(?m)^#print axioms (\w+)\s*$",s)==ALL
 assert s.startswith("import WeilDefect.Arithmetic.CP_C1E_FrozenFlatSchwartz\n")
 assert s.rstrip().endswith("end\nend WeilDefect")
 for marker in [
  "neutralCPC1EFrozenOriginal_matrix_eq_completeDivisor",
  "neutralCPC1D_original_eq_target_of_nine_phase_readings",
  "neutralCPC1EFrozenFamily_supportedOriginal",
  "neutralIV007OriginalMixedEntry",
  "neutralIV007OriginalDivisorEntry",
  "Complex.I • neutralCPC1EFrozenFamily",
  "hHerm hDiag hPlus hPhase",
 ]: assert marker in s,marker
 assert not re.search(r"(?m)^\s*(?:axiom|constant|opaque|unsafe)\b",s)
 assert not re.search(r"\b(?:sorry|admit|sorryAx|native_decide)\b",s)
 for p,pin in BLOBS.items():assert blob(p)==pin,("upstream drift",str(p),blob(p),pin)
 assert Path("lean-toolchain").read_text().strip()=="leanprover/lean4:v4.34.0"
 assert Path("lakefile.toml").is_file()
 print("CP-C1(F/G) 5 frozen-source new declarations; 7 source/axiom prints; D/E frozen blobs PASS NOT LEAN")
def parse(raw):
 assert not re.search(r"error:|##\[error\]|sorryAx|unsolved goals",raw,re.I)
 rows=PAT.findall(raw)
 assert len(rows)==len(ALL),("wrong report count",len(rows),len(ALL))
 found={}
 for name,inside,none in rows:
  assert name in ALL and name not in found,("unknown/duplicate declaration",name)
  assert bool(inside)!=bool(none),("malformed axiom result",name)
  axioms=[] if none else [a.strip() for a in inside.split(",") if a.strip()]
  assert len(axioms)==len(set(axioms))
  assert set(axioms)<=GOOD,("nonstandard axiom",name,axioms)
  found[name]=axioms
 assert set(found)==set(ALL),("missing reports",set(ALL)-set(found))
 return found
def selftest():
 lines=["info: proof.lean:1:0: 'WeilDefect."+n+
        "' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]\n"
        for n in ALL]
 raw="".join(lines)
 assert len(parse(raw))==7
 bad=[
  raw.replace("Quot.sound","sorryAx",1),
  raw.replace("Quot.sound","my.axiom",1),
  raw.replace("propext","propext, propext",1),
  raw+lines[0],
  raw.replace("'WeilDefect."+ALL[0]+"'","'WeilDefect.unknown'",1),
  raw.replace("'WeilDefect."+ALL[0]+"'","'WeilDefect."+ALL[1]+"'",1),
  raw.replace(" depends on axioms:"," error: depends on axioms:",1),
 ]
 for fake in bad:
  try: parse(fake)
  except AssertionError: pass
  else: raise AssertionError("failed a negative control")
 print("CP-C1(F/G) strict multiline seven-report parser + seven negative controls PASS NOT LEAN")
def verify():
 preflight()
 for p in [OBJ,EOBJ,ERECEIPT,LOG]:
  assert p.is_file() and p.stat().st_size>0,("missing real build evidence",str(p))
 parent=json.loads(ERECEIPT.read_text())
 assert parent.get("status")=="GENUINE LEAN KERNEL + STANDARD AXIOMS PASS"
 assert parent.get("compiled_olean_sha256")==sha(EOBJ)
 assert parent["source_sha256"][str(E)]==sha(E)
 rec={
  "schema":"CP-C1FG-frozen-original-target-and-old-block-Lean4.34-v1",
  "status":"GENUINE KERNEL AND STANDARD AXIOMS PASS",
  "original_source_git_blobs":{str(p):pin for p,pin in BLOBS.items()},
  "source_sha256":{str(p):sha(p) for p in [SRC,E,D,Path("lean-toolchain"),Path("lakefile.toml")]},
  "compiled_olean_sha256":sha(OBJ),
  "cp_c1e_compiled_olean_sha256":sha(EOBJ),
  "cp_c1e_strict_receipt_sha256":sha(ERECEIPT),
  "genuine_standard_axioms":parse(LOG.read_text()),
  "independent_target_nine_readings_certified":False,
  "independent_two_radius_target_coherence_certified":False,
  "analytic_nine_reading_interval_budget_formalized":False,
  "global_Weil_positivity":False,"RH":False,
 }
 OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+"\n")
 print("CP-C1(F/G) 5/5 new genuine original frozen-source Lean theorems + 2 original strict axiom reports PASS")
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("mode",choices=["preflight","selftest","verify"])
 {"preflight":preflight,"selftest":selftest,"verify":verify}[p.parse_args().mode]()
