#!/usr/bin/env python3
"""CP017 genuine external Zeta 4.35 original Hardy-Z rational budget kernel audit.

Only real compiled .olean of CP017 and all imported CP013-016 source
candidate dependencies plus SIX actual #print axioms standard-only
receipts may emit a kernel PASS. Even then the analytical hypotheses
(derivative anchor, uniform curvature and new zero existence)
remain UNPROVED.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
SOURCE=BASE/"CP017CurvatureBudget.lean"
OLEAN=BASE/".lake/build/lib/lean/CP017CurvatureBudget.olean"
DEPENDENCIES=(
  "CP013RSOnly","CP013Seam","CP014FiniteCut","CP014ZetaCut",
  "CP014HardyRank","CP015SourceWitnesses",
  "CP016FirstRSRank","CP016MonotoneAttach"
)
LOG=BASE/"cp017-real-source-curvature-axioms.log"
RECEIPT=BASE/"cp017-conditional-original-hardyZ-curvature-kernel-receipt.json"
UPSTREAM_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
ALLOWED={"propext","Classical.choice","Quot.sound"}
TARGETS=(
  "CP017CurvatureBudget.exact_positive_derivative_margin",
  "CP017CurvatureBudget.uniform_derivative_margin_of_rational_budget",
  "CP017CurvatureBudget.strictMonoOn_original_hardyZ_of_rational_budget",
  "CP017CurvatureBudget.derivative_variation_of_curvature_bound",
  "CP017CurvatureBudget.strictMonoOn_original_hardyZ_of_curvature_bound",
  "CP017CurvatureBudget.refined_narrow_root_is_source_53rd_of_rational_budget",
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    deps={name:BASE/".lake/build/lib/lean"/(name+".olean")
          for name in DEPENDENCIES}
    paths=[SOURCE,OLEAN,LOG,BASE/"lean-toolchain",*deps.values()]
    absent=[str(p) for p in paths if not p.is_file()]
    if absent:
        raise SystemExit("NOT_READY: genuine external Zeta v4.35 Lean .olean and #print axioms missing: "+repr(absent))
    if (BASE/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
        raise SystemExit("NOT_READY: Zeta toolchain does not match pinned v4.35")
    body=SOURCE.read_text("utf-8")
    if re.search(r"(?m)^\s*(sorry|axiom)\b",body):
        raise SystemExit("NOT_READY: source includes actual axiom or sorry declaration")
    for t in [
      "12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a",
      "|deriv Zeta.hardyZ t - deriv Zeta.hardyZ a|",
      "∀ t ∈ Ico a b",
      "StrictMonoOn Zeta.hardyZ (Icc a b)",
      "norm_image_sub_le_of_norm_deriv_le_segment",
      "(hzero : riemannZeta",
    ]:
        if t not in body:
            raise SystemExit("NOT_READY: explicit UNPROVED analytic assumption missing: "+t)
    log=LOG.read_text("utf-8")
    if "sorryAx" in log or "error:" in log or "unsolved goals" in log:
        raise SystemExit("NOT_READY: original Lean compiler failure/admitted source")
    axioms={}
    for target in TARGETS:
        pat=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        res=pat.findall(log)
        if len(res)!=1:
            raise SystemExit("NOT_READY: missing/ambiguous REAL Lean #print axioms: "+target)
        depset={a.strip() for a in res[0].split(",") if a.strip()}
        if not depset<=ALLOWED:
            raise SystemExit("NOT_READY: disallowed axiom in "+target+": "+repr(depset-ALLOWED))
        axioms[target]=sorted(depset)
    receipt={
      "status":"CP017_ORIGINAL_HARDYZ_RATIONAL_CURVATURE_CONDITIONAL_KERNEL_PASS_ONLY",
      "interpretation":"Lean kernel verifies 12/5 anchor PLUS uniform curvature4 imply strict HardyZ mono and conditional source rank53 numerical identification.",
      "original_zeta_commit":UPSTREAM_COMMIT,
      "toolchain":"leanprover/lean4:v4.35.0",
      "actual_new_source_sha256":sha(SOURCE),
      "actual_new_olean_sha256":sha(OLEAN),
      "imported_actual_dependency_oleans_sha256":{n:sha(p) for n,p in deps.items()},
      "actual_standard_axioms":axioms,
      "actual_axiom_log_sha256":sha(LOG),
      "positive_derivative_margin":"4647/25000",
      "actual_derivative_anchor_12_div5_proved":False,
      "actual_uniform_hardyZ_curvature_le4_proved":False,
      "actually_certified_zero_in_narrow_bracket":False,
      "original_numeric_first_RS_root_identified":False,
      "original_signed_Weil_to_zero_spectral_equality":False,
      "RH_or_global_Weil_positivity":False
    }
    RECEIPT.write_text(json.dumps(receipt,indent=2)+"\n","utf-8")
    print(receipt["status"])
    print("Conditional original rank53 bridge only: NONE of its three independent analytic inputs is certified.")

if __name__=="__main__":
    main()
