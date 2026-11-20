#!/usr/bin/env python3
"""IV010 strict ORIGINAL mixed zeta one-new-support extension audit.

Only a real Lean build and strict standard-axiom inspection may promote
the nine new proof candidates. Original cross-support zeta estimates
remain HYPOTHESES: this stage establishes the precise analytic gate,
not positivity on any newly enlarged support.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.olean")
LOG = Path("iv010-original-cross-support-axioms.log")
OUT = Path("iv010-original-cross-support-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralNF740HermitianTwoBlockPSD",
    "neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal",
    "neutralIV008OriginalMixedEntry_hermitian",
    "neutralIV007OriginalMixedEnergy_natural",
]
NEW = [
    "neutralIV010TwoTests_supported",
    "neutralIV010TwoTests_physicalSum",
    "neutralIV010TwoSource_literalBlock",
    "neutralIV010Mixed_hermitian",
    "neutralIV010Diagonal_im_zero",
    "neutralIV010OldPlusNew_exactBlock",
    "neutralIV010OldPlusNew_realBlock",
    "neutralIV010HermitianTwoBlock_nonnegative",
    "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
]
NAMES = UPSTREAM + NEW
SOURCE_DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVHermitianTwoBlockPSD.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormulaAutomatic.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaWeilZeroForm.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarCoercivity.lean"),
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def preflight() -> None:
    raw = LEAN.read_text()
    tokens = (
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization",
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVHermitianTwoBlockPSD",
        "Zeta23.EF.literatureRHS",
        "neutralIV009PhysicalSchwartzSum",
        "neutralIV007OriginalMixedEnergy a s u",
        "neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal",
        "neutralIV007OriginalMixedEnergy_natural",
        "neutralIV008OriginalMixedEntry_hermitian",
        "neutralNF740HermitianTwoBlockPSD",
        "neutralIV010OldPlusNew_exactBlock",
        "neutralIV010OldPlusNew_realBlock",
        "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
    )
    for token in tokens:
        assert token in raw, f"Missing exact source token: {token}"
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", raw, re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b", raw)
    assertions = re.findall(r"^#print axioms (\w+)$", raw, re.M)
    assert assertions == NAMES, (assertions, NAMES)
    theorems = re.findall(r"^theorem (neutralIV010\w+)", raw, re.M)
    assert theorems == NEW, (theorems, NEW)
    for p in SOURCE_DEPS:
        assert p.is_file(), p
    print("IV010 source preflight PASS: original cross-support mixed block/cross-bound gates and nine proposed theorems. KERNEL VERIFICATION PENDING, NO NEW ZETA CROSS BOUND.")

def verify() -> None:
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, "Actual compiled Lean olean missing"
    log = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        log, re.I,
    ), "Lean error or sorryAx forbidden"
    found = {}
    for name in NAMES:
        key = "'WeilDefect." + name + "'"
        matches = re.findall(re.escape(key) + r" depends on axioms: \[([^\]]*)\]", log, re.S)
        none = re.findall(re.escape(key) + r" does not depend on any axioms", log, re.S)
        assert len(matches) + len(none) == 1, (name, len(matches), len(none))
        axioms = [] if none else [v.strip() for v in matches[0].split(",") if v.strip()]
        assert set(axioms) <= ALLOWED, (name, axioms)
        found[name] = axioms
    receipt = {
        "schema": "IV010-original-cross-support-Schur-mixed-block-kernel-v1",
        "scope": "Exact old mixed-block transport + one newly admitted physical Schwartz test literal EF cross row/column; sharp complex mixed determinant bound implies one-site nonnegativity as a CONDITIONAL theorem.",
        "source_sha256": {str(p): digest(p) for p in [LEAN] + SOURCE_DEPS},
        "compiled_olean_sha256": digest(OLEAN),
        "upstream_source_anchors": UPSTREAM,
        "new_iv010_theorems": NEW,
        "axioms": found,
        "new_cross_support_zeta_estimate_established": False,
        "positivity_on_new_support_established": False,
        "global_Weil_positivity_established": False,
        "RH_established": False,
    }
    OUT.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("IV010 exact original mixed-cross SUPPORT GATE: 9 NEW LEAN KERNEL PASS, 4 authentic upstream anchors. New zeta cross estimate remains OPEN; no global PSD or RH.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("preflight", "verify"))
    args = p.parse_args()
    if args.stage == "preflight":
        preflight()
    else:
        verify()
