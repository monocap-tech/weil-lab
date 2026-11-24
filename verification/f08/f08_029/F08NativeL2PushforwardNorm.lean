import WeilDefect.Generated.F08.NativeFrequencyScalingMeasure

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal

/-!
F08-029: rigorous source-native passage of a genuine RealComplexL2
element to the correctly scaled frequency pushforward measure, preserving
the Lp equivalence-class/a.e. semantics and recording the *exact*
ENNReal norm factor. No claim of same-volume unitary rescaling or
strong continuity is made here.
-/

/-- Every original complex L² vector remains square-integrable after the
true nonzero physical/frequency scaling measure is substituted. -/
theorem f08_029_volumeLp_memLp_pushforward
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    MemLp (fun ξ : ℝ => k ξ) 2
      (f08_027_scaledFrequencyMeasure lam) := by
  rw [f08_027_scaledFrequencyMeasure_jacobian lam hlam]
  exact (Lp.memLp k).smul_measure (by simp)

/-- Genuine L² equivalence class under the correct pushforward frequency
measure; this is a change of measure, not dilation composition. -/
def f08_029_volumeLpToPushforward
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    Lp ℂ 2 (f08_027_scaledFrequencyMeasure lam) :=
  (f08_029_volumeLp_memLp_pushforward lam hlam k).toLp
    (fun ξ : ℝ => k ξ)

/-- No pointwise representative ambiguity is introduced by the native
Lp change of measure. -/
theorem f08_029_volumeLpToPushforward_ae
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    (f08_029_volumeLpToPushforward lam hlam k : ℝ → ℂ) =ᵐ[
      f08_027_scaledFrequencyMeasure lam] fun ξ => k ξ := by
  exact (f08_029_volumeLp_memLp_pushforward lam hlam k).coeFn_toLp

/-- Exact L² extended norm transformation under source measure rescaling.
The factor is not one: multiplication by λ alone does NOT preserve volume. -/
theorem f08_029_volumeLp_eLpNorm_jacobian
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    eLpNorm (fun ξ : ℝ => k ξ) 2
      (f08_027_scaledFrequencyMeasure lam) =
    (ENNReal.ofReal
        (abs ((lam ^ Module.finrank ℝ ℝ)⁻¹))) ^
        ((1 / (2 : ℝ≥0∞)).toReal) •
      eLpNorm (fun ξ : ℝ => k ξ) 2 volume := by
  have hc :
      ENNReal.ofReal (abs ((lam ^ Module.finrank ℝ ℝ)⁻¹)) ≠ 0 := by
    apply ENNReal.ofReal_ne_zero_iff.mpr
    exact abs_pos.mpr (inv_ne_zero (pow_ne_zero _ hlam))
  rw [f08_027_scaledFrequencyMeasure_jacobian lam hlam]
  exact eLpNorm_smul_measure_of_ne_zero hc
    (fun ξ : ℝ => k ξ) 2 (volume : Measure ℝ)

/-- Exact norm formula for the native complex L² class in the new measure,
rather than an illicit isometry claim without normalization. -/
theorem f08_029_volumeLpToPushforward_norm
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    ‖f08_029_volumeLpToPushforward lam hlam k‖ =
      ENNReal.toReal
        ((ENNReal.ofReal
            (abs ((lam ^ Module.finrank ℝ ℝ)⁻¹))) ^
            ((1 / (2 : ℝ≥0∞)).toReal) •
          eLpNorm (fun ξ : ℝ => k ξ) 2 volume) := by
  change
    ‖(f08_029_volumeLp_memLp_pushforward lam hlam k).toLp
      (fun ξ : ℝ => k ξ)‖ = _
  rw [Lp.norm_toLp]
  rw [f08_029_volumeLp_eLpNorm_jacobian lam hlam k]

#print axioms f08_029_volumeLp_memLp_pushforward
#print axioms f08_029_volumeLpToPushforward_ae
#print axioms f08_029_volumeLp_eLpNorm_jacobian
#print axioms f08_029_volumeLpToPushforward_norm

end
end WeilDefect
