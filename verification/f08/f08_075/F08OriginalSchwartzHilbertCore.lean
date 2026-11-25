import WeilDefect.Generated.F08.TerminalOriginalFixedSupportSmoothDensity
import WeilDefect.Morphology.NeutralLogHilbertCarrier
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap Topology

/-- The physical representatives in the certified fixed-window core are
actual supported Schwartz functions in the complete original weighted carrier.
No source arithmetic equality or Green representability is assumed. -/
theorem f08_075_originalSchwartzHilbert_approx
    (a : ℝ) (ha : 0 < a) (k : NeutralLogHilbertCarrier a)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ q : NeutralLogHilbertCarrier a, ∃ s : 𝓢(ℝ, ℂ),
      tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a ∧
      (∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) ∧
      neutralLogPhysical q.val = s.toLp 2 volume ∧
      ‖q - k‖ < ε := by
  let f := neutralLogHilbertToCanonical k
  obtain ⟨g, h, hsm, hcompact, hsupp, hae, herr⟩ :=
    f08_073_original_fixedSupport_smooth_approx ha f ε hε
  let s : 𝓢(ℝ, ℂ) := hcompact.toSchwartzMap hsm
  have hsg : (s : ℝ → ℂ) = h := rfl
  have hgs : g.val = s.toLp 2 volume := by
    apply Lp.ext_iff.mpr
    have hs := s.coeFn_toLp 2 (volume : Measure ℝ)
    rw [hsg] at hs
    exact hae.trans hs.symm
  refine ⟨neutralCanonicalToLogHilbert g, s, ?_, ?_, ?_, ?_⟩
  · rw [hsg]
    exact hsupp
  · intro x hx
    by_contra hn
    have hmem : x ∈ Function.support h := by
      change h x ≠ 0
      simpa only [← hsg] using hn
    have hinner := hsupp (subset_closure hmem)
    exact hx ⟨hinner.1.le, hinner.2.le⟩
  · change neutralLogPhysical (neutralLogWeightedL2 g) = _
    rw [neutralLogPhysical_weighted]
    exact hgs
  · have hk : neutralLogWeightedL2 f = k.val :=
      congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse k)
    change ‖neutralLogWeightedL2 g - k.val‖ < ε
    rw [hk] at herr
    exact herr

/-- The exact carrier lift of the original canonical Schwartz representative
is forced by physical equality, not an additional choice of coordinates. -/
theorem f08_075_originalHilbert_eq_of_physical_eq
    {a : ℝ} (p q : NeutralLogHilbertCarrier a)
    (h : neutralLogPhysical p.val = neutralLogPhysical q.val) : p = q := by
  have hc : neutralLogHilbertToCanonical p = neutralLogHilbertToCanonical q := by
    apply Subtype.ext
    exact h
  calc
    p = neutralCanonicalToLogHilbert (neutralLogHilbertToCanonical p) :=
      (neutralLogHilbertToCanonical_rightInverse p).symm
    _ = neutralCanonicalToLogHilbert (neutralLogHilbertToCanonical q) :=
      congrArg neutralCanonicalToLogHilbert hc
    _ = q := neutralLogHilbertToCanonical_rightInverse q

#print axioms f08_075_originalSchwartzHilbert_approx
#print axioms f08_075_originalHilbert_eq_of_physical_eq

end
end WeilDefect
