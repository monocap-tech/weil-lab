# NF735 — Two-support pilot: exact moving cross window and mixed Gram condition

## 0. Scope and provenance

Phase IV research-only branch, stacked on NF734. No Phase III numerical dependencies are changed, and no global Weil positivity or RH result is claimed. The mathematical observations below refer separately to (a) authenticated Weil-Lab source definitions, (b) a new abstract proof proposal, and (c) an *external unreviewed preprint*.

### Source-checked repository facts

- `neutralNF600SmoothCollarLower : neutralNF599SmoothCollarLower (2/5)` is an *infinite-dimensional*, authentic literal-EF coercivity theorem for all complex Schwartz tests supported in fixed original collars E, based on local gamma, pole and prime estimates.
- `neutralNF598SmoothWeil` is the real part of `Zeta23.EF.literatureRHS` applied to **windowed** `neutralWindowCorrelation (11/10)`. For any test not supported in the fixed 11/10 window, this definition cannot yet be identified with the unwindowed global Weil form.
- `neutralNF598GraphWeil` is the signed full-divisor difference of squared P/N norms / 2; the literal-EF identification exists in NF598 *under its exact window-lift and support hypotheses*.
- The original two collars are the fixed open intervals `(-11/10,-11/10+1/500) ∪ (11/10-1/500,11/10)`. The NF600 prime exclusion uses this precise disconnected geometry, including the special n=9 cross-shift.

## 1. A complete *infinite-dimensional two-generator* theorem inside the old support

The source-bound new module `ActualZetaPhaseIVLocalSpan.lean` proposes:

```
∀ s,t : 𝓢(ℝ,ℂ),  supp(s)⊆E → supp(t)⊆E →
∀ z,w : ℂ,
 (2/5) * ‖(z • s + w • t).toLp 2 volume‖²
      ≤ neutralNF598SmoothWeil (z • s + w • t)
```

It uses exactly `neutralNF600SmoothCollarLower`, plus the elementary fact that E-supported functions are closed under complex linear combinations. It does **not** need Gram matrix positivity, 242 generators or the numerical solve. It is a retyping of the actual literal-EF theorem and a test that our formal class is already linear.

The generalized statement for any finite sum within E then follows by induction on the finite index set; the new two-element wrapper is a first bounded Lean test, not a claim of fully formalized arbitrary finite span.

## 2. The new support geometry

Let

```
 I=[0,d],   J=[L-d,L],  f|_{Iᶜ}=0,  g|_{Jᶜ}=0.
 k_{g,f}(u)=∫ℝ g(x+u) conj(f(x)) dx.
```

If the cross integrand is nonzero, then `x∈[0,d]` and `x+u∈[L-d,L]`. Exactly

```
             L - 2d ≤ u ≤ L.
```

Therefore

```
 supp(k_{g,f}) ⊆ [L-2d,L]
 k_{g,f}(log n)=0 for any n whenever
      log n < L-2d  or  log n > L.
```

These are **exact support statements**, not numerical approximations, and need no assumption of primality. For any Weil explicit formula in which the oriented prime-power cross term samples this literal correlation at log n, the only candidate contributors lie in the moving multiplicative window

```
                exp(L-2d) ≤ n ≤ exp(L).
```

This *conditional interface* is the useful reduction: one source pair has finitely many possible arithmetic prime-power interactions, but the active set moves as L grows. It is **not** a fixed list of primes and does not inherit the original n=9-only budget.

The new standalone Mathlib Lean module `ActualZetaPhaseIVTwoSupportGeometry.lean` proves the exact vanishing lemma and logarithmic-integer corollary at the level of the **unwindowed** correlation integral (kernel acceptance pending). It does not identify that integral with the actual NF598 EF prime term. The missing EF orientation, sign, conjugation, and window-removal step remains separate.

## 3. Minimal two-block positivity condition

A real two-dimensional Hermitian restriction has quadratic energy

```
             q(u,v)=a*u²+2m*u*v+b*v²,
             a=Q(f), b=Q(g), m=Re B(f,g).
```

A necessary and sufficient elementary condition for `q(u,v)≥0` for *all real* u,v is

```
                 a≥0, b≥0, m²≤a*b.
```

The new pure Lean module implements the **sufficient** direction only, using exact square completion:

```
 a*q(u,v)=(a*u+m*v)²+(a*b-m²)*v²
```

for a>0, and treats a=0 separately. Kernel verification pending.

For arbitrary complex coefficient combinations one needs the **Hermitian** version

```
            |B(f,g)|² ≤ B(f,f)*B(g,g)
```

with diagonal nonnegativity and an exact form dictionary. This is the specific mixed-support threshold, not an assumption we may import without proof. The extant NF600 coercivity on E already controls all mixed combinations *inside E*; it supplies no cross estimate between translated support intervals outside E.

## 4. Relevant independent research discovered

**Payam Danesh, “A quantitative two-interval criterion for the Riemann hypothesis”, arXiv:2611.10726, posted November 7, 2026**.
- The preprint *claims* that, for two moving compact intervals `[0,w(L)]` and `[L-w(L),L]` with subexponentially shrinking widths, the RH is equivalent to an eventually uniform Cauchy–Schwarz bound on the normalized mixed Weil pairing.
- It derives the same support-window geometry `[L-2w(L),L]` for the oriented cross correlation and describes the prime contribution in a moving multiplicative interval.
- It argues that hypothetical off-critical-line zeros force exponential normalized cross-term violations for sufficiently separated pairs.

External source: https://arxiv.org/abs/2611.10726 (sections 2–5, especially theorem 4). This is **an external, recent, unreviewed claim**; we have not independently audited its full proof or imported it into Lean. It is strong evidence that the two-support mixed pairing is a *natural research reformulation*, not evidence that the necessary arithmetic inequality is easy or known.

A related prior literature source: Bombieri, “Remarks on Weil's quadratic functional in the theory of prime numbers, I” (2000), dealing with finite unions of support intervals. Literature claims must never be used as unexplained Lean axioms.

## 5. Falsifiable Phase IV plan

1. **Proof-check this module**: accept exact cross-correlation support and the generic real 2×2 determinant criterion in standalone Mathlib; separately compile the new literal-EF two-generator span theorem on the original source.
2. **Exact Weil form dictionary**: introduce the unwindowed centered mixed pairing on compact smooth tests, prove its sesquilinearity / Hermitian symmetry, and identify its diagonal with the original NF598 EF *on tests supported in the frozen original window*. Do not change the paper Fourier sign or lose the poles.
3. **First nonlocal two-support test**: choose explicit d>0 and L>2d, and compute or bound the *full* mixed entry: moving prime-power samples, archimedean off-diagonal term, and the pole moments. Establish the exact determinant sign rather than testing diagonals alone.
4. **Extension diagnostic**: analyze whether the required mixed Cauchy–Schwarz bound, uniformly in L and d, is actually a restatement of RH (as the Danesh preprint claims under additional width hypotheses). If so, a tautological reduction is an exact reformulation, but it is not a proof of RH. Look for a strict stronger input from the NF600 geometric gamma/pole/prime bounds or another structural invariant.
5. **Keep Phase III separate**: continue original analytical-bank, physical row, vector, and global matrix custody independently. No speculative positivity lemma discharges those Boolean gate obligations.

## 6. Verdict

- **New exact support reduction:** an arbitrary two-support mixed correlation samples prime powers only in a moving short interval `[L-2d,L]` on the log axis.
- **New explicit criterion:** assembling local positive diagonal blocks requires signed off-diagonal control / Hermitian Gram PSD; individual local coercivity is not enough.
- **Key warning:** the hoped-for uniform mixed inequality may itself be equivalent to RH. A radical retyping can isolate the question but cannot discharge an equivalent, unproved hypothesis.

Both Lean modules and their CI remain **pending**, unless individually recovered with standard-axiom receipts. No unconditional Phase IV extension, global Weil positivity, RH, or main merge.
