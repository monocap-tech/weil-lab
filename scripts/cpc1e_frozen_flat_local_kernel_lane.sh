#!/usr/bin/env bash
# Explicit local Lean4.34 B->C->D->E certification. NO Actions dispatch.
set -euo pipefail
cd "$(dirname "$0")/.."
command -v lake >/dev/null || { echo "Pinned elan/Lean Lake required" >&2; exit 1; }
test "$(cat lean-toolchain)" = "leanprover/lean4:v4.34.0"
# This fails closed if the earlier repaired CP-C1(B) has any Lean errors.
bash scripts/cpc1b_c1c_c1d_local_kernel_lane.sh
python3 -m py_compile scripts/cpc1e_frozen_cp001_prime_geometry.py \
  scripts/cpc1e_frozen_flat_kernel_gate.py
python3 scripts/cpc1e_frozen_flat_kernel_gate.py selftest
python3 scripts/cpc1e_frozen_flat_kernel_gate.py preflight
python3 scripts/cpc1e_frozen_cp001_prime_geometry.py | tee cpc1e-rational-preflight-NOT-LEAN.log
lake build WeilDefect.Arithmetic.CP_C1E_FrozenFlatSchwartz 2>&1 | tee cpc1e-original-Lean-build.log
test -s .lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1E_FrozenFlatSchwartz.olean
lake env lean WeilDefect/Arithmetic/CP_C1E_FrozenFlatSchwartz.lean \
  2>&1 | tee cpc1e-original-kernel-axioms.log
python3 scripts/cpc1e_frozen_flat_kernel_gate.py verify
test -s cpc1e-original-kernel-receipt.json
echo "CP-C1(E) genuine exact flat physical Schwartz kernel + 16 axiom receipts PASS"
