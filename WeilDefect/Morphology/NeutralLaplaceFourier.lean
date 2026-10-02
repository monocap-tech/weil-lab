import WeilDefect.Morphology.NeutralFiniteGauss

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped FourierTransform

def neutralLaplaceKernel (b x : ℝ) : ℂ := (Real.exp (-b * |x|) : ℂ)

def neutralLaplaceOscillation (b t x : ℝ) : ℂ :=
  Complex.exp (-(b : ℂ) * (|x| : ℂ) - (t : ℂ) * (x : ℂ) * Complex.I)

theorem neutralLaplaceKernel_integrable {b : ℝ} (hb : 0 < b) :
    Integrable (neutralLaplaceKernel b) volume := by
  apply (integrable_norm_iff (by
    exact (by fun_prop : Continuous (neutralLaplaceKernel b)).aestronglyMeasurable)).mp
  simpa [neutralLaplaceKernel, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos (Real.exp_pos _)] using integrable_exp_neg_rate_abs hb

theorem neutralLaplaceOscillation_left (b t x : ℝ) (hx : x ≤ 0) :
    Complex.exp (((b : ℂ) - (t : ℂ) * Complex.I) * (x : ℂ)) =
      neutralLaplaceOscillation b t x := by
  unfold neutralLaplaceOscillation
  rw [abs_of_nonpos hx]
  congr 1
  push_cast
  ring

theorem neutralLaplaceOscillation_right (b t x : ℝ) (hx : 0 < x) :
    Complex.exp ((-(b : ℂ) - (t : ℂ) * Complex.I) * (x : ℂ)) =
      neutralLaplaceOscillation b t x := by
  unfold neutralLaplaceOscillation
  rw [abs_of_pos hx]
  congr 1
  ring

/-- Genuine convergence and exact evaluation of the damped Fourier integral. -/
theorem neutralLaplaceOscillation_integral {b : ℝ} (hb : 0 < b) (t : ℝ) :
    Integrable (neutralLaplaceOscillation b t) volume ∧
    (∫ x, neutralLaplaceOscillation b t x) =
      ((b : ℂ) - (t : ℂ) * Complex.I)⁻¹ +
        ((b : ℂ) + (t : ℂ) * Complex.I)⁻¹ := by
  have hlRe : 0 < ((b : ℂ) - (t : ℂ) * Complex.I).re := by simpa using hb
  have hrRe : (-(b : ℂ) - (t : ℂ) * Complex.I).re < 0 := by simpa using neg_lt_zero.mpr hb
  have hl : IntegrableOn (neutralLaplaceOscillation b t) (Set.Iic 0) volume := by
    apply (integrableOn_congr_fun ?_ measurableSet_Iic).mp
      (integrableOn_exp_mul_complex_Iic hlRe 0)
    intro x hx
    exact neutralLaplaceOscillation_left b t x (Set.mem_Iic.mp hx)
  have hr : IntegrableOn (neutralLaplaceOscillation b t) (Set.Ioi 0) volume := by
    apply (integrableOn_congr_fun ?_ measurableSet_Ioi).mp
      (integrableOn_exp_mul_complex_Ioi hrRe 0)
    intro x hx
    exact neutralLaplaceOscillation_right b t x (Set.mem_Ioi.mp hx)
  have hi : Integrable (neutralLaplaceOscillation b t) volume := by
    have h := hl.union hr
    rw [Set.Iic_union_Ioi] at h
    exact integrableOn_univ.mp h
  refine ⟨hi, ?_⟩
  rw [← integral_add_compl measurableSet_Iic hi, Set.compl_Iic]
  have hleft : (∫ x in Set.Iic 0, neutralLaplaceOscillation b t x) =
      ∫ x in Set.Iic 0, Complex.exp (((b : ℂ) - (t : ℂ) * Complex.I) * (x : ℂ)) := by
    apply setIntegral_congr_fun measurableSet_Iic
    intro x hx
    exact (neutralLaplaceOscillation_left b t x (Set.mem_Iic.mp hx)).symm
  have hright : (∫ x in Set.Ioi 0, neutralLaplaceOscillation b t x) =
      ∫ x in Set.Ioi 0, Complex.exp ((-(b : ℂ) - (t : ℂ) * Complex.I) * (x : ℂ)) := by
    apply setIntegral_congr_fun measurableSet_Ioi
    intro x hx
    exact (neutralLaplaceOscillation_right b t x (Set.mem_Ioi.mp hx)).symm
  rw [hleft, hright, integral_exp_mul_complex_Iic hlRe,
    integral_exp_mul_complex_Ioi hrRe]
  simp only [Complex.ofReal_zero, mul_zero, Complex.exp_zero, div_eq_mul_inv, one_mul]
  rw [show -(b : ℂ) - (t : ℂ) * Complex.I =
    -((b : ℂ) + (t : ℂ) * Complex.I) by ring, inv_neg]
  ring

/-- Fourier normalization is exactly mathlib's t=2πξ convention. -/
theorem neutralLaplaceKernel_fourier {b : ℝ} (hb : 0 < b) (ξ : ℝ) :
    𝓕 (neutralLaplaceKernel b) ξ =
      ((b : ℂ) - ((2 * Real.pi * ξ : ℝ) : ℂ) * Complex.I)⁻¹ +
        ((b : ℂ) + ((2 * Real.pi * ξ : ℝ) : ℂ) * Complex.I)⁻¹ := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  have heq : (fun x : ℝ => Complex.exp ((-2 * Real.pi * x * ξ : ℝ) * Complex.I) •
      neutralLaplaceKernel b x) = neutralLaplaceOscillation b (2 * Real.pi * ξ) := by
    ext x
    simp only [neutralLaplaceKernel, neutralLaplaceOscillation, smul_eq_mul,
      ← Complex.ofReal_exp, ← Complex.exp_add]
    congr 1
    push_cast
    ring
  rw [heq]
  exact (neutralLaplaceOscillation_integral hb _).2

theorem neutralLaplace_resolvent_eq {b : ℝ} (hb : 0 < b) (t : ℝ) :
    ((b : ℂ) - (t : ℂ) * Complex.I)⁻¹ + ((b : ℂ) + (t : ℂ) * Complex.I)⁻¹ =
      ((2*b / (b^2+t^2) : ℝ) : ℂ) := by
  have hd : b^2+t^2 ≠ 0 := ne_of_gt (by nlinarith [sq_nonneg t, sq_pos_of_pos hb])
  apply Complex.ext <;>
    simp [Complex.inv_re, Complex.inv_im, Complex.normSq_apply, pow_two] <;>
    field_simp <;> ring

/-- The rational term in the finite digamma recurrence is exactly the
transform of its physical exponential, not just a similar coefficient. -/
theorem neutralGaussReciprocal_fourier (n : ℕ) (ξ : ℝ) :
    𝓕 (neutralLaplaceKernel (2*(n : ℝ)+1/2)) ξ =
      (neutralGaussReciprocal n (2 * Real.pi * ξ) : ℂ) := by
  have hb : 0 < 2*(n : ℝ)+1/2 := by positivity
  rw [neutralLaplaceKernel_fourier hb, neutralLaplace_resolvent_eq hb]
  congr 1
  unfold neutralGaussReciprocal
  have hd : (n : ℝ)+1/4 > 0 := by positivity
  field_simp
  ring

end

end WeilDefect
