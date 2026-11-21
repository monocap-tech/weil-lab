#!/usr/bin/env bash
# IV025: run the EARLIEST original unresolved actual Lean kernel gate,
# IV009 finite-complex-Schwartz full divisor polarization, in a
# working tree with the pinned Lean/Mathlib toolchain installed.
#
# This is deliberately a MANUAL recovery runner; do not attach it to
# pull_request or enqueue 60+ unrelated repo workflows. It creates
# REAL source-specific build, axiom and audit receipts if and only if
# the kernel genuinely accepts the actual source.
#
# Usage from repository root:
#   bash scripts/iv025_recover_first_original_lean.sh
#
# No sorry/axiom is introduced, no source theorem is weakened.
set -euo pipefail

if [[ ! -f lakefile.toml || ! -f lean-toolchain ]]; then
  echo 'FAIL: Run from the actual Weil-Lab repository root with tracked Lake config.'
  exit 2
fi
if ! command -v lake >/dev/null 2>&1; then
  echo 'BLOCKED: pinned Lean lake executable is not installed or not on PATH.'
  echo 'No Lean kernel certification was performed.'
  exit 2
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo 'BLOCKED: python3 is needed for source and strict axiom auditor.'
  exit 2
fi

echo '[IV025] Earliest source-only IV009 preflight (not a Lean result).'
python3 scripts/iv009_original_schwartz_polarization_audit.py preflight

echo '[IV025] Preserve tracked source toolchain and Lake config fingerprints.'
sha256sum lean-toolchain lakefile.toml |
  tee iv025-original-pinned-config-sha256.txt

echo '[IV025] Resolve Mathlib from tracked lakefile.toml (pinned v4.34.0).'
lake update
test -s lake-manifest.json
sha256sum lake-manifest.json |
  tee iv025-original-Lake-generated-manifest-sha256.txt
lake exe cache get

echo '[IV025] ORIGINAL complete Schwartz finite-sum Lean build.'
# Failure exits IMMEDIATELY even when tee was used.
lake build WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization 2>&1 |
  tee iv025-original-iv009-first-kernel-build.log

echo '[IV025] REAL direct strict original axioms, not source-only inventory.'
lake env lean WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean 2>&1 |
  tee iv009-original-schwartz-polarization-axioms.log

echo '[IV025] Require exact source-bound compiled .olean and all standard-only source axioms.'
python3 scripts/iv009_original_schwartz_polarization_audit.py verify
test -s iv009-original-schwartz-polarization-kernel-audit.json

echo '[IV025] REAL IV009 kernel/audit PASS. This does not certify downstream IV017–IV023.'
