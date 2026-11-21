#!/usr/bin/env python3
"""CP016 fail-closed REAL original Zeta v4.35 first RS rank .olean custody.

A successful receipt certifies existence of the 53rd original source
positive-height zero by rank, not a numerical narrow Euler/RS zero
enclosure or original signed Weil form equality. Conditional attach
requires actual HardyZ StrictMonoOn and actual narrowed source zero.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
SRC=("CP016FirstRSRank","CP016MonotoneAttach")
DEPENDENCY=("CP013RSOnly","CP013Seam","CP014FiniteCut",
            "CP014ZetaCut","CP014HardyRank","CP015SourceWitnesses")
OUTPUT=ROOT/"cp016-original-firstRS-ordinal53-kernel.json"
LOG=ROOT/"cp016-real-zeta-ordinal-axioms.log"
ORIGINAL_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
ALLOWED={"propext","Classical.choice","Quot.sound"}
TARGETS=(
    "CP016FirstRSRank.exists_least_original_RS_witness",
    "CP016FirstRSRank.original_roots_below_least_RS_are_exactly_Euler",
    "CP016FirstRSRank.N_at_original_least_RS_root_eq_52",
    "CP016FirstRSRank.original_53rd_positive_zeta_zero_exists",
    "CP016FirstRSRank.original_first_RS_zero_has_no_preceding_zero",
    "CP016FirstRSRank.original_least_RS_root_unique",
    "CP016MonotoneAttach.refined_critical_root_is_RS_source_witness",
    "CP016MonotoneAttach.refined_root_equals_original_53rd_of_hardy_monotone",
)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    sources={m:ROOT/(m+".lean") for m in SRC}
    oleans={m:ROOT/".lake/build/lib/lean"/(m+".olean") for m in SRC+DEPENDENCY}
    required=[*sources.values(),*oleans.values(),LOG,ROOT/"lean-toolchain"]
    absent=[str(p) for p in required if not p.is_file()]
    if absent:
        raise SystemExit("NOT_READY: genuine original external Zeta4.35 compiler outputs missing: "+repr(absent))
    if (ROOT/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
        raise SystemExit("NOT_READY: actual toolchain is not original Lean v4.35")
    for m,s in sources.items():
        body=s.read_text("utf-8")
        if re.search(r"(?m)^\s*(axiom|sorry)\b",body):
            raise SystemExit("NOT_READY: forbidden new axiom/sorry in "+m)
    rank=sources["CP016FirstRSRank"].read_text("utf-8")
    attach=sources["CP016MonotoneAttach"].read_text("utf-8")
    if ("riemannZeta.N z.im = 52" not in rank or
        "original_53rd_positive_zeta_zero_exists" not in rank):
        raise SystemExit("NOT_READY: original source ordinal 53 theorem missing")
    if ("(hmono : StrictMonoOn Zeta.hardyZ" not in attach or
        "refined_root_equals_original_53rd_of_hardy_monotone" not in attach):
        raise SystemExit("NOT_READY: strictly conditional analytic root identification missing")
    log=LOG.read_text("utf-8")
    if "sorryAx" in log or "error:" in log or "unsolved goals" in log:
        raise SystemExit("NOT_READY: actual Lean source compiler error or admission")
    per={}
    for name in TARGETS:
        rx=re.compile(re.escape("'"+name+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        matches=rx.findall(log)
        if len(matches)!=1:
            raise SystemExit("NOT_READY: missing/nonunique actual #print axioms "+name)
        deps={a.strip() for a in matches[0].split(",") if a.strip()}
        if not deps<=ALLOWED:
            raise SystemExit("NOT_READY: nonstandard original Lean axioms "+name+": "+repr(deps-ALLOWED))
        per[name]=sorted(deps)
    result={
        "status":"CP016_ORIGINAL_SOURCE_53RD_POSITIVE_ZERO_ORDINAL_KERNEL_PASS",
        "scope":"Source-defined least RS zero has N(γ)=52, with no intervening zero above 149.5. Conditional Hardy Z refined root attach; NOT a certified numeric value for γ.",
        "pinned_upstream_original_Zeta_commit":ORIGINAL_COMMIT,
        "original_Lean_toolchain":"leanprover/lean4:v4.35.0",
        "actual_new_source_sha256":{m:sha(p) for m,p in sources.items()},
        "actual_compiled_new_olean_sha256":{m:sha(oleans[m]) for m in SRC},
        "actual_compiled_dependencies_sha256":{m:sha(oleans[m]) for m in DEPENDENCY},
        "actual_axiom_log_sha256":sha(LOG),
        "actual_standard_axioms":per,
        "first_source_RS_positive_zero_ordinal":53,
        "numerically_identified_root_150_05352042":False,
        "proved_original_first_RS_row_right_endpoint":False,
        "uniform_original_HardyZ_derivative_positivity":False,
        "original_spectral_Weil_3x3_dictionary":False,
        "global_Weil_positivity_or_RH":False
    }
    OUTPUT.write_text(json.dumps(result,indent=2)+"\n","utf-8")
    print(result["status"])
    print("IMPORTANT: source-rank proof is NOT a narrow numerical zero enclosure.")
if __name__=="__main__":
    main()
