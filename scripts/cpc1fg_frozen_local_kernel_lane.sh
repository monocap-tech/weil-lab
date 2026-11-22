#!/usr/bin/env bash
# One approved local B->C->D->E->F/G direct Lean4.34 gate.
set -euo pipefail
cd "$(dirname "$0")/.."
test "$(cat lean-toolchain)" = "leanprover/lean4:v4.34.0"
command -v lake >/dev/null || { echo "Pinned elan/Lake missing" >&2; exit 1; }
python3 -m py_compile scripts/cpc1fg_frozen_kernel_receipt_gate.py
python3 scripts/cpc1fg_frozen_kernel_receipt_gate.py preflight
python3 scripts/cpc1fg_frozen_kernel_receipt_gate.py selftest
bash scripts/cpc1e_frozen_flat_local_kernel_lane.sh
lake build WeilDefect.Arithmetic.CP_C1FG_FrozenTargetAndRadiusGlue \
  2>&1 | tee cpc1fg-original-Lean-build.log
test -s .lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1FG_FrozenTargetAndRadiusGlue.olean
lake env lean WeilDefect/Arithmetic/CP_C1FG_FrozenTargetAndRadiusGlue.lean \
  2>&1 | tee cpc1fg-original-kernel-axioms.log
python3 scripts/cpc1fg_frozen_kernel_receipt_gate.py verify
test -s cpc1fg-original-kernel-receipt.json
echo "CP-C1(F/G) genuine original frozen source Lean4.34 kernel PASS"
