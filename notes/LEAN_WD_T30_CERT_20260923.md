# LEAN-H1-P1 — WD-T30 Certificate
Date: 2026-09-23

## Target

```math
\boxed{
\text{WD-T30 — two-mode selected-preserving multiplier}.
}
```

## Formal content

Let

```math
C:V\to\mathbb C
```

be a complex-linear selected-response functional and let

```math
\psi_1,\psi_2\in V.
```

If

```math
C(\psi_1)\ne0
\quad\text{or}\quad
C(\psi_2)\ne0,
```

Lean constructs

```math
\beta_1=C(\psi_2),
\qquad
\beta_2=-C(\psi_1),
```

with

```math
(\beta_1,\beta_2)\ne(0,0)
```

and proves

```math
\boxed{
C(\beta_1\psi_1+\beta_2\psi_2)=0.
}
```

The degenerate branch

```math
C=0
```

is also formalized, proving every mode is selected-preserving.

This matches the stable theorem's algebraic/function-space content; no
explicit-formula or actual-zeta premise is consumed.

## Certification evidence

GitHub Actions run:

```math
\texttt{35953990661}
```

checked repository head:

```math
\texttt{6836f64a22544a2bd51daeb97d97bf824d339def}.
```

The single target

```math
\texttt{WeilDefect.Arithmetic.Scalarization}
```

built successfully under Lean 4.34.0 / mathlib v4.34.0, and the repository
unfinished-proof/project-axiom gate passed.

## Status

```math
\boxed{
\text{WD-T30: LEAN-CERTIFIED}.
}
```

No second theorem was started in this pass.
