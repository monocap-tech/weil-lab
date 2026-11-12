# RPB-74 — WD-T40 F-1 static closure and build handoff

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **STATIC LINE CLOSED / F-1 SOURCE FROZEN AT AUDITED GIT BLOB / DETERMINISTIC BUILD HANDOFF NOW VERIFIES EXACT BLOB, ROOT IMPORT, MODULE BUILD, AND TRUST SCAN / NO STATIC SOURCE BLOCKER REMAINS / BUILD CERTIFICATION STILL REQUIRES A REAL LEAN RUNNER / F-2 REMAINS CLOSED**

## 0. Objective

RPB-71 through RPB-73 established declaration/API, typeclass, and proof-term static passes for the F-1 carrier.

RPB-74 closes the static line and converts the remaining obligation into one deterministic build handoff.

## 1. Frozen carrier source

The audited carrier module is:

~~~text
WeilDefect/Morphology/NeutralFourierCarrier.lean
~~~

Its Git blob SHA is:

~~~text
93f05eceb07ffda593181d0e9293caa0a05705ac
~~~

This is the exact source state that passed:

~~~text
RPB-71  STATIC API PASS
RPB-72  TYPECLASS STATIC PASS
RPB-73  PROOF-TERM STATIC PASS
~~~

No F-2 definition is present in the file.

## 2. Root-library custody

The project root imports the carrier through the exact line:

~~~text
import WeilDefect.Morphology.NeutralFourierCarrier
~~~

The build handoff checks that this import is still present before compiling.

## 3. Deterministic build handoff

The repository-local command is:

~~~text
scripts/check_neutral_fourier_carrier.sh
~~~

RPB-74 strengthens that script so it now checks, in order:

1. the current carrier file hashes to the frozen audited Git blob;
2. the project root imports the carrier module;
3. Lake builds exactly `WeilDefect.Morphology.NeutralFourierCarrier`;
4. the carrier source contains no top-level `axiom`, `sorry`, or `admit` declaration.

If the carrier source changes after RPB-74, the script fails before build and prints both expected and actual Git blob IDs.

Thus a future green run cannot silently certify a different carrier revision.

## 4. Trust-scan hardening

The unfinished-proof scan now uses a portable explicit end condition:

~~~text
^[[:space:]]*(axiom|sorry|admit)([[:space:]]|$)
~~~

rather than relying on a grep word-boundary escape.

This reduces shell/grep portability risk.

## 5. Build script state

The updated build script Git blob SHA is:

~~~text
eb60a028a37c26a341c43132f24ac068b84c0879
~~~

The script itself is not a certificate.

It is the canonical execution handoff for the first environment in which Lean/Lake actually runs.

## 6. F-1 closure classification

Current F-1 state:

~~~text
SOURCE IMPLEMENTED
STATIC API PASS
TYPECLASS STATIC PASS
PROOF-TERM STATIC PASS
STATIC LINE EXHAUSTED
BUILD CERTIFICATION INFRASTRUCTURE-BLOCKED
~~~

No further static source audit is authorized unless:

- the frozen carrier blob changes; or
- a real Lean compiler diagnostic identifies a new issue.

## 7. What remains before F-2

Exactly one gate remains:

~~~text
run scripts/check_neutral_fourier_carrier.sh
on a working pinned Lean 4.34.0 / mathlib v4.34.0 environment.
~~~

A successful run closes F-1.

A real compiler error reopens only the failing F-1 declaration.

Until one of those occurs, F-2 remains NOT STARTED.

## 8. RPB-74 determination

~~~math
\boxed{
\textbf{RPB-74 — F-1 IS STATICALLY EXHAUSTED AND FROZEN; THE ONLY REMAINING OBLIGATION IS A REAL LEAN BUILD OF THE AUDITED BLOB.}
}
~~~

WD-T40 remains mathematically P4-AUDIT-PASSED and formally LEAN-BLOCKED.

## Next cursor

~~~text
RPB-75 / WD-T40 F-1 BUILD EXECUTION GATE
~~~

The next pass should do only one thing: attempt the frozen build handoff in any newly available real Lean environment. If no Lean runner is available, record the unchanged gate and halt; do not restart static audits and do not begin F-2.