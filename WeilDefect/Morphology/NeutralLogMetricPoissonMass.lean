import WeilDefect.Morphology.NeutralLogMetricPoisson

namespace WeilDefect
noncomputable section
open MeasureTheory Real

/-- Exact reduction to the standard integrable Cauchy kernel. -/
theorem neutralLogMetricPoissonDensity_cauchy (t x : ℝ) (ht : 0 < t) :
    neutralLogMetricPoissonDensity t x =
      (2 / t) * (1 + ((2 * Real.pi / t) * x) ^ 2)⁻¹ := by
  have htne : t ≠ 0 := ne_of_gt ht
  have hd : t ^ 2 + 4 * Real.pi ^ 2 * x ^ 2 ≠ 0 := by
    have hh : 0 ≤ 4 * Real.pi ^ 2 * x ^ 2 := by positivity
    nlinarith [sq_pos_of_pos ht]
  have hc : 1 + ((2 * Real.pi / t) * x) ^ 2 ≠ 0 := by positivity
  unfold neutralLogMetricPoissonDensity
  field_simp [htne, hd, hc] <;> ring

/-- Physical integrability follows from the exact Cauchy reduction. -/
theorem neutralLogMetricPoissonDensity_integrable (t : ℝ) (ht : 0 < t) :
    Integrable (neutralLogMetricPoissonDensity t) := by
  have hb : 2 * Real.pi / t ≠ 0 := by positivity
  have h := (integrable_inv_one_add_mul_sq hb).const_mul (2 / t)
  have heq : neutralLogMetricPoissonDensity t =
      (fun x : ℝ => (2 / t) * (1 + ((2 * Real.pi / t) * x) ^ 2)⁻¹) := by
    funext x
    exact neutralLogMetricPoissonDensity_cauchy t x ht
  rw [heq]
  exact h

/-- The density is positive everywhere for positive Poisson time. -/
theorem neutralLogMetricPoissonDensity_positive (t x : ℝ) (ht : 0 < t) :
    0 < neutralLogMetricPoissonDensity t x := by
  unfold neutralLogMetricPoissonDensity
  have hden : 0 < t ^ 2 + 4 * Real.pi ^ 2 * x ^ 2 := by
    have hh : 0 ≤ 4 * Real.pi ^ 2 * x ^ 2 := by positivity
    nlinarith [sq_pos_of_pos ht]
  exact div_pos (by linarith) hden

/-- Exact mass one, with the project's 2*pi normalization. -/
theorem neutralLogMetricPoissonDensity_integral (t : ℝ) (ht : 0 < t) :
    (∫ x : ℝ, neutralLogMetricPoissonDensity t x) = 1 := by
  have heq : neutralLogMetricPoissonDensity t =
      (fun x : ℝ => (2 / t) * (1 + ((2 * Real.pi / t) * x) ^ 2)⁻¹) := by
    funext x
    exact neutralLogMetricPoissonDensity_cauchy t x ht
  rw [heq, integral_const_mul, integral_univ_inv_one_add_mul_sq,
    abs_of_pos (by positivity : 0 < 2 * Real.pi / t)]
  field_simp [ne_of_gt ht, ne_of_gt Real.pi_pos] <;> ring

/-- The absolute mass also equals one, supplying the convolution L1 budget. -/
theorem neutralLogMetricPoissonDensity_norm_integral (t : ℝ) (ht : 0 < t) :
    (∫ x : ℝ, ‖neutralLogMetricPoissonDensity t x‖) = 1 := by
  have heq : (fun x : ℝ => ‖neutralLogMetricPoissonDensity t x‖) =
      neutralLogMetricPoissonDensity t := by
    funext x
    rw [Real.norm_eq_abs, abs_of_pos (neutralLogMetricPoissonDensity_positive t x ht)]
  rw [heq]
  exact neutralLogMetricPoissonDensity_integral t ht

end
end WeilDefect
