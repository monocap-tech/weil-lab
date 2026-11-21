#!/usr/bin/env python3
"""CP013 ACTUAL original external v4.35 Lean source-only RS split audit.

Only accepts compiled 1,747,950 RS-only and reassembled 52+RS
.olean/standard-axiom receipts, NOT a numeric first RS source-row
index attachment, NOT a proved N(149.5)=52, NOT new narrow zero signs.
"""
import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
SOURCES=[BASE/"CP013RSOnly.lean",BASE/"CP013Seam.lean"]
OLEANS=[
    BASE/".lake/build/lib/lean/CP013RSOnly.olean",
    BASE/".lake/build/lib/lean/CP013Seam.olean",
]
LOG=BASE/"cp013-original-RS-only-axioms.log"
OUTPUT=BASE/"cp013-original-RS-only-kernel-receipt.json"
UPSTREAM_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
ALLOWED={"propext","Classical.choice","Quot.sound"}
TARGETS=[
    "CP013RSOnly.all_original_RS_only",
    "CP013Seam.allOriginalSplit",
    "CP013Seam.rsOnlyLength",
    "CP013Seam.eulerOnlyLength",
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    needed=SOURCES+OLEANS+[LOG, BASE/"lean-toolchain"]
    if not all(path.is_file() for path in needed):
        raise SystemExit("NOT_READY: actual separate original full v4.35 RS-only/Seam oleans and axiom outputs required")
    if (BASE/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
        raise SystemExit("NOT_READY: original Zeta external toolchain changed")
    for src in SOURCES:
        body=src.read_text("utf-8")
        if re.search(r"(?m)^\s*(sorry|axiom)\b",body):
            raise SystemExit(f"NOT_READY: prohibited original source declaration/admission {src}")
    rs, seam=(x.read_text("utf-8") for x in SOURCES)
    if "theorem all_original_RS_only : BatchSpec 1747950 149500 1000 1000449286 1000 :=" not in rs:
        raise SystemExit("NOT_READY: RS-only source theorem has wrong length/boundaries")
    if "BatchSpec.append first52Euler allRS rfl rfl rfl" not in seam:
        raise SystemExit("NOT_READY: no literal original Euler/RS seam")
    log=LOG.read_text("utf-8")
    if "sorryAx" in log or "error:" in log:
        raise SystemExit("NOT_READY: genuine Lean compiler failure or sorry axiom in logs")
    reports={}
    for target in TARGETS:
        pattern=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        matches=pattern.findall(log)
        if len(matches)!=1:
            raise SystemExit(f"NOT_READY: no actual single standard-axiom receipt {target}")
        axioms={a.strip() for a in matches[0].split(",") if a.strip()}
        if not axioms<=ALLOWED:
            raise SystemExit(f"NOT_READY: unapproved original Lean axioms for {target}: {sorted(axioms-ALLOWED)}")
        reports[target]=sorted(axioms)
    output={
        "status":"CP013_ORIGINAL_1747950_RS_ONLY_AND_52_EULER_SPLIT_KERNEL_PASS",
        "scope":"Original source separate certified batches with count and endpoints ONLY",
        "original_upstream_commit":UPSTREAM_COMMIT,
        "original_lean_toolchain":"v4.35.0",
        "original_first_euler_count":52,
        "original_RS_count":1747950,
        "original_full_count":1748002,
        "original_method_seam":"149500/1000",
        "source_sha256":{p.name:sha(p) for p in SOURCES},
        "actual_olean_sha256":{p.name:sha(p) for p in OLEANS},
        "real_axiom_log_sha256":sha(LOG),
        "actual_standard_axioms":reports,
        "numerical_original_index53_row_binding_proved":False,
        "N_at_seam_149500_div1000_kernel_proved":False,
        "CP008_CP010_refined_root_signs_proved":False,
        "original_Weil_spectral_dictionary_proved":False,
    }
    OUTPUT.write_text(json.dumps(output,indent=2)+"\n","utf-8")
    print(output["status"])
    print("This proves source RS-only bundle existence, not its specific indexed decimal rows.")

if __name__=="__main__":
    main()
