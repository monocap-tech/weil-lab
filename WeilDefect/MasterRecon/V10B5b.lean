import WeilDefect.MasterRecon.V10B2
import WeilDefect.MasterRecon.V10B3a

/-! V10B5b: sum literal V10B2 rectangle energies over arbitrary finite
integer cells. Half-open cells avoid overlap; the angular weighted
slice bounds and outer integrability are explicit analytical inputs.
This module is independent of the unverified multiplier modules. -/
namespace WeilDefect.MasterRecon.V10B5b

open Set MeasureTheory
open scoped Interval BigOperators

def heightCell (n : ℤ) : Set ℝ := Ioc (n : ℝ) ((n : ℝ)+1)

theorem heightCell_unique (n m : ℤ) (y : ℝ)
    (hn : y ∈ heightCell n) (hm : y ∈ heightCell m) : n = m := by
  change (n : ℝ) < y ∧ y ≤ (n : ℝ)+1 at hn
  change (m : ℝ) < y ∧ y ≤ (m : ℝ)+1 at hm
  by_contra h
  rcases lt_or_gt_of_ne h with hlt | hgt
  · have hc : ((n+1 : ℤ) : ℝ) ≤ (m : ℝ) := by exact_mod_cast (show n+1 ≤ m by omega)
    push_cast at hc
    linarith [hn.2, hm.1]
  · have hc : ((m+1 : ℤ) : ℝ) ≤ (n : ℝ) := by exact_mod_cast (show m+1 ≤ n by omega)
    push_cast at hc
    linarith [hm.2, hn.1]

theorem finite_indicator_integral (J : Finset ℤ) (F : ℝ → ℝ)
    (hF : Integrable F) :
    Integrable (fun y => ∑ n ∈ J, (heightCell n).indicator F y) ∧
    (∫ y, ∑ n ∈ J, (heightCell n).indicator F y) =
      ∑ n ∈ J, ∫ y in heightCell n, F y := by
  classical
  induction J using Finset.induction_on with
  | empty => simp
  | @insert n J hn ih =>
    have hi : Integrable ((heightCell n).indicator F) :=
      hF.indicator measurableSet_Ioc
    simp only [Finset.sum_insert hn]
    refine ⟨hi.add ih.1, ?_⟩
    rw [integral_add hi ih.1, integral_indicator (show MeasurableSet (heightCell n) from measurableSet_Ioc), ih.2]

theorem finite_cell_integral (J : Finset ℤ) (F : ℝ → ℝ)
    (hF : Integrable F) (h0 : ∀ y, 0 ≤ F y) :
    (∑ n ∈ J, ∫ y in heightCell n, F y) ≤ ∫ y, F y := by
  classical
  obtain ⟨hi, he⟩ := finite_indicator_integral J F hF
  rw [← he]
  apply integral_mono hi hF
  intro y
  change (∑ n ∈ J, (heightCell n).indicator F y) ≤ F y
  by_cases h : ∃ n ∈ J, y ∈ heightCell n
  · obtain ⟨n, hn, hy⟩ := h
    rw [Finset.sum_eq_single n]
    · simp [Set.indicator_of_mem hy]
    · intro m hm hne
      exact Set.indicator_of_notMem (fun hym => hne (heightCell_unique m n y hym hy)) _
    · exact fun hnot => (hnot hn).elim
  · have hz : (∑ n ∈ J, (heightCell n).indicator F y) = 0 := by
      apply Finset.sum_eq_zero
      intro n hn
      exact Set.indicator_of_notMem (fun hy => h ⟨n,hn,hy⟩) _
    rw [hz]
    exact h0 y

theorem cell_energy_bound (F : ℝ → ℝ) (hF : Continuous F)
    (h0 : ∀ y, 0 ≤ F y) (n : ℤ) :
    Real.log (|(n : ℝ)|+3) * (∫ y in (n : ℝ)..(n : ℝ)+1, F y) ≤
      2 * ∫ y in heightCell n, V10B3a.weight y * F y := by
  let a : ℝ := n
  have ha : a ≤ a+1 := by linarith
  have hc : Continuous V10B3a.weight := by
    unfold V10B3a.weight
    apply Continuous.log (by fun_prop)
    intro y
    linarith [abs_nonneg y]
  have hl := hF.const_mul (Real.log (|a|+3))
  have hr := (hc.mul hF).const_mul 2
  have hm := intervalIntegral.integral_mono_on (μ := volume) ha
    (hl.intervalIntegrable a (a+1)) (hr.intervalIntegrable a (a+1))
    (fun y hy => by
      change Real.log (|a|+3) * F y ≤ 2 * (V10B3a.weight y * F y)
      have h := mul_le_mul_of_nonneg_right (V10B3a.cell_weight a y hy.1 hy.2) (h0 y)
      linarith only [h])
  change (∫ y in a..a+1, Real.log (|a|+3) * F y) ≤
    ∫ y in a..a+1, 2 * (V10B3a.weight y * F y) at hm
  rw [intervalIntegral.integral_const_mul, intervalIntegral.integral_const_mul] at hm
  rw [intervalIntegral.integral_of_le ha, intervalIntegral.integral_of_le ha] at hm
  change Real.log (|a|+3)*(∫ y in a..a+1, F y) ≤
    2*(∫ y in Ioc a (a+1), V10B3a.weight y*F y)
  rw [intervalIntegral.integral_of_le ha]
  exact hm

theorem finite_row_budget (J : Finset ℤ) (F : ℝ → ℝ)
    (hF : Continuous F) (h0 : ∀ y, 0 ≤ F y)
    (hi : Integrable (fun y => V10B3a.weight y * F y)) :
    (∑ n ∈ J, Real.log (|(n : ℝ)|+3) *
      (∫ y in (n : ℝ)..(n : ℝ)+1, F y)) ≤
      2 * ∫ y, V10B3a.weight y * F y := by
  calc
    _ ≤ ∑ n ∈ J, 2 * ∫ y in heightCell n, V10B3a.weight y * F y :=
      Finset.sum_le_sum (fun n _ => cell_energy_bound F hF h0 n)
    _ = 2 * ∑ n ∈ J, ∫ y in heightCell n, V10B3a.weight y * F y := by
      rw [Finset.mul_sum]
    _ ≤ _ := mul_le_mul_of_nonneg_left
      (finite_cell_integral J _ hi (fun y => mul_nonneg (V10B3a.weight_pos y).le (h0 y))) (by norm_num)

theorem interval_integral_finite_sum (J : Finset ℤ) (F : ℤ → ℝ → ℝ)
    (a : ℝ) (hi : ∀ n ∈ J, IntervalIntegrable (F n) volume a (a+1)) :
    IntervalIntegrable (fun x => ∑ n ∈ J, F n x) volume a (a+1) ∧
    (∫ x in a..a+1, ∑ n ∈ J, F n x) =
      ∑ n ∈ J, ∫ x in a..a+1, F n x := by
  classical
  induction J using Finset.induction_on with
  | empty => simp
  | @insert n J hn ih =>
    have h₁ := hi n (Finset.mem_insert_self n J)
    obtain ⟨h₂, he⟩ := ih (fun m hm => hi m (Finset.mem_insert_of_mem hm))
    simp only [Finset.sum_insert hn]
    exact ⟨h₁.add h₂, by rw [intervalIntegral.integral_add h₁ h₂, he]⟩

theorem rectangle_budget (H X Y Z : ℝ → ℝ → ℂ) (a B : ℝ)
    (J : Finset ℤ)
    (hc : ∀ x, Continuous (fun y => ‖H x y‖^2 + ‖Y x y‖^2))
    (hd : ∀ x, Continuous (fun y => ‖X x y‖^2 + ‖Z x y‖^2))
    (hi : ∀ x ∈ Icc a (a+1), Integrable
      (fun y => V10B3a.weight y * (‖H x y‖^2 + ‖Y x y‖^2)))
    (hj : ∀ x ∈ Icc a (a+1), Integrable
      (fun y => V10B3a.weight y * (‖X x y‖^2 + ‖Z x y‖^2)))
    (houter : ∀ n ∈ J, IntervalIntegrable (fun x =>
      V10B2.rowEnergy H Y (n : ℝ) x + V10B2.rowEnergy X Z (n : ℝ) x) volume a (a+1))
    (hB : ∀ x ∈ Icc a (a+1),
      (∫ y, V10B3a.weight y * (‖H x y‖^2 + ‖Y x y‖^2)) +
      (∫ y, V10B3a.weight y * (‖X x y‖^2 + ‖Z x y‖^2)) ≤ B) :
    (∑ n ∈ J, Real.log (|(n : ℝ)|+3) *
      V10B2.rectangleEnergy H X Y Z a (n : ℝ)) ≤ 2 * B := by
  let R : ℤ → ℝ → ℝ := fun n x => Real.log (|(n : ℝ)|+3) *
    (V10B2.rowEnergy H Y (n : ℝ) x + V10B2.rowEnergy X Z (n : ℝ) x)
  have hR : ∀ n ∈ J, IntervalIntegrable (R n) volume a (a+1) :=
    fun n hn => (houter n hn).const_mul _
  obtain ⟨hs, he⟩ := interval_integral_finite_sum J R a hR
  have hp : ∀ x ∈ Icc a (a+1), (∑ n ∈ J, R n x) ≤ 2*B := by
    intro x hx
    have h₁ := finite_row_budget J _ (hc x) (fun y => by positivity) (hi x hx)
    have h₂ := finite_row_budget J _ (hd x) (fun y => by positivity) (hj x hx)
    have hsplit : (∑ n ∈ J, R n x) =
      (∑ n ∈ J, Real.log (|(n : ℝ)|+3) * V10B2.rowEnergy H Y (n : ℝ) x) +
      (∑ n ∈ J, Real.log (|(n : ℝ)|+3) * V10B2.rowEnergy X Z (n : ℝ) x) := by
      simp only [R, mul_add, Finset.sum_add_distrib]
    rw [hsplit]
    unfold V10B2.rowEnergy
    linarith [hB x hx]
  calc
    _ = ∑ n ∈ J, ∫ x in a..a+1, R n x := by
      apply Finset.sum_congr rfl
      intro n hn
      unfold V10B2.rectangleEnergy R
      rw [intervalIntegral.integral_const_mul]
    _ = (∫ x in a..a+1, ∑ n ∈ J, R n x) := he.symm
    _ ≤ ∫ x in a..a+1, (2*B) :=
      intervalIntegral.integral_mono_on (by linarith) hs
        (continuous_const.intervalIntegrable a (a+1)) hp
    _ = 2*B := by simp [intervalIntegral.integral_const]

end WeilDefect.MasterRecon.V10B5b

#print axioms WeilDefect.MasterRecon.V10B5b.heightCell_unique
#print axioms WeilDefect.MasterRecon.V10B5b.finite_indicator_integral
#print axioms WeilDefect.MasterRecon.V10B5b.finite_cell_integral
#print axioms WeilDefect.MasterRecon.V10B5b.cell_energy_bound
#print axioms WeilDefect.MasterRecon.V10B5b.finite_row_budget
#print axioms WeilDefect.MasterRecon.V10B5b.interval_integral_finite_sum
#print axioms WeilDefect.MasterRecon.V10B5b.rectangle_budget
