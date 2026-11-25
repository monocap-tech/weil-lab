import WeilDefect.Generated.F08.NativeLogDilationFactor
import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology

/-- Frequency measurability of the exact original logarithmic correction. -/
theorem f08_057_logDilationFactor_continuous (lam : ℝ) :
    Continuous (fun xi : ℝ => f08_025_logDilationFactor lam xi) := by
  unfold f08_025_logDilationFactor
  apply Real.continuous_sqrt.comp
  apply logarithmicFourierWeight_continuous.div
    (logarithmicFourierWeight_continuous.comp (continuous_const.mul continuous_id))
  intro xi
  exact ne_of_gt (lt_of_lt_of_le zero_lt_one
    (one_le_logarithmicFourierWeight (lam * xi)))

/-- Uniform squared error of the exact correction on inward scales. -/
theorem f08_057_logDilationFactor_sub_one_sq_le
    (lam xi : ℝ) (hlo : (1 / 2 : ℝ) ≤ lam) (hhi : lam ≤ 1) :
    (f08_025_logDilationFactor lam xi - 1) ^ 2 ≤ 2 + Real.log 2 := by
  have h := f08_025_logDilationFactor_sq_le lam xi hlo hhi
  have hn := f08_025_logDilationFactor_nonneg lam xi
  nlinarith

/-- Exact fixed-vector correction error tends to zero as scales approach
one from the inward interval. No physical Fourier scaling is asserted. -/
theorem f08_057_logDilationFixedVector_error_tendsto (k : RealComplexL2) :
    Tendsto (fun lam : ℝ =>
      ∫ xi : ℝ, (f08_025_logDilationFactor lam xi - 1) ^ 2 *
        ‖k xi‖ ^ 2 ∂volume)
      (𝓝[Set.Icc (1 / 2 : ℝ) 1] (1 : ℝ)) (𝓝 (0 : ℝ)) := by
  let l := 𝓝[Set.Icc (1 / 2 : ℝ) 1] (1 : ℝ)
  let F : ℝ → ℝ → ℝ := fun lam xi =>
    (f08_025_logDilationFactor lam xi - 1) ^ 2 * ‖k xi‖ ^ 2
  let B : ℝ → ℝ := fun xi => (2 + Real.log 2) * ‖k xi‖ ^ 2
  have hk : Integrable (fun xi : ℝ => ‖k xi‖ ^ 2) volume :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable k)).mp (Lp.memLp k)
  have hB : Integrable B volume := hk.const_mul _
  have hm : ∀ᶠ lam in l, AEStronglyMeasurable (F lam) volume := by
    apply Filter.Eventually.of_forall
    intro lam
    exact (((f08_057_logDilationFactor_continuous lam).sub continuous_const).pow 2).aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable k).norm.pow 2)
  have hnear : ∀ᶠ lam in l, lam ∈ Set.Icc (1 / 2 : ℝ) 1 :=
    self_mem_nhdsWithin
  have hb : ∀ᶠ lam in l, ∀ᵐ xi ∂volume, ‖F lam xi‖ ≤ B xi := by
    filter_upwards [hnear] with lam hlam
    apply Filter.Eventually.of_forall
    intro xi
    have hn : 0 ≤ F lam xi := by
      dsimp [F]
      positivity
    rw [Real.norm_eq_abs, abs_of_nonneg hn]
    exact mul_le_mul_of_nonneg_right
      (f08_057_logDilationFactor_sub_one_sq_le lam xi hlam.1 hlam.2) (sq_nonneg _)
  have hp : ∀ᵐ xi ∂volume, Tendsto (fun lam => F lam xi) l
      (𝓝 ((fun _ : ℝ => (0 : ℝ)) xi)) := by
    apply Filter.Eventually.of_forall
    intro xi
    have h : Tendsto (fun lam : ℝ => f08_025_logDilationFactor lam xi) l (𝓝 (1 : ℝ)) :=
      (f08_025_logDilationFactor_tendsto_one xi).mono_left nhdsWithin_le_nhds
    have hs : Tendsto (fun lam => f08_025_logDilationFactor lam xi - 1) l (𝓝 (0 : ℝ)) := by
      simpa using h.sub_const (1 : ℝ)
    simpa [F] using (hs.pow 2).mul_const (‖k xi‖ ^ 2)
  have H := MeasureTheory.tendsto_integral_filter_of_dominated_convergence
    (F := F) (f := fun _ : ℝ => (0 : ℝ)) B hm hb hB hp
  simpa [F, l] using H

#print axioms f08_057_logDilationFactor_continuous
#print axioms f08_057_logDilationFactor_sub_one_sq_le
#print axioms f08_057_logDilationFixedVector_error_tendsto

end
end WeilDefect
