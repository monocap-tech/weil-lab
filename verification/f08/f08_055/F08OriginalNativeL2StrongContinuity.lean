import WeilDefect.Generated.F08.OriginalCompactSchwartzFilteredDCT
import WeilDefect.Generated.F08.OriginalNativeL2SquareIntegral
import WeilDefect.Generated.F08.CompactSchwartzNativeL2Dense
import WeilDefect.Generated.F08.NativeL2ContinuityDenseTransfer

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology SchwartzMap

/-- Strong continuity on the actual compact-Schwartz image in the
original complex Lebesgue L². The square integral is exactly the
native difference norm squared, not merely a pointwise proxy. -/
theorem f08_055_originalCompactSchwartz_native_tendsto
    (g : 𝓢(ℝ, ℂ)) (hg : HasCompactSupport (g : ℝ → ℂ)) :
    Tendsto
      (fun lam : f08_038_nonzeroScale =>
        f08_030_nativeFrequencyDilation lam.1 lam.2
          (SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ) g))
      (𝓝 (⟨1, one_ne_zero⟩ : f08_038_nonzeroScale))
      (𝓝 (SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ) g)) := by
  let k : RealComplexL2 := SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ) g
  have hs : Tendsto
      (fun lam : f08_038_nonzeroScale =>
        ‖f08_030_nativeFrequencyDilation lam.1 lam.2 k - k‖ ^ 2)
      (𝓝 (⟨1, one_ne_zero⟩ : f08_038_nonzeroScale)) (𝓝 (0 : ℝ)) := by
    simpa only [k, f08_052_originalSchwartz_nativeDifference_norm_sq] using
      f08_051_originalCompactSchwartz_squareIntegral_tendsto g hg
  change Tendsto
    (fun lam : f08_038_nonzeroScale => f08_030_nativeFrequencyDilation lam.1 lam.2 k)
    (𝓝 (⟨1, one_ne_zero⟩ : f08_038_nonzeroScale)) (𝓝 k)
  rw [Metric.tendsto_nhds]
  intro ε hε
  have hsmall := (Metric.tendsto_nhds.mp hs) (ε ^ 2) (by positivity)
  filter_upwards [hsmall] with lam hlam
  rw [Real.dist_eq, sub_zero, abs_of_nonneg (sq_nonneg _)] at hlam
  rw [dist_eq_norm]
  by_contra! hge
  have hprod := mul_nonneg (sub_nonneg.mpr hge)
    (add_nonneg (norm_nonneg (f08_030_nativeFrequencyDilation lam.1 lam.2 k - k)) hε.le)
  nlinarith

/-- Unconditional strong continuity at scale one of the original
normalized complex L² frequency dilation, on every native L² vector.
No compact-support hypothesis on k and no assumed dense-core limit. -/
theorem f08_055_originalNativeL2_dilation_tendsto (k : RealComplexL2) :
    Tendsto
      (fun lam : f08_038_nonzeroScale =>
        f08_030_nativeFrequencyDilation lam.1 lam.2 k)
      (𝓝 (⟨1, one_ne_zero⟩ : f08_038_nonzeroScale)) (𝓝 k) := by
  refine f08_038_nativeL2_tendsto_of_dense_core _
    f08_037_compactSchwartz_denseInOriginalL2 ?_ k
  intro v hv
  obtain ⟨g, hg, rfl⟩ := hv
  exact f08_055_originalCompactSchwartz_native_tendsto g hg

#print axioms f08_055_originalCompactSchwartz_native_tendsto
#print axioms f08_055_originalNativeL2_dilation_tendsto

end
end WeilDefect
