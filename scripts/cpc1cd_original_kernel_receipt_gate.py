#!/usr/bin/env python3
"""CP-C1(C/D) original Weil direct kernel/axiom receipt. Preflight != LEAN."""
import argparse, hashlib, json, re
from pathlib import Path
import cpc1c_original_finite3_source_preflight as c1c
import cpc1d_original_nine_scalar_preflight as c1d

ROOT=Path("WeilDefect/Arithmetic")
SPECS={
 "C":("CP_C1C_OriginalCompleteDivisorFinite3",
   ["neutralIV008OriginalMixedEntry_eq_divisor",
    "neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal",
    "neutralCPC1C_originalFiniteThree_matrix_eq_divisor",
    "neutralCPC1C_originalFiniteThree_diagonal_eq_divisorEnergy",
    "neutralCPC1C_originalFiniteThree_divisorHermitian"]),
 "D":("CP_C1D_OriginalNineProbeCompatibility",
   ["neutralIV008OriginalMixedEntry_eq_divisor",
    "neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal",
    "neutralCPC1D_original_re_from_physicalProbes",
    "neutralCPC1D_original_im_from_physicalProbes",
    "neutralCPC1D_divisor_re_from_physicalProbes",
    "neutralCPC1D_divisor_im_from_physicalProbes",
    "neutralCPC1D_original_eq_target_of_nine_phase_readings"]),
}
IVS={
 ROOT/"ActualZetaPhaseIVOriginalMixedHermitian.lean":"0a7b6cc16670160c6f4b338a36c6d51ae730dde7",
 ROOT/"ActualZetaPhaseIVOriginalSchwartzPolarization.lean":"fa794132d438d095436879c4f78d9340ea29be02",
}
B=ROOT/"CP_C1B_OriginalNineProbeSource.lean"
BO=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1B_OriginalNineProbeSource.olean")
BR=Path("cpc1b-original-kernel-receipt.json")
ALLOWED={"propext","Classical.choice","Quot.sound"}
PAT=re.compile(r"'WeilDefect\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|(does not depend on any axioms))",re.S)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def git_blob(p):
 b=p.read_bytes()
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def preflight():
 c1c.main(); c1d.main()
 assert Path("lean-toolchain").read_text().strip()=="leanprover/lean4:v4.34.0"
 for p,x in IVS.items(): assert git_blob(p)==x,(str(p),x)
 print("CP-C1(C/D) original-source pinned preflight PASS; NOT LEAN.")
def parse(log,names):
 assert not re.search(r"error:|##\[error\]|sorryAx|unsolved goals",log,re.I)
 matches=PAT.findall(log)
 assert len(matches)==len(names),("wrong axiom print count",len(matches),len(names))
 out={}
 for name,raw,none in matches:
  assert name in names and name not in out,("extra/duplicate",name)
  assert bool(raw)!=bool(none),("bad print",name)
  ax=[] if none else [x.strip() for x in raw.split(",") if x.strip()]
  assert len(ax)==len(set(ax)),("duplicate axiom",name)
  assert set(ax)<=ALLOWED,("forbidden axiom",name,ax)
  out[name]=ax
 assert set(out)==set(names),("missing axiom report",set(names)-set(out))
 return out
def selftest():
 for tag,(mod,names) in SPECS.items():
  lines=["info: x:1:0: 'WeilDefect."+n+"' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]\n" for n in names]
  good="".join(lines)
  assert len(parse(good,names))==len(names)
  for bad in [good.replace("Quot.sound","sorryAx",1),
              good.replace("Quot.sound","rogue",1),
              good.replace("propext","propext, propext",1),
              good+lines[0],
              good.replace("'WeilDefect."+names[0]+"'","'WeilDefect.unknown'",1),
              good.replace("'WeilDefect."+names[0]+"'","'WeilDefect."+names[1]+"'",1),
              good.replace(" depends on axioms:"," error: depends on axioms:",1)]:
   try: parse(bad,names)
   except AssertionError: pass
   else: raise AssertionError((tag,"negative control failed"))
 print("CP-C1(C/D) parser 14 negative controls PASS; NOT LEAN.")
def verify():
 preflight()
 assert BO.is_file() and BO.stat().st_size>0
 assert BR.is_file()
 b=json.loads(BR.read_text())
 assert b.get("status")=="GENUINE KERNEL + AXIOM PASS"
 assert b["compiled_olean_sha256"]==sha(BO)
 assert b["source_sha256"][str(B)]==sha(B)
 out={
  "schema":"CP-C1CD-original-source-Lean4.34-v1",
  "status":"GENUINE DIRECT KERNEL AND STANDARD AXIOM PASS",
  "b_receipt_sha256":sha(BR),"b_compiled_olean_sha256":sha(BO),
  "original_source_git_blobs":{str(p):x for p,x in IVS.items()},
  "source_sha256":{str(p):sha(p) for p in [B,*IVS,
    *[ROOT/(m+".lean") for m,_ in SPECS.values()],
    Path("lean-toolchain"),Path("lakefile.toml")]},
  "olean_sha256":{},"axioms":{},
  "frozen_flat_cp001_bumps_proved":False,
  "independent_target_matches_nine_readings":False,
  "complete_external_zero_roster_proved":False,
  "global_Weil_positivity_proved":False,"RH_proved":False}
 for tag,(mod,names) in SPECS.items():
  obj=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")/(mod+".olean")
  log=Path("cpc1"+tag.lower()+"-original-kernel-axioms.log")
  assert obj.is_file() and obj.stat().st_size>0
  assert log.is_file() and log.stat().st_size>0
  out["olean_sha256"][tag]=sha(obj)
  out["axioms"][tag]=parse(log.read_text(),names)
 Path("cpc1c-cpc1d-original-kernel-receipt.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print("CP-C1(C/D) 3+5 new Lean theorems, 12 actual standard-only axiom prints PASS.")
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("mode",choices=["preflight","selftest","verify"])
 {"preflight":preflight,"selftest":selftest,"verify":verify}[p.parse_args().mode]()
