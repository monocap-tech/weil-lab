import WeilDefect.Arithmetic.ActualZetaArchimedeanCoordinates
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_WeilEF_digamma_growth_strip
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_Stirling_differentiableAt_digamma
import Mathlib.MeasureTheory.Measure.Haar.NormedSpace

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped ComplexConjugate
set_option maxHeartbeats 800000

private theorem quarter_line_noninteger (r : ℝ) :
    (1 / 4 + Complex.I * (r : ℂ) / 2 : ℂ) ∈ Complex.integerComplement := by
  rintro ⟨k, hk⟩
  have he := congrArg Complex.re hk
  simp at he
  have h4 : (4 * k : ℤ) = (1 : ℤ) := by
    have : (4 : ℝ) * k = 1 := by rw [he]; norm_num
    exact_mod_cast this
  omega

/-- Continuity of the actual gamma bracket, with its quarter-line domain proved. -/
theorem neutralActualZetaGammaBracket_continuous :
    Continuous Zeta23.EF.gammaBracket := by
  have h : Continuous (fun r : ℝ => Complex.digamma
      (1 / 4 + Complex.I * (r : ℂ) / 2)) := by
    apply continuous_iff_continuousAt.mpr
    intro r
    exact ContinuousAt.comp (g := Complex.digamma)
      (f := fun t : ℝ => (1 / 4 + Complex.I * (t : ℂ) / 2 : ℂ))
      (Zeta23.Stirling.differentiableAt_digamma
        (quarter_line_noninteger r)).continuousAt (by fun_prop)
  exact (Complex.continuous_re.comp h).sub continuous_const

/-- A linear majorant for the native symbol follows from certified digamma growth. -/
theorem neutralActualZetaArchimedeanSymbol_bound :
    ∃ D : ℝ, 0 < D ∧ ∀ ξ : ℝ,
      ‖compactWindowArchimedeanSymbol (2 * Real.pi * ξ)‖ ≤ D * (1 + ‖ξ‖) := by
  obtain ⟨C, hC, hg⟩ := Zeta23.WeilEF.digamma_growth_strip
  have hb : ∀ r : ℝ, ‖Zeta23.EF.gammaBracket r‖ ≤
      C * (2 + |r|) + |Real.log Real.pi| := by
    intro r
    let z : ℂ := 1 / 4 + Complex.I * (r : ℂ) / 2
    have hre : z.re = 1 / 4 := by simp [z]
    have him : z.im = r / 2 := by simp [z]
    have hd := hg z (by rw [hre]) (by rw [hre]; norm_num)
    have hl : Real.log (2 + |z.im|) ≤ 2 + |r| := by
      have hp : 0 < 2 + |z.im| := by positivity
      have h := Real.log_le_sub_one_of_pos hp
      rw [him, abs_div] at h
      rw [him, abs_div]
      norm_num
      norm_num at h
      linarith [abs_nonneg r]
    calc
      ‖Zeta23.EF.gammaBracket r‖ ≤ |(Complex.digamma z).re| +
          |Real.log Real.pi| := by
        exact norm_sub_le _ _
      _ ≤ ‖Complex.digamma z‖ + |Real.log Real.pi| :=
        add_le_add_right (Complex.abs_re_le_norm _) _
      _ ≤ C * Real.log (2 + |z.im|) + |Real.log Real.pi| :=
        add_le_add_right hd _
      _ ≤ C * (2 + |r|) + |Real.log Real.pi| :=
        by linarith [mul_le_mul_of_nonneg_left hl hC.le]
  let D := C * (2 + 2 * Real.pi) + |Real.log Real.pi| + 1
  refine ⟨D, by dsimp [D]; positivity, ?_⟩
  intro ξ
  rw [← neutralActualZetaGammaBracket_native]
  have h := hb (2 * Real.pi * ξ)
  have he : |2 * Real.pi * ξ| = 2 * Real.pi * ‖ξ‖ := by
    rw [abs_mul, abs_mul, abs_of_pos Real.pi_pos]
    norm_num [Real.norm_eq_abs]
  rw [he] at h
  simp only [Real.norm_eq_abs] at h ⊢
  dsimp [D]
  nlinarith [abs_nonneg ξ, abs_nonneg (Real.log Real.pi),
    mul_nonneg hC.le (abs_nonneg ξ),
    mul_nonneg (abs_nonneg (Real.log Real.pi)) (abs_nonneg ξ),
    mul_nonneg hC.le Real.pi_pos.le]

/-- Absolute integrability of the digamma-weighted concrete mixed spectrum
is derived from the already proved zeroth and first Fourier moments. -/
theorem neutralActualZetaGreenArchimedean_spectral_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (fun ξ : ℝ =>
      (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
        neutralActualZetaGreenCorrelationSpectrum a v w ξ) := by
  obtain ⟨D, hD, hb⟩ := neutralActualZetaArchimedeanSymbol_bound
  have h0 := (neutralActualZetaGreenCorrelationSpectrum_integrable a v w).norm
  have h1 := neutralActualZetaGreenCorrelationSpectrum_moments a ha v w 1 (by norm_num)
  have hi := (h0.add h1).const_mul D
  have hc : Continuous (fun ξ : ℝ =>
      (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ)) := by
    simp_rw [← neutralActualZetaGammaBracket_native]
    exact Complex.continuous_ofReal.comp
      (neutralActualZetaGammaBracket_continuous.comp (by fun_prop))
  apply hi.mono' (hc.aestronglyMeasurable.mul
    (neutralActualZetaGreenCorrelationSpectrum_integrable a v w).aestronglyMeasurable)
  filter_upwards [] with ξ
  simp only [norm_mul, Complex.norm_real, Pi.add_apply, Pi.mul_apply, pow_one]
  calc
    _ ≤ (D * (1 + ‖ξ‖)) * ‖neutralActualZetaGreenCorrelationSpectrum a v w ξ‖ :=
      mul_le_mul_of_nonneg_right (hb ξ) (norm_nonneg _)
    _ = _ := by ring

private theorem arch_integrand_ae
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (fun ξ : ℝ =>
      neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w)
        ((-2 * Real.pi * ξ : ℝ) : ℂ) *
          (Zeta23.EF.gammaBracket (-2 * Real.pi * ξ) : ℂ)) =ᵐ[volume]
    (fun ξ : ℝ => (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
      neutralActualZetaGreenCorrelationSpectrum a v w ξ) := by
  filter_upwards [neutralActualZetaGreenCorrelationInverse_raw_spectrum_ae a ha v w]
    with ξ hξ
  rw [hξ, neutralActualZetaGammaBracket_mathlib]
  exact mul_comm _ _

/-- The original real-frequency literal integrand is absolutely integrable. -/
theorem neutralActualZetaGreenArchimedean_literal_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (fun r : ℝ =>
      neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w) (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ)) := by
  have hi := (neutralActualZetaGreenArchimedean_spectral_integrable a ha v w).congr
    (arch_integrand_ae a ha v w).symm
  exact (integrable_comp_mul_left_iff _ (show -2 * Real.pi ≠ 0 by
    exact mul_ne_zero (by norm_num) Real.pi_ne_zero)).mp hi

/-- Exact change of variables transports the literal archimedean term to
the existing native symbol on the same mixed physical Fourier spectrum. -/
theorem neutralActualZetaGreenArchimedeanForm_spectral
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenArchimedeanForm a v w =
      ∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
        neutralActualZetaGreenCorrelationSpectrum a v w ξ := by
  let F : ℝ → ℂ := fun r =>
    neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w) (r : ℂ) *
      (Zeta23.EF.gammaBracket r : ℂ)
  have h := Measure.integral_comp_mul_left F (-2 * Real.pi)
  have habs : |(-2 * Real.pi)⁻¹| = 1 / (2 * Real.pi) := by
    rw [show -2 * Real.pi = -(2 * Real.pi) by ring,
      inv_neg, abs_neg, abs_of_pos (inv_pos.mpr (by positivity))]
    simp only [one_div]
  rw [habs, Complex.real_smul] at h
  have he : (∫ ξ : ℝ, F ((-2 * Real.pi) * ξ)) =
      ∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
        neutralActualZetaGreenCorrelationSpectrum a v w ξ :=
    integral_congr_ae (arch_integrand_ae a ha v w)
  unfold neutralActualZetaGreenArchimedeanForm
  have hc : (1 / (2 * Real.pi) : ℂ) = ((1 / (2 * Real.pi) : ℝ) : ℂ) := by
    push_cast
    rfl
  rw [hc]
  exact h.symm.trans he

end
end WeilDefect
