import WeilDefect.Morphology.NeutralLogMetricTruncatedBounds
import Mathlib.MeasureTheory.Integral.Bochner.Set

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology

/-- Any increasing sequence of finite time intervals exhausting positive
 time recovers the genuinely convergent full jump density off the diagonal. -/
theorem neutralLogMetricTruncatedJumpDensity_tendsto
    (ε R : ℕ → ℝ)
    (hmono : Monotone (fun n => Icc (ε n) (R n)))
    (hcover : (⋃ n, Icc (ε n) (R n)) = Ioi (0 : ℝ))
    (r : ℝ) (hr : 0 < r) :
    Tendsto (fun n => neutralLogMetricTruncatedJumpDensity (ε n) (R n) r)
      atTop (𝓝 (neutralLogMetricJumpDensity r)) := by
  have hi : IntegrableOn (fun t : ℝ =>
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2))
      (⋃ n, Icc (ε n) (R n)) := by
    rw [hcover]
    exact neutralLogMetricJumpDensity_integrable r hr
  have ht := tendsto_setIntegral_of_monotone
    (fun n => measurableSet_Icc (a := ε n) (b := R n)) hmono hi
  have htwo : Tendsto (fun _ : ℕ => (2 : ℝ)) atTop (𝓝 (2 : ℝ)) :=
    tendsto_const_nhds
  simpa only [neutralLogMetricTruncatedJumpDensity,
    neutralLogMetricJumpDensity, hcover] using htwo.mul ht

/-- Signed spatial displacements have the same off-diagonal limit;
 the full density is evaluated at absolute distance. -/
theorem neutralLogMetricTruncatedJumpDensity_tendsto_abs
    (ε R : ℕ → ℝ)
    (hmono : Monotone (fun n => Icc (ε n) (R n)))
    (hcover : (⋃ n, Icc (ε n) (R n)) = Ioi (0 : ℝ))
    (r : ℝ) (hr : r ≠ 0) :
    Tendsto (fun n => neutralLogMetricTruncatedJumpDensity (ε n) (R n) r)
      atTop (𝓝 (neutralLogMetricJumpDensity |r|)) := by
  simpa only [neutralLogMetricTruncatedJumpDensity_abs] using
    neutralLogMetricTruncatedJumpDensity_tendsto ε R hmono hcover |r|
      (abs_pos.mpr hr)

end
end WeilDefect
