import WeilDefect.MasterRecon.V10B78a

/-! V10B79a: error transfer from arbitrary authenticated approximate
physical loads. No historical numerical coefficients or matrix entries
are instantiated. No prime-zero or coercivity assumption is discharged. -/
namespace WeilDefect.MasterRecon.V10B79a
open MeasureTheory Set
open scoped InnerProduct BigOperators
open V08I (logCarrier)
open V08K (supportMeasure)
open V10B69a (J dividedTrial)
open V10B78a (archPole load correctedLoad)

abbrev E := V08F.PhysicalL2 (supportMeasure (1/4))

noncomputable def rowCorrection (a : Fin 16 → ℂ) : E :=
  ∑ i, a i • V10B68a.rowVector i

theorem corrected_error (j : Fin 16) (a : Fin 16 → ℂ) (q : E) :
    correctedLoad j a - (q-rowCorrection a) = load j-q := by
  unfold correctedLoad rowCorrection
  abel

theorem trial_entry_error (i j : Fin 16) (q : E) (e : ℝ)
    (he : ‖load i-q‖ ≤ e) :
    ‖inner ℂ (archPole (dividedTrial i)) (dividedTrial j) -
      inner ℂ q (J (dividedTrial j))‖ ≤ e*‖J (dividedTrial j)‖ := by
  rw [V10B78a.trial_entry_pair, ← inner_sub_left]
  exact (norm_inner_le_norm _ _).trans
    (mul_le_mul_of_nonneg_right he (norm_nonneg _))

theorem corrected_pair_error (j : Fin 16) (a : Fin 16 → ℂ) (q : E)
    (e : ℝ) (he : ‖load j-q‖ ≤ e) (w : logCarrier (1/4))
    (hw : w ∈ V10B17b.retainedᗮ) :
    ‖inner ℂ (archPole (dividedTrial j)) w -
      inner ℂ (q-rowCorrection a) (J w)‖ ≤ e*‖J w‖ := by
  rw [V10B78a.corrected_pair j a w hw, ← inner_sub_left, corrected_error]
  exact (norm_inner_le_norm _ _).trans
    (mul_le_mul_of_nonneg_right he (norm_nonneg _))

theorem gram_entry_error (r s p q : E) :
    ‖inner ℂ r s-inner ℂ p q‖ ≤
      ‖r-p‖*‖s-q‖+‖r-p‖*‖q‖+‖p‖*‖s-q‖ := by
  have h : inner ℂ r s-inner ℂ p q =
      inner ℂ (r-p) (s-q)+inner ℂ (r-p) q+inner ℂ p (s-q) := by
    simp only [inner_sub_left,inner_sub_right]
    ring
  rw [h]
  calc
    _ ≤ ‖inner ℂ (r-p) (s-q)+inner ℂ (r-p) q‖+‖inner ℂ p (s-q)‖ :=
      norm_add_le _ _
    _ ≤ ‖inner ℂ (r-p) (s-q)‖+‖inner ℂ (r-p) q‖+‖inner ℂ p (s-q)‖ :=
      add_le_add_right (norm_add_le _ _) _
    _ ≤ _ := add_le_add
      (add_le_add (norm_inner_le_norm _ _) (norm_inner_le_norm _ _))
      (norm_inner_le_norm _ _)

theorem corrected_gram_error (i j : Fin 16) (a b : Fin 16 → ℂ) (p q : E) :
    ‖inner ℂ (correctedLoad i a) (correctedLoad j b) -
      inner ℂ (p-rowCorrection a) (q-rowCorrection b)‖ ≤
      ‖load i-p‖*‖load j-q‖+
      ‖load i-p‖*‖q-rowCorrection b‖+
      ‖p-rowCorrection a‖*‖load j-q‖ := by
  have h := gram_entry_error (correctedLoad i a) (correctedLoad j b)
    (p-rowCorrection a) (q-rowCorrection b)
  rw [corrected_error, corrected_error] at h
  exact h

end WeilDefect.MasterRecon.V10B79a

#print axioms WeilDefect.MasterRecon.V10B79a.corrected_error
#print axioms WeilDefect.MasterRecon.V10B79a.trial_entry_error
#print axioms WeilDefect.MasterRecon.V10B79a.corrected_pair_error
#print axioms WeilDefect.MasterRecon.V10B79a.gram_entry_error
#print axioms WeilDefect.MasterRecon.V10B79a.corrected_gram_error
