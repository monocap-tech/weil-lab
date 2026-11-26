import WeilDefect.Arithmetic.ActualZetaIV123OriginalPoleReceiver
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap BigOperators ComplexConjugate

/-- Physical row budget on the actual signed packed Gram, with no
assumption of complementary positivity. -/
def neutralIV124PhysicalBudget (k : ℕ) (hk : 0 < k) : ℝ :=
  ∑ i : Fin k, (5/2:ℝ) *
    neutralIV109RowConstant (11/10:ℝ) (neutralIV100Carrier k hk i)^2 /
    neutralIV104Mass k hk i

theorem neutralIV124PhysicalBudget_nonneg (k : ℕ) (hk : 0 < k) :
    0 ≤ neutralIV124PhysicalBudget k hk := by
  unfold neutralIV124PhysicalBudget
  apply Finset.sum_nonneg
  intro i hi
  exact div_nonneg (mul_nonneg (by norm_num) (sq_nonneg _))
    (neutralIV100Carrier_mass_pos k hk i).le

theorem neutralIV124RowBudget_physical (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV108RowBudget k hk v ≤
      neutralIV124PhysicalBudget k hk * ‖v.toLp 2 volume‖^2 := by
  unfold neutralIV108RowBudget neutralIV124PhysicalBudget
  rw [Finset.sum_mul]
  apply Finset.sum_le_sum
  intro i hi
  have hu := neutralIV009OriginalCollars_supported_window _
    (neutralIV100Carrier_collars k hk i)
  have hb := neutralIV109Mixed_physical_bound (11/10:ℝ) (by norm_num)
    (neutralIV100Carrier k hk i) v hu hv
  change ‖neutralIV106CrossRHS k hk v i‖ ≤
    neutralIV109RowConstant (11/10:ℝ) (neutralIV100Carrier k hk i) *
      ‖v.toLp 2 volume‖ at hb
  have hs := pow_le_pow_left₀ (norm_nonneg _) hb 2
  calc
    _ ≤ (5/2:ℝ) *
        (neutralIV109RowConstant (11/10:ℝ) (neutralIV100Carrier k hk i) *
          ‖v.toLp 2 volume‖)^2 / neutralIV104Mass k hk i :=
      div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left hs (by norm_num))
        (neutralIV100Carrier_mass_pos k hk i).le
    _ = _ := by ring

/-- Gårding comparison after exact packed Schur elimination. -/
theorem neutralIV124Schur_garding (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    ‖neutralIV102Lift (11/10:ℝ) v hv‖^2 ≤
      neutralIV107SchurEnergy k hk v +
      (neutralActualZetaNativeLogError (11/10:ℝ) +
       neutralPhysicalPoleEnergyConstant (11/10:ℝ) +
       neutralIV124PhysicalBudget k hk) * ‖v.toLp 2 volume‖^2 := by
  have hq := neutralIV109Original_garding (11/10:ℝ) (by norm_num) v hv
  have hr := le_trans (neutralIV108Response_le_rowBudget k hk v)
    (neutralIV124RowBudget_physical k hk v hv)
  unfold neutralIV107SchurEnergy
  linarith only [hq, hr]

/-- Receiver for a proved logarithmic lower weight on the constrained tail.
The leakage bound is deliberately explicit, not assumed for all residuals. -/
theorem neutralIV124Schur_tail_of_log_lower (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (L eta : ℝ)
    (hlog : L * ‖v.toLp 2 volume‖^2 ≤
      ‖neutralIV102Lift (11/10:ℝ) v hv‖^2)
    (hmargin : eta ≤ L - (neutralActualZetaNativeLogError (11/10:ℝ) +
      neutralPhysicalPoleEnergyConstant (11/10:ℝ) +
      neutralIV124PhysicalBudget k hk)) :
    eta * ‖v.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk v := by
  have h := neutralIV124Schur_garding k hk v hv
  have hm := mul_le_mul_of_nonneg_right hmargin
    (sq_nonneg ‖v.toLp 2 volume‖)
  linarith only [hlog, h, hm]

/-- Scalar convex combination for retaining logarithmic frequency growth.
All coefficients and the exact convex-weight condition are explicit. -/
theorem neutralIV124Weighted_lower (S J m M eta theta : ℝ)
    (hS : J - M*m ≤ S) (hTail : eta*m ≤ S)
    (h0 : 0 ≤ theta) (h1 : theta ≤ 1) :
    theta*J + ((1-theta)*eta-theta*M)*m ≤ S := by
  have hA := mul_le_mul_of_nonneg_left hS h0
  have hB := mul_le_mul_of_nonneg_left hTail (sub_nonneg.mpr h1)
  linarith only [hA, hB]

#print axioms neutralIV124PhysicalBudget_nonneg
#print axioms neutralIV124RowBudget_physical
#print axioms neutralIV124Schur_garding
#print axioms neutralIV124Schur_tail_of_log_lower
#print axioms neutralIV124Weighted_lower

end
end WeilDefect
