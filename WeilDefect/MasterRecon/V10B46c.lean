import WeilDefect.MasterRecon.V10B46a
import WeilDefect.MasterRecon.V10B46b

/-! V10B46c: conditional literal optimized constraint receiver.
The row identity must be established from the supported physical trials
and their row-scaled constraints; no source attachment is assumed implicitly. -/
namespace WeilDefect.MasterRecon.V10B46c
open scoped BigOperators Matrix
open WeilDefect.MasterRecon.V10B45a
open WeilDefect.MasterRecon.V10B46a
open WeilDefect.MasterRecon.V10B46b
open WeilDefect.MasterRecon.V10B33b

noncomputable def highCorrection (j : Fin 16) : ℝ :=
  ∑ k ∈ Finset.range 72, (v j (17+2*k):ℝ)*(I (17+2*k)/I 15)

theorem highCorrection_bound (j : Fin 16) :
    |highCorrection j| ≤ reserve j := by
  unfold highCorrection
  apply higher_mode_error
  intro k _
  obtain ⟨h₀,h₁⟩ := high_pair_ratio (17+2*k) (by omega)
  rw [abs_of_nonneg h₀]
  exact h₁

theorem row_identity_surjective (M : Matrix (Fin 16) (Fin 16) ℂ)
    (hM : ∀ i j, M i j = base i j +
      if i.val=15 then (highCorrection j:ℂ) else 0) :
    Function.Surjective M.mulVec := by
  apply optimized_surjective
  intro i j
  rw [hM,add_sub_cancel_left]
  by_cases hi : i.val=15
  · rw [if_pos hi,Complex.norm_real,Real.norm_eq_abs]
    exact highCorrection_bound j
  · rw [if_neg hi,norm_zero]
    exact reserve_nonneg j

theorem optimized_section {H : Type*} [AddCommGroup H] [Module ℂ H]
    (L : H →ₗ[ℂ] (Fin 16 → ℂ)) (trial : Fin 16 → H)
    (hrow : ∀ i j, L (trial j) i = base i j +
      if i.val=15 then (highCorrection j:ℂ) else 0) :
    ∀ g : H, ∃ a : Fin 16 → ℂ, g-(∑ j, a j • trial j) ∈ L.ker := by
  let M : Matrix (Fin 16) (Fin 16) ℂ := fun i j => L (trial j) i
  exact constraint_section L trial M (fun _ _ => rfl)
    (row_identity_surjective M hrow)

end WeilDefect.MasterRecon.V10B46c

#print axioms WeilDefect.MasterRecon.V10B46c.highCorrection_bound
#print axioms WeilDefect.MasterRecon.V10B46c.row_identity_surjective
#print axioms WeilDefect.MasterRecon.V10B46c.optimized_section
