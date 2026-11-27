import Mathlib

namespace WeilDefect
noncomputable section
open Finset Matrix Equiv Filter
open scoped BigOperators Topology

/-- Ordered-tuple Cauchy–Binet, avoiding subset enumeration and sorting.
Repeated tuples contribute zero automatically. -/
theorem neutralIV106E18PExpansion {k N : ℕ}
    (A : Matrix (Fin k) (Fin N) ℝ) (B : Matrix (Fin N) (Fin k) ℝ) :
    (A*B).det = ∑ p : Fin k → Fin N,
      (A.submatrix id p).det * ∏ i, B (p i) i := by
  classical
  calc
    (A*B).det = ∑ p : Fin k → Fin N, ∑ σ : Equiv.Perm (Fin k),
        ((Equiv.Perm.sign σ : ℤ):ℝ) * ∏ i, A (σ i) (p i)*B (p i) i := by
      simp only [Matrix.det_apply',Matrix.mul_apply,prod_univ_sum,mul_sum,Fintype.piFinset_univ]
      rw [Finset.sum_comm]
    _ = _ := by
      apply Finset.sum_congr rfl
      intro p hp
      rw [Matrix.det_apply',Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro σ hσ
      rw [Finset.prod_mul_distrib]
      simp only [Matrix.submatrix_apply,id_eq]
      ring

/-- Averaging over tuple permutations replaces the second product by
its determinant. The exact multiplicity is the number of permutations. -/
theorem neutralIV106E18PTuple (k N : ℕ)
    (A : Matrix (Fin k) (Fin N) ℝ) (B : Matrix (Fin N) (Fin k) ℝ) :
    (Nat.factorial k:ℝ)*(A*B).det =
      ∑ p : Fin k → Fin N, (A.submatrix id p).det*(B.submatrix p id).det := by
  classical
  symm
  calc
    _ = ∑ σ : Equiv.Perm (Fin k), ∑ p : Fin k → Fin N,
        (A.submatrix id p).det *
          (((Equiv.Perm.sign σ : ℤ):ℝ)*∏ i, B (p (σ i)) i) := by
      simp_rw [Matrix.det_apply' (B.submatrix _ id),Finset.mul_sum,
        Matrix.submatrix_apply,id_eq]
      rw [Finset.sum_comm]
    _ = ∑ _σ : Equiv.Perm (Fin k), (A*B).det := by
      apply Finset.sum_congr rfl
      intro σ hσ
      rw [neutralIV106E18PExpansion]
      let e : (Fin k → Fin N) ≃ (Fin k → Fin N) :=
        { toFun := fun p => p ∘ σ
          invFun := fun p => p ∘ σ.symm
          left_inv := by intro p; funext i; simp
          right_inv := by intro p; funext i; simp }
      apply Fintype.sum_equiv e
      intro p
      have hdet : (A.submatrix id (e p)).det =
          ((Equiv.Perm.sign σ : ℤ):ℝ)*(A.submatrix id p).det := by
        change ((A.submatrix id p).submatrix id σ).det = _
        exact Matrix.det_permute' σ _
      rw [hdet]
      change _ * (_ * ∏ i, B (p (σ i)) i) =
        _ * (∏ i, B (p (σ i)) i)
      ring
    _ = _ := by simp [Finset.sum_const,nsmul_eq_mul,Fintype.card_perm]

/-- The orientation factor is given as a pair product. This avoids
requiring a separate parity formula for the reversing permutation. -/
def neutralIV106E18POrient (k : ℕ) : ℝ :=
  ∏ i : Fin k, ∏ _j ∈ Finset.Ioi i, (-1:ℝ)

theorem neutralIV106E18POrient_ne (k : ℕ) :
    neutralIV106E18POrient k ≠ 0 := by
  unfold neutralIV106E18POrient
  exact Finset.prod_ne_zero_iff.mpr fun i _ =>
    Finset.prod_ne_zero_iff.mpr fun j _ => by norm_num

/-- The product of the two oriented Vandermonde determinants has
nonnegative factors for every tuple, irrespective of its ordering. -/
theorem neutralIV106E18PPair (k : ℕ) (x y : Fin k → ℝ) :
    neutralIV106E18POrient k*(Matrix.vandermonde y).det*
      (Matrix.vandermonde x).det =
      ∏ i : Fin k, ∏ j ∈ Finset.Ioi i, (y i-y j)*(x j-x i) := by
  unfold neutralIV106E18POrient
  rw [Matrix.det_vandermonde,Matrix.det_vandermonde,
    ← Finset.prod_mul_distrib,← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i hi
  rw [← Finset.prod_mul_distrib,← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro j hj
  ring

def neutralIV106E18PMinor {k : ℕ} (W X Y : ℕ → ℝ) (p : Fin k → ℕ) : ℝ :=
  (∏ i, W (p i)) *
    (∏ i : Fin k, ∏ j ∈ Finset.Ioi i,
      (Y (p i)-Y (p j))*(X (p j)-X (p i)))

theorem neutralIV106E18PMinor_nonneg {k : ℕ} (W X Y : ℕ → ℝ)
    (hw : ∀ n, 0 ≤ W n) (hx : StrictMono X) (hy : StrictAnti Y)
    (p : Fin k → ℕ) : 0 ≤ neutralIV106E18PMinor W X Y p := by
  unfold neutralIV106E18PMinor
  apply mul_nonneg (Finset.prod_nonneg fun i _ => hw (p i))
  apply Finset.prod_nonneg
  intro i hi
  apply Finset.prod_nonneg
  intro j hj
  rcases le_total (p i) (p j) with h | h
  · exact mul_nonneg (sub_nonneg.mpr (hy.antitone h))
      (sub_nonneg.mpr (hx.monotone h))
  · exact mul_nonneg_of_nonpos_of_nonpos
      (sub_nonpos.mpr (hy.antitone h)) (sub_nonpos.mpr (hx.monotone h))

theorem neutralIV106E18PMinor_pos {k : ℕ} (W X Y : ℕ → ℝ)
    (hx : StrictMono X) (hy : StrictAnti Y)
    (p : Fin k → ℕ) (hp : StrictMono p) (hw : ∀ i, 0 < W (p i)) :
    0 < neutralIV106E18PMinor W X Y p := by
  unfold neutralIV106E18PMinor
  apply mul_pos (Finset.prod_pos fun i _ => hw i)
  apply Finset.prod_pos
  intro i hi
  apply Finset.prod_pos
  intro j hj
  have hij := hp (Finset.mem_Ioi.mp hj)
  exact mul_pos (sub_pos.mpr (hy hij)) (sub_pos.mpr (hx hij))

def neutralIV106E18PPartial (k N : ℕ) (W X Y : ℕ → ℝ) :
    Matrix (Fin k) (Fin k) ℝ :=
  fun i j => ∑ n ∈ Finset.range N, W n*Y n^i.val*X n^j.val

theorem neutralIV106E18PPartial_formula (k N : ℕ) (W X Y : ℕ → ℝ) :
    (Nat.factorial k:ℝ)*
      (neutralIV106E18POrient k*(neutralIV106E18PPartial k N W X Y).det) =
        ∑ p : Fin k → Fin N,
          neutralIV106E18PMinor W X Y (fun i => (p i).val) := by
  classical
  let A : Matrix (Fin k) (Fin N) ℝ := fun i n => Y n.val^i.val
  let B : Matrix (Fin N) (Fin k) ℝ := fun n j => W n.val*X n.val^j.val
  have he : A*B = neutralIV106E18PPartial k N W X Y := by
    ext i j
    rw [Matrix.mul_apply,neutralIV106E18PPartial,← Fin.sum_univ_eq_sum_range]
    apply Finset.sum_congr rfl
    intro n hn
    dsimp [A,B]
    ring
  have ht := neutralIV106E18PTuple k N A B
  rw [he] at ht
  rw [← mul_left_comm,ht,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro p hp
  have hA : A.submatrix id p =
      (Matrix.vandermonde (fun i => Y (p i).val))ᵀ := by
    ext i j
    rfl
  have hB : B.submatrix p id =
      Matrix.of (fun i j => W (p i).val*
        Matrix.vandermonde (fun i => X (p i).val) i j) := by
    ext i j
    rfl
  rw [hA,hB,Matrix.det_transpose,Matrix.det_mul_column]
  unfold neutralIV106E18PMinor
  rw [← neutralIV106E18PPair]
  ring

/-- One fixed strictly positive tuple survives in every larger truncation.
No cancellation and no determinant limit equal to zero can occur. -/
theorem neutralIV106E18PFixed_lower (k N : ℕ) (W X Y : ℕ → ℝ)
    (hw : ∀ n, 0 ≤ W n) (hx : StrictMono X) (hy : StrictAnti Y)
    (hN : k+1 ≤ N) :
    neutralIV106E18PMinor W X Y (fun i : Fin k => i.val+1) ≤
      (Nat.factorial k:ℝ)*
        (neutralIV106E18POrient k*(neutralIV106E18PPartial k N W X Y).det) := by
  classical
  rw [neutralIV106E18PPartial_formula]
  let p : Fin k → Fin N := fun i => ⟨i.val+1,by omega⟩
  exact Finset.single_le_sum
    (fun q _ => neutralIV106E18PMinor_nonneg W X Y hw hx hy
      (fun i => (q i).val)) (Finset.mem_univ p)

/-- Generic infinite opposite-order Vandermonde rank theorem.
Entrywise HasSum is the only convergence input. -/
theorem neutralIV106E18PInfinite (k : ℕ) (W X Y : ℕ → ℝ)
    (hw : ∀ n, 0 ≤ W n) (hwpos : ∀ n, 0 < n → 0 < W n)
    (hx : StrictMono X) (hy : StrictAnti Y)
    (A : Matrix (Fin k) (Fin k) ℝ)
    (hs : ∀ i j, HasSum (fun n : ℕ => W n*Y n^i.val*X n^j.val) (A i j)) :
    0 < neutralIV106E18POrient k*A.det := by
  let C := neutralIV106E18PMinor W X Y (fun i : Fin k => i.val+1)
  have hC : 0 < C := neutralIV106E18PMinor_pos W X Y hx hy _
    (fun i j hij => by omega) (fun i => hwpos _ (by omega))
  have ht : Tendsto (fun N => neutralIV106E18PPartial k N W X Y)
      atTop (𝓝 A) := by
    apply tendsto_pi_nhds.mpr
    intro i
    apply tendsto_pi_nhds.mpr
    intro j
    exact (hs i j).tendsto_sum_nat
  have hd : Tendsto (fun N => (neutralIV106E18PPartial k N W X Y).det)
      atTop (𝓝 A.det) := (continuous_id.matrix_det.continuousAt.tendsto).comp ht
  have hlim : Tendsto (fun N => (Nat.factorial k:ℝ)*
      (neutralIV106E18POrient k*(neutralIV106E18PPartial k N W X Y).det))
      atTop (𝓝 ((Nat.factorial k:ℝ)*(neutralIV106E18POrient k*A.det))) :=
    tendsto_const_nhds.mul (tendsto_const_nhds.mul hd)
  have hle : C ≤ (Nat.factorial k:ℝ)*(neutralIV106E18POrient k*A.det) :=
    le_of_tendsto hlim (eventually_atTop.mpr ⟨k+1,fun N hN =>
      neutralIV106E18PFixed_lower k N W X Y hw hx hy hN⟩)
  exact pos_of_mul_pos_right (hC.trans_le hle) (by positivity)

theorem neutralIV106E18PRank (k : ℕ) (W X Y : ℕ → ℝ)
    (hw : ∀ n, 0 ≤ W n) (hwpos : ∀ n, 0 < n → 0 < W n)
    (hx : StrictMono X) (hy : StrictAnti Y)
    (A : Matrix (Fin k) (Fin k) ℝ)
    (hs : ∀ i j, HasSum (fun n : ℕ => W n*Y n^i.val*X n^j.val) (A i j)) :
    A.det ≠ 0 := by
  intro hz
  have hh := neutralIV106E18PInfinite k W X Y hw hwpos hx hy A hs
  rw [hz,mul_zero] at hh
  exact (lt_irrefl 0) hh

#print axioms neutralIV106E18PExpansion
#print axioms neutralIV106E18PTuple
#print axioms neutralIV106E18POrient_ne
#print axioms neutralIV106E18PPair
#print axioms neutralIV106E18PMinor_nonneg
#print axioms neutralIV106E18PMinor_pos
#print axioms neutralIV106E18PPartial_formula
#print axioms neutralIV106E18PFixed_lower
#print axioms neutralIV106E18PInfinite
#print axioms neutralIV106E18PRank
end
end WeilDefect
