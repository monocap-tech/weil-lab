import WeilDefect.Arithmetic.ActualZetaSourceGraph

namespace WeilDefect
noncomputable section
open InnerProductSpace MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate ENNReal BigOperators
set_option maxHeartbeats 800000

/-- Finite selection of actual multiplicity coordinates, without an orbit
quotient or repeated-channel convention. -/
def neutralActualZetaSelectedProjection
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaGreenCoefficients →L[ℂ] NeutralActualZetaGreenCoefficients := by
  classical
  exact ∑ q ∈ s,
    (lp.singleContinuousLinearMap ℂ 2
      (fun _ : NeutralActualZetaDivisorCoordinate => ℂ) q).comp
      (lp.evalCLM ℂ (fun _ : NeutralActualZetaDivisorCoordinate => ℂ) 2 q)

theorem neutralActualZetaSelectedProjection_apply
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaSelectedProjection s u = ∑ q ∈ s, lp.single 2 q (u q) := by
  classical
  simp [neutralActualZetaSelectedProjection, _root_.sum_apply, lp.evalCLM, lp.evalₗ]

theorem neutralActualZetaSelectedProjection_coordinate
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u : NeutralActualZetaGreenCoefficients) (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaSelectedProjection s u q = if q ∈ s then u q else 0 := by
  classical
  rw [neutralActualZetaSelectedProjection_apply]
  simp only [lp.coeFn_sum, Finset.sum_apply, lp.single_apply, Finset.sum_pi_single]

/-- Exact unselected complement in the same coefficient space. -/
def neutralActualZetaBackgroundProjection
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaGreenCoefficients →L[ℂ] NeutralActualZetaGreenCoefficients :=
  ContinuousLinearMap.id ℂ _ - neutralActualZetaSelectedProjection s

theorem neutralActualZetaSelectedProjection_norm_sq
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u : NeutralActualZetaGreenCoefficients) :
    ‖neutralActualZetaSelectedProjection s u‖ ^ 2 = ∑ q ∈ s, ‖u q‖ ^ 2 := by
  rw [neutralActualZetaSelectedProjection_apply]
  simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
    lp.norm_sum_single (by norm_num : 0 < (2 : ℝ≥0∞).toReal) (fun q => u q) s

/-- The selected and background squared norms add exactly, not merely by a
triangle bound. -/
theorem neutralActualZetaCoefficient_selected_background_energy
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u : NeutralActualZetaGreenCoefficients) :
    ‖neutralActualZetaSelectedProjection s u‖ ^ 2 +
      ‖neutralActualZetaBackgroundProjection s u‖ ^ 2 = ‖u‖ ^ 2 := by
  have h := lp.norm_compl_sum_single
    (by norm_num : 0 < (2 : ℝ≥0∞).toReal) u s
  simp only [ENNReal.toReal_ofNat, Real.rpow_two] at h
  have hb : neutralActualZetaBackgroundProjection s u =
      u - ∑ q ∈ s, lp.single 2 q (u q) := by
    simp only [neutralActualZetaBackgroundProjection, ContinuousLinearMap.sub_apply,
      ContinuousLinearMap.id_apply, neutralActualZetaSelectedProjection_apply]
  rw [neutralActualZetaSelectedProjection_norm_sq, hb, h]
  ring

theorem neutralActualZetaCoefficient_projections_norm_le
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u : NeutralActualZetaGreenCoefficients) :
    ‖neutralActualZetaSelectedProjection s u‖ ≤ ‖u‖ ∧
    ‖neutralActualZetaBackgroundProjection s u‖ ≤ ‖u‖ := by
  have h := neutralActualZetaCoefficient_selected_background_energy s u
  have hp := norm_nonneg (neutralActualZetaSelectedProjection s u)
  have hb := norm_nonneg (neutralActualZetaBackgroundProjection s u)
  have hu := norm_nonneg u
  constructor <;> nlinarith [sq_nonneg ‖neutralActualZetaSelectedProjection s u‖,
    sq_nonneg ‖neutralActualZetaBackgroundProjection s u‖]

/-- Full-divisor P/N already includes both partner coordinates. This second
factor of 1/sqrt(2) converts its signed energy to the literal Weil normalization. -/
def neutralActualZetaSourceNormalization : ℂ := (Real.sqrt 2 : ℂ)⁻¹

theorem neutralActualZetaSourceNormalization_norm_sq :
    ‖neutralActualZetaSourceNormalization‖ ^ 2 = (1 / 2 : ℝ) := by
  unfold neutralActualZetaSourceNormalization
  rw [norm_inv, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _), inv_pow, Real.sq_sqrt (by norm_num)]
  norm_num

def neutralActualZetaNormalizedPositiveAnalysis (a : ℝ) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  neutralActualZetaSourceNormalization • neutralActualZetaPositiveAnalysis a

def neutralActualZetaNormalizedNegativeAnalysis (a : ℝ) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  neutralActualZetaSourceNormalization • neutralActualZetaNegativeAnalysis a

def neutralActualZetaSelectedNegativeAnalysis (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (neutralActualZetaSelectedProjection s).comp
    (neutralActualZetaNormalizedNegativeAnalysis a)

def neutralActualZetaBackgroundNegativeAnalysis (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (neutralActualZetaBackgroundProjection s).comp
    (neutralActualZetaNormalizedNegativeAnalysis a)

theorem neutralActualZetaNegativeAnalysis_selected_background (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) (f : NeutralActualZetaSourceDomain a) :
    neutralActualZetaSelectedNegativeAnalysis a s f +
      neutralActualZetaBackgroundNegativeAnalysis a s f =
        neutralActualZetaNormalizedNegativeAnalysis a f := by
  simp only [neutralActualZetaSelectedNegativeAnalysis,
    neutralActualZetaBackgroundNegativeAnalysis, ContinuousLinearMap.comp_apply,
    neutralActualZetaBackgroundProjection, ContinuousLinearMap.sub_apply,
    ContinuousLinearMap.id_apply]
  abel

theorem neutralActualZetaNegativeAnalysis_selected_background_energy (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) (f : NeutralActualZetaSourceDomain a) :
    ‖neutralActualZetaSelectedNegativeAnalysis a s f‖ ^ 2 +
      ‖neutralActualZetaBackgroundNegativeAnalysis a s f‖ ^ 2 =
        ‖neutralActualZetaNormalizedNegativeAnalysis a f‖ ^ 2 :=
  neutralActualZetaCoefficient_selected_background_energy s
    (neutralActualZetaNormalizedNegativeAnalysis a f)

/-- The actual finite selected energy, including the full-divisor half factor. -/
theorem neutralActualZetaSelectedNegativeAnalysis_energy (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) (f : NeutralActualZetaSourceDomain a) :
    ‖neutralActualZetaSelectedNegativeAnalysis a s f‖ ^ 2 =
      (1 / 2 : ℝ) * ∑ q ∈ s,
        ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralActualZetaSourcePhysical a f)‖ ^ 2 := by
  classical
  change ‖neutralActualZetaSelectedProjection s
    (neutralActualZetaNormalizedNegativeAnalysis a f)‖ ^ 2 = _
  rw [neutralActualZetaSelectedProjection_norm_sq]
  simp only [neutralActualZetaNormalizedNegativeAnalysis, ContinuousLinearMap.smul_apply,
    lp.coeFn_smul, Pi.smul_apply, norm_smul, mul_pow,
    neutralActualZetaSourceNormalization_norm_sq]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro q hq
  rw [(neutralActualZetaSourceAnalysis_sampling a f q).2]

/-- Signed form on the complete source graph; positivity is not asserted. -/
def neutralActualZetaSourceQuadratic (a : ℝ) (f : NeutralActualZetaSourceDomain a) : ℝ :=
  ‖neutralActualZetaNormalizedPositiveAnalysis a f‖ ^ 2 -
    ‖neutralActualZetaNormalizedNegativeAnalysis a f‖ ^ 2

/-- Positive energy minus the unselected negative energy. Realization as
an effective-positive synthesis requires a separate positivity/factorization proof. -/
def neutralActualZetaEffectiveBackgroundQuadratic (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) (f : NeutralActualZetaSourceDomain a) : ℝ :=
  ‖neutralActualZetaNormalizedPositiveAnalysis a f‖ ^ 2 -
    ‖neutralActualZetaBackgroundNegativeAnalysis a s f‖ ^ 2

theorem neutralActualZetaEffectiveBackgroundQuadratic_add_selected (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) (f : NeutralActualZetaSourceDomain a) :
    neutralActualZetaEffectiveBackgroundQuadratic a s f =
      neutralActualZetaSourceQuadratic a f +
        ‖neutralActualZetaSelectedNegativeAnalysis a s f‖ ^ 2 := by
  unfold neutralActualZetaEffectiveBackgroundQuadratic neutralActualZetaSourceQuadratic
  have h := neutralActualZetaNegativeAnalysis_selected_background_energy a s f
  linarith

/-- Normalization attaches directly to the certified zero form on the same
lifted Green vector, without a new source-representation premise. -/
theorem neutralActualZetaGreenSourceQuadratic_eq_zeroForm (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaSourceQuadratic a (neutralActualZetaGreenSourceLift a ha v) =
      (neutralActualZetaGreenZeroForm a v v).re := by
  unfold neutralActualZetaSourceQuadratic
  simp only [neutralActualZetaNormalizedPositiveAnalysis,
    neutralActualZetaNormalizedNegativeAnalysis, ContinuousLinearMap.smul_apply,
    norm_smul, mul_pow, neutralActualZetaSourceNormalization_norm_sq]
  have h := neutralActualZetaGreenSourceLift_energy a ha v
  rw [← neutralActualZetaGreenZeroForm_source_quadratic_re a ha v] at h
  linarith

/-- Actual finite-selected/background arithmetic attachment on unchanged
Green vectors. Neither background positivity nor retained-mode membership is assumed. -/
theorem neutralActualZetaGreenEffectiveBackground_native (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate) (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaEffectiveBackgroundQuadratic a s (neutralActualZetaGreenSourceLift a ha v) =
      (∫ ξ : ℝ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) +
      2 * (conj (sourceWindowMoment a (-(1/2)) (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a v)).re +
      (1 / 2 : ℝ) * ∑ q ∈ s,
        ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2 := by
  rw [neutralActualZetaEffectiveBackgroundQuadratic_add_selected,
    neutralActualZetaGreenSourceQuadratic_eq_zeroForm a ha v,
    neutralActualZetaGreenZeroForm_source_quadratic_re a ha v,
    neutralActualZetaSelectedNegativeAnalysis_energy,
    neutralActualZetaGreenSourceLift_physical]

end
end WeilDefect
