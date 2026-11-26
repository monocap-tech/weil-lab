import WeilDefect.MasterRecon.V10B1

/-! V10B2: compose unit-interval evaluation into a rectangle bound,
then sum arbitrary finite weighted cell families. Outer integrability
of the cell energies is explicit; the actual Mellin slices and global
weighted integrals are attached in later gates. -/
namespace WeilDefect.MasterRecon.V10B2

open Set MeasureTheory
open scoped Interval BigOperators

noncomputable def rowEnergy (H Y : ℝ → ℝ → ℂ) (b x : ℝ) : ℝ :=
  ∫ y in b..b+1, (‖H x y‖ ^ 2 + ‖Y x y‖ ^ 2)

noncomputable def rectangleEnergy (H X Y Z : ℝ → ℝ → ℂ) (a b : ℝ) : ℝ :=
  ∫ x in a..a+1, (rowEnergy H Y b x + rowEnergy X Z b x)

/-- Apply the x-evaluation inequality first and the y-evaluation
inequalities to both resulting slices. No Fubini interchange is
assumed in this receiver. -/
theorem rectangle_eval_of_slices
    (H X Y Z : ℝ → ℝ → ℂ) (a b p q : ℝ)
    (hp : p ∈ Icc a (a+1)) (hq : q ∈ Icc b (b+1))
    (hx : ‖H p q‖ ^ 2 ≤
      2 * ∫ x in a..a+1, (‖H x q‖ ^ 2 + ‖X x q‖ ^ 2))
    (hy : ∀ x ∈ Icc a (a+1),
      ‖H x q‖ ^ 2 ≤ 2 * rowEnergy H Y b x)
    (hxy : ∀ x ∈ Icc a (a+1),
      ‖X x q‖ ^ 2 ≤ 2 * rowEnergy X Z b x)
    (hleft : IntervalIntegrable
      (fun x => ‖H x q‖ ^ 2 + ‖X x q‖ ^ 2) volume a (a+1))
    (hright : IntervalIntegrable
      (fun x => rowEnergy H Y b x + rowEnergy X Z b x) volume a (a+1)) :
    ‖H p q‖ ^ 2 ≤ 4 * rectangleEnergy H X Y Z a b := by
  have hm := intervalIntegral.integral_mono_on
    (by linarith : a ≤ a+1) hleft (hright.const_mul 2)
    (fun x hx' => show ‖H x q‖ ^ 2 + ‖X x q‖ ^ 2 ≤
      2 * (rowEnergy H Y b x + rowEnergy X Z b x) from
      by linarith [hy x hx', hxy x hx'])
  rw [intervalIntegral.integral_const_mul] at hm
  unfold rectangleEnergy
  linarith

/-- Actual differentiable slices discharge the three evaluation
inequalities using V10B1. Outer interval integrability is still
stated separately, to be discharged by joint continuity. -/
theorem rectangle_eval
    (H X Y Z : ℝ → ℝ → ℂ) (a b p q : ℝ)
    (hp : p ∈ Icc a (a+1)) (hq : q ∈ Icc b (b+1))
    (hcH : Continuous (fun x => H x q))
    (hcX : Continuous (fun x => X x q))
    (hxr : ∀ x, HasDerivAt (fun u => (H u q).re) (X x q).re x)
    (hxi : ∀ x, HasDerivAt (fun u => (H u q).im) (X x q).im x)
    (hcyH : ∀ x, Continuous (H x))
    (hcyX : ∀ x, Continuous (X x))
    (hcyY : ∀ x, Continuous (Y x))
    (hcyZ : ∀ x, Continuous (Z x))
    (hyr : ∀ x y, HasDerivAt (fun v => (H x v).re) (Y x y).re y)
    (hyi : ∀ x y, HasDerivAt (fun v => (H x v).im) (Y x y).im y)
    (hzr : ∀ x y, HasDerivAt (fun v => (X x v).re) (Z x y).re y)
    (hzi : ∀ x y, HasDerivAt (fun v => (X x v).im) (Z x y).im y)
    (houter : IntervalIntegrable
      (fun x => rowEnergy H Y b x + rowEnergy X Z b x) volume a (a+1)) :
    ‖H p q‖ ^ 2 ≤ 4 * rectangleEnergy H X Y Z a b := by
  apply rectangle_eval_of_slices H X Y Z a b p q hp hq
  · exact V10B1.unit_eval_complex _ _ hcH hcX hxr hxi a p hp
  · intro x _
    exact V10B1.unit_eval_complex _ _ (hcyH x) (hcyY x) (hyr x) (hyi x) b q hq
  · intro x _
    exact V10B1.unit_eval_complex _ _ (hcyX x) (hcyZ x) (hzr x) (hzi x) b q hq
  · exact ((hcH.norm.pow 2).add (hcX.norm.pow 2)).intervalIntegrable a (a+1)
  · exact houter

theorem rectangle_energy_nonnegative (H X Y Z : ℝ → ℝ → ℂ) (a b : ℝ) :
    0 ≤ rectangleEnergy H X Y Z a b := by
  unfold rectangleEnergy
  apply intervalIntegral.integral_nonneg (by linarith)
  intro x _
  unfold rowEnergy
  apply add_nonneg <;> apply intervalIntegral.integral_nonneg (by linarith) <;>
    intro y _ <;> positivity

/-- The cell weights may include repeated samples through multiplicity;
the point set need not have a minimum spacing. -/
theorem finite_weighted_cell {ι : Type*} (S : Finset ι)
    (m v : ι → ℝ) (E C : ℝ)
    (hm : ∀ i ∈ S, 0 ≤ m i)
    (hv : ∀ i ∈ S, v i ≤ 4 * E)
    (hE : 0 ≤ E)
    (hcount : ∑ i ∈ S, m i ≤ C) :
    ∑ i ∈ S, m i * v i ≤ 4 * C * E := by
  calc
    (∑ i ∈ S, m i * v i) ≤ ∑ i ∈ S, m i * (4 * E) :=
      Finset.sum_le_sum (fun i hi => mul_le_mul_of_nonneg_left (hv i hi) (hm i hi))
    _ = (∑ i ∈ S, m i) * (4 * E) := by rw [Finset.sum_mul]
    _ ≤ C * (4 * E) := mul_le_mul_of_nonneg_right hcount (by positivity)
    _ = 4 * C * E := by ring

theorem finite_weighted_rectangles {ι κ : Type*}
    (J : Finset κ) (S : κ → Finset ι)
    (m v : ι → ℝ) (E C : κ → ℝ)
    (hm : ∀ j ∈ J, ∀ i ∈ S j, 0 ≤ m i)
    (hv : ∀ j ∈ J, ∀ i ∈ S j, v i ≤ 4 * E j)
    (hE : ∀ j ∈ J, 0 ≤ E j)
    (hcount : ∀ j ∈ J, ∑ i ∈ S j, m i ≤ C j) :
    ∑ j ∈ J, ∑ i ∈ S j, m i * v i ≤ 4 * ∑ j ∈ J, C j * E j := by
  calc
    (∑ j ∈ J, ∑ i ∈ S j, m i * v i) ≤ ∑ j ∈ J, 4 * C j * E j :=
      Finset.sum_le_sum (fun j hj =>
        finite_weighted_cell (S j) m v (E j) (C j) (hm j hj) (hv j hj)
          (hE j hj) (hcount j hj))
    _ = 4 * ∑ j ∈ J, C j * E j := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _
      ring

end WeilDefect.MasterRecon.V10B2

#print axioms WeilDefect.MasterRecon.V10B2.rectangle_eval_of_slices
#print axioms WeilDefect.MasterRecon.V10B2.rectangle_eval
#print axioms WeilDefect.MasterRecon.V10B2.rectangle_energy_nonnegative
#print axioms WeilDefect.MasterRecon.V10B2.finite_weighted_cell
#print axioms WeilDefect.MasterRecon.V10B2.finite_weighted_rectangles
