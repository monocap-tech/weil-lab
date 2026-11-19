import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramDiagonalDominance

namespace WeilDefect

/-!
NF660: finite-dimensional diagonal-dominance coercivity, independent of
numerical data. This lemma does not assume that a proposed interval witness
is true. A subsequent attachment must bind the exact original physical Gram
entries to the NF658 intervals and NF659 integer-transformed intervals.
-/

noncomputable section
open Finset

/-- A symmetric real finite matrix dominates its row Gershgorin payments
in the actual, untransformed real quadratic form. -/
theorem neutralNF660SymmetricRowPayment_bound
    {n : ℕ} (a : Fin n → Fin n → ℝ) (y : Fin n → ℝ)
    (ha : ∀ i j, a i j = a j i) :
    (∑ i : Fin n,
       (a i i - ∑ j : Fin n, if i = j then (0 : ℝ) else |a i j|) * y i ^ 2)
      ≤ ∑ i : Fin n, ∑ j : Fin n, a i j * y i * y j := by
  classical
  let pay : ℝ := ∑ i : Fin n, ∑ j : Fin n,
    (if i = j then (0 : ℝ) else |a i j|) * y i ^ 2
  let colpay : ℝ := ∑ i : Fin n, ∑ j : Fin n,
    (if i = j then (0 : ℝ) else |a i j|) * y j ^ 2
  let cross : ℝ := ∑ i : Fin n, ∑ j : Fin n,
    if i = j then (0 : ℝ) else a i j * y i * y j
  let diag : ℝ := ∑ i : Fin n, a i i * y i ^ 2
  have hswap : colpay = pay :=
    neutralNF659OffDiagonalAbs_swap a y ha
  have hterm (i j : Fin n) :
      (if i = j then (0 : ℝ) else
          (|a i j| * (y i ^ 2 + y j ^ 2) + 2 * a i j * y i * y j)) =
        (if i = j then (0 : ℝ) else |a i j|) * y i ^ 2 +
        (if i = j then (0 : ℝ) else |a i j|) * y j ^ 2 +
        2 * (if i = j then (0 : ℝ) else a i j * y i * y j) := by
    by_cases hij : i = j
    · simp [hij]
    · simp only [if_neg hij]
      ring
  have henergy :
      (∑ i : Fin n, ∑ j : Fin n,
        if i = j then (0 : ℝ) else
          (|a i j| * (y i ^ 2 + y j ^ 2) + 2 * a i j * y i * y j))
        = pay + colpay + 2 * cross := by
    calc
      _ = ∑ i : Fin n, ∑ j : Fin n,
          ((if i = j then (0 : ℝ) else |a i j|) * y i ^ 2 +
           (if i = j then (0 : ℝ) else |a i j|) * y j ^ 2 +
           2 * (if i = j then (0 : ℝ) else a i j * y i * y j)) := by
        apply Finset.sum_congr rfl
        intro i _
        apply Finset.sum_congr rfl
        intro j _
        exact hterm i j
      _ = pay + colpay + 2 * cross := by
        simp only [Finset.sum_add_distrib, ← Finset.mul_sum]
        rfl
  have hnonneg := neutralNF659OffDiagonalEnergy_nonneg a y
  rw [henergy, hswap] at hnonneg
  have hcross : -pay ≤ cross := by
    linarith
  have hdiagterm (i j : Fin n) :
      a i j * y i * y j =
        (if i = j then a i i * y i ^ 2 else (0 : ℝ)) +
        (if i = j then (0 : ℝ) else a i j * y i * y j) := by
    by_cases hij : i = j
    · subst j
      simp [pow_two]
    · simp [hij]
  have hrow (i : Fin n) :
      (∑ j : Fin n, a i j * y i * y j) =
        a i i * y i ^ 2 +
          ∑ j : Fin n, if i = j then (0 : ℝ) else a i j * y i * y j := by
    calc
      _ = ∑ j : Fin n,
          ((if i = j then a i i * y i ^ 2 else (0 : ℝ)) +
           (if i = j then (0 : ℝ) else a i j * y i * y j)) := by
        apply Finset.sum_congr rfl
        intro j _
        exact hdiagterm i j
      _ = _ := by
        rw [Finset.sum_add_distrib]
        simp
  have hquadratic :
      (∑ i : Fin n, ∑ j : Fin n, a i j * y i * y j) = diag + cross := by
    calc
      _ = ∑ i : Fin n,
          (a i i * y i ^ 2 +
           ∑ j : Fin n, if i = j then (0 : ℝ) else a i j * y i * y j) := by
        apply Finset.sum_congr rfl
        intro i _
        exact hrow i
      _ = diag + cross := by
        simp only [Finset.sum_add_distrib]
        rfl
  have hpayment :
      (∑ i : Fin n,
        (a i i - ∑ j : Fin n, if i = j then (0 : ℝ) else |a i j|) * y i ^ 2)
          = diag - pay := by
    dsimp [diag, pay]
    simp only [sub_mul, Finset.sum_sub_distrib, Finset.sum_mul]
  rw [hpayment, hquadratic]
  linarith

/-- Uniform strict or non-strict diagonal dominance supplies a concrete
Euclidean coercivity margin for every real vector. -/
theorem neutralNF660Dominance_coercivity
    {n : ℕ} (a : Fin n → Fin n → ℝ) (y : Fin n → ℝ)
    (ha : ∀ i j, a i j = a j i) (margin : ℝ)
    (hm : ∀ i : Fin n,
      margin ≤ a i i -
        ∑ j : Fin n, if i = j then (0 : ℝ) else |a i j|) :
    margin * (∑ i : Fin n, y i ^ 2) ≤
      ∑ i : Fin n, ∑ j : Fin n, a i j * y i * y j := by
  calc
    margin * (∑ i : Fin n, y i ^ 2) =
        ∑ i : Fin n, margin * y i ^ 2 := by
          rw [Finset.mul_sum]
    _ ≤ ∑ i : Fin n,
        (a i i - ∑ j : Fin n,
          if i = j then (0 : ℝ) else |a i j|) * y i ^ 2 := by
          apply Finset.sum_le_sum
          intro i _
          exact mul_le_mul_of_nonneg_right (hm i) (sq_nonneg _)
    _ ≤ _ := neutralNF660SymmetricRowPayment_bound a y ha

/-- A certified interval matrix controls the *actual* row margin,
independently of the calculation that produced its centers and radii. -/
theorem neutralNF660Interval_rowMargin
    {n : ℕ} (a c r : Fin n → Fin n → ℝ)
    (h : ∀ i j, |a i j - c i j| ≤ r i j)
    (margin : ℝ)
    (hm : ∀ i : Fin n,
      margin ≤ c i i - r i i -
        ∑ j : Fin n, if i = j then (0 : ℝ) else |c i j| + r i j) :
    ∀ i : Fin n,
      margin ≤ a i i -
        ∑ j : Fin n, if i = j then (0 : ℝ) else |a i j| := by
  classical
  intro i
  have hdiag : c i i - r i i ≤ a i i := by
    have hh := (abs_le.mp (h i i)).1
    linarith
  have habs (j : Fin n) : |a i j| ≤ |c i j| + r i j := by
    calc
      |a i j| = |(a i j - c i j) + c i j| := by ring
      _ ≤ |a i j - c i j| + |c i j| := abs_add_le _ _
      _ ≤ r i j + |c i j| := add_le_add_right (h i j) _
      _ = |c i j| + r i j := by ring
  have hpay :
      (∑ j : Fin n, if i = j then (0 : ℝ) else |a i j|) ≤
      (∑ j : Fin n, if i = j then (0 : ℝ) else |c i j| + r i j) := by
    apply Finset.sum_le_sum
    intro j _
    by_cases hij : i = j
    · simp [hij]
    · simpa only [if_neg hij] using habs j
  linarith [hm i]

theorem neutralNF660Interval_coercivity
    {n : ℕ} (a c r : Fin n → Fin n → ℝ)
    (ha : ∀ i j, a i j = a j i)
    (h : ∀ i j, |a i j - c i j| ≤ r i j)
    (margin : ℝ)
    (hm : ∀ i : Fin n,
      margin ≤ c i i - r i i -
        ∑ j : Fin n, if i = j then (0 : ℝ) else |c i j| + r i j)
    (y : Fin n → ℝ) :
    margin * (∑ i : Fin n, y i ^ 2) ≤
      ∑ i : Fin n, ∑ j : Fin n, a i j * y i * y j := by
  exact neutralNF660Dominance_coercivity a y ha margin
    (neutralNF660Interval_rowMargin a c r h margin hm)

#print axioms neutralNF660Interval_coercivity
end
end WeilDefect
