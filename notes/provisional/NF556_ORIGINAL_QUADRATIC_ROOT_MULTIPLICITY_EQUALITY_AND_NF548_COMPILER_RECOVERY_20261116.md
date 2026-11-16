# NF556 — Exact quadratic odd-dual root multiplicity in Lean and NF548 compiler recovery

**2026-11-16 PT. Draft stacked on NF555 PR #583. The new source-independent quadratic root-multiplicity theorem and the NF548 repairs are committed but are NOT Lean accepted until focused CI passes. Source-graph, Weil sign, W_ODD_NEG and RH remain open.**

## 1. Compiler audit (actual observations)

NF555 PR #583 brought two new verifications:

- `nf555-standalone-quadratic-lean`, run `43965276132`, job `133642962114`: **LEAN PASS**, proving the exact polynomial square-node factorization, the substitution-factorization of `X*p(X²)`, and the nonzero cofactor at positive original oscillator frequencies.
- `nf555-symbolic-actual-source-quadratic-audit`, same run, job `133642961978`: **PASS**, preserving the original NF407 SHA/frequency/multiplicity custody and checking 308 exact symbolic coefficients over `ℚ[X,Z]` with `Z` an indeterminate for π.

The genuine original NF547 source smoothness repair is also now accepted *within the NF555 source-chain job*: the latest failure moved **forward** to `ActualZetaOriginalCanonicalEvenCollarCutoff.lean` (NF548), run `43965276132`, job `133642961316`. Do not interpret the overall source-chain workflow as PASS: it failed at NF548.

New observed NF548 errors:
1. At line 57, the EVEN cutoff identity leaves one normalized `c + -x` argument not matched by the previous `-x + c` rewrite; no mathematical parity issue. NF556 repairs the rewrite to match the elaborated normal form, maintaining the original two identical translated Mathlib bumps.
2. At lines 85 and 99, `dsimp [neutralNF548CollarCenter]` unnecessarily fails when Lean has already reduced this definition. NF556 replaces these with a non-failing `simp only` normalization before linear arithmetic.

NF556's two repairs are **candidate Lean source implementations pending fresh CI**. NF549–NF551 remain compiler pending behind NF548.

## 2. Mathematical theorem: exact root multiplicity, without a high chain-rule identity

Let `p : ℝ[X]` be nonzero, and let `ω>0`. Define the **odd source dual polynomial**

```
F(X)=X*p(X²)
```

and `r=rootMultiplicity (ω²) p`. Mathlib provides the exact root factorization
```
p(Y)=(Y-ω²)^r*q(Y),       q(ω²)≠0.
```

NF555 has now compiled in Lean the underlying polynomial identity
```
F(X)=(X-ω)^r * [X*(X+ω)^r*q(X²)]
```
and the strict nonvanishing of the second factor at `X=ω`.

NF556 composes these facts with Mathlib's `Polynomial.rootMultiplicity_mul`, `Polynomial.rootMultiplicity_X_sub_C_pow`, and `Polynomial.rootMultiplicity_eq_zero` into the concrete theorem:

```
neutralNF556OriginalDualQuadraticRootMultiplicity
    (p : Polynomial ℝ) (hp : p ≠ 0) (ω : ℝ) (hω : 0 < ω) :
    rootMultiplicity ω (X * p.comp (X ^ 2)) =
      rootMultiplicity (ω ^ 2) p
```

The new file is `WeilDefect/Arithmetic/ActualZetaOriginalJ242QuadraticRootMultiplicity.lean`. It imports the *accepted* NF555 quadratic factorization and invokes only standard polynomial root multiplicity APIs, without any source-independence axiom. **The new complete equality proof awaits Lean compilation.**

## 3. Finite source proof after NF556

The intended genuine-source transfer has become particularly direct:

1. Actual original 241 oscillator rows and true `sinh(x/2)` pole yield an odd-jet left-kernel identity. The NF554 SHA-pinned all-entry auditor checked its complete 58,564 symbolic coefficients; a source-specific Lean differentiation theorem remains to be built.
2. Each oscillator block requires vanishing first `m_f` derivatives of `F(X)=Xp(X²)` at the original positive `ω_f=2πf`.
3. NF554's accepted Mathlib Hermite derivative theorem gives `rootMultiplicity ω_f F≥m_f`.
4. **NF556's new proposed exact theorem** transfers this to `rootMultiplicity (ω_f²) p≥m_f`.
5. The genuine pole row forces `p(-1/4)=0`; the original 67 positive squared nodes are distinct and disjoint from the pole. Their multiplicity product `H` has degree `241+1=242` and divides `p` when `p≠0`.
6. NF553's **LEAN PASS** degree-242 divisor obstruction gives `p=0`, and the real/complex finite-square matrix transfer would establish **original global generator independence**.
7. NF551 real-analytic collar identity and NF550 source weighted-square positivity would then establish genuine original 242 canonical Gram positivity, *after those modules and the source-specific theorem compile*.

No determinant expansion, numerical Gram, surrogate source, or arbitrary independence axiom is required for this finite source proof.

## 4. Verification and limits

New CI `.github/workflows/nf556-original-quadratic-multiplicity.yml` has separate pinned Lean jobs for:
- standalone exact rootMultiplicity equality;
- sequential genuine NF546→NF551 compiler recovery, including repaired canonical NF548 cutoff.

No new numeric or source-only auditor is substituted for these mathematical Lean gates. NF555's original symbolic source audit and NF554's 58,564 true source coefficient audit are already PASS.

**Remaining open, not transferred:** source-specific Lean odd-jet derivative identity; construction and degree of the dual polynomial from 242 coefficients; 68-node multiplicity-product divisibility; real/complex rank transfer; full unconditional global original J242 independence; REAL-data conjugation-equivariant correction; unconditional original Gram in Lean; NF528 full divisor graph convergence; NF527 full gamma+prime n9+both poles 1/10 coercivity; NF539 signed Weil identity; W_ODD_NEG; RH.

## 5. NF557 target

First obtain actual CI acceptance of NF556's full rootMultiplicity equality and NF548 cutoff repairs. Resolve any new NF549–NF551 compiler errors from their real logs, then formalize the 68-node polynomial product divisor or the original source-specific dual coefficient construction in Lean.
