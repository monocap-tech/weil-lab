import WeilDefect.MasterRecon.V10B39a

/-! V10B52a: the literal physical Legendre family has the same finite
polynomial span as physical monomials. No rational inverse oracle. -/
namespace WeilDefect.MasterRecon.V10B52a

open Polynomial
open scoped BigOperators
open WeilDefect.MasterRecon.V10B33a
open WeilDefect.MasterRecon.V10B39a

noncomputable def affine : ℝ[X] := C 2 * X + C (1/2)

noncomputable def physicalRow (j : ℕ) : ℝ[X] :=
  C ((-1:ℝ)^j) * (shiftedReal j).comp affine

theorem affine_degree : affine.degree = 1 := by
  unfold affine
  have h : (C (2:ℝ) * X).degree = 1 :=
    degree_C_mul_X (by norm_num)
  rw [degree_add_C (by rw [h]; norm_num),h]

theorem physicalRow_degree (j : ℕ) : (physicalRow j).degree = j := by
  unfold physicalRow
  have ha : 0 < affine.degree := by rw [affine_degree]; norm_num
  rw [degree_C_mul (pow_ne_zero _ (by norm_num : (-1:ℝ) ≠ 0)),
    degree_comp ha,shiftedReal_degree,affine_degree,mul_one]

theorem physicalRow_eval (j : ℕ) (x : ℝ) :
    (physicalRow j).eval x = legendre j (2*x+1/2) := by
  unfold physicalRow shiftedReal affine legendre
  rw [eval_mul,eval_C,eval_comp,eval_add,eval_mul,eval_C,eval_X,eval_C,eval_map]
  rw [aeval_def,algebraMap_int_eq]

theorem functional_zero_of_graded {E : Type*} [AddCommGroup E] [Module ℝ E]
    (F : ℝ[X] →ₗ[ℝ] E) (q : ℕ → ℝ[X])
    (hq : ∀ j, (q j).degree = j) (n : ℕ)
    (hz : ∀ j<n, F (q j)=0) (p : ℝ[X]) (hp : p.degree < (n:WithBot ℕ)) :
    F p=0 := by
  obtain ⟨a,ha⟩ := graded_span q hq n p hp
  rw [ha,map_sum]
  apply Finset.sum_eq_zero
  intro j hj
  have he : C (a j)*q j = a j • q j := by
    rw [Algebra.smul_def,Polynomial.algebraMap_apply,Algebra.algebraMap_self_apply]
  rw [he,map_smul,hz j (Finset.mem_range.mp hj),smul_zero]

theorem physical_moment_kernel {E : Type*} [AddCommGroup E] [Module ℝ E]
    (F : ℝ[X] →ₗ[ℝ] E) (n : ℕ) :
    (∀ j<n, F ((X:ℝ[X])^j)=0) ↔ (∀ j<n, F (physicalRow j)=0) := by
  constructor
  · intro h j hj
    apply functional_zero_of_graded F (fun i => (X:ℝ[X])^i)
      (fun i => degree_X_pow i) n h
    rw [physicalRow_degree]
    exact_mod_cast hj
  · intro h j hj
    apply functional_zero_of_graded F physicalRow physicalRow_degree n h
    rw [degree_X_pow]
    exact_mod_cast hj

end WeilDefect.MasterRecon.V10B52a

#print axioms WeilDefect.MasterRecon.V10B52a.affine_degree
#print axioms WeilDefect.MasterRecon.V10B52a.physicalRow_degree
#print axioms WeilDefect.MasterRecon.V10B52a.physicalRow_eval
#print axioms WeilDefect.MasterRecon.V10B52a.functional_zero_of_graded
#print axioms WeilDefect.MasterRecon.V10B52a.physical_moment_kernel
