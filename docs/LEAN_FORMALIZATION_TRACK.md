# Lean Formalization Track
## LEAN-H1 — Certification before H1-P5

This track temporarily preempts H1-P5.

The project does **not** resume public-package assembly until LEAN-H1 is exhausted under the current Horizon-1 theorem inventory.

## Toolchain

Pinned baseline:

\[
\boxed{
\text{Lean 4.34.0}
\qquad
\text{mathlib v4.34.0}.
}
\]

The project uses:

- \`lean-toolchain\`;
- \`lakefile.toml\`;
- the \`WeilDefect\` Lean namespace;
- GitHub Actions build verification.

## Certification rule

A theorem is **LEAN-CERTIFIED** only if:

1. its Lean declaration exists in the repository;
2. the declaration contains no \`sorry\`, \`admit\), or project \`axiom\`;
3. the pinned Lean/mathlib build succeeds in CI;
4. the theorem-ID-to-declaration map is recorded durably.

A proof downstream from an imported external theorem is not called a full Lean certification of that external theorem.

Instead the status is:

\[
\boxed{
\text{LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
\]

The imported premise itself remains separately unformalized until its source theorem is reconstructed in Lean.

## Phases

### LEAN-H1-P0 — Infrastructure and vertical pilot — COMPLETE

- initialize Lake/mathlib project;
- pin toolchain;
- establish CI;
- prohibit \`sorry\`, \`admit\`, and project \`axiom\`;
- certify a small vertical slice of algebraic theorem/example statements.

### LEAN-H1-P1 — Algebraic and finite-dimensional core — ACTIVE

Primary targets:

- WD-T05;
- WD-T07;
- WD-T09;
- WD-T14;
- WD-T20;
- WD-T21;
- WD-T26;
- WD-T27;
- WD-X01 through WD-X07.

### LEAN-H1-P2 — Operator screening core

Targets:

- WD-T01 through WD-T13 excluding statements already discharged;
- Douglas-dependent theorems formalized downstream from an explicit imported-premise interface until Douglas itself is reconstructed or mapped to an existing mathlib theorem.

### LEAN-H1-P3 — Filtration and persistence core

Targets:

- WD-T15 through WD-T19;
- weak/strong convergence;
- endpoint intersection spaces;
- quotient/index arguments;
- boundary amplification.

### LEAN-H1-P4 — Zeta-Weil specialization

Targets:

- WD-T20 through WD-T36;
- imported analytic results represented as explicit premises where their source proofs have not yet been formalized;
- no hidden project axioms.

### LEAN-H1-P5 — Composite morphology

Targets:

- WD-T37 through WD-T39;
- certify the deductions from already certified internal theorems and explicit external premises;
- preserve every P4.3 branch/custody correction.

### LEAN-H1-P6 — Imported-source reconstruction frontier

Attempt direct Lean reconstruction of load-bearing external results where feasible:

- Douglas factorization if not already available in mathlib;
- Bombieri finite inertia/multiplicity;
- zeta zero counting;
- compact-window explicit formula;
- special-function asymptotics.

This phase may terminate with exact formalization blockers if reconstructing an external analytic theorem requires a corpus far larger than this project.

## Exhaustion condition

LEAN-H1 is exhausted only when every stable Horizon-1 theorem/example has one of the following durable states:

\[
\boxed{
\begin{array}{l}
\text{LEAN-CERTIFIED},\\
\text{LEAN-CERTIFIED-FROM-IMPORTED-PREMISE},\\
\text{LEAN-BLOCKED with an exact formal dependency/blocker},\\
\text{SCOPE-ONLY}.
\end{array}
}
\]

A theorem may not remain merely “not attempted.”

Only after this exhaustion condition is met does the project resume:

\[
\boxed{
\texttt{H1-P5.0 / PUBLIC PACKAGE ARCHITECTURE}.
}
\]

## Current cursor

\[
\boxed{
\texttt{LEAN-H1-P1 / WD-X02 — CRITICAL SCREENING WITHOUT AN ATTAINED NEUTRAL VECTOR}.
}
\]
