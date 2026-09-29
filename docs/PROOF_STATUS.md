# Proof Status

This page is the compact status surface for Horizon 1.

The canonical theorem-by-theorem inventory is [Theorem Ledger](THEOREM_LEDGER.md).
The canonical dependency/source audit is [Dependency Audit](DEPENDENCY_AUDIT.md).

## Status model

At the H1-P4 documentation layer, a theorem carries two independent classifications: **mathematical standing** and **audit/source verification status**. LEAN-H1 adds a third, separate **formal-certification status**, recorded in [Lean Status](LEAN_STATUS.md). None of these axes should be inferred from another.

### Mathematical standing

- **INTERNAL-PROOF** — proof text exists in this repository under stated hypotheses.
- **DERIVED** — exact reduction/reformulation from retained inputs.
- **IMPORTED** — consumed from external literature.
- **CONDITIONAL** — depends on an explicitly named branch hypothesis.
- **EXAMPLE** — explicit sharpness/possibility construction.
- **SCOPE** — jurisdiction rule rather than an independent theorem.
- **OPEN** — downstream obligation not established.

### H1-P4 audit/source verification status

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
\text{WD-T01 through WD-T40}
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
| H1-P5 | COMPLETE | public manuscript/package and final package audit |

---

## Imported-source status

Exact pins are now complete in [Imported Source Pins](IMPORTED_SOURCE_PINS.md).

SOURCE-PINNED inputs:

1. Douglas factorization — WD-T02;
2. Bombieri finite Weil inertia/multiplicity/kernel estimates — WD-T22, WD-T23, WD-T28;
3. standard zeta zero counting — WD-T28, WD-T31;
4. compact-window geometric explicit formula — WD-T34, WD-T35, WD-T38, WD-T40;
5. digamma asymptotics — WD-T35, WD-T40.

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

Historically stopped at:

```math
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
```

That interface is now discharged negatively by WD-T40.

### WD-T40 — Gaussian support-gap null-extension exclusion

**Standing:** INTERNAL-PROOF / CONDITIONAL on WD-T38 carrier hypotheses.
**Verification:** P4-AUDIT-PASSED.

Concludes:

```math
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}
\text{ is discharged negatively.}
}
```



**Formalization:** LEAN-BLOCKED after RPB-67. The exact blocker is the missing
physical real-line Fourier/distribution carrier lift, followed by the
project-local Gaussian support-gap and strip-holomorphy stack. A completed
faithful formalization is expected to be
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE unless EXT-4/EXT-5 are reconstructed.

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

## Horizon-1 interface status

The remaining primary open stop-line interface is:

```math
\boxed{
\texttt{AZ-NEXTJET-LOC}.
}
```

`C-ACTUAL-KPH-FLOOR` also remains open as a stronger special-packet sufficient refinement of the negative interface.

The neutral interface

```text
AZ-FIN-WEIL-NULL-EXTENSION
```

is **DISCHARGED NEGATIVELY** by WD-T40 under the WD-T38 carrier hypotheses.

PAP/MTP closure and RH are not proved by this repository.

## Internal theorem audit

WD-T01 through WD-T36 are now

```math
\boxed{
\text{P4-AUDIT-PASSED}.
}
```

See [Internal Proof Audit](INTERNAL_PROOF_AUDIT.md).

The composite morphology theorems WD-T37 through WD-T39 are COMPOSITE-AUDIT-PASSED. WD-T40 is P4-AUDIT-PASSED.

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

## Next project cursor

The post-Horizon RPB promotion audit has added WD-T40. The next research cursor is:

```math
\boxed{
\texttt{RPB-75 / WD-T40 F-1 BUILD EXECUTION GATE}
}
```


---

## Lean formalization closure

Formal certification no longer preempts H1-P5: the LEAN-H1 gate has been satisfied. This status transition records readiness only; it does not itself start public-package work.

Canonical control:

- [Lean Formalization Track](LEAN_FORMALIZATION_TRACK.md)
- [Lean Status Ledger](LEAN_STATUS.md)

Current formalization cursor:

```math
\boxed{
\texttt{LEAN-H1 EXHAUSTED}
}
```

WD-X06 is `LEAN-CERTIFIED`; all stable Horizon-1 theorem/example rows now have durable final Lean states. See [Lean Status Ledger](LEAN_STATUS.md) for certificate evidence.

H1-P5.0 through H1-P5.5 are complete. The post-WD-T40 package revalidation also passed; see [Public Package Audit](PUBLIC_PACKAGE_AUDIT.md). **Horizon 1 is complete.** The next post-Horizon research cursor is RPB-69 / WD-T40 physical Fourier carrier build certification.
