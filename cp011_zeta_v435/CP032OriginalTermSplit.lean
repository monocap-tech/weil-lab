module

public import Zeta.EulerMaclaurin.Continuation
public import Zeta.Zeros.HardyZ

/-!
CP032 — isolated original Zeta-v4.35 Euler–Maclaurin finite-term split.
Only genuinely published original upstream modules; none of the
CP026–CP031 uncompiled local source candidates are imported.

The original approximant is decomposed into the 255 genuine
Dirichlet terms, the pole and half terms, and six Bernoulli
correction terms. This is a SOURCE PROOF CANDIDATE, not a kernel
acceptance receipt. The termwise rational bounds generated outside
Lean have NOT been proved in Lean. No external JSON is imported as
an axiom, and no actual original zeta zero is claimed.
-/

@[expose] public section

namespace CP032OriginalTermSplit

noncomputable abbrev point (t : ℝ) : ℂ :=
  (1 / 2 : ℂ) + Complex.I * (t : ℂ)

noncomputable abbrev dirichletTerm (t : ℝ) (n : ℕ) : ℂ :=
  (n : ℂ) ^ (-point t)

noncomputable abbrev poleTerm (t : ℝ) : ℂ :=
  (256 : ℂ) ^ (1 - point t) / (point t - 1)

noncomputable abbrev halfTerm (t : ℝ) : ℂ :=
  (256 : ℂ) ^ (-point t) / 2

noncomputable abbrev bernoulliTerm (t : ℝ) (k : ℕ) : ℂ :=
  ((bernoulli (2 * k) : ℝ) / ((2 * k)! : ℝ) : ℂ) *
      (ascPochhammer ℂ (2 * k - 1)).eval (point t) *
      (256 : ℂ) ^ (-point t - ((2 * k - 1 : ℕ) : ℂ))

/-- Original M=6,N=256 definitional source identity; this is an
UNCOMPILED proof candidate, with no imported numeric certificate. -/
theorem original_M6N256_finite_expansion (t : ℝ) :
    zetaApproximant (point t) 6 256 =
      (∑ n ∈ Finset.Ico 1 256, dirichletTerm t n) +
        poleTerm t + halfTerm t +
        (∑ k ∈ Finset.Icc 1 6, bernoulliTerm t k) := by
  rfl

/-- A generic source termwise real interval theorem; use actual
source-term memberships as explicit hypotheses, NEVER JSON axioms. -/
theorem component_sum_interval {α : Type*}
    (s : Finset α) (f lo hi : α → ℝ)
    (h : ∀ i ∈ s, lo i ≤ f i ∧ f i ≤ hi i) :
    (∑ i ∈ s, lo i) ≤ (∑ i ∈ s, f i) ∧
      (∑ i ∈ s, f i) ≤ (∑ i ∈ s, hi i) := by
  constructor
  · exact Finset.sum_le_sum (fun i hi => (h i hi).1)
  · exact Finset.sum_le_sum (fun i hi => (h i hi).2)

/-- Integer-grid interval: source expression membership awaits
actual Zeta v4.35 Lean proof at each term and both exact heights. -/
def cellMembership (x : ℝ) (lo hi : ℤ) : Prop :=
  (lo : ℝ) / (10 : ℝ) ^ 15 ≤ x ∧
    x ≤ (hi : ℝ) / (10 : ℝ) ^ 15

/-- CP033 first unconditional ORIGINAL Dirichlet term, at EVERY real height.
This is the actual source n=1 complex power, not a JSON axiom. -/
theorem dirichlet_one (t : ℝ) :
    dirichletTerm t 1 = 1 := by
  simp [dirichletTerm]

/-- CP033 first exact rational term membership on the 10^15 grid.
Both endpoints are a specialization of this universal source fact.
The generated CP032 broad n=1 interval is compatible but not trusted. -/
theorem dirichlet_one_exact_cells (t : ℝ) :
    cellMembership (dirichletTerm t 1).re 1000000000000000 1000000000000000 ∧
      cellMembership (dirichletTerm t 1).im 0 0 := by
  rw [dirichlet_one]
  norm_num [cellMembership]

end CP032OriginalTermSplit

#print axioms CP032OriginalTermSplit.original_M6N256_finite_expansion
#print axioms CP032OriginalTermSplit.component_sum_interval
#print axioms CP032OriginalTermSplit.dirichlet_one
#print axioms CP032OriginalTermSplit.dirichlet_one_exact_cells
