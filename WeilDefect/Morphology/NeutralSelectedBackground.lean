import WeilDefect.Morphology.Neutral
import WeilDefect.Screening.ResidualBudget

namespace WeilDefect

noncomputable section

open ContinuousLinearMap
open scoped InnerProduct

variable {H Kpos M B : Type*}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
  [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
  [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
  [NormedAddCommGroup B] [InnerProductSpace ℂ B] [CompleteSpace B]

/-- The retained selected null identity leaves exactly the negative background
covariance in the full shared defect. No source-form identification is used. -/
theorem wd_t38_full_defect_on_selected_neutral
    (P : Kpos →L[ℂ] H) (C : M →L[ℂ] Kpos)
    (S_B : B →L[ℂ] H) (u : M) (k : H)
    (hunit : (C†) (C u) = u) (hreal : C u = (P†) k) (hk : k ≠ 0) :
    WDT07.sharedDefect P (neutralNegativeSynthesis P C) S_B k =
      -S_B ((S_B†) k) := by
  have hn := (wd_t38_p3_u2_physical_neutral_null_mode P C u k hunit hreal hk).2
  change (WDT01.physicalDefect P (neutralNegativeSynthesis P C) -
    S_B ∘L S_B†) k = _
  rw [ContinuousLinearMap.sub_apply]
  change neutralWeilOperator P C k - S_B ((S_B†) k) = _
  rw [hn, zero_sub]

/-- A selected unit-gain null mode is full-null exactly when its unselected
negative analysis coefficient vanishes. This condition is not inferred from
selected neutrality. -/
theorem wd_t38_full_null_iff_background_analysis_zero
    (P : Kpos →L[ℂ] H) (C : M →L[ℂ] Kpos)
    (S_B : B →L[ℂ] H) (u : M) (k : H)
    (hunit : (C†) (C u) = u) (hreal : C u = (P†) k) (hk : k ≠ 0) :
    WDT07.sharedDefect P (neutralNegativeSynthesis P C) S_B k = 0 ↔
      (S_B†) k = 0 := by
  rw [wd_t38_full_defect_on_selected_neutral P C S_B u k hunit hreal hk,
    neg_eq_zero]
  constructor
  · intro hc
    have hi : inner ℂ (S_B ((S_B†) k)) k = 0 := by rw [hc, inner_zero_left]
    rw [← ContinuousLinearMap.adjoint_inner_right S_B ((S_B†) k) k] at hi
    exact inner_self_eq_zero.mp hi
  · intro hc
    rw [hc, map_zero]

/-- Consume the existing WD-T10 background reduction with the effective
positive synthesis. The same unit-gain identity now cancels the full shared
defect; no additional background-null premise is needed. Actual zeta/Weil
source identification remains separate. -/
theorem wd_t38_effective_positive_full_null
    (Spos : Kpos →L[ℂ] H) (X_B : B →L[ℂ] Kpos)
    (S_B : B →L[ℂ] H)
    (hXB : WDT02.IsContraction X_B)
    (hB : S_B = -(Spos ∘L X_B))
    (C : M →L[ℂ] Kpos) (u : M) (k : H)
    (hunit : (C†) (C u) = u)
    (hreal : C u = ((WDT10.effectivePositive Spos X_B)†) k)
    (hk : k ≠ 0) :
    WDT07.sharedDefect Spos
      (neutralNegativeSynthesis (WDT10.effectivePositive Spos X_B) C) S_B k = 0 := by
  rw [WDT10.wd_t10_full_defect_reduction Spos
    (neutralNegativeSynthesis (WDT10.effectivePositive Spos X_B) C)
    S_B X_B hXB hB]
  exact (wd_t38_p3_u2_physical_neutral_null_mode
    (WDT10.effectivePositive Spos X_B) C u k hunit hreal hk).2

end

end WeilDefect
