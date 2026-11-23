import WeilDefect.Generated.F08.ActualMollifierWeightedDCT
import Mathlib.Analysis.SpecificLimits.Basic

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped FourierTransform Topology

/-!
F08-017. Actual explicit family of positive normalized C-infinity source physical
mollifiers, with radii exactly 2/(n+1) → 0. Discharges the last *sequence*
hypothesis of certified F08-013 and F08-015 weighted spectral convergence.

This is an explicit construction of ContDiffBump (0:ℝ), not an assumed
shrinking family and not an abstract multiplier. It does NOT establish
the Fourier/Plancherel identification of source physical convolutions in
the original weighted RealComplexL2 carrier, nor full supported density.
-/

/-- Explicit source-physical shrinking bump with inner radius 1/(n+1)
and outer radius 2/(n+1), centered exactly at zero in the real log coordinate.
The HasContDiffBump ℝ instance supplies the actual C-infinity function. -/
def f08_017_shrinkingBump (n : ℕ) : ContDiffBump (0 : ℝ) where
  rIn := ((n : ℝ) + 1)⁻¹
  rOut := 2 * ((n : ℝ) + 1)⁻¹
  rIn_pos := by positivity
  rIn_lt_rOut := by
    have hp : 0 < ((n : ℝ) + 1)⁻¹ := by positivity
    nlinarith

/-- The physical support radius is an explicit, genuine positive real number. -/
theorem f08_017_shrinkingBump_radius
    (n : ℕ) :
    (f08_017_shrinkingBump n).rOut =
      2 * (1 / ((n : ℝ) + 1)) := by
  simp [f08_017_shrinkingBump, one_div]

/-- No hypothesis on a bump sequence: the fully specified family shrinks. -/
theorem f08_017_shrinkingBump_radius_tendsto_zero :
    Tendsto (fun n : ℕ => (f08_017_shrinkingBump n).rOut)
      atTop (𝓝 (0 : ℝ)) := by
  simpa only [f08_017_shrinkingBump_radius, mul_zero] using
    ((tendsto_one_div_add_atTop_nhds_zero_nat :
      Tendsto (fun n : ℕ => (1 : ℝ) / ((n : ℝ) + 1))
        atTop (𝓝 (0 : ℝ))).const_mul 2)

/-- Every member is an actual smooth C-infinity complex function of real log
position and has unit complex mass, not merely a formal frequency symbol. -/
theorem f08_017_actual_shrinking_mollifier_smooth_mass_one
    (n : ℕ) :
    ContDiff ℝ (↑(⊤ : ℕ∞))
      (f08_011_complexMollifier (f08_017_shrinkingBump n)) ∧
    (∫ x : ℝ,
      f08_011_complexMollifier (f08_017_shrinkingBump n) x ∂volume) =
      (1 : ℂ) := by
  exact ⟨f08_011_complexMollifier_smooth _,
    f08_011_complexMollifier_integral _⟩

/-- Arbitrarily small fixed physical support collars are eventually satisfied
by the actual normalized compactly supported bump family. -/
theorem f08_017_actual_shrinking_mollifier_eventual_support
    (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop,
      Function.support
        (f08_011_complexMollifier (f08_017_shrinkingBump n)) ⊆
        Set.Icc (-ε) ε := by
  have hevent : ∀ᶠ n : ℕ in atTop,
      (f08_017_shrinkingBump n).rOut < ε :=
    f08_017_shrinkingBump_radius_tendsto_zero.eventually
      (eventually_lt_nhds hε)
  filter_upwards [hevent] with n hn
  exact f08_011_complexMollifier_support_epsilon
    (f08_017_shrinkingBump n) ε hn.le

/-- Unconditional Fourier multiplier pointwise convergence: the actual
explicit normalized source bump family has no remaining shrinking
sequence hypothesis. -/
theorem f08_017_explicit_mollifier_multiplier_tendsto_one
    (ξ : ℝ) :
    Tendsto
      (fun n : ℕ =>
        f08_015_originalMollifierMultiplier (f08_017_shrinkingBump n) ξ)
      atTop (𝓝 (1 : ℂ)) :=
  f08_015_original_mollifier_multiplier_tendsto_one
    f08_017_shrinkingBump f08_017_shrinkingBump_radius_tendsto_zero ξ

/-- Concrete, no-sequence-hypothesis original logarithmic-frequency weighted
dominated convergence for an actual constructed physical mollifier family.
Only the original source weighted-energy hypothesis on F remains. -/
theorem f08_017_explicit_mollifier_weighted_error_tendsto_zero
    (F : RealComplexL2)
    (hF : Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) volume) :
    Tendsto (fun n : ℕ => ∫ ξ : ℝ,
      logarithmicFourierWeight ξ *
        ‖(f08_015_originalMollifierMultiplier
            (f08_017_shrinkingBump n) ξ - 1) * F ξ‖ ^ 2 ∂volume)
      atTop (𝓝 (0 : ℝ)) :=
  f08_015_original_mollifier_weighted_error_tendsto_zero
    F hF f08_017_shrinkingBump
      f08_017_shrinkingBump_radius_tendsto_zero

#print axioms f08_017_shrinkingBump_radius
#print axioms f08_017_shrinkingBump_radius_tendsto_zero
#print axioms f08_017_actual_shrinking_mollifier_smooth_mass_one
#print axioms f08_017_actual_shrinking_mollifier_eventual_support
#print axioms f08_017_explicit_mollifier_multiplier_tendsto_one
#print axioms f08_017_explicit_mollifier_weighted_error_tendsto_zero

end
end WeilDefect
