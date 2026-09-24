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
- **SOURCE-PIN-PENDING** — the external source family is known, but exact theorem/equation pinning remains.
- **COMPOSITE-AUDIT-PENDING** — morphology package still needs expanded dependency/hypothesis audit.
- **SCOPE-ONLY** — no proof certification is claimed.

The historical word **PROVED** in earlier files means internal proof standing. It does not mean independently certified or formally verified.

---

## Inventory

Current canonical IDs:

\[
\boxed{
\text{WD-T01 through WD-T39}
}
\]

for theorem/reduction statements,

\[
\boxed{
\text{WD-X01 through WD-X07}
}
\]

for examples/sharpness witnesses, and

\[
\boxed{
\text{WD-S01 through WD-S05}
}
\]

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
| H1-P4 | ACTIVE | theorem/source/proof audit |
| H1-P5 | PENDING | public manuscript/package |

---

## Imported-source audit queue

The load-bearing external inputs currently awaiting exact source pinning are:

1. Douglas factorization — WD-T02;
2. Bombieri finite Weil inertia/multiplicity/kernel estimates — WD-T22, WD-T23, WD-T28;
3. standard zeta zero counting — WD-T28, WD-T31;
4. compact-window geometric explicit formula — WD-T34, WD-T35;
5. digamma/Stirling asymptotics — WD-T35.

Anderson–Trapp shorting and Suzuki's operator framework are contextual/non-load-bearing for the current theorem statements.

---

## Composite morphology standing

### WD-T37 — Negative defect morphology

**Standing:** CONDITIONAL COMPOSITE.  
**Verification:** COMPOSITE-AUDIT-PENDING.

Stops at:

\[
\boxed{
\texttt{AZ-NEXTJET-LOC}
}
\]

with C-ACTUAL-KPH-FLOOR as a stronger special-packet interface.

### WD-T38 — Neutral defect morphology

**Standing:** CONDITIONAL COMPOSITE.  
**Verification:** COMPOSITE-AUDIT-PENDING.

Stops at:

\[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
\]

### WD-T39 — Noncompact background morphology

**Standing:** INTERNAL/CONDITIONAL COMPOSITE.  
**Verification:** COMPOSITE-AUDIT-PENDING.

Introduces no new RH-facing interface.

---

## Scope guards

The current audit prohibits the following silent transfers:

- unweighted sampling frames \(\not\Rightarrow\) native Problem-1 coercivity;
- explicit-formula arithmetic terms are not extra positive screening budget;
- weighted next-jet localization \(\not\Rightarrow\) source-free near-field lower bound;
- neutral equality \(\not\Rightarrow\) termwise vanishing;
- background escape \(\not\Rightarrow\) loss of an anchored selected ray;
- fixed finite packet criticality does not admit a third non-attained/no-limit branch.

---

## Open Horizon-1 interfaces

The following remain OPEN:

\[
\boxed{
\texttt{AZ-NEXTJET-LOC},
\qquad
\texttt{C-ACTUAL-KPH-FLOOR},
\qquad
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
\]

PAP/MTP closure and RH are not proved by this repository.

## Current audit cursor

\[
\boxed{
\texttt{H1-P4.1 / IMPORTED SOURCE PINNING}
}
\]
