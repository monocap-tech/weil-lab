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
\text{H1-P1 COMPLETE}
\qquad
\text{H1-P2 COMPLETE}
\qquad
\text{H1-P3 ACTIVE}.
}
\]

Project terms such as **horizon**, **phase**, **standing**, **interface**, **custody**, and **screening** are fixed in the [Terminology Registry](docs/TERMINOLOGY.md).

H1-P1 is now complete. Its three abstract layers are [Abstract Defect Calculus](docs/ABSTRACT_DEFECT_CALCULUS.md), [Restricted-Channel Transfer](docs/RESTRICTED_CHANNEL_TRANSFER.md), and [Support Filtration and Persistence Limits](docs/SUPPORT_FILTRATION_PERSISTENCE.md).

The central operator is

\[
D=S_+S_+^*-S_-S_-^*,
\]

and the sign problem is equivalent to contractive Douglas screening.

For a fixed finite selected negative sector, the support-filtration analysis further shows that critical or negative right-approaching sequences force a nonzero nonpositive right-limit ray. Therefore genuinely nonpersistent approximate neutrality requires an infinite or moving-sector mechanism.

The project has now entered **H1-P2: Zeta-Weil specialization**. The first mapping pass is complete; see [Zeta-Weil Specialization Map](docs/ZETA_WEIL_SPECIALIZATION_MAP.md).

The specialization separates generic screening theory from three zeta-facing layers: Weil/Krein pair geometry, zeta-divisor structure, and explicit-formula arithmetic.

H1-P2 is now complete.

The zero-side specialization gives the selected residue zero-moment law

[
mathbf1^Tv=0,
]

which forces

[
R_v(z)=O(|z|^{-2}).
]

The explicit-formula attachment sharpens this to the quantitative far-tail estimate

[
mathcal F_{v,R}
=
O((log R)/R),
]

leaving the weighted completed-(Xi) next-jet field as the exact negative-branch arithmetic obstruction.

On the neutral branch, fixed compact support yields finitely many prime translations and logarithmic principal order

[
Psi_c(t)=log|t|+O_c(1).
]

The project has now entered **H1-P3: defect morphology theorem**.

H1-P3.0 is complete: the negative branch is packaged in [Negative Defect Morphology Theorem](docs/NEGATIVE_DEFECT_MORPHOLOGY.md). It isolates the exact endpoint-jump, normalized-negativity, zero-moment, far-tail, and next-jet morphology without assuming the downstream actual-zeta exclusion.

H1-P3.1 is also complete: [Neutral Defect Morphology Theorem](docs/NEUTRAL_DEFECT_MORPHOLOGY.md) packages the attained-neutral branch as a physical compact-window Weil null mode governed by a logarithmic-order operator plus finitely many arithmetic translations, with the support question left open.

H1-P3.2 completes the morphology phase: [Noncompact Background Morphology Theorem](docs/NONCOMPACT_BACKGROUND_MORPHOLOGY.md) separates moving selected-sector escape from unselected-background escape and from fixed full-divisor convergence.

The project is now in **H1-P4: proof audit and theorem normalization**.

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

The prior zeta traversal explicitly produced the following negative and neutral branches. H1-P2.0 now sharpens the abstract approximate-neutral issue: for one fixed finite selected packet, critical right-approach already forces an actual nonpositive persistent ray. Nonpersistent approximate neutrality can remain only through moving packets or infinite-background escape.

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
- [Support Filtration and Persistence](docs/SUPPORT_FILTRATION_PERSISTENCE.md) — right limits, endpoint jumps, and representative blow-up.
- [Zeta-Weil Specialization Map](docs/ZETA_WEIL_SPECIALIZATION_MAP.md) — exact mapping from abstract carriers to the zero-side and arithmetic layers.
- [Quartet Channel and Residue Structure](docs/QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) — canonical pair geometry, finite inertia, zero moments, and compact synthesis.
- [Explicit-Formula Arithmetic Attachment](docs/EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) — far-tail localization, completed-Ξ next jets, finite prime shifts, and logarithmic form order.
- [Negative Defect Morphology Theorem](docs/NEGATIVE_DEFECT_MORPHOLOGY.md) — packaged fixed-packet negative endpoint morphology and stop line.
- [Neutral Defect Morphology Theorem](docs/NEUTRAL_DEFECT_MORPHOLOGY.md) — attained-neutral null mode, logarithmic operator, and null-extension stop line.
- [Noncompact Background Morphology Theorem](docs/NONCOMPACT_BACKGROUND_MORPHOLOGY.md) — moving selected escape, background escape, and fixed full-divisor convergence.
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
