import WeilDefect.Arithmetic.ActualZetaIV106E19GOrientedBounds
import Mathlib.LinearAlgebra.Matrix.Adjugate

namespace WeilDefect
noncomputable section
open Finset Matrix Filter
open scoped BigOperators Topology

def neutralIV106E19HPreviousPartial (k N : ℕ) (W X Y : ℕ → ℝ) :
    Fin k → ℝ :=
  fun i => ∑ n ∈ Finset.range N, W n*Y n^i.val/X n

/-- Specialize the finite Cramer bound to the actual opposite-order
Vandermonde factors. No separation bound between nodes is required. -/
theorem neutralIV106E19HPartial_bounds (k N : ℕ) (W X Y : ℕ → ℝ)
    (hw : ∀ n, 0 ≤ W n) (hx : StrictMono X) (hy : StrictAnti Y)
    (hx1 : ∀ n, 1 ≤ X n) (j : Fin k) :
    let A := neutralIV106E18PPartial k N W X Y
    let b := neutralIV106E19HPreviousPartial k N W X Y
    let C := (Nat.factorial k:ℝ)*neutralIV106E18POrient k*((-1:ℝ)^j.val)*
      (A.updateCol j b).det
    let D := (Nat.factorial k:ℝ)*neutralIV106E18POrient k*A.det
    0 ≤ C ∧ C ≤ (Nat.choose k (j.val+1):ℝ)*D := by
  classical
  let U : Matrix (Fin k) (Fin N) ℝ := fun i n => Y n.val^i.val
  let V : Matrix (Fin N) (Fin k) ℝ := fun n l => W n.val*X n.val^l.val
  have hA : U*V = neutralIV106E18PPartial k N W X Y := by
    ext i l
    rw [Matrix.mul_apply,neutralIV106E18PPartial,← Fin.sum_univ_eq_sum_range]
    apply Finset.sum_congr rfl
    intro n hn
    dsimp [U,V]
    ring
  have hb : (fun i : Fin k => ∑ n : Fin N, U i n*(W n.val/X n.val)) =
      neutralIV106E19HPreviousPartial k N W X Y := by
    funext i
    unfold neutralIV106E19HPreviousPartial
    rw [← Fin.sum_univ_eq_sum_range]
    apply Finset.sum_congr rfl
    intro n hn
    dsimp [U]
    ring
  have ho (p : Fin k → Fin N) :
      0 ≤ neutralIV106E18POrient k*(U.submatrix id p).det*(V.submatrix p id).det := by
    have hu : U.submatrix id p =
        (Matrix.vandermonde (fun i => Y (p i).val))ᵀ := by
      ext i l
      rfl
    have hv : V.submatrix p id =
        Matrix.of (fun i l => W (p i).val*
          Matrix.vandermonde (fun i => X (p i).val) i l) := by
      ext i l
      rfl
    rw [hu,hv,Matrix.det_transpose,Matrix.det_mul_column]
    have he : neutralIV106E18POrient k*(Matrix.vandermonde (fun i => Y (p i).val)).det*
        ((∏ i, W (p i).val)*(Matrix.vandermonde (fun i => X (p i).val)).det) =
        neutralIV106E18PMinor W X Y (fun i => (p i).val) := by
      unfold neutralIV106E18PMinor
      rw [← neutralIV106E18PPair]
      ring
    rw [he]
    exact neutralIV106E18PMinor_nonneg W X Y hw hx hy _
  have h := neutralIV106E19GFinite_bounds U (fun n => W n.val) (fun n => X n.val)
    (fun n => hx1 n.val) (neutralIV106E18POrient k) (fun p => ho p) j
  change 0 ≤ (Nat.factorial k:ℝ)*neutralIV106E18POrient k*((-1:ℝ)^j.val)*
      ((U*V).updateCol j (fun i => ∑ n : Fin N, U i n*(W n.val/X n.val))).det ∧
    (Nat.factorial k:ℝ)*neutralIV106E18POrient k*((-1:ℝ)^j.val)*
      ((U*V).updateCol j (fun i => ∑ n : Fin N, U i n*(W n.val/X n.val))).det ≤
      (Nat.choose k (j.val+1):ℝ)*((Nat.factorial k:ℝ)*neutralIV106E18POrient k*(U*V).det) at h
  rw [hA,hb] at h
  exact h

/-- Continuity of column replacement, expressed entrywise to avoid a
separate analytic premise on the Cramer map. -/
theorem neutralIV106E19HUpdate_limit {k : ℕ}
    (A : ℕ → Matrix (Fin k) (Fin k) ℝ) (b : ℕ → Fin k → ℝ)
    (M : Matrix (Fin k) (Fin k) ℝ) (v : Fin k → ℝ)
    (hA : Tendsto A atTop (𝓝 M)) (hb : Tendsto b atTop (𝓝 v)) (j : Fin k) :
    Tendsto (fun N => (A N).updateCol j (b N)) atTop (𝓝 (M.updateCol j v)) := by
  classical
  apply tendsto_pi_nhds.mpr
  intro i
  apply tendsto_pi_nhds.mpr
  intro l
  by_cases hl : l=j
  · subst l
    simpa [Matrix.updateCol_apply] using (tendsto_pi_nhds.mp hb i)
  · simpa [Matrix.updateCol_apply,hl] using
      (tendsto_pi_nhds.mp (tendsto_pi_nhds.mp hA i) l)

/-- Infinite coefficient reserve from the same finite numerator
enclosure. The denominator is proved strictly oriented by E18P. -/
theorem neutralIV106E19HInfinite_bounds (k : ℕ) (W X Y : ℕ → ℝ)
    (hw : ∀ n, 0 ≤ W n) (hwpos : ∀ n, 0 < n → 0 < W n)
    (hx : StrictMono X) (hy : StrictAnti Y) (hx1 : ∀ n, 1 ≤ X n)
    (A : Matrix (Fin k) (Fin k) ℝ) (b : Fin k → ℝ)
    (hs : ∀ i j, HasSum (fun n : ℕ => W n*Y n^i.val*X n^j.val) (A i j))
    (ht : ∀ i, HasSum (fun n : ℕ => W n*Y n^i.val/X n) (b i))
    (j : Fin k) :
    0 ≤ (-1:ℝ)^j.val*((A.updateCol j b).det/A.det) ∧
      (-1:ℝ)^j.val*((A.updateCol j b).det/A.det) ≤ (Nat.choose k (j.val+1):ℝ) := by
  have hA : Tendsto (fun N => neutralIV106E18PPartial k N W X Y)
      atTop (𝓝 A) := by
    apply tendsto_pi_nhds.mpr
    intro i
    apply tendsto_pi_nhds.mpr
    intro l
    exact (hs i l).tendsto_sum_nat
  have hb : Tendsto (fun N => neutralIV106E19HPreviousPartial k N W X Y)
      atTop (𝓝 b) := by
    apply tendsto_pi_nhds.mpr
    intro i
    exact (ht i).tendsto_sum_nat
  let o := (Nat.factorial k:ℝ)*neutralIV106E18POrient k
  have hpos : 0 < o*A.det := by
    dsimp [o]
    rw [mul_assoc]
    exact mul_pos (by positivity) (neutralIV106E18PInfinite k W X Y hw hwpos hx hy A hs)
  have hd := (continuous_id.matrix_det.continuousAt.tendsto).comp hA
  have hc := (continuous_id.matrix_det.continuousAt.tendsto).comp
    (neutralIV106E19HUpdate_limit _ _ A b hA hb j)
  have hr := neutralIV106E19ERatio_limit _ _ (o*A.det)
    (o*((-1:ℝ)^j.val)*(A.updateCol j b).det) (Nat.choose k (j.val+1):ℝ)
    (tendsto_const_nhds.mul hd) (tendsto_const_nhds.mul hc) hpos
    (Filter.Eventually.of_forall (fun N => neutralIV106E19HPartial_bounds k N W X Y hw hx hy hx1 j))
  have ho : o ≠ 0 := fun hz => by rw [hz,zero_mul] at hpos; exact (lt_irrefl 0) hpos
  have ha : A.det ≠ 0 := fun hz => by rw [hz,mul_zero] at hpos; exact (lt_irrefl 0) hpos
  have he : o*((-1:ℝ)^j.val)*(A.updateCol j b).det/(o*A.det) =
      (-1:ℝ)^j.val*((A.updateCol j b).det/A.det) := by
    field_simp [ho,ha] <;> ring
  rwa [he] at hr

/-- The response equation is exact, by adjugate transport. The
coefficient definition does not request a numerical inverse. -/
theorem neutralIV106E19HSolve {k : ℕ} (A : Matrix (Fin k) (Fin k) ℝ)
    (b : Fin k → ℝ) (ha : A.det ≠ 0) :
    A *ᵥ (fun j => (A.updateCol j b).det/A.det) = b := by
  have he : (fun j => (A.updateCol j b).det/A.det) =
      A.det⁻¹ • Matrix.cramer A b := by
    funext j
    simp [Matrix.cramer_apply,div_eq_mul_inv,mul_comm]
  rw [he, Matrix.mulVec_smul, Matrix.mulVec_cramer, smul_smul, inv_mul_cancel₀ ha,one_smul]

#print axioms neutralIV106E19HPartial_bounds
#print axioms neutralIV106E19HUpdate_limit
#print axioms neutralIV106E19HInfinite_bounds
#print axioms neutralIV106E19HSolve
end
end WeilDefect
