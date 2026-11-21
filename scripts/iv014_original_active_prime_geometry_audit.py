#!/usr/bin/env python3
"""IV014 genuine zeta Λ-active prime geometry strict Lean kernel audit.

No source preflight is a proof. The original full divisors, exact
prime Λ(n)/sqrt(n), physical Schwartz correlation, and genuine pole+
Gamma remainder are used directly. Both original new-support diagonal
positivity and the residual Schur inequality remain OPEN assumptions.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean")
OLEAN=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.olean")
LOG=Path("iv014-original-active-prime-geometry-axioms.log")
OUT=Path("iv014-original-active-prime-geometry-kernel-audit.json")
ALLOWED={"propext","Classical.choice","Quot.sound"}

UPSTREAM=[
  "neutralIV011OriginalMixedPrime_eq_finite",
  "neutralIV013OriginalMixed_eq_analytic_sub_prime",
  "neutralIV012OriginalMixedArch_norm_le_gammaBudget",
  "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
]
NEW=[
  "neutralIV014ActiveSeparated_of_strong",
  "neutralIV014ActiveCorrelation_vanish",
  "neutralIV014ActivePhysicalOverlap_zero",
  "neutralIV014ActiveFinitePrimeBudget_zero",
  "neutralIV014ActiveMixedPrime_zero",
  "neutralIV014ActiveMixed_eq_analytic",
  "neutralIV014ActiveSeparated_of_intervalGap",
  "neutralIV014ActiveArithmeticBudget_eq_residual",
  "neutralIV014ActiveMixed_norm_le_residualBudget",
  "neutralIV014ActiveOneNew_nonnegative_of_residual",
]
NAMES=UPSTREAM+NEW
DEPS=[
  "WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean",
  "WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean",
  "WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean",
  "WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean",
  "WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean",
  "WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean",
  "WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean",
  "WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean",
  "WeilDefect/Arithmetic/ActualZetaCorrelationPoles.lean",
  "WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean",
  "WeilDefect/Arithmetic/ActualZetaLiteralFormula.lean",
  "WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean",
]

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def preflight():
    source=LEAN.read_text()
    for token in (
      "import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation",
      "ArithmeticFunction.vonMangoldt n ≠ 0",
      "neutralIV013OriginalPrimeSeparated",
      "neutralIV011MixedCorrelation_eq_schwartzIntegral",
      "neutralIV012PhysicalOverlapCost",
      "neutralIV012OriginalFinitePrimeOverlapBudget",
      "neutralIV011OriginalMixedPrime_eq_finite",
      "neutralIV013OriginalMixed_eq_analytic_sub_prime",
      "neutralIV014ActiveSeparated_of_intervalGap",
      "neutralIV014ActiveMixed_norm_le_residualBudget",
      "neutralIV014ActiveOneNew_nonnegative_of_residual",
    ):
        assert token in source,("missing actual original source marker",token)
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",source,re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b",source)
    assert re.findall(r"^theorem (neutralIV014\w+)",source,re.M)==NEW
    assert re.findall(r"^#print axioms (\w+)$",source,re.M)==NAMES
    for path in DEPS:
        assert Path(path).is_file(),path
    print("IV014 genuine original source preflight PASS: 10 Λ-active prime interval/EF reduction proofs and 4 source anchors. LEAN KERNEL VERIFICATION PENDING.")

def verify():
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size>0,"Actual compiled Lean kernel .olean REQUIRED"
    log=LOG.read_text()
    assert not re.search(r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",log,re.I)
    results={}
    for name in NAMES:
        target="'WeilDefect."+name+"'"
        has=re.findall(re.escape(target)+r" depends on axioms: \[([^\]]*)\]",log,re.S)
        none=re.findall(re.escape(target)+r" does not depend on any axioms",log,re.S)
        assert len(has)+len(none)==1,(name,has,none)
        axioms=[] if none else [x.strip() for x in has[0].split(",") if x.strip()]
        assert set(axioms)<=ALLOWED,(name,axioms)
        results[name]=axioms
    record={
      "schema":"IV014-original-vonMangoldt-active-geometric-prime-free-kernel-v1",
      "scope":"Original full Λ-active translated source separation; literal pole/Gamma residual and source-specific conditional one-new-support Schur positivity. Does not claim existence of nonzero new supports or unconditional analytic inequality.",
      "source_sha256":{str(path):sha(path) for path in [LEAN]+list(map(Path,DEPS))},
      "compiled_olean_sha256":sha(OLEAN),
      "upstream_source_anchors":UPSTREAM,
      "new_theorems":NEW,
      "axioms":results,
      "nonzero_genuinely_enlarged_schwartz_test_constructed":False,
      "new_zeta_residual_square_bound_proved":False,
      "new_zeta_diagonal_nonnegative_proved":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
    }
    OUT.write_text(json.dumps(record,sort_keys=True,indent=2)+"\n")
    print("IV014 SOURCE ORIGINAL Λ-active arithmetic geometry KERNEL PASS: 10 new genuine-source and 4 original-source anchors; no new-support positivity claim.")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight":preflight()
    else:verify()
