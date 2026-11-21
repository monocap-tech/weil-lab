#!/usr/bin/env python3
"""IV009 — strict ORIGINAL zeta full-divisor Schwartz polarization audit.

A preflight is source inspection only. The authentic IV009 Lean source must
compile directly and produce a real .olean before any theorem is counted.
Every new theorem and upstream arithmetic / collar anchor must carry only
standard kernel axioms and an immutable source-bound audit record.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.olean")
LOG = Path("iv009-original-schwartz-polarization-axioms.log")
OUT = Path("iv009-original-schwartz-polarization-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralWindowEvaluation_eq_inner",
    "neutralActualZetaDivisor_rawTransform_summable_of_contDiff",
    "neutralIV008OriginalMixedEntry_eq_divisor",
    "neutralNF738OriginalFiniteCollarSpan_coercive",
]
NEW = [
    "neutralIV009PhysicalSchwartzSum_supported",
    "neutralIV009WindowEvaluation_finiteLinear",
    "neutralIV009OriginalPairTerm_summable",
    "neutralIV009OriginalDivisorTerm_finiteExpansion",
    "neutralIV009FiniteMixedEnergy_eq_originalDivisorDiagonal",
    "neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal",
    "neutralIV009OriginalCollars_supported_window",
    "neutralIV009OriginalCollars_mixedEnergy_lower",
]
NAMES = UPSTREAM + NEW
DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteLocalSpan.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarCoercivity.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaRawGreenSampling.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormulaAutomatic.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean"),
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def preflight() -> None:
    raw = LEAN.read_text()
    checks = (
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalMixedHermitian",
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVFiniteLocalSpan",
        "neutralWindowEvaluation_eq_inner",
        "SchwartzMap.toLpCLM",
        "neutralActualZetaDivisor_rawTransform_summable_of_contDiff",
        "neutralIV008OriginalMixedEntry_eq_divisor",
        "neutralIV009OriginalPairTerm",
        "neutralIV009WeightedPairTerm",
        "neutralIV009PhysicalSchwartzSum",
        "neutralIV009FiniteMixedEnergy_eq_originalDivisorDiagonal",
        "Summable.tsum_finsetSum",
        "Zeta23.EF.literatureRHS",
        "neutralNF738OriginalFiniteCollarSpan_coercive",
        "(2/5:ℝ)",
    )
    for w in checks:
        assert w in raw, f"Missing source marker {w}"
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", raw, re.M), "Untrusted declarations prohibited"
    assert not re.search(r"\b(?:sorry|sorryAx)\b", raw), "Untrusted proof marker prohibited"
    prints = re.findall(r"^#print axioms (\w+)$", raw, re.M)
    assert prints == NAMES, (prints, NAMES)
    declarations = re.findall(r"^theorem (neutralIV009\w+)", raw, re.M)
    assert declarations == NEW, (declarations, NEW)
    for dep in DEPS:
        assert dep.is_file(), dep
    print("IV009 source preflight PASS: eight new original mixed/divisor/polarization/local-collar proof candidates and four genuine upstream receipts. LEAN KERNEL PENDING.")

def verify() -> None:
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, "Actual compiled Lean object missing"
    raw = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        raw, re.I,
    ), "Lean compiler error, untrusted declaration or sorryAx"
    found = {}
    for name in NAMES:
        key = "'WeilDefect." + name + "'"
        matches = re.findall(re.escape(key) + r" depends on axioms: \[([^\]]*)\]", raw, re.S)
        none = re.findall(re.escape(key) + r" does not depend on any axioms", raw, re.S)
        assert len(matches) + len(none) == 1, (name, len(matches), len(none))
        axioms = [] if none else [x.strip() for x in matches[0].split(",") if x.strip()]
        assert set(axioms) <= ALLOWED, (name, axioms)
        found[name] = axioms
    receipt = {
        "schema": "IV009-original-schwartz-finite-sum-polarization-kernel-v1",
        "scope": "Authentic Schwartz finite mixed-to-diagonal zeta EF via all-multiplicity divisor summability, plus exact frozen-collar 2/5 mixed Gram coercivity.",
        "source_sha256": {str(f): digest(f) for f in [LEAN] + DEPS},
        "compiled_olean_sha256": digest(OLEAN),
        "upstream_source_anchors": UPSTREAM,
        "new_iv009_theorems": NEW,
        "axioms": found,
        "arbitrary_new_support_positivity_proved": False,
        "universal_complex_schwartz_positivity_proved": False,
        "global_Weil_positivity_proved": False,
        "RH_proved": False,
    }
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("IV009 SOURCE-SPECIFIC KERNEL PASS: 8 new full-divisor Schwartz polarization/local original-collar theorems, 4 upstream receipts, strictly standard Lean axioms. NO GLOBAL POSITIVITY.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("preflight", "verify"))
    args = p.parse_args()
    if args.stage == "preflight":
        preflight()
    else:
        verify()
