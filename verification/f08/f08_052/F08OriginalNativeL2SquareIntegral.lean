import WeilDefect.Generated.F08.NativeFrequencyDilation
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic
import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal SchwartzMap InnerProductSpace

/-- The original Lebesgue complex L² norm squared is the actual
integral of the pointwise representative's squared norm. -/
theorem f08_052_originalL2_norm_sq_eq_integral (k : RealComplexL2) :
    ‖k‖ ^ 2 = ∫ ξ : ℝ, ‖k ξ‖ ^ 2 ∂volume := by
  calc
    ‖k‖ ^ 2 = RCLike.re (inner ℂ k k) := norm_sq_eq_re_inner k
    _ = RCLike.re (∫ ξ : ℝ, inner ℂ (k ξ) (k ξ) ∂volume) := by
      rw [MeasureTheory.L2.inner_def]
    _ = ∫ ξ : ℝ, RCLike.re (inner ℂ (k ξ) (k ξ)) ∂volume := by
      exact (integral_re (MeasureTheory.L2.integrable_inner (𝕜 := ℂ) k k)).symm
    _ = ∫ ξ : ℝ, ‖k ξ‖ ^ 2 ∂volume := by
      apply integral_congr_ae
      exact Filter.Eventually.of_forall (fun ξ => (norm_sq_eq_re_inner (k ξ)).symm)

/-- Exact original normalized dilation difference norm for native
Schwartz-to-Lp images. All representative substitutions are a.e.;
the scaled substitution uses the actual pushforward Jacobian. -/
theorem f08_052_originalSchwartz_nativeDifference_norm_sq
    (g : 𝓢(ℝ, ℂ)) (lam : ℝ) (hlam : lam ≠ 0) :
    ‖f08_030_nativeFrequencyDilation lam hlam
        (SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ) g) -
        (SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ) g)‖ ^ 2 =
      ∫ ξ : ℝ, ‖(Complex.ofReal (Real.sqrt (abs lam))) •
        g (lam * ξ) - g ξ‖ ^ 2 ∂volume := by
  let k : RealComplexL2 := SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ) g
  change ‖f08_030_nativeFrequencyDilation lam hlam k - k‖ ^ 2 = _
  have hk : (k : ℝ → ℂ) =ᵐ[volume] (g : ℝ → ℂ) := by
    simpa only [k, SchwartzMap.toLpCLM_apply] using
      g.coeFn_toLp 2 (volume : Measure ℝ)
  have hac : f08_027_scaledFrequencyMeasure lam ≪ (volume : Measure ℝ) := by
    rw [f08_027_scaledFrequencyMeasure_jacobian lam hlam]
    exact Measure.smul_absolutelyContinuous
  have hkg := (f08_027_scale_measurePreserving lam).quasiMeasurePreserving.ae_eq_comp
    (hac.ae_eq hk)
  rw [f08_052_originalL2_norm_sq_eq_integral]
  apply integral_congr_ae
  filter_upwards [Lp.coeFn_sub (f08_030_nativeFrequencyDilation lam hlam k) k,
    f08_030_nativeFrequencyDilation_ae lam hlam k, hk, hkg] with ξ hsub hd hplain hscaled
  change k (lam * ξ) = g (lam * ξ) at hscaled
  simp only [Pi.sub_apply, hsub, hd, hplain, hscaled]

#print axioms f08_052_originalL2_norm_sq_eq_integral
#print axioms f08_052_originalSchwartz_nativeDifference_norm_sq

end
end WeilDefect
