# Weil Defect

A public research repository for a defect-theoretic analysis of **Weil's quadratic
form**, its finite negative-index structure, spectral screening, persistent
negative directions, and compact-window neutral modes.

> **Status:** Research program / theorem consolidation.
>
> **Scope:** This repository does not claim a proof of the Riemann Hypothesis.

## Scope and separation

The project separates two mathematical layers that must not be conflated:

- **Weil-defect theory:** finite negative index, screening, persistence,
  compact-window neutrality, and their operator-theoretic structure.
- **Actual-zeta exclusion:** the additional arithmetic input needed to rule out
  the remaining defect geometries for the actual zeta divisor.

The first layer can be developed and audited independently of the second. The
working architecture is

```math
\boxed{
\text{finite negative index}
\longrightarrow
\text{spectral screening / support filtration}
\longrightarrow
\begin{cases}
\text{fixed-packet negative persistence},\\
\text{fixed-packet attained-neutral persistence},\\
\text{moving/infinite-sector or background noncompactness}.
\end{cases}
}
```

Only after this defect geometry is isolated does the program ask whether the
**actual zeta divisor** can realize the remaining branches.

## Horizon 1

The repository is currently organized under
[Horizon 1 — Independent Weil-Defect Theory](docs/HORIZON_1.md). Its stop
boundary is deliberately before RH closure.

| Phase | Scope | Status |
| --- | --- | --- |
| H1-P0 | Consolidation and custody | Complete |
| H1-P1 | Abstract defect calculus | Complete |
| H1-P2 | Zeta-Weil specialization | Complete |
| H1-P3 | Defect morphology theorem | Complete |
| H1-P4 | Proof audit and theorem normalization | Complete |
| LEAN-H1 | Lean certification track | **Exhausted** |
| H1-P5 | Public mathematical package | Ready — not started |

Within H1-P4, source pinning, the internal proof audit, the composite
morphology audit, and the examples/sharpness audit are complete. The Lean certification track is exhausted. The next project cursor is
**H1-P5.0 / Public Package Architecture**, recorded but not started. Stable public theorem IDs and the
audit surfaces are canonical in the
[Theorem Ledger](docs/THEOREM_LEDGER.md),
[Dependency Audit](docs/DEPENDENCY_AUDIT.md),
[Imported Source Pins](docs/IMPORTED_SOURCE_PINS.md),
[Internal Proof Audit](docs/INTERNAL_PROOF_AUDIT.md), and
[Composite Morphology Audit](docs/COMPOSITE_MORPHOLOGY_AUDIT.md), and
[Examples and Sharpness Audit](docs/EXAMPLES_SHARPNESS_AUDIT.md).

Project terms such as **horizon**, **phase**, **standing**, **interface**,
**custody**, and **screening** are fixed in the
[Terminology Registry](docs/TERMINOLOGY.md).

Formal verification has reached its exhaustion condition. See the
[Lean Formalization Track](docs/LEAN_FORMALIZATION_TRACK.md) and
[Lean Status Ledger](docs/LEAN_STATUS.md). H1-P5.0 is next, but no public-package work has been started in this closure pass.

## Core mathematical picture

The abstract defect calculus is organized around

```math
D=S_{+}S_{+}^{*}-S_{-}S_{-}^{*},
```

with the sign problem reduced to contractive Douglas screening. For a fixed
finite selected negative sector, critical or negative right-approach forces a
nonzero nonpositive right-limit ray. Within that fixed-finite-sector right-limit setting, a genuinely nonpersistent **selected** approximate-neutral branch is excluded; selected-ray nonpersistence requires a moving/infinite selected sector. Unselected-background noncompactness is a separate later phenomenon: it can obstruct strong full-coefficient compactness after the selected ray is already anchored, but it does not erase that ray.

Under the zeta-Weil specialization, a selected residue vector satisfies

```math
\mathbf{1}^{T}v=0,
```

which forces

```math
R_{v}(z)=O(|z|^{-2}).
```

The explicit-formula attachment sharpens the far-field contribution to

```math
\mathcal{F}_{v,R}
=
O\!\left(\frac{\log R}{R}\right),
```

leaving a weighted completed $\Xi$ next-jet field as the negative-branch
arithmetic obstruction.

On the neutral branch, fixed compact support produces only finitely many
prime-power translations, with principal order

```math
\Psi_{c}(t)=\log|t|+O_{c}(1).
```

These statements are packaged in the negative, neutral, and noncompact
morphology documents linked below.

## Current theorem picture

| Component | Current standing |
| --- | --- |
| Finite Weil negative index | Imported theorem + exact specialization |
| Rank-one defect formulation | Derived |
| Critical-line tail monotonicity | Internal proof with stated inputs |
| Spectral screening distinction | Structural |
| Persistent normalized Weil negativity | Conditional theorem |
| Quartet zero-moment law | Internal proof in the selected quartet model |
| $O(\lvert z\rvert^{-2})$ far-field decay | Internal proof |
| Weighted next-jet localization | Internal reduction under stated source/multiplier hypotheses |
| Compact-window neutral equation $W_{c}k=0$ | Conditional theorem |
| Fixed-window log-order operator + finite prime shifts | Derived |
| Actual-zeta next-jet exclusion | Open |
| Neutral null-extension rigidity | Open |
| RH | Open |

See [Proof Status](docs/PROOF_STATUS.md) for precise hypotheses, mathematical
standing, and verification state.

## RH-facing interfaces

Horizon 1 deliberately stops before two primary actual-zeta interfaces, with one stronger special-packet refinement on the negative side:

- `AZ-NEXTJET-LOC` — control or exclusion of the weighted near next-jet field.
- `C-ACTUAL-KPH-FLOOR` — stronger special-packet KPH/transversality floor that can serve as a sufficient refinement of `AZ-NEXTJET-LOC` where its packet hypotheses apply.
- `AZ-FIN-WEIL-NULL-EXTENSION` — exterior support/null-extension rigidity for
  an actual compact-window neutral mode.

The negative morphology reaches the first interface after

```math
\mathbf{1}^{T}v=0
\quad\Longrightarrow\quad
R_{v}(z)=O(|z|^{-2})
\quad\Longrightarrow\quad
\mathcal{F}_{v,R}=O\!\left(\frac{\log R}{R}\right).
```

The neutral morphology reaches the third interface from the compact-window
equation

```math
W_{c}k=0.
```

These interfaces are downstream obligations; none is imported upstream to
prove the Horizon-1 morphology theorem that reaches it.

## Repository map

### Horizon and audit control

- [Horizon 1](docs/HORIZON_1.md) — phase gates and the Horizon-1 stop boundary.
- [Theorem Ledger](docs/THEOREM_LEDGER.md) — stable theorem IDs, standing,
  verification status, and historical aliases.
- [Dependency Audit](docs/DEPENDENCY_AUDIT.md) — normalized theorem DAG,
  imported-source boundaries, scope guards, and audit queue.
- [Imported Source Pins](docs/IMPORTED_SOURCE_PINS.md) — exact load-bearing
  external statements, equation locations, and convention map.
- [Proof Status](docs/PROOF_STATUS.md) — compact theorem and phase status.
- [Terminology Registry](docs/TERMINOLOGY.md) — canonical project vocabulary.
- [Research Map](docs/RESEARCH_MAP.md) — dependency graph and current frontier.
- [References](docs/REFERENCES.md) — background literature used by the program.

### H1-P1 — Abstract defect calculus

- [Abstract Defect Calculus](docs/ABSTRACT_DEFECT_CALCULUS.md) — zeta-independent
  operator theory.
- [Restricted-Channel Transfer](docs/RESTRICTED_CHANNEL_TRANSFER.md) — selected
  finite sectors, background budget, and shorting.
- [Support Filtration and Persistence](docs/SUPPORT_FILTRATION_PERSISTENCE.md) —
  right limits, endpoint jumps, representative blow-up, and moving-sector
  escape.

### H1-P2 — Zeta-Weil specialization

- [Zeta-Weil Specialization Map](docs/ZETA_WEIL_SPECIALIZATION_MAP.md) — mapping
  from abstract carriers to Weil/divisor/arithmetic structure.
- [Quartet Channel and Residue Structure](docs/QUARTET_CHANNEL_RESIDUE_STRUCTURE.md)
  — pair geometry, finite inertia, zero moments, and compact synthesis.
- [Explicit-Formula Arithmetic Attachment](docs/EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md)
  — far-tail localization, completed $\Xi$ next jets, finite prime shifts, and
  logarithmic form order.

### H1-P3 — Defect morphology

- [Negative Defect Morphology Theorem](docs/NEGATIVE_DEFECT_MORPHOLOGY.md) —
  fixed-packet negative endpoint morphology and stop line.
- [Neutral Defect Morphology Theorem](docs/NEUTRAL_DEFECT_MORPHOLOGY.md) —
  attained-neutral null mode, logarithmic operator, and null-extension stop
  line.
- [Noncompact Background Morphology Theorem](docs/NONCOMPACT_BACKGROUND_MORPHOLOGY.md)
  — moving selected escape, background escape, and fixed full-divisor negative weak
  limits.

### Consolidation record

- [Initial Consolidation](notes/WEIL_DEFECT_CONSOLIDATION_0_20260923.md) — first
  full public consolidation checkpoint.

## Background

The project sits in the lineage of work on Weil's criterion, finite truncations
of the Weil quadratic form, compact-window positivity, and operator
realizations of the explicit formula.

Particularly relevant references include:

- Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of
  prime numbers, I*.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*.
- Recent work on certified compact-window Weil positivity and
  Landau–Widom-type spectral behavior.

See [References](docs/REFERENCES.md) for the repository's source list.

## Verification convention

The project separates **mathematical standing** from **verification status**.
An internal proof under stated hypotheses is not, by that fact alone,
independently certified or formally verified.

A stable theorem ID is a name, not a certification mark. Verification claims
are promoted only by an explicit later audit or certificate artifact.
