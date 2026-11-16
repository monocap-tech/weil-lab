import WeilDefect.Arithmetic.ActualZetaOriginalJ242WeightedCollarGram
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension

namespace WeilDefect
noncomputable section
open Function MeasureTheory Metric
open scoped SchwartzMap ContDiff ComplexConjugate

/-!
NF548 — AN EXPLICIT C∞, REAL EVEN NONNEGATIVE, NONZERO strict
original endpoint two-collar cutoff, using Mathlib's genuine
smooth unit-ball bump u. No postulated existence of χ and no
source modification.

The cutoff is built from two *equal* translated/scaled copies
of Mathlib's nonnegative even bump, centered at ±1099/1000,
of radius 1/2000. Both compact support intervals lie strictly
inside the unchanged original E of B=11/10 and δ=1/500.
-/

private def nf548u : ℝ → ℝ := ExistsContDiffBumpBase.u

def neutralNF548CollarCenter : ℝ := 1099 / 1000

/-- Actual original positive and negative endpoint bump:
both centered away from the old support boundary. -/
def neutralNF548RealEvenCollarCutoff (x : ℝ) : ℝ :=
  nf548u (2000 * (x - neutralNF548CollarCenter)) +
    nf548u (2000 * (x + neutralNF548CollarCenter))

/-- The chosen Mathlib bump is smooth to all orders. -/
private theorem nf548u_smooth : ContDiff ℝ ∞ nf548u :=
  ExistsContDiffBumpBase.u_smooth ℝ

private theorem nf548u_nonneg (x : ℝ) : 0 ≤ nf548u x :=
  ExistsContDiffBumpBase.u_nonneg x

private theorem nf548u_neg (x : ℝ) : nf548u (-x) = nf548u x :=
  ExistsContDiffBumpBase.u_neg x

/-- The TRUE cutoff is C∞; no flat-endpoint regularity proof is
recreated from scratch or assumed as a local axiom. -/
theorem neutralNF548RealEvenCollarCutoff_smooth :
    ContDiff ℝ ∞ neutralNF548RealEvenCollarCutoff := by
  have h₁ : ContDiff ℝ ∞
      (fun x : ℝ => (2000 : ℝ) * (x - neutralNF548CollarCenter)) := by
    fun_prop
  have h₂ : ContDiff ℝ ∞
      (fun x : ℝ => (2000 : ℝ) * (x + neutralNF548CollarCenter)) := by
    fun_prop
  exact (nf548u_smooth.comp h₁).add (nf548u_smooth.comp h₂)

/-- The source-preserving χ is EVEN, unlike a generic arbitrary
complex cutoff in NF547. -/
theorem neutralNF548RealEvenCollarCutoff_even (x : ℝ) :
    neutralNF548RealEvenCollarCutoff (-x) =
      neutralNF548RealEvenCollarCutoff x := by
  have h₁ :
      (2000 : ℝ) * (-x - neutralNF548CollarCenter) =
        -((2000 : ℝ) * (x + neutralNF548CollarCenter)) := by ring
  have h₂ :
      (2000 : ℝ) * (neutralNF548CollarCenter + -x) =
        -((2000 : ℝ) * (x - neutralNF548CollarCenter)) := by ring
  simp only [neutralNF548RealEvenCollarCutoff, h₁, h₂,
    nf548u_neg, add_comm]

/-- The source-preserving χ is NONNEGATIVE pointwise. -/
theorem neutralNF548RealEvenCollarCutoff_nonneg (x : ℝ) :
    0 ≤ neutralNF548RealEvenCollarCutoff x := by
  unfold neutralNF548RealEvenCollarCutoff
  exact add_nonneg (nf548u_nonneg _) (nf548u_nonneg _)

/-- Exact source-positive bump geometry: u(2000(x-c)) can be nonzero
only STRICTLY INSIDE the original positive terminal collar. -/
private theorem nf548PositiveBump_inside (x : ℝ)
    (h : nf548u (2000 * (x - neutralNF548CollarCenter)) ≠ 0) :
    x ∈ Set.Ioo ((11 / 10 : ℝ) - 1 / 500) (11 / 10 : ℝ) := by
  have hu : (2000 * (x - neutralNF548CollarCenter)) ∈
      Function.support nf548u := h
  rw [show Function.support nf548u = ball (0 : ℝ) 1 from
    ExistsContDiffBumpBase.u_support ℝ] at hu
  have habs : |2000 * (x - neutralNF548CollarCenter)| < 1 := by
    simpa only [Metric.mem_ball, dist_zero_right, Real.norm_eq_abs] using hu
  rcases abs_lt.mp habs with ⟨hlo, hhi⟩
  constructor <;> simp only [neutralNF548CollarCenter] at * <;> linarith

/-- Mirror geometry: the other copy stays strictly inside the
original NEGATIVE terminal collar. -/
private theorem nf548NegativeBump_inside (x : ℝ)
    (h : nf548u (2000 * (x + neutralNF548CollarCenter)) ≠ 0) :
    x ∈ Set.Ioo (-(11 / 10 : ℝ)) (-(11 / 10 : ℝ) + 1 / 500) := by
  have hu : (2000 * (x + neutralNF548CollarCenter)) ∈
      Function.support nf548u := h
  rw [show Function.support nf548u = ball (0 : ℝ) 1 from
    ExistsContDiffBumpBase.u_support ℝ] at hu
  have habs : |2000 * (x + neutralNF548CollarCenter)| < 1 := by
    simpa only [Metric.mem_ball, dist_zero_right, Real.norm_eq_abs] using hu
  rcases abs_lt.mp habs with ⟨hlo, hhi⟩
  constructor <;> simp only [neutralNF548CollarCenter] at * <;> linarith

/-- THE ORIGINAL strict E support, not merely the large full
physical window. This is pointwise vanishing outside exact E. -/
theorem neutralNF548RealEvenCollarCutoff_supported (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    neutralNF548RealEvenCollarCutoff x = 0 := by
  have h₁ : nf548u (2000 * (x - neutralNF548CollarCenter)) = 0 := by
    by_contra hn
    exact hx (Or.inr (nf548PositiveBump_inside x hn))
  have h₂ : nf548u (2000 * (x + neutralNF548CollarCenter)) = 0 := by
    by_contra hn
    exact hx (Or.inl (nf548NegativeBump_inside x hn))
  simp [neutralNF548RealEvenCollarCutoff, h₁, h₂]

/-- χ is COMPACTLY SUPPORTED in the original physical aperture.
In fact it vanishes outside the much thinner authentic two collars. -/
theorem neutralNF548RealEvenCollarCutoff_hasCompactSupport :
    HasCompactSupport neutralNF548RealEvenCollarCutoff := by
  apply HasCompactSupport.of_support_subset_isCompact
    (show IsCompact (Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ)) from
      isCompact_Icc)
  intro x hx
  by_contra hout
  apply hx
  apply neutralNF548RealEvenCollarCutoff_supported x
  intro hE
  rcases hE with hleft | hright
  · exact hout ⟨hleft.1.le, by linarith [hleft.2]⟩
  · exact hout ⟨by linarith [hright.1], hright.2.le⟩

/-- The canonical real cutoff is nonzero, with positive mass on the
positive collar. The corresponding negative value follows by evenness. -/
theorem neutralNF548RealEvenCollarCutoff_pos_center :
    0 < neutralNF548RealEvenCollarCutoff neutralNF548CollarCenter := by
  have h0mem : (0 : ℝ) ∈ Function.support nf548u := by
    rw [show Function.support nf548u = ball (0 : ℝ) 1 from
      ExistsContDiffBumpBase.u_support ℝ]
    simp
  have h0 : 0 < nf548u 0 :=
    lt_of_le_of_ne (nf548u_nonneg 0) (Ne.symm h0mem)
  have hother :
      0 ≤ nf548u (2000 *
        (neutralNF548CollarCenter + neutralNF548CollarCenter)) :=
    nf548u_nonneg _
  unfold neutralNF548RealEvenCollarCutoff
  convert add_pos_of_pos_of_nonneg h0 hother using 1 <;>
    simp [neutralNF548CollarCenter]

/-- χ is STRICTLY POSITIVE on a whole nonempty real open
interval lying inside the original positive collar. This supplies
the concrete open set needed for the original weighted Gram
analytic-independence argument, not just positivity at one point. -/
theorem neutralNF548RealEvenCollarCutoff_pos_interval
    (x : ℝ)
    (hx : x ∈ Set.Ioo
      (neutralNF548CollarCenter - 1 / 2000)
      (neutralNF548CollarCenter + 1 / 2000)) :
    0 < neutralNF548RealEvenCollarCutoff x := by
  have ha : |(2000 : ℝ) * (x - neutralNF548CollarCenter)| < 1 := by
    apply abs_lt.mpr
    constructor <;> dsimp [neutralNF548CollarCenter] at * <;> linarith [hx.1, hx.2]
  have hs :
      ((2000 : ℝ) * (x - neutralNF548CollarCenter)) ∈
        Function.support nf548u := by
    rw [show Function.support nf548u = ball (0 : ℝ) 1 from
      ExistsContDiffBumpBase.u_support ℝ]
    simpa only [Metric.mem_ball, dist_zero_right, Real.norm_eq_abs] using ha
  have hp :
      0 < nf548u ((2000 : ℝ) * (x - neutralNF548CollarCenter)) :=
    lt_of_le_of_ne (nf548u_nonneg _) (Ne.symm hs)
  have hn :
      0 ≤ nf548u ((2000 : ℝ) * (x + neutralNF548CollarCenter)) :=
    nf548u_nonneg _
  exact add_pos_of_pos_of_nonneg hp hn

/-- The matching negative original collar has the same positivity
interval, by exact evenness, not by a second chosen cutoff. -/
theorem neutralNF548RealEvenCollarCutoff_pos_negative_interval
    (x : ℝ)
    (hx : -x ∈ Set.Ioo
      (neutralNF548CollarCenter - 1 / 2000)
      (neutralNF548CollarCenter + 1 / 2000)) :
    0 < neutralNF548RealEvenCollarCutoff x := by
  simpa [neutralNF548RealEvenCollarCutoff_even x] using
    neutralNF548RealEvenCollarCutoff_pos_interval (-x) hx

/-- Embed the same explicit REAL cutoff into ℂ, preserving the
genuine source's complex-linear selected moment convention. -/
def neutralNF548ComplexEvenCollarCutoff (x : ℝ) : ℂ :=
  (neutralNF548RealEvenCollarCutoff x : ℂ)

theorem neutralNF548ComplexEvenCollarCutoff_smooth :
    ContDiff ℝ ∞ neutralNF548ComplexEvenCollarCutoff := by
  exact (Complex.ofRealCLM.contDiff.comp
    neutralNF548RealEvenCollarCutoff_smooth)

theorem neutralNF548ComplexEvenCollarCutoff_supported (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    neutralNF548ComplexEvenCollarCutoff x = 0 := by
  simp [neutralNF548ComplexEvenCollarCutoff,
    neutralNF548RealEvenCollarCutoff_supported x hx]

theorem neutralNF548ComplexEvenCollarCutoff_hasCompactSupport :
    HasCompactSupport neutralNF548ComplexEvenCollarCutoff := by
  apply HasCompactSupport.of_support_subset_isCompact
    (show IsCompact (Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ)) from
      isCompact_Icc)
  intro x hx
  by_contra hout
  apply hx
  apply neutralNF548ComplexEvenCollarCutoff_supported x
  intro hE
  rcases hE with hleft | hright
  · exact hout ⟨hleft.1.le, by linarith [hleft.2]⟩
  · exact hout ⟨by linarith [hright.1], hright.2.le⟩

theorem neutralNF548ComplexEvenCollarCutoff_even (x : ℝ) :
    neutralNF548ComplexEvenCollarCutoff (-x) =
      neutralNF548ComplexEvenCollarCutoff x := by
  exact congrArg Complex.ofReal (neutralNF548RealEvenCollarCutoff_even x)

/-- The actual χ is now a CONCRETE original-source supported,
nonnegative real even smooth function, rather than an existence
hypothesis. Its true original 242 weighted Gram is an actual
endomorphism; POSITIVITY of this particular endomorphism still
requires the remaining original exponential-polynomial uniqueness
and weighted integral proofs in Lean. -/
def neutralNF548CanonicalOriginalWeightedGram :
    Module.End ℂ (Fin 242 → ℂ) :=
  neutralNF547OriginalWeightedGram
    neutralNF548ComplexEvenCollarCutoff
    neutralNF548ComplexEvenCollarCutoff_smooth
    neutralNF548ComplexEvenCollarCutoff_hasCompactSupport

end
end WeilDefect
