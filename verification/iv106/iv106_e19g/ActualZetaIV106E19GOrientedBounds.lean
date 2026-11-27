import WeilDefect.Arithmetic.ActualZetaIV106E19GInterpolation
import WeilDefect.Arithmetic.ActualZetaIV106E19EShiftedPivot

namespace WeilDefect
noncomputable section
open Finset Matrix Filter
open scoped BigOperators Topology

/-- Finite signed numerator enclosure for the reciprocal response.
The positivity input is precisely the oriented tuple determinant product,
already supplied by the opposite-order Vandermonde mechanism. -/
theorem neutralIV106E19GFinite_bounds {k N : ℕ}
    (U : Matrix (Fin k) (Fin N) ℝ)
    (W X : Fin N → ℝ)
    (hx : ∀ n, 1 ≤ X n)
    (o : ℝ)
    (ho : ∀ p : Fin k → Fin N, 0 ≤
      o*(U.submatrix id p).det*
        ((Matrix.of fun n j => W n * X n^j.val :
          Matrix (Fin N) (Fin k) ℝ).submatrix p id).det)
    (j : Fin k) :
    let V : Matrix (Fin N) (Fin k) ℝ := fun n l => W n * X n^l.val
    let b : Fin N → ℝ := fun n => W n / X n
    let A := U*V
    let C := (Nat.factorial k:ℝ)*o*((-1:ℝ)^j.val)*
      (A.updateCol j (fun i => ∑ n, U i n*b n)).det
    let D := (Nat.factorial k:ℝ)*o*A.det
    0 ≤ C ∧ C ≤ (Nat.choose k (j.val+1):ℝ)*D := by
  classical
  dsimp only
  let V : Matrix (Fin N) (Fin k) ℝ := fun n l => W n * X n^l.val
  let b : Fin N → ℝ := fun n => W n/X n
  let c : (Fin k → Fin N) → Fin k → ℝ :=
    fun p => neutralIV106E19GCoeff (fun i => (X (p i))⁻¹)
  let w : (Fin k → Fin N) → ℝ :=
    fun p => o*(U.submatrix id p).det*(V.submatrix p id).det
  have hrep (p : Fin k → Fin N) (i : Fin k) :
      b (p i) = ∑ l, c p l*V (p i) l := by
    have h := neutralIV106E19GReciprocal (fun a => X (p a))
      (fun a => (lt_of_lt_of_le zero_lt_one (hx (p a))).ne') i
    have hh := congrArg (fun z : ℝ => W (p i)*z) h
    dsimp [b,c,V]
    rw [Finset.mul_sum] at hh
    convert hh using 1
    · ring
    · apply Finset.sum_congr rfl
      intro l hl
      ring
  have hn := neutralIV106E19FNumerator U V j b c hrep
  have hd := neutralIV106E18PTuple k N U V
  have hN : (Nat.factorial k:ℝ)*o*((-1:ℝ)^j.val)*
      ((U*V).updateCol j (fun i => ∑ n, U i n*b n)).det =
      ∑ p, w p*((-1:ℝ)^j.val*c p j) := by
    calc
      _ = o*((-1:ℝ)^j.val)*((Nat.factorial k:ℝ)*
          ((U*V).updateCol j (fun i => ∑ n, U i n*b n)).det) := by ring
      _ = _ := by
        rw [hn,Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro p hp
        dsimp [w]
        ring
  have hD : (Nat.factorial k:ℝ)*o*(U*V).det = ∑ p, w p := by
    calc
      _ = o*((Nat.factorial k:ℝ)*(U*V).det) := by ring
      _ = _ := by
        rw [hd,Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro p hp
        dsimp [w]
        ring
  have hc (p : Fin k → Fin N) :
      0 ≤ (-1:ℝ)^j.val*c p j ∧
      (-1:ℝ)^j.val*c p j ≤ (Nat.choose k (j.val+1):ℝ) := by
    apply neutralIV106E19GCoeff_bound
    intro i
    exact ⟨inv_nonneg.mpr (zero_le_one.trans (hx _)),inv_le_one_of_one_le₀ (hx _)⟩
  have hw (p : Fin k → Fin N) : 0 ≤ w p := ho p
  change 0 ≤ (Nat.factorial k:ℝ)*o*((-1:ℝ)^j.val)*
      ((U*V).updateCol j (fun i => ∑ n, U i n*b n)).det ∧
    (Nat.factorial k:ℝ)*o*((-1:ℝ)^j.val)*
      ((U*V).updateCol j (fun i => ∑ n, U i n*b n)).det ≤
    (Nat.choose k (j.val+1):ℝ)*((Nat.factorial k:ℝ)*o*(U*V).det)
  rw [hN,hD]
  exact neutralIV106E19EWeighted w (fun p => (-1:ℝ)^j.val*c p j) _ hw hc

#print axioms neutralIV106E19GFinite_bounds
end
end WeilDefect
