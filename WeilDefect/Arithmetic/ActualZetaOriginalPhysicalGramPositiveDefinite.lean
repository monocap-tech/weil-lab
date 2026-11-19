import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramCoercivityClosure

namespace WeilDefect

/-!
NF668: algebraic consequences of a genuinely coercive real finite Gram
matrix. This module is source-independent. Its original physical
specialization consumes the now Lean-certified NF665 source theorem.
-/

noncomputable section
open Finset

/-- The authentic row action of a real finite Gram matrix. -/
def neutralNF668GramApply {n : ℕ}
    (H : Fin n → Fin n → ℝ) (x : Fin n → ℝ) (i : Fin n) : ℝ :=
  ∑ j : Fin n, H i j * x j

theorem neutralNF668SqNorm_pos {n : ℕ}
    (x : Fin n → ℝ) (hx : x ≠ 0) :
    0 < neutralNF661SqNorm x := by
  classical
  have hex : ∃ i : Fin n, x i ≠ 0 := by
    by_contra h
    push_neg at h
    apply hx
    funext i
    exact h i
  obtain ⟨i, hi⟩ := hex
  have hi0 : (x i)^2 ≠ 0 := pow_ne_zero 2 hi
  have hisq : 0 < (x i)^2 :=
    lt_of_le_of_ne (sq_nonneg (x i)) (Ne.symm hi0)
  unfold neutralNF661SqNorm
  apply Finset.sum_pos' (fun j _ => sq_nonneg (x j))
  exact ⟨i, Finset.mem_univ _, hisq⟩

theorem neutralNF668Quadratic_eq_apply {n : ℕ}
    (H : Fin n → Fin n → ℝ) (x : Fin n → ℝ) :
    neutralNF661Quadratic H x =
      ∑ i : Fin n, neutralNF668GramApply H x i * x i := by
  unfold neutralNF661Quadratic neutralNF668GramApply
  apply Finset.sum_congr rfl
  intro i _
  calc
    (∑ j : Fin n, H i j * x i * x j) =
        ∑ j : Fin n, (H i j * x j) * x i := by
      apply Finset.sum_congr rfl
      intro j _
      ring
    _ = (∑ j : Fin n, H i j * x j) * x i := by
      rw [Finset.sum_mul]

theorem neutralNF668Quadratic_pos_of_coercivity {n : ℕ}
    (H : Fin n → Fin n → ℝ) (c : ℝ) (hc : 0 < c)
    (hcoercivity : ∀ x : Fin n → ℝ,
      c * neutralNF661SqNorm x ≤ neutralNF661Quadratic H x)
    (x : Fin n → ℝ) (hx : x ≠ 0) :
    0 < neutralNF661Quadratic H x := by
  exact lt_of_lt_of_le (mul_pos hc (neutralNF668SqNorm_pos x hx))
    (hcoercivity x)

/-- A coercive finite real Gram matrix has no nonzero kernel. -/
theorem neutralNF668GramKernel_trivial {n : ℕ}
    (H : Fin n → Fin n → ℝ) (c : ℝ) (hc : 0 < c)
    (hcoercivity : ∀ x : Fin n → ℝ,
      c * neutralNF661SqNorm x ≤ neutralNF661Quadratic H x)
    (x : Fin n → ℝ)
    (hzero : ∀ i : Fin n, neutralNF668GramApply H x i = 0) :
    x = 0 := by
  have hqzero : neutralNF661Quadratic H x = 0 := by
    rw [neutralNF668Quadratic_eq_apply]
    apply Finset.sum_eq_zero
    intro i _
    rw [hzero i]
    ring
  by_contra hx
  have hpos := neutralNF668Quadratic_pos_of_coercivity
    H c hc hcoercivity x hx
  rw [hqzero] at hpos
  exact (lt_irrefl (0 : ℝ)) hpos

/-- Quantitative Gram coercivity implies injectivity of its exact
finite row action. There is no assumption of numerical invertibility. -/
theorem neutralNF668GramApply_injective {n : ℕ}
    (H : Fin n → Fin n → ℝ) (c : ℝ) (hc : 0 < c)
    (hcoercivity : ∀ x : Fin n → ℝ,
      c * neutralNF661SqNorm x ≤ neutralNF661Quadratic H x) :
    Function.Injective (neutralNF668GramApply H) := by
  intro x y hxy
  have hsub (i : Fin n) :
      neutralNF668GramApply H (fun j => x j - y j) i =
        neutralNF668GramApply H x i -
          neutralNF668GramApply H y i := by
    simp only [neutralNF668GramApply, mul_sub, Finset.sum_sub_distrib]
  have hzero : ∀ i : Fin n,
      neutralNF668GramApply H (fun j => x j - y j) i = 0 := by
    intro i
    rw [hsub i, congrFun hxy i]
    ring
  have heq := neutralNF668GramKernel_trivial H c hc
    hcoercivity (fun j => x j - y j) hzero
  funext i
  have hi := congrArg (fun f : Fin n → ℝ => f i) heq
  have hid : x i - y i = 0 := by simpa using hi
  exact sub_eq_zero.mp hid

/-- At most one coefficient vector solves a prescribed finite
physical Gram equation. This conclusion does not assert existence. -/
theorem neutralNF668GramSolution_unique {n : ℕ}
    (H : Fin n → Fin n → ℝ) (c : ℝ) (hc : 0 < c)
    (hcoercivity : ∀ x : Fin n → ℝ,
      c * neutralNF661SqNorm x ≤ neutralNF661Quadratic H x)
    (b x y : Fin n → ℝ)
    (hx : neutralNF668GramApply H x = b)
    (hy : neutralNF668GramApply H y = b) :
    x = y :=
  neutralNF668GramApply_injective H c hc hcoercivity
    (hx.trans hy.symm)

#print axioms neutralNF668SqNorm_pos
#print axioms neutralNF668Quadratic_eq_apply
#print axioms neutralNF668Quadratic_pos_of_coercivity
#print axioms neutralNF668GramKernel_trivial
#print axioms neutralNF668GramApply_injective
#print axioms neutralNF668GramSolution_unique

end
end WeilDefect
