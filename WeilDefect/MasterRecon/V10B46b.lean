import WeilDefect.MasterRecon.V10B45a
import WeilDefect.MasterRecon.V10B33b
import Mathlib.Analysis.Normed.Group.Int

/-! V10B46b: optimized integer matrix surjectivity under the coarse
higher-mode reserve. Matrix-entry attachment remains an explicit input. -/
namespace WeilDefect.MasterRecon.V10B46b
open scoped BigOperators Matrix
open WeilDefect.MasterRecon.V10B45a
open WeilDefect.MasterRecon.V10B33b

noncomputable def base : Matrix (Fin 16) (Fin 16) ℂ :=
  fun i j => (v j i.val:ℂ)

noncomputable def reserve (j : Fin 16) : ℝ := (highMass j:ℝ)/256

theorem base_norm (i j : Fin 16) :
    ‖base i j‖ = ((v j i.val).natAbs:ℝ) := by
  unfold base
  rw [Complex.norm_intCast,Int.norm_eq_abs,← Int.cast_abs,Int.abs_eq_natAbs]
  norm_cast

theorem base_margin (i : Fin 16) :
    (denom:ℝ)+(∑ j ∈ Finset.univ.erase i, ‖base i j‖) < ‖base i i‖ := by
  simp only [base_norm]
  exact_mod_cast leading_margin i

theorem reserve_nonneg (j : Fin 16) : 0 ≤ reserve j := by
  unfold reserve
  positivity

theorem total_reserve :
    (∑ j : Fin 16, reserve j) < (denom:ℝ) := by
  have h : (∑ j : Fin 16, (highMass j:ℝ)) < 7*(denom:ℝ) := by
    exact_mod_cast high_mass_bound
  have hd : (0:ℝ)<(denom:ℝ) := by exact_mod_cast denom_pos
  unfold reserve
  rw [← Finset.sum_div]
  linarith

theorem optimized_surjective (M : Matrix (Fin 16) (Fin 16) ℂ)
    (hM : ∀ i j, ‖M i j-base i j‖ ≤ reserve j) :
    Function.Surjective M.mulVec := by
  apply dominance_from_reserves M base (fun _ j => reserve j) hM
  intro i
  rw [Finset.sum_add_distrib]
  have hs := Finset.sum_erase_add Finset.univ reserve (Finset.mem_univ i)
  have hm := base_margin i
  have hr := total_reserve
  linarith

theorem higher_mode_error (col : Fin 16) (r : ℕ → ℝ)
    (hr : ∀ k<72, |r k| ≤ 1/256) :
    |∑ k ∈ Finset.range 72, (v col (17+2*k):ℝ)*r k| ≤ reserve col := by
  calc
    _ ≤ ∑ k ∈ Finset.range 72, |(v col (17+2*k):ℝ)*r k| := by
      simpa only [Real.norm_eq_abs] using
        norm_sum_le (Finset.range 72) (fun k => (v col (17+2*k):ℝ)*r k)
    _ ≤ ∑ k ∈ Finset.range 72, ((v col (17+2*k)).natAbs:ℝ)*(1/256) := by
      apply Finset.sum_le_sum
      intro k hk
      rw [abs_mul,← Int.cast_abs,Int.abs_eq_natAbs]
      push_cast
      exact mul_le_mul_of_nonneg_left (hr k (Finset.mem_range.mp hk)) (by positivity)
    _ = reserve col := by
      unfold reserve highMass
      push_cast
      rw [← Finset.sum_mul]
      ring

end WeilDefect.MasterRecon.V10B46b

#print axioms WeilDefect.MasterRecon.V10B46b.base_norm
#print axioms WeilDefect.MasterRecon.V10B46b.base_margin
#print axioms WeilDefect.MasterRecon.V10B46b.reserve_nonneg
#print axioms WeilDefect.MasterRecon.V10B46b.total_reserve
#print axioms WeilDefect.MasterRecon.V10B46b.optimized_surjective
#print axioms WeilDefect.MasterRecon.V10B46b.higher_mode_error
