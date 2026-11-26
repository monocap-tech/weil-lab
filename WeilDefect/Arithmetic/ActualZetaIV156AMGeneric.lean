import WeilDefect.Arithmetic.ActualZetaIV155AMSchurReceiver

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators

/-- Extract a single positive signed coefficient from the nonnegative
row sum. This makes the density integrability bound follow from the
same row certificate rather than a separate global ratio bank. -/
theorem neutralIV156Ratio_cap {ι : Type*} (P : Finset ι)
    (a s : ι → ℝ) (H : ℝ → ℝ) (C x : ℝ) (n : ι) (hn : n ∈ P)
    (ha : ∀ k ∈ P, 0 ≤ a k) (han : 0 < a n)
    (hH : ∀ y, 0 ≤ H y)
    (hr : ∑ k ∈ P, a k*(H (x+s k)+H (x+(-s k))) ≤ C*H x) :
    H (x+s n) ≤ (C/a n)*H x ∧ H (x+(-s n)) ≤ (C/a n)*H x := by
  have hterm : a n*(H (x+s n)+H (x+(-s n))) ≤ C*H x :=
    (Finset.single_le_sum (f := fun k => a k*(H (x+s k)+H (x+(-s k))))
      (fun k hk => mul_nonneg (ha k hk) (add_nonneg (hH _) (hH _))) hn).trans hr
  constructor
  · have hh : H (x+s n)*a n ≤ C*H x := by
      calc
        _ ≤ a n*(H (x+s n)+H (x+(-s n))) := by
          rw [mul_comm (H (x+s n))]
          exact mul_le_mul_of_nonneg_left (le_add_of_nonneg_right (hH _)) han.le
        _ ≤ _ := hterm
    rw [div_mul_eq_mul_div]
    exact (le_div_iff₀ han).2 hh
  · have hh : H (x+(-s n))*a n ≤ C*H x := by
      calc
        _ ≤ a n*(H (x+s n)+H (x+(-s n))) := by
          rw [mul_comm (H (x+(-s n)))]
          exact mul_le_mul_of_nonneg_left (le_add_of_nonneg_left (hH _)) han.le
        _ ≤ _ := hterm
    rw [div_mul_eq_mul_div]
    exact (le_div_iff₀ han).2 hh

/-- Discharge both density integrability hypotheses from the same row
cap and positive coefficients, for measurable f with integrable square. -/
theorem neutralIV156Real_form {ι : Type*} (P : Finset ι)
    (a s : ι → ℝ) (H f : ℝ → ℝ) (C : ℝ)
    (ha : ∀ n ∈ P, 0 < a n) (hH : ∀ x, 0 ≤ H x) (hC : 0 ≤ C)
    (hHm : Measurable H) (hfm : Measurable f)
    (hz : ∀ x, H x = 0 → f x = 0)
    (hf2 : Integrable (fun x : ℝ => f x^2))
    (hc : ∀ n ∈ P, Integrable (fun x : ℝ => f x*f (x+s n)))
    (hrow : ∀ x, f x ≠ 0 →
      ∑ n ∈ P, a n * (H (x+s n)+H (x+(-s n))) ≤ C*H x) :
    (∑ n ∈ P, a n * ((∫ x : ℝ, f x*f (x+s n)) +
        (∫ x : ℝ, f x*f (x-s n)))) ≤ C*∫ x : ℝ, f x^2 := by
  have ha0 : ∀ n ∈ P, 0 ≤ a n := fun n hn => (ha n hn).le
  apply neutralIV155Real_form P a s H f C ha0 hH hC hz hf2 hc
  · intro n hn
    exact neutralIV154Density_integrable H f (s n) (C/a n) hHm hfm hH
      (div_nonneg hC (ha0 n hn)) hz
      (fun x _ hfx => (neutralIV156Ratio_cap P a s H C x n hn ha0 (ha n hn) hH (hrow x hfx)).1) hf2
  · intro n hn
    exact neutralIV154Density_integrable H f (-s n) (C/a n) hHm hfm hH
      (div_nonneg hC (ha0 n hn)) hz
      (fun x _ hfx => (neutralIV156Ratio_cap P a s H C x n hn ha0 (ha n hn) hH (hrow x hfx)).2) hf2
  · exact hrow

/-- Absolute complex finite sum comparison. The real Schur form
receives the norm function, without treating A as positive. -/
theorem neutralIV156Complex_form {ι : Type*} (P : Finset ι)
    (a s : ι → ℝ) (f : ℝ → ℂ)
    (ha : ∀ n ∈ P, 0 ≤ a n) :
    ‖∑ n ∈ P, (a n:ℂ) * ((∫ x : ℝ, f x * star (f (x+s n))) +
      (∫ x : ℝ, f x * star (f (x-s n))))‖ ≤
      ∑ n ∈ P, a n * ((∫ x : ℝ, ‖f x‖*‖f (x+s n)‖) +
        (∫ x : ℝ, ‖f x‖*‖f (x-s n)‖)) := by
  apply le_trans (norm_sum_le _ _)
  apply Finset.sum_le_sum
  intro n hn
  rw [norm_mul, Complex.norm_real, Real.norm_of_nonneg (ha n hn)]
  apply mul_le_mul_of_nonneg_left _ (ha n hn)
  apply le_trans (norm_add_le _ _)
  apply add_le_add
  · exact neutralIV155Complex_integral f (s n)
  · simpa only [sub_eq_add_neg] using neutralIV155Complex_integral f (-s n)

#print axioms neutralIV156Ratio_cap
#print axioms neutralIV156Real_form
#print axioms neutralIV156Complex_form
end
end WeilDefect
