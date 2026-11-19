import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramTransformedDominance

namespace WeilDefect

/-!
NF665: elementary finite preconditioner mechanics.
The map y ↦ Kᵀy is defined without numerical approximations.
The bound is Cauchy–Schwarz with the actual finite Frobenius norm.
The inverse exists under a proved lower-triangular/nonzero-diagonal
hypothesis, not because a solver asserted a nonzero determinant.
-/

noncomputable section
open Finset

def neutralNF665TransposeAction {n : ℕ}
    (K : Fin n → Fin n → ℝ) (y : Fin n → ℝ) (p : Fin n) : ℝ :=
  ∑ i : Fin n, y i * K i p

theorem neutralNF665FrobeniusNorm_bound {n : ℕ}
    (K : Fin n → Fin n → ℝ) (y : Fin n → ℝ) :
    neutralNF661SqNorm (neutralNF665TransposeAction K y) ≤
      (∑ i : Fin n, ∑ j : Fin n, (K i j)^2) *
        neutralNF661SqNorm y := by
  unfold neutralNF661SqNorm neutralNF665TransposeAction
  calc
    (∑ p : Fin n, (∑ i : Fin n, y i * K i p)^2) ≤
      ∑ p : Fin n,
        (∑ i : Fin n, (K i p)^2) * (∑ i : Fin n, y i^2) := by
        apply Finset.sum_le_sum
        intro p _
        convert Finset.sum_mul_sq_le_sq_mul_sq
          (Finset.univ : Finset (Fin n))
          (fun i => y i) (fun i => K i p) using 1 <;> ring
    _ = (∑ p : Fin n, ∑ i : Fin n, (K i p)^2) *
          (∑ i : Fin n, y i^2) := by
        rw [Finset.sum_mul]
    _ = (∑ i : Fin n, ∑ p : Fin n, (K i p)^2) *
          (∑ i : Fin n, y i^2) := by
        rw [Finset.sum_comm]

theorem neutralNF665FourSum_exchange {n : ℕ}
    (f : Fin n → Fin n → Fin n → Fin n → ℝ) :
    (∑ i : Fin n, ∑ j : Fin n, ∑ p : Fin n, ∑ q : Fin n,
      f i j p q) =
      ∑ p : Fin n, ∑ q : Fin n, ∑ i : Fin n, ∑ j : Fin n,
        f i j p q := by
  calc
    _ = ∑ i : Fin n, ∑ p : Fin n, ∑ j : Fin n, ∑ q : Fin n,
          f i j p q := by
      apply Finset.sum_congr rfl
      intro i _
      exact Finset.sum_comm
    _ = ∑ p : Fin n, ∑ i : Fin n, ∑ j : Fin n, ∑ q : Fin n,
          f i j p q := Finset.sum_comm
    _ = ∑ p : Fin n, ∑ i : Fin n, ∑ q : Fin n, ∑ j : Fin n,
          f i j p q := by
      apply Finset.sum_congr rfl
      intro p _
      apply Finset.sum_congr rfl
      intro i _
      exact Finset.sum_comm
    _ = ∑ p : Fin n, ∑ q : Fin n, ∑ i : Fin n, ∑ j : Fin n,
          f i j p q := by
      apply Finset.sum_congr rfl
      intro p _
      exact Finset.sum_comm

theorem neutralNF665Quadratic_congruence {n : ℕ}
    (H K : Fin n → Fin n → ℝ) (y : Fin n → ℝ) :
    neutralNF661Quadratic (neutralNF662Congruence K H) y =
      neutralNF661Quadratic H (neutralNF665TransposeAction K y) := by
  unfold neutralNF661Quadratic neutralNF662Congruence
  calc
    (∑ i : Fin n, ∑ j : Fin n,
      (∑ p : Fin n, ∑ q : Fin n, K i p * K j q * H p q) *
        y i * y j) =
      ∑ i : Fin n, ∑ j : Fin n, ∑ p : Fin n, ∑ q : Fin n,
        K i p * K j q * H p q * y i * y j := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      simp only [Finset.sum_mul]
    _ = ∑ p : Fin n, ∑ q : Fin n, ∑ i : Fin n, ∑ j : Fin n,
          K i p * K j q * H p q * y i * y j :=
      neutralNF665FourSum_exchange
        (fun i j p q => K i p * K j q * H p q * y i * y j)
    _ = ∑ p : Fin n, ∑ q : Fin n,
          H p q * (∑ i : Fin n, y i * K i p) *
            (∑ j : Fin n, y j * K j q) := by
      apply Finset.sum_congr rfl
      intro p _
      apply Finset.sum_congr rfl
      intro q _
      calc
        (∑ i : Fin n, ∑ j : Fin n,
            K i p * K j q * H p q * y i * y j) =
          ∑ i : Fin n, ∑ j : Fin n,
            (H p q * (y i * K i p)) * (y j * K j q) := by
          apply Finset.sum_congr rfl
          intro i _
          apply Finset.sum_congr rfl
          intro j _
          ring
        _ = ∑ i : Fin n,
              (H p q * (y i * K i p)) *
                (∑ j : Fin n, y j * K j q) := by
          apply Finset.sum_congr rfl
          intro i _
          rw [Finset.mul_sum]
        _ = (∑ i : Fin n, H p q * (y i * K i p)) *
              (∑ j : Fin n, y j * K j q) := by
          rw [Finset.sum_mul]
        _ = H p q * (∑ i : Fin n, y i * K i p) *
              (∑ j : Fin n, y j * K j q) := by
          rw [Finset.mul_sum]
    _ = ∑ p : Fin n, ∑ q : Fin n,
          H p q * neutralNF665TransposeAction K y p *
            neutralNF665TransposeAction K y q := rfl

/-- A nonsingular lower-triangular real matrix gives a genuinely
surjective coordinate map. Uses determinant, not an analytic assumption. -/
theorem neutralNF665Transpose_surjective_of_lower {n : ℕ}
    (K : Matrix (Fin n) (Fin n) ℝ)
    (hTri : K.IsLowerTriangular)
    (hDiag : ∀ i : Fin n, K i i ≠ 0) :
    ∀ x : Fin n → ℝ, ∃ y : Fin n → ℝ,
      neutralNF665TransposeAction K y = x := by
  have hDet : K.det ≠ 0 :=
    (hTri.det_ne_zero_iff).2 (fun i => hDiag i)
  have hUnit : IsUnit K :=
    (Matrix.isUnit_iff_isUnit_det K).2
      (isUnit_iff_ne_zero.mpr hDet)
  have hSurj :
      Function.Surjective
        (fun y : Fin n → ℝ => Matrix.vecMul y K) :=
    (Matrix.vecMul_surjective_iff_isUnit).2 hUnit
  intro x
  obtain ⟨y, hy⟩ := hSurj x
  refine ⟨y, ?_⟩
  funext p
  have hp := congrArg (fun v : Fin n → ℝ => v p) hy
  simpa [neutralNF665TransposeAction, Matrix.vecMul, dotProduct,
    mul_comm] using hp

#print axioms neutralNF665FrobeniusNorm_bound
#print axioms neutralNF665FourSum_exchange
#print axioms neutralNF665Quadratic_congruence
#print axioms neutralNF665Transpose_surjective_of_lower

end
end WeilDefect
