#!/usr/bin/env python3
"""IV011 strict original mixed prime-support arithmetic and Schur-necessity audit.

A successful preflight is NOT a Lean kernel certificate. The independent
Lean build and 16 source-bound #print axioms receipts are necessary to
promote any theorem. No missing zeta cross-support inequality is assumed.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.olean")
LOG = Path("iv011-original-cross-support-arithmetic-axioms.log")
OUT = Path("iv011-original-cross-support-arithmetic-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralIV006Schwartz_window_ae",
    "neutralIV010OldPlusNew_realBlock",
    "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
    "neutralNF600Correlation_eq",
]
NEW = [
    "neutralIV011MixedCorrelation_eq_schwartzIntegral",
    "neutralIV011MixedCorrelation_vanish_far",
    "neutralIV011MixedPrime_logFar_vanish",
    "neutralIV011ExistsPrimeCutoff",
    "neutralIV011OriginalMixedPrime_eq_finite",
    "neutralIV011OriginalMixed_arithmeticSplit",
    "neutralIV011OriginalMixed_finitePrimeArithmetic",
    "neutralIV011SchurMinimizer_value",
    "neutralIV011SchurFailure_negative",
    "neutralIV011OriginalCrossFailure_negativeWitness",
    "neutralIV011OriginalCrossBound_necessary",
    "neutralIV011OriginalOneNew_nonnegative_iff_crossBound",
]
NAMES = UPSTREAM + NEW
DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVHermitianTwoBlockPSD.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaLiteralFormula.lean"),
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
]

def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def preflight() -> None:
    raw = LEAN.read_text()
    for token in (
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportExtension",
        "import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeBound",
        "measurePreserving_sub_right",
        "neutralIV006Schwartz_window_ae",
        "neutralWindowCorrelation",
        "neutralIV011MixedCorrelation_vanish_far",
        "neutralIV011MixedPrime_logFar_vanish",
        "Real.log_lt_log",
        "ArithmeticFunction.vonMangoldt n / Real.sqrt n",
        "tsum_eq_sum",
        "Zeta23.EF.literatureRHS",
        "neutralIV011OriginalMixed_finitePrimeArithmetic",
        "neutralIV010OldPlusNew_realBlock",
        "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
        "neutralIV011OriginalCrossFailure_negativeWitness",
        "neutralIV011OriginalOneNew_nonnegative_iff_crossBound",
    ):
        assert token in raw, f"Missing authentic source marker {token}"
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", raw, re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b", raw)
    assert re.findall(r"^#print axioms (\w+)$", raw, re.M) == NAMES
    assert re.findall(r"^theorem (neutralIV011\w+)", raw, re.M) == NEW
    for dep in DEPS:
        assert dep.is_file(), dep
    print("IV011 original-source preflight PASS: 12 proof candidates, 4 genuine upstream anchors; independent Lean compiler + axioms PENDING.")

def verify() -> None:
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, "Real Lean .olean required"
    raw = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        raw, re.I,
    ), "Lean error, non-kernel axiom, or sorryAx in compiler log"
    found = {}
    for name in NAMES:
        label = "'WeilDefect." + name + "'"
        yes = re.findall(re.escape(label) + r" depends on axioms: \[([^\]]*)\]", raw, re.S)
        no = re.findall(re.escape(label) + r" does not depend on any axioms", raw, re.S)
        assert len(yes) + len(no) == 1, (name, len(yes), len(no))
        axioms = [] if no else [x.strip() for x in yes[0].split(",") if x.strip()]
        assert set(axioms) <= ALLOWED, (name, axioms)
        found[name] = axioms
    report = {
        "schema": "IV011-genuine-zeta-cross-support-prime-cutoff-and-strict-Schur-witness-v1",
        "scope": "Mixed compact Schwartz correlation support radius a+b, exact finite von-Mangoldt prime truncation, unchanged literal pole/arch terms, necessary and sufficient new-support mixed Schur bound when D>0.",
        "source_sha256": {str(p): sha256(p) for p in [LEAN] + DEPS},
        "compiled_olean_sha256": sha256(OLEAN),
        "source_anchors": UPSTREAM,
        "new_iv011_theorems": NEW,
        "axioms": found,
        "new_zeta_cross_bound_established": False,
        "new_zeta_diagonal_nonnegative_established": False,
        "global_Weil_positivity_established": False,
        "RH_established": False,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("IV011 exact arithmetic prime cutoff and sharp conditional Schur necessity: 12 NEW KERNEL PASS; source/axiom custody verified. Still NO new-support positivity.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("preflight", "verify"))
    stage = parser.parse_args().stage
    if stage == "preflight":
        preflight()
    else:
        verify()
