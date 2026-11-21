#!/usr/bin/env python3
"""IV016: strict direct Lean kernel custody of complete original frozen
finite ±log n gap and genuine source prime-free new self-diagonal.

Unlike IV015's independent exact-rational Fraction gap receipt, IV016
requires the WHOLE four-collar/signed logarithmic inequality in an
actual compiled Lean theorem, with standard-only axiom audit.

The authentic NF543 two collars, frozen c=1/5,r=1/1000,N=10, complete
original von Mangoldt prime sum and true pole+Gamma remainder are
source-bound. No oracle, surrogate matrix or global Weil positivity.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.olean")
LOG = Path("iv016-original-concrete-prime-gap-diagonal-axioms.log")
OUT = Path("iv016-original-concrete-prime-gap-diagonal-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralIV015ExistsComplexSchwartzBump",
    "neutralIV015FrozenConcrete_logCutoff",
    "neutralIV014ActiveMixedPrime_zero",
    "neutralIV015FrozenCollar_activeSeparated_of_gap",
]
NEW = [
    "neutralIV016FrozenLogBand_lt10",
    "neutralIV016NatLog_nonnegative",
    "neutralIV016AbsClearance",
    "neutralIV016FrozenFourSignedGaps_of_band",
    "neutralIV016FrozenConcrete_allIntegerGap",
    "neutralIV016FrozenConcrete_originalPrimeFreeBump",
    "neutralIV016FrozenSelfLogClearance",
    "neutralIV016FrozenSelfActiveGap",
    "neutralIV016FrozenSmallBump_selfPrime_zero",
    "neutralIV016ExistsConcretePrimeFreeMixedAndDiagonal",
]
NAMES = UPSTREAM + NEW
DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteLocalSpan.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVLocalSpan.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollar242Correction.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeGeometry.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationPoles.lean"),
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
    Path("scripts/iv015_frozen_collar_exact_log_gap.py"),
    Path("scripts/iv015_original_nonzero_two_collar_schwartz_audit.py"),
    Path("lean-toolchain"),
    Path("lake-manifest.json"),
]

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def source_preflight():
    raw = LEAN.read_text()
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", raw, re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b", raw)
    assert re.findall(r"^theorem (neutralIV016\w+)", raw, re.M) == NEW
    assert re.findall(r"^#print axioms (\w+)$", raw, re.M) == NAMES
    for marker in (
        "neutralIV015FrozenTwoCollarActiveGap",
        "neutralIV016FrozenConcrete_allIntegerGap",
        "neutralIV016FrozenConcrete_originalPrimeFreeBump",
        "Real.log_two_gt_d9",
        "Real.log_two_lt_d9",
        "Real.log_three_gt_d9",
        "Real.log_three_lt_d9",
        "Real.log_five_gt_d9",
        "Real.log_four_eq",
        "ArithmeticFunction.vonMangoldt_ne_zero_iff",
        "neutralIV016FrozenSelfActiveGap",
        "neutralIV014ActiveSeparated_of_intervalGap",
        "neutralIV014ActiveMixedPrime_zero",
        "neutralIV014ActiveMixed_eq_analytic",
        "neutralIV010Diagonal",
        "neutralIV013OriginalMixedAnalyticRemainder",
        "neutralIV016ExistsConcretePrimeFreeMixedAndDiagonal",
    ):
        assert marker in raw, ("Missing actual original source", marker)
    for p in DEPS:
        assert p.is_file(),p
    print("IV016 SOURCE PREFLIGHT PASS: 10 direct exact-log original Lean proof candidates and 4 upstream authentic source axioms; real LEAN KERNEL PENDING.")


def kernel_verify():
    source_preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, (
        "Real compiled original ±log n kernel theorem object REQUIRED")
    raw = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        raw, re.I,
    ), "Lean error or sorryAx"
    axioms = {}
    for name in NAMES:
        target = "'WeilDefect." + name + "'"
        yes = re.findall(
            re.escape(target) + r" depends on axioms: \[([^\]]*)\]", raw, re.S)
        none = re.findall(
            re.escape(target) + r" does not depend on any axioms", raw, re.S)
        assert len(yes)+len(none)==1,(name, len(yes), len(none))
        found = [] if none else [x.strip() for x in yes[0].split(",") if x.strip()]
        assert set(found) <= ALLOWED, (name,found)
        axioms[name] = found
    report = {
        "schema":"IV016-original-true-two-collar-complete-Lean-log-gap-prime-free-diagonal-v1",
        "scope":"Original NF543 two-collar nonzero Schwartz t(c)=1, finite n<10 exact Real.log inequality closed in Lean, genuine original mixed and new diagonal von-Mangoldt contribution zero, pole+Gamma unchanged.",
        "source_sha256":{str(p):sha(p) for p in [LEAN]+DEPS},
        "compiled_olean_sha256":sha(OLEAN),
        "upstream_true_source_anchors":UPSTREAM,
        "new_proved_Lean_declarations":NEW,
        "axioms":axioms,
        "concrete_finite_log_gap_proved_inside_Lean":True,
        "concrete_nonzero_complex_Schwartz_bump_created":True,
        "original_mixed_vonMangoldt_prime_term_zero":True,
        "original_new_diagonal_vonMangoldt_prime_term_zero":True,
        "new_diagonal_pole_Gamma_remainder_sign_established":False,
        "new_support_schur_determinant_established":False,
        "global_Weil_positivity_established":False,
        "RH_established":False,
    }
    OUT.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print("IV016 REAL ORIGINAL LEAN KERNEL PASS: 10 standard-axiom proof declarations + 4 true source anchors; concrete log gap and literal mixed+diagonal prime zero. New diagonal SIGN NOT established.")

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight":
        source_preflight()
    else:
        kernel_verify()
