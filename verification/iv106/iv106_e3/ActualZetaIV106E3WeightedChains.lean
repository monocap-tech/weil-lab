import Mathlib

namespace WeilDefect
noncomputable section
open scoped BigOperators

/-- Weighted two-variable inequality, without square roots or eigenvalue premises. -/
theorem neutralIV106E3Weighted_pair (u v x y : ℝ) (hx : 0 < x) (hy : 0 < y) :
    2*u*v ≤ (y/x)*u^2+(x/y)*v^2 := by
  have he : (y/x)*u^2+(x/y)*v^2 =
      ((y*u)^2+(x*v)^2)/(x*y) := by
    field_simp [hx.ne',hy.ne']
    <;> ring
  rw [he]
  apply (le_div_iff₀ (mul_pos hx hy)).mpr
  nlinarith only [sq_nonneg (y*u-x*v)]

/-- A positive weighted row bound controls the entire symmetric real quadratic form. -/
theorem neutralIV106E3Weighted_chain {ι : Type*} [Fintype ι]
    (A : ι → ι → ℝ) (w u : ι → ℝ) (L : ℝ)
    (hA : ∀ i j, 0 ≤ A i j) (hs : ∀ i j, A i j = A j i)
    (hw : ∀ i, 0 < w i)
    (hr : ∀ i, ∑ j, A i j*(w j/w i) ≤ L) :
    (∑ i, ∑ j, A i j*u i*u j) ≤ L*∑ i, u i^2 := by
  classical
  let B : ι → ι → ℝ := fun i j => A i j*(w j/w i)*u i^2
  have hp (i j : ι) : 2*(A i j*u i*u j) ≤ B i j+B j i := by
    have h := mul_le_mul_of_nonneg_left
      (neutralIV106E3Weighted_pair (u i) (u j) (w i) (w j) (hw i) (hw j)) (hA i j)
    dsimp [B]
    rw [← hs i j]
    nlinarith only [h]
  have hsum : (∑ i, ∑ j, 2*(A i j*u i*u j)) ≤
      ∑ i, ∑ j, (B i j+B j i) := by
    exact Finset.sum_le_sum (fun i _ => Finset.sum_le_sum (fun j _ => hp i j))
  have hswap : (∑ i, ∑ j, B j i) = ∑ i, ∑ j, B i j := by
    rw [Finset.sum_comm]
  simp only [← Finset.mul_sum, Finset.sum_add_distrib, hswap] at hsum
  have hrow (i : ι) : (∑ j, B i j) ≤ L*u i^2 := by
    dsimp [B]
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (hr i) (sq_nonneg _)
  have hrows : (∑ i, ∑ j, B i j) ≤ L*∑ i, u i^2 := by
    rw [Finset.mul_sum]
    exact Finset.sum_le_sum (fun i _ => hrow i)
  linarith only [hsum,hrows]

/-- Complex entries are controlled by their moduli with the same row constant. -/
theorem neutralIV106E3Complex_chain {ι : Type*} [Fintype ι]
    (A : ι → ι → ℝ) (w : ι → ℝ) (z : ι → ℂ) (L : ℝ)
    (hA : ∀ i j, 0 ≤ A i j) (hs : ∀ i j, A i j = A j i)
    (hw : ∀ i, 0 < w i)
    (hr : ∀ i, ∑ j, A i j*(w j/w i) ≤ L) :
    (∑ i, ∑ j, A i j*(star (z i)*z j).re) ≤ L*∑ i, ‖z i‖^2 := by
  have hp (i j : ι) : (star (z i)*z j).re ≤ ‖z i‖*‖z j‖ := by
    calc
      _ ≤ |(star (z i)*z j).re| := le_abs_self _
      _ ≤ ‖star (z i)*z j‖ := Complex.abs_re_le_norm _
      _ = _ := by rw [norm_mul, norm_star]
  calc
    _ ≤ ∑ i, ∑ j, A i j*‖z i‖*‖z j‖ := by
      apply Finset.sum_le_sum
      intro i hi
      apply Finset.sum_le_sum
      intro j hj
      rw [mul_assoc]
      exact mul_le_mul_of_nonneg_left (hp i j) (hA i j)
    _ ≤ _ := neutralIV106E3Weighted_chain A w (fun i => ‖z i‖) L hA hs hw hr

#print axioms neutralIV106E3Weighted_pair
#print axioms neutralIV106E3Weighted_chain
#print axioms neutralIV106E3Complex_chain
end
end WeilDefect
