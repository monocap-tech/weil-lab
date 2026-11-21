import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalFourCellSignedCapacity
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWholeThreeCellSchwartzPartition
import Mathlib.Analysis.Distribution.SchwartzSpace.CompactSupport
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric
open scoped SchwartzMap ComplexConjugate

/-!
IV023 — THE ACTUAL ORIGINAL FOUR-CELL COMPLEX SCHWARTZ PARTITION.

Historical source:
* unchanged two strict NF543 original collars;
* first added cell [+1/5 ±1/500] from IV020/021;
* second added cell [-1/5 ±1/4000] from IV022.

IV021 proved (as a Lean source candidate) a real Schwartz-preserving
smooth cut separating the FIRST new cell from the frozen collars.
IV023 supplies the MISSING SECOND smooth cut, then composes the
two actual continuous Schwartz multipliers. Thus every physical
complex Schwartz function f supported in the full four-cell union
admits an ACTUAL decomposition

    f = f_old + f_first + f_second

where every term has the claimed literal real physical support.
No discontinuous indicator, finite Gram basis, assumed projection
equivalence, spectral eigenvector or positivity axiom is used.

These are pending direct kernel compilation and standard axiom audit.
-/

/-- A smooth Mathlib C-infinity compact bump centered at the new
SECOND real source coordinate -1/5, with a plateau of radius1/20
and outer support radius1/10. The entire second interval is inside
the plateau and the complete ORIGINAL first three-cell support is
outside the outer ball. The cutoff is an auxiliary proof coordinate. -/
def neutralIV023SecondCutoff : ContDiffBump (-(1/5:ℝ)) :=
  ⟨(1/20:ℝ), (1/10:ℝ), by norm_num, by norm_num⟩

/-- The new second cutoff is EXACTLY ONE on the entire second
closed real interval, not merely at its center. -/
theorem neutralIV023SecondCutoff_one
    (x : ℝ) (hx : x ∈ neutralIV022FourthCellInterval) :
    neutralIV023SecondCutoff x = 1 := by
  apply neutralIV023SecondCutoff.one_of_mem_closedBall
  have hdist : dist x (-(1/5:ℝ)) ≤ (1/20:ℝ) := by
    rw [Real.dist_eq]
    unfold neutralIV022FourthCellInterval at hx
    apply abs_le.mpr
    constructor <;> linarith [hx.1,hx.2]
  simpa only [Metric.mem_closedBall] using hdist

/-- The same real smooth cutoff is EXACTLY ZERO on the full
ORIGINAL three-cell region: BOTH unchanged NF543 collars
AND the entire first-new doubled-radius interval. -/
theorem neutralIV023SecondCutoff_base_zero
    (x : ℝ) (hx : x ∈ neutralIV020WideThreeCellSupport) :
    neutralIV023SecondCutoff x = 0 := by
  apply neutralIV023SecondCutoff.zero_of_le_dist
  change (1/10:ℝ) ≤ dist x (-(1/5:ℝ))
  rw [Real.dist_eq]
  change x ∈ neutralNF543OriginalCollars ∪
    neutralIV020WidePhysicalInterval at hx
  rcases hx with hOld | hFirst
  · rcases hOld with hL | hR
    · rw [abs_of_neg (by linarith [hL.2])]
      linarith [hL.2]
    · rw [abs_of_pos (by linarith [hR.1])]
      linarith [hR.1]
  · unfold neutralIV020WidePhysicalInterval at hFirst
    rw [abs_of_pos (by linarith [hFirst.1])]
    linarith [hFirst.1]

/-- Smooth compact support gives genuine Schwartz-multiplier
admissibility: temperate growth is checked in Mathlib, not
silently assumed for a sharp indicator. -/
theorem neutralIV023SecondCutoff_hasTemperateGrowth :
    (fun x : ℝ => neutralIV023SecondCutoff x).HasTemperateGrowth := by
  exact neutralIV023SecondCutoff.hasCompactSupport.hasTemperateGrowth
    neutralIV023SecondCutoff.contDiff

/-- Genuine complex Schwartz SECOND physical component using
Mathlib's actual continuous smooth scalar multiplication map. -/
def neutralIV023SecondPart (f : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  SchwartzMap.smulLeftCLM ℂ
    (fun x : ℝ => neutralIV023SecondCutoff x) f

theorem neutralIV023SecondPart_apply
    (f : 𝓢(ℝ,ℂ)) (x : ℝ) :
    neutralIV023SecondPart f x =
      neutralIV023SecondCutoff x • f x := by
  exact SchwartzMap.smulLeftCLM_apply_apply
    neutralIV023SecondCutoff_hasTemperateGrowth f x

/-- The first three-cell Schwartz component is the actual
pointwise difference from the new physical second component. -/
def neutralIV023BasePart (f : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  f - neutralIV023SecondPart f

/-- EXACT 3+1 physical source partition for EVERY complex Schwartz
function supported in the full original four-cell union. -/
theorem neutralIV023FourCell_split_threePlusOne
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x=0) :
    (∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport →
        neutralIV023BasePart f x = 0) ∧
    (∀ x : ℝ,
      x ∉ neutralIV022FourthCellInterval →
        neutralIV023SecondPart f x = 0) ∧
    f = neutralIV023BasePart f + neutralIV023SecondPart f := by
  have hBase :
      ∀ x : ℝ, x ∉ neutralIV020WideThreeCellSupport →
        neutralIV023BasePart f x = 0 := by
    intro x hx
    by_cases hSecond : x ∈ neutralIV022FourthCellInterval
    · simp [neutralIV023BasePart,
        neutralIV023SecondPart_apply,
        neutralIV023SecondCutoff_one x hSecond]
    · have hfzero : f x = 0 :=
        hf x (by
          intro h
          exact h.elim hx hSecond)
      simp [neutralIV023BasePart,
        neutralIV023SecondPart_apply,hfzero]
  have hSecond :
      ∀ x : ℝ, x ∉ neutralIV022FourthCellInterval →
        neutralIV023SecondPart f x = 0 := by
    intro x hx
    rw [neutralIV023SecondPart_apply]
    by_cases hBaseCell : x ∈ neutralIV020WideThreeCellSupport
    · rw [neutralIV023SecondCutoff_base_zero x hBaseCell]
      simp
    · have hfzero : f x=0 :=
        hf x (by intro h; exact h.elim hBaseCell hx)
      simp [hfzero]
  refine ⟨hBase,hSecond,?_⟩
  change f = (f - neutralIV023SecondPart f) +
    neutralIV023SecondPart f
  exact (sub_add_cancel f (neutralIV023SecondPart f)).symm

/-- The actual old and first-new Schwartz components of the
three-cell base are defined by IV021's Mathlib smooth multiplier.
All three source parts are REAL complex Schwartz functions. -/
def neutralIV023OldPart (f : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  neutralIV021OldCellPart (neutralIV023BasePart f)

def neutralIV023FirstPart (f : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  neutralIV021NewCellPart (neutralIV023BasePart f)

/-- COMPLETE physical 2+1+1 Schwartz decomposition, including
literal old and both new support predicates. In particular,
NO finite-dimensionality assumption on f is needed. -/
theorem neutralIV023EveryFourCellSchwartz_decomposes
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x=0) :
    neutralNF735InOriginalCollars (neutralIV023OldPart f) ∧
    (∀ x : ℝ, x ∉ neutralIV020WidePhysicalInterval →
      neutralIV023FirstPart f x=0) ∧
    (∀ x : ℝ, x ∉ neutralIV022FourthCellInterval →
      neutralIV023SecondPart f x=0) ∧
    f = (neutralIV023OldPart f +
      neutralIV023FirstPart f) + neutralIV023SecondPart f := by
  obtain ⟨hBase,hSecond,hSplit⟩ :=
    neutralIV023FourCell_split_threePlusOne f hf
  obtain ⟨hOld,hFirst,hThreeSplit⟩ :=
    neutralIV021EveryThreeCellSchwartz_decomposes
      (neutralIV023BasePart f) hBase
  change
    neutralNF735InOriginalCollars
      (neutralIV021OldCellPart (neutralIV023BasePart f)) ∧
    (∀ x : ℝ, x ∉ neutralIV020WidePhysicalInterval →
      neutralIV021NewCellPart (neutralIV023BasePart f) x=0) ∧
    (∀ x : ℝ, x ∉ neutralIV022FourthCellInterval →
      neutralIV023SecondPart f x=0) ∧
    f = (neutralIV021OldCellPart (neutralIV023BasePart f) +
      neutralIV021NewCellPart (neutralIV023BasePart f)) +
      neutralIV023SecondPart f
  refine ⟨hOld,hFirst,hSecond,?_⟩
  rw [← hThreeSplit]
  exact hSplit

#print axioms neutralIV021EveryThreeCellSchwartz_decomposes
#print axioms neutralIV022FourCell_volume
#print axioms neutralIV023SecondCutoff_one
#print axioms neutralIV023SecondCutoff_base_zero
#print axioms neutralIV023SecondCutoff_hasTemperateGrowth
#print axioms neutralIV023SecondPart_apply
#print axioms neutralIV023FourCell_split_threePlusOne
#print axioms neutralIV023EveryFourCellSchwartz_decomposes

end
end WeilDefect
