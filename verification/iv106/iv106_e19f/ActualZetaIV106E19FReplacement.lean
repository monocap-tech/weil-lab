import WeilDefect.Arithmetic.ActualZetaIV106E18PDeterminantTransfer

namespace WeilDefect
noncomputable section
open Finset Matrix
open scoped BigOperators

/-- Replacing a column by an exact column combination does not require
invertibility. This is important for repeated tuples in Cauchy-Binet. -/
theorem neutralIV106E19FTuple_replace {k : ℕ}
    (V : Matrix (Fin k) (Fin k) ℝ) (j : Fin k)
    (b c : Fin k → ℝ)
    (h : ∀ i, b i = ∑ l, c l * V i l) :
    (V.updateCol j b).det = c j * V.det := by
  have he : b = fun i => ∑ l, c l • V i l := by
    funext i
    simpa only [smul_eq_mul] using h i
  rw [he, Matrix.det_updateCol_sum, smul_eq_mul]

/-- Column replacement commutes with the left rectangular factor. -/
theorem neutralIV106E19FUpdate_mul {k N : ℕ}
    (U : Matrix (Fin k) (Fin N) ℝ)
    (V : Matrix (Fin N) (Fin k) ℝ)
    (j : Fin k) (b : Fin N → ℝ) :
    (U*V).updateCol j (fun i => ∑ n, U i n*b n) =
      U*(V.updateCol j b) := by
  classical
  ext i l
  by_cases hl : l = j
  · subst l
    simp [Matrix.mul_apply, Matrix.updateCol_apply]
  · simp [Matrix.mul_apply, Matrix.updateCol_apply, hl]

/-- The actual ordered-tuple Cauchy-Binet numerator, including repeated
tuples, is a weighted sum of tuple interpolation coefficients. No
determinant division occurs in the proof. -/
theorem neutralIV106E19FNumerator {k N : ℕ}
    (U : Matrix (Fin k) (Fin N) ℝ)
    (V : Matrix (Fin N) (Fin k) ℝ)
    (j : Fin k) (b : Fin N → ℝ)
    (c : (Fin k → Fin N) → Fin k → ℝ)
    (h : ∀ (p : Fin k → Fin N) i, b (p i) =
      ∑ l, c p l * V (p i) l) :
    (Nat.factorial k:ℝ) *
      ((U*V).updateCol j (fun i => ∑ n, U i n*b n)).det =
      ∑ p : Fin k → Fin N,
        c p j*(U.submatrix id p).det*(V.submatrix p id).det := by
  classical
  rw [neutralIV106E19FUpdate_mul, neutralIV106E18PTuple]
  apply Finset.sum_congr rfl
  intro p hp
  have he : (V.updateCol j b).submatrix p id =
      (V.submatrix p id).updateCol j (fun i => b (p i)) := by
    ext i l
    by_cases hl : l=j <;> simp [Matrix.submatrix_apply,Matrix.updateCol_apply,hl]
  rw [he, neutralIV106E19FTuple_replace _ j _ (c p) (fun i => by
    simpa only [Matrix.submatrix_apply,id_eq] using h p i)]
  ring

#print axioms neutralIV106E19FTuple_replace
#print axioms neutralIV106E19FUpdate_mul
#print axioms neutralIV106E19FNumerator
end
end WeilDefect
