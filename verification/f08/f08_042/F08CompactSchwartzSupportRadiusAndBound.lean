import WeilDefect.Morphology.NeutralCanonicalFormDomain
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic
import Mathlib.Topology.MetricSpace.Bounded

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap

/-!
F08-042: source-native compact-Schwartz domination prerequisites.

These statements concern the true real-frequency Schwartz functions whose
native complex Lebesgue L² images are dense by original F08-037.
The finite radius makes the common finite-support envelope for λ near one
possible. The seminorm bound supplies a source-exact global amplitude.

Neither statement asserts an L² dominated-convergence theorem.
The original F08-030 a.e. representative and F08-040 pointwise limit must
still be integrated and converted through the original Lp equivalence class.
Neither bound says physical Fourier inverse support is compact.
-/

/-- Genuine compact Schwartz support is contained in some symmetric
finite real interval, expressed as zero outside that interval. -/
theorem f08_042_compactSchwartz_supportRadius
    (g : 𝓢(ℝ, ℂ)) (hg : HasCompactSupport (g : ℝ → ℂ)) :
    ∃ R : ℝ, 0 ≤ R ∧ ∀ ξ : ℝ, R < |ξ| → g ξ = 0 := by
  have hcompact : IsCompact (tsupport (g : ℝ → ℂ)) := hg.isCompact
  obtain ⟨r, hr⟩ := hcompact.isBounded.subset_closedBall (0 : ℝ)
  refine ⟨max 0 r, le_max_left _ _, ?_⟩
  intro ξ hξ
  by_contra hne
  have hmem : ξ ∈ Function.support (g : ℝ → ℂ) := hne
  have htsupport : ξ ∈ tsupport (g : ℝ → ℂ) :=
    subset_tsupport (g : ℝ → ℂ) hmem
  have hclosed : ξ ∈ Metric.closedBall (0 : ℝ) r := hr htsupport
  have hbound : |ξ| ≤ r := by
    simpa [Metric.mem_closedBall, Real.dist_eq] using hclosed
  exact (not_lt_of_ge (hbound.trans (le_max_right 0 r))) hξ

/-- The original Schwartz seminorm gives a global norm bound for the
same genuine complex-valued Schwartz representative. -/
theorem f08_042_originalSchwartz_globalBound
    (g : 𝓢(ℝ, ℂ)) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ ξ : ℝ, ‖g ξ‖ ≤ M := by
  refine ⟨SchwartzMap.seminorm ℝ 0 0 g, ?_, ?_⟩
  · positivity
  · intro ξ
    exact SchwartzMap.norm_le_seminorm ℝ g ξ

#print axioms f08_042_compactSchwartz_supportRadius
#print axioms f08_042_originalSchwartz_globalBound

end
end WeilDefect
