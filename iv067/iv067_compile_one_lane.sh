#!/usr/bin/env bash
# IV067: explicit/manual one-lane compilation. NO PR trigger, NO historical fanout.
# Install files under paths recorded in IV067 bundle and invoke inside a committed
# original checkout whose HEAD descends from the original IV023 source pin.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
mkdir -p verification/iv067/out
# Pinned manifest creation MUST precede manifest-sensitive preflight.
lake update
python3 iv067/iv067_source_gate.py --mode local --root "$ROOT"
python3 iv067/iv067_source_gate.py --mode source --root "$ROOT"
lake exe cache get
# Both logs are actual processes, not generated or hand-edited receipt data.
python3 - <<'PY'
from pathlib import Path
import time
p=Path('verification/iv067/out/compiler_started_ns.txt')
p.write_text(str(time.time_ns())+'\n')
PY
# Critical: remove the OLD target, forcing a new compiler output.
rm -f .lake/build/lib/lean/WeilDefect/Arithmetic/IV066OriginalSourcePilot.olean
rm -f .lake/build/lib/lean/WeilDefect/Arithmetic/IV066OriginalSourcePilot.ilean
lake build WeilDefect.Arithmetic.IV066OriginalSourcePilot \
  > verification/iv067/out/IV067_build.log 2>&1 || {
    cat verification/iv067/out/IV067_build.log
    echo 'IV067 LEAN BUILD FAILED; no PASS receipt produced' >&2
    exit 1
  }
# Must process actual Lean #print axioms, with exit status preserved.
lake env lean verification/IV066AxiomAudit.lean \
  > verification/iv067/out/IV067_axioms.log 2>&1 || {
    cat verification/iv067/out/IV067_axioms.log
    echo 'IV067 AXIOM COMPILER FAILED; no PASS receipt produced' >&2
    exit 1
  }
python3 iv067/iv067_source_gate.py --mode receipts --root "$ROOT" \
  --build-log verification/iv067/out/IV067_build.log \
  --axiom-log verification/iv067/out/IV067_axioms.log \
  --start-stamp verification/iv067/out/compiler_started_ns.txt \
  --output verification/iv067/out/IV067_kernel_receipt.json
