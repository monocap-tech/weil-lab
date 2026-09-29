#!/usr/bin/env bash
set -euo pipefail

lake build WeilDefect.Morphology.NeutralFourierCarrier

if grep -R -nE '^[[:space:]]*(axiom|sorry|admit)\b' \
  WeilDefect/Morphology/NeutralFourierCarrier.lean; then
  echo "Unfinished or project-axiom declaration found in NeutralFourierCarrier.lean."
  exit 1
fi

echo "NeutralFourierCarrier build and trusted-declaration check passed."
