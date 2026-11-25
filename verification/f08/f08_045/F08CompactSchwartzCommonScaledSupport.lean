import WeilDefect.Generated.F08.CompactSchwartzSupportRadiusAndBound

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap

/-!
F08-045: one common source-frequency support interval for a compact Schwartz
function g and its scaled representative g (lam * xi) near the identity.

This theorem uses the actual F08-042 original finite support-radius theorem,
and its conclusion concerns actual source Schwartz representatives, never
pointwise values of arbitrary RealComplexL2 equivalence classes.

This is one mathematical prerequisite for the original F08-030 normalized
dilation's common integrable squared-difference envelope. It does NOT
claim domination, dominated convergence, L² norm convergence, original
weighted physical form-core density, signed Weil positivity or RH.
-/

/-- A single interval [-2R, 2R] contains the support of the original
Schwartz representative g and that of g (lam * ·) for every real
lam between 1/2 and 3/2. -/
theorem f08_045_compactSchwartz_commonScaledSupport
    (g : 𝓢(ℝ, ℂ)) (hg : HasCompactSupport (g : ℝ → ℂ)) :
    ∃ R : ℝ, 0 ≤ R ∧
      ∀ lam ξ : ℝ,
        (1 / 2 : ℝ) ≤ lam →
        lam ≤ (3 / 2 : ℝ) →
        2 * R < |ξ| →
          g ξ = 0 ∧ g (lam * ξ) = 0 := by
  obtain ⟨R, hR, hgR⟩ := f08_042_compactSchwartz_supportRadius g hg
  refine ⟨R, hR, ?_⟩
  intro lam ξ hlam_low _hlam_high hout
  have hlam_nonneg : 0 ≤ lam := by linarith
  have hξR : R < |ξ| := by linarith
  have hscaled : R < |lam * ξ| := by
    rw [abs_mul, abs_of_nonneg hlam_nonneg]
    have hscale : (1 / 2 : ℝ) * |ξ| ≤ lam * |ξ| :=
      mul_le_mul_of_nonneg_right hlam_low (abs_nonneg ξ)
    have hhalf : R < (1 / 2 : ℝ) * |ξ| := by linarith
    exact lt_of_lt_of_le hhalf hscale
  exact ⟨hgR ξ hξR, hgR (lam * ξ) hscaled⟩

#print axioms f08_045_compactSchwartz_commonScaledSupport

end
end WeilDefect
