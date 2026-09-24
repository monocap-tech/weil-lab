# Dependency Audit
## H1-P4.0 — Theorem DAG, source boundaries, and audit debt

This document audits the architecture of the Horizon-1 theorem inventory without introducing new mathematical claims.

The canonical stable IDs are defined in [Theorem Ledger](THEOREM_LEDGER.md).

---

# 1. Normalized dependency DAG

## Abstract screening spine

\[
\boxed{
\text{WD-T01}
\longrightarrow
\text{WD-T02}
\longrightarrow
\begin{cases}
\text{WD-T03},\\
\text{WD-T04},\\
\text{WD-T05}.
\end{cases}
}
\]

Positive restoration is separately encoded by

\[
\boxed{
\text{WD-T06}.
}
\]

## Selected/background spine

\[
\boxed{
\text{WD-T07}
\longrightarrow
\begin{cases}
\text{WD-T08},\\
\text{WD-T09}
\end{cases}
}
\]

and

\[
\boxed{
\text{WD-T02}
+
\text{WD-T09}
\longrightarrow
\text{WD-T10}
\longrightarrow
\text{WD-T12}.
}
\]

The finite-sector spectral statement is

\[
\boxed{
\text{WD-T03}
\longrightarrow
\text{WD-T11}.
}
\]

Complement elimination and finite shadows are

\[
\boxed{
\text{WD-T13},
\qquad
\text{WD-T14}.
}
\]

## Support-filtration spine

\[
\boxed{
\text{WD-T15}
\longrightarrow
\begin{cases}
\text{WD-T16},\\
\text{WD-T17},\\
\text{WD-T18}.
\end{cases}
}
\]

Physical realization gives

\[
\boxed{
\text{WD-T16}
+
\text{physical realization hypotheses}
\longrightarrow
\text{WD-T19}.
}
\]

## Zeta-Weil pair spine

\[
\boxed{
\text{WD-T20}
\longrightarrow
\text{WD-T21}.
}
\]

Bombieri's imported finite inertia theorem supplies

\[
\boxed{
\text{WD-T22}.
}
\]

Multiplicity reduction is

\[
\boxed{
\text{WD-T23}.
}
\]

Finite exponential independence gives

\[
\boxed{
\text{WD-T24}
\longrightarrow
\text{WD-T25}.
}
\]

The selected residue chain is

\[
\boxed{
\text{WD-T20}
\longrightarrow
\text{WD-T26}
\longrightarrow
\text{WD-T27}.
}
\]

Native compact synthesis gives

\[
\boxed{
\text{WD-T28}
\longrightarrow
\text{WD-T29}.
}
\]

## Explicit-formula spine

Scalarization and far localization are

\[
\boxed{
\text{WD-T30}
+
\text{WD-T27}
\longrightarrow
\text{WD-T31}.
}
\]

The completed-\(\Xi\) representation is

\[
\boxed{
\text{WD-T32}.
}
\]

Explicit-formula co-adaptation is

\[
\boxed{
\text{WD-T33}.
}
\]

The compact-window neutral arithmetic chain is

\[
\boxed{
\text{WD-T34}
\longrightarrow
\text{WD-T35}
\longrightarrow
\text{WD-T36}.
}
\]

---

# 2. Morphology dependencies

## Negative morphology

\[
\boxed{
\begin{array}{c}
\text{WD-T16}\\
\downarrow\\
\text{WD-T19}\\
\downarrow\\
\text{WD-T07}\\
\downarrow\\
\text{WD-T26}\to\text{WD-T27}\\
\downarrow\\
\text{WD-T30}+\text{WD-T31}\\
\downarrow\\
\text{WD-T32}\\
\downarrow\\
\text{WD-T33}\\
\downarrow\\
\boxed{\text{WD-T37}}
\end{array}
}
\]

The downstream interface is

\[
\boxed{
\texttt{AZ-NEXTJET-LOC}.
}
\]

C-ACTUAL-KPH-FLOOR is a stronger special-packet interface and is not used to prove WD-T37.

## Neutral morphology

\[
\boxed{
\text{WD-T17}
+
\text{finite-exception unit-gain/physical-realization hypotheses}
\longrightarrow
\text{physical null mode}
}
\]

followed by

\[
\boxed{
\text{WD-T34}
\to
\text{WD-T35}
\to
\text{WD-T36}
\to
\boxed{\text{WD-T38}}.
}
\]

The downstream interface is

\[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
\]

No later boundary-trace, Stieltjes, or UCP diagnostic is consumed by WD-T38.

## Noncompact morphology

Moving selected-sector escape uses the compactness distinction encoded by

\[
\boxed{
\text{WD-T15},
\text{ WD-T16},
\text{ WD-T17}
}
\]

plus explicit examples such as WD-X05.

Unselected-background classification uses

\[
\boxed{
\text{WD-T07}
+
\text{WD-T14}
}
\]

and fixed selected-ray hypotheses inherited from WD-T37.

This packages as

\[
\boxed{
\text{WD-T39}.
}
\]

---

# 3. Imported-source boundary

Only a small subset of the theorem spine consumes external theorems as load-bearing inputs.

## EXT-1 — Douglas factorization theorem

Consumed by

\[
\boxed{
\text{WD-T02}.
}
\]

Downstream theorems WD-T03, WD-T10, and WD-T11 use the reduced screening solution produced in that framework.

**Audit debt:** pin the exact statement used: range inclusion / Loewner majorization / factorization equivalence and the reduced-solution normalization.

## EXT-2 — Bombieri finite Weil theory

Consumed directly by

\[
\boxed{
\text{WD-T22},
\qquad
\text{WD-T23}.
}
\]

Bombieri's kernel/column estimate is retained as corroborating context, but after P4.2 it is **not load-bearing** for WD-T28.

WD-T28 now uses an internal Dirichlet-resolvent estimate plus EXT-3 zero counting.

Exact source pins for the Bombieri finite-index and multiplicity statements are recorded in [Imported Source Pins](IMPORTED_SOURCE_PINS.md).

## EXT-3 — Standard zeta zero counting

Consumed in

\[
\boxed{
\text{WD-T28},
\qquad
\text{WD-T31}.
}
\]

**Audit debt:** choose one canonical zero-count statement and specify whether multiplicity is included.

## EXT-4 — Compact-window geometric explicit formula

Consumed in

\[
\boxed{
\text{WD-T34},
\qquad
\text{WD-T35}.
}
\]

**Audit debt:** pin the exact support convention for

\[
\log n<2c
\]

versus boundary equality, and pin the Fourier-normalization constants used by the operator form.

## EXT-5 — Digamma/Stirling asymptotic

Consumed in

\[
\boxed{
\text{WD-T35}.
}
\]

**Audit debt:** record a standard source/formula for

\[
\Re\psi\!\left(\frac14+\frac{it}{2}\right)
=
\log|t|+O(1).
\]

## EXT-6 — Anderson–Trapp shorting

Not required for the strictly positive Schur-complement proof of WD-T13.

It is background support for extending shorting beyond the invertible-block setting.

Therefore it is non-load-bearing for the current WD-T13 statement.

## EXT-7 — Suzuki operator framework

Contextual/background for the nonlocal operator species.

It is not load-bearing for WD-T34–WD-T38 as currently stated.

---

# 4. Source-free internal theorem boundary

The following stable theorem IDs have proofs contained in the current repository once standard Hilbert-space facts are admitted:

\[
\boxed{
\begin{gathered}
\text{WD-T01},\text{ T03--T19},\\
\text{WD-T20--T21},\text{ T24--T27},\\
\text{WD-T29--T33},\text{ T36}.
\end{gathered}
}
\]

This classification is architectural only.

It does not convert their verification status from P4-AUDIT-PENDING to independently verified.

---

# 5. Conditional boundary

The morphology statements are conditional because they begin from explicit branch hypotheses.

## WD-T37

Consumes:
- fixed finite selected packet;
- nonnegative endpoint selected space;
- normalized selected amplitude tending to zero;
- strictly negative normalized selected signature limit.

The theorem does not assert that such a branch exists for actual zeta.

## WD-T38

Consumes:
- fixed finite selected packet;
- attained rather than negative-fall-through critical alternative;
- finite-exception unit-gain relation;
- physical adjoint realization.

The theorem does not assert that every critical branch has these properties.

## WD-T39

Its background-stability/full-divisor statements are conditional on an already anchored fixed selected ray where stated.

The moving-sector compactness classification itself is unconditional Hilbert-space structure.

---

# 6. Scope-guard audit

The following forbidden transfers are now explicit.

### SG-1 — Metric transfer

Unweighted \(L^2/PW_t\) frame statements may not be promoted to native Problem-1 coercivity without an explicit comparison theorem.

### SG-2 — Double-counting arithmetic

Prime/pole/archimedean explicit-formula terms are not additional \(K_+\) coefficient channels.

### SG-3 — Near-field lower bound

Weighted next-jet localization does not imply a uniform source-free lower bound for the near field.

### SG-4 — Neutral termwise vanishing

\(Q_c(k)=0\) does not imply separate vanishing of pole, prime, and archimedean terms.

### SG-5 — Background custody

Unselected-background escape does not erase a fixed selected negative ray.

### SG-6 — Fixed-packet approximate neutrality

A non-attained critical morphology with no right-limit ray cannot occur inside one fixed finite selected sector.

---

# 7. Cycle audit

The normalized Horizon-1 theorem graph is acyclic.

The two open interfaces occur strictly downstream of the theorem packages:

\[
\text{WD-T37}
\longrightarrow
\texttt{AZ-NEXTJET-LOC},
\]

and

\[
\text{WD-T38}
\longrightarrow
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
\]

Neither interface is used upstream to prove the morphology theorem that reaches it.

The special-packet interface C-ACTUAL-KPH-FLOOR is likewise not imported into the generic WD-T37 chain.

This closes the principal circularity audit at the dependency-graph level.

---

# 8. P4 audit queue

The next audit passes should proceed in this order.

## P4.1 — Imported source pinning — COMPLETE

Exact pins are recorded in [Imported Source Pins](IMPORTED_SOURCE_PINS.md).

## P4.2 — Internal proof audit — COMPLETE

WD-T01 through WD-T36 are P4-AUDIT-PASSED at the internal Horizon-1 level.

Corrections and theorem-by-theorem findings are recorded in [Internal Proof Audit](INTERNAL_PROOF_AUDIT.md).

## P4.3 — Composite morphology audit

Check WD-T37 through WD-T39 by expanding every composite dependency and confirming that no branch hypothesis is silently strengthened.

## P4.4 — Examples and sharpness audit

Verify WD-X01 through WD-X07 and link each example to the theorem hypothesis/sharpness point it tests.

---

# 9. H1-P4.0 determination

The theorem inventory now has:

- stable additive public IDs;
- immutable historical aliases;
- a normalized DAG;
- explicit imported-source boundaries;
- explicit conditional branch boundaries;
- explicit scope guards;
- no dependency-cycle use of the RH-facing interfaces.

No mathematical theorem has been added in this pass.

## Next cursor

\[
\boxed{
\texttt{H1-P4.3 / COMPOSITE MORPHOLOGY AUDIT}
}
\]


---

# 10. P4.1 source-pin disposition

The following external inputs are now SOURCE-PINNED:

- Douglas (1966), Theorem 1;
- Bombieri (2000), Theorem 8;
- Bombieri (2000), Lemma 10;
- Bombieri (2000), equation (7.7) in the proof of Theorem 6;
- Titchmarsh (1986), Theorem 9.2 / equation (9.2.1);
- Zhu (2026), equations (2)–(3);
- DLMF 5.11.2.

Exact conventions are recorded in [Imported Source Pins](IMPORTED_SOURCE_PINS.md).

Source pinning does not complete the internal proof audit.


---

# 11. P4.2 internal-audit disposition

WD-T01 through WD-T36 are now P4-AUDIT-PASSED.

Five audit-level corrections were applied:

- WD-T13 uniformly positive Schur hypothesis;
- WD-T28 direct resolvent Hilbert–Schmidt proof;
- WD-T33 adaptive-multiplier quantifier restriction;
- WD-T35 compact-window domain and pole bound;
- WD-T36 no-positive-Sobolev-coercivity formulation.

See [Internal Proof Audit](INTERNAL_PROOF_AUDIT.md).

This status is internal audit only, not independent certification.
