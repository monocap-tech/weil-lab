import WeilDefect.MasterRecon.V10B16b
import WeilDefect.MasterRecon.V10B8c
import WeilDefect.MasterRecon.V10B17Defs
import Mathlib.Analysis.Complex.ExponentialBounds

/-! Prime-free small support: sharpen the one-sided Stirling estimate
and retain only the negative pole direction. -/
namespace WeilDefect.MasterRecon.V10B17a

open Complex MeasureTheory Set
open scoped InnerProduct ComplexConjugate
open V08I (logCarrier logWeight)
open V10B8e (gammaSymbol residual)

theorem globalBudget_le_24 : V10B15a.globalBudget ≤ 24 := by
  have hp : 0 ≤ Real.log Real.pi := Real.log_nonneg (by linarith [Real.pi_gt_three])
  have h4 : Real.log Real.pi ≤ 2*Real.log 2 := by
    have h := Real.log_le_log Real.pi_pos (by linarith [Real.pi_lt_d2] : Real.pi ≤ 4)
    have he : Real.log (4:ℝ) = 2*Real.log 2 := by
      rw [show (4:ℝ) = 2*2 by norm_num,Real.log_mul (by norm_num) (by norm_num)]
      ring
    rwa [he] at h
  have h6 : Real.log (6:ℝ) = Real.log 2+Real.log 3 := by
    rw [show (6:ℝ) = 2*3 by norm_num,Real.log_mul (by norm_num) (by norm_num)]
  unfold V10B15a.globalBudget
  rw [abs_of_nonneg hp,h6]
  linarith [Real.log_two_lt_d9,Real.log_three_lt_d9]

theorem high_at_three (hV : V10B8f.VerticalStirling) (u : ℝ) (hu : 3 < |u|) :
    (1/4:ℝ)*logWeight u ≤ gammaSymbol u := by
  let v := -Real.pi*u
  have hv : 9 ≤ |v| := by
    dsimp [v]
    rw [abs_mul,abs_neg,abs_of_pos Real.pi_pos]
    nlinarith [Real.pi_gt_three, mul_nonneg (show 0 ≤ Real.pi-3 by linarith [Real.pi_gt_three])
      (show 0 ≤ |u|-3 by linarith)]
  have hvp : 0 < |v| := by linarith
  have hsq : 81 ≤ v^2 := by rw [← sq_abs]; nlinarith
  have he : 5/v^2 ≤ (5/81:ℝ) := by
    apply (div_le_iff₀ (by linarith : 0 < v^2)).mpr
    linarith
  have hψ := (abs_le.mp (hV v (by linarith))).1
  have hlog : 2*Real.log 3 ≤ Real.log |v| := by
    have h := Real.log_le_log (by norm_num : (0:ℝ) < 9) hv
    rw [show (9:ℝ) = 3*3 by norm_num,Real.log_mul (by norm_num) (by norm_num)] at h
    linarith
  have hp : Real.log Real.pi ≤ Real.log 3+1/20 := by
    have h := Real.log_le_sub_one_of_pos (div_pos Real.pi_pos (by norm_num : (0:ℝ)<3))
    rw [Real.log_div Real.pi_pos.ne' (by norm_num)] at h
    linarith [Real.pi_lt_d2]
  have hw : Real.log (2+2*|v|) ≤ Real.log 3+Real.log |v| := by
    rw [← Real.log_mul (by norm_num : (3:ℝ) ≠ 0) hvp.ne']
    exact Real.log_le_log (by positivity) (by linarith)
  rw [V10B8f.gammaSymbol_reparam,V10B8f.weight_reparam]
  change (1/4:ℝ)*Real.log (2+2*|v|) ≤
    (Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re-Real.log Real.pi
  linarith [Real.log_three_gt_d9]

theorem small_symbol_split (hV : V10B8f.VerticalStirling)
    (hC : ∀ u, |residual u| ≤ 24) (f : ℝ → ℂ)
    (ha : Integrable (fun u => gammaSymbol u*‖f u‖^2))
    (hw : Integrable (fun u => logWeight u*‖f u‖^2))
    (hf : Integrable (fun u => ‖f u‖^2)) :
    (1/4:ℝ)*(∫ u, logWeight u*‖f u‖^2) -
      24*(∫ u in Icc (-3:ℝ) 3, ‖f u‖^2) ≤
      ∫ u, gammaSymbol u*‖f u‖^2 := by
  apply V10B16a.signed_split _ _ _ _ measurableSet_Icc _ _ ha hw hf
  · intro u _
    simpa using V10B16b.low_symbol 24 0 hC u
  · intro u hu
    have h : 3 < |u| := by
      by_contra hn
      exact hu (abs_le.mp (le_of_not_gt hn))
    exact high_at_three hV u h


theorem pole_nonneg_of_difference_zero (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t)
    (hg : poleDifference t ht g = 0) :
    0 ≤ (inner ℂ (V10B8c.poleOperator t ht g) g).re := by
  have he : V10B8c.eval t (1/2) ht g = V10B8c.eval t (-1/2) ht g := sub_eq_zero.mp hg
  rw [V10B8c.pole_pairing,he]
  simp only [Complex.add_re,Complex.mul_re,Complex.conj_re,Complex.conj_im]
  nlinarith [sq_nonneg (V10B8c.eval t (-1/2) ht g).re,
    sq_nonneg (V10B8c.eval t (-1/2) ht g).im]

end WeilDefect.MasterRecon.V10B17a

#print axioms WeilDefect.MasterRecon.V10B17a.globalBudget_le_24
#print axioms WeilDefect.MasterRecon.V10B17a.high_at_three
#print axioms WeilDefect.MasterRecon.V10B17a.small_symbol_split
#print axioms WeilDefect.MasterRecon.V10B17a.pole_nonneg_of_difference_zero
