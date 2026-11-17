# NF567 — True original J242 complex global independence, unconditional canonical Gram proof candidate, and NF550 compiler recovery

**2026-11-16 PT. Draft stacked on NF566 PR #594. All new NF567 theorem implementations and physical-source repairs COMMITTED. New Lean compiler acceptance PENDING. This note does NOT assert that original global independence, strict canonical Gram positivity, corrected RH-facing scalar, W_ODD_NEG, or RH have been proved.**

## 1. Actual GitHub compiler observations

At this stage the NF564 run #43987898385 completed four focused jobs:

- Source-exact original NF554 58,564 coefficient audit **PASS**, job 133720688825.
- Full odd-dual polynomial Hermite algebra **FAIL**, job 133720688267, line 119. The prior proof rewrote a nested `(-1)^n` factor using `rw [←pow_add, Nat.sub_add_cancel]`, which mistakenly rewrote the outer product and left an unmatched exponent `r+n`. NF565 already committed a targeted intermediate-factor rewrite; new acceptance still queued.
- True all-241 source oscillator analytic-to-Hermite bridge **FAIL**, job 133720688738, at the upstream original NF561 scaled sine/cosine and monomial derivative selector. Those earlier errors were concrete reserved omega syntax, Nat-if real cast and a non-progressing simplifier, for which NF565 committed corrections. No new acceptance has yet been reported.
- Original NF546–NF551 physical source **FAIL**, job 133720688669, in `ActualZetaOriginalCanonicalGramWeightedSquare.lean`, downstream of **NF549 LEAN PASS**. It showed (a) max recursion depth in finite original L2 synthesis a.e. proof, (b) original basis-function representation mismatch, (c) reverse complex-Hermitian integrand multiplication order, (d) unclosed real-part of an exact complex integral after ofReal coercion.

The NF565 run #43989828358 and NF566 run #43992070417 jobs were all still **QUEUED** at latest check. No invented verification pass.

Confirmed accepted from previous runs: genuine original NF542–NF549 physical construction and NF549 continuous Gram pairing **LEAN PASS**; generic NF553–NF556 Hermite degree/multiplicity/positive-frequency quadratic root transfer **LEAN PASS**; original NF557–NF560 exact dual coefficients and genuine analytic sinh(x/2) pole, including `p_a(-1/4)=0` under its true left-kernel column, **LEAN PASS within original NF562 source-pole successful build**.

## 2. Real → complex base change of the ORIGINAL finite odd-jet matrix

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242ComplexOddJetMatrixInvertible.lean` defines:

```
A_ℂ := (neutralNF560ActualOriginalOddJetMatrix).map Complex.ofRealHom.
```

Here `A_ℝ[n,j]` is precisely the (2n+1)-st initial analytic derivative of the unchanged NF407 selected real function j_j, for all 241 true trig monomial oscillators and the true final sinh pole. There is no alternate complex basis.

The new candidate theorems include:

- Exact entry equality `A_ℂ[n,j]=(A_ℝ[n,j]:ℂ)`.
- Exact determinant base change `det A_ℂ = Complex.ofReal(det A_ℝ)` using `RingHom.map_det`.
- If NF566's genuine source real `IsUnit A_ℝ` compiles, `IsUnit A_ℂ` follows by `IsUnit.map Complex.ofRealHom` and `Matrix.isUnit_iff_isUnit_det`.
- Therefore the complex left-kernel `d ᵥ* A_ℂ=0` is trivial.

**All are exact source-dependent Lean proof candidates; they are NOT compiler-accepted yet because the real NF566 theorem and NF567 module remain pending.** This does not by itself establish local-collar analytic uniqueness or strict Gram positivity.

## 3. GENUINE global real and complex generator independence

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242GlobalComplexSourceIndependence.lean` goes beyond finite matrix invertibility.

It proves candidate smoothness of every historical actual real source generator (the real-analytic 241 monomial sine/cosine modes and last sinh(x/2)), and applies Mathlib's exact `iteratedDeriv_fun_sum` and `iteratedDeriv_const_mul_field` to ANY finite original REAL combination:

```
D^m [ Σ_(j<242) a_j j_j(x) ]_(x=0)
   = Σ_(j<242) a_j (D^m j_j)(0).
```

If the real combination vanishes globally, every one of its 242 odd derivatives at zero vanishes. Those equations are precisely `A_ℝ *ᵥ a=0`. The NF566 genuine original real matrix `IsUnit`, once accepted, forces `a=0`. No global source-independence assumption is introduced.

Next, for an arbitrary original complex coefficient vector d, the actual complex physical source combination is

```
S_d(x)=Σ_j d_j * ((j_j(x):ℝ):ℂ).
```

Because each original j_j is real, the real and imaginary parts of S_d are the genuine original real source combinations of `Re d` and `Im d). If S_d vanishes on every real x, the real global theorem forces both coefficient vectors to vanish. The candidate original global COMPLEX independence theorem is:

```
∀ d:Fin242→ℂ,
 (∀ x:ℝ, neutralNF550OriginalSourceCombination d x=0) → d=0.
```

This directly addresses the original NF551 global independence Prop, rather than claiming that complex matrix invertibility alone proves functional source independence.

**The global real/complex analytic proof candidates have not yet compiled.**

## 4. Remove original NF550/551 independence hypotheses

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242UnconditionalCanonicalGram.lean` imports the authentic NF551 real-analytic collar unique-continuation theorem and the NF550 physical weighted-square source Gram. It supplies the original global-complex independence theorem proven in the preceding candidate module rather than accepting it as a hypothesis.

The new explicit candidate outputs are:

1. `NeutralNF551OriginalJ242GlobalIndependence`, from original analytic source rank;
2. the canonical fixed original endpoint collar separation `NeutralNF550OriginalCollarSeparatesJ242`, via NF551 local-to-global analytic identity;
3. **strict canonical source Gram** for every complex d ≠0:
   ```
   0 < (Σ_i conj(d_i)*(neutralNF548CanonicalOriginalWeightedGram d)_i).re;
   ```
4. injectivity of the exact original weighted Gram;
5. the ORIGINAL 242 physical-moment-matching, strict-E-supported Schwartz right inverse through `NeutralNF543RightInverse`, with no extra Gram positivity axiom.

This is an implementation of the full source rank → local collar → canonical strict Gram → right inverse architecture. **None of these NF567 new dependent theorems are Lean PASS.** In particular, NF550 weighted-square and NF551 analytic identity remain independent compiler obligations, and the original NF566 real matrix proof is not accepted yet.

## 5. Targeted NF550 compiler recovery

NF567 edits the genuine original NF550 `ActualZetaOriginalCanonicalGramWeightedSquare.lean`, preserving χ, full physical [-11/10,11/10], original E, all 242 frequencies/source functions, the actual NF549 source pairing, and complex coefficients:

- sets `maxRecDepth 4096` around only the L2 a.e. finite synthesis proof, restoring the previous depth afterwards;
- returns to the exact proven NF549 `Pi.basisFun_repr` normalization of the genuine source coordinates instead of the ineffective alternative simplifier;
- corrects the Hermitian inner-product scalar factor order using Mathlib's commutative complex multiplication rather than assuming the two expressions syntactically equal;
- states an explicitly typed `integral_ofReal` equality for the complex-to-real weighted squared norm, avoiding the previous unclosed coercion simplifier.

These repairs are **candidate**, not yet compiler accepted. If compilation reaches NF551, solve downstream errors from the real logs instead of replacing the analytic source with an unverified abstract independence assertion.

## 6. Verification and strict mathematical boundary

New `.github/workflows/nf567-original-complex-global-independence.yml` runs three independent checks: full NF566 genuine original real matrix → NF567 complex matrix + global analytic independence; the original NF549→NF551 physical Gram and NF567 unconditional strict Gram/Schwartz right inverse; and unchanged original SHA-pinned 58,564 source coefficients.

The true original finite source rank/Gram status is **IMPLEMENTED AS LEAN CANDIDATES, pending full compiler acceptance**. CI queuing is not a pass.

Even full original unconditional canonical Gram positivity would not prove the entire Riemann Hypothesis: NF528 full original all-multiplicity positive/negative divisor source graph convergence, NF527 full gamma+prime n=9 both-pole 1/10 coercivity, NF539 complete signed original Weil scalar identity, real-data correction conjugation equivariance, W_ODD_NEG and RH remain **OPEN**.

## NF568 target

Check actual NF567 and pending NF565/NF566 CI and fix the first precise Lean failures, focusing on finite original oscillator derivative/68-root assembly and NF550 a.e./integral proof. Obtain verified original real IsUnit before depending on complex global independence, and verified NF550/NF551 before advertising strict canonical Gram. Once both sides pass, certify the final original source-specific Schwartz right inverse and tackle real-data conjugation-equivariant correction; do not reopen numerical Gram or surrogate source investigations.
