#!/usr/bin/env python3
"""IV013 genuine original mixed zeta phase-interference/prime-free audit.

All 9 new original-source theorems remain Lean candidates until a real
kernel compile and independent standard-axiom receipts succeed. This
stage does not assert the new-support arithmetic alignment inequality,
the new diagonal sign, global Weil positivity or RH.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.olean")
LOG = Path("iv013-original-phase-cancellation-axioms.log")
OUT = Path("iv013-original-phase-cancellation-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralIV011OriginalMixed_finitePrimeArithmetic",
    "neutralIV011OriginalCrossFailure_negativeWitness",
    "neutralIV012OriginalMixed_norm_le_arithmeticBudget",
    "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
]
NEW = [
    "neutralIV013OriginalMixed_eq_analytic_sub_prime",
    "neutralIV013OriginalMixed_phaseInterference",
    "neutralIV013OriginalMixed_crossBound_iff_alignment",
    "neutralIV013PrimeSeparated_correlationVanish",
    "neutralIV013PrimeSeparated_originalPrime_zero",
    "neutralIV013PrimeSeparated_originalMixed_eq_analytic",
    "neutralIV013OriginalOneNew_nonnegative_of_alignment",
    "neutralIV013OriginalOneNew_negative_of_alignmentFailure",
    "neutralIV013PrimeSeparated_oneNew_nonnegative_of_analyticBound",
]
NAMES = UPSTREAM + NEW
DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationPoles.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaLiteralFormula.lean"),
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def preflight() -> None:
    source = LEAN.read_text()
    for term in (
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope",
        "neutralIV011OriginalMixedPrime b s t",
        "neutralIV011OriginalMixedPole b s t",
        "neutralIV011OriginalMixedArch b s t",
        "neutralIV013OriginalMixedAnalyticRemainder",
        "neutralIV013OriginalMixed_phaseInterference",
        "neutralIV013OriginalMixed_crossBound_iff_alignment",
        "neutralIV013OriginalPrimeSeparated",
        "neutralIV011MixedCorrelation_eq_schwartzIntegral",
        "neutralIV011OriginalMixedPrime_eq_finite",
        "neutralIV011OriginalCrossFailure_negativeWitness",
        "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
        "neutralIV013PrimeSeparated_oneNew_nonnegative_of_analyticBound",
    ):
        assert term in source, ("Missing original arithmetic marker", term)
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", source, re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b", source)
    assert re.findall(r"^#print axioms (\w+)$", source, re.M) == NAMES
    assert re.findall(r"^theorem (neutralIV013\w+)", source, re.M) == NEW
    for dep in DEPS:
        assert dep.is_file(), dep
    print("IV013 original source preflight PASS: 9 phase-aware arithmetic and prime-separated source candidates, 4 upstream receipts. LEAN KERNEL PENDING.")

def verify() -> None:
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, "Real original Lean compiled object missing"
    log = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        log, re.I,
    ), "Lean compiler or nonstandard axiom failure"
    found = {}
    for name in NAMES:
        target = "'WeilDefect." + name + "'"
        yes = re.findall(re.escape(target) + r" depends on axioms: \[([^\]]*)\]", log, re.S)
        no = re.findall(re.escape(target) + r" does not depend on any axioms", log, re.S)
        assert len(yes) + len(no) == 1, (name, len(yes), len(no))
        axioms = [] if no else [v.strip() for v in yes[0].split(",") if v.strip()]
        assert set(axioms) <= ALLOWED, (name, axioms)
        found[name] = axioms
    result = {
        "schema": "IV013-original-zeta-cross-support-phase-cancellation-prime-free-kernel-v1",
        "scope": "Exact original arithmetic finite prime vs pole/Gamma complex-phase interference; prime-separated Schwartz source criteria; conditional sharp new-support positivity/negative-witness gates.",
        "source_sha256": {str(p): digest(p) for p in [LEAN] + DEPS},
        "compiled_olean_sha256": digest(OLEAN),
        "upstream_source_anchors": UPSTREAM,
        "new_iv013_theorems": NEW,
        "axioms": found,
        "new_support_cross_arithmetic_alignment_established": False,
        "prime_separation_condition_established_for_new_test": False,
        "new_support_diagonal_positivity_established": False,
        "global_Weil_positivity_established": False,
        "RH_established": False,
    }
    OUT.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("IV013 PHASE-SENSITIVE ORIGINAL SOURCE LEAN KERNEL PASS: 9 proof receipts + 4 upstream. No unconditional support extension.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("preflight", "verify"))
    if p.parse_args().stage == "preflight":
        preflight()
    else:
        verify()
