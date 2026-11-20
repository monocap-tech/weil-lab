# NF741 — Phase IV: actual two-argument Weil explicit formula under window enlargement

**Canonical iteration:** NF741, based on canonical Phase IV NF740 PR #765 and registered in [the repository NF registry](https://github.com/monocap-tech/weil-lab/issues/761).

**Standing at commit:** **Source committed / new Lean kernel verification pending.** No new theorem is counted LEAN PASS until the dedicated actual-source workflow and all twelve strict standard-axiom audits succeed. No merged-main, global positivity, RH or numerical Phase III closure assertion.

## 1. Why this is the next essential Phase IV retyping

The original complete signed Weil form is represented in the repository through the actual physical **window** observation `neutralWindowEvaluation a`, the actual two-argument `neutralWindowCorrelation a f g`, and the genuine `Zeta23.EF.literatureRHS`. Earlier Phase IV investigation located the pre-existing two-argument NF533 mixed explicit formula, but left support-window naturality unproved as a standalone attached theorem.

A common mistake would be to infer that because `a` appears in these definitions, changing `a` changes the underlying arithmetic Weil pairing. That is **false when both functions are fixed and already supported in the smaller window**. The original integrals and EF values depend on the actual test functions, not on an arbitrary larger cutoff in which they are viewed.

The required source-specific theorem is not positivity and not a limit theorem. It is an exact identity in the original conventions.

## 2. Mathematical statement — two arbitrary COMPLEX Schwartz inputs

For arbitrary `s,t : 𝓢(ℝ,ℂ)` supported inside the symmetric interval `[-a,a]`, and `a≤b`, define the authentic physical L² tests `f=s.toLp 2 volume`, `g=t.toLp 2 volume`. The proposed NF741 declarations establish:

```text
neutralWindowRepresentative a f =ᵐ[volume] s
neutralWindowRepresentative b f =ᵐ[volume] s

neutralWindowEvaluation a z f = neutralWindowEvaluation b z f
    for every COMPLEX z

neutralWindowCorrelation a f g = neutralWindowCorrelation b f g
    as entire ℝ→ℂ functions

Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g)
  = Zeta23.EF.literatureRHS (neutralWindowCorrelation b f g).
```

The **actual full-multiplicity divisor** sampling series also agrees term by term, including conjugate-coordinate samples at every genuine zeta divisor copy:

```text
Σ'_q conj(WindowEval_a (conj z_q) f) * WindowEval_a z_q g
 = Σ'_q conj(WindowEval_b (conj z_q) f) * WindowEval_b z_q g.
```

No new zeta-zero enumeration, zero-counting estimate, real-odd reflection law or RH assumption enters these equalities.

## 3. Exact proof correspondence (source-grounded)

The new file `WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean` imports **existing original NF source**, not the pending IV003–IV005 exploratory modules:

- `neutralNF573WindowEvaluation_eq_raw_of_ae`: exact original window-transform → raw transform once the physical window representative agrees a.e. with a fixed test.
- `neutralWindowCorrelation_eq_realBilinearConvolution`: *actual* mixed window correlation is the real-bilinear convolution of window representatives, with the first argument conjugate-reflected.
- `neutralActualZetaWindowCorrelation_literature_of_contDiff`: genuine arithmetic zeta mixed EF, including original zero multiplicities and the nonzero archimedean/prime/pole terms (an accepted source anchor, not reproved here).

The new generalized Schwartz representative lemma says any complex Schwartz supported in `[-a,a]` agrees a.e. with its own original window representative. The potentially nontrivial bookkeeping step is transporting an a.e. equality under `x↦-x`: NF741 uses the actual Lebesgue-preserving negation identity `Measure.map_neg_eq_self`. Then the existing Mathlib `convolution_congr` transports BOTH input representatives through the literal correlation. Since the correlations are **equal as functions**, applying the actual `Zeta23.EF.literatureRHS` preserves the *complete* arithmetic value, without any new bound, estimate, or normalizing convention.

There are exactly nine new proposed theorem declarations:
`neutralNF741Schwartz_window_ae`,
`neutralNF741Schwartz_support_expand`,
`neutralNF741WindowEvaluation_eq_of_support`,
`neutralNF741WindowReflection_ae`,
`neutralNF741WindowCorrelation_eq_of_support`,
`neutralNF741LiteralMixedEF_eq_of_support`,
`neutralNF741MixedDivisorSum_eq_of_support`,
`neutralNF741LiteralMixedEF_natural`,
`neutralNF741LiteralDiagonalWeil_natural`.

## 4. What this *does not* prove

This is a conditional-in-**support** source identity, not conditional-on-RH: once support fits inside both windows, `b` is a choice of representation. Enlarging the window does **not** enlarge the support class on which NF600 has established `2/5` coercivity, and does not prove positive mixed determinants across new test supports.

In particular, the following remain OPEN:

- An unconditional source-graph lift of **every** compact complex Schwartz test in every window; IV005 has a promising conjugate-reflection proof **candidate**, not yet kernel/audited acceptance.
- Exact compatibility, or a canonical identification, of the `NeutralActualZetaSourceDomain a` graph lifts themselves as `a` varies. The source-graph Hilbert norms and analysis vectors need not be literally equal across windows, even when their physical EF values match.
- Exact connection of the repo's sign, conjugation and test-class convention to the full external Weil positivity criterion, for every admissible function.
- Global positive semidefiniteness of mixed Gram matrices for arbitrary finite function families. Canonical NF740's three-support obstruction is a generic reminder that checking all two-block minors does not alone certify an arbitrary larger Gram matrix. This is an actual analytic/number theoretic barrier, not removed by window naturality.
- Every original Phase III numerical analytic-bank, physical matrix, vector and payment attachment. NF741 imports no original NF702/703 numerical proofs and makes no new numerical gate claim.

## 5. CI and audit custody

The workflow `.github/workflows/nf741-actual-mixed-window-naturality.yml` is independent of the Phase III index-zero matrix runner workflow. Its stages:

1. Exact original source preflight, including all nine theorem names, no `sorry` or `axiom` declarations, actual zeta EF and full divisor references.
2. Pinned Lean 4.34 / Mathlib cache and original full source dependency build.
3. Direct new Lean proof build and second independent `#print axioms` check for all nine new declarations **plus three accepted genuine source anchors**.
4. Enforce exclusively standard `[propext, Classical.choice, Quot.sound]` axioms, reject any `sorryAx` or kernel error, and SHA-bind source/compiled object and source dependencies in a machine-readable receipt.

**Kernel pending** until this job finishes successfully. A committed proof candidate does NOT establish mathematical source custody.

## 6. Research implication and recommended follow-up

This NF directly tests the hypothesis that support-window naturality is a *representation mismatch*, not new mathematics. If it passes Lean, the literal two-argument arithmetic EF is stable under enlarging any window containing the two physical tests.

That does **not** make positivity stable under enlarging the permitted support itself. The next legitimate question is whether the existing local prime/pole/archimedean bound can control larger supports or produce a positive-semidefinite simultaneous mixed Gram factorization. IV005 graph-lift compilation and the real mixed positivity obstruction should be addressed independently. Neither RH nor global Weil positivity is silently imported as a premise.

**Milestone definition:** *Proof of exact original mixed EF window naturality, not closure of Phase IV or the Weil criterion.*
