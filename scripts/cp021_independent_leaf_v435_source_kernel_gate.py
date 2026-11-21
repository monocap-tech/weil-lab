#!/usr/bin/env python3
"""CP021 isolated upstream-original Zeta/Mathlib LEAF compiler custody.

Goal: make genuine old-Zeta v4.35 source acceptance possible without
compiling EVEN ONE new local CP013–CP020 draft. Two isolated leaf libs:
  CP021BorweinLeaf (10 theorem candidates);
  CP021GermLeaf (3 theorem candidates).

Tests:
 --self-test: exact Fraction/Bernoulli/13-factor numeric budget;
 --source-root, --mathlib-root: immutable original Git blobs, genuine
   signatures and zero new local imports, 13 theorem/axiom source names;
 --kernel-audit: requires 2 REAL .olean binaries and 13 REAL actual
   original Lean4.35 #print axioms receipts, standard-only.
No source-only result may be promoted as a new Lean kernel PASS.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"cp011_zeta_v435"
COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
LEAN_TOOLCHAIN="leanprover/lean4:v4.35.0"
ORIG_ZETA={
  "Zeta/EulerMaclaurin/Continuation.lean":"1bb01e946fa7e344497eaf7694fbecff0a714d09",
  "Zeta/EulerMaclaurin/ErrorBound.lean":"01184af0dbfd1369e14725e02e990b016bedfe6f",
}
ORIG_MATHLIB={
  "Mathlib/RingTheory/Polynomial/Pochhammer.lean":"f3503627af3430a48c087b85b03095e84dfb2824",
  "Mathlib/NumberTheory/Bernoulli.lean":"45d389886738789e80185fd2a6da4185727ab502",
  "Mathlib/Analysis/Calculus/IteratedDeriv/Lemmas.lean":"d9348833bece1297dd8ffe57e6b976fcc268af38",
  "Mathlib/Analysis/Complex/Norm.lean":"0e2b6317a777c4d168a9098fb17ad33323efd4c3",
  "Mathlib/Analysis/SpecialFunctions/Pow/Real.lean":"97c12aed7085a7fc77727567d87e508064b49a18",
}
NAMES={
"CP021BorweinLeaf":(
  "norm_ascPochhammer_eval_le_product",
  "original_bernoulli_fourteen",
  "source_B14_coefficient_norm",
  "majorant_product_nonneg",
  "source_circle_geometry",
  "original_Borwein_prefactor_le",
  "original_complex_cpow_bound",
  "original_Borwein_omitted_term_le",
  "exact_original_Borwein_real_envelope",
  "original_Borwein_all_circles",
),
"CP021GermLeaf":(
  "original_zeta_EM_germs_equal",
  "original_zeta_EM_derivative_error_identity",
  "original_center_valid",
)}
ORIGINAL_SIGNATURES={
  "Zeta/EulerMaclaurin/Continuation.lean":(
    "theorem riemannZeta_eq_approximant_add_remainder",
    "noncomputable abbrev zetaRemainder",
    "noncomputable abbrev zetaApproximant",
  ),
  "Zeta/EulerMaclaurin/ErrorBound.lean":(
    "noncomputable abbrev zetaRemainderBound",
    "theorem norm_zetaRemainder_le",
  ),
  "Mathlib/RingTheory/Polynomial/Pochhammer.lean":(
    "theorem ascPochhammer_succ_eval",),
  "Mathlib/NumberTheory/Bernoulli.lean":(
    "def bernoulli' (n : ℕ)", "def bernoulli (n : ℕ)"),
  "Mathlib/Analysis/Calculus/IteratedDeriv/Lemmas.lean":(
    "lemma Filter.EventuallyEq.iteratedDeriv_eq",),
  "Mathlib/Analysis/Complex/Norm.lean":(
    "theorem abs_re_le_norm",),
  "Mathlib/Analysis/SpecialFunctions/Pow/Real.lean":(
    "theorem norm_cpow_eq_rpow_re_of_pos",
    "theorem rpow_neg",
    "theorem rpow_le_rpow_of_exponent_le"),
}
ALLOWED={"propext","Classical.choice","Quot.sound"}
AXLOG=BASE/"cp021-real-original-leaf-axioms.log"
RESULT=BASE/"cp021-independent-original-leaf-actual-kernel.json"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def blob(p):
  h=hashlib.sha1(b"blob "+str(p.stat().st_size).encode()+b"\0")
  with p.open("rb") as f:
    for chunk in iter(lambda:f.read(1048576),b""):
      h.update(chunk)
  return h.hexdigest()

def b(n):
  plus=[Q(1)]
  for k in range(1,n+1):
    plus.append(Q(1)-sum(Q(comb(k,i),k-i+1)*plus[i] for i in range(k)))
  return (-1)**n*plus[n]

def exact_test():
  assert Q("149.5")==Q(299,2)
  assert Q("150.05353")-Q(299,2)==Q(55353,100000)
  assert Q(1,2)+Q("150.05353")+Q(1,4)<151
  assert Q(151+13, Q(13)+Q(1,4))==Q(656,53)
  assert b(1)==-Q(1,2) and b(12)==-Q(691,2730) and b(14)==Q(7,6)
  major=Q(656,53)*Q(7,6*factorial(14))*Q(prod(range(151,164)),256**13)
  assert major==Q(181596617021805363,633825300114114700748351602688)
  assert Q(2,10**13)<major<Q(3,10**13)
  for k in range(4):
    assert Q(factorial(k))*major*4**k < Q(factorial(k))*Q(3,10**13)*4**k
  assert factorial(3)*Q(3,10**13)*4**3==Q(1152,10**13)
  print("CP021 UPSTREAM-ONLY LEAF EXACT FRACTION/PIN-PROOF PREFLIGHT: PASS NOT LEAN")
  print("  Original 13-factor Borwein rational majorant:",major)
  print("  k=0,1,2,3 exact Cauchy scalar derivative budgets:",
        [str(Q(factorial(k))*Q(3,10**13)*4**k) for k in range(4)])
  print("  Deliberately false too-tight original cap 2e-13 rejected.")

def verify_leaf_sources():
  for mod,targets in NAMES.items():
    p=BASE/(mod+".lean")
    code=p.read_text("utf-8")
    imports=re.findall(r"(?m)^\s*(?:public )?import\s+([^\n]+)",code)
    if len(imports)==0 or any(not t.startswith(("Zeta.","Mathlib.")) for t in imports):
      raise ValueError(f"{mod}: dependency contamination, imported {imports!r}")
    if re.search(r"(?m)^\s*(sorry|axiom|opaque|constant)\b",code):
      raise ValueError(f"{mod}: new unproved axiom/constant/admission")
    declarations=re.findall(r"(?m)^theorem\s+([A-Za-z0-9_']+)\b",code)
    prints=re.findall(r"(?m)^#print axioms\s+("+re.escape(mod)+r"\.[A-Za-z0-9_']+)\b",code)
    expected=[mod+"."+t for t in targets]
    if declarations!=list(targets) or prints!=expected:
      raise ValueError(f"{mod}: malformed source theorem/#print axioms roster {declarations!r},{prints!r}")
  borwein=(BASE/"CP021BorweinLeaf.lean").read_text("utf-8")
  if "abs_of_nonneg ht.1" in borwein:
    raise ValueError("SOURCE-TYPE ERROR: abs_of_nonneg requires 0<=t, not a<=t")
  if not all(s in borwein for s in (
      "have ht_nonneg : (0 : ℝ) ≤ t := by",
      "have ha_nonneg : (0 : ℝ) ≤ a := by norm_num [a]",
      "exact ha_nonneg.trans ht.1",
      "abs_of_nonneg ht_nonneg",
      "simpa only [hdist] using this")):
    raise ValueError("CP022 concrete positive-ordinate geometry repair missing from upstream-only leaf")
  print("CP021 ORIGINAL-ZETA/ORIGINAL-MATHLIB-ONLY LEAF DEPENDENCY CUT: 2/2 SOURCE PASS NOT LEAN")
  print("  zero CP013–CP020 imports; 13 exact kernel-declaration target names.")

def verify_upstream(zeta,mathlib):
  for base,pins in ((zeta,ORIG_ZETA),(mathlib,ORIG_MATHLIB)):
    for name,expected in pins.items():
      path=base/name
      if blob(path)!=expected:
        raise ValueError(f"{name}: genuine original blob differs from frozen SHA")
      txt=path.read_text("utf-8")
      for needle in ORIGINAL_SIGNATURES[name]:
        if needle not in txt:
          raise ValueError(f"{name}: genuine original theorem signature {needle!r} absent")
  print("CP022 SEVEN FROZEN UPSTREAM ORIGINAL GIT BLOB+API GATES: 7/7 PASS NOT LEAN")

def genuine_kernel_audit():
  verify_leaf_sources()
  deps={name:BASE/".lake/build/lib/lean"/(name+".olean") for name in NAMES}
  required=[BASE/(name+".lean") for name in NAMES]+list(deps.values())+[AXLOG,BASE/"lean-toolchain"]
  missing=[str(p) for p in required if not p.is_file()]
  if missing:
    raise ValueError("NOT_READY: real source .olean/standard-axiom output missing: "+repr(missing))
  if (BASE/"lean-toolchain").read_text("utf-8").strip()!=LEAN_TOOLCHAIN:
    raise ValueError("NOT_READY: external original Zeta v4.35 toolchain mismatch")
  log=AXLOG.read_text("utf-8")
  if "sorryAx" in log or "unsolved goals" in log or "error:" in log:
    raise ValueError("NOT_READY: actual Lean compiler error/admission")
  verified={}
  for mod,targets in NAMES.items():
    for t in targets:
      full=mod+"."+t
      regex=re.compile(re.escape("'"+full+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
      found=regex.findall(log)
      if len(found)!=1:
        raise ValueError("NOT_READY: missing/ambiguous actual source #print axioms "+full)
      axioms={a.strip() for a in found[0].split(",") if a.strip()}
      if not axioms<=ALLOWED:
        raise ValueError("NOT_READY: nonstandard axiom in "+full+": "+repr(axioms-ALLOWED))
      verified[full]=sorted(axioms)
  out={
    "status":"CP021_GENUINE_UPSTREAM_ONLY_ORIGINAL_ZETA435_LEAF_KERNEL_PASS",
    "scope":"Only independent true Borwein complex-circle bound (10 theorems) and original ζ=EM+R derivative germ equality (3 theorems); source numerical and analytic Hardy-Z enclosures separately OPEN.",
    "original_Zeta_commit":COMMIT,"original_toolchain":LEAN_TOOLCHAIN,
    "leaf_new_actual_source_sha256":{n:sha(BASE/(n+".lean")) for n in NAMES},
    "leaf_new_actual_compiled_olean_sha256":{n:sha(p) for n,p in deps.items()},
    "actual_standard_axioms":verified,"actual_axiom_log_sha256":sha(AXLOG),
    "inherited_CP013_CP020_local_olean_dependencies":0,
    "complete_analytic_Cauchy_holomorphy_new_olean_accepted":False,
    "actual_original_HardyZ_derivative_anchor_proved":False,
    "actual_original_HardyZ_uniform_curvature_proved":False,
    "actual_original_narrow_root53_sign_accepted":False,
    "original_signed_Weil_spectral_dictionary":False,
    "global_Weil_positivity_or_RH":False,
  }
  RESULT.write_text(json.dumps(out,indent=2)+"\n","utf-8")
  print(out["status"])

def main():
  ap=argparse.ArgumentParser()
  ap.add_argument("--self-test",action="store_true")
  ap.add_argument("--source-check",action="store_true")
  ap.add_argument("--original-zeta",type=Path)
  ap.add_argument("--original-mathlib",type=Path)
  ap.add_argument("--kernel-audit",action="store_true")
  args=ap.parse_args()
  if args.self_test: exact_test()
  if args.source_check: verify_leaf_sources()
  if bool(args.original_zeta)!=bool(args.original_mathlib):
    ap.error("must provide BOTH frozen original source roots")
  if args.original_zeta: verify_upstream(args.original_zeta,args.original_mathlib)
  if args.kernel_audit: genuine_kernel_audit()
  if not (args.self_test or args.source_check or args.original_zeta or args.kernel_audit):
    ap.print_help()

if __name__=="__main__":
  try:main()
  except (OSError,ValueError,UnicodeError) as e:
    raise SystemExit("CP021 NOT_READY/FAIL: "+str(e))
