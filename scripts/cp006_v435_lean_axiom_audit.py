#!/usr/bin/env python3
"""Strict CP006 isolated upstream v4.35 Lean axiom/.olean witness audit.

Requires an ACTUALLY completed lake build and real #print axioms log.
Does not certify exported zero brackets or the v4.34 original Weil dictionary.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1] / "cp006_zeta_v435"
SOURCE=ROOT / "CP006ZeroBridge.lean"
OLEAN=ROOT / ".lake/build/lib/lean/CP006ZeroBridge.olean"
LOG=ROOT / "cp006-upstream-axiom-log.txt"
OUT=ROOT / "cp006-external-kernel-audit.json"
AX={"propext","Classical.choice","Quot.sound"}
TARGET=[
    "CP006ZeroBridge.certified_count_at_gram",
    "CP006ZeroBridge.certified_total_zero_count_at_gram",
    "CP006ZeroBridge.certified_finite_height_line",
    "CP006ZeroBridge.certified_finite_height_simple",
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    assert SOURCE.is_file() and OLEAN.is_file() and LOG.is_file(), "MISSING real source/olean/axiom log"
    source=SOURCE.read_text(encoding="utf-8")
    logs=LOG.read_text(encoding="utf-8")
    assert "sorryAx" not in logs and "error:" not in logs, "Lean errors or sorryAx"
    assert not re.search(r"\bsorry\b",source), "Source contains sorry"
    assertions={}
    for target in TARGET:
        rex=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        matches=rex.findall(logs)
        assert len(matches)==1, f"Require one actual Lean axiom receipt for {target}, found {len(matches)}"
        axioms={a.strip() for a in matches[0].split(",") if a.strip()}
        assert axioms<=AX, f"Forbidden axioms for {target}: {axioms-AX}"
        assertions[target]=sorted(axioms)
    receipt={
        "status":"UPSTREAM_V435_LEAN_BRIDGE_PASS_ONLY",
        "scope":"Imported Zeta finite-height theorem and exact Turing count only, NOT exported ordinate list or Weil source",
        "source_sha256":sha(SOURCE),
        "olean_sha256":sha(OLEAN),
        "axioms":assertions,
    }
    OUT.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(receipt["status"])

if __name__=="__main__":
    main()
