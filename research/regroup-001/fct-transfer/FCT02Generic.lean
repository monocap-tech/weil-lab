import Mathlib

namespace WeilDefect

noncomputable section
open Finset

theorem neutralNF658CrossTerm_lower (a u v : ℝ) :
    -|a| * (u^2 + v^2) ≤ 2*a*u*v := by
  rcases le_total 0 a with ha | ha
  · rw [abs_of_nonneg ha]
    have hs : 0 ≤ a * (u+v)^2 :=
      mul_nonneg ha (sq_nonneg _)
    nlinarith
  · rw [abs_of_nonpos ha]
    have hs : 0 ≤ (-a) * (u-v)^2 :=
      mul_nonneg (neg_nonneg.mpr ha) (sq_nonneg _)
    nlinarith

theorem neutralNF658Bilinear_enclosure
    (center radius actual u v : ℝ)
    (h : |actual-center| ≤ radius) :
    center*u*v - radius*|u*v| ≤ actual*u*v := by
  have hp : |(actual-center)*(u*v)| ≤ radius*|u*v| := by
    rw [abs_mul]
    exact mul_le_mul_of_nonneg_right h (abs_nonneg _)
  have hn : -(radius*|u*v|) ≤ (actual-center)*(u*v) :=
    (neg_le_of_abs_le hp)
  nlinarith [hn]

theorem neutralNF659WeightedSum_bound
    {ι : Type*} [Fintype ι] (w a c r : ι → ℝ)
    (h : ∀ i, |a i - c i| ≤ r i) :
    |(∑ i, w i * a i) - (∑ i, w i * c i)| ≤
      ∑ i, |w i| * r i := by
  have ht (i : ι) :
      |w i * (a i - c i)| ≤ |w i| * r i := by
    rw [abs_mul]
    exact mul_le_mul_of_nonneg_left (h i) (abs_nonneg _)
  calc
    |(∑ i, w i * a i) - (∑ i, w i * c i)| =
        |∑ i, w i * (a i - c i)| := by
          simp only [mul_sub, Finset.sum_sub_distrib]
    _ ≤ ∑ i, |w i * (a i - c i)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i, |w i| * r i :=
      Finset.sum_le_sum (fun i _ => ht i)

theorem neutralNF659DoubleSum_bound
    {ι κ : Type*} [Fintype ι] [Fintype κ]
    (w a c r : ι → κ → ℝ)
    (h : ∀ i j, |a i j - c i j| ≤ r i j) :
    |(∑ i, ∑ j, w i j * a i j) -
        (∑ i, ∑ j, w i j * c i j)| ≤
      ∑ i, ∑ j, |w i j| * r i j := by
  have hi (i : ι) :
      |(∑ j, w i j * a i j) -
          (∑ j, w i j * c i j)| ≤
        ∑ j, |w i j| * r i j :=
    neutralNF659WeightedSum_bound
      (w i) (a i) (c i) (r i) (h i)
  have ho := neutralNF659WeightedSum_bound
    (fun _ : ι => (1 : ℝ))
    (fun i => ∑ j, w i j * a i j)
    (fun i => ∑ j, w i j * c i j)
    (fun i => ∑ j, |w i j| * r i j) hi
  simpa only [one_mul, abs_one] using ho

theorem neutralNF659CongruenceEntry_bound
    {n : ℕ}
    (H C E K : Fin n → Fin n → ℝ)
    (h : ∀ p q, |H p q - C p q| ≤ E p q)
    (i j : Fin n) :
    |(∑ p : Fin n, ∑ q : Fin n, K i p * K j q * H p q) -
        (∑ p : Fin n, ∑ q : Fin n, K i p * K j q * C p q)| ≤
      ∑ p : Fin n, ∑ q : Fin n,
        |K i p * K j q| * E p q := by
  exact neutralNF659DoubleSum_bound
    (fun p q => K i p * K j q) H C E h

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
      simp [pow_two] <;> ring
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
      |a i j| = |(a i j - c i j) + c i j| := by rw [sub_add_cancel]
      _ ≤ |a i j - c i j| + |c i j| := abs_add_le _ _
      _ ≤ r i j + |c i j| := by
          simpa only [add_comm] using (add_le_add_right (h i j) (|c i j|))
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

def neutralNF661Quadratic {n : ℕ}
    (a : Fin n → Fin n → ℝ) (x : Fin n → ℝ) : ℝ :=
  ∑ i : Fin n, ∑ j : Fin n, a i j * x i * x j

def neutralNF661SqNorm {n : ℕ} (x : Fin n → ℝ) : ℝ :=
  ∑ i : Fin n, x i ^ 2

theorem neutralNF661SqNorm_nonneg {n : ℕ} (x : Fin n → ℝ) :
    0 ≤ neutralNF661SqNorm x := by
  unfold neutralNF661SqNorm
  exact Finset.sum_nonneg (fun i _ => sq_nonneg _)

theorem neutralNF661Coercivity_of_preconditioned
    {n : ℕ}
    (H B : Fin n → Fin n → ℝ)
    (T : (Fin n → ℝ) → (Fin n → ℝ))
    (m normBound target : ℝ)
    (htarget : 0 ≤ target)
    (hmargin : ∀ y, m * neutralNF661SqNorm y ≤
      neutralNF661Quadratic B y)
    (hcongruence : ∀ y,
      neutralNF661Quadratic B y =
        neutralNF661Quadratic H (T y))
    (hnorm : ∀ y,
      neutralNF661SqNorm (T y) ≤ normBound * neutralNF661SqNorm y)
    (honto : ∀ x, ∃ y, T y = x)
    (hgate : target * normBound ≤ m) :
    ∀ x, target * neutralNF661SqNorm x ≤
      neutralNF661Quadratic H x := by
  intro x
  obtain ⟨y, hy⟩ := honto x
  subst x
  have hnorm' := hnorm y
  have hpos := neutralNF661SqNorm_nonneg y
  calc
    target * neutralNF661SqNorm (T y) ≤
        target * (normBound * neutralNF661SqNorm y) :=
      mul_le_mul_of_nonneg_left hnorm' htarget
    _ = (target * normBound) * neutralNF661SqNorm y := by ring
    _ ≤ m * neutralNF661SqNorm y :=
      mul_le_mul_of_nonneg_right hgate hpos
    _ ≤ neutralNF661Quadratic B y := hmargin y
    _ = neutralNF661Quadratic H (T y) := hcongruence y

theorem neutralNF662SymmetricLower_to_full
    {n : ℕ} (H C E : Fin n → Fin n → ℝ)
    (hH : ∀ i j, H i j = H j i)
    (hC : ∀ i j, C i j = C j i)
    (hE : ∀ i j, E i j = E j i)
    (hLower : ∀ i j, j.val ≤ i.val →
      |H i j - C i j| ≤ E i j) :
    ∀ i j, |H i j - C i j| ≤ E i j := by
  intro i j
  by_cases hij : j.val ≤ i.val
  · exact hLower i j hij
  · have hji : i.val ≤ j.val := by omega
    have hb := hLower j i hji
    rw [← hH i j, ← hC i j, ← hE i j] at hb
    exact hb

def neutralNF662Congruence {n : ℕ}
    (K H : Fin n → Fin n → ℝ) (i j : Fin n) : ℝ :=
  ∑ p : Fin n, ∑ q : Fin n, K i p * K j q * H p q

def neutralNF662Center {n : ℕ}
    (K C : Fin n → Fin n → ℝ) (i j : Fin n) : ℝ :=
  ∑ p : Fin n, ∑ q : Fin n, K i p * K j q * C p q

def neutralNF662Radius {n : ℕ}
    (K E : Fin n → Fin n → ℝ) (i j : Fin n) : ℝ :=
  ∑ p : Fin n, ∑ q : Fin n, |K i p * K j q| * E p q

theorem neutralNF662ActualCongruence_enclosed
    {n : ℕ} (H C E K : Fin n → Fin n → ℝ)
    (h : ∀ i j, |H i j - C i j| ≤ E i j)
    (i j : Fin n) :
    |neutralNF662Congruence K H i j -
      neutralNF662Center K C i j| ≤
        neutralNF662Radius K E i j := by
  exact neutralNF659CongruenceEntry_bound H C E K h i j

def neutralNF663CenterInteger {n : ℕ}
    (K C : Fin n → Fin n → ℤ) (i j : Fin n) : ℤ :=
  ∑ p : Fin n, ∑ q : Fin n, K i p * K j q * C p q

def neutralNF663RadiusInteger {n : ℕ}
    (K E : Fin n → Fin n → ℤ) (i j : Fin n) : ℤ :=
  ∑ p : Fin n, ∑ q : Fin n, |K i p * K j q| * E p q

theorem neutralNF663CenterInteger_cast {n : ℕ}
    (K C : Fin n → Fin n → ℤ) (i j : Fin n) :
    (neutralNF663CenterInteger K C i j : ℝ) =
      ∑ p : Fin n, ∑ q : Fin n,
        (K i p : ℝ) * (K j q : ℝ) * (C p q : ℝ) := by
  simp only [neutralNF663CenterInteger, Int.cast_sum, Int.cast_mul]

theorem neutralNF663RadiusInteger_cast {n : ℕ}
    (K E : Fin n → Fin n → ℤ) (i j : Fin n) :
    (neutralNF663RadiusInteger K E i j : ℝ) =
      ∑ p : Fin n, ∑ q : Fin n,
        |(K i p : ℝ) * (K j q : ℝ)| * (E p q : ℝ) := by
  simp only [neutralNF663RadiusInteger, Int.cast_sum,
    Int.cast_mul, Int.cast_abs]

theorem neutralNF663Center_scale {n : ℕ}
    (K C : Fin n → Fin n → ℤ) (S : ℝ) (hS : S ≠ 0)
    (i j : Fin n) :
    neutralNF662Center
      (fun a b => (K a b : ℝ) / S)
      (fun a b => (C a b : ℝ) / S) i j =
      (neutralNF663CenterInteger K C i j : ℝ) / S ^ 3 := by
  unfold neutralNF662Center
  calc
    (∑ p : Fin n, ∑ q : Fin n,
      (K i p : ℝ) / S * ((K j q : ℝ) / S) * ((C p q : ℝ) / S)) =
        ∑ p : Fin n, ∑ q : Fin n,
          ((K i p : ℝ) * (K j q : ℝ) * (C p q : ℝ)) / S ^ 3 := by
      apply Finset.sum_congr rfl
      intro p _
      apply Finset.sum_congr rfl
      intro q _
      field_simp [hS] <;> ring
    _ = (∑ p : Fin n, ∑ q : Fin n,
          (K i p : ℝ) * (K j q : ℝ) * (C p q : ℝ)) / S ^ 3 := by
      simp only [Finset.sum_div]
    _ = (neutralNF663CenterInteger K C i j : ℝ) / S ^ 3 := by
      rw [neutralNF663CenterInteger_cast]

theorem neutralNF663Radius_scale {n : ℕ}
    (K E : Fin n → Fin n → ℤ) (S : ℝ) (hS : 0 < S)
    (i j : Fin n) :
    neutralNF662Radius
      (fun a b => (K a b : ℝ) / S)
      (fun a b => (E a b : ℝ) / S) i j =
      (neutralNF663RadiusInteger K E i j : ℝ) / S ^ 3 := by
  unfold neutralNF662Radius
  calc
    (∑ p : Fin n, ∑ q : Fin n,
      |((K i p : ℝ) / S) * ((K j q : ℝ) / S)| *
        ((E p q : ℝ) / S)) =
        ∑ p : Fin n, ∑ q : Fin n,
          (|(K i p : ℝ) * (K j q : ℝ)| * (E p q : ℝ)) / S ^ 3 := by
      apply Finset.sum_congr rfl
      intro p _
      apply Finset.sum_congr rfl
      intro q _
      rw [abs_mul, abs_div, abs_div, abs_of_pos hS]
      rw [abs_mul]
      field_simp [ne_of_gt hS] <;> ring
    _ = (∑ p : Fin n, ∑ q : Fin n,
          |(K i p : ℝ) * (K j q : ℝ)| * (E p q : ℝ)) / S ^ 3 := by
      simp only [Finset.sum_div]
    _ = (neutralNF663RadiusInteger K E i j : ℝ) / S ^ 3 := by
      rw [neutralNF663RadiusInteger_cast]

theorem neutralNF663ActualIntegerCongruence_enclosed {n : ℕ}
    (H : Fin n → Fin n → ℝ)
    (K C E : Fin n → Fin n → ℤ)
    (S : ℝ) (hS : 0 < S)
    (hSource : ∀ p q : Fin n,
      |H p q - (C p q : ℝ) / S| ≤ (E p q : ℝ) / S)
    (i j : Fin n) :
    |neutralNF662Congruence (fun a b => (K a b : ℝ) / S)
        H i j -
      (neutralNF663CenterInteger K C i j : ℝ) / S ^ 3| ≤
      (neutralNF663RadiusInteger K E i j : ℝ) / S ^ 3 := by
  have hb := neutralNF662ActualCongruence_enclosed
    H (fun a b => (C a b : ℝ) / S)
      (fun a b => (E a b : ℝ) / S)
      (fun a b => (K a b : ℝ) / S)
    hSource i j
  rw [neutralNF663Center_scale K C S (ne_of_gt hS) i j,
      neutralNF663Radius_scale K E S hS i j] at hb
  exact hb

theorem neutralNF664Congruence_symm {n : ℕ}
    (K H : Fin n → Fin n → ℝ)
    (hH : ∀ p q, H p q = H q p)
    (i j : Fin n) :
    neutralNF662Congruence K H i j =
      neutralNF662Congruence K H j i := by
  unfold neutralNF662Congruence
  calc
    (∑ p : Fin n, ∑ q : Fin n, K i p * K j q * H p q) =
      ∑ q : Fin n, ∑ p : Fin n, K i p * K j q * H p q :=
        Finset.sum_comm
    _ = ∑ q : Fin n, ∑ p : Fin n, K j q * K i p * H q p := by
      apply Finset.sum_congr rfl
      intro q _
      apply Finset.sum_congr rfl
      intro p _
      rw [hH p q]
      ring
    _ = ∑ p : Fin n, ∑ q : Fin n, K j p * K i q * H p q := rfl

theorem neutralNF664ScaledRowMargin
    {n : ℕ} (T U : Fin n → Fin n → ℤ)
    (denom : ℝ) (hd : 0 < denom) (m : ℤ)
    (hm : ∀ i : Fin n,
      m ≤ T i i - U i i -
        ∑ j : Fin n, if i = j then (0 : ℤ)
          else |T i j| + U i j) :
    ∀ i : Fin n,
      (m : ℝ) / denom ≤
        (T i i : ℝ) / denom - (U i i : ℝ) / denom -
        ∑ j : Fin n, if i = j then (0 : ℝ)
          else |(T i j : ℝ) / denom| + (U i j : ℝ) / denom := by
  classical
  intro i
  have hs (j : Fin n) :
      (if i = j then (0 : ℝ) else
        |(T i j : ℝ) / denom| + (U i j : ℝ) / denom) =
      ((if i = j then (0 : ℤ) else |T i j| + U i j : ℤ) : ℝ) / denom := by
    by_cases hij : i = j
    · simp [hij]
    · simp only [if_neg hij, Int.cast_add, Int.cast_abs]
      rw [abs_div, abs_of_pos hd]
      ring
  have hcast :
      (m : ℝ) ≤ (T i i : ℝ) - (U i i : ℝ) -
        ∑ j : Fin n,
          ((if i = j then (0 : ℤ) else |T i j| + U i j : ℤ) : ℝ) := by
    exact_mod_cast hm i
  have hdiv := (div_le_div_of_nonneg_right hcast hd.le)
  have hrewrite :
      ((T i i : ℝ) - (U i i : ℝ) -
        ∑ j : Fin n,
          ((if i = j then (0 : ℤ) else |T i j| + U i j : ℤ) : ℝ)) / denom =
      (T i i : ℝ) / denom - (U i i : ℝ) / denom -
        ∑ j : Fin n,
          (if i = j then (0 : ℝ) else
            |(T i j : ℝ) / denom| + (U i j : ℝ) / denom) := by
    rw [sub_div, sub_div, Finset.sum_div]
    congr 1
    apply Finset.sum_congr rfl
    intro j _
    exact (hs j).symm
  rw [hrewrite] at hdiv
  exact hdiv

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
          have hfactor :
              (∑ i : Fin n, H p q * (y i * K i p)) =
                H p q * (∑ i : Fin n, y i * K i p) := by
            rw [Finset.mul_sum]
          rw [hfactor]
    _ = ∑ p : Fin n, ∑ q : Fin n,
          H p q * neutralNF665TransposeAction K y p *
            neutralNF665TransposeAction K y q := rfl

theorem neutralNF665Transpose_surjective_of_lower {n : ℕ}
    (K : Matrix (Fin n) (Fin n) ℝ)
    (hTri : K.IsLowerTriangular)
    (hDiag : ∀ i : Fin n, K i i ≠ 0) :
    ∀ x : Fin n → ℝ, ∃ y : Fin n → ℝ,
      neutralNF665TransposeAction K y = x := by
  have hDet : K.det ≠ 0 := by
    rw [Matrix.det_of_isLowerTriangular K hTri]
    exact Finset.prod_ne_zero_iff.mpr (fun i _ => hDiag i)
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
  simpa only [neutralNF665TransposeAction, Matrix.vecMul_apply_eq_sum]
    using hp

#print axioms neutralNF658CrossTerm_lower
#print axioms neutralNF658Bilinear_enclosure
#print axioms neutralNF659WeightedSum_bound
#print axioms neutralNF659DoubleSum_bound
#print axioms neutralNF659CongruenceEntry_bound
#print axioms neutralNF659OffDiagonalEnergy_nonneg
#print axioms neutralNF659OffDiagonalAbs_swap
#print axioms neutralNF660SymmetricRowPayment_bound
#print axioms neutralNF660Dominance_coercivity
#print axioms neutralNF660Interval_rowMargin
#print axioms neutralNF660Interval_coercivity
#print axioms neutralNF661Quadratic
#print axioms neutralNF661SqNorm
#print axioms neutralNF661SqNorm_nonneg
#print axioms neutralNF661Coercivity_of_preconditioned
#print axioms neutralNF662SymmetricLower_to_full
#print axioms neutralNF662Congruence
#print axioms neutralNF662Center
#print axioms neutralNF662Radius
#print axioms neutralNF662ActualCongruence_enclosed
#print axioms neutralNF663CenterInteger
#print axioms neutralNF663RadiusInteger
#print axioms neutralNF663CenterInteger_cast
#print axioms neutralNF663RadiusInteger_cast
#print axioms neutralNF663Center_scale
#print axioms neutralNF663Radius_scale
#print axioms neutralNF663ActualIntegerCongruence_enclosed
#print axioms neutralNF664Congruence_symm
#print axioms neutralNF664ScaledRowMargin
#print axioms neutralNF665TransposeAction
#print axioms neutralNF665FrobeniusNorm_bound
#print axioms neutralNF665FourSum_exchange
#print axioms neutralNF665Quadratic_congruence
#print axioms neutralNF665Transpose_surjective_of_lower

end
end WeilDefect
