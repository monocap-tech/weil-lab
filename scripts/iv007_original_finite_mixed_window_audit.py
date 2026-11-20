#!/usr/bin/env python3
"""IV007 strict source-bound original mixed finite-family audit.

Source preflight is NOT kernel acceptance. The new seven IV007 theorems
must be built by Lean and audited with the three IV006 source anchors;
no positivity of the zeta Weil form is assumed or asserted.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN = Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean")
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.olean")
LOG = Path("iv007-original-finite-mixed-window-axioms.log")
OUT = Path("iv007-original-finite-mixed-window-kernel-audit.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

UPSTREAM = [
    "neutralIV006LiteralMixedEF_natural",
    "neutralIV006MixedDivisorSum_eq_of_support",
    "neutralIV006Schwartz_support_expand",
]
NEW = [
    "neutralIV007OriginalMixedEntry_natural",
    "neutralIV007OriginalDivisorEntry_natural",
    "neutralIV007OriginalMixedMatrix_natural",
    "neutralIV007OriginalMixedEnergy_natural",
    "neutralIV007OriginalMixedEnergy_re_natural",
    "neutralIV007FixedFamilyRealNonnegative_iff",
    "neutralIV007UniversalRealNonnegative_antitone",
]
NAMES = UPSTREAM + NEW

SOURCE_DEPS = [
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalRealOddSchwartzFullSource.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaSmoothCorrelationRegularity.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalSignedGraphForm.lean"),
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def preflight() -> None:
    raw = LEAN.read_text()
    assert "import WeilDefect.Arithmetic.ActualZetaPhaseIVWindowNaturality" in raw
    for witness in (
        "Zeta23.EF.literatureRHS",
        "neutralWindowCorrelation a",
        "neutralActualZetaDivisorOrdinate",
        "NeutralActualZetaDivisorCoordinate",
        "neutralIV007OriginalMixedEnergy",
        "neutralIV007UniversalRealNonnegative",
        "neutralIV006Schwartz_support_expand",
        "Finset.sum_congr",
    ):
        assert witness in raw, witness
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b", raw, re.M)
    assert not re.search(r"\b(?:sorry|sorryAx)\b", raw)
    prints = re.findall(r"^#print axioms (\w+)$", raw, re.M)
    assert prints == NAMES, (prints, NAMES)
    theorems = re.findall(r"^theorem (neutralIV007\w+)", raw, re.M)
    assert theorems == NEW, (theorems, NEW)
    for p in SOURCE_DEPS:
        assert p.is_file(), str(p)
    print("IV007 preflight PASS: seven proposed finite-family original mixed identities and three exact IV006 upstream anchors. LEAN KERNEL PENDING.")

def verify() -> None:
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size > 0, "compiled olean missing"
    raw = LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        raw,
        re.I,
    ), "Lean error/sorry forbidden"
    found = {}
    for name in NAMES:
        key = "'WeilDefect." + name + "'"
        parts = re.findall(re.escape(key) + r" depends on axioms: \[([^\]]*)\]", raw, re.S)
        none = re.findall(re.escape(key) + r" does not depend on any axioms", raw, re.S)
        assert len(parts) + len(none) == 1, (name, len(parts), len(none))
        axs = [] if none else [x.strip() for x in parts[0].split(",") if x.strip()]
        assert set(axs) <= ALLOWED, (name, axs)
        found[name] = axs
    out = {
        "schema": "IV007-original-finite-family-mixed-window-kernel-v1",
        "scope": "Exact mixed EF and divisor matrices and all finite complex mixed energies across containing windows. Fixed families only.",
        "source_sha256": {str(p): digest(p) for p in [LEAN] + SOURCE_DEPS},
        "compiled_olean_sha256": digest(OLEAN),
        "upstream_iv006_anchors": UPSTREAM,
        "new_iv007_theorems": NEW,
        "axioms": found,
        "universal_nonnegativity_established": False,
        "larger_support_nonnegativity_established": False,
        "source_graph_compatibility_established": False,
        "global_Weil_positivity_established": False,
        "RH_established": False,
    }
    OUT.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print("IV007 KERNEL PASS: seven actual finite-family mixed-window proofs and three IV006 anchors accepted with standard axioms. NO GLOBAL POSITIVITY CLAIM.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("preflight", "verify"))
    args = parser.parse_args()
    if args.stage == "preflight":
        preflight()
    else:
        verify()
