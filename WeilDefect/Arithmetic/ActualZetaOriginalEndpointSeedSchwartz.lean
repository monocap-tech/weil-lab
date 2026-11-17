import WeilDefect.Arithmetic.ActualZetaOriginalEndpointMollifier
import WeilDefect.Arithmetic.ActualZetaOriginalRawWindowDictionary
import WeilDefect.Arithmetic.ActualZetaOriginalCollar242Correction

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-! NF581: package the literal real-valued seed as a compact smooth
complex Schwartz test, with the original moment-correction geometry.
The source amplitude is not replaced by a polynomial. -/

theorem neutralNF581Seed_originalCollars
    (h : ℝ → ℝ) (s : ℝ) (hs : 0 < s) (hs' : s < 1)
    (hh : ∀ u, u ∉ neutralNF578PositiveCollar → h u = 0)
    (x : ℝ) (hx : x ∉ neutralNF543OriginalCollars) :
    neutralNF579Seed h s hs' x = 0 := by
  apply neutralNF579Seed_supported h s hs hs' hh x
  · intro hp
    apply hx
    right
    change (11/10:ℝ)-1/500 < x ∧ x < 11/10
    change (549/500:ℝ) < x ∧ x < 11/10 at hp
    constructor <;> linarith [hp.1,hp.2]
  · intro hp
    apply hx
    left
    change -(11/10:ℝ) < x ∧ x < -(11/10:ℝ)+1/500
    change (549/500:ℝ) < -x ∧ -x < 11/10 at hp
    constructor <;> linarith [hp.1,hp.2]

/-- There is an actual Schwartz representative of the affine-mollified
seed, not an extra smooth-approximation existence assumption. -/
theorem neutralNF581Seed_existsSchwartz
    (h : ℝ → ℝ) (hi : Integrable h volume)
    (s : ℝ) (hs : 0 < s) (hs' : s < 1)
    (hh : ∀ u, u ∉ neutralNF578PositiveCollar → h u = 0) :
    ∃ g : 𝓢(ℝ,ℂ),
      (∀ x, g x = (neutralNF579Seed h s hs' x : ℂ)) ∧
      (∀ x, conj (g x) = g x) ∧
      (∀ x, g (-x) = -g x) ∧
      (∀ x, x ∉ neutralNF543OriginalCollars → g x = 0) := by
  let f : ℝ → ℂ := fun x => (neutralNF579Seed h s hs' x : ℂ)
  have hsm : ContDiff ℝ ∞ f :=
    Complex.ofRealCLM.contDiff.comp (neutralNF579Seed_smooth h hi s hs hs')
  have hc : ∀ x, x ∉ neutralNF543OriginalCollars → f x = 0 := by
    intro x hx
    simp [f,neutralNF581Seed_originalCollars h s hs hs' hh x hx]
  have hw : ∀ x, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0 := by
    intro x hx
    apply hc
    intro he
    apply hx
    rcases he with hl | hr
    · exact ⟨hl.1.le, by linarith [hl.2]⟩
    · exact ⟨by linarith [hr.1], hr.2.le⟩
  have hcomp : HasCompactSupport f :=
    exists_compact_iff_hasCompactSupport.mp ⟨_, isCompact_Icc, hw⟩
  let g : 𝓢(ℝ,ℂ) := hcomp.toSchwartzMap hsm
  have hg (x : ℝ) : g x = f x := rfl
  refine ⟨g, fun x => hg x, ?_, ?_, ?_⟩
  · intro x
    rw [hg]
    simp [f]
  · intro x
    rw [hg, hg]
    simp [f,neutralNF579Seed_odd h s hs' x]
  · intro x hx
    rw [hg]
    exact hc x hx

end
end WeilDefect
