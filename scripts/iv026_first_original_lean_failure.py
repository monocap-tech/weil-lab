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
# Lean JSON/CLI and GitHub Actions traces use TWO actual formats:
#   source.lean:111:2: error: ...
#   2026-...Z error: source.lean:111:2: ...
# The SECOND form is the one present in the REAL failed
# IV009 run 44844586039 (job 136661046862). Losing this
# source position would prevent targeted compiler recovery.
LEAN_LOC_STANDARD=re.compile(r"(?P<file>[^\s:]+\.lean):(?P<line>\d+):(?P<column>\d+):\s*error:\s*(?P<message>[^\n]*)")
LEAN_LOC_PREFIXED=re.compile(r"\berror:\s*(?P<file>[^\s:]+\.lean):(?P<line>\d+):(?P<column>\d+):\s*(?P<message>[^\n]*)")
LEAN_ERROR=re.compile(r"(?m)^(?:\d{4}-\d\d-\d\dT[^\s]+\s+)?\s*(?:error:|##\[error\])",re.I)

def located_errors(raw):
    return sorted(
      [m for pattern in (LEAN_LOC_STANDARD,LEAN_LOC_PREFIXED)
       for m in pattern.finditer(raw)],
      key=lambda m:m.start()
    )
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
    matches=located_errors(raw)
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
      # EXACT source formatting observed in actual failed IV009
      # GitHub Actions run 44844586039, job 136661046862:
      ("2026-11-21T01:26:37.2914974Z error: WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean:111:2: 'change' tactic failed, pattern\n",
        "LEAN_SOURCE_ERROR",111,2),
      # Alternative direct Lean diagnostic:
      ("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean:111:8: error: tactic 'change' failed\n",
        "LEAN_SOURCE_ERROR",111,8),
      # Timestamped infrastructure errors must not be treated as
      # successful builds or reported as an original source location.
      ("2026-11-21T01:26:37.2914974Z error: toolchain unavailable\n",
        "LEAN_OR_TOOLCHAIN_ERROR_UNLOCATED",None,None),
      ("error: network dependency unavailable\n",
        "LEAN_OR_TOOLCHAIN_ERROR_UNLOCATED",None,None),
      ("Building WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization\n",
        "NO_ERROR_FOUND_IN_BUILD_LOG_ONLY",None,None),
    ]
    for raw,want,line,column in cases:
        matches=located_errors(raw)
        generic=list(LEAN_ERROR.finditer(raw))
        actual=("LEAN_SOURCE_ERROR" if matches else
            "LEAN_OR_TOOLCHAIN_ERROR_UNLOCATED" if generic else
            "NO_ERROR_FOUND_IN_BUILD_LOG_ONLY")
        assert actual==want,(want,actual)
        assert ((int(matches[0].group("line")) if matches else None)==line)
        assert ((int(matches[0].group("column")) if matches else None)==column)
    assert not located_errors("warning: no original Lean failure")
    print("IV028 original first-error diagnostic parser PASS: REAL 44844586039 timestamp-prefixed IV009 source error line111:2, conventional Lean error, timestamped setup failures, and false-green build-only control. NONKERNEL.")
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
