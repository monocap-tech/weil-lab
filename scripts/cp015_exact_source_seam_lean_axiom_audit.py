#!/usr/bin/env python3
"""CP015 source-WITNESS FULL 149.5 exact cut genuine external Lean kernel gate.

Only actual compilation of original upstream v4.35 Zeta plus CP013 RS-only
and CP014 finite card/simplicity dependencies may justify promoting the
NEW unconditional N(149.5)=52 theorem; no fabricated Lean proof receipts.

This gate does not certify root53's refined ordinate or original signed
Weil/zero-side equivalence.  Numerical source SHA checks are separate.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
SOURCE=BASE/"CP015SourceWitnesses.lean"
OLEAN=BASE/".lake/build/lib/lean/CP015SourceWitnesses.olean"
LOG=BASE/"cp015-original-1495-source-actual-axioms.log"
RECEIPT=BASE/"cp015-1495-unconditional-lean-receipt.json"
PREREQ=(
    BASE/".lake/build/lib/lean/CP013RSOnly.olean",
    BASE/".lake/build/lib/lean/CP013Seam.olean",
    BASE/".lake/build/lib/lean/CP014FiniteCut.olean",
    BASE/".lake/build/lib/lean/CP014ZetaCut.olean",
)
REQUIRED=(
    "CP015SourceWitnesses.eulerRoots_card",
    "CP015SourceWitnesses.rsRoots_card",
    "CP015SourceWitnesses.rsRoots_above",
    "CP015SourceWitnesses.eulerRoots_subset",
    "CP015SourceWitnesses.rsRoots_subset",
    "CP015SourceWitnesses.euler_rs_disjoint",
    "CP015SourceWitnesses.original_complete_positive_roster_is_euler_union_rs",
    "CP015SourceWitnesses.no_original_zero_exactly_at_149500_div1000",
    "CP015SourceWitnesses.original_N_at_149500_div1000_eq_52",
)
ALLOWED={"propext","Classical.choice","Quot.sound"}
COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    required=(SOURCE,OLEAN,LOG,BASE/"lean-toolchain",*PREREQ)
    missing=[str(x) for x in required if not x.is_file()]
    if missing:
        raise SystemExit(f"NOT_READY: Genuine compiled original CP013, CP014, CP015 .olean or axioms missing: {missing}")
    if (BASE/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
        raise SystemExit("NOT_READY: external Zeta toolchain must be exactly original 4.35")
    source=SOURCE.read_text("utf-8")
    actual=source.split("@[expose] public section")[-1]
    if re.search(r"(?m)^\s*(axiom|sorry)\b",actual):
        raise SystemExit("NOT_READY: new Lean source includes an admitted axiom or sorry")
    if "theorem original_N_at_149500_div1000_eq_52 :" not in source:
        raise SystemExit("NOT_READY: missing unconditional 149.5 source cut declaration")
    if "N_at_Euler_RS_seam_eq_52_of_source_witnesses" not in source:
        raise SystemExit("NOT_READY: source-root witness discharge no longer occurs")
    log=LOG.read_text("utf-8")
    if "sorryAx" in log or "error:" in log or "unsolved goals" in log:
        raise SystemExit("NOT_READY: compiler error or hidden sorry axiom in genuine Lean output")
    axioms={}
    for target in REQUIRED:
        pattern=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        found=pattern.findall(log)
        if len(found)!=1:
            raise SystemExit(f"NOT_READY: missing/duplicate actual #print axioms output: {target}")
        deps={x.strip() for x in found[0].split(",") if x.strip()}
        if not deps<=ALLOWED:
            raise SystemExit(f"NOT_READY: nonstandard axioms in {target}: {sorted(deps-ALLOWED)}")
        axioms[target]=sorted(deps)
    result={
        "status":"CP015_ORIGINAL_ZETA_UNCONDITIONAL_N_1495_EQ_52_KERNEL_PASS",
        "scope":"Original first52 Euler / 1747950 RS source-root saturation, NO zero at exact 149.5 seam, N(149.5)=52; NOT original ordinal53 numeric enclosure or global RH",
        "external_pinned_upstream_commit":COMMIT,
        "real_upstream_Lean":"leanprover/lean4:v4.35.0",
        "source_sha256":sha(SOURCE),
        "actual_olean_sha256":sha(OLEAN),
        "actual_log_sha256":sha(LOG),
        "imported_certified_olean_sha256":{x.name:sha(x) for x in PREREQ},
        "actual_axioms":axioms,
        "unconditional_N_1495_eq_52_if_this_receipt_exists":True,
        "local_N_15005353_eq_53_proved":False,
        "no_original_zero_at_1495_Lean_proved_if_receipt_exists":True,
        "root53_Euler_sign_proof_accepted":False,
        "original_batch_index53_decimal_endpoints_proved":False,
        "global_Weil_positivity_or_RH":False,
    }
    RECEIPT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(result["status"])
    print("Root53 rank/narrow sign and Weil zero-side dictionary are still NOT proved.")


if __name__=="__main__":
    main()
