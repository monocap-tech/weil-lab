import WeilDefect.Arithmetic.ActualZetaPhaseIVLocalSpan
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap

/-!
NF738 canonical Phase IV: actual source-specific original literal signed EF
local-coercivity theorem on ARBITRARY FINITE complex linear combinations of
Schwartz functions all supported in the same frozen two original collars.

This is an exact infinite-dimensional (within a fixed support class)
consequence of Lean-accepted NF600, without a new numerical matrix bank.

The older symbols neutralNF735* are historical Phase IV source identifiers.
Nothing here identifies the fixed-window form with a global arbitrary-support
Weil form or proves positivity of mixtures across distinct translated windows.
-/

/-- Original-collar support is preserved by ANY finite complex linear
combination, not merely the two-generator combination proved in NF736's
legacy-named local-span module. -/
theorem neutralNF738OriginalCollars_finset_linear
    {ι : Type*} (F : Finset ι)
    (s : ι → 𝓢(ℝ,ℂ)) (c : ι → ℂ)
    (hs : ∀ i ∈ F, neutralNF735InOriginalCollars (s i)) :
    neutralNF735InOriginalCollars (∑ i ∈ F, c i • s i) := by
  classical
  induction F using Finset.induction_on with
  | empty =>
      intro x hx
      simp
  | @insert i F hi ih =>
      have hsi : neutralNF735InOriginalCollars (s i) :=
        hs i (Finset.mem_insert_self i F)
      have hrest : ∀ j ∈ F, neutralNF735InOriginalCollars (s j) := by
        intro j hj
        exact hs j (Finset.mem_insert_of_mem hj)
      have hhead : neutralNF735InOriginalCollars (c i • s i) :=
        neutralNF735OriginalCollars_smul (c i) (s i) hsi
      have htail : neutralNF735InOriginalCollars (∑ j ∈ F, c j • s j) :=
        ih hrest
      simpa [Finset.sum_insert hi] using
        neutralNF735OriginalCollars_add (c i • s i)
          (∑ j ∈ F, c j • s j) hhead htail

/-- Actual literal zeta EF 2/5 signed coercivity for every FINITE complex
linear combination within the original two-collar support E. This is the
existing strong NF600 universal support theorem applied to a finite sum,
not a new numerical certificate or a global support-exhaustion theorem. -/
theorem neutralNF738OriginalFiniteCollarSpan_coercive
    {ι : Type*} (F : Finset ι)
    (s : ι → 𝓢(ℝ,ℂ)) (c : ι → ℂ)
    (hs : ∀ i ∈ F, neutralNF735InOriginalCollars (s i)) :
    (2/5:ℝ) * ‖(∑ i ∈ F, c i • s i).toLp 2 volume‖^2 ≤
      neutralNF598SmoothWeil (∑ i ∈ F, c i • s i) := by
  exact neutralNF600SmoothCollarLower _
    (neutralNF738OriginalCollars_finset_linear F s c hs)

/-- Actual literal original fixed-window EF is nonnegative on every
finite complex span INSIDE E. No new support location is asserted. -/
theorem neutralNF738OriginalFiniteCollarSpan_nonnegative
    {ι : Type*} (F : Finset ι)
    (s : ι → 𝓢(ℝ,ℂ)) (c : ι → ℂ)
    (hs : ∀ i ∈ F, neutralNF735InOriginalCollars (s i)) :
    0 ≤ neutralNF598SmoothWeil (∑ i ∈ F, c i • s i) := by
  have h := neutralNF738OriginalFiniteCollarSpan_coercive F s c hs
  have h0 : (0 : ℝ) ≤
      (2/5:ℝ) * ‖(∑ i ∈ F, c i • s i).toLp 2 volume‖^2 := by
    positivity
  exact h0.trans h

/-- A genuinely nonzero finite local superposition has strictly positive
literal EF value. Nonzeroness is a separate hypothesis, not smuggled in
from individual nonzero generators (which might cancel). -/
theorem neutralNF738OriginalFiniteCollarSpan_positive
    {ι : Type*} (F : Finset ι)
    (s : ι → 𝓢(ℝ,ℂ)) (c : ι → ℂ)
    (hs : ∀ i ∈ F, neutralNF735InOriginalCollars (s i))
    (hne : (∑ i ∈ F, c i • s i).toLp 2 volume ≠ 0) :
    0 < neutralNF598SmoothWeil (∑ i ∈ F, c i • s i) := by
  have h := neutralNF738OriginalFiniteCollarSpan_coercive F s c hs
  have hn : 0 < ‖(∑ i ∈ F, c i • s i).toLp 2 volume‖ :=
    norm_pos_iff.mpr hne
  have hp : (0:ℝ) <
      (2/5:ℝ) * ‖(∑ i ∈ F, c i • s i).toLp 2 volume‖^2 :=
    mul_pos (by norm_num) (sq_pos_of_pos hn)
  exact hp.trans_le h

#print axioms neutralNF738OriginalCollars_finset_linear
#print axioms neutralNF738OriginalFiniteCollarSpan_coercive
#print axioms neutralNF738OriginalFiniteCollarSpan_nonnegative
#print axioms neutralNF738OriginalFiniteCollarSpan_positive

end
end WeilDefect
