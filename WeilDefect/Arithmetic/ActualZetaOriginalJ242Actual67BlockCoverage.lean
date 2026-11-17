import WeilDefect.Arithmetic.ActualZetaOriginalJ242SourceFunctions
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
NF567 — original 67 distinct frequency block INDEX COMPLETENESS.

This standalone file imports the genuine NF545 original 67 pair table
and 241 flattened monomial-frequency nodes, with NO pending NF561
analytic oscillator differentiation, NF565 dual polynomial or NF550
physical Gram dependencies.

For every original frequency group and each historical order k<m_g,
it identifies a literal authentic original 241-column index carrying
that exact ordered pair. It also checks the true 67-block
multiplicity sum 241. No source interpolation or surrogate basis.
-/

/-- Original group at an *actual* one of the 67 frozen rational
NF407 frequency/multiplicity pairs, no reordering. -/
def neutralNF567OriginalGroupAt (g : Fin 67) : ℚ × ℕ :=
  nf545OriginalSelectedFrequencyGroups[g.val]'(by
    simpa only [nf545OriginalFrequencyGroupCount] using g.isLt)

/-- Real angular frequency of the frozen g-th original group. -/
def neutralNF567OriginalGroupOmega (g : Fin 67) : ℝ :=
  2 * Real.pi * ((neutralNF567OriginalGroupAt g).1 : ℝ)

/-- Every frozen source group has strictly positive multiplicity;
this is the exact 67-element original NF407 table, not a
hypothetical collection of blocks. -/
private theorem neutralNF567OriginalAllGroupMultiplicities_pos :
    ∀ g : Fin 67, 0 < (neutralNF567OriginalGroupAt g).2 := by
  decide +kernel

theorem neutralNF567OriginalGroupAt_multiplicity_pos (g : Fin 67) :
    0 < (neutralNF567OriginalGroupAt g).2 :=
  neutralNF567OriginalAllGroupMultiplicities_pos g

/-- Direct exact ORIGINAL 67-block multiplicity budget from the
frozen NF407 table: 241 oscillator directions before the sinh
pole, not an abstract Hermite interpolation dimension. -/
theorem neutralNF567OriginalAll67GroupMultiplicities_sum :
    (∑ g : Fin 67, (neutralNF567OriginalGroupAt g).2) = 241 := by
  decide +kernel

/-- For every genuine frequency group g and EVERY k in its
original range, recover a specific genuine Fin241 oscillator
column carrying exactly (f_g,k). This is the source-index
completeness hypothesis required by the 67-block Hermite argument,
proved rather than assumed. -/
theorem neutralNF567OriginalEveryBlockOrder_isActualSource
    (g : Fin 67) (k : ℕ)
    (hk : k < (neutralNF567OriginalGroupAt g).2) :
    ∃ i : Fin 241,
      nf545OriginalOscillatorNodeAt i =
        ((neutralNF567OriginalGroupAt g).1, k) := by
  have hg :
      neutralNF567OriginalGroupAt g ∈
        nf545OriginalSelectedFrequencyGroups := by
    unfold neutralNF567OriginalGroupAt
    exact List.get_mem _ _
  have hr :
      k ∈ List.range (neutralNF567OriginalGroupAt g).2 :=
    List.mem_range.mpr hk
  have hm :
      ((neutralNF567OriginalGroupAt g).1, k) ∈
        nf545OriginalSelectedOscillatorNodes := by
    unfold nf545OriginalSelectedOscillatorNodes
    apply List.mem_flatMap.mpr
    refine ⟨neutralNF567OriginalGroupAt g, hg, ?_⟩
    apply List.mem_map.mpr
    exact ⟨k, hr, rfl⟩
  obtain ⟨idx, hidx⟩ := List.mem_iff_get.mp hm
  have hbound : idx.val < 241 := by
    simpa only [nf545OriginalSelectedOscillatorNodes_length] using idx.isLt
  refine ⟨⟨idx.val, hbound⟩, ?_⟩
  simpa only [nf545OriginalOscillatorNodeAt, List.get_eq_getElem] using hidx


end
end WeilDefect
