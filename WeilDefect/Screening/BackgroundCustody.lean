import WeilDefect.Screening.Quadratic
import WeilDefect.Screening.DefectIndex
import Mathlib

namespace WeilDefect.WDT07

open scoped InnerProduct
open ContinuousLinearMap
open WeilDefect
open WeilDefect.WDT01

variable {H Kpos Kneg B : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
variable [NormedAddCommGroup Kneg] [InnerProductSpace ℂ Kneg] [CompleteSpace Kneg]
variable [NormedAddCommGroup B] [InnerProductSpace ℂ B] [CompleteSpace B]

/--
WD-T07 pointwise operator-form custody:
adding an unselected negative background can only decrease the quadratic form.
-/
theorem wd_t07_full_le_selected
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (S_B : B →L[ℂ] H)
    (h : H) :
    fullQuadratic Spos Sneg S_B h
      ≤ selectedQuadratic Spos Sneg h := by
  unfold fullQuadratic
  have hsquare : 0 ≤ ‖(S_B†) h‖ ^ 2 := sq_nonneg _
  linarith

/--
Every k-dimensional selected negative witness remains a k-dimensional
negative witness after aggregation with an arbitrary negative background.
This is the finite-rank-spectrum form of ind₋(D_full) ≥ ind₋(D_M).
-/
theorem wd_t07_negative_rank_custody
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (S_B : B →L[ℂ] H)
    (k : ℕ) :
    HasNegativeRank
        (selectedQuadratic Spos Sneg)
        (Set.univ : Set H) k
      →
    HasNegativeRank
        (fullQuadratic Spos Sneg S_B)
        (Set.univ : Set H) k := by
  rintro ⟨T, hcarrier, hneg⟩
  refine ⟨T, hcarrier, ?_⟩
  intro x hx
  exact wd_t07_selected_negative_implies_full
    Spos Sneg S_B (T x) (hneg x hx)

/--
The converse custody implication fails already in one complex dimension:
the selected defect can be identically zero while a background channel creates
strict full negativity.
-/
theorem wd_t07_converse_failure :
    let Z : ℂ →L[ℂ] ℂ := 0
    let I : ℂ →L[ℂ] ℂ := ContinuousLinearMap.id ℂ ℂ
    selectedQuadratic Z Z 1 = 0
      ∧ fullQuadratic Z Z I 1 < 0 := by
  simp [selectedQuadratic, fullQuadratic, ContinuousLinearMap.adjoint_id]

/--
A sharper scalar custody witness: full negativity is present at h=1 while
selected negativity is absent at that same vector.
-/
theorem wd_t07_full_negative_without_selected_negative :
    let Z : ℂ →L[ℂ] ℂ := 0
    let I : ℂ →L[ℂ] ℂ := ContinuousLinearMap.id ℂ ℂ
    fullQuadratic Z Z I 1 < 0
      ∧ ¬ selectedQuadratic Z Z 1 < 0 := by
  simp [selectedQuadratic, fullQuadratic, ContinuousLinearMap.adjoint_id]

/--
WD-T07 assembled:
the full quadratic form is the selected form minus a background norm square;
selected finite negative rank is inherited by the full defect; but full
negativity does not determine selected-sector ownership.
-/
theorem wd_t07_selected_background_monotonicity_and_custody :
    (∀
      (Spos : Kpos →L[ℂ] H)
      (Sneg : Kneg →L[ℂ] H)
      (S_B : B →L[ℂ] H)
      (h : H),
      fullQuadratic Spos Sneg S_B h
        =
      selectedQuadratic Spos Sneg h - ‖(S_B†) h‖ ^ 2)
    ∧
    (∀
      (Spos : Kpos →L[ℂ] H)
      (Sneg : Kneg →L[ℂ] H)
      (S_B : B →L[ℂ] H)
      (h : H),
      fullQuadratic Spos Sneg S_B h
        ≤ selectedQuadratic Spos Sneg h)
    ∧
    (∀
      (Spos : Kpos →L[ℂ] H)
      (Sneg : Kneg →L[ℂ] H)
      (S_B : B →L[ℂ] H)
      (k : ℕ),
      HasNegativeRank
          (selectedQuadratic Spos Sneg)
          (Set.univ : Set H) k
        →
      HasNegativeRank
          (fullQuadratic Spos Sneg S_B)
          (Set.univ : Set H) k)
    ∧
    (let Z : ℂ →L[ℂ] ℂ := 0
     let I : ℂ →L[ℂ] ℂ := ContinuousLinearMap.id ℂ ℂ
     fullQuadratic Z Z I 1 < 0
       ∧ ¬ selectedQuadratic Z Z 1 < 0) := by
  refine ⟨?_, ?_, ?_, wd_t07_full_negative_without_selected_negative⟩
  · intro Spos Sneg S_B h
    exact wd_t07_selected_full_identity Spos Sneg S_B h
  · intro Spos Sneg S_B h
    exact wd_t07_full_le_selected Spos Sneg S_B h
  · intro Spos Sneg S_B k
    exact wd_t07_negative_rank_custody Spos Sneg S_B k

end WeilDefect.WDT07
