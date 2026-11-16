# NF563 — Repair the exact original NF550 weighted-square identity and establish the first genuine oscillator→dual root

**2026-11-16 PT. Draft stacked on NF562 PR #590. New source-specific mathematics and compiler repairs COMMITTED; NF563 Lean verification PENDING. No unconditional original generator independence, unconditional canonical Gram strict positivity, signed Weil certificate, W_ODD_NEG or RH claim.**

## 1. Actual preceding compiler boundary

The complete NF561 original physical source-chain run `43976006178`, job `133680034578`, passed the original NF546→NF549 modules. It specifically reports

```
Built WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramPhysicalIntegral
```

under pinned Lean 4.34.0. Therefore genuine original J242 physical L², canonical even two-collar cutoff, smooth 242-source synthesis, and the exact NF549 continuous physical Gram integral are accepted within this dependent build.

The same compiler job subsequently **FAILED** in

```
WeilDefect/Arithmetic/ActualZetaOriginalCanonicalGramWeightedSquare.lean
```

and the latest error log identifies a collection of *source-level proof gaps in the implementation*, not a mathematical inconsistency:

1. The a.e. sum of 242 L² representatives is a `Finset.sum` in the function space, whereas the expected theorem was pointwise `fun x => Σ_i...`. The missing `Finset.sum_apply` conversion also left an unnormalized `Pi.basisFun.equivFun` coefficient.
2. The collar support argument contained `dsimp` tactics with nothing left to simplify.
3. A conjugation/norm rewrite was aimed at a different subterm. The correct real identity is `Complex.normSq_eq_conj_mul_self` followed by `Complex.normSq_eq_norm_sq`, together with associativity of multiplication by the fixed cutoff χ.
4. The inner-product integrand needs `RCLike.inner_apply` to reduce it to the actual complex scalar formula.
5. `fun_prop` could not discover the previously accepted `neutralNF546OriginalComplexGenerator_continuous` lemma. The correct original finite sum continuity uses `continuous_finsetSum` and the explicit genuine source continuity of each term.
6. One complex coercion proof referred to an unqualified `ofReal_mul`, rather than Mathlib's `Complex.ofReal_mul`; this broke the subsequent real-integral rewrite.

NF563 commits targeted repairs to all six sites in **the exact genuine original NF550 source**. It preserves the physical window `[-11/10,11/10]`, the actual NF548 even two-collar cutoff χ, all 242 source generators, the unchanged Schwartz synthesis, original complex coefficients, the complete physical continuous integral, and the original Gram. These are **candidate Lean repairs**, not accepted until CI reports success.

NF550's exact mathematical goal remains

```
Σ_(i<242) conj(d_i) Gχ(d)_i
  = ∫_(x:ℝ) χ(x) · ‖Σ_(j<242) d_j j_j(x)‖² dx
```

with complex-to-real coercions interpreted precisely. The right-hand side is nonnegative because χ is real nonnegative. **Strict positivity** still depends on global original source independence, and is NOT established by the weighted-square integral identity alone.

## 2. First genuine positive-source oscillator-to-dual polynomial identity

NF562 initiated full source-indexed all-order trigonometric derivative formulas, but NF563 also isolates the most immediate *actual* source-to-polynomial bridge for monomial order k=0. This new proof is independent of arbitrary degree-k product simplification, although it imports the generic NF561 sine jet (which itself is still awaiting corrected compiler acceptance).

New file:

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242FirstSineOddJetDual.lean
```

Let `a : Fin 242→ℝ` be the genuine original odd-jet left-kernel coefficient vector. Define its exact signed dual

```
p_a(T) = Σ_(n=0..241) (-1)^n a_n T^n.
```

For any real angular frequency `ω`, the polynomial power identity is

```
Σ_(n<242) a_n (-1)^n ω^(2n+1) = ω p_a(ω²).
```

Using the genuine higher derivative theorem for `sin(ωx)`:

```
Σ_(n<242) a_n
 [D^(2n+1) sin(ωx)]_(x=0)
  = ω p_a(ω²).
```

The source-specific theorem then states the above with the LHS literally `nf545OriginalSelectedRealGenerator ⟨i.val,...⟩`, whenever the actual original NF407 oscillator index `i : Fin 241` has its **authentic monomial order k_i=0**. Because the 67 source blocks are historical contiguous lists `k=0,...,m_f−1` and all lengths are positive, this statement applies to the zero-order sine column in each of the 67 original frequency groups (the index-of-block proof remains to be assembled). No substituted frequency or artificial sine generator is used.

The module also instantiates the first **actual** source index explicitly:

```
nf545OriginalOscillatorNodeAt 0 = (37/64, 0),
ω₀=2π·37/64 > 0.
```

Its true analytic odd-derivative source-left-kernel equation is

```
Σ_(n<242) a_n [D^(2n+1) j_0](0)
    = ω₀ p_a(ω₀²).
```

Therefore if the original 242x242 odd-jet matrix has the first oscillator's left-kernel column relation equal to zero, it forces the **first genuine positive squared-frequency root**

```
p_a((2π·37/64)²)=0.
```

No degree/root budget argument or original source independence is assumed. All theorems are actual Lean **candidate proofs, pending compiler acceptance**.

This is an explicit example of connecting the **analytic original oscillator** to the **signed dual polynomial**. It is not yet the full relation for the other 240 oscillator columns, and in particular not yet the derivative-of-frequency order k>0 correspondence.

## 3. New verification architecture

NF563 workflow `.github/workflows/nf563-original-first-oscillator-dual-and-weighted-square.yml` separately tests:

- the actual original 37/64, k=0 sine generator, all original k=0 columns under their literal order condition, the exact 242-row polynomial evaluation, and the true first positive-squared-frequency root;
- genuine full physical NF546–NF549 source compiler chain plus repaired NF550 canonical weighted-square module and downstream NF550 separation / NF551 local-global analytic identity;
- exact SHA-pinned original NF554 all 58,564 original oscillator plus genuine sinh pole coefficient comparisons.

No new `axiom`, `sorry`, or `admit` is introduced in the new first oscillator file. Existing original source custodial SHA checks remain intact.

## 4. Independent generic oscillator compiler status

NF561 initial trigonometric/Leibniz standalone Lean **FAILED** at run `43976006178`, job `133680034759`. Its errors concerned bad `mul_comm` simplification of `2n`, missing real-field type parameter in `iteratedDeriv_fun_pow_zero`, and missing `ContDiff` notation scope. NF562 committed targeted exact fixes and parity/factorial-ratio results, but their latest standalone compiler jobs remain queued; hence neither NF562 nor the new NF563 oscillator step is currently accepted.

NF561 original pole source job **FAILED** at NF559 power-rewrite orientation; NF562 also committed a correction, with acceptance pending. The true NF560 sinh analytic derivative theorem therefore remains compiler pending.

The already accepted independent algebraic infrastructure is NF553 degree obstruction, NF554 Hermite derivative root multiplicity, NF555 quadratic factorization/cofactor, and NF556 exact positive-frequency squared-root multiplicity equality. None of these accepted results by themselves proves independence of the 242 original analytic generators.

## 5. Full remaining independence and RH boundary

The finite original source task remains:

1. Compile NF562/NF563 authentic odd-derivative theorems, including original sinh pole and all k=0/k>0 oscillator columns.
2. Prove source-specific analytic odd-jet left-kernel identities for **all** `k<m_f`: `Σ_n a_n j_(f,k)^(2n+1)(0) = (-1)^floor(k/2) D_ω^k[ω p_a(ω²)]|_(ω=2πf)`.
3. Combine NF554 and NF556 multiplicity transfer at 67 distinct positive squared real frequencies with the exact genuine `-1/4` sinh pole, yielding an original 68-node root budget of 242, and formalize simultaneous root-factor divisibility.
4. Apply the accepted NF553 degree obstruction, NF558 coefficient injectivity, and the square 242x242 matrix left-to-right kernel transfer for **real** coefficients; then use real/imaginary decomposition to prove **original complex source global independence**.
5. Connect that theorem to the actual NF551 local-global collar identity and original NF550 physical weighted-square Gram to remove the outstanding independence premise and obtain unconditional strict positivity, after full compiler acceptance of both modules.

The real-valuedness/conjugation-equivariance of correction for real original data is a separate open gate.

NF528 authentic positive/negative all-multiplicity divisor graph convergence, NF527 original complete 1/10 gamma+prime n=9+both poles coercivity, NF539 signed Weil source identity, W_ODD_NEG and RH remain **OPEN**.

**NF564 target:** repair any actual NF563 CI errors in weighted-square proof, genuine source k=0 dual polynomial and new oscillator derivatives; then generalize the oscillator source-to-dual bridge to arbitrary monomial order `k` and build the 68-node simultaneous multiplicity contradiction in Lean.
