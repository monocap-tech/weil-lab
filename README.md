# Weil Defect

A public research repository for a defect-theoretic analysis of **Weil's quadratic form**, its finite negative-index structure, spectral screening, persistent negative directions, and compact-window neutral modes.

> **Status:** research program / theorem consolidation.  
> **This repository does not claim a proof of the Riemann Hypothesis.**

## What is being separated

The central organizational point is that there are two distinct mathematical objects:

\[
\boxed{\text{Weil-defect theory}}
\]

and

\[
\boxed{\text{the actual-zeta exclusion needed to close RH}.}
\]

The first can be studied independently of the second.

The working architecture is

\[
\boxed{
\text{finite negative index}
\longrightarrow
\text{spectral screening}
\longrightarrow
\begin{cases}
\text{negative persistence},\\
\text{neutral persistence},
\end{cases}
}
\]

followed, only at the final stage, by questions about whether the **actual zeta divisor** can realize the remaining defect geometry.

## First research horizon

The project is currently organized under [Horizon 1 — Independent Weil-Defect Theory](docs/HORIZON_1.md).

Its stop boundary is deliberately before RH closure. Horizon 1 is complete when the abstract defect calculus, zeta-Weil specialization, defect morphologies, proof audit, and public mathematical package are complete—even if the downstream actual-zeta interfaces remain open.

Current position:

\[
\boxed{
\text{H1-P0 COMPLETE}
\qquad
\text{H1-P1 ACTIVE}.
}
\]

Project terms such as **horizon**, **phase**, **standing**, **interface**, **custody**, and **screening** are fixed in the [Terminology Registry](docs/TERMINOLOGY.md).

H1-P1.0 has now extracted the first zeta-independent theorem package; see [Abstract Defect Calculus](docs/ABSTRACT_DEFECT_CALCULUS.md).

Its central operator is

\[
D=S_+S_+^*-S_-S_-^*,
\]

and the sign problem is equivalent to contractive Douglas screening. The abstraction also reveals a non-attained **approximate-neutral boundary** distinct from an actual neutral mode.

## Current theorem picture

| Component | Current standing |
| --- | --- |
| Finite Weil negative index | imported theorem + exact specialization |
| Rank-one defect formulation | derived |
| Critical-line tail monotonicity | proved with stated inputs |
| Spectral screening distinction | structural |
| Persistent normalized Weil negativity | conditional theorem |
| Quartet zero-moment law | proved in the selected quartet model |
| \(O(|z|^{-2})\) far-field decay | proved |
| Weighted next-jet localization | exact reduction |
| Compact-window neutral equation \(W_c k=0\) | conditional theorem |
| Fixed-window log-order operator + finite prime shifts | derived |
| Actual-zeta next-jet exclusion | open |
| Neutral null-extension rigidity | open |
| RH | open |

See [Proof status](docs/PROOF_STATUS.md) for precise hypotheses and scope.

## Zeta-facing branches currently identified

The prior zeta traversal explicitly produced the following negative and neutral branches. H1-P1.0 additionally identifies an abstract approximate-neutral critical case; whether that case is realizable in the zeta-Weil specialization is now an H1-P2/P3 question.

### Negative-persistence branch

A persistent negative direction produces a selected residue vector \(v\neq0\) with

\[
\mathbf 1^T v=0,
\]

hence

\[
R_v(z)
=
\sum_{\rho_j\in F}\frac{v_j}{z-\rho_j}
=
O(|z|^{-2}).
\]

After far-field control, the surviving compensation localizes to

\[
\mathcal N_v[\psi]
=
\sum_{\mu\notin F}^{\rm near}
m_\mu\psi(\mu)
\frac{H_v^{(m_\mu)}(\mu)}
{\Xi^{(m_\mu)}(\mu)}.
\]

The missing actual-zeta input is tracked as

\[
\texttt{AZ-NEXTJET-LOC}
\quad/\quad
\texttt{C-ACTUAL-KPH-FLOOR}.
\]

### Neutral branch

A compact-window neutral mode satisfies

\[
\boxed{W_c k=0}.
\]

At fixed support \(c\),

\[
\mathcal W_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n})
+
\mathcal R_{\rm pole},
\]

with principal symbol

\[
\Psi_c(t)=\log|t|+O_c(1).
\]

The remaining problem is tracked as

\[
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
\]

## Repository layout

- [Horizon 1](docs/HORIZON_1.md) — first finite research horizon and phase gates.
- [Abstract Defect Calculus](docs/ABSTRACT_DEFECT_CALCULUS.md) — H1-P1 zeta-independent operator theory.
- [Restricted-Channel Transfer](docs/RESTRICTED_CHANNEL_TRANSFER.md) — selected finite sectors, background budget, and shorting.
- [Terminology Registry](docs/TERMINOLOGY.md) — canonical project vocabulary.
- [Proof status](docs/PROOF_STATUS.md) — theorem-by-theorem standing.
- [Research map](docs/RESEARCH_MAP.md) — dependency graph and current frontier.
- [References](docs/REFERENCES.md) — background literature used by the program.
- [Initial consolidation](notes/WEIL_DEFECT_CONSOLIDATION_0_20260923.md) — first full consolidation checkpoint.

The public surface is intentionally conservative: theorem statements, hypotheses, open obligations, and provenance are kept separate.

## Background

The project sits in the lineage of work on Weil's criterion, finite truncations of the Weil quadratic form, compact-window positivity, and operator realizations of the explicit formula.

Particularly relevant references include:

- Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*.
- Recent work on certified compact-window Weil positivity and Landau--Widom-type spectral behavior.

## Public-status convention

- **PROVED** — established within the stated framework/hypotheses.
- **CONDITIONAL** — proved assuming an explicitly named hypothesis or branch condition.
- **DERIVED** — exact reformulation/reduction from retained inputs.
- **OPEN** — required for a later closure but not established.

No statement is promoted merely because it is repeatedly used or numerically supported.
