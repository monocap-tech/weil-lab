#!/usr/bin/env python3
"""CP027 true-original two-critical-line-center Borwein proof custody.

Original Zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3
Lean4.35 + Mathlib v4.35, not substitute zeta or source hypotheses.

The source formula, with M=6,N=256, z=1/2+i*t:
  zetaRemainderBound(z,6,256)
    = ‖z+13‖/(z.re+13) *
      ‖(bernoulli 14/14!) * (ascPochhammer 13)(z)*256^(-z-13)‖.

For the two exact original heights t=150.05352 and 150.05353:
  Re z = 1/2, |z|<=1/2+t<151, |z+13|<=164,
  (Re z+13)=27/2, K<=328/27.
  |B14|=7/6, |(z)13|<=∏j=0..12(151+j),
  |256^(-z-13)|<=256^-13.

Exact resulting rational:
  [328/27]*[7/(6*14!)]*∏(151+j)/256^13
   = 1069402300239520471/3802951800684688204490109616128
   < 3/10^13
This is an EXACT SOURCE-ONLY rational check. The new Lean proof
source is still NOT original v4.35 kernel accepted; only genuine
.olean files and standard-only #print axioms can certify the two
premise discharges. The two FINITE A_6,256 sign premises remain OPEN.

No RH, global Weil positivity, source ordinal53, curvature, CI
build/completion status, or numerical Lean claims are implied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from fractions import Fraction as F
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
LEAN=BASE/"cp011_zeta_v435"
SRC=LEAN/"CP027PointwiseBorwein.lean"
BRIDGE=LEAN/"CP027TwoFiniteSigns.lean"
UPSTREAM_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
TOOLCHAIN="leanprover/lean4:v4.35.0"
UPSTREAM_PINS={
    "Zeta/EulerMaclaurin/ErrorBound.lean":
      ("01184af0dbfd1369e14725e02e990b016bedfe6f",
       "noncomputable abbrev zetaRemainderBound"),
    "Zeta/EulerMaclaurin/Continuation.lean":
      ("1bb01e946fa7e344497eaf7694fbecff0a714d09",
       "noncomputable abbrev zetaApproximant"),
}
MATHLIB_PINS={
    "Mathlib/NumberTheory/Bernoulli.lean":
      ("45d389886738789e80185fd2a6da4185727ab502",
       "def bernoulli (n : ℕ)"),
    "Mathlib/RingTheory/Polynomial/Pochhammer.lean":
      ("f3503627af3430a48c087b85b03095e84dfb2824",
       "theorem ascPochhammer_succ_eval"),
    "Mathlib/Analysis/SpecialFunctions/Pow/Real.lean":
      ("97c12aed7085a7fc77727567d87e508064b49a18",
       "theorem norm_cpow_eq_rpow_re_of_pos"),
}
NAMES=[
    "original_ascending_pochhammer_norm",
    "original_B14",
    "original_B14_norm",
    "center_geometry",
    "center_prefactor",
    "original_cpow_norm",
    "original_omitted_term",
    "exact_center_majorant",
    "original_center_Borwein",
    "original_center_Borwein_left",
    "original_center_Borwein_right",
]
T0=F(15005352,100000)
T1=F(15005353,100000)
PREF=F(328,27)
CAP=F(3,10**13)
PURE=F(7,6*math.factorial(14))*F(math.prod(range(151,164)),256**13)
ENVELOPE=PREF*PURE
EXPECTED=F(1069402300239520471,3802951800684688204490109616128)
ALLOWED={"propext","Classical.choice","Quot.sound"}

def bernoulli(n):
    seq=[F(1)]
    for k in range(1,n+1):
        seq.append(F(1)-sum(
            F(math.comb(k,j),k-j+1)*seq[j]
            for j in range(k)))
    return ((-1)**n)*seq[n]

def arithmetic_selftest():
    assert bernoulli(0)==1 and bernoulli(1)==-F(1,2)
    assert bernoulli(12)==-F(691,2730)
    assert bernoulli(14)==F(7,6)
    assert T0==F("150.05352") and T1==F("150.05353")
    assert 0<T0<T1<F(151)-F(1,2)
    for t in (T0,T1):
        # Original s=1/2+i t, triangle norm upper 1/2 + t:
        assert F(1,2)+t<F(151)
        assert F(1,2)+13==F(27,2)
        assert (F(151)+13)/F(27,2)==PREF
    assert ENVELOPE==EXPECTED
    assert ENVELOPE<CAP
    assert ENVELOPE>F(28,10**14)   # reject a false 2.8e-13 cap
    assert (F(13)*PURE)>CAP        # K<13 alone is insufficient
    assert (PREF*F(7,6*math.factorial(14))*F(math.prod(range(151,164)),128**13))>CAP
    # True circle majorant is weaker but still < cap:
    assert ENVELOPE<F(656,53)*PURE<CAP
    assert CAP-ENVELOPE>0
    print("CP027 ORIGINAL TWO POINTS B14/POC13/328div27 FRACTION BOUND: PASS NOT LEAN")
    print("  original center prefactor <= 328/27")
    print("  exact original center upper =", ENVELOPE)
    print("  decimal upper ≈",format(float(ENVELOPE),".18e"))
    print("  strict remaining margin =", CAP-ENVELOPE)
    print("  2 root source-point caps: MATHEMATICAL original analytic candidates, NOT LEAN")
    print("  negative controls: K<=13 NOT sufficient; cutoff N=128 invalid; 2.8e-13 too tight")

def source_contract():
    src=SRC.read_text("utf8")
    bridge=BRIDGE.read_text("utf8")
    imports=re.findall(r"(?m)^public import\s+(\S+)",src)
    if not imports or any(not n.startswith(("Zeta.","Mathlib.")) for n in imports):
        raise ValueError("CP027 point leaf imports uncompiled local CP module")
    if re.search(r"(?m)^\s*(sorry|axiom|constant|opaque|unsafe)\b",src+"\n"+bridge):
        raise ValueError("CP027 source uses an untrusted proof admission")
    n=re.findall(r"(?m)^theorem\s+([A-Za-z0-9_']+)\b",src)
    prints=re.findall(r"(?m)^#print axioms\s+CP027PointwiseBorwein\.([A-Za-z0-9_']+)\b",src)
    if n!=NAMES or prints!=NAMES:
        raise ValueError(f"new source theorem/axiom source roster drift: {n}, {prints}")
    if re.findall(r"(?m)^theorem\s+([A-Za-z0-9_']+)\b",bridge)!=[
        "original_narrow_critical_line_zero_of_two_finite_signs"]:
        raise ValueError("CP027 exact two finite signs integration theorem missing")
    if not all(s in bridge for s in (
        "public import CP026OriginalPointBridge",
        "public import CP027PointwiseBorwein",
        "original_center_Borwein_left",
        "original_center_Borwein_right",
        "hFiniteLeft","hFiniteRight")):
        raise ValueError("CP027 bridge did not pay exactly two Borwein premises")
    if not all(s in src for s in (
        "zetaRemainderBound (center t) 6 256",
        "theorem original_center_Borwein_left",
        "theorem original_center_Borwein_right",
        "(328 : ℝ) / 27",
        "(151 : ℝ) + j",
        "Real.rpow_le_rpow_of_exponent_le")):
        raise ValueError("CP027 center lemma original math/API contents drift")
    config=(LEAN/"lakefile.toml").read_text("utf8")
    for lib in ("CP027PointwiseBorwein","CP027TwoFiniteSigns"):
        if f'name = "{lib}"' not in config:
            raise ValueError("unregistered original compiler target "+lib)
    if (LEAN/"lean-toolchain").read_text().strip()!=TOOLCHAIN:
        raise ValueError("source Lean compiler toolchain drift")
    print("CP027 UPSTREAM-ONLY POINT LEAF AND TWO FINITE SIGN BRIDGE SOURCE: 12/12 CONTRACT PASS NOT LEAN")

def git_sha(path):
    h=hashlib.sha1(b"blob "+str(path.stat().st_size).encode()+b"\0")
    with path.open("rb") as f:
        for piece in iter(lambda:f.read(1<<20),b""):h.update(piece)
    return h.hexdigest()

def source_sha_audit(zeta,mathlib):
    for base,pins in ((zeta,UPSTREAM_PINS),(mathlib,MATHLIB_PINS)):
        for path,(sha,token) in pins.items():
            item=base/path
            if git_sha(item)!=sha or token not in item.read_text("utf8"):
                raise ValueError("true frozen Git SHA/API mismatch "+path)
    print("CP027 FIVE IMMUTABLE ORIGINAL ZETA/MATHLIB SOURCE GATES: 5/5 PASS NOT LEAN")

def real_kernel_audit():
    source_contract()
    targets={
        "CP027PointwiseBorwein":NAMES,
        "CP027TwoFiniteSigns":["original_narrow_critical_line_zero_of_two_finite_signs"]
    }
    for mod,names in targets.items():
        olean=LEAN/".lake/build/lib/lean"/(mod+".olean")
        log=LEAN/(mod+"-actual-source-axioms.log")
        if not olean.is_file() or not log.is_file():
            raise ValueError("NOT READY genuine original .olean or axiom log missing: "+mod)
        text=log.read_text("utf8")
        if "error:" in text or "sorryAx" in text or "unsolved goals" in text:
            raise ValueError("NOT READY: original Lean actually rejected source "+mod)
        for name in names:
            reg=re.compile(re.escape("'"+mod+"."+name+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
            matches=reg.findall(text)
            if len(matches)!=1:
                raise ValueError("NOT READY missing actual unique axiom log "+mod+"."+name)
            axioms={v.strip() for v in matches[0].split(",") if v.strip()}
            if not axioms<=ALLOWED:
                raise ValueError("NOT READY nonstandard axiom in "+mod+"."+name+": "+str(axioms-ALLOWED))
    print("CP027 ACTUAL TWO ORIGINAL v4.35 MODULE KERNEL COMPILATIONS/12 STANDARD AXIOMS: PASS")
    print("  ORIGINAL 2 FINITE A6N256 SIGN CERTIFICATES STILL UNPAID")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--source-check",action="store_true")
    p.add_argument("--original-zeta",type=Path)
    p.add_argument("--original-mathlib",type=Path)
    p.add_argument("--kernel-audit",action="store_true")
    p.add_argument("--receipt",type=Path)
    a=p.parse_args()
    if a.self_test: arithmetic_selftest()
    if a.source_check: source_contract()
    if bool(a.original_zeta)!=bool(a.original_mathlib):
        p.error("need BOTH original Zeta AND Mathlib roots")
    if a.original_zeta:source_sha_audit(a.original_zeta,a.original_mathlib)
    if a.kernel_audit:real_kernel_audit()
    if a.receipt:
        if not (a.self_test and a.source_check and a.original_zeta):
            raise ValueError("NOT READY source receipt requires exact math, 12 proof-candidate declarations, and true 5 upstream blob/API checks")
        o={
            "status":"CP027_ORIGINAL_CENTER_BORWEIN_FRACTION_AND_SOURCE_PRECHECK_PASS_NOT_LEAN",
            "original_upstream_zeta_git_commit":UPSTREAM_COMMIT,
            "original_Lean":TOOLCHAIN,
            "original_five_pinned_Git_blobs":{k:v[0] for k,v in {**UPSTREAM_PINS,**MATHLIB_PINS}.items()},
            "source_only_pointwise_majorant_ratio":str(ENVELOPE),
            "source_only_pointwise_majorant_float":format(float(ENVELOPE),".18e"),
            "original_two_target_heights":[str(T0),str(T1)],
            "original_B14":"7/6",
            "original_prefactor":"328/27",
            "original_13_factor_Pochhammer_numerical_constant":str(math.prod(range(151,164))),
            "original_theta_and_numerical_BRACKET_intact":True,
            "unpaid_new_Lean_pointwise_left":True,
            "unpaid_new_Lean_pointwise_right":True,
            "unpaid_new_Lean_left_finite_sign":True,
            "unpaid_new_Lean_right_finite_sign":True,
            "CP027_actual_Lean_4_35_kernels_compiled":False,
            "CP027_original_narrow_root_unconditional_Lean_theorem":False,
            "source_ordinal53_identification":False,
            "full_interval_curvature":False,
            "global_signed_Weil_spectral_equivalence":False,
            "RH":False,
        }
        a.receipt.write_text(json.dumps(o,indent=2)+"\n",encoding="utf8")
        print(o["status"])
    if not any((a.self_test,a.source_check,a.original_zeta,a.kernel_audit)):
        p.print_help()
if __name__=="__main__":
    try:main()
    except (AssertionError,OSError,ValueError,UnicodeError) as e:
        raise SystemExit("CP027 NOT READY / INVALID: "+repr(e))
