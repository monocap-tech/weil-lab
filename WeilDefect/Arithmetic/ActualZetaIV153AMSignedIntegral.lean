import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory

/-- Zero-safe weighted density. Division by zero is Lean's totalized
real division; f must vanish wherever the weight is zero. -/
def neutralIV153Density (H f : ℝ → ℝ) (s x : ℝ) : ℝ :=
  f x ^ 2 * H (x+s) / H x

theorem neutralIV153Young (a b p q : ℝ) (hp : 0 < p) (hq : 0 < q) :
    2*a*b ≤ a^2*q/p+b^2*p/q := by
  apply (mul_le_mul_right₀ (mul_pos hp hq)).mp
  calc
    (2*a*b)*(p*q) ≤ a^2*q^2+b^2*p^2 := by nlinarith [sq_nonneg (a*q-b*p)]
    _ = (a^2*q/p+b^2*p/q)*(p*q) := by
      field_simp [ne_of_gt hp, ne_of_gt hq] <;> ring

/-- Handles both positive and zero weights, including window endpoints. -/
theorem neutralIV153ZeroSafeYoung (H f : ℝ → ℝ) (s x : ℝ)
    (hH : ∀ y, 0 ≤ H y) (hf : ∀ y, H y = 0 → f y = 0) :
    2*f x*f (x+s) ≤
      neutralIV153Density H f s x + neutralIV153Density H f (-s) (x+s) := by
  have he : x+s+(-s) = x := by ring
  unfold neutralIV153Density
  rw [he]
  by_cases hx : H x = 0
  · simp [hx, hf x hx]
  by_cases hy : H (x+s) = 0
  · simp [hy, hf (x+s) hy]
  exact neutralIV153Young _ _ _ _
    (lt_of_le_of_ne (hH x) (Ne.symm hx))
    (lt_of_le_of_ne (hH (x+s)) (Ne.symm hy))

/-- Translation invariance for the reverse signed density. -/
theorem neutralIV153Reverse_integral (H f : ℝ → ℝ) (s : ℝ) :
    (∫ x : ℝ, neutralIV153Density H f (-s) (x+s)) =
      ∫ x : ℝ, neutralIV153Density H f (-s) x := by
  exact integral_add_right_eq_self (neutralIV153Density H f (-s)) s

theorem neutralIV153Cross_symmetry (f : ℝ → ℝ) (s : ℝ) :
    (∫ x : ℝ, f x*f (x+s)) = ∫ x : ℝ, f x*f (x-s) := by
  calc
    (∫ x : ℝ, f x*f (x+s)) =
        ∫ x : ℝ, f (x+s)*f ((x+s)-s) := by
          apply integral_congr_ae
          filter_upwards [] with x
          rw [show x+s-s=x by ring, mul_comm]
    _ = _ := integral_add_right_eq_self (fun x : ℝ => f x*f (x-s)) s

/-- The signed-pair cross integral is controlled by the two weighted
densities. Integrability is explicit; no physical regularity asserted. -/
theorem neutralIV153Signed_integral (H f : ℝ → ℝ) (s : ℝ)
    (hH : ∀ y, 0 ≤ H y) (hf : ∀ y, H y = 0 → f y = 0)
    (hc : Integrable (fun x : ℝ => f x*f (x+s)))
    (hp : Integrable (neutralIV153Density H f s))
    (hm : Integrable (neutralIV153Density H f (-s)))
    (hmt : Integrable (fun x : ℝ => neutralIV153Density H f (-s) (x+s))) :
    (∫ x : ℝ, f x*f (x+s)) + (∫ x : ℝ, f x*f (x-s)) ≤
      (∫ x : ℝ, neutralIV153Density H f s x) +
      (∫ x : ℝ, neutralIV153Density H f (-s) x) := by
  have hmono := integral_mono (hc.const_mul 2) (hp.add hmt)
    (fun x => by simpa only [mul_assoc] using neutralIV153ZeroSafeYoung H f s x hH hf)
  change (∫ x : ℝ, 2*(f x*f (x+s))) ≤
    ∫ x : ℝ, neutralIV153Density H f s x + neutralIV153Density H f (-s) (x+s) at hmono
  rw [integral_const_mul, integral_add hp hmt, neutralIV153Reverse_integral] at hmono
  rw [← neutralIV153Cross_symmetry f s]
  linarith

#print axioms neutralIV153Young
#print axioms neutralIV153ZeroSafeYoung
#print axioms neutralIV153Reverse_integral
#print axioms neutralIV153Cross_symmetry
#print axioms neutralIV153Signed_integral

end
end WeilDefect
