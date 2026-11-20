# IV003 — Actual signed full-divisor mixed pairing: the zero-side bridge was already typed

*Phase IV research branch, separate from NF735 original numerical/Lean runner certification.* No claims of global Weil positivity, unconditional RH or completed Phase III. New Lean source is a **candidate**, unless a successful independent kernel and axiom audit is subsequently recorded. Old NF734/NF735 CI runs remain separate and do not certify IV003.

## 1. Research result: the mixed zero-side operation already exists in the source architecture

Read actual `ActualZetaSourceGraph.lean`, `ActualZetaSourceDecomposition.lean`, `ActualZetaOriginalSignedGraphForm.lean`, `ActualZetaRawSamplesToFullSourceGraph.lean`, and `ActualZetaOriginalCollarCoercivity.lean`.

The literal graph domain is a complex closed submodule
`NeutralActualZetaSourceDomain a`, with two **linear** full-multiplicity divisor analysis maps
`P_a = neutralActualZetaPositiveAnalysis a` and
`N_a = neutralActualZetaNegativeAnalysis a`.

The established NF598 diagonal is
```text
Q_a(u) = (‖P_a u‖² - ‖N_a u‖²)/2.
```

No external zero-form or RH is needed to *define* the canonical mixed Hermitian form
```text
B_a(u,v) = ( ⟪P_a v, P_a u⟫_ℂ - ⟪N_a v, N_a u⟫_ℂ )/2.
```

We intentionally reverse the Mathlib inner-product input arguments: Mathlib is linear in the second entry; this form is linear in the FIRST entry, matching the convention in Danesh (2026), Eq. (2). It satisfies by Hilbert algebra
```text
B_a(u,u) = Q_a(u) ∈ ℝ,
B_a(u,v) = conj (B_a(v,u)),
Q_a(u+v)-Q_a(u-v) = 4 Re B_a(u,v),
Q_a(u+i v)-Q_a(u-i v) = 4 Im B_a(u,v).
```
In particular, **retyping diagonal positivity as Hermitian mixed-form positivity does not require the missing new zero-side construction**. The new file `ActualZetaPhaseIVExactMixedGraph.lean` proposes the actual source-specific definition and Lean proofs of diagonal equality, first-slot linearity, and joint graph-topology continuity. Its original-local diagonal coercivity wrapper uses NF600 + NF598 under a true graph-lift/physical-realization premise.

## 2. Exact pre-existing off-diagonal coordinate identity (critical)

The repository already proves `neutralLogPairSource_mixed_difference` in `ActualZetaSourceDecomposition.lean`. Written at each actual zeta-divisor coordinate q (including every multiplicity copy), with P/N coefficient vectors and centered paired window transforms `F_u`, `F_v`, it states
```text
conj(Pu[q]) Pv[q] - conj(Nu[q]) Nv[q]
  = conj(Fu[conj z_q]) Fv[z_q]
  + conj(Fu[z_q]) Fv[conj z_q].
```

This identity already has **two different source arguments**: it is genuinely mixed. The new `neutralIV003GraphMixed_coordinate` is an exact source-specific wrapper applying the accepted `neutralActualZetaSourceAnalysis_sampling` identities to the full graph domain. It is not the same as simply polarizing an arbitrary diagonal scalar.

The remaining summation transport can exploit the existing multiplicity-respecting divisor partner equivalence, together with `lp` mixed inner-product convergence and `neutralActualZetaWindowCorrelation_literature_of_contDiff` for TWO physical functions. That final all-divisor-to-literal-EF mixed equality has NOT been established as a new unconditional theorem by IV003.

## 3. A topology result we can state already, and its limitation

The full source graph norm includes both signed analysis vectors. The existing theorem `neutralActualZetaSourceAnalysis_norm_le` shows
```
‖P_a u‖ ≤ ‖u‖_graph,     ‖N_a u‖ ≤ ‖u‖_graph.
```
Therefore complex Hilbert Cauchy-Schwarz and the triangle inequality imply
```text
|B_a(u,v)| ≤ ½(‖P_a u‖‖P_a v‖ + ‖N_a u‖‖N_a v‖)
           ≤ ‖u‖_graph ‖v‖_graph.
```
Thus the mixed form is *jointly continuous in the existing source graph topology*, for every `a`. The new Lean `neutralIV003GraphMixed_continuous` candidate states that fact directly.

This **does not** prove continuity with respect to the ordinary physical L² norm, or continuity across different window parameters `a`. Nor does this inequality imply the strong *Weil-energy* Cauchy-Schwarz bound `|B(u,v)|²≤Q(u)Q(v)`: the graph norm is positive by construction, while `Q` is a signed difference.

## 4. The unexpectedly useful quantifier split: arbitrary complex smooth tests vs graph lifts

NF600 already proves the literal EF coercivity for **every complex Schwartz test supported in the old two collars**. However the existing NF573 graph-lift theorem `neutralNF573OriginalRealOddSchwartz_fullSource` is formulated for **real odd** collar Schwartz tests.

This difference must not be hidden. The graph's abstract linearity does NOT by itself lift every complex supported Schwartz input. The generic accepted `neutralActualZetaFullSourceLiftOfRawSamples` needs:
- membership of the logarithmic physical carrier; and
- `ℓ²` square-summability of BOTH authentic off-real actual-divisor sample families.

The currently accepted convenient odd input path, `neutralActualZetaOddPhysicalWindowSample_sq_summable`, uses the exact real-odd conjugation identity to turn absolute convergence of autocorrelation samples into single-family `ℓ²`. That input argument is **not valid for arbitrary complex f**.

For a generic smooth compact test, an alternative direct route is expected from integration by parts in a fixed strip and zeta zero counting: for each fixed support window,
```text
sup_{|σ|≤1/2} |F_f(σ+iγ)| ≤ C_{f,k}(1+|γ|)^{-k}
```
for sufficiently high `k`, and hence `∑_ρ |F_f(z_ρ)|²<∞` and partner samples too. This is a plausible standard-analysis bridge, **NOT yet a certified theorem in the repository for the entire complex class**. A new numerical matrix is not needed.

## 5. The global support step does not require L² density if the target is compact smooth tests

The external Weil criterion can be formulated on a suitable compactly supported smooth test class. Such a test lies in some finite interval `[-a,a]`; one could use a variable-window strategy:
```text
∀ a>0, ∀ supported complex smooth f inside [-a,a],
  (graph lift + correctly normalized literal EF) ∧ Q_a(f)≥0.
```

If the conventions and admissible class are matched exactly, that quantification covers the compact-test criterion **without** an additional abstract density limit. It still requires the hard uniform positivity argument for *arbitrary* supports, and exact independence of the EF value from an enlarged window. The fixed old collar class is not dense in a larger physical L² window.

This identifies a sharper type mismatch than “finite dimensional ⇒ infinite dimensional”: 
```text
fixed support E, real-odd full graph lifts
  → arbitrary finite windows, all admissible smooth test types
  → exact mixed EF across windows
  → universal positive semidefinite Weil energy.
```

## 6. The surviving arithmetic barrier

NF735 already establishes the support of an oriented cross correlation for `f` on `[0,d]` and `g` on `[L-d,L]`:
```text
supp k_(g,f) ⊆ [L-2d,L].
```
Danesh (arXiv:2611.10726v1, Nov 7 2026) writes an explicit moving-window prime-power formula for the mixed pairing in Section 5, Eq. (36); its full kernel includes archimedean/pole contributions and the moving prime-power sum, not just isolated primes.

This is an **external unreviewed equivalence claim**, not an imported Lean proof. In particular a uniform mixed Weil-energy Cauchy-Schwarz estimate might be as hard as RH. The bounded full source graph mixed form does not prove it, because its bound uses graph norms rather than signed Weil energies.

## 7. Next actionable exact proof targets

- **IV004**: kernel-verify the signed Hermitian source mixed form, its existing two-argument coordinate dictionary, and the *summed* mixed EF identity on a common supported smooth test class; audit zero/partner reindexing, normalization, conjugation and every multiplicity.
- **IV005**: extend the full graph lift to arbitrary complex compact smooth tests by a direct zero-count/vertical-transform decay estimate; do not assume real-odd conjugation.
- **IV006**: formalize changing the support-window parameter and prove invariance of the *literal* unwindowed mixed EF under enlargement of a window containing both supports.
- **IV007**: analyze the actual variable-separation mixed Gram determinant including archimedean, pole, and prime-power pieces. It would be circular to postulate nonnegative determinants for every support and call that a proof.

Keep this **IV-numbered research track** separate from the NF runner numbering to prevent the NF734 numerical/Phase-IV collision from recurring. No Phase III production branch or frozen numerical data are modified.

## Standing

IV003 source proposals committed; none of its new declarations is counted as accepted until a new source-bound kernel/axiom audit succeeds. The exact off-diagonal per-zero identity in NF source is **already present**; claiming it as a new theorem would be inaccurate. The contribution is extraction of the correct first-slot-linear signed mixed form, explicit exact coordinate specialization and an improved map of the remaining type mismatches.
