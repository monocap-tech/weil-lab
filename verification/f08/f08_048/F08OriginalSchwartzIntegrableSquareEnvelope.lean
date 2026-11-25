import WeilDefect.Generated.F08.OriginalSchwartzNormalizedDifferenceBounds
import Mathlib.MeasureTheory.Integral.IntegrableOn
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap

/-- Common Lebesgue-integrable indicator envelope for the actual normalized
Schwartz difference squared, uniform for all scales in [1/2,3/2].
Frequency support only; no limit or physical form-core assertion. -/
theorem f08_048_originalSchwartz_integrableSquareEnvelope
    (g : 𝓢(ℝ, ℂ)) (hg : HasCompactSupport (g : ℝ → ℂ)) :
    ∃ B : ℝ → ℝ, Integrable B volume ∧
      (∀ ξ : ℝ, 0 ≤ B ξ) ∧
      ∀ lam ξ : ℝ, (1 / 2 : ℝ) ≤ lam → lam ≤ (3 / 2 : ℝ) →
        ‖(Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ) - g ξ‖ ^ 2 ≤ B ξ := by
  obtain ⟨R, hR, hs⟩ := f08_045_compactSchwartz_commonScaledSupport g hg
  obtain ⟨M, hM, hb⟩ := f08_046_originalSchwartz_normalizedDifferenceSquareBound g
  let C : ℝ := ((Real.sqrt (3 / 2 : ℝ) + 1) * M) ^ 2
  let I : Set ℝ := Set.Icc (-(2 * R)) (2 * R)
  have hI : MeasurableSet I := measurableSet_Icc
  have hfin : volume I ≠ ⊤ := by
    dsimp [I]
    rw [Real.volume_Icc]
    exact ENNReal.ofReal_ne_top
  have hconst : IntegrableOn (fun _ : ℝ => C) I volume :=
    integrableOn_const hfin
  refine ⟨I.indicator (fun _ : ℝ => C), hconst.integrable_indicator hI, ?_, ?_⟩
  · intro ξ
    by_cases hξ : ξ ∈ I
    · simpa [Set.indicator_of_mem hξ, C] using (sq_nonneg ((Real.sqrt (3 / 2 : ℝ) + 1) * M))
    · simp [Set.indicator_of_notMem hξ]
  · intro lam ξ hlo hhi
    by_cases hξ : ξ ∈ I
    · simpa [Set.indicator_of_mem hξ, C] using hb lam ξ hlo hhi
    · have hout : 2 * R < |ξ| := by
        by_contra! hh
        exact hξ (abs_le.mp hh)
      obtain ⟨h1, h2⟩ := hs lam ξ hlo hhi hout
      simp [Set.indicator_of_notMem hξ, h1, h2]

#print axioms f08_048_originalSchwartz_integrableSquareEnvelope

end
end WeilDefect
