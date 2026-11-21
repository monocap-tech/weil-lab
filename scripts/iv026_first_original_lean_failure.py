#!/usr/bin/env python3
"""IV026: isolate the FIRST actual IV009 original Lean compiler failure.

The real target is the unchanged Zeta23 original finite-complex-Schwartz
divisor-polarization theorem source. This parser is a DIAGNOSTIC, not a
Lean compiler and never certifies any mathematical theorem.

On the currently queued GitHub job no compiler log exists; emit an
explicit NOT_RUN/NO_COMPILER_LOG receipt rather than hallucinating a
kernel result. Once a real run produces a log, preserve its source
line, column, Lean message, and SHA custody for a precise repair.

Run from repository root:
 python3 scripts/iv026_first_original_lean_failure.py \
   --log iv009-original-schwartz-polarization-build.log \
   --output iv026-first-original-Lean-kernel-diagnostic.json
 python3 scripts/iv026_first_original_lean_failure.py --selftest
"""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path

SRC=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean")
DEFAULT_LOG=Path("iv009-original-schwartz-polarization-build.log")
DEFAULT_OUT=Path("iv026-first-original-Lean-kernel-diagnostic.json")

# Mathlib and Lean emit either "file:line:column: error:" or a
# standalone "error:" block. Preserve exact first source diagnostic.
LEAN_LOC=re.compile(r"(?P<file>[^\s:]+\.lean):(?P<line>\d+):(?P<column>\d+):\s*error:\s*(?P<message>.*)")
LEAN_ERROR=re.compile(r"(^|\n)\s*(?:error:|##\[error\])",re.I)
NO_PROOF_MARKERS=("sorryAx", "declaration uses `sorry`")

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def inspect(log_path=DEFAULT_LOG):
    if not SRC.is_file():
        raise FileNotFoundError("Original IV009 source not present; cannot make a source-bound report")
    report={
        "schema":"IV026-original-IV009-first-compiler-failure-triage-v1",
        "target":"WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization",
        "source_path":str(SRC),
        "source_sha256":sha(SRC),
        "log_path":str(log_path),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "github_head_sha":os.environ.get("GITHUB_SHA"),
        "kernel_certified_by_this_script":False,
        "original_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    if not log_path.is_file():
        report.update({
            "status":"NO_COMPILER_LOG",
            "log_sha256":None,
            "first_real_Lean_error":None,
            "next_action":"Obtain a genuinely executed direct original IV009 Lean job or run the opt-in pinned IV025 recovery script. Queued GitHub Actions has no diagnostic.",
        })
        return report

    raw=log_path.read_text(errors="replace")
    report["log_sha256"]=sha(log_path)
    matches=list(LEAN_LOC.finditer(raw))
    general=list(LEAN_ERROR.finditer(raw))
    if matches:
        first=matches[0]
        report["first_real_Lean_error"]={
            "file":first.group("file"),
            "line":int(first.group("line")),
            "column":int(first.group("column")),
            "message":first.group("message")[:1500],
        }
        report["status"]="LEAN_SOURCE_ERROR"
        report["next_action"]="Repair this FIRST original Lean source error and rerun the genuine kernel/axiom gate. Do not certify later IV stages."
    elif general or any(marker in raw for marker in NO_PROOF_MARKERS):
        at=(general[0].start() if general else min((raw.index(m) for m in NO_PROOF_MARKERS if m in raw),default=0))
        report["first_real_Lean_error"]={
            "file":None,"line":None,"column":None,
            "message":raw[max(0,at-150):at+1600],
        }
        report["status"]="LEAN_OR_TOOLCHAIN_ERROR_UNLOCATED"
        report["next_action"]="Inspect earliest failing actual GitHub step/Lean diagnostic; do not infer proof success."
    else:
        report["first_real_Lean_error"]=None
        report["status"]="NO_ERROR_FOUND_IN_BUILD_LOG_ONLY"
        report["next_action"]="A green build log is INSUFFICIENT. Require real .olean, source-bound direct #print axioms standard-only audit and IV009 kernel JSON receipt."
    return report

def selftest():
    cases=[
      ("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean:111:8: error: tactic 'change' failed\n","LEAN_SOURCE_ERROR",111),
      ("error: toolchain unavailable\n","LEAN_OR_TOOLCHAIN_ERROR_UNLOCATED",None),
      ("Building WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization\n","NO_ERROR_FOUND_IN_BUILD_LOG_ONLY",None),
    ]
    for raw,want,line in cases:
        matches=list(LEAN_LOC.finditer(raw))
        general=list(LEAN_ERROR.finditer(raw))
        actual=("LEAN_SOURCE_ERROR" if matches else
            "LEAN_OR_TOOLCHAIN_ERROR_UNLOCATED" if general else
            "NO_ERROR_FOUND_IN_BUILD_LOG_ONLY")
        assert actual==want,(want,actual)
        assert ((int(matches[0].group("line")) if matches else None)==line)
    assert LEAN_LOC.search("not a compiler proof")
    is None
    print("IV026 FIRST-ERROR source diagnostic parser: located original Lean failure, toolchain failure, false green build-only control all PASS. Not a Lean kernel proof.")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--log",type=Path,default=DEFAULT_LOG)
    ap.add_argument("--output",type=Path,default=DEFAULT_OUT)
    ap.add_argument("--selftest",action="store_true")
    args=ap.parse_args()
    if args.selftest:
        selftest()
        return
    receipt=inspect(args.log)
    args.output.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(f"IV026 FIRST REAL ORIGINAL LEAN DIAGNOSTIC: {receipt['status']}; kernel acceptance NOT inferred. See {args.output}")

if __name__=="__main__":
    main()
