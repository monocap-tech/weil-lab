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
| WD-T33 | WeilDefect.wd_t33_adaptive_cocancellation | LEAN-CERTIFIED |
| WD-T30 | WeilDefect.wd_t30_two_mode_kernel_combination + WeilDefect.wd_t30_zero_functional_preserves_every_mode | LEAN-CERTIFIED |
| WD-X01 | WeilDefect.wd_x01_partial_sum + WeilDefect.wd_x01_finite_defect_negative + WeilDefect.wd_x01_finite_defect_formula + WeilDefect.wd_x01_defect_tendsto_zero | LEAN-CERTIFIED |
| WD-T26 | \`WeilDefect.wd_t26_finite_pair_zero_moment\` | LEAN-IN-PROGRESS |
| WD-X03 | \`WeilDefect.wd_x03_individual_not_compositional\` | LEAN-IN-PROGRESS |
| WD-X04 | \`WeilDefect.wd_x04_shorted_covariance_identity\` | LEAN-IN-PROGRESS |
| WD-X07 | WeilDefect.wd_x07_response_identity + WeilDefect.wd_x07_real_response_formula + WeilDefect.wd_x07_scaled_response_tendsto_neg_one | LEAN-CERTIFIED |

The statuses above become LEAN-CERTIFIED only after the pinned CI build succeeds.

## Current formalization cursor

\[
\boxed{
\texttt{LEAN-H1-P0 / INFRASTRUCTURE AND VERTICAL PILOT}.
}
\]


## First certificate evidence

The first stable-ID certifications were built at Lean commit:

\[
\boxed{
\texttt{c125114e2dd39fa3907f8690ca39d9c899468caf}.
}
\]

GitHub Actions run:

\[
\boxed{
\texttt{35949414095}.
}
\]

The run completed successfully with all of:

- pinned dependency resolution;
- mathlib cache fetch;
- Lake build;
- unfinished/project-axiom rejection.

Thus WD-X03 and WD-X04 satisfy the repository's LEAN-CERTIFIED rule.

WD-T26 and WD-X07 remain LEAN-IN-PROGRESS because their current declarations certify only algebraic cores, not yet the complete stable theorem/example statements.

## Current formalization cursor

\[
\boxed{
\texttt{LEAN-H1-P1 / ALGEBRAIC AND FINITE-DIMENSIONAL CORE}.
}
\]


## WD-X01 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-X01: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.wd_x01_weight_sq_telescope;
- WeilDefect.wd_x01_partial_sum;
- WeilDefect.wd_x01_finite_defect_negative;
- WeilDefect.wd_x01_finite_defect_formula;
- WeilDefect.wd_x01_defect_tendsto_zero.

The dedicated theorem CI checked only:

\[
\texttt{WeilDefect/Examples/SpectralScreening.lean}.
\]

Certificate run:

\[
\boxed{
\texttt{35952789867}
}
\]

at repository head:

\[
\boxed{
\texttt{6ef0dffba1a8732d554b15ee906c64fe60bc63c7}.
}
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- Lean compilation of the WD-X01 target;
- repository unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-X07 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-X07: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.wd_x07_response_identity;
- WeilDefect.wd_x07_real_response_formula;
- WeilDefect.wd_x07_scaled_response_tendsto_neg_one.

The certificate proves the exact two-point rational identity and an explicit
sharpness witness with nonzero inverse-square leading coefficient.

The current theorem file blob

\[
\texttt{83196783b21e40eee21ca74c12b3b8094c2af391}
\]

is identical to the blob checked successfully by GitHub Actions run

\[
\boxed{
\texttt{35951096357}.
}
\]

That run checked repository commit

\[
\texttt{e9f158d3c8fb5b85494d08931d62cddfc8d4a534}
\]

under the pinned Lean 4.34.0 / mathlib v4.34.0 environment and passed the
unfinished-proof/project-axiom gate.

A later dedicated WD-X07 rerun was also launched for redundant single-target
confirmation; certification does not depend on it because the exact current
Lean source blob is already kernel-checked.

No other stable theorem ID is promoted by this certificate.


## WD-T30 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T30: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.wd_t30_two_mode_selected_preserving;
- WeilDefect.wd_t30_both_zero_selected_preserving;
- WeilDefect.wd_t30_two_mode_kernel_combination;
- WeilDefect.wd_t30_zero_functional_preserves_every_mode.

The stable theorem is represented at the functional level:

given a complex-linear selected-response functional \(C\) and two multiplier
modes \(\psi_1,\psi_2\) whose selected responses are not both zero, Lean
constructs a nontrivial coefficient pair \((\beta_1,\beta_2)\) with

\[
C(\beta_1\psi_1+\beta_2\psi_2)=0.
\]

The identically-zero functional branch is also formalized: every mode is
selected-preserving.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Arithmetic.Scalarization}
\]

through Lake.

Certificate run:

\[
\boxed{
\texttt{35953990661}
}
\]

at repository head:

\[
\boxed{
\texttt{6836f64a22544a2bd51daeb97d97bf824d339def}.
}
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T33 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T33: LEAN-CERTIFIED}.
}
\]

Formal declaration:

- WeilDefect.wd_t33_adaptive_cocancellation.

The certificate formalizes the exact cutoffwise algebraic implication:

\[
N+F=P+A,
\qquad
N=A
\quad\Longrightarrow\quad
P=F.
\]

This is the complete algebraic content of the audited WD-T33 co-adaptation theorem.
The analytic interpretation of \(N,F,P,A\) belongs to the surrounding explicit-formula
setup and is not assumed by the Lean proof.

The current theorem file blob

\[
\texttt{d01f92d725b9ad412130424b74bea9efadcda1e1}
\]

is identical to the blob included in successful full-library GitHub Actions run

\[
\boxed{
\texttt{35951096357}.
}
\]

That run checked commit

\[
\texttt{e9f158d3c8fb5b85494d08931d62cddfc8d4a534}
\]

with:

- pinned dependency resolution;
- mathlib cache retrieval;
- full Lake build;
- unfinished-proof/project-axiom rejection.

A later dedicated WD-T33-only CI run was also launched; certification does not depend
on it because the exact current source blob was already kernel-checked in the successful
full-library run.

No other stable theorem ID is promoted by this certificate.
