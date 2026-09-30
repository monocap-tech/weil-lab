#!/usr/bin/env bash
set -euo pipefail

module_file="WeilDefect/Morphology/NeutralFourierCarrier.lean"
root_file="WeilDefect.lean"
expected_blob="231ef346f14ba210826471a7817208d9c44059e6"

actual_blob="$(git hash-object "$module_file")"
if [[ "$actual_blob" != "$expected_blob" ]]; then
  echo "NeutralFourierCarrier.lean differs from the RPB-74 audited blob."
  echo "expected: $expected_blob"
  echo "actual:   $actual_blob"
  exit 1
fi

if ! grep -Fxq 'import WeilDefect.Morphology.NeutralFourierCarrier' "$root_file"; then
  echo "Root library does not import NeutralFourierCarrier."
  exit 1
fi

lake build WeilDefect.Morphology.NeutralFourierCarrier

if grep -nE '^[[:space:]]*(axiom|sorry|admit)([[:space:]]|$)' "$module_file"; then
  echo "Unfinished or project-axiom declaration found in NeutralFourierCarrier.lean."
  exit 1
fi

echo "NeutralFourierCarrier audited blob, root import, build, and trust checks passed."
