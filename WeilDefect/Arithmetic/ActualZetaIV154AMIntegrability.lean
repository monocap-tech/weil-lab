import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory

/-- A bounded nonnegative weight ratio yields an integrable weighted
density for any measurable function with integrable square. The ratio
bound is required only where H is positive and f is nonzero. -/
theorem neutralIV154Density_integrable (H f : ℝ → ℝ) (s C : ℝ)
    (hH : Measurable H) (hf : Measurable f)
    (hH0 : ∀ x, 0 ≤ H x) (hC : 0 ≤ C)
    (hzero : ∀ x, H x = 0 → f x = 0)
    (hcap : ∀ x, 0 < H x → f x ≠ 0 → H (x+s) ≤ C*H x)
    (h2 : Integrable (fun x : ℝ => f x ^ 2)) :
    Integrable (fun x : ℝ => f x ^ 2 * H (x+s) / H x) := by
  have hm : Measurable (fun x : ℝ => f x ^ 2 * H (x+s) / H x) :=
    ((hf.pow_const 2).mul (hH.comp (measurable_id.add_const s))).div hH
  apply (h2.const_mul C).mono_nonneg hm.aestronglyMeasurable
  · filter_upwards [] with x
    exact div_nonneg (mul_nonneg (sq_nonneg _) (hH0 _)) (hH0 _)
  · filter_upwards [] with x
    by_cases hz : H x = 0
    · simp [hz, hzero x hz]
    by_cases hfx : f x = 0
    · simp [hfx]
    have hp : 0 < H x := lt_of_le_of_ne (hH0 x) (Ne.symm hz)
    apply (div_le_iff₀ hp).2
    calc
      f x ^ 2 * H (x+s) ≤ f x ^ 2 * (C*H x) :=
        mul_le_mul_of_nonneg_left (hcap x hp hfx) (sq_nonneg _)
      _ = C * f x ^ 2 * H x := by ring

/-- Translation of an integrable density requires no extra hypothesis. -/
theorem neutralIV154Translated_integrable (g : ℝ → ℝ) (s : ℝ)
    (hg : Integrable g) : Integrable (fun x : ℝ => g (x+s)) :=
  hg.comp_add_right s

/-- The complex cross term is dominated by the real absolute-value cross term. -/
theorem neutralIV154Complex_cross (z w : ℂ) :
    (z * star w).re ≤ ‖z‖ * ‖w‖ := by
  calc
    (z * star w).re ≤ ‖z * star w‖ := Complex.re_le_norm _
    _ = _ := by rw [norm_mul, norm_star]

#print axioms neutralIV154Density_integrable
#print axioms neutralIV154Translated_integrable
#print axioms neutralIV154Complex_cross

end
end WeilDefect
