import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.Normed.Group.Basic

/-! V10B33b: exact constraint coverage from strict row diagonal
dominance. This independent receiver does not depend on the digamma
or Legendre expansion. The literal entries and their bounds are inputs. -/
namespace WeilDefect.MasterRecon.V10B33b

open scoped BigOperators Matrix

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

theorem dominant_kernel (M : Matrix ι ι ℂ)
    (h : ∀ i, (∑ j ∈ Finset.univ.erase i, ‖M i j‖) < ‖M i i‖)
    (x : ι → ℂ) (hx : M *ᵥ x = 0) : x = 0 := by
  classical
  by_contra hn
  obtain ⟨k,hk⟩ : ∃ k, x k ≠ 0 := by
    by_contra! hh
    exact hn (funext hh)
  obtain ⟨i,hi,hmax⟩ := Finset.exists_max_image Finset.univ
    (fun j => ‖x j‖) ⟨k,Finset.mem_univ k⟩
  have hp : 0 < ‖x i‖ := (norm_pos_iff.mpr hk).trans_le (hmax k (Finset.mem_univ k))
  have hz : ∑ j, M i j*x j = 0 := by
    have hh := congrFun hx i
    simpa only [Matrix.mulVec, dotProduct, Pi.zero_apply] using hh
  have he := Finset.sum_erase_add Finset.univ (fun j => M i j*x j) (Finset.mem_univ i)
  rw [hz] at he
  have hd : M i i*x i = -(∑ j ∈ Finset.univ.erase i, M i j*x j) := by
    linear_combination he
  have hnorm : ‖M i i‖*‖x i‖ ≤ (∑ j ∈ Finset.univ.erase i, ‖M i j‖)*‖x i‖ := by
    calc
      _ = ‖M i i*x i‖ := (norm_mul _ _).symm
      _ = ‖∑ j ∈ Finset.univ.erase i, M i j*x j‖ := by rw [hd,norm_neg]
      _ ≤ ∑ j ∈ Finset.univ.erase i, ‖M i j*x j‖ := norm_sum_le _ _
      _ ≤ ∑ j ∈ Finset.univ.erase i, ‖M i j‖*‖x i‖ := by
        apply Finset.sum_le_sum
        intro j hj
        rw [norm_mul]
        exact mul_le_mul_of_nonneg_left (hmax j (Finset.mem_univ j)) (norm_nonneg _)
      _ = _ := (Finset.sum_mul _ _ _).symm
  exact (not_lt_of_ge hnorm) (mul_lt_mul_of_pos_right (h i) hp)

theorem dominant_surjective (M : Matrix ι ι ℂ)
    (h : ∀ i, (∑ j ∈ Finset.univ.erase i, ‖M i j‖) < ‖M i i‖) :
    Function.Surjective M.mulVec := by
  let L := Matrix.toLin' M
  have hinj : Function.Injective L := by
    intro a b hab
    apply sub_eq_zero.mp
    have hz : L (a-b) = 0 := by rw [map_sub,hab,sub_self]
    exact dominant_kernel M h (a-b) hz
  exact LinearMap.injective_iff_surjective.mp hinj

theorem dominance_from_reserves (M A : Matrix ι ι ℂ) (e : ι → ι → ℝ)
    (herr : ∀ i j, ‖M i j-A i j‖ ≤ e i j)
    (h : ∀ i, (∑ j ∈ Finset.univ.erase i, (‖A i j‖+e i j)) <
      ‖A i i‖-e i i) :
    Function.Surjective M.mulVec := by
  apply dominant_surjective
  intro i
  have hd : ‖A i i‖-e i i ≤ ‖M i i‖ := by
    have hb := norm_add_le (A i i-M i i) (M i i)
    rw [sub_add_cancel,norm_sub_rev] at hb
    linarith [herr i i]
  have ho : (∑ j ∈ Finset.univ.erase i, ‖M i j‖) ≤
      ∑ j ∈ Finset.univ.erase i, (‖A i j‖+e i j) := by
    apply Finset.sum_le_sum
    intro j _
    have hb := norm_add_le (M i j-A i j) (A i j)
    rw [sub_add_cancel] at hb
    linarith [herr i j]
  exact (ho.trans_lt (h i)).trans_le hd

variable {H : Type*} [AddCommGroup H] [Module ℂ H]

theorem constraint_section (L : H →ₗ[ℂ] (ι → ℂ)) (v : ι → H)
    (M : Matrix ι ι ℂ) (hM : ∀ i j, M i j = L (v j) i)
    (hs : Function.Surjective M.mulVec) :
    ∀ g : H, ∃ a : ι → ℂ, g-(∑ j, a j • v j) ∈ L.ker := by
  intro g
  obtain ⟨a,ha⟩ := hs (L g)
  refine ⟨a,?_⟩
  change L (g-∑ j, a j • v j) = 0
  rw [map_sub,map_sum]
  apply sub_eq_zero.mpr
  funext i
  have hi := congrFun ha i
  simp only [Matrix.mulVec,dotProduct] at hi
  rw [← hi,Finset.sum_apply]
  apply Finset.sum_congr rfl
  intro j _
  rw [map_smul,hM,Pi.smul_apply,smul_eq_mul,mul_comm]

end WeilDefect.MasterRecon.V10B33b

#print axioms WeilDefect.MasterRecon.V10B33b.dominant_kernel
#print axioms WeilDefect.MasterRecon.V10B33b.dominant_surjective
#print axioms WeilDefect.MasterRecon.V10B33b.dominance_from_reserves
#print axioms WeilDefect.MasterRecon.V10B33b.constraint_section
