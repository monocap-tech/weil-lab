import WeilDefect.Morphology.NeutralLogMetricLaplace
import WeilDefect.Morphology.NeutralLogMetricTruncatedLimit
import WeilDefect.Arithmetic.LogarithmicForm

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology

/-- Increasing finite time cutoffs recover the exact existing
 logarithmic weight at every frequency, including zero. -/
theorem neutralLogMetricLaplaceCutoff_tendsto
    (ε R : ℕ → ℝ)
    (hmono : Monotone (fun n => Icc (ε n) (R n)))
    (hcover : (⋃ n, Icc (ε n) (R n)) = Ioi (0 : ℝ)) (ξ : ℝ) :
    Tendsto (fun n => 1 + ∫ t in Icc (ε n) (R n),
      neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t)
      atTop (𝓝 (logarithmicFourierWeight ξ)) := by
  have hi : IntegrableOn (neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ|)
      (⋃ n, Icc (ε n) (R n)) := by
    rw [hcover]
    exact neutralLogMetricLaplaceIntegrand_integrable _ _ (Real.exp_pos _) (abs_nonneg ξ)
  have ht := tendsto_setIntegral_of_monotone
    (fun n => measurableSet_Icc (a := ε n) (b := R n)) hmono hi
  rw [hcover] at ht
  have h1 : Tendsto (fun _ : ℕ => (1 : ℝ)) atTop (𝓝 (1 : ℝ)) :=
    tendsto_const_nhds
  have h := h1.add ht
  rw [← neutralLogMetricLaplace_weight |ξ| (abs_nonneg ξ)] at h
  exact h

/-- The concrete reciprocal/natural exhaustion recovers log(e+|ξ|). -/
theorem neutralLogMetricLaplaceCutoff_natural_tendsto (ξ : ℝ) :
    Tendsto (fun n : ℕ => 1 +
      ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
        neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t)
      atTop (𝓝 (logarithmicFourierWeight ξ)) := by
  exact neutralLogMetricLaplaceCutoff_tendsto
    (fun n => 1 / ((n : ℝ) + 1)) (fun n => (n : ℝ) + 1)
    neutralLogMetricTimeCutoff_monotone neutralLogMetricTimeCutoff_iUnion ξ

/-- The complex Laplace coefficient of the cancelled Poisson multiplier
 converges to the canonical logarithmic multiplier. -/
theorem neutralLogMetricPoissonLaplaceCoefficient_tendsto (ξ : ℝ) :
    Tendsto (fun n : ℕ => (1 : ℂ) +
      ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (1 - (Real.exp (-t * |ξ|) : ℂ)))
      atTop (𝓝 (logarithmicFourierWeight ξ : ℂ)) := by
  have he (t : ℝ) :
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (1 - (Real.exp (-t * |ξ|) : ℂ)) =
      (neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t : ℂ) := by
    have ht : -t * |ξ| = -|ξ| * t := by ring
    rw [ht]
    unfold neutralLogMetricLaplaceIntegrand
    push_cast
    ring
  simp_rw [he, integral_complex_ofReal]
  have hc := (Complex.continuous_ofReal.tendsto (logarithmicFourierWeight ξ)).comp
    (neutralLogMetricLaplaceCutoff_natural_tendsto ξ)
  simpa only [Complex.ofReal_add, Complex.ofReal_one] using hc

end
end WeilDefect
