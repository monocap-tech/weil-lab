import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMatrixProductReceipts

namespace WeilDefect
open Finset

/-! NF683: deterministic signed-digit packing.  A packed equality
is not a hash: bounded digit uniqueness recovers every coordinate.
The bound on the actual dot products is an explicit hypothesis
discharged by independently checked operand bounds. -/

def neutralNF683Pack (B : ℤ) {n : ℕ} (x : Fin n → ℤ) : ℤ :=
  ∑ j, x j * B ^ j.val

theorem neutralNF683Pack_succ (B : ℤ) {n : ℕ}
    (x : Fin (n+1) → ℤ) :
    neutralNF683Pack B x =
      x 0 + B * neutralNF683Pack B (fun j : Fin n => x j.succ) := by
  unfold neutralNF683Pack
  rw [Fin.sum_univ_succ]
  simp only [Fin.val_zero, pow_zero, mul_one, Fin.val_succ, pow_succ,
    Finset.mul_sum]
  congr 1
  apply Finset.sum_congr rfl
  intro j _
  ring

theorem neutralNF683Pack_zero_small (B : ℤ) (hB : 0 < B)
    (n : ℕ) (x : Fin n → ℤ) (hx : ∀ j, |x j| < B)
    (hpack : neutralNF683Pack B x = 0) : ∀ j, x j = 0 := by
  induction n with
  | zero =>
    intro j
    exact Fin.elim0 j
  | succ n ih =>
    let tail : Fin n → ℤ := fun j => x j.succ
    have he : x 0 + B * neutralNF683Pack B tail = 0 := by
      rw [← neutralNF683Pack_succ B x]
      exact hpack
    have hsmall := abs_lt.mp (hx 0)
    have ht : neutralNF683Pack B tail = 0 := by
      by_contra hn
      rcases lt_or_gt_of_ne hn with hn | hn
      · have hle : neutralNF683Pack B tail ≤ -1 := by omega
        have hm := mul_le_mul_of_nonneg_left hle (le_of_lt hB)
        simp only [mul_neg, mul_one] at hm
        omega
      · have hle : (1 : ℤ) ≤ neutralNF683Pack B tail := by omega
        have hm := mul_le_mul_of_nonneg_left hle (le_of_lt hB)
        simp only [mul_one] at hm
        omega
    have h0 : x 0 = 0 := by simpa [ht] using he
    have hs : ∀ j : Fin n, tail j = 0 :=
      ih tail (fun j => hx j.succ) ht
    intro j
    refine Fin.cases h0 (fun k => hs k) j

theorem neutralNF683Pack_sub (B : ℤ) {n : ℕ} (x y : Fin n → ℤ) :
    neutralNF683Pack B (fun j => x j - y j) =
      neutralNF683Pack B x - neutralNF683Pack B y := by
  simp only [neutralNF683Pack, sub_mul, Finset.sum_sub_distrib]

theorem neutralNF683Pack_injective_bounded (B : ℤ) (hB : 0 < B)
    {n : ℕ} (x y : Fin n → ℤ)
    (hsmall : ∀ j, |x j - y j| < B)
    (he : neutralNF683Pack B x = neutralNF683Pack B y) :
    ∀ j, x j = y j := by
  have hz : neutralNF683Pack B (fun j => x j - y j) = 0 := by
    rw [neutralNF683Pack_sub, he, sub_self]
  intro j
  exact sub_eq_zero.mp (neutralNF683Pack_zero_small B hB n _ hsmall hz j)

theorem neutralNF683Pack_dot (B : ℤ) {m n : ℕ}
    (x : Fin m → ℤ) (Y : Fin m → Fin n → ℤ) :
    neutralNF683Pack B (fun j => neutralNF626Dot x (fun k => Y k j)) =
      neutralNF626Dot x (fun k => neutralNF683Pack B (Y k)) := by
  unfold neutralNF683Pack neutralNF626Dot
  simp_rw [Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro k _
  apply Finset.sum_congr rfl
  intro j _
  ring

/-- Independently checked operand and result bounds suffice; the
error bound does not presuppose any product-coordinate equality. -/
theorem neutralNF683Dot_error_bound {m n : ℕ}
    (x : Fin m → ℤ) (Y : Fin m → Fin n → ℤ) (z : Fin n → ℤ)
    (X M Z B : ℤ)
    (hX : ∑ k, |x k| ≤ X) (hM : 0 ≤ M)
    (hY : ∀ k j, |Y k j| ≤ M) (hZ : ∀ j, |z j| ≤ Z)
    (hB : X*M+Z < B) (j : Fin n) :
    |neutralNF626Dot x (fun k => Y k j) - z j| < B := by
  have hd : |neutralNF626Dot x (fun k => Y k j)| ≤ X*M := by
    unfold neutralNF626Dot
    calc
      |∑ k, x k * Y k j| ≤ ∑ k, |x k * Y k j| :=
        Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ k, |x k| * M := by
        apply Finset.sum_le_sum
        intro k _
        rw [abs_mul]
        exact mul_le_mul_of_nonneg_left (hY k j) (abs_nonneg _)
      _ = (∑ k, |x k|)*M := by rw [Finset.sum_mul]
      _ ≤ X*M := mul_le_mul_of_nonneg_right hX hM
  calc
    |neutralNF626Dot x (fun k => Y k j) - z j| ≤
        |neutralNF626Dot x (fun k => Y k j)| + |z j| := by
      simpa only [sub_eq_add_neg, abs_neg] using
        abs_add_le (neutralNF626Dot x (fun k => Y k j)) (-z j)
    _ ≤ X*M+Z := add_le_add hd (hZ j)
    _ < B := hB

theorem neutralNF683PackedProducts {m n : ℕ}
    (x : Fin m → ℤ) (Y : Fin m → Fin n → ℤ) (z : Fin n → ℤ)
    (X M Z B : ℤ) (hpos : 0 < B)
    (hX : ∑ k, |x k| ≤ X) (hM : 0 ≤ M)
    (hY : ∀ k j, |Y k j| ≤ M) (hZ : ∀ j, |z j| ≤ Z)
    (hB : X*M+Z < B)
    (hpack : neutralNF626Dot x (fun k => neutralNF683Pack B (Y k)) =
      neutralNF683Pack B z) :
    ∀ j, neutralNF626Dot x (fun k => Y k j) = z j := by
  apply neutralNF683Pack_injective_bounded B hpos
  · exact neutralNF683Dot_error_bound x Y z X M Z B hX hM hY hZ hB
  · rw [neutralNF683Pack_dot]
    exact hpack

#print axioms neutralNF683Pack_succ
#print axioms neutralNF683Pack_zero_small
#print axioms neutralNF683Pack_injective_bounded
#print axioms neutralNF683Pack_dot
#print axioms neutralNF683Dot_error_bound
#print axioms neutralNF683PackedProducts

end WeilDefect
