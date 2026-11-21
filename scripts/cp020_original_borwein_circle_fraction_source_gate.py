#!/usr/bin/env python3
"""CP020 exact original-source Borwein circle bound and derivative transport.

This script proves only rational NUMERICAL inequalities in Python.  It
checks all original pinned Git SHA and genuine theorem names.  It does
not compile Lean, prove a complex-analytic theorem, obtain an .olean or
certify actual original Hardy-Z curvature/root existence.

Mathematical source reduction:
  Re(z)>=1/4; |z|<=151 for all |z-(1/2+it)|=1/4,
  149.5<=t<=150.05353.
  B14=7/6, ||(z)_13|| <= ∏(151+j), |256^(-z-13)| <= 256^-13.
  K<=656/53.
  Hence original Borwein<=EXACT_RATIO<3/10^13.
  Holomorphy + actual original Cauchy then imply
  ||D^k(ζ-A)|| <= k!(3/10^13)*4^k.

External Python tests confirm rational arithmetic and negative controls.
New Lean source proof candidate claims ALL the quantified real/complex
steps and will require real original v4.35 kernel receipts.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
ORIGINAL_MATHLIB="v4.35.0"
ZETA_BLOBS={
 "Zeta/EulerMaclaurin/Continuation.lean":"1bb01e946fa7e344497eaf7694fbecff0a714d09",
 "Zeta/EulerMaclaurin/ErrorBound.lean":"01184af0dbfd1369e14725e02e990b016bedfe6f",
}
MATHLIB_BLOBS={
 "Mathlib/RingTheory/Polynomial/Pochhammer.lean":
   "f3503627af3430a48c087b85b03095e84dfb2824",
 "Mathlib/NumberTheory/Bernoulli.lean":
   "45d389886738789e80185fd2a6da4185727ab502",
 "Mathlib/Analysis/Calculus/IteratedDeriv/Lemmas.lean":
   "d9348833bece1297dd8ffe57e6b976fcc268af38",
 "Mathlib/Analysis/Complex/Liouville.lean":
   "70382d63ec267d2704790b1d77692e1f5cd5faed",
}
LEANS={
 "CP020Pochhammer.lean":[
    "norm_ascPochhammer_eval_le_product",
    "original_bernoulli_fourteen",
    "source_B14_coefficient_norm",
    "majorant_product_nonneg"],
 "CP020BorweinCircle.lean":[
    "source_circle_geometry",
    "original_Borwein_prefactor_le",
    "original_complex_cpow_bound",
    "original_Borwein_omitted_term_le",
    "exact_original_Borwein_real_envelope",
    "original_Borwein_all_circles",
    "original_EM_Cauchy_all_heights",
    "original_EM_third_derivative_all_heights"],
 "CP020DerivativeTransport.lean":[
    "original_zeta_EM_germs_equal",
    "original_zeta_EM_derivative_error_identity",
    "original_center_valid",
    "original_zeta_approximant_derivative_error_all_heights",
    "original_zeta_approximant_third_derivative_error_all_heights"],
}
SOURCE_SIGNATURES={
 "Zeta/EulerMaclaurin/Continuation.lean":[
    "theorem riemannZeta_eq_approximant_add_remainder",
    "noncomputable abbrev zetaApproximant",
    "noncomputable abbrev zetaRemainder"],
 "Zeta/EulerMaclaurin/ErrorBound.lean":[
    "theorem norm_zetaRemainder_le",
    "noncomputable abbrev zetaRemainderBound"],
 "Mathlib/RingTheory/Polynomial/Pochhammer.lean":[
    "theorem ascPochhammer_succ_eval"],
 "Mathlib/NumberTheory/Bernoulli.lean":[
    "def bernoulli' (n : ℕ)",
    "def bernoulli (n : ℕ)"],
 "Mathlib/Analysis/Calculus/IteratedDeriv/Lemmas.lean":[
    "lemma Filter.EventuallyEq.iteratedDeriv_eq"],
 "Mathlib/Analysis/Complex/Liouville.lean":[
    "theorem norm_iteratedDeriv_le_of_forall_mem_sphere_norm_le"],
}
LEFT=F(299,2)
RIGHT=F(15005353,100000)
RADIUS=F(1,4)
BORWEIN_CAP=F(3,10**13)
EXACT_RATIO=F(181596617021805363,633825300114114700748351602688)

def bernoulli_via_recurrence(n):
    positive=[F(1)]
    for k in range(1,n+1):
        val=F(1)-sum(
            F(math.comb(k,j),k-j+1)*positive[j] for j in range(k))
        positive.append(val)
    return (-1)**n * positive[n]

def exact_test():
    assert LEFT==F("149.5") and RIGHT==F("150.05353")
    assert LEFT<RIGHT and RIGHT-LEFT==F(55353,100000)
    assert F(1,2)-RADIUS==F(1,4)
    assert F(1,2)+RIGHT+RADIUS==F(15080353,100000)<151
    # uniform original Borwein K majorant:
    assert F(151+13,F(1,4)+13)==F(656,53)
    # genuine rational Bernoulli coefficient via independent recurrence:
    assert bernoulli_via_recurrence(1)==-F(1,2)
    assert bernoulli_via_recurrence(12)==-F(691,2730)
    assert bernoulli_via_recurrence(14)==F(7,6)
    prod=math.prod(151+j for j in range(13))
    bound=F(656,53)*F(7,6*math.factorial(14))*F(prod,256**13)
    assert bound==EXACT_RATIO and bound<BORWEIN_CAP
    for k in range(4):
        ck=F(math.factorial(k))*BORWEIN_CAP/RADIUS**k
        assert ck>F(math.factorial(k))*EXACT_RATIO/RADIUS**k
    assert F(math.factorial(3))*BORWEIN_CAP/RADIUS**3==F(1152,10**13)
    # rigorous algebraic counterchecks, NOT actual ζ counterexamples:
    assert EXACT_RATIO>F(2,10**13)
    assert F(4,10**13)>BORWEIN_CAP
    assert F(math.factorial(3))*BORWEIN_CAP/RADIUS**3>F(1,10**10)
    print("CP020 EXACT ORIGINAL BORWEIN COMPLEX-CIRCLE ENVELOPE: PASS — NOT LEAN")
    print("  source 151 bound and original K<=656/53 exact: PASS")
    print("  independent B14 recurrence gives 7/6 exact: PASS")
    print("  13-factor Pochhammer rational envelope =",EXACT_RATIO)
    print("  strict cap =",BORWEIN_CAP)
    for k in range(4):
        print(f"  k={k} conditional Cauchy cap =",F(math.factorial(k))*BORWEIN_CAP/RADIUS**k)
    print("  deliberately stronger-false source bounds rejected: PASS")
    print("  universal original complex inequalities remain NEW LEAN SOURCE CANDIDATES")

def git_blob(p):
    h=hashlib.sha1(b"blob "+str(p.stat().st_size).encode()+b"\0")
    with p.open("rb") as f:
        for part in iter(lambda:f.read(1<<20),b""):
            h.update(part)
    return h.hexdigest()

def source_gate(zeta,mathlib,receipt):
    sources={}
    for base,pins in ((zeta,ZETA_BLOBS),(mathlib,MATHLIB_BLOBS)):
        for name,expected in pins.items():
            f=base/name
            got=git_blob(f)
            if got!=expected:
                raise ValueError(f"Original Git blob mismatch {name} got {got} expected {expected}")
            sources[name]=f.read_text("utf-8")
    for name,needles in SOURCE_SIGNATURES.items():
        for needle in needles:
            if needle not in sources[name]:
                raise ValueError("Pinned ORIGINAL source theorem signature drift "+name+" :: "+needle)
    for name,targets in LEANS.items():
        p=ROOT/"cp011_zeta_v435"/name
        body=p.read_text("utf-8")
        for target in targets:
            if f"theorem {target}" not in body or f"#print axioms CP020{name[5:-5]}.{target}" not in body:
                raise ValueError("Missing CP020 new Lean source theorem/axiom checker: "+name+" :: "+target)
        if "\nsorry\n" in body or "\naxiom " in body:
            raise ValueError("Explicit untrusted Lean axiom/sorry: "+name)
    body=(ROOT/"cp011_zeta_v435/CP020DerivativeTransport.lean").read_text("utf-8")
    if "Filter.EventuallyEq.iteratedDeriv_eq" not in body:
        raise ValueError("Missing actual ORIGINAL Mathlib derivative-germ equality method")
    content={
      "status":"CP020_ORIGINAL_SIX_BLOB_SOURCE_AND_FRACTION_PASS_NOT_KERNEL",
      "original_zeta_commit":COMMIT,"original_mathlib_ref":ORIGINAL_MATHLIB,
      "original_sha_pins":{**ZETA_BLOBS,**MATHLIB_BLOBS},
      "new_Lean_theorem_source_targets":{n:targets for n,targets in LEANS.items()},
      "genuine_all_circle_source_inequality_proved_by_Lean":False,
      "actual_original_v435_compiled_oleans_available":False,
      "exact_complex_circle_radius":"1/4",
      "exact_source_height_window":[str(LEFT),str(RIGHT)],
      "exact_original_Borwein_upper":str(EXACT_RATIO),
      "strict_uniform_complex_remainder_cap":str(BORWEIN_CAP),
      "Cauchy_derivative_caps_if_Lean_source_proofs_compile":[
        str(F(math.factorial(k))*BORWEIN_CAP/RADIUS**k) for k in range(4)],
      "actual_original_zeta_approximant_derivative_transport_Lean_proved":False,
      "HardyZ_derivative_anchor_2_4_verified":False,
      "HardyZ_uniform_curvature_le4_verified":False,
      "new_original_root53_numeric_sign_verified":False,
      "original_signed_Weil_spectral_dictionary":False,
      "global_Weil_positivity_or_RH":False,
    }
    receipt.write_text(json.dumps(content,indent=2)+"\n",encoding="utf-8")
    print(content["status"])

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--zeta",type=Path)
    p.add_argument("--mathlib",type=Path)
    p.add_argument("--receipt",type=Path,
                   default=Path("cp020-original-source-Borwein-fraction.json"))
    args=p.parse_args()
    if args.self_test:exact_test()
    if bool(args.zeta)!=bool(args.mathlib):
        p.error("Need BOTH original frozen Zeta and Mathlib source roots")
    if args.zeta:
        try:source_gate(args.zeta,args.mathlib,args.receipt)
        except (OSError,UnicodeError,ValueError) as e:
            raise SystemExit("NOT_READY: "+str(e))
    if not (args.self_test or args.zeta):p.print_help()

if __name__=="__main__":
    main()
