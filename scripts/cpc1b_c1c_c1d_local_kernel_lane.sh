#!/usr/bin/env bash
# Single original Lean v4.34 physical Weil source gate, NOT an Actions launch.
set -euo pipefail
cd "$(dirname "$0")/.."
test "$(cat lean-toolchain)" = "leanprover/lean4:v4.34.0"
command -v python3 >/dev/null
command -v lake >/dev/null || { echo "Lean/elan not installed" >&2; exit 1; }
python3 -m py_compile scripts/cpc1b_original_source_gate.py scripts/cpc1b_original_kernel_receipt_gate.py scripts/cpc1c_original_finite3_source_preflight.py scripts/cpc1d_original_nine_scalar_preflight.py scripts/cpc1cd_original_kernel_receipt_gate.py
python3 scripts/cpc1b_original_source_gate.py --upstream
python3 scripts/cpc1b_original_kernel_receipt_gate.py selftest
python3 scripts/cpc1b_original_kernel_receipt_gate.py preflight
python3 scripts/cpc1cd_original_kernel_receipt_gate.py selftest
python3 scripts/cpc1cd_original_kernel_receipt_gate.py preflight
lake update
lake exe cache get
for item in "B CP_C1B_OriginalNineProbeSource cpc1b" "C CP_C1C_OriginalCompleteDivisorFinite3 cpc1c" "D CP_C1D_OriginalNineProbeCompatibility cpc1d"; do
  read -r tag mod prefix <<< "$item"
  lake build WeilDefect.Arithmetic."$mod" 2>&1 | tee "$prefix"-original-Lean-build.log
  test -s .lake/build/lib/lean/WeilDefect/Arithmetic/"$mod".olean
  lake env lean WeilDefect/Arithmetic/"$mod".lean 2>&1 | tee "$prefix"-original-kernel-axioms.log
  if [[ "$tag" == "B" ]]; then
    python3 scripts/cpc1b_original_kernel_receipt_gate.py verify
  fi
done
python3 scripts/cpc1cd_original_kernel_receipt_gate.py verify
test -s cpc1b-original-kernel-receipt.json
test -s cpc1c-cpc1d-original-kernel-receipt.json
echo "CP-C1(B/C/D) genuine direct compiler and strict kernel receipt PASS."
