import WeilDefect.MasterRecon.V08I

/-! V10B3a: logarithmic weight algebra for the rectangle sampling
and weighted convolution arguments. The analytic Young inequality
and actual Fourier multiplier attachment remain separate. -/
namespace WeilDefect.MasterRecon.V10B3a

noncomputable def weight (y : ℝ) : ℝ := Real.log (2 + |y|)

theorem weight_lower (y : ℝ) : Real.log 2 ≤ weight y := by
  unfold weight
  apply Real.log_le_log (by norm_num)
  linarith [abs_nonneg y]

theorem weight_pos (y : ℝ) : 0 < weight y :=
  (Real.log_pos (by norm_num : (1 : ℝ) < 2)).trans_le (weight_lower y)

theorem weight_cycles (u : ℝ) :
    weight (2 * Real.pi * u) = V08I.logWeight u := rfl

theorem weight_subadditive (u v : ℝ) :
    weight (u + v) ≤ weight u + weight v := by
  unfold weight
  have hu : 0 < 2 + |u| := by positivity
  have hv : 0 < 2 + |v| := by positivity
  rw [← Real.log_mul hu.ne' hv.ne']
  apply Real.log_le_log (by positivity)
  have h := abs_add_le u v
  nlinarith [mul_nonneg (abs_nonneg u) (abs_nonneg v), abs_nonneg u, abs_nonneg v]

theorem weight_product (u v : ℝ) :
    weight (u + v) ≤ (2 / Real.log 2) * weight u * weight v := by
  have hl : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hu := weight_lower u
  have hv := weight_lower v
  have h1 := mul_le_mul_of_nonneg_right hu (weight_pos v).le
  have h2 := mul_le_mul_of_nonneg_left hv (weight_pos u).le
  have hsum : Real.log 2 * (weight u + weight v) ≤ 2 * weight u * weight v := by
    nlinarith only [h1, h2]
  calc
    weight (u + v) ≤ weight u + weight v := weight_subadditive u v
    _ ≤ (2 / Real.log 2) * weight u * weight v := by
      have hh : weight u + weight v ≤ (2 * weight u * weight v) / Real.log 2 :=
        (le_div_iff₀ hl).2 (by simpa [mul_comm] using hsum)
      calc
        weight u + weight v ≤ (2 * weight u * weight v) / Real.log 2 := hh
        _ = (2 / Real.log 2) * weight u * weight v := by ring

/-- The local counting weight is controlled everywhere in the
corresponding closed unit cell, including endpoints. -/
theorem cell_weight (n y : ℝ) (hy : n ≤ y) (hy' : y ≤ n + 1) :
    Real.log (|n| + 3) ≤ 2 * weight y := by
  have hd : |n - y| ≤ 1 := abs_le.mpr ⟨by linarith, by linarith⟩
  have hn : |n| ≤ |y| + 1 := by
    calc
      |n| = |(n-y)+y| := by congr 1 <;> ring
      _ ≤ |n-y| + |y| := abs_add_le _ _
      _ ≤ |y| + 1 := by linarith
  unfold weight
  rw [← Real.log_pow (2 + |y|) 2]
  apply Real.log_le_log (by positivity)
  nlinarith [sq_nonneg |y|, abs_nonneg y]

end WeilDefect.MasterRecon.V10B3a

#print axioms WeilDefect.MasterRecon.V10B3a.weight_lower
#print axioms WeilDefect.MasterRecon.V10B3a.weight_pos
#print axioms WeilDefect.MasterRecon.V10B3a.weight_cycles
#print axioms WeilDefect.MasterRecon.V10B3a.weight_subadditive
#print axioms WeilDefect.MasterRecon.V10B3a.weight_product
#print axioms WeilDefect.MasterRecon.V10B3a.cell_weight
