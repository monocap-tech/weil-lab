# Proof Status

This page is the compact status surface for Horizon 1.

The canonical theorem-by-theorem inventory is [Theorem Ledger](THEOREM_LEDGER.md).
The canonical dependency/source audit is [Dependency Audit](DEPENDENCY_AUDIT.md).

## Two-axis status model

A theorem now carries two independent statuses.

### Mathematical standing

- **INTERNAL-PROOF** — proof text exists in this repository under stated hypotheses.
- **DERIVED** — exact reduction/reformulation from retained inputs.
- **IMPORTED** — consumed from external literature.
- **CONDITIONAL** — depends on an explicitly named branch hypothesis.
- **EXAMPLE** — explicit sharpness/possibility construction.
- **SCOPE** — jurisdiction rule rather than an independent theorem.
- **OPEN** — downstream obligation not established.

### Verification status

- **P4-AUDIT-PENDING** — internal proof has not yet completed the Horizon-1 line-by-line audit.
- **P4-AUDIT-PASSED** — Horizon-1 internal audit passed after any recorded corrections; not independent certification.
- **SOURCE-PIN-PENDING** — the external source family is known, but exact theorem/equation pinning remains.
- **SOURCE-PINNED** — exact external theorem/equation and convention are fixed; internal consumption may still await audit.
- **COMPOSITE-AUDIT-PENDING** — morphology package still needs expanded dependency/hypothesis audit.
- **COMPOSITE-AUDIT-PASSED** — expanded dependency/hypothesis composition audit passed after any recorded corrections.
- **SCOPE-ONLY** — no proof certification is claimed.
- **EXAMPLE-AUDIT-PASSED** — example calculation and sharpness role passed the Horizon-1 internal examples audit.

The historical word **PROVED** in earlier files means internal proof standing. It does not mean independently certified or formally verified.

---

## Inventory

Current canonical IDs:

```math
\boxed{
\text{WD-T01 through WD-T39}
}
```

for theorem/reduction statements,

```math
\boxed{
\text{WD-X01 through WD-X07}
}
```

for examples/sharpness witnesses, and

```math
\boxed{
\text{WD-S01 through WD-S05}
}
```

for scope guards.

Historical labels such as WD-A1, ZW1-T7, or P3-N4 remain immutable aliases.

---

## Phase standing

| Phase | Status | Canonical package |
| --- | --- | --- |
| H1-P0 | COMPLETE | repository/terminology/custody setup |
| H1-P1 | COMPLETE | abstract defect calculus |
| H1-P2 | COMPLETE | zeta-Weil specialization |
| H1-P3 | COMPLETE | negative, neutral, and noncompact morphologies |
| H1-P4 | COMPLETE | theorem/source/proof audit |
| H1-P5 | PAUSED | public manuscript/package; resumes after LEAN-H1 exhaustion |

---

## Imported-source status

Exact pins are now complete in [Imported Source Pins](IMPORTED_SOURCE_PINS.md).

SOURCE-PINNED inputs:

1. Douglas factorization — WD-T02;
2. Bombieri finite Weil inertia/multiplicity/kernel estimates — WD-T22, WD-T23, WD-T28;
3. standard zeta zero counting — WD-T28, WD-T31;
4. compact-window geometric explicit formula — WD-T34, WD-T35;
5. digamma asymptotics — WD-T35.

Anderson–Trapp shorting and Suzuki's operator framework remain contextual/non-load-bearing for the current theorem statements.

---

## Composite morphology standing

### WD-T37 — Negative defect morphology

**Standing:** CONDITIONAL COMPOSITE.
**Verification:** COMPOSITE-AUDIT-PASSED.

Stops at:

```math
\boxed{
\texttt{AZ-NEXTJET-LOC}
}
```

with C-ACTUAL-KPH-FLOOR as a stronger special-packet interface.

### WD-T38 — Neutral defect morphology

**Standing:** CONDITIONAL COMPOSITE.
**Verification:** COMPOSITE-AUDIT-PASSED.

Stops at:

```math
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
```

### WD-T39 — Noncompact background morphology

**Standing:** INTERNAL/CONDITIONAL COMPOSITE.
**Verification:** COMPOSITE-AUDIT-PASSED.

Introduces no new RH-facing interface.

---

## Scope guards

The current audit prohibits the following silent transfers:

- unweighted sampling frames $\not\Rightarrow$ native Problem-1 coercivity;
- explicit-formula arithmetic terms are not extra positive screening budget;
- weighted next-jet localization $\not\Rightarrow$ source-free near-field lower bound;
- neutral equality $\not\Rightarrow$ termwise vanishing;
- background escape $\not\Rightarrow$ loss of an anchored selected ray;
- fixed finite packet criticality does not admit a third non-attained/no-limit branch.

---

## Open Horizon-1 interfaces

The following remain OPEN:

```math
\boxed{
\texttt{AZ-NEXTJET-LOC},
\qquad
\texttt{C-ACTUAL-KPH-FLOOR},
\qquad
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
```

PAP/MTP closure and RH are not proved by this repository.

## Internal theorem audit

WD-T01 through WD-T36 are now

```math
\boxed{
\text{P4-AUDIT-PASSED}.
}
```

See [Internal Proof Audit](INTERNAL_PROOF_AUDIT.md).

The composite morphology theorems WD-T37 through WD-T39 are COMPOSITE-AUDIT-PASSED.

See [Composite Morphology Audit](COMPOSITE_MORPHOLOGY_AUDIT.md).

## Examples and sharpness audit

WD-X01 through WD-X07 are now

```math
\boxed{
\text{EXAMPLE-AUDIT-PASSED}.
}
```

See [Examples and Sharpness Audit](EXAMPLES_SHARPNESS_AUDIT.md).

All H1-P4 audit classes are complete.

## Deferred post-LEAN cursor

The mathematical audit is complete, but public-package assembly is intentionally paused while LEAN-H1 is active. When the formalization exhaustion condition is met, work resumes at:

```math
\boxed{
\texttt{H1-P5.0 / PUBLIC PACKAGE ARCHITECTURE}
}
```


---

## Lean formalization priority

Formal certification now preempts H1-P5 public-package work.

Canonical control:

- [Lean Formalization Track](LEAN_FORMALIZATION_TRACK.md)
- [Lean Status Ledger](LEAN_STATUS.md)

Current formalization cursor:

```math
\boxed{
\texttt{LEAN-H1-P1 / WD-X06 — POSITIVE-COORDINATE MASS LOSS STRENGTHENS CRITICALITY TO NEGATIVITY}
}
```

WD-X05 is `LEAN-CERTIFIED`; the active sharpness-example cursor is WD-X06. See [Lean Status Ledger](LEAN_STATUS.md) for live certificate state.

H1-P5 resumes only after LEAN-H1 exhaustion.
