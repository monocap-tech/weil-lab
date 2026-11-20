#!/usr/bin/env python3
"""IV008 strict source-bound ORIGINAL mixed zeta Weil Hermitian audit.

Checks genuine full divisor conjugation + the literal NF533 EF attachment,
not an abstract Hermitian placeholder. Preflight NEVER means Lean accepted.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.olean")
LOG = Path("iv008-original-mixed-hermitian-axioms.log")
OUT = Path("iv008-original-mixed-hermitian-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond",
    "neutralActualZetaDivisorPairEquiv",
    "neutralIV007OriginalMixedEntry_natural",
]
NEW = [
    "neutralIV008SchwartzWindow_hasCompactSupport",
    "neutralIV008OriginalMixedEntry_eq_divisor",
    "neutralIV008OriginalDivisorEntry_hermitian",
    "neutralIV008OriginalMixedEntry_hermitian",
    "neutralIV008OriginalMixedDiagonal_im_zero",
    "neutralIV008OriginalMixedEnergy_im_zero",
    "neutralIV008OriginalMixedEnergy_eq_re",
]
NAMES = UPSTREAM + NEW
SOURCE_DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaSmoothCorrelationRegularity.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormulaAutomatic.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaWeilZeroForm.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean"),
]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def preflight() -> None:
    raw = LEAN.read_text()
    for required in (
        "import WeilDefect.Arithmetic.ActualZetaPhaseIVFiniteMixedWindowSystem",
        "import WeilDefect.Arithmetic.ActualZetaWeilZeroForm",
        "neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond",
        "neutralActualZetaDivisorPairEquiv.tsum_eq",
        "neutralActualZetaDivisorOrdinate_pair",
        "neutralIV007OriginalDivisorEntry",
        "neutralIV007OriginalMixedEntry",
        "neutralIV007OriginalMixedEnergy",
        "Complex.conj_tsum",
    ):
        assert required in raw, required
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", raw, re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b", raw)
    prints = re.findall(r"^#print axioms (\w+)$", raw, re.M)
    assert prints == NAMES, (prints, NAMES)
    defs = re.findall(r"^theorem (neutralIV008\w+)", raw, re.M)
    assert defs == NEW, (defs, NEW)
    for p in SOURCE_DEPS:
        assert p.is_file(), p
    print("IV008 preflight PASS: exact original mixed zeta Weil source and seven new Hermitian/real-axis proof candidates; Lean kernel pending.")

def verify() -> None:
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, "Compiled original IV008 olean missing"
    raw = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        raw, re.I,
    ), "Kernel error or untrusted proof forbidden"
    found = {}
    for name in NAMES:
        key = "'WeilDefect." + name + "'"
        parts = re.findall(re.escape(key) + r" depends on axioms: \[([^\]]*)\]", raw, re.S)
        none = re.findall(re.escape(key) + r" does not depend on any axioms", raw, re.S)
        assert len(parts) + len(none) == 1, (name, len(parts), len(none))
        axioms = [] if none else [x.strip() for x in parts[0].split(",") if x.strip()]
        assert set(axioms) <= ALLOWED, (name, axioms)
        found[name] = axioms
    out = {
        "schema": "IV008-original-mixed-zeta-hermitian-source-bound-v1",
        "scope": "Hermitian original mixed EF from all-multiplicity divisor involution, with real finite complex coefficient energies on fixed supported Schwartz families.",
        "source_sha256": {str(p): sha256(p) for p in [LEAN] + SOURCE_DEPS},
        "compiled_olean_sha256": sha256(OLEAN),
        "upstream_source_anchors": UPSTREAM,
        "new_iv008_theorems": NEW,
        "axioms": found,
        "original_mixed_signed_hermitian_attached": True,
        "physical_sum_polarization_proved": False,
        "new_support_positivity_proved": False,
        "global_Weil_positivity_proved": False,
        "RH_proved": False,
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("IV008 original mixed Weil Hermitian/real finite energy: 7 source-specific LEAN KERNEL PASS with standard axiom custody. NO positivity/polarization claim.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("preflight", "verify"))
    args = p.parse_args()
    if args.stage == "preflight":
        preflight()
    else:
        verify()
