import WeilDefect.MasterRecon.V08B
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-! V08C: quantitative logarithmic frequency tail and compact cutoff
receiver. The frequency density is the actual squared complex norm.
The Plancherel identity and compactness of each bounded-band operator
must still be attached to the supported logarithmic carrier. -/
namespace WeilDefect.MasterRecon.V08C

open MeasureTheory Set Filter
open scoped Topology

theorem log_tail_bound (μ : Measure ℝ) (F : ℝ → ℂ) (R : ℝ)
    (hR : 0 ≤ R) (hF : Integrable (fun u => ‖F u‖ ^ 2) μ)
    (hw : Integrable (fun u => Real.log (2 + |u|) * ‖F u‖ ^ 2) μ) :
    (∫ u in {u : ℝ | R < |u|}, ‖F u‖ ^ 2 ∂μ) ≤
      (∫ u, Real.log (2 + |u|) * ‖F u‖ ^ 2 ∂μ) /
        Real.log (2 + R) := by
  have hp : 0 < Real.log (2 + R) := Real.log_pos (by linarith)
  have hs : MeasurableSet {u : ℝ | R < |u|} :=
    measurableSet_lt measurable_const measurable_id.abs
  have h₁ : (∫ u in {u : ℝ | R < |u|},
      Real.log (2 + R) * ‖F u‖ ^ 2 ∂μ) ≤
      (∫ u in {u : ℝ | R < |u|},
        Real.log (2 + |u|) * ‖F u‖ ^ 2 ∂μ) := by
    apply setIntegral_mono_on (hF.const_mul _).integrableOn hw.integrableOn hs
    intro u hu
    have hu' : R < |u| := hu
    apply mul_le_mul_of_nonneg_right _ (sq_nonneg _)
    exact Real.log_le_log (by linarith) (by linarith)
  have h₂ : (∫ u in {u : ℝ | R < |u|},
      Real.log (2 + |u|) * ‖F u‖ ^ 2 ∂μ) ≤
      ∫ u, Real.log (2 + |u|) * ‖F u‖ ^ 2 ∂μ := by
    apply setIntegral_le_integral hw
    filter_upwards with u
    exact mul_nonneg (Real.log_nonneg (by linarith [abs_nonneg u])) (sq_nonneg _)
  rw [integral_const_mul] at h₁
  apply (le_div_iff₀ hp).2
  rw [mul_comm]
  exact h₁.trans h₂

theorem exp_cutoff_tail (μ : Measure ℝ) (F : ℝ → ℂ) (n : ℕ) (B : ℝ)
    (hB : 0 ≤ B)
    (hF : Integrable (fun u => ‖F u‖ ^ 2) μ)
    (hw : Integrable (fun u => Real.log (2 + |u|) * ‖F u‖ ^ 2) μ)
    (henergy : (∫ u, Real.log (2 + |u|) * ‖F u‖ ^ 2 ∂μ) ≤ B) :
    (∫ u in {u : ℝ | Real.exp ((n : ℝ) + 1) < |u|},
      ‖F u‖ ^ 2 ∂μ) ≤ B / ((n : ℝ) + 1) := by
  let R := Real.exp ((n : ℝ) + 1)
  have hR : 0 < R := Real.exp_pos _
  have hlog : (n : ℝ) + 1 ≤ Real.log (2 + R) := by
    have h := Real.log_le_log hR (by linarith : R ≤ 2 + R)
    change Real.log (Real.exp ((n : ℝ) + 1)) ≤ _ at h
    rw [Real.log_exp] at h
    exact h
  have hp : 0 < Real.log (2 + R) := Real.log_pos (by linarith)
  calc
    (∫ u in {u : ℝ | R < |u|}, ‖F u‖ ^ 2 ∂μ) ≤
        (∫ u, Real.log (2 + |u|) * ‖F u‖ ^ 2 ∂μ) /
          Real.log (2 + R) := log_tail_bound μ F R hR.le hF hw
    _ ≤ B / Real.log (2 + R) := div_le_div_of_nonneg_right henergy hp.le
    _ ≤ B / ((n : ℝ) + 1) := div_le_div_of_nonneg_left hB (by positivity) hlog

variable {H L : Type*}
variable [NormedAddCommGroup H] [NormedSpace ℂ H]
variable [NormedAddCommGroup L] [NormedSpace ℂ L] [CompleteSpace L]

theorem compact_of_squared_cutoff_error
    (C : H →L[ℂ] L) (P : ℕ → H →L[ℂ] L)
    (hP : ∀ n, IsCompactOperator (P n))
    (herr : ∀ n x, ‖C x - P n x‖ ^ 2 ≤ ‖x‖ ^ 2 / ((n : ℝ) + 1)) :
    IsCompactOperator C := by
  have hlim : Tendsto P atTop (𝓝 C) := by
    apply Metric.tendsto_atTop.2
    intro e he
    obtain ⟨N, hN⟩ := Metric.tendsto_atTop.1
      (tendsto_one_div_add_atTop_nhds_zero_nat (𝕜 := ℝ))
      ((e / 2) ^ 2) (by positivity)
    refine ⟨N, fun n hn => ?_⟩
    have hh := hN n hn
    rw [Real.dist_eq, sub_zero, abs_of_nonneg (by positivity)] at hh
    have hop : ‖P n - C‖ ≤ e / 2 := by
      apply ContinuousLinearMap.opNorm_le_bound _ (by positivity)
      intro x
      change ‖P n x - C x‖ ≤ e / 2 * ‖x‖
      rw [norm_sub_rev]
      have hsq := herr n x
      have hmul := mul_le_mul_of_nonneg_left hh.le (sq_nonneg ‖x‖)
      have hsq' : ‖C x - P n x‖ ^ 2 ≤ (e / 2 * ‖x‖) ^ 2 := by
        calc
          _ ≤ ‖x‖ ^ 2 / ((n : ℝ) + 1) := hsq
          _ ≤ ‖x‖ ^ 2 * (e / 2) ^ 2 := by
            simpa only [div_eq_mul_inv, one_div] using hmul
          _ = _ := by ring
      exact (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp hsq'
    rw [dist_eq_norm]
    exact hop.trans_lt (by linarith)
  exact isCompactOperator_of_tendsto hlim (Eventually.of_forall hP)

/-- Attach the actual log-tail integral to an abstract band cutoff
operator. No identification of arbitrary cutoffs with Fourier
projections is claimed. -/
theorem compact_of_log_frequency_cutoffs
    (μ : Measure ℝ) (C : H →L[ℂ] L) (P : ℕ → H →L[ℂ] L)
    (F : H → ℝ → ℂ) (hP : ∀ n, IsCompactOperator (P n))
    (hF : ∀ x, Integrable (fun u => ‖F x u‖ ^ 2) μ)
    (hw : ∀ x, Integrable (fun u => Real.log (2 + |u|) * ‖F x u‖ ^ 2) μ)
    (henergy : ∀ x, (∫ u, Real.log (2 + |u|) * ‖F x u‖ ^ 2 ∂μ) ≤ ‖x‖ ^ 2)
    (htail : ∀ n x, ‖C x - P n x‖ ^ 2 =
      ∫ u in {u : ℝ | Real.exp ((n : ℝ) + 1) < |u|}, ‖F x u‖ ^ 2 ∂μ) :
    IsCompactOperator C := by
  apply compact_of_squared_cutoff_error C P hP
  intro n x
  rw [htail]
  exact exp_cutoff_tail μ (F x) n _ (sq_nonneg _) (hF x) (hw x) (henergy x)

end WeilDefect.MasterRecon.V08C

#print axioms WeilDefect.MasterRecon.V08C.log_tail_bound
#print axioms WeilDefect.MasterRecon.V08C.exp_cutoff_tail
#print axioms WeilDefect.MasterRecon.V08C.compact_of_squared_cutoff_error
#print axioms WeilDefect.MasterRecon.V08C.compact_of_log_frequency_cutoffs
