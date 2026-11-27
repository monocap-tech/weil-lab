import WeilDefect.MasterRecon.V10B30a

/-! The Basel midpoint error is a scalar multiple of the physical
trial Gram. The moment correction is defined relative to the literal
integral, so this algebra is independent of the scalar series proof. -/
namespace WeilDefect.MasterRecon.V10B31b

open scoped BigOperators
open V10B30a (moment block)

noncomputable def adjustedBlock (m n : ℕ) (a b : ℕ → ℝ) (δ : ℝ) : ℝ :=
  ∑ j ∈ Finset.range m, ∑ k ∈ Finset.range n,
    a j*b k*(moment 2 (j+k)-2*δ*moment 0 (j+k))

theorem adjusted_block (m n : ℕ) (a b : ℕ → ℝ) (δ : ℝ) :
    adjustedBlock m n a b δ = block m n 2 a b-2*δ*block m n 0 a b := by
  unfold adjustedBlock block
  rw [Finset.mul_sum,← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro j _
  rw [Finset.mul_sum,← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro k _
  ring

theorem residual_adjustment (m n : ℕ) (a b p q : ℕ → ℝ) (δ L : ℝ) :
    L*(block m m 0 a b-(block m n 1 a q+block m n 1 b p)/2+
        adjustedBlock n n p q δ/4) -
      L*(block m m 0 a b-(block m n 1 a q+block m n 1 b p)/2+
        block n n 2 p q/4) = -(δ/2)*(L*block n n 0 p q) := by
  rw [adjusted_block]
  ring

theorem adjustment_quadratic {ι : Type*} [Fintype ι]
    (N R R' : ι → ι → ℝ) (δ : ℝ)
    (h : ∀ i j, R' i j-R i j = -(δ/2)*N i j) (x : ι → ℝ) :
    (∑ i, ∑ j, x i*x j*R' i j) -
      (∑ i, ∑ j, x i*x j*R i j) =
        -(δ/2)*(∑ i, ∑ j, x i*x j*N i j) := by
  rw [← Finset.sum_sub_distrib,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [← Finset.sum_sub_distrib,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [← mul_sub,h i j]
  ring

theorem adjustment_bound {ι : Type*} [Fintype ι]
    (N R R' : ι → ι → ℝ) (δ ε T : ℝ)
    (h : ∀ i j, R' i j-R i j = -(δ/2)*N i j)
    (he : |δ| ≤ ε) (hT : 0 ≤ T) (x : ι → ℝ)
    (hN : 0 ≤ ∑ i, ∑ j, x i*x j*N i j)
    (hB : (∑ i, ∑ j, x i*x j*N i j) ≤ T*(∑ i, (x i)^2)) :
    |(∑ i, ∑ j, x i*x j*R' i j) -
      (∑ i, ∑ j, x i*x j*R i j)| ≤ ε*T*(∑ i, (x i)^2)/2 := by
  rw [adjustment_quadratic N R R' δ h x,abs_mul,abs_neg,abs_div,abs_of_nonneg hN,
    abs_of_pos (by norm_num : (0:ℝ)<2)]
  have he' : 0 ≤ ε := (abs_nonneg δ).trans he
  have hh : |δ|/2 ≤ ε/2 := div_le_div_of_nonneg_right he (by norm_num)
  calc
    _ ≤ (ε/2)*(T*(∑ i, (x i)^2)) :=
      mul_le_mul hh hB hN (by positivity)
    _ = _ := by ring

end WeilDefect.MasterRecon.V10B31b

#print axioms WeilDefect.MasterRecon.V10B31b.adjusted_block
#print axioms WeilDefect.MasterRecon.V10B31b.residual_adjustment
#print axioms WeilDefect.MasterRecon.V10B31b.adjustment_quadratic
#print axioms WeilDefect.MasterRecon.V10B31b.adjustment_bound
