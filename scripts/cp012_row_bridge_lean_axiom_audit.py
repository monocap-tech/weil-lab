#!/usr/bin/env python3
"""CP012: fail-closed actual original Zeta 4.35 CONDITIONAL row bridge audit.

Even a real kernel PASS here proves only
  IndexedSlotContains Z k a b -> refined_zero_matches_original_slot
It does NOT prove IndexedSlotContains for source zero #53 or any of the
1,748,002 original rows. That remains an independent REQUIRED theorem.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
SOURCE=ROOT/"CP012RowReceipt.lean"
OLEAN=ROOT/".lake/build/lib/lean/CP012RowReceipt.olean"
LOG=ROOT/"cp012-row-receipt-axioms.log"
OUTPUT=ROOT/"cp012-conditional-row-bridge-kernel-receipt.json"
TARGETS=(
  "CP012RowReceipt.ExactSourceRowAt.implies_containment",
  "CP012RowReceipt.refined_root_equals_canonical_at_index",
  "CP012RowReceipt.refined_root_of_exact_source_row",
)
ALLOWED={"propext","Classical.choice","Quot.sound"}
UPSTREAM_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    required=(SOURCE,OLEAN,LOG,ROOT/"lean-toolchain",
              ROOT/".lake/build/lib/lean/CP011CanonicalRoster.olean")
    if not all(x.is_file() for x in required):
        raise SystemExit("NOT_READY: original CP011 and new CP012 compiled real .olean plus actual axiom logs required")
    if (ROOT/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
        raise SystemExit("NOT_READY: original upstream toolchain drift")
    source=SOURCE.read_text("utf-8")
    if re.search(r"\bsorry\b",source) or re.search(r"(?m)^\s*axiom\s+", source):
        raise SystemExit("NOT_READY: source contains sorry or new axiom declaration")
    if "structure IndexedSlotContains" not in source:
        raise SystemExit("NOT_READY: missing explicit indexed source containment premise")
    if "(hslot : IndexedSlotContains Z k a b)" not in source:
        raise SystemExit("NOT_READY: theorem missing its unproved source-index receipt parameter")
    log=LOG.read_text("utf-8")
    if "sorryAx" in log or "error:" in log:
        raise SystemExit("NOT_READY: failed original Lean or sorry axiom in compiler output")
    found={}
    for target in TARGETS:
        pattern=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        hits=pattern.findall(log)
        if len(hits)!=1:
            raise SystemExit(f"NOT_READY: no genuine unique Lean #print axioms output for {target}")
        deps={x.strip() for x in hits[0].split(",") if x.strip()}
        if not deps<=ALLOWED:
            raise SystemExit(f"NOT_READY: nonstandard axioms for {target}: {deps-ALLOWED}")
        found[target]=sorted(deps)
    receipt={
        "status":"CP012_CONDITIONAL_INDEXED_SLOT_BRIDGE_ONLY",
        "source_commit":UPSTREAM_COMMIT,
        "lean_version":"v4.35.0",
        "source_sha256":sha(SOURCE),
        "actual_olean_sha256":sha(OLEAN),
        "actual_CP011_dependency_olean_sha256":sha(
            ROOT/".lake/build/lib/lean/CP011CanonicalRoster.olean"),
        "actual_axiom_log_sha256":sha(LOG),
        "per_target_axioms":found,
        "unproved_hypothesis":
            "IndexedSlotContains certifiedZeroCount (Fin 52 ...) a b",
        "full_zero_53_row_attached":False,
        "new_refined_numerical_root_kernel_signs":False,
        "original_Weil_to_full_spectral_dictionary":False,
        "rh_or_global_Weil_positivity":False
    }
    OUTPUT.write_text(json.dumps(receipt,indent=2)+"\n","utf-8")
    print(receipt["status"])
    print("A conditional row bridge is not a completed original source row binding.")

if __name__=="__main__":
    main()
