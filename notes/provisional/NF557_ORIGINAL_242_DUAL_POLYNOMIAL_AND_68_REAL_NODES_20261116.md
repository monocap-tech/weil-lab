# NF557 — Actual 242-dimensional dual polynomial and exact original 68-node source certificate

**2026-11-16 PT. Draft stacked on NF556 PR #584. New NF557 Lean source module and focused CI committed; new verification pending. No unconditional original J242 independence / canonical Gram or RH claim.**

## 1. Newly accepted generic Lean theorem

NF556's new standalone original odd-dual quadratic theorem is **LEAN PASS**, GitHub run `43967237428`, job `133649771451`. For every real nonzero polynomial `p` and positive `ω`, it formalizes

```
rootMultiplicity ω (X * p.comp (X^2))
  = rootMultiplicity (ω^2) p.
```

This is a genuine proved Mathlib-based algebraic result. It consumes NF555's previously accepted square-factor/cofactor lemmas and NF554's accepted generic derivative-multiplicity theorem. It is **generic**; not an unconditional original generator-independence theorem.

NF556's separate *real original NF546→NF551 source-chain compiler job* was still executing at this report's latest check. Its final result is not inferred from the standalone success. The NF548 canonical even cutoff repair was committed in NF556 and awaits source-chain acceptance.

## 2. Replace an abstract dual polynomial with the ORIGINAL concrete 242-dimensional object

Define for the 242 real coefficients `a : Fin 242 → ℝ`:

```
p_a(T) = Σ_(n : Fin 242) (-1)^n a_n T^n.
```

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242DualPolynomialSourceNodes.lean` implements this exact polynomial, with no reindexing or numerical surrogate, and a candidate polynomial degree proof

```
neutralNF557OriginalDualPolynomial_natDegree_lt :
   (p_a).natDegree < 242.
```

This is the true left-kernel dual polynomial of the **odd** derivative matrix at orders `1,3,...,483`; it is not a free polynomial chosen to dodge the source.

The coefficient-injectivity lemma `p_a=0 → a=0` remains to be compiled. It follows by uniqueness of polynomial monomial coefficients, but NF557 does not pretend that step is yet formalized.

## 3. Exact original 67 oscillator normalized square nodes

The NF545 Lean source table is a frozen, exact list of 67 positive rational `(f,m_f)` blocks, 241 oscillator monomial rows, and the separate original true index-241 `sinh(x/2)` pole. NF557 now defines

```
nf557RationalSquareNodes = [(f^2) | (f,m_f) in original groups].
```

The new Lean source candidates establish:

- **67** normalized squared-frequency nodes;
- **all 67 rational squares strictly positive**;
- **all 67 pairwise distinct** by exact rational decision, without approximating `π`;
- pole source label `-1/4` cannot coincide with any positive rational square;
- the **true real squared nodes** `4π² f² = (2π)² f²` remain distinct after injective scaling by nonzero `(2π)²`;
- the original total Hermite multiplicity is exactly `Σ_f m_f + 1 = 241+1=242`.

These are source-specific implementations, not merely generic claims about an arbitrary 67-node set. Their new pinned Lean compilation is pending.

The true negative pole node `-1/4` is still distinguished by sign from all positive real oscillator squares. There is no new frequency chosen, no replacement sinh pole, and no off-source lower-dimensional Gram.

## 4. Endgame after these source certificates

The source-specific left-kernel argument will then read:

1. For `a : Fin 242→ℝ`, define the concrete `p_a` as above.
2. From `a^T A=0` for the true 242×242 original odd initial derivative matrix, show for each original `(f,m_f)` that the first `m_f` derivatives of `F_a(X)=X*p_a(X²)` vanish at `ω_f=2πf`, and that `p_a(-1/4)=0`. **This actual derivative bridge remains OPEN in Lean.**
3. NF554's accepted Hermite derivative theorem gives `rootMultiplicity ω_f F_a≥m_f`; NF556's **accepted** exact quadratic theorem transfers this to `rootMultiplicity (ω_f²) p_a≥m_f`, if `p_a≠0`.
4. The new source-specific rational/real node facts make the 68 nodes distinct, with total required multiplicity `242`. Prove their polynomial root factors simultaneously divide `p_a` (or use a multiset root-count degree bound) — **OPEN in Lean**.
5. NF553's accepted degree contradiction and the new `natDegree p_a <242` force `p_a=0`; coefficient injectivity gives `a=0`.
6. By square finite-matrix rank and real/imaginary decomposition, infer global independence of the **original complex** 242 generators; then use NF551 local/global identity and NF550 canonical positive weighted square, **once those exact source modules compile**.

The finite **left-kernel** orientation is deliberate: the odd-source relations are in the **right** kernel. For a real square matrix, left-kernel triviality implies invertibility; formalizing this rank transfer is a separate obligation. The previous audits should not be mistaken for that Lean proof.

## 5. CI and non-transfer

New workflow `.github/workflows/nf557-original-dual-polynomial-nodes.yml` independently compiles the actual-source NF557 module, checks for proof placeholders, and replays the immutable NF407 67-block source and complete NF554 58,564-entry original dual derivative audit.

**NF557 new proof compiler acceptance pending.** No original-source independence axiom introduced.

Original NF528 all-multiplicity positive/negative divisor graph convergence, NF527 full 1/10 gamma+prime n=9+both poles coercivity, NF539 signed identity, REAL-conjugation correction, W_ODD_NEG and RH **OPEN**.

## 6. NF558 target

Obtain focused compilation of the NF557 source-specific squared-node and dual degree proofs, and check the upstream NF548→NF551 compiler diagnostics. Then formalize the polynomial coefficient-injectivity lemma and the original 242 odd-jet source-derivative-to-polynomial bridge. No substitute determinant or generic independence assumption.
