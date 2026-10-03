import WeilDefect.Morphology.NeutralLogMultiplierSourceAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap InnerProductSpace
open scoped InnerProduct ComplexConjugate

/-- Physical compact-window evaluation, with the retained positive exponent
convention. It is a window integral, not the L2 Fourier transform at a point. -/
def neutralWindowEvaluation (a : ℝ) (z : ℂ) (f : RealComplexL2) : ℂ :=
  ∫ x in Set.Icc (-a) a, f x * Complex.exp (Complex.I * z * (x : ℂ))

/-- Actual raw synthesis column in the retained native convention. -/
def neutralExponentialColumn (a : ℝ) (z : ℂ) (x : ℝ) : ℂ :=
  (Set.Icc (-a) a).indicator
    (fun x => Complex.exp (-Complex.I * z * (x : ℂ))) x

theorem neutralExponentialColumn_memLp (a : ℝ) (z : ℂ) :
    MemLp (neutralExponentialColumn a z) 2 volume := by
  have hc : Continuous (fun x : ℝ => Complex.exp (-Complex.I * z * (x : ℂ))) := by
    fun_prop
  have hm : AEStronglyMeasurable (neutralExponentialColumn a z) volume :=
    hc.aestronglyMeasurable.indicator measurableSet_Icc
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hi : IntegrableOn
      (fun x : ℝ => ‖Complex.exp (-Complex.I * z * (x : ℂ))‖ ^ 2)
      (Set.Icc (-a) a) volume := (hc.norm.pow 2).integrableOn_Icc
  apply (hi.integrable_indicator measurableSet_Icc).congr
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;> simp [neutralExponentialColumn, hx]

def neutralExponentialColumnL2 (a : ℝ) (z : ℂ) : RealComplexL2 :=
  (neutralExponentialColumn_memLp a z).toLp (neutralExponentialColumn a z)

/-- First-antilinear inner products give evaluation at the conjugate ordinate.
No Fourier point evaluation of an arbitrary L2 representative is used. -/
theorem neutralExponentialColumnL2_inner (a : ℝ) (z : ℂ) (f : RealComplexL2) :
    inner ℂ (neutralExponentialColumnL2 a z) f =
      neutralWindowEvaluation a (conj z) f := by
  rw [L2.inner_def]
  unfold neutralWindowEvaluation
  rw [← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [(neutralExponentialColumn_memLp a z).coeFn_toLp] with x hx
  change inner ℂ ((neutralExponentialColumn_memLp a z).toLp
    (neutralExponentialColumn a z) x) (f x) = _
  rw [hx]
  by_cases hmem : x ∈ Set.Icc (-a) a
  · simp only [neutralExponentialColumn, Set.indicator_of_mem hmem,
      RCLike.inner_apply', ← Complex.exp_conj, map_mul, map_neg,
      Complex.conj_I, Complex.conj_ofReal, neg_neg]
    ring
  · simp [neutralExponentialColumn, hmem, RCLike.inner_apply']

/-- Concrete source vector in the complete form carrier: the actual physical
inclusion adjoint applied to the compact raw column. -/
def neutralLogExponentialSource (a : ℝ) (z : ℂ) : NeutralLogHilbertCarrier a :=
  ((neutralLogPhysicalInclusion a)†) (neutralExponentialColumnL2 a z)

theorem neutralLogExponentialSource_inner (a : ℝ) (z : ℂ)
    (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralLogExponentialSource a z) f =
      neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val) := by
  rw [neutralLogExponentialSource, adjoint_inner_left,
    neutralExponentialColumnL2_inner]
  rfl

/-- Actual continuous selected evaluation on the logarithmic domain. -/
def neutralLogExponentialAnalysis (a : ℝ) (z : ℂ) :
    NeutralLogHilbertCarrier a →L[ℂ] ℂ :=
  InnerProductSpace.toDual ℂ (NeutralLogHilbertCarrier a)
    (neutralLogExponentialSource a z)

theorem neutralLogExponentialAnalysis_eq (a : ℝ) (z : ℂ)
    (f : NeutralLogHilbertCarrier a) :
    neutralLogExponentialAnalysis a z f =
      neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val) :=
  neutralLogExponentialSource_inner a z f

/-- Retained pair diagonalization applied to the actual source columns. -/
def neutralLogPositivePairSource (a : ℝ) (z : ℂ) : NeutralLogHilbertCarrier a :=
  ((Real.sqrt 2)⁻¹ : ℂ) •
    (neutralLogExponentialSource a z + neutralLogExponentialSource a (conj z))

def neutralLogNegativePairSource (a : ℝ) (z : ℂ) : NeutralLogHilbertCarrier a :=
  ((Real.sqrt 2)⁻¹ : ℂ) •
    (neutralLogExponentialSource a z - neutralLogExponentialSource a (conj z))

theorem neutralLogPositivePairSource_inner (a : ℝ) (z : ℂ)
    (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralLogPositivePairSource a z) f =
      ((Real.sqrt 2)⁻¹ : ℂ) *
        (neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val) +
          neutralWindowEvaluation a z (neutralLogPhysical f.val)) := by
  change inner ℂ (((Real.sqrt 2 : ℝ) : ℂ)⁻¹ •
    ((neutralLogExponentialSource a z).val +
      (neutralLogExponentialSource a (conj z)).val)) f.val = _
  rw [_root_.inner_smul_left (𝕜 := ℂ) (E := RealComplexL2),
    _root_.inner_add_left (𝕜 := ℂ) (E := RealComplexL2)]
  have h1 : inner ℂ (neutralLogExponentialSource a z).val f.val =
      neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val) :=
    neutralLogExponentialSource_inner a z f
  have h2 : inner ℂ (neutralLogExponentialSource a (conj z)).val f.val =
      neutralWindowEvaluation a z (neutralLogPhysical f.val) := by
    simpa only [starRingEnd_apply, star_star] using
      neutralLogExponentialSource_inner a (conj z) f
  rw [h1, h2]
  simp only [map_inv₀, Complex.conj_ofReal]

theorem neutralLogNegativePairSource_inner (a : ℝ) (z : ℂ)
    (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralLogNegativePairSource a z) f =
      ((Real.sqrt 2)⁻¹ : ℂ) *
        (neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val) -
          neutralWindowEvaluation a z (neutralLogPhysical f.val)) := by
  change inner ℂ (((Real.sqrt 2 : ℝ) : ℂ)⁻¹ •
    ((neutralLogExponentialSource a z).val -
      (neutralLogExponentialSource a (conj z)).val)) f.val = _
  rw [_root_.inner_smul_left (𝕜 := ℂ) (E := RealComplexL2),
    _root_.inner_sub_left (𝕜 := ℂ) (E := RealComplexL2)]
  have h1 : inner ℂ (neutralLogExponentialSource a z).val f.val =
      neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val) :=
    neutralLogExponentialSource_inner a z f
  have h2 : inner ℂ (neutralLogExponentialSource a (conj z)).val f.val =
      neutralWindowEvaluation a z (neutralLogPhysical f.val) := by
    simpa only [starRingEnd_apply, star_star] using
      neutralLogExponentialSource_inner a (conj z) f
  rw [h1, h2]
  simp only [map_inv₀, Complex.conj_ofReal]

theorem neutralLogPositivePairSource_conjugate (a : ℝ) (z : ℂ) :
    neutralLogPositivePairSource a (conj z) = neutralLogPositivePairSource a z := by
  simp only [neutralLogPositivePairSource, starRingEnd_apply, star_star]
  rw [add_comm]

theorem neutralLogNegativePairSource_conjugate (a : ℝ) (z : ℂ) :
    neutralLogNegativePairSource a (conj z) = -neutralLogNegativePairSource a z := by
  simp only [neutralLogNegativePairSource, starRingEnd_apply, star_star, smul_sub, neg_sub]

/-- Actual selected negative pair energy, constructed from the compact columns. -/
def neutralLogSelectedPairOperator (a : ℝ) (z : ℂ) :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  rankOne ℂ (neutralLogNegativePairSource a z) (neutralLogNegativePairSource a z)

theorem neutralLogSelectedPairOperator_mixed (a : ℝ) (z : ℂ)
    (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogSelectedPairOperator a z g) =
      conj (inner ℂ (neutralLogNegativePairSource a z) f) *
        inner ℂ (neutralLogNegativePairSource a z) g := by
  rw [neutralLogSelectedPairOperator, inner_right_rankOne_apply,
    ← inner_conj_symm f (neutralLogNegativePairSource a z)]


/-- Actual real quadratic energy of the selected negative pair. -/
theorem neutralLogSelectedPairOperator_diagonal (a : ℝ) (z : ℂ)
    (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogSelectedPairOperator a z f) =
      ((‖inner ℂ (neutralLogNegativePairSource a z) f‖ ^ 2 : ℝ) : ℂ) := by
  simp only [neutralLogSelectedPairOperator_mixed, Complex.conj_mul', Complex.ofReal_pow]

/-- The convention swap leaves the concrete selected pair operator unchanged. -/
theorem neutralLogSelectedPairOperator_conjugate (a : ℝ) (z : ℂ) :
    neutralLogSelectedPairOperator a (conj z) = neutralLogSelectedPairOperator a z := by
  apply ContinuousLinearMap.ext
  intro f
  simp only [neutralLogSelectedPairOperator, neutralLogNegativePairSource_conjugate,
    rankOne_apply, inner_neg_left, neg_smul, smul_neg, neg_neg]

end

end WeilDefect
