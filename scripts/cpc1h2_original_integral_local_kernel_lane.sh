#!/usr/bin/env bash
# Strict single one-leaf original frozen H2 source lane; no PR/dispatch here.
set -euo pipefail
cd "$(dirname "$0")/.."
test "$(cat lean-toolchain)" = "leanprover/lean4:v4.34.0"
command -v lake >/dev/null || { echo 'Pinned Lake unavailable' >&2; exit 1; }
python3 -m py_compile scripts/cpc1h2_original_integral_kernel_gate.py
python3 scripts/cpc1h2_original_integral_kernel_gate.py preflight
python3 scripts/cpc1h2_original_integral_kernel_gate.py selftest
# Produce authenticated upstream receipt and verify its exact .olean.
bash scripts/cpc1fg_frozen_local_kernel_lane.sh
lake build WeilDefect.Arithmetic.CP_C1H_OriginalPointwisePrimeCorrelation 2>&1 | tee cpc1h1-original-Lean-build.log
test -s .lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1H_OriginalPointwisePrimeCorrelation.olean
lake env lean WeilDefect/Arithmetic/CP_C1H_OriginalPointwisePrimeCorrelation.lean 2>&1 | tee cpc1h1-original-kernel-axioms.log
python3 scripts/cpc1h_original_pointwise_kernel_gate.py verify
lake build WeilDefect.Arithmetic.CP_C1H2_OriginalFrozenCorrelationIntegrals 2>&1 | tee cpc1h2-original-Lean-build.log
test -s .lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1H2_OriginalFrozenCorrelationIntegrals.olean
lake env lean WeilDefect/Arithmetic/CP_C1H2_OriginalFrozenCorrelationIntegrals.lean 2>&1 | tee cpc1h2-original-kernel-axioms.log
python3 scripts/cpc1h2_original_integral_kernel_gate.py verify
test -s cpc1h2-original-kernel-receipt.json
echo 'CP-C1(H2) genuine frozen original correlation Lean4.34 kernel PASS.'
