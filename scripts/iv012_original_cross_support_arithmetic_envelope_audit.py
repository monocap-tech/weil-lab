#!/usr/bin/env python3
"""IV012 genuine zeta mixed prime/pole/Gamma arithmetic envelope audit.

Source preflight is NOT kernel acceptance. Requires actual Lean source
compilation and only-standard-axiom receipts for 13 new and 4 upstream
declarations. The envelope-square estimate and new diagonal positivity
remain UNPROVED mathematical hypotheses.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.olean")
LOG = Path("iv012-original-arithmetic-envelope-axioms.log")
OUT = Path("iv012-original-arithmetic-envelope-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralIV011OriginalMixed_finitePrimeArithmetic",
    "neutralIV011OriginalMixed_arithmeticSplit",
    "neutralIV011OriginalOneNew_nonnegative_iff_crossBound",
    "neutralWindowCorrelation_poleCrossTerms",
]
NEW = [
    "neutralIV012PhysicalOverlapCost_nonnegative",
    "neutralIV012MixedCorrelation_norm_le_overlap",
    "neutralIV012OriginalPrimeOverlapBudget_nonnegative",
    "neutralIV012OriginalMixedPrime_norm_le_overlapBudget",
    "neutralIV012OriginalPoleMomentBudget_nonnegative",
    "neutralIV012OriginalMixedPole_eq_sourceMoments",
    "neutralIV012OriginalMixedPole_norm_le_momentBudget",
    "neutralIV012OriginalGammaAbsoluteBudget_nonnegative",
    "neutralIV012OriginalMixedArch_norm_le_gammaBudget",
    "neutralIV012OriginalMixedArithmeticBudget_nonnegative",
    "neutralIV012OriginalMixed_norm_le_arithmeticBudget",
    "neutralIV012OriginalMixedSchur_of_arithmeticBudget",
    "neutralIV012OriginalOneNew_nonnegative_of_budget",
]
NAMES = UPSTREAM + NEW
SOURCE_DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationPoles.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaLiteralFormula.lean"),
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def preflight() -> None:
    raw = LEAN.read_text()
    checks = (
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff",
        "neutralIV011MixedCorrelation_eq_schwartzIntegral",
        "neutralIV011OriginalMixedPrime_eq_finite",
        "ArithmeticFunction.vonMangoldt n / Real.sqrt n",
        "neutralIV012PhysicalOverlapCost",
        "neutralIV012OriginalFinitePrimeOverlapBudget",
        "neutralIV012OriginalPoleMomentBudget",
        "neutralWindowCorrelation_poleCrossTerms",
        "sourceWindowMoment b",
        "neutralIV012OriginalGammaAbsoluteBudget",
        "Zeta23.EF.gammaBracket",
        "Zeta23.paperFT",
        "neutralIV011OriginalMixed_arithmeticSplit",
        "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
        "neutralIV012OriginalOneNew_nonnegative_of_budget",
    )
    for token in checks:
        assert token in raw, ("Missing source marker", token)
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", raw, re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b", raw)
    actual = re.findall(r"^#print axioms (\w+)$", raw, re.M)
    assert actual == NAMES, (actual, NAMES)
    actual_new = re.findall(r"^theorem (neutralIV012\w+)", raw, re.M)
    assert actual_new == NEW, (actual_new, NEW)
    for dep in SOURCE_DEPS:
        assert dep.is_file(), dep
    print("IV012 source preflight PASS: 13 original-source prime/pole/Gamma envelope proof candidates and 4 genuine upstream anchors; LEAN KERNEL PENDING.")

def verify() -> None:
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, "Original compiled Lean .olean required"
    log = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        log, re.I,
    ), "Lean error / nonstandard axiom / sorryAx"
    found = {}
    for name in NAMES:
        label = "'WeilDefect." + name + "'"
        yes = re.findall(re.escape(label) + r" depends on axioms: \[([^\]]*)\]", log, re.S)
        no = re.findall(re.escape(label) + r" does not depend on any axioms", log, re.S)
        assert len(yes) + len(no) == 1, (name, len(yes), len(no))
        axioms = [] if no else [v.strip() for v in yes[0].split(",") if v.strip()]
        assert set(axioms) <= ALLOWED, (name, axioms)
        found[name] = axioms
    report = {
        "schema": "IV012-genuine-zeta-prime-pole-gamma-Schur-envelope-kernel-v1",
        "scope": "Original physical Schwartz overlap-cost finite-prime norm bound, exact two-pole moment budget, original gamma Fourier absolute-integral bound, and conditional Schur extension by budget-square domination.",
        "source_sha256": {str(p): digest(p) for p in [LEAN] + SOURCE_DEPS},
        "compiled_olean_sha256": digest(OLEAN),
        "upstream_source_anchors": UPSTREAM,
        "new_iv012_theorems": NEW,
        "axioms": found,
        "envelope_square_bound_established": False,
        "new_diagonal_nonnegativity_established": False,
        "expanded_support_positivity_established": False,
        "global_Weil_positivity_established": False,
        "RH_established": False,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("IV012 ORIGINAL SOURCE-SPECIFIC LEAN KERNEL PASS: 13 new and 4 upstream axiom certificates. New mixed Schur budget inequality NOT discharged.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("preflight", "verify"))
    if parser.parse_args().stage == "preflight":
        preflight()
    else:
        verify()
