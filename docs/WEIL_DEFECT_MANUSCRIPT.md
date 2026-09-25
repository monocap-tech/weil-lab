# Weil-Defect Theory: Screening, Persistence, and Zeta-Weil Morphology

> Public technical manuscript — Horizon 1 working assembly.
>
> Mathematical statements in this manuscript are indexed by the stable
> `WD-Txx` identifiers.  Verification status is separate from mathematical
> standing; see the public verification matrix when assembled.

## Abstract

This manuscript develops an operator-theoretic defect calculus for indefinite
coefficient spaces, isolates the role of finite selected negative sectors
under monotone support filtrations, specializes the resulting structure to the
zeta-Weil setting, and classifies the remaining negative, neutral, and
noncompact defect morphologies.

The independent theory stops before the actual-zeta exclusion problem.  Its
purpose is to determine exactly what is forced by screening, finite-sector
compactness, divisor geometry, residue cancellation, and compact-window
explicit-formula structure, and to expose the additional statements that an
RH application would still require.

No open actual-zeta interface is assumed in order to prove the Horizon-1
morphology statements that reach it.

---

# Part I. Abstract Weil-defect calculus

## 1. Coefficient spaces, synthesis, and the physical defect

Introduce the positive/negative coefficient splitting, synthesis operator,
Krein signature, and the physical defect

```math
D=S_{+}S_{+}^{*}-S_{-}S_{-}^{*}.
```

Public theorem block: `WD-T01`–`WD-T05`.

### 1.1 Physical/coefficient sign transfer

[Assembly target: WD-T01.]

### 1.2 Contractive screening and reduced solutions

[Assembly targets: WD-T02–WD-T04.]

### 1.3 Rank-one specialization

[Assembly target: WD-T05.]

## 2. Positive truncation and selected/background custody

Explain monotone positive screening and why selected negativity survives
aggregation while aggregate negativity does not recover selected custody.

Public theorem block: `WD-T06`–`WD-T09`.

## 3. Background elimination and finite selected-sector inertia

Develop residual screening, sequential background consumption, finite-sector
singular-value inertia, shorted covariance, and finite positive shadows.

Public theorem block: `WD-T10`–`WD-T14`.

## 4. Support filtration and right-limit persistence

Define monotone support families, right-limit spaces, endpoint jumps, fixed
finite selected-sector compactness, the critical dichotomy, endpoint quotient
control, and boundary amplification.

Public theorem block: `WD-T15`–`WD-T19`.

### 4.1 Fixed-sector persistence principle

The public summary theorem produced by this part is:

```math
\boxed{
\text{fixed finite selected sector}
+
\text{critical/negative right approach}
\Longrightarrow
\text{nonzero nonpositive right-limit ray}.
}
```

### 4.2 Critical dichotomy

At criticality, strong recovery of the positive coefficient gives an attained
neutral limit; positive-coordinate mass loss can instead strengthen the limit
to strict negativity.

Sharpness witnesses: `WD-X05`, `WD-X06`.

---

# Part II. Zeta-Weil specialization

## 5. Pair geometry and finite Weil inertia

Introduce the critical/off-critical pair decomposition and its relation to the
abstract positive/negative coefficient channels.

Public theorem block: `WD-T20`–`WD-T23`.

Imported finite-inertia/multiplicity inputs remain explicitly identified.

## 6. Finite frequency rigidity and residue cancellation

Develop finite distinct-frequency independence, the finite Problem-1
noncompensation statement, pair-residue construction, and the zero-moment law.

Public theorem block: `WD-T24`–`WD-T26`.

The key selected residue identity is:

```math
\boxed{\mathbf 1^T v=0.}
```

## 7. Rational response, native compactness, and far-field order

From zero moment, derive inverse-square rational-response decay, attach the
native Problem-1 compactness input, and isolate finite-head approximation and
kernel-combination consequences.

Public theorem block: `WD-T27`–`WD-T31`, with `WD-T30` placed by role.

Sharpness witness: `WD-X07`.

## 8. Completed next-jet and compact-window arithmetic

Develop the completed next-jet representation, adaptive cocancellation limit,
finite prime-power translation structure, logarithmic compact-window order,
and the failure of any free positive-Sobolev upgrade.

Public theorem block: `WD-T32`–`WD-T36`.

---

# Part III. Defect morphology

## 9. Persistent negative morphology

Public composite: `WD-T37`.

Narrative chain:

```math
\text{persistent selected negative defect}
\Longrightarrow
\text{selected zero-moment source}
\Longrightarrow
O(|z|^{-2})\text{ far response}
\Longrightarrow
O((\log R)/R)\text{ far field}
\Longrightarrow
\text{weighted near next-jet morphology}.
```

The branch stops at `AZ-NEXTJET-LOC`.  The stronger
`C-ACTUAL-KPH-FLOOR` is a special-packet refinement, not an already-proved
conclusion.

## 10. Attained neutral morphology

Public composite: `WD-T38`.

An attained unit-gain neutral branch gives a carrier-identified compact-window
null mode, together with threshold-aware finite prime shifts and logarithmic
principal order.

The branch stops at `AZ-FIN-WEIL-NULL-EXTENSION`.

## 11. Noncompact and moving/background morphology

Public composite: `WD-T39`.

Keep distinct:

1. full-coordinate escape;
2. fixed selected-packet persistence;
3. unselected-background norm escape;
4. bounded weak/tail escape;
5. strong background compactness.

Sharpness witnesses: `WD-X05`, `WD-X06`.

---

# Part IV. Sharpness

## 12. What the hypotheses prevent

Consolidated examples: `WD-X01`–`WD-X07`.

Each example is interpreted only as a sharpness witness for a stated theorem
boundary.  None is used as a substitute for a proof-producing theorem.

---

# Part V. Verification and boundary

## 13. Mathematical standing versus formal verification

This section will summarize the public verification matrix.

The manuscript keeps separate:

```text
mathematical standing
Lean verification standing
external-source custody
RH-facing openness
```

In particular, `LEAN-CERTIFIED-FROM-IMPORTED-PREMISE` means that Lean
certifies the downstream deduction from an explicit premise, not the external
analytic theorem represented by that premise.

## 14. Outputs delivered to the actual-zeta boundary

The independent theory delivers three explicitly typed frontier obligations:

```text
AZ-NEXTJET-LOC
C-ACTUAL-KPH-FLOOR
AZ-FIN-WEIL-NULL-EXTENSION
```

These are described in the RH-interface appendix.  They are not theorem IDs
and are not counted among the results proved by Horizon 1.

## 15. Conclusion

The completed package will state what the Weil-defect theory establishes,
which hypotheses are sharp, how the zeta-Weil specialization reaches the
remaining interfaces, and exactly where responsibility passes from the
independent theory to actual-zeta analysis.

It will not claim RH closure.

---

# Appendices

## Appendix A. Stable theorem index

See `PUBLIC_THEOREM_INDEX.md` when assembled.

## Appendix B. Verification matrix

See `PUBLIC_VERIFICATION_MATRIX.md` when assembled.

## Appendix C. Dependency map

See `PUBLIC_DEPENDENCY_MAP.md` when assembled.

## Appendix D. Examples and sharpness

See `PUBLIC_EXAMPLES.md` when assembled.

## Appendix E. RH-facing interfaces

See `RH_INTERFACE_APPENDIX.md` when assembled.
