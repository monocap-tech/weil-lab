import WeilDefect.Generated.F08.OriginalMollifierFourierLimit
import WeilDefect.Generated.F08.OriginalWeightedMollifierMultiplier

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped FourierTransform Topology

/-!
F08-015 — genuinely constructed original-source mollifier multipliers satisfy
every premise of the original weighted logarithmic Fourier dominated-convergence
gate F08-005, not only abstract assumed Fourier multipliers.

The actual positive complex C-infinity physical function is F08-011; its
Fourier contraction is F08-011; its exact negative-2π Fourier convergence
is F08-013; the original logarithmic weight and weighted DCT are F08-005.

This does not construct the shrinking-radius bump sequence: hr is explicit.
This does not assert the physical convolution/Fourier Plancherel domain bridge,
smooth fixed-radius core density, or source signed Weil form positivity.
-/

/-- Actual ordinary Fourier multiplier of a genuine F08-011 normalized
compactly supported complex physical mollifier in source log coordinates. -/
def f08_015_originalMollifierMultiplier
    (φ : ContDiffBump (0 : ℝ)) (ξ : ℝ) : ℂ :=
  (𝓕 (f08_011_complexMollifier φ)) ξ

/-- A genuine integrable physical mollifier has a continuous ordinary
complex Fourier multiplier, not just a stipulated measurable one. -/
theorem f08_015_original_mollifier_multiplier_continuous
    (φ : ContDiffBump (0 : ℝ)) :
    Continuous (f08_015_originalMollifierMultiplier φ) := by
  change Continuous (𝓕 (f08_011_complexMollifier φ))
  exact VectorFourier.fourierIntegral_continuous
    Real.continuous_fourierChar (innerSL ℝ).continuous₂
    (f08_011_complexMollifier_integrable φ)

/-- The actual physical Fourier multiplier satisfies the exact
almost-everywhere strongly measurable premise of F08-005. -/
theorem f08_015_original_mollifier_multiplier_measurable
    (φ : ContDiffBump (0 : ℝ)) :
    AEStronglyMeasurable (f08_015_originalMollifierMultiplier φ) volume :=
  (f08_015_original_mollifier_multiplier_continuous φ).aestronglyMeasurable

/-- The existing unit-mass, nonnegative physical source bump produces
an actual norm-one bounded complex multiplier, not an abstract estimate. -/
theorem f08_015_original_mollifier_multiplier_contraction
    (φ : ContDiffBump (0 : ℝ)) (ξ : ℝ) :
    ‖f08_015_originalMollifierMultiplier φ ξ‖ ≤ 1 :=
  f08_011_complexMollifier_fourier_norm_le_one φ ξ

/-- Actual mollifier multiplier deviation has integrable squared error
against the original logarithmic Weil form frequency weight, provided
the original source frequency representative has finite form energy. -/
theorem f08_015_original_mollifier_log_error_integrable
    (F : RealComplexL2)
    (hF : Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) volume)
    (φ : ContDiffBump (0 : ℝ)) :
    Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ *
        ‖(f08_015_originalMollifierMultiplier φ ξ - 1) * F ξ‖ ^ 2)
      volume := by
  exact f08_005_log_multiplier_error_integrable F hF
    (f08_015_originalMollifierMultiplier φ)
    (f08_015_original_mollifier_multiplier_measurable φ)
    (f08_015_original_mollifier_multiplier_contraction φ)

/-- A genuine sequence of physical normalized compact smooth bumps whose
actual support radii shrink to zero satisfies F08-005's pointwise limit
premise for the exact original Fourier transform. -/
theorem f08_015_original_mollifier_multiplier_tendsto_one
    (φ : ℕ → ContDiffBump (0 : ℝ))
    (hr : Tendsto (fun n => (φ n).rOut) atTop (𝓝 (0 : ℝ)))
    (ξ : ℝ) :
    Tendsto (fun n => f08_015_originalMollifierMultiplier (φ n) ξ)
      atTop (𝓝 (1 : ℂ)) :=
  f08_013_original_mollifier_fourier_tendsto_one φ hr ξ

/-- Actual instantiated original-source logarithmic Fourier weighted
dominated convergence of genuine physical mollifier multipliers, with no
abstract multiplier measurability, contraction, or convergence hypothesis.
The only family hypothesis is shrinking true source support radii. -/
theorem f08_015_original_mollifier_weighted_error_tendsto_zero
    (F : RealComplexL2)
    (hF : Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) volume)
    (φ : ℕ → ContDiffBump (0 : ℝ))
    (hr : Tendsto (fun n => (φ n).rOut) atTop (𝓝 (0 : ℝ))) :
    Tendsto (fun n => ∫ ξ : ℝ,
      logarithmicFourierWeight ξ *
        ‖(f08_015_originalMollifierMultiplier (φ n) ξ - 1) *
          F ξ‖ ^ 2 ∂volume)
      atTop (𝓝 (0 : ℝ)) := by
  apply f08_005_log_multiplier_error_tendsto_zero F hF
    (fun n ξ => f08_015_originalMollifierMultiplier (φ n) ξ)
  · intro n
    exact f08_015_original_mollifier_multiplier_measurable (φ n)
  · intro n ξ
    exact f08_015_original_mollifier_multiplier_contraction (φ n) ξ
  · intro ξ
    exact f08_015_original_mollifier_multiplier_tendsto_one φ hr ξ

#print axioms f08_015_original_mollifier_multiplier_continuous
#print axioms f08_015_original_mollifier_multiplier_measurable
#print axioms f08_015_original_mollifier_multiplier_contraction
#print axioms f08_015_original_mollifier_log_error_integrable
#print axioms f08_015_original_mollifier_multiplier_tendsto_one
#print axioms f08_015_original_mollifier_weighted_error_tendsto_zero

end
end WeilDefect
