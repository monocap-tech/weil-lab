import WeilDefect.MasterRecon.V10B14b

/-! Generic norm error for a doubly compressed physical defect.
The middle operator is not truncated: its approximation, if needed,
must have a separate certified error bound. -/
namespace WeilDefect.MasterRecon.V10B14c

open scoped InnerProduct

variable {H E : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]

noncomputable def pullback (J : H →L[ℂ] E) (B : E →L[ℂ] E) : H →L[ℂ] H :=
  J.adjoint.comp (B.comp J)

theorem pullback_difference (J P : H →L[ℂ] E) (B : E →L[ℂ] E) :
    pullback J B-pullback P B =
      (J-P).adjoint.comp (B.comp J)+P.adjoint.comp (B.comp (J-P)) := by
  ext x : 1
  simp only [pullback,ContinuousLinearMap.sub_apply,ContinuousLinearMap.add_apply,
    ContinuousLinearMap.comp_apply,map_sub]
  abel

theorem pullback_error (J P : H →L[ℂ] E) (B : E →L[ℂ] E)
    (ε : ℝ) (hε : ‖J-P‖ ≤ ε) :
    ‖pullback J B-pullback P B‖ ≤ ‖B‖*ε*(2*‖J‖+ε) := by
  have he0 := (norm_nonneg (J-P)).trans hε
  have hP : ‖P‖ ≤ ‖J‖+ε := by
    have he : P = J-(J-P) := by abel
    calc
      ‖P‖ = ‖J-(J-P)‖ := congrArg norm he
      _ ≤ ‖J‖+‖J-P‖ := norm_sub_le _ _
      _ ≤ _ := add_le_add_right hε _
  rw [pullback_difference]
  have h1 := (ContinuousLinearMap.opNorm_comp_le (J-P).adjoint (B.comp J)).trans
    (mul_le_mul_of_nonneg_left (ContinuousLinearMap.opNorm_comp_le B J) (norm_nonneg _))
  have h2 := (ContinuousLinearMap.opNorm_comp_le P.adjoint (B.comp (J-P))).trans
    (mul_le_mul_of_nonneg_left (ContinuousLinearMap.opNorm_comp_le B (J-P)) (norm_nonneg _))
  rw [ContinuousLinearMap.adjoint.norm_map] at h1 h2
  have h1' := h1.trans (mul_le_mul_of_nonneg_right hε (by positivity :
    0 ≤ ‖B‖*‖J‖))
  have h2' := h2.trans (mul_le_mul_of_nonneg_left
    (mul_le_mul_of_nonneg_left hε (norm_nonneg B)) (norm_nonneg P))
  have h2'' := h2'.trans (mul_le_mul_of_nonneg_right hP (by positivity :
    0 ≤ ‖B‖*ε))
  calc
    _ ≤ ‖(J-P).adjoint.comp (B.comp J)‖+‖P.adjoint.comp (B.comp (J-P))‖ :=
      norm_add_le _ _
    _ ≤ _ := by nlinarith only [h1',h2'']

theorem principal_error (J P : H →L[ℂ] E) (B : E →L[ℂ] E)
    (ε : ℝ) (hε : ‖J-P‖ ≤ ε) :
    ‖(1+pullback J B)-(1+pullback P B)‖ ≤ ‖B‖*ε*(2*‖J‖+ε) := by
  have he : (1+pullback J B)-(1+pullback P B) = pullback J B-pullback P B := by abel
  rw [he]
  exact pullback_error J P B ε hε

end WeilDefect.MasterRecon.V10B14c

#print axioms WeilDefect.MasterRecon.V10B14c.pullback_difference
#print axioms WeilDefect.MasterRecon.V10B14c.pullback_error
#print axioms WeilDefect.MasterRecon.V10B14c.principal_error
