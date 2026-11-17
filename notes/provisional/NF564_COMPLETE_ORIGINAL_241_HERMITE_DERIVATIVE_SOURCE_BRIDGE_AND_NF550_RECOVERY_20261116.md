# NF564 — Complete original oscillator source odd-jet → Hermite dual reduction, and NF550 physical Gram compiler repair

**2026-11-16 PT. Draft stacked on NF563 PR #591. New algebraic and source-analytic Lean modules and NF550 repairs COMMITTED. Their NF564 compiler acceptance is PENDING. No original generator independence, unconditional original Gram strict positivity, signed Weil, W_ODD_NEG or RH conclusion is claimed.**

## 1. Verified concrete compiler breakthrough: genuine original sinh pole LEAN PASS

The NF562 source-pole GitHub Actions job (run `43979120808`, job `133690686104`) is **SUCCESS**. Its actual logs explicitly show

```
Built WeilDefect.Arithmetic.ActualZetaOriginalJ242OriginalPoleDual
Built WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualPoleOddDerivatives
```

Thus the original NF407 index-241 **actual analytic function** `j_241(x)=sinh(x/2)`, its exact odd iterated derivatives `j_241^(2n+1)(0)=2^(-(2n+1))`, the true original 242×242 analytic odd-jet matrix's final column, and its left-kernel implication `p_a(-1/4)=0` have now been compiler accepted. This is a verified source-analytic theorem rather than Python coefficients or a formal assumed pole column.

The same run's source custody audit job `133690686115` **PASS**, preserving the exact original oscillator 58,322 symbolic coefficients and true 242 sinh coefficients, with no source replacement.

## 2. Earlier accepted foundations and current real compiler stops

- Original physical source moment/cutoff/integral chain NF542–NF549: **LEAN PASS**, with NF549 explicit acceptance inside NF561 physical source job `133680034578`.
- NF553–NF556 algebraic Hermite degree obstruction, derivative→root multiplicity, quadratic factorization/cofactor and exact positive-frequency root multiplicity transfer: **LEAN PASS**.
- NF557–NF560 exact dual coefficient and genuine pole: **LEAN PASS inside NF562 successful source-pole job**.
- NF561–NF563 original oscillator analytic derivatives and first actual oscillator sine→dual root: **Lean compilation pending or previously failing**, not transferred from the source-only auditor.
- NF550 physical weighted-square and NF551 local-global analytic source branch: **not compiler accepted**. The first full weighted-square compiler failure occurred in `ActualZetaOriginalCanonicalGramWeightedSquare.lean`, downstream of NF549.
- The latest NF562 oscillator job `133690685721` failed on the earlier NF561 scaled sin/cos and monomial parser/type lemmas. Later NF562 targeted fixes are committed, but queued reruns had not yet been accepted at drafting. No false acceptance is inferred.

## 3. Mathematical NF564 bridge: exact polynomial all-order derivative coefficients

For the unchanged original 242 odd-jet real coefficient vector `a : Fin 242 → ℝ`, let

```
p_a(T) = Σ_(n<242) (-1)^n a_n T^n
F_a(X) = X*p_a(X²) = Σ_(n<242) (-1)^n a_n X^(2n+1).
```

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242OddDualHermitePolynomialDerivatives.lean` defines the actual signed `F_a` polynomial and gives candidate Lean proofs of:

```
F_a(ω)=ω*p_a(ω²)

eval ω (derivative^[k] F_a)
 = Σ_(n<242) (-1)^n a_n *
    Nat.descFactorial (2n+1) k * ω^(2n+1-k)
```

for every real `ω` and every natural `k`, including orders greater than the monomial degree where the exact descending factorial vanishes. It uses Mathlib's genuine `iterate_derivative_sum`, `iterate_derivative_C_mul` and `iterate_derivative_X_pow_eq_C_mul` with no approximation.

It also formalizes the exact signed coefficient conversions

```
Nat.descFactorial m k = k!*choose(m,k)
(-1)^r*(-1)^n = (-1)^(n-r)   (r≤n).
```

These are the mathematical identities needed to match both original sine/cosine derivatives with the dual polynomial's **higher Hermite derivatives**, including the original `(-1)^floor(k/2)` source parity.

**All new NF564 polynomial declarations are Lean CANDIDATES pending compilation.**

## 4. Complete genuine oscillator-type analytic → Hermite identities

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242OscillatorHermiteDualBridge.lean` combines the NF562 authentic monomial-sine/cosine derivative theorems with NF564's precise real signed descending factorial algebra.

For any real `ω`, any `r≥0` and any historical real `a : Fin242→ℝ`:

```
Σ_(n<242) a_n *
  [D_x^(2n+1)(x^(2r)*sin(ωx))]_(x=0)
    = (-1)^r [D_X^(2r)F_a](ω)

Σ_(n<242) a_n *
  [D_x^(2n+1)(x^(2r+1)*cos(ωx))]_(x=0)
    = (-1)^r [D_X^(2r+1)F_a](ω).
```

This includes BOTH regimes `r≤n` (exact factorial/sign calculation) and `r>n` (both sides zero from the true initial-monomial jet and the zero descending factorial). It is the COMPLETE generic analytic-to-Hermite identity for both forms found in the original NF407 source, not just the k=0 sine case isolated in NF563.

The new source-specific final module is

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242SourceIndexedHermiteBridge.lean
```

It selects the *literal frozen original* pair `(f_i,k_i)` for EVERY `i : Fin241`, and proves candidate identities

```
Σ_(n<242) a_n A[n,i]
  = (-1)^(k_i/2) *
      eval (2πf_i) (derivative^[k_i] F_a).

[Σ_n a_n A[n,i]=0] ⇒
      eval (2πf_i) (derivative^[k_i] F_a)=0.
```

No alternate oscillator list, rescaled pi, polynomial surrogate for the true analytic source, independent Gram axiom, or numerical determinant is involved. Here `A` is the actual original source odd-initial-derivative matrix `A[n,j]=j_j^(2n+1)(0)`, instantiated on `j_i`.

**The generic and source-indexed complete bridge are formal implementation CANDIDATES, NOT LEAN PASS until CI proves them.**

## 5. NF550 physical Gram repair, from real errors

NF563 originally committed corrections to the actual original NF550 source weighted-square proof after earlier CI logs. NF564 tightens two particularly sensitive aspects:

1. First lift each original L² representative to its exact source window function almost everywhere; sum these as functions with `eventuallyEq_sum` and use `Finset.sum_apply` *before* composing with `Lp.coeFn_fun_finsetSum`. This resolves the previous mismatch between pointwise finite sums and sums in function space; the original full-window L² class remains correct.
2. Once the true χ-weighted squared norm is cast back to real, prove the real-part integral via `integral_ofReal` and `Complex.ofReal_re` instead of a fragile unmatched rewrite.

The already committed genuine original source conjugate-norm scalar identity uses `Complex.normSq_eq_conj_mul_self` and `Complex.normSq_eq_norm_sq`, and continuity uses original NF546 source continuity, not an unsupported `fun_prop` search.

**NF550 and downstream NF551 remain compiler pending.** Nonnegative Gram identity alone does NOT establish strict positivity without real/complex source independence.

## 6. What remains between NF564 and a proved original finite Gram

If the NF564 all-241 source Hermite identities compile, the remaining finite algebraic route has been substantially shortened:

1. Formalize for each original frequency group `(f,m_f)` that the historical expanded source list includes exactly the `m_f` orders `k=0,...,m_f−1`. The exact rational list and total 241 oscillator count are accepted, but the group-to-index Hermite aggregation is a separate Lean obligation.
2. From an authentic 242×242 source matrix left-kernel vector, derive all `F_a^{(k)}(ω_f)=0` for `0≤k<m_f` at each of the **67 positive** original `ω_f=2πf`, plus genuine pole `p_a(-1/4)=0` from the now **LEAN PASS** NF560 source theorem.
3. Apply the already **LEAN PASS** NF554 Hermite derivative/root theorem and NF556 quadratic multiplicity theorem to obtain `rootMultiplicity(4π²f²,p_a)≥m_f`; add the separate negative pole. Prove **simultaneous** 68-node multiplicity-product divisibility or the equivalent multiset root-degree bound.
4. Their exact source multiplicity total `Σ m_f+1=242` contradicts the accepted source-specific `natDegree p_a<242` if `p_a≠0`; coefficient extraction gives `a=0`.
5. Transfer trivial real left kernel of this actual square source matrix to source rank, original complex coefficients and global generator independence; apply NF551 analytic collar uniqueness + NF550 actual nonnegative/strict Gram identity to remove remaining conditional assumptions. This final connection remains OPEN.
6. Independently certify original real-data correction conjugation equivariance; it does not follow from arbitrary complex Gram positivity alone.

The larger NF528 complete actual positive/negative all-multiplicity divisor source graph, NF527 original gamma+prime n9/both poles 1/10 coercivity, NF539 signed Weil source identity, W_ODD_NEG and RH **OPEN**.

## 7. Verification and NF565 target

New workflow `.github/workflows/nf564-original-full-hermite-source-bridge.yml` independently compiles:
- exact original F_a=Xp_a(X²), all formal Hermite derivative coefficients, signed factorial/parity bridge;
- genuine all-241 oscillator source analytic-to-Hermite identity at the unchanged original frequencies;
- repaired genuine NF546→NF551 physical weighted-square/analytic source chain;
- SHA-pinned original 58,564-entry odd-jet coefficient audit.

No new proof holes are introduced in NF564 modules.

**NF565 target**: use actual NF564 Lean diagnostics to repair the new generic and source-indexed oscillator Hermite bridges, recover NF550→NF551, and formalize the 67-block source index/multiplicity aggregation and 68-node product root-degree contradiction. Avoid numerical determinant or sampled Gram substitutions.
