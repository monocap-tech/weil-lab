#!/usr/bin/env python3
"""CP-C1(E) true frozen flat source/Lean receipt; preflight != LEAN."""
import argparse, hashlib, json, re
from pathlib import Path
from cpc1e_frozen_cp001_prime_geometry import main as replay
P=Path("WeilDefect/Arithmetic")
SRC=P/"CP_C1E_FrozenFlatSchwartz.lean"
OBJ=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1E_FrozenFlatSchwartz.olean")
LOG=Path("cpc1e-original-kernel-axioms.log")
GEO=Path("cpc1e-frozen-cp001-prime-geometry.json")
PAR=Path("cpc1c-cpc1d-original-kernel-receipt.json")
OUT=Path("cpc1e-original-kernel-receipt.json")
B=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1B_OriginalNineProbeSource.olean")
C=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1C_OriginalCompleteDivisorFinite3.olean")
D=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1D_OriginalNineProbeCompatibility.olean")
PINS={
 P/"ActualZetaPhaseIVOriginalMixedHermitian.lean":"0a7b6cc16670160c6f4b338a36c6d51ae730dde7",
 P/"ActualZetaPhaseIVOriginalSchwartzPolarization.lean":"fa794132d438d095436879c4f78d9340ea29be02",
 P/"CP_C1C_OriginalCompleteDivisorFinite3.lean":"a8f0b093f7a6dee3123118359c776b32a8e5ec1d",
 P/"CP_C1D_OriginalNineProbeCompatibility.lean":"3e6feabb5fc139f79f208d0c87e6db1d3e008ad2",
}
NEW=[
"neutralCPC1EFlatProfile_eq_frozen",
"neutralCPC1EFlatProfile_contDiff",
"neutralCPC1EFlatProfile_zero",
"neutralCPC1EFlatProfile_zero_outside",
"neutralCPC1EFlatReal_center",
"neutralCPC1EFlatReal_zero_outside",
"neutralCPC1EFlatReal_contDiff",
"neutralCPC1EFlatComplex_contDiff",
"neutralCPC1EFlatComplex_hasCompactSupport",
"neutralCPC1EFlatSchwartz_apply",
"neutralCPC1EFlatSchwartz_center",
"neutralCPC1EFlatSchwartz_zero_outside",
"neutralCPC1EFrozenFamily_supportedOriginal",
"neutralCPC1EFrozenOriginal_matrix_eq_completeDivisor",
]
NAMES=[
"neutralCPC1C_originalFiniteThree_matrix_eq_divisor",
"neutralCPC1D_original_eq_target_of_nine_phase_readings",
]+NEW
AX=re.compile(r"'WeilDefect\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|(does not depend on any axioms))",re.S)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p):
 b=p.read_bytes()
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def preflight():
 s=SRC.read_text()
 assert re.findall(r"(?m)^theorem (neutralCPC1E\w+)\b",s)==NEW
 assert re.findall(r"(?m)^#print axioms (\w+)\s*$",s)==NAMES
 for token in [
 "import WeilDefect.Arithmetic.CP_C1D_OriginalNineProbeCompatibility",
 "expNegInvGlue (1 - u ^ 2)",
 "expNegInvGlue.contDiff",
 "neutralCPC1EFlatComplex_hasCompactSupport",
 "toSchwartzMap",
 "neutralCPC1C_originalFiniteThree_matrix_eq_divisor",
 "(-1099 / 1000) (1 / 2000)",
 "(1099 / 1000) (1 / 2000)",
 "(1 / 5) r hr",
 ]: assert token in s,token
 assert s.rstrip().endswith("end\nend WeilDefect")
 assert not re.search(r"(?m)^\s*(axiom|opaque|constant|unsafe)\b",s)
 assert not re.search(r"\b(sorry|admit|native_decide|sorryAx)\b",s)
 for p,x in PINS.items():assert blob(p)==x,(str(p),blob(p),x)
 assert Path("lean-toolchain").read_text().strip()=="leanprover/lean4:v4.34.0"
 g=replay()
 assert g["old_radius"]=="1/2000"
 assert g["lower_bounds"]["I9"]=="3/6050000"
 assert g["lower_bounds"]["mass_normalized_prime_offdiagonal"]=="1/6050"
 print("CP-C1(E): 14 exact-profile Lean candidates; 16 axiom requests, true frozen rational n9 source PASS; NOT LEAN")
def parse(s):
 assert not re.search(r"error:|##\[error\]|sorryAx|unsolved goals",s,re.I)
 rows=AX.findall(s)
 assert len(rows)==len(NAMES),(len(rows),len(NAMES))
 found={}
 for n,raw,none in rows:
  assert n in NAMES and n not in found,n
  assert bool(raw)!=bool(none),n
  vals=[] if none else [x.strip() for x in raw.split(",") if x.strip()]
  assert len(vals)==len(set(vals)) and set(vals)<={"propext","Classical.choice","Quot.sound"},(n,vals)
  found[n]=vals
 assert set(found)==set(NAMES)
 return found
def selftest():
 lines=["'WeilDefect."+n+"' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]\n" for n in NAMES]
 base="".join(lines)
 assert len(parse(base))==16
 for wrong in [base.replace("Quot.sound","sorryAx",1),base.replace("Quot.sound","rogue",1),
               base.replace("propext","propext, propext",1),base+lines[0],
               base.replace("'WeilDefect."+NAMES[0]+"'","'WeilDefect.unknown'",1),
               base.replace("'WeilDefect."+NAMES[0]+"'","'WeilDefect."+NAMES[1]+"'",1),
               base.replace(" depends on axioms:"," error: depends on axioms:",1)]:
  try:parse(wrong)
  except AssertionError:pass
  else:raise AssertionError("fake axiom transcript accepted")
 print("CP-C1(E): 16 multiline axiom prints, seven negative parser controls PASS; NOT LEAN")
def verify():
 preflight()
 for p in [OBJ,LOG,GEO,PAR,B,C,D]:
  assert p.is_file() and p.stat().st_size>0,str(p)
 parent=json.loads(PAR.read_text())
 assert parent["status"]=="GENUINE DIRECT KERNEL AND STANDARD AXIOM PASS"
 assert parent["b_compiled_olean_sha256"]==sha(B)
 for tag,obj in [("C",C),("D",D)]:
  assert parent["olean_sha256"][tag]==sha(obj)
 assert json.loads(GEO.read_text())==replay()
 rec={"schema":"CP-C1E-exact-flat-CP001-Lean4.34-v1",
      "status":"GENUINE LEAN KERNEL + STANDARD AXIOMS PASS",
      "source_sha256":{str(p):sha(p) for p in [SRC,*PINS,Path("lean-toolchain"),Path("lakefile.toml")]},
      "original_source_git_blobs":{str(p):x for p,x in PINS.items()},
      "compiled_olean_sha256":sha(OBJ),"bcd_receipt_sha256":sha(PAR),
      "rational_geometry_sha256":sha(GEO),"axioms":parse(LOG.read_text()),
      "prime_integral_lower_bound_formalized_in_Lean":False,
      "independent_spectral_nine_probes_proved":False,
      "global_Weil_positivity":False,"RH":False}
 OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+"\n")
 print("CP-C1(E) 14 original flat Schwartz Lean theorems + 2 upstream strict axiom checks: REAL PASS")
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("mode",choices=["preflight","selftest","verify"])
 {"preflight":preflight,"selftest":selftest,"verify":verify}[p.parse_args().mode]()
