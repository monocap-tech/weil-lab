import WeilDefect.Morphology.NeutralCanonicalFormDomain
import Mathlib.MeasureTheory.Function.LpSpace.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar

namespace WeilDefect
noncomputable section

open MeasureTheory

/-!
F08-027 first source-typed native L² dilation bridge. The rescaled
measure is the *actual pushforward* of Lebesgue volume, and not
Lebesgue volume itself. The corresponding composition map is a
genuine isometry between these two distinct L² measure spaces.

This module does NOT yet assert that sqrt(λ) * f(λ ·) is a same-volume
RealComplexL2 isometry, nor prove L² dilation strong continuity,
source Fourier scaling, fixed-support smooth core, or Weil positivity.
-/

/-- The actual frequency-space measure under multiplication by λ. -/
def f08_027_scaledFrequencyMeasure (lam : ℝ) : Measure ℝ :=
  Measure.map (fun ξ : ℝ => lam * ξ) volume

/-- Ordinary real scaling is measure preserving *to its pushforward
measure*. The claim with the same Lebesgue measure on both sides
would be false unless |λ| = 1. -/
theorem f08_027_scale_measurePreserving (lam : ℝ) :
    MeasurePreserving (fun ξ : ℝ => lam * ξ)
      volume (f08_027_scaledFrequencyMeasure lam) := by
  refine ⟨measurable_const_mul lam, ?_⟩
  rfl

/-- The exact Haar/Lebesgue Jacobian of nonzero one-dimensional
physical/frequency scaling, with no dropped measure factor. -/
theorem f08_027_scaledFrequencyMeasure_jacobian
    (lam : ℝ) (hlam : lam ≠ 0) :
    f08_027_scaledFrequencyMeasure lam =
      ENNReal.ofReal
        (abs ((lam ^ Module.finrank ℝ ℝ)⁻¹)) • (volume : Measure ℝ) := by
  change Measure.map (lam • ·) (volume : Measure ℝ) = _
  exact Measure.map_addHaar_smul (volume : Measure ℝ) hlam

/-- Genuine complex L² composition isometry with the correct source
measure. This is NOT an unweighted same-volume dilation operator. -/
def f08_027_nativeFrequencyPullback (lam : ℝ) :
    Lp ℂ 2 (f08_027_scaledFrequencyMeasure lam) →ₗᵢ[ℂ] RealComplexL2 :=
  Lp.compMeasurePreservingₗᵢ ℂ (fun ξ : ℝ => lam * ξ)
    (f08_027_scale_measurePreserving lam)

/-- The native isometry has exactly the L² norm of its element in
the appropriately pushed-forward source measure. -/
theorem f08_027_nativeFrequencyPullback_norm
    (lam : ℝ) (k : Lp ℂ 2 (f08_027_scaledFrequencyMeasure lam)) :
    ‖f08_027_nativeFrequencyPullback lam k‖ = ‖k‖ :=
  (f08_027_nativeFrequencyPullback lam).norm_map k

/-- Its concrete L² representative is the literal frequency-scaled
function almost everywhere with respect to original Lebesgue volume. -/
theorem f08_027_nativeFrequencyPullback_ae
    (lam : ℝ) (k : Lp ℂ 2 (f08_027_scaledFrequencyMeasure lam)) :
    (f08_027_nativeFrequencyPullback lam k : ℝ → ℂ) =ᵐ[volume]
      fun ξ => k (lam * ξ) := by
  exact Lp.coeFn_compMeasurePreserving k
    (f08_027_scale_measurePreserving lam)

#print axioms f08_027_scale_measurePreserving
#print axioms f08_027_scaledFrequencyMeasure_jacobian
#print axioms f08_027_nativeFrequencyPullback_norm
#print axioms f08_027_nativeFrequencyPullback_ae

end
end WeilDefect
