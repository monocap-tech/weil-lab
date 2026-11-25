import WeilDefect.Arithmetic.ActualZetaIV091OriginalGreenMomentNormalizationGate
import Mathlib.Analysis.InnerProductSpace.Basic

namespace WeilDefect
noncomputable section

open MeasureTheory FourierTransform InnerProductSpace
open scoped FourierTransform ComplexConjugate

/-- Cauchy–Schwarz for absolute mixed Fourier products, through the actual
real L² norm representatives. -/
theorem neutralIV092L2_mixedNorm_integral_le (f g : RealComplexL2) :
    (∫ ξ : ℝ, ‖f ξ‖ * ‖g ξ‖) ≤ ‖f‖ * ‖g‖ := by
  have hf : MemLp (fun ξ : ℝ => ‖f ξ‖) 2 volume := (Lp.memLp f).norm
  have hg : MemLp (fun ξ : ℝ => ‖g ξ‖) 2 volume := (Lp.memLp g).norm
  let F : Lp ℝ 2 (volume : Measure ℝ) := hf.toLp _
  let G : Lp ℝ 2 (volume : Measure ℝ) := hg.toLp _
  have hF : ‖F‖ = ‖f‖ := by
    change ‖hf.toLp _‖ = ‖f‖
    rw [Lp.norm_toLp, eLpNorm_norm _ (Lp.aestronglyMeasurable f), ← Lp.norm_def]
  have hG : ‖G‖ = ‖g‖ := by
    change ‖hg.toLp _‖ = ‖g‖
    rw [Lp.norm_toLp, eLpNorm_norm _ (Lp.aestronglyMeasurable g), ← Lp.norm_def]
  have hi : inner ℝ F G = ∫ ξ : ℝ, ‖f ξ‖ * ‖g ξ‖ := by
    rw [MeasureTheory.L2.inner_def]
    apply integral_congr_ae
    filter_upwards [MemLp.coeFn_toLp hf, MemLp.coeFn_toLp hg] with ξ hξ hη
    change inner ℝ ((hf.toLp _) ξ) ((hg.toLp _) ξ) = _
    rw [Real.inner_apply, hξ, hη]
  rw [← hi, ← hF, ← hG]
  exact real_inner_le_norm F G

/-- Exact mixed absolute moment identity on the actual weak derivative,
including both factors of the ordinary Fourier derivative constant. -/
theorem neutralIV092GreenGradientMoment_integral
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (∫ ξ : ℝ, ‖(𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2) ξ‖ *
      ‖(𝓕 (neutralActualZetaGradientSynthesis a w) : RealComplexL2) ξ‖) =
      (2 * Real.pi)^2 * ∫ ξ : ℝ, neutralIV091GreenSpectralMoment a v w ξ := by
  rw [← integral_const_mul]
  apply integral_congr_ae
  filter_upwards [neutralActualZetaFourierDerivativeProduct_ae a ha v,
    neutralActualZetaFourierDerivativeProduct_ae a ha w] with ξ hv hw
  rw [hv, hw]
  have hk : ‖(2 * Real.pi * Complex.I : ℂ)‖ = 2 * Real.pi := by
    norm_num [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg Real.pi_pos.le]
  unfold neutralActualZetaFourierDerivativeProduct
  rw [norm_mul, norm_mul, hk, Complex.norm_real,
      norm_mul, norm_mul, hk, Complex.norm_real]
  simp only [neutralIV091GreenSpectralMoment, neutralActualZetaGreenCorrelationSpectrum,
    norm_mul, Complex.norm_conj, Real.norm_eq_abs]
  calc
    _ = (2 * Real.pi)^2 * (|ξ|^2 *
        (‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ *
         ‖(𝓕 (neutralActualZetaGreenSynthesis a w) : RealComplexL2) ξ‖)) := by ring
    _ = _ := by rw [sq_abs]

/-- Quantitative moment control by the actual constructed gradient norms,
without an extra spectral regularity premise. -/
theorem neutralIV092GreenGradientMoment_le
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (2 * Real.pi)^2 * (∫ ξ : ℝ, neutralIV091GreenSpectralMoment a v w ξ) ≤
      ‖neutralActualZetaGradientSynthesis a v‖ *
        ‖neutralActualZetaGradientSynthesis a w‖ := by
  have h := neutralIV092L2_mixedNorm_integral_le
    (𝓕 (neutralActualZetaGradientSynthesis a v))
    (𝓕 (neutralActualZetaGradientSynthesis a w))
  rw [neutralIV092GreenGradientMoment_integral a ha v w,
      Lp.norm_fourier_eq, Lp.norm_fourier_eq] at h
  exact h

/-- Original zero-form error, measured in physical weak derivative energy. -/
theorem neutralIV092GreenZeroForm_gradient_error_bound
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) :
    ‖neutralActualZetaGreenZeroForm a v w -
      neutralIV086PhysicalWeilFinite M N (neutralActualZetaGreenCorrelationInverse a v w)‖ ≤
      (‖neutralActualZetaGradientSynthesis a v‖ *
        ‖neutralActualZetaGradientSynthesis a w‖) / ((N : ℝ)+1)^2 := by
  calc
    _ ≤ (2 * Real.pi)^2 / ((N : ℝ)+1)^2 *
        ∫ ξ : ℝ, neutralIV091GreenSpectralMoment a v w ξ :=
      neutralIV091GreenZeroForm_error_bound a ha v w M N hM
    _ = ((2 * Real.pi)^2 * ∫ ξ : ℝ, neutralIV091GreenSpectralMoment a v w ξ) /
        ((N : ℝ)+1)^2 := by ring
    _ ≤ _ := div_le_div_of_nonneg_right (neutralIV092GreenGradientMoment_le a ha v w)
      (sq_nonneg _)

/-- The diagonal bound is the physical gradient-energy truncation budget. -/
theorem neutralIV092GreenZeroForm_gradient_diagonal_error_bound
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) :
    ‖neutralActualZetaGreenZeroForm a v v -
      neutralIV086PhysicalWeilFinite M N (neutralActualZetaGreenCorrelationInverse a v v)‖ ≤
      ‖neutralActualZetaGradientSynthesis a v‖^2 / ((N : ℝ)+1)^2 := by
  simpa only [pow_two] using neutralIV092GreenZeroForm_gradient_error_bound a ha v v M N hM

#print axioms neutralIV092L2_mixedNorm_integral_le
#print axioms neutralIV092GreenGradientMoment_integral
#print axioms neutralIV092GreenGradientMoment_le
#print axioms neutralIV092GreenZeroForm_gradient_error_bound
#print axioms neutralIV092GreenZeroForm_gradient_diagonal_error_bound

end
end WeilDefect
