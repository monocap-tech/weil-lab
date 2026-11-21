#!/usr/bin/env python3
"""CP014 real original-Zeta-v4.35 kernel audit.

ONLY a completed genuine external-v4.35 lean build, three compiled .olean
and real standard-axioms #print receipts can upgrade source candidates.
Even successful Lean certification here leaves the original Euler/RS
witness-set coverage HYPOTHESES OPEN and N(150.05353)=53 unproved.
"""
import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
MODULES=("CP014EulerCutLower","CP014FiniteCut","CP014ZetaCut","CP014HardyRank")
DEPS=("CP013RSOnly","CP013Seam")
NAMES={
    "CP014EulerCutLower":(
        "CP014EulerCutLower.fifty_two_le_N_at_original_Euler_seam",
    ),
    "CP014FiniteCut":(
        "CP014FiniteCut.exhausted_by_two_disjoint_parts",
        "CP014FiniteCut.exact_low_partition",
        "CP014FiniteCut.original_seam_root_cardinality",
    ),
    "CP014HardyRank":(
        "CP014HardyRank.unique_critical_zero_of_hardy_strictMonoOn",
    ),
    "CP014ZetaCut":(
        "CP014ZetaCut.N_eq_card_below_original_gram",
        "CP014ZetaCut.original_full_source_finite_zero_card",
        "CP014ZetaCut.zerosUnder_cut_filter",
        "CP014ZetaCut.N_at_Euler_RS_seam_eq_52_of_source_witnesses",
    ),
}
ALLOWED={"propext","Classical.choice","Quot.sound"}
LOG=BASE/"cp014-original-seam-actual-axioms.log"
RECEIPT=BASE/"cp014-cut-count-conditional-kernel-receipt.json"
UPSTREAM_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    src={x:BASE/f"{x}.lean" for x in MODULES}
    oleans={x:BASE/f".lake/build/lib/lean/{x}.olean" for x in MODULES+DEPS}
    required=[*src.values(),*oleans.values(),LOG,BASE/"lean-toolchain"]
    if not all(x.is_file() for x in required):
        raise SystemExit("NOT_READY: original CP013 plus actual CP014 compiled four .olean and real axiom logs missing")
    if (BASE/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
        raise SystemExit("NOT_READY: original external toolchain drift")
    for m,s in src.items():
        contents=s.read_text("utf-8")
        if re.search(r"(?m)^\s*(sorry|axiom)\b",contents):
            raise SystemExit("NOT_READY: original Lean proof candidate includes axiom/admitted proof: "+m)
    cut=src["CP014ZetaCut"].read_text("utf-8")
    for text in ["(hEsub : E ⊆ zerosUnder", "(hRsub : R ⊆ zerosUnder",
                 "(hdisjoint : Disjoint E R)", "(hEbelow : ∀ z ∈ E",
                 "(hRabove : ∀ z ∈ R", "(hcut : (149500 : ℝ) / 1000 ≤"]:
        if text not in cut:
            raise SystemExit("NOT_READY: source theorem no longer declares missing coverage/cut premise: "+text)
    log=LOG.read_text("utf-8")
    if "sorryAx" in log or "error:" in log:
        raise SystemExit("NOT_READY: compiled Lean sorry or error reported")
    claims={}
    for module,names in NAMES.items():
        for target in names:
            rx=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
            found=rx.findall(log)
            if len(found)!=1:
                raise SystemExit(f"NOT_READY: missing or duplicated real Lean #print axioms {target}")
            ax={x.strip() for x in found[0].split(",") if x.strip()}
            if not ax <= ALLOWED:
                raise SystemExit(f"NOT_READY: disallowed axioms in {target}: {sorted(ax-ALLOWED)}")
            claims[target]=sorted(ax)
    output={
        "status":"CP014_ORIGINAL_ZETA_SEAM_PARTIAL_KERNEL_ONLY",
        "meaning":"Original 52<=N(149.5), original full zero count as finset cardinal, conditional N(149.5)=52 given authentic source witness cover, conditional HardyZ monotone uniqueness",
        "upstream_original_commit":UPSTREAM_COMMIT,
        "original_upstream_toolchain":"leanprover/lean4:v4.35.0",
        "source_sha256":{x:sha(p) for x,p in src.items()},
        "actual_olean_sha256":{x:sha(p) for x,p in oleans.items()},
        "actual_axiom_log_sha256":sha(LOG),
        "certified_standard_axioms":claims,
        "new_unconditional_N_1495_eq_52_Lean_proved":False,
        "new_source_Euler_RS_zero_finset_coverage_Lean_proved":False,
        "N_15005353_le_53_Lean_proved":False,
        "HardyZ_strict_monotonicity_on_root53_window_proved":False,
        "CP010_refined_root_exists_Lean_proved":False,
        "signed_Weil_to_spectral_dictionary_Lean_proved":False,
    }
    RECEIPT.write_text(json.dumps(output,indent=2)+"\n","utf-8")
    print(output["status"])
    print("A conditional finite-cut theorem is NOT an unconditional N(149.5)=52 theorem.")

if __name__=="__main__":
    main()
