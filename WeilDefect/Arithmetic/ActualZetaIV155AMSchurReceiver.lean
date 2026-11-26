import WeilDefect.Arithmetic.ActualZetaIV153AMSignedIntegral
import WeilDefect.Arithmetic.ActualZetaIV154AMIntegrability

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators

/-- The physical row cap implies a bound for the weighted density sum,
including the zero-weight branch. This generic theorem does not assert
the row cap for a particular numerical certificate. -/
theorem neutralIV155Density_sum {ι : Type*} (P : Finset ι)
    (a s : ι → ℝ) (H f : ℝ → ℝ) (C x : ℝ)
    (hH : 0 ≤ H x) (hC : 0 ≤ C)
    (hz : H x = 0 → f x = 0)
    (hrow : f x ≠ 0 → ∑ n ∈ P, a n * (H (x+s n) + H (x+(-s n))) ≤ C*H x) :
    (∑ n ∈ P, a n * (neutralIV153Density H f (s n) x +
      neutralIV153Density H f (-s n) x)) ≤ C*f x^2 := by
  by_cases hf : f x = 0
  · simp [neutralIV153Density,hf]
  have hp : 0 < H x := lt_of_le_of_ne hH (Ne.symm (fun h => hf (hz h)))
  have he : (∑ n ∈ P, a n * (neutralIV153Density H f (s n) x +
      neutralIV153Density H f (-s n) x)) =
      (f x^2 / H x) * ∑ n ∈ P, a n * (H (x+s n)+H (x+(-s n))) := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro n hn
    unfold neutralIV153Density
    ring
  rw [he]
  calc
    _ ≤ (f x^2 / H x) * (C*H x) :=
      mul_le_mul_of_nonneg_left (hrow hf) (div_nonneg (sq_nonneg _) hH)
    _ = C*f x^2 := by field_simp [ne_of_gt hp] <;> ring

/-- Conditional finite symmetric Schur form estimate for real test
functions. Every analytic and pointwise hypothesis is explicit. -/
theorem neutralIV155Real_form {ι : Type*} (P : Finset ι)
    (a s : ι → ℝ) (H f : ℝ → ℝ) (C : ℝ)
    (ha : ∀ n ∈ P, 0 ≤ a n) (hH : ∀ x, 0 ≤ H x) (hC : 0 ≤ C)
    (hz : ∀ x, H x = 0 → f x = 0)
    (hf2 : Integrable (fun x : ℝ => f x^2))
    (hc : ∀ n ∈ P, Integrable (fun x : ℝ => f x*f (x+s n)))
    (hp : ∀ n ∈ P, Integrable (neutralIV153Density H f (s n)))
    (hm : ∀ n ∈ P, Integrable (neutralIV153Density H f (-s n)))
    (hrow : ∀ x, f x ≠ 0 →
      ∑ n ∈ P, a n * (H (x+s n)+H (x+(-s n))) ≤ C*H x) :
    (∑ n ∈ P, a n * ((∫ x : ℝ, f x*f (x+s n)) +
        (∫ x : ℝ, f x*f (x-s n)))) ≤ C*∫ x : ℝ, f x^2 := by
  let D : ι → ℝ → ℝ := fun n x => a n *
    (neutralIV153Density H f (s n) x + neutralIV153Density H f (-s n) x)
  have hD : ∀ n ∈ P, Integrable (D n) := by
    intro n hn
    exact ((hp n hn).add (hm n hn)).const_mul (a n)
  calc
    _ ≤ ∑ n ∈ P, ∫ x : ℝ, D n x := by
      apply Finset.sum_le_sum
      intro n hn
      have hi := neutralIV153Signed_integral H f (s n) hH hz (hc n hn)
        (hp n hn) (hm n hn) ((hm n hn).comp_add_right (s n))
      unfold D
      rw [integral_const_mul, integral_add (hp n hn) (hm n hn)]
      exact mul_le_mul_of_nonneg_left hi (ha n hn)
    _ = ∫ x : ℝ, ∑ n ∈ P, D n x := (integral_finsetSum P hD).symm
    _ ≤ ∫ x : ℝ, C*f x^2 := by
      apply integral_mono (integrable_finsetSum P hD) (hf2.const_mul C)
      intro x
      exact neutralIV155Density_sum P a s H f C x (hH x) hC (hz x) (hrow x)
    _ = _ := by rw [integral_const_mul]

/-- Absolute complex cross-integral domination, not just the real part.
No positivity of the translation operator is assumed. -/
theorem neutralIV155Complex_integral (f : ℝ → ℂ) (s : ℝ) :
    ‖∫ x : ℝ, f x * star (f (x+s))‖ ≤
      ∫ x : ℝ, ‖f x‖ * ‖f (x+s)‖ := by
  calc
    _ ≤ ∫ x : ℝ, ‖f x * star (f (x+s))‖ := norm_integral_le_integral_norm _
    _ = _ := by simp only [norm_mul, norm_star]

#print axioms neutralIV155Density_sum
#print axioms neutralIV155Real_form
#print axioms neutralIV155Complex_integral

end
end WeilDefect
