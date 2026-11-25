import WeilDefect.Generated.F08.OriginalSchwartzIntegrableSquareEnvelope
import WeilDefect.Generated.F08.OriginalSchwartzDilationPointwise
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology SchwartzMap

/-- Filtered Lebesgue dominated convergence of the exact normalized
compact-Schwartz representative squared difference, on the original
nonzero real scale subtype. Native Lp norm identification is separate. -/
theorem f08_051_originalCompactSchwartz_squareIntegral_tendsto
    (g : 𝓢(ℝ, ℂ)) (hg : HasCompactSupport (g : ℝ → ℂ)) :
    Tendsto
      (fun lam : f08_040_nonzeroScale =>
        ∫ ξ : ℝ, ‖(Complex.ofReal (Real.sqrt (abs lam.1))) •
          g (lam.1 * ξ) - g ξ‖ ^ 2 ∂volume)
      (𝓝 (⟨1, one_ne_zero⟩ : f08_040_nonzeroScale)) (𝓝 0) := by
  let oneScale : f08_040_nonzeroScale := ⟨1, one_ne_zero⟩
  let F : f08_040_nonzeroScale → ℝ → ℝ := fun lam ξ =>
    ‖(Complex.ofReal (Real.sqrt (abs lam.1))) • g (lam.1 * ξ) - g ξ‖ ^ 2
  obtain ⟨B, hB, _hBnonneg, hdom⟩ :=
    f08_048_originalSchwartz_integrableSquareEnvelope g hg
  have hnear : ∀ᶠ lam : f08_040_nonzeroScale in 𝓝 oneScale,
      (1 / 2 : ℝ) ≤ lam.1 ∧ lam.1 ≤ (3 / 2 : ℝ) := by
    have hv : Tendsto (fun lam : f08_040_nonzeroScale => lam.1)
        (𝓝 oneScale) (𝓝 (1 : ℝ)) :=
      continuous_subtype_val.continuousAt
    have hi : Set.Ioo (1 / 2 : ℝ) (3 / 2 : ℝ) ∈ 𝓝 (1 : ℝ) :=
      Ioo_mem_nhds (by norm_num) (by norm_num)
    filter_upwards [hv hi] with lam hlam
    exact ⟨le_of_lt hlam.1, le_of_lt hlam.2⟩
  have hm : ∀ᶠ lam in 𝓝 oneScale, AEStronglyMeasurable (F lam) volume := by
    apply Filter.Eventually.of_forall
    intro lam
    have he : Continuous (fun ξ : ℝ => g (lam.1 * ξ)) :=
      g.continuous.comp (continuous_const.mul continuous_id)
    have hs : Continuous (fun ξ : ℝ =>
        (Complex.ofReal (Real.sqrt (abs lam.1))) • g (lam.1 * ξ) - g ξ) :=
      (continuous_const.smul he).sub g.continuous
    exact (hs.norm.pow 2).aestronglyMeasurable
  have hb : ∀ᶠ lam in 𝓝 oneScale, ∀ᵐ ξ ∂volume, ‖F lam ξ‖ ≤ B ξ := by
    filter_upwards [hnear] with lam hlam
    apply Filter.Eventually.of_forall
    intro ξ
    have hnonneg : 0 ≤ F lam ξ := by
      dsimp [F]
      positivity
    rw [Real.norm_eq_abs, abs_of_nonneg hnonneg]
    exact hdom lam.1 ξ hlam.1 hlam.2
  have hp : ∀ᵐ ξ ∂volume, Tendsto (fun lam => F lam ξ)
      (𝓝 oneScale) (𝓝 ((fun _ : ℝ => (0 : ℝ)) ξ)) := by
    apply Filter.Eventually.of_forall
    intro ξ
    have h := f08_040_originalSchwartzDilation_pointwise_tendsto g ξ
    have hd := h.sub (tendsto_const_nhds (b := g ξ))
    simpa [F, oneScale] using (hd.norm.pow 2)
  have H := MeasureTheory.tendsto_integral_filter_of_dominated_convergence
    (F := F) (f := fun _ : ℝ => (0 : ℝ)) B hm hb hB hp
  simpa [F, oneScale] using H

#print axioms f08_051_originalCompactSchwartz_squareIntegral_tendsto

end
end WeilDefect
