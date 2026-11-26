import WeilDefect.MasterRecon.V10B4a
import Mathlib.Analysis.Fourier.FourierTransformDeriv

/-! V10B4b: Fourier kernel decay from two integrable derivatives.
The uniform physical derivative bounds for the supported cutoff
family and the weighted L¹ integrability are separate obligations. -/
namespace WeilDefect.MasterRecon.V10B4b

open MeasureTheory
open scoped FourierTransform

theorem fourier_norm_le (p : ℝ → ℂ) (u : ℝ) :
    ‖𝓕 p u‖ ≤ ∫ x, ‖p x‖ := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  refine (norm_integral_le_integral_norm _).trans (le_of_eq ?_)
  apply integral_congr_ae
  filter_upwards with x
  rw [norm_smul, Complex.norm_exp_ofReal_mul_I, one_mul]

theorem fourier_deriv_twice (p : ℝ → ℂ)
    (hp : Integrable p) (hp' : Integrable (deriv p))
    (hp'' : Integrable (deriv (deriv p)))
    (hd : Differentiable ℝ p) (hd' : Differentiable ℝ (deriv p))
    (u : ℝ) :
    𝓕 (deriv (deriv p)) u =
      (2 * (Real.pi : ℂ) * Complex.I * (u : ℂ)) ^ 2 * 𝓕 p u := by
  rw [Real.fourier_deriv hp' hd' hp'', Real.fourier_deriv hp hd hp']
  simp only [smul_eq_mul]
  ring

theorem derivative_factor_norm (u : ℝ) :
    ‖2 * (Real.pi : ℂ) * Complex.I * (u : ℂ)‖ ^ 2 =
      (2 * Real.pi) ^ 2 * u ^ 2 := by
  simp only [norm_mul, norm_ofNat, Complex.norm_real, Real.norm_eq_abs,
    Complex.norm_I, mul_one, abs_of_nonneg Real.pi_pos.le, mul_pow, sq_abs]

theorem fourier_second_moment_bound (p : ℝ → ℂ)
    (hp : Integrable p) (hp' : Integrable (deriv p))
    (hp'' : Integrable (deriv (deriv p)))
    (hd : Differentiable ℝ p) (hd' : Differentiable ℝ (deriv p))
    (u : ℝ) :
    (2 * Real.pi) ^ 2 * u ^ 2 * ‖𝓕 p u‖ ≤ ∫ x, ‖deriv (deriv p) x‖ := by
  have h := fourier_norm_le (deriv (deriv p)) u
  rw [fourier_deriv_twice p hp hp' hp'' hd hd' u,
    norm_mul, norm_pow, derivative_factor_norm] at h
  exact h

theorem fourier_quadratic_decay (p : ℝ → ℂ)
    (hp : Integrable p) (hp' : Integrable (deriv p))
    (hp'' : Integrable (deriv (deriv p)))
    (hd : Differentiable ℝ p) (hd' : Differentiable ℝ (deriv p))
    (A B : ℝ) (hA : (∫ x, ‖p x‖) ≤ A)
    (hB : (∫ x, ‖deriv (deriv p) x‖) ≤ B) (u : ℝ) :
    ‖𝓕 p u‖ ≤ (A + B / (2 * Real.pi) ^ 2) / (1 + u ^ 2) := by
  have h0 := (fourier_norm_le p u).trans hA
  have h2 := (fourier_second_moment_bound p hp hp' hp'' hd hd' u).trans hB
  have hc : 0 < (2 * Real.pi) ^ 2 := by positivity
  have h2' : u ^ 2 * ‖𝓕 p u‖ ≤ B / (2 * Real.pi) ^ 2 := by
    apply (le_div_iff₀ hc).2
    calc
      u ^ 2 * ‖𝓕 p u‖ * (2 * Real.pi) ^ 2 =
          (2 * Real.pi) ^ 2 * u ^ 2 * ‖𝓕 p u‖ := by ring
      _ ≤ B := h2
  apply (le_div_iff₀ (by positivity : 0 < 1 + u ^ 2)).2
  nlinarith only [h0, h2']

theorem uniform_fourier_quadratic_decay {ι : Type*} (p : ι → ℝ → ℂ)
    (hp : ∀ i, Integrable (p i))
    (hp' : ∀ i, Integrable (deriv (p i)))
    (hp'' : ∀ i, Integrable (deriv (deriv (p i))))
    (hd : ∀ i, Differentiable ℝ (p i))
    (hd' : ∀ i, Differentiable ℝ (deriv (p i)))
    (A B : ℝ) (hA : ∀ i, (∫ x, ‖p i x‖) ≤ A)
    (hB : ∀ i, (∫ x, ‖deriv (deriv (p i)) x‖) ≤ B) :
    ∀ i u, ‖𝓕 (p i) u‖ ≤ (A + B / (2 * Real.pi) ^ 2) / (1 + u ^ 2) :=
  fun i u => fourier_quadratic_decay (p i) (hp i) (hp' i) (hp'' i)
    (hd i) (hd' i) A B (hA i) (hB i) u

end WeilDefect.MasterRecon.V10B4b

#print axioms WeilDefect.MasterRecon.V10B4b.fourier_norm_le
#print axioms WeilDefect.MasterRecon.V10B4b.fourier_deriv_twice
#print axioms WeilDefect.MasterRecon.V10B4b.derivative_factor_norm
#print axioms WeilDefect.MasterRecon.V10B4b.fourier_second_moment_bound
#print axioms WeilDefect.MasterRecon.V10B4b.fourier_quadratic_decay
#print axioms WeilDefect.MasterRecon.V10B4b.uniform_fourier_quadratic_decay
