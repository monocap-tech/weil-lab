# NF738 — Arbitrary finite complex spans within the original frozen two-collar Weil support

**Canonical iteration:** NF738 · **Research track:** Phase IV analytical/interface formalization · **Stacked on:** [canonical NF736 PR #760](https://github.com/monocap-tech/weil-lab/pull/760) · **Shared registry:** [Issue #761](https://github.com/monocap-tech/weil-lab/issues/761).

## 1. Actual accepted starting theorem, not a source proposal

The original repository already contains:

```lean
neutralNF600SmoothCollarLower :
  neutralNF599SmoothCollarLower (2/5)
```

where `neutralNF599SmoothCollarLower` unfolds to a statement over **every complex Schwartz function** supported in the *same fixed original collars* E:

```lean
∀ s : 𝓢(ℝ,ℂ),
 (∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) →
 (2/5:ℝ) * ‖s.toLp 2 volume‖^2 ≤ neutralNF598SmoothWeil s
```

This is a literal **signed original EF** form built with `neutralWindowCorrelation (11/10)`, with its exact original real-part convention. It is not a blanket unwindowed, arbitrary-support form, and it is not merely numerical Gram positivity.

More specifically, the **genuine source-specific two-generator** consequence built in the historical `nf735` local-span module passed Lean's kernel and strict standard-axiom audit in **job 136461473716** of [run 44786163030](https://github.com/monocap-tech/weil-lab/actions/runs/44786163030), immutable accepted artifact **[14656510729](https://github.com/monocap-tech/weil-lab/actions/runs/44786163030/artifacts/14656510729)**. All four original local two-generator declarations depend only on `propext`, `Classical.choice`, `Quot.sound`. The same GitHub workflow's separate *pure moving-support geometry* job failed at the time; **successful job-level Lean acceptance is real and distinct from overall run conclusion**. A later repair added the missing Lebesgue `MeasureSpace ℝ` import to that unrelated pure module.

The historical source symbols `neutralNF735Original…` belong to the canonical **NF736** research iteration; their names remain unchanged for provenance. Their success does not imply global mixed support positivity.

## 2. The new NF738 exact Lean propositions

`WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteLocalSpan.lean` extends from two generators to **any finite index set of arbitrary type, any complex coefficients and any complex Schwartz generators** supported in E.

Let `F : Finset ι`, `s : ι → 𝓢(ℝ,ℂ)`, `c : ι → ℂ`, and let

[
S = \sum_{i\in F} c_i s_i.
]

If **every generator** is supported in E, the new proof candidates state:

**Finite support closure**

[
\operatorname{supp}(S) \subseteq E.
]

**Literal original signed Weil coercivity**

[
\boxed{\quad \frac25\lVert S\rVert_{L^2}^2
      \le \operatorname{Weil}_{\mathrm{EF},\,11/10}(S).\quad}
]

**Nonnegativity**

[
0 \le \operatorname{Weil}_{\mathrm{EF},\,11/10}(S).
]

**Strict positivity for a genuinely nonzero sum**

[
S\ne0\text{ in }L^2
\quad\Longrightarrow\quad
\operatorname{Weil}_{\mathrm{EF},\,11/10}(S)>0.
]

The final hypothesis concerns the **whole sum**: nonzero individual generators can cancel; none is implicitly presumed linearly independent.

Each proof uses already accepted `neutralNF735OriginalCollars_add`, `neutralNF735OriginalCollars_smul`, and especially **`neutralNF600SmoothCollarLower`**. This formalizes a consequence of the accepted infinite-dimensional local theorem; it does not use additional numerical solves, new physical matrices, or unsupported EF identities.

The new Lean theorem names are:

```lean
neutralNF738OriginalCollars_finset_linear
neutralNF738OriginalFiniteCollarSpan_coercive
neutralNF738OriginalFiniteCollarSpan_nonnegative
neutralNF738OriginalFiniteCollarSpan_positive
```

**Current standing:** these are **new committed proof candidates** until their own Lean kernel job and printed strict standard-axiom audit succeed.

## 3. Certification and reproducibility

`scripts/nf738_phaseiv_original_finite_span_audit.py` requires the **immutable successful original job**, all four upstream exact source theorem names, upstream source SHA-256 and the exact published axiom receipt. It checks each new theorem is present, uses the genuine local original source definitions and has no source-level `sorry`/`admit`/`axiom`/`unsafe` declaration.

The `NF738` CI workflow:

1. Checks successful upstream *job* 136461473716 in run 44786163030 and the exact nonexpired artifact 14656510729, without incorrectly claiming the entire upstream run passed.
2. Restores the accepted source-bound original EF two-generator proof receipt and checks its SHA and standard axioms.
3. Builds the **full source-specific** new Lean module against the original NF600 dependencies with the pinned Lean/Mathlib source environment.
4. Directly recompiles its four new declarations, parses their printed axiom sets, rejects `sorryAx` and other nonstandard premises, and publishes `nf738-original-finite-complex-collar-span-kernel-audit.json` **only after a genuine Lean PASS**.

## 4. What this establishes—and what it does not

The **existing NF600 theorem** already ranges over an infinite-dimensional function class restricted to E. NF738 packages the closure under arbitrary finite complex sums and the strict nonzero case into convenient reusable formal lemmas.

This does **not** enlarge the support E or identify `neutralWindowCorrelation (11/10)` with the unwindowed Weil autocorrelation for arbitrary translated tests. It does **not** derive mixed cross-support Hermitian Gram positivity or the necessary Cauchy–Schwarz bound on variable support intervals. It does not prove density of E-supported functions in the global test topology, global Weil positivity, or the Riemann Hypothesis.

Further Phase IV work must verify the exact global form dictionary (orientation, conjugation, signs, pole/gamma/prime terms, variable window and topology), and only then attempt the off-diagonal estimates for **distinct support locations**. This is the actual gap between the strong accepted local theorem and the classical global Weil criterion.

The concurrently queued **Phase III NF737** original index-zero numerical source and gate pilot are not used to establish the present fixed-support finite-span consequence.
