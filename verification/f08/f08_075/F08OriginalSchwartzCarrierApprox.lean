import WeilDefect.Generated.F08.TerminalOriginalFixedSupportSmoothDensity
import WeilDefect.Arithmetic.ActualZetaLogCarrierSchwartzCompact

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ContDiff

/-- Strict interior Schwartz representatives are dense in the exact original
weighted Hilbert carrier. No Green-range or arithmetic attachment premise. -/
theorem f08_075_original_schwartzCarrier_approx
    {a : ℝ} (ha : 0 < a) (k : NeutralLogHilbertCarrier a)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ q : NeutralLogHilbertCarrier a, ∃ s : 𝓢(ℝ, ℂ),
      tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a ∧
      (∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) ∧
      neutralLogPhysical q.val = s.toLp 2 volume ∧
      ‖q - k‖ < ε := by
  obtain ⟨g, h, hh, hc, hs, hae, he⟩ :=
    f08_073_original_fixedSupport_smooth_approx ha
      (neutralLogHilbertToCanonical k) ε hε
  let s : 𝓢(ℝ, ℂ) := hc.toSchwartzMap hh
  let q : NeutralLogHilbertCarrier a := neutralCanonicalToLogHilbert g
  refine ⟨q, s, ?_, ?_, ?_, ?_⟩
  · change tsupport h ⊆ Set.Ioo (-a) a
    exact hs
  · intro x hx
    by_contra hn
    have hm : x ∈ Function.support h := by
      change h x ≠ 0 at hn
      exact hn
    have hi := hs (show x ∈ tsupport h from subset_closure hm)
    exact hx ⟨hi.1.le, hi.2.le⟩
  · change neutralLogPhysical (neutralLogWeightedL2 g) = s.toLp 2 volume
    rw [neutralLogPhysical_weighted]
    apply Lp.ext
    filter_upwards [hae, s.coeFn_toLp 2 volume] with x hx hy
    exact hx.trans hy.symm
  · have hk : neutralLogWeightedL2 (neutralLogHilbertToCanonical k) = k.val :=
      congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse k)
    rw [hk] at he
    change ‖neutralLogWeightedL2 g - k.val‖ < ε
    exact he

#print axioms f08_075_original_schwartzCarrier_approx
end
end WeilDefect
