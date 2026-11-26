import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory

/-- Reciprocal-frequency tangent, avoiding a spectral probability measure. -/
theorem neutralIV106D1Log_tangent (R x : ℝ) (hR : 0 < R) (hx : 0 < x) :
    Real.log R + 1/2 - R^2/(2*x^2) ≤ Real.log x := by
  have h := Real.log_le_sub_one_of_pos
    (show 0 < R^2 / x^2 by positivity)
  rw [Real.log_div (pow_ne_zero _ hR.ne') (pow_ne_zero _ hx.ne'),
    Real.log_pow, Real.log_pow] at h
  have he : R^2/(2*x^2) = (R^2/x^2)/2 := by ring
  rw [he]
  linarith

/-- Integrate a reciprocal-moment envelope without integrating log |ξ|
separately. The supplied energy density is the original Gamma density. -/
theorem neutralIV106D1Energy_receiver
    (g f r : ℝ → ℝ) (A B M J : ℝ)
    (hg : Integrable g volume) (hf : Integrable f volume)
    (hr : Integrable r volume)
    (hB : 0 ≤ B) (hm : (∫ x, f x) = M)
    (hj : (∫ x, r x) ≤ J*M)
    (hbound : ∀ᵐ x ∂volume, A*f x - B*r x ≤ g x) :
    (A-B*J)*M ≤ ∫ x, g x := by
  have hi := integral_mono_ae ((hf.const_mul A).sub (hr.const_mul B)) hg hbound
  change (∫ x : ℝ, A * f x - B * r x) ≤ (∫ x : ℝ, g x) at hi
  rw [integral_sub (hf.const_mul A) (hr.const_mul B),
    integral_const_mul, integral_const_mul, hm] at hi
  have hmul := mul_le_mul_of_nonneg_left hj hB
  nlinarith only [hi, hmul]

#print axioms neutralIV106D1Log_tangent
#print axioms neutralIV106D1Energy_receiver
end
end WeilDefect
