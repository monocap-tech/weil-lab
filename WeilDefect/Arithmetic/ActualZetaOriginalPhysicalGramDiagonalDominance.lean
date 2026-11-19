import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramCoercivityLemmas

namespace WeilDefect

/-! NF659: source-independent pieces of the finite-dimensional
Gershgorin / diagonal-dominance positivity argument. The off-diagonal
energy is nonnegative termwise, and symmetric row/column payments
can be interchanged without approximating the underlying matrix. -/

theorem neutralNF659OffDiagonalEnergy_nonneg
    {n : ℕ} (a : Fin n → Fin n → ℝ) (y : Fin n → ℝ) :
    0 ≤ ∑ i : Fin n, ∑ j : Fin n,
      if i = j then (0 : ℝ) else
        (|a i j| * (y i ^ 2 + y j ^ 2) + 2 * a i j * y i * y j) := by
  apply Finset.sum_nonneg
  intro i _
  apply Finset.sum_nonneg
  intro j _
  by_cases hij : i = j
  · simp [hij]
  · simp only [if_neg hij]
    have h := neutralNF658CrossTerm_lower (a i j) (y i) (y j)
    nlinarith

theorem neutralNF659OffDiagonalAbs_swap
    {n : ℕ} (a : Fin n → Fin n → ℝ) (y : Fin n → ℝ)
    (ha : ∀ i j, a i j = a j i) :
    (∑ i : Fin n, ∑ j : Fin n,
      (if i = j then (0 : ℝ) else |a i j|) * y j ^ 2) =
    (∑ i : Fin n, ∑ j : Fin n,
      (if i = j then (0 : ℝ) else |a i j|) * y i ^ 2) := by
  calc
    (∑ i : Fin n, ∑ j : Fin n,
      (if i = j then (0 : ℝ) else |a i j|) * y j ^ 2) =
        ∑ j : Fin n, ∑ i : Fin n,
          (if i = j then (0 : ℝ) else |a i j|) * y j ^ 2 :=
      Finset.sum_comm
    _ = ∑ j : Fin n, ∑ i : Fin n,
          (if j = i then (0 : ℝ) else |a j i|) * y j ^ 2 := by
      apply Finset.sum_congr rfl
      intro j _
      apply Finset.sum_congr rfl
      intro i _
      by_cases hij : i = j
      · subst j
        simp
      · have hji : j ≠ i := Ne.symm hij
        simp only [if_neg hij, if_neg hji, ha i j]
    _ = (∑ i : Fin n, ∑ j : Fin n,
      (if i = j then (0 : ℝ) else |a i j|) * y i ^ 2) := rfl

#print axioms neutralNF659OffDiagonalEnergy_nonneg
#print axioms neutralNF659OffDiagonalAbs_swap

end WeilDefect
