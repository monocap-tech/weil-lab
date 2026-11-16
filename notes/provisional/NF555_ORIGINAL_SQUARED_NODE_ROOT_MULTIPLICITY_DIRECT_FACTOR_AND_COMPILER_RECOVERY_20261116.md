# NF555 — Direct quadratic root-multiplicity transfer for the authentic original 242 odd-jet source

**2026-11-16 PT. Draft stacked on NF554 PR #582. NF554 standalone polynomial multiplicity Lean PASS; full original 242 dual odd-jet source coefficient audit PASS. NF555 quadratic-source Lean and NF547 repair compiler acceptance PENDING. All global Weil/RH obligations OPEN.**

## 1. Accepted upstream status and actual failure

The accepted state is now:

- NF542–NF545 pinned original-source Lean **PASS**.
- NF546 authentic 242 full-window physical L² moments, including the genuine index-241 sinh pole, **LEAN PASS** on NF552 head, workflow #43958541249.
- NF552 original complete 242x242 odd-jet determinant/68-node Hermite-product modular *source audit PASS*, job 133619443020.
- NF553 generic polynomial degree-242 divisor obstruction and real squared-node/pole separation **LEAN PASS**, job 133628641547. Exact original determinant sign/source audit **PASS**, job 133628641424.
- **NF554 standalone generic characteristic-zero polynomial root-multiplicity Lean PASS**, job 133635543354, run #43963140728. Genuine NF407 source 58,322 oscillator + 242 sinh odd-jet symbolic coefficient audit **PASS**, job 133635543317.
- NF554 genuine NF547 source-smoothness build now fails **only** at `ActualZetaOriginalJ242WeightedCollarGram.lean:38`. The compiler shows `Complex.ofRealCLM.contDiff.comp hreal` proves the right mathematical function but `simpa only [neutralNF546OriginalComplexGenerator, Function.comp_def]` does not normalize the complex continuous-linear-map application to the source's complex coercion. NF555 removes this avoidable elaboration obstacle via an explicit definitional `change` before `exact Complex.ofRealCLM.contDiff.comp hreal`. This is a **candidate repair** pending a fresh Lean result. NF548–NF551 remain blocked upstream.

## 2. New mathematical reduction: no Faà di Bruno or triangular chain-rule matrix

NF553 and NF554 reduced unconditional original-source independence to the following remaining bridge: if all derivatives of

```
F(X) := X * p(X²)
```

of orders `k<m_f` vanish at the genuine positive oscillator frequency `ω_f=2πf`, show that `p` has a root of multiplicity at least `m_f` at its positive squared node `t_f=ω_f²`.

A general higher-order chain rule / triangular matrix formula is **unnecessary**. Root multiplicity is preserved under a quadratic change of variables away from the critical point `ω=0`, and the entire argument is an elementary polynomial factorization.

Fix any real polynomial `p≠0` and `ω>0`. Put

```
t = ω², r = rootMultiplicity t p.
```

Polynomial Euclidean division by the root factor supplies

```
p(Y) = (Y-t)^r q(Y),  q(t)≠0.
```

Then, **identically as real polynomials**,

```
F(X) = X * p(X²)
     = X * (X²-ω²)^r * q(X²)
     = (X-ω)^r * [X*(X+ω)^r*q(X²)].
```

At the positive root `X=ω`, the bracket is

```
ω*(2ω)^r*q(ω²) ≠ 0
```

because `ω>0` and `q(t)≠0`.

Consequently, the root multiplicity of `F` at `ω` is **exactly** `r`:

```
rootMultiplicity ω (X * p.comp (X²)) = rootMultiplicity (ω²) p.
```

This is the required algebraic bridge. In particular, if `F` has vanishing derivatives below order `m_f`, Mathlib's now-accepted NF554 generic lemma gives `m_f ≤ rootMultiplicity ω F`, and the equality above yields `m_f ≤ rootMultiplicity t_f p`.

**The equality is a complete paper proof, not yet an unconditionally compiled Lean theorem.** The new NF555 standalone module proves candidate building blocks for its exact factorization and nonzero cofactor, with no additional axiom or source surrogate.

## 3. New Lean module

`WeilDefect/Arithmetic/ActualZetaOriginalJ242QuadraticRootFactor.lean` implements candidate theorems:

1. `neutralNF555SquareNodeFactorization`: exact `X²−ω²=(X−ω)(X+ω)`.
2. `neutralNF555OriginalDualQuadraticFactorization`: exact polynomial identity for `F=X*p(X²)` whenever `p=(X−ω²)^m q`.
3. `neutralNF555OriginalDualQuadraticCofactor_nonzero`: at every **genuine original positive** `ω`, cofactor evaluation is nonzero whenever `q(ω²)≠0`.

These target only standard polynomial algebra and `eval` API. Their Lean compilation is pending. The separate Mathlib root-multiplicity computation required to turn these into the exact equality above will be the next local algebraic wiring stage.

## 4. Exact original-source symbolic replay without setting π=1

New source auditor:

```
scripts/local_replay/verify_nf555_original_quadratic_root_factorization.py
```

The auditor checks SHA-pinned NF407 source identity, NF500 true native raw custody SHA, exact original 67 positive rational frequency blocks, all 241 actual oscillator order rows, and the genuine index-241 sinh pole.

For each authentic `(f,m_f)`, it treats `π` as a formal indeterminate `Z` and independently constructs both sides of

```
(X² − 4 f² Z²)^m = (X−2fZ)^m * (X+2fZ)^m
```

over exact bivariate rational polynomial arithmetic `Q[X,Z]`. One side uses the explicit binomial formula; the other uses sparse polynomial convolution. It compares all exact nonzero coefficients for every original block and all prescribed original multiplicities, totaling

```
Σ_f (m_f+1) = 241 + 67 = 308
```

symbolic coefficient comparisons.

This is not an approximation of π and does not assume a numerical square-frequency collision test. The true negative sinh node `−1/4` is disjoint from every positive oscillator square for actual π>0. This Python audit and new pinned Lean workflow are committed, verification pending.

## 5. Terminal original global independence pipeline

Once the generic quadratic multiplicity equality above compiles, the exact remaining steps are:

1. Formalize the genuine NF407 source dual polynomial `p(t)=Σ_{n<242}(-1)^n a_n t^n` and its exact derivative identity with `F(X)=X*p(X²)` (NF554 already audits all 58,564 symbolic source coefficients).
2. Obtain `m_f ≤ rootMultiplicity (4π² f²) p` for all exact original 67 frequencies from NF554 derivatives plus the new quadratic bridge, and `p(-1/4)=0` from the genuine sinh pole.
3. Using the 68 pairwise distinct real nodes, establish `H(t)=(t+1/4)∏_f(t-4π² f²)^{m_f} ∣ p`. The product is monic with degree `242`; NF553's accepted degree obstruction yields `p=0`.
4. Invert the actual 242 odd-jet matrix and extend from real to complex coefficients, proving the existing `NeutralNF551OriginalJ242GlobalIndependence` **without hypothesis**.
5. Pass through NF551 real-analytic local/global identity and NF550 exact weighted-square theorem to obtain unconditional strict positivity of the **original** canonical 242 Gram in Lean.

The original-source REAL-valuedness/conjugation-equivariance of the final correction for real data is an independent still-open requirement, despite its odd symmetry.

## 6. Non-transfer and NF556 target

This is **finite source independence**, not the full Weil certificate. It does not resolve NF528 true inward/affine mollification and positive/negative all-multiplicity divisor graph convergence, NF527 exact gamma+prime n9+both poles 1/10 coercivity, NF539 complete signed Weil source identity, W_ODD_NEG, or RH. All remain **OPEN**.

**Next NF556:** obtain compiler acceptance for repaired NF547→NF551 and the standalone NF555 square-factor/cofactor lemmas. Then formalize the generic exact rootMultiplicity equality via Mathlib's existing polynomial root-factorization API, before tackling source-specific coefficient-to-derivative Lean proof.
