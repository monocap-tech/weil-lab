# Lean Status Ledger

This file records formal verification separately from mathematical standing and P4 audit status.

## Status labels

- **LEAN-NOT-ATTEMPTED** — not yet entered into the formalization queue.
- **LEAN-IN-PROGRESS** — a Lean declaration or infrastructure exists but has not yet passed the pinned CI build.
- **LEAN-CERTIFIED** — kernel-checked under the pinned toolchain with no project \`sorry\`, \`admit\`, or \`axiom\`.
- **LEAN-CERTIFIED-FROM-IMPORTED-PREMISE** — Lean verifies the downstream deduction from an explicit external premise, but not the external theorem itself.
- **LEAN-BLOCKED** — direct formalization is exhausted for the current pass and an exact missing formal dependency is recorded.
- **SCOPE-ONLY** — jurisdiction rule rather than a theorem.

## Declaration map

| Stable ID | Lean declaration | Status |
| --- | --- | --- |
| WD-T26 | \`WeilDefect.wd_t26_finite_pair_zero_moment\` | LEAN-IN-PROGRESS |
| WD-X03 | \`WeilDefect.wd_x03_individual_not_compositional\` | LEAN-IN-PROGRESS |
| WD-X04 | \`WeilDefect.wd_x04_shorted_covariance_identity\` | LEAN-IN-PROGRESS |
| WD-X07 | \`WeilDefect.wd_x07_response_identity\` | LEAN-IN-PROGRESS |

The statuses above become LEAN-CERTIFIED only after the pinned CI build succeeds.

## Current formalization cursor

\[
\boxed{
\texttt{LEAN-H1-P0 / INFRASTRUCTURE AND VERTICAL PILOT}.
}
\]
