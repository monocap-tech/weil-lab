#!/usr/bin/env python3
"""CP011 fail-closed original Zeta v4.35 true canonical roster theorem audit.

A cheap script checking a Lean source declaration is NOT a Lean proof. This
audit requires the actual compiled .olean and live #print axioms receipt
after the full original external pinned source package was fetched/built.
It does not accept a proof for new Euler/RS bracket existence or signed Weil.
"""
import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
LEAN=BASE/"CP011CanonicalRoster.lean"
OLEAN=BASE/".lake/build/lib/lean/CP011CanonicalRoster.olean"
LOG=BASE/"cp011-actual-axioms.log"
RECEIPT=BASE/"cp011-canonical-source-roster-kernel.json"
TARGETS=(
    "CP011CanonicalRoster.every_positive_zero_is_original_witness",
    "CP011CanonicalRoster.unique_zero_in_original_slot",
    "CP011CanonicalRoster.refined_root_identifies_original_slot",
    "CP011CanonicalRoster.pinned_external_positive_root_is_member"
)
ALLOWED={"propext","Classical.choice","Quot.sound"}
COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    required=(LEAN,OLEAN,LOG,BASE/"lean-toolchain")
    if not all(p.is_file() for p in required):
        raise SystemExit("NOT_READY: actual source/compiled .olean/real axiom log/toolchain missing")
    if (BASE/"lean-toolchain").read_text().strip()!="leanprover/lean4:v4.35.0":
        raise SystemExit("NOT_READY: wrong Lean toolchain")
    source=LEAN.read_text("utf-8")
    log=LOG.read_text("utf-8")
    if re.search(r"\bsorry\b",source) or "sorryAx" in log or "error:" in log:
        raise SystemExit("NOT_READY: no admitted axioms or Lean compile errors accepted")
    result={}
    for target in TARGETS:
        rx=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        matches=rx.findall(log)
        if len(matches)!=1:
            raise SystemExit(f"NOT_READY: missing/duplicate true Lean axiom line for {target}")
        axioms={a.strip() for a in matches[0].split(",") if a.strip()}
        if not axioms<=ALLOWED:
            raise SystemExit(f"NOT_READY: nonstandard axioms {sorted(axioms-ALLOWED)} for {target}")
        result[target]=sorted(axioms)
    receipt={
        "status":"CP011_ORIGINAL_COUNT_EXHAUSTIVENESS_AND_SLOT_UNIQUENESS_LEAN_PASS_ONLY",
        "scope":"Positive zeros below original certified Gram point; exact original per-slot uniqueness; NOT NEW Euler/RS sign proofs, original zero shard rows or signed Weil",
        "external_source_commit":COMMIT,
        "lean_toolchain":"leanprover/lean4:v4.35.0",
        "compiled_source_sha256":sha256(LEAN),
        "actual_compiled_olean_sha256":sha256(OLEAN),
        "actual_lean_axiom_log_sha256":sha256(LOG),
        "per_decl_axioms":result
    }
    RECEIPT.write_text(json.dumps(receipt,indent=2)+"\n","utf-8")
    print(receipt["status"])

if __name__=="__main__":
    main()
