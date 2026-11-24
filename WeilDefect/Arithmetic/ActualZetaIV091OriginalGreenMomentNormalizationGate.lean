import WeilDefect.Arithmetic.ActualZetaIV090OriginalIntegratedGammaErrorGate
import WeilDefect.Arithmetic.ActualZetaLiteralFormula
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped FourierTransform

/-!
IV091: discharge IV090's second absolute Fourier moment on the
actual Green correlation inverse, keeping the original paper/Mathlib
Fourier dilation and its Jacobian. No positivity or RH claim.
-/

def neutralIV091OrdinaryMoment (k : ℝ → ℂ) (ξ : ℝ) : ℝ :=
  ξ^2 * ‖(𝓕 k) ξ‖

def neutralIV091GreenSpectralMoment
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (ξ : ℝ) : ℝ :=
  ξ^2 * ‖neutralActualZetaGreenCorrelationSpectrum a v w ξ‖

/-- Exact a.e. equality on the original Green carrier, including the
actual inverse correlation rather than a substitute smooth test. -/
theorem neutralIV091GreenMoment_ae
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralIV091OrdinaryMoment (neutralActualZetaGreenCorrelationInverse a v w)
      =ᵐ[volume] neutralIV091GreenSpectralMoment a v w := by
  filter_upwards [neutralActualZetaGreenCorrelation_fourier_spectrum_ae a ha v w]
    with ξ hξ
  unfold neutralIV091OrdinaryMoment neutralIV091GreenSpectralMoment
  rw [Real.fourier_congr_ae
    (neutralActualZetaGreenCorrelationInverse_ae a ha v w) ξ, hξ]

theorem neutralIV091GreenOrdinaryMoment_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (neutralIV091OrdinaryMoment
      (neutralActualZetaGreenCorrelationInverse a v w)) := by
  have h : Integrable (neutralIV091GreenSpectralMoment a v w) := by
    simpa only [neutralIV091GreenSpectralMoment, Real.norm_eq_abs, sq_abs]
      using neutralActualZetaGreenCorrelationSpectrum_secondMoment a ha v w
  exact h.congr (neutralIV091GreenMoment_ae a ha v w).symm

/-- The paper transform uses angular frequency r, with
xi = -r/(2*pi). The squared frequency factor is not omitted. -/
theorem neutralIV091MomentProfile_eq_scaled (k : ℝ → ℂ) :
    neutralIV090MomentProfile k = fun r : ℝ =>
      (2 * Real.pi)^2 *
        neutralIV091OrdinaryMoment k ((-(1 / (2 * Real.pi))) * r) := by
  funext r
  unfold neutralIV090MomentProfile neutralIV091OrdinaryMoment
  rw [Zeta23.EF.paperFT_ofReal_eq_fourier_Zeta23_EF_paper_inversion,
    show -(1 / (2 * Real.pi)) * r = -r / (2 * Real.pi) by ring]
  have he : (2 * Real.pi)^2 * (-r / (2 * Real.pi))^2 = r^2 := by
    field_simp [Real.pi_ne_zero] <;> ring
  rw [← mul_assoc, he]

/-- The certified IV090 moment premise is discharged on every actual
mixed Green inverse correlation, not merely on selected modes. -/
theorem neutralIV091GreenPaperMoment_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (neutralIV090MomentProfile
      (neutralActualZetaGreenCorrelationInverse a v w)) := by
  rw [neutralIV091MomentProfile_eq_scaled]
  have hn : (-(1 / (2 * Real.pi)) : ℝ) ≠ 0 := by
    exact neg_ne_zero.mpr (div_ne_zero one_ne_zero (mul_ne_zero (by norm_num) Real.pi_ne_zero))
  exact ((neutralIV091GreenOrdinaryMoment_integrable a ha v w).comp_mul_left' hn).const_mul _

/-- Exact Jacobian: the paper second moment is (2*pi)^3 times
the second absolute moment of the actual ordinary Green spectrum. -/
theorem neutralIV091GreenPaperMoment_integral
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (∫ r : ℝ, neutralIV090MomentProfile
      (neutralActualZetaGreenCorrelationInverse a v w) r) =
      (2 * Real.pi)^3 * ∫ ξ : ℝ, neutralIV091GreenSpectralMoment a v w ξ := by
  rw [neutralIV091MomentProfile_eq_scaled, integral_const_mul,
    Measure.integral_comp_mul_left]
  have habs : |(-(1 / (2 * Real.pi)) : ℝ)⁻¹| = 2 * Real.pi := by
    rw [inv_neg, abs_neg, one_div, inv_inv, abs_of_pos (by positivity)]
  rw [habs, smul_eq_mul, integral_congr_ae (neutralIV091GreenMoment_ae a ha v w)]
  ring

/-- Exact quantitative error for the original Green zero form.
Only the actual ordinary mixed spectral moment remains as a constant;
no extra moment premise or assumed positivity. -/
theorem neutralIV091GreenZeroForm_error_bound
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) :
    ‖neutralActualZetaGreenZeroForm a v w -
      neutralIV086PhysicalWeilFinite M N (neutralActualZetaGreenCorrelationInverse a v w)‖ ≤
      (2 * Real.pi)^2 / ((N : ℝ)+1)^2 *
        ∫ ξ : ℝ, neutralIV091GreenSpectralMoment a v w ξ := by
  have hs : ∀ u : ℝ, neutralActualZetaGreenCorrelationInverse a v w u ≠ 0 →
      |u| ≤ 2*a := by
    intro u hu
    apply abs_le.mpr
    by_contra h
    exact hu (neutralActualZetaGreenCorrelationInverse_supported a ha v w u
      (fun hmem => h ⟨hmem.1, hmem.2⟩))
  rw [neutralActualZetaGreenZeroForm_literature a ha v w]
  have hb := neutralIV090WeilError_bound M N _
    (neutralActualZetaGreenCorrelationInverse_contDiff a ha v w)
    (show 0 ≤ 2*a by positivity) hs hM
    (neutralIV091GreenPaperMoment_integrable a ha v w)
  rw [neutralIV091GreenPaperMoment_integral a ha v w] at hb
  convert hb using 1
  field_simp [Real.pi_ne_zero] <;> ring

#print axioms neutralIV091GreenMoment_ae
#print axioms neutralIV091GreenOrdinaryMoment_integrable
#print axioms neutralIV091MomentProfile_eq_scaled
#print axioms neutralIV091GreenPaperMoment_integrable
#print axioms neutralIV091GreenPaperMoment_integral
#print axioms neutralIV091GreenZeroForm_error_bound

end
end WeilDefect
