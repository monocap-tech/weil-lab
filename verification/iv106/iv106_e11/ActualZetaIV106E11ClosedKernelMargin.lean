import WeilDefect.Arithmetic.ActualZetaIV106E10IntegratedCoercivity

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped InnerProduct

/-- Preserve the strict physical mass reserve through the actual constrained
density theorem, with no additional smooth-core hypothesis. -/
theorem neutralIV106E11Closed_mass (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0) :
    (5003/5000:ℝ)*‖neutralLogPhysical q.val‖^2 ≤
      (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  let S : Set (NeutralLogHilbertCarrier (11/10:ℝ)) :=
    {x | (5003/5000:ℝ)*‖neutralLogPhysical x.val‖^2 ≤
      (inner ℂ x (neutralActualZetaLogWeilFormOperator (11/10) x)).re}
  have hleft : Continuous (fun x : NeutralLogHilbertCarrier (11/10:ℝ) =>
      (5003/5000:ℝ)*‖neutralLogPhysical x.val‖^2) :=
    continuous_const.mul (((neutralLogPhysical.continuous.comp continuous_subtype_val).norm).pow 2)
  have hright : Continuous (fun x : NeutralLogHilbertCarrier (11/10:ℝ) =>
      (inner ℂ x (neutralActualZetaLogWeilFormOperator (11/10) x)).re) :=
    Complex.continuous_re.comp
      (continuous_id.inner (neutralActualZetaLogWeilFormOperator (11/10)).continuous)
  have hc : IsClosed S := isClosed_le hleft hright
  have hs : (neutralIV106C3Core (11/10:ℝ) : Set (NeutralLogHilbertCarrier (11/10:ℝ))) ∩
      {x | neutralIV106C3Constraints 665 k hk x = 0} ⊆ S := by
    intro x hx
    exact neutralIV106E10Core_margin k hk x hx.2 hx.1
  have h := closure_minimal hs hc
  rw [neutralIV106C3Actual_kernel_closure 665 k hk] at h
  exact h hq

/-- Sharp scalar combination of the physical mass margin and Gårding
estimate. The reserve is not rounded down to one. -/
theorem neutralIV106E11Scalar (c D M E L : ℝ)
    (hc : 0 < c) (hD : 0 ≤ D) (hm : c*M ≤ E) (hL : L ≤ E+D*M) :
    c/(c+D)*L ≤ E := by
  have hd : 0 < c+D := add_pos_of_pos_of_nonneg hc hD
  have h1 := mul_le_mul_of_nonneg_left hL hc.le
  have h2 := mul_le_mul_of_nonneg_left hm hD
  rw [div_mul_eq_mul_div]
  apply (div_le_iff₀ hd).mpr
  nlinarith only [h1,h2]

def neutralIV106E11Alpha : ℝ :=
  (5003/5000:ℝ)/((5003/5000:ℝ)+neutralIV106C2Loss (11/10:ℝ))

theorem neutralIV106E11Alpha_pos : 0 < neutralIV106E11Alpha := by
  unfold neutralIV106E11Alpha
  exact div_pos (by norm_num) (add_pos_of_pos_of_nonneg (by norm_num)
    (neutralIV106C2Loss_nonneg _))

/-- Actual logarithmic form-norm coercivity on the entire closed kernel. -/
theorem neutralIV106E11Closed_log (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0) :
    neutralIV106E11Alpha*‖q‖^2 ≤
      (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  exact neutralIV106E11Scalar _ _ _ _ _ (by norm_num)
    (neutralIV106C2Loss_nonneg _)
    (neutralIV106E11Closed_mass k hk q hq)
    (neutralActualZetaLogWeilFormOperator_garding _ q)

/-- Nonzero vectors in the actual constrained kernel have strictly positive energy. -/
theorem neutralIV106E11Closed_strict (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0) (hn : q ≠ 0) :
    0 < (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  exact (mul_pos neutralIV106E11Alpha_pos (pow_pos (norm_pos_iff.mpr hn) 2)).trans_le
    (neutralIV106E11Closed_log k hk q hq)

#print axioms neutralIV106E11Closed_mass
#print axioms neutralIV106E11Scalar
#print axioms neutralIV106E11Alpha_pos
#print axioms neutralIV106E11Closed_log
#print axioms neutralIV106E11Closed_strict
end
end WeilDefect
