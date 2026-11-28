import WeilDefect.MasterRecon.V10B21b
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

/-! V10B21c: explicit integrable envelope for the operator-valued
digamma integrand. Strong measurability remains a separate premise
of the final Bochner receiver. -/
namespace WeilDefect.MasterRecon.V10B21c

open MeasureTheory Set Filter
open V08I (FullL2)
open V10B8d (shift)

noncomputable def denominator (r : ℝ) : ℝ := 1-Real.exp (-2*r)

noncomputable def numerator (f : FullL2) (r : ℝ) : FullL2 :=
  (2*Real.exp (-2*r)) • f -
    Real.exp (-r/2) • (shift r f+shift (-r) f)

noncomputable def actionTerm (f : FullL2) (r : ℝ) : FullL2 :=
  (denominator r)⁻¹ • numerator f r

theorem denominator_lower (r : ℝ) (hr : 0 < r) :
    2*r ≤ (1+2*r)*denominator r := by
  have h := mul_le_mul_of_nonneg_right (Real.add_one_le_exp (2*r))
    (Real.exp_pos (-2*r)).le
  rw [← Real.exp_add,show 2*r+(-2*r)=0 by ring,Real.exp_zero] at h
  unfold denominator
  nlinarith only [h]

theorem denominator_pos (r : ℝ) (hr : 0 < r) : 0 < denominator r := by
  unfold denominator
  have h : Real.exp (-2*r) < Real.exp 0 := Real.exp_lt_exp.mpr (by linarith)
  rw [Real.exp_zero] at h
  linarith

theorem denominator_near (r : ℝ) (hr : 0 < r) (hr1 : r ≤ 1) :
    2*r/3 ≤ denominator r := by
  have h := denominator_lower r hr
  have h' := mul_le_mul_of_nonneg_right (show 1+2*r ≤ 3 by linarith)
    (denominator_pos r hr).le
  linarith

theorem denominator_far (r : ℝ) (hr : 1 ≤ r) : 2/3 ≤ denominator r := by
  have h : Real.exp (-2*r) ≤ Real.exp (-2*1) :=
    Real.exp_le_exp.mpr (by linarith)
  have h' : (2:ℝ)/3 ≤ denominator 1 := by
    simpa only [mul_one] using denominator_near 1 (by norm_num) (by norm_num)
  exact h'.trans (sub_le_sub_left h 1)

theorem coefficient_near (r : ℝ) (hr : 0 ≤ r) :
    |2*Real.exp (-2*r)-2*Real.exp (-r/2)| ≤ 3*r := by
  have h : Real.exp (-2*r) ≤ Real.exp (-r/2) :=
    Real.exp_le_exp.mpr (by linarith)
  rw [abs_of_nonpos (by linarith)]
  have he : Real.exp (-2*r) = Real.exp (-r/2)*Real.exp (-(3*r/2)) := by
    rw [← Real.exp_add]
    congr 1
    ring
  rw [he]
  have h₁ := Real.add_one_le_exp (-(3*r/2))
  have h₂ : 0 ≤ 1-Real.exp (-(3*r/2)) := by
    have h' := Real.exp_le_exp.mpr (show -(3*r/2) ≤ 0 by linarith)
    rw [Real.exp_zero] at h'
    linarith
  have h₃ : Real.exp (-r/2) ≤ 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by linarith)
  have h₄ := mul_le_mul_of_nonneg_right h₃ h₂
  nlinarith only [h₁,h₄]

theorem numerator_split (f : FullL2) (r : ℝ) :
    numerator f r =
      (2*Real.exp (-2*r)-2*Real.exp (-r/2)) • f -
      Real.exp (-r/2) • (shift r f-f) -
      Real.exp (-r/2) • (shift (-r) f-f) := by
  unfold numerator
  have he : (2*Real.exp (-r/2)) • f =
      Real.exp (-r/2) • f + Real.exp (-r/2) • f := by
    rw [show 2*Real.exp (-r/2) = Real.exp (-r/2)+Real.exp (-r/2) by ring,add_smul]
  rw [sub_smul,smul_sub,smul_sub,smul_add,he]
  abel

theorem opposite_shift_norm (r : ℝ) (f : FullL2) :
    ‖shift (-r) f-f‖ = ‖shift r f-f‖ := by
  rw [← V10B8d.shift_norm r (shift (-r) f-f),map_sub]
  have h := V10B8d.shift_inverse (-r) f
  rw [neg_neg] at h
  rw [h,norm_sub_rev]

theorem numerator_near (f : FullL2) (C r : ℝ) (hC : 0 ≤ C)
    (hr : 0 < r) (hshift : ‖shift r f-f‖ ≤ C*Real.sqrt r) :
    ‖numerator f r‖ ≤ 3*r*‖f‖+2*C*Real.sqrt r := by
  rw [numerator_split]
  have hm : Real.exp (-r/2) ≤ 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by linarith)
  have h₁ := mul_le_mul_of_nonneg_right (coefficient_near r hr.le) (norm_nonneg f)
  have h₂ := mul_le_mul hm hshift (norm_nonneg _) zero_le_one
  have h₃ : ‖shift (-r) f-f‖ ≤ C*Real.sqrt r := by rwa [opposite_shift_norm]
  have h₄ := mul_le_mul hm h₃ (norm_nonneg _) zero_le_one
  have ha := norm_sub_le ((2*Real.exp (-2*r)-2*Real.exp (-r/2)) • f)
    (Real.exp (-r/2) • (shift r f-f))
  have hb := norm_sub_le (((2*Real.exp (-2*r)-2*Real.exp (-r/2)) • f)-
    Real.exp (-r/2) • (shift r f-f)) (Real.exp (-r/2) • (shift (-r) f-f))
  simp only [norm_smul,Real.norm_eq_abs,abs_of_pos (Real.exp_pos _)] at ha hb
  linarith only [ha,hb,h₁,h₂,h₄]

theorem action_near (f : FullL2) (C r : ℝ) (hC : 0 ≤ C)
    (hr : 0 < r) (hr1 : r ≤ 1) (hshift : ‖shift r f-f‖ ≤ C*Real.sqrt r) :
    ‖actionTerm f r‖ ≤ (9/2:ℝ)*‖f‖+3*C*(Real.sqrt r)⁻¹ := by
  have hd := denominator_pos r hr
  have hs := Real.sqrt_pos.2 hr
  have h := numerator_near f C r hC hr hshift
  unfold actionTerm
  rw [norm_smul,Real.norm_eq_abs,abs_of_pos (inv_pos.mpr hd),inv_mul_eq_div]
  apply (div_le_iff₀ hd).mpr
  have he : (9/2:ℝ)*‖f‖+3*C*(Real.sqrt r)⁻¹ ≥ 0 := by positivity
  have hh := mul_le_mul_of_nonneg_left (denominator_near r hr hr1) he
  have hid : ((9/2:ℝ)*‖f‖+3*C*(Real.sqrt r)⁻¹)*(2*r/3) =
      3*r*‖f‖+2*C*Real.sqrt r := by
    have hsq : r = Real.sqrt r * Real.sqrt r := by
      rw [← pow_two,Real.sq_sqrt hr.le]
    have hi : (Real.sqrt r)⁻¹*r = Real.sqrt r := by
      calc
        _ = (Real.sqrt r)⁻¹*(Real.sqrt r*Real.sqrt r) := congrArg ((Real.sqrt r)⁻¹ * ·) hsq
        _ = Real.sqrt r := by rw [← mul_assoc,inv_mul_cancel₀ hs.ne',one_mul]
    calc
      _ = 3*r*‖f‖+2*C*((Real.sqrt r)⁻¹*r) := by ring
      _ = _ := by rw [hi]
  rw [hid] at hh
  exact h.trans hh

theorem action_far (f : FullL2) (r : ℝ) (hr : 1 ≤ r) :
    ‖actionTerm f r‖ ≤ 6*‖f‖*Real.exp (-r/2) := by
  have hd := denominator_pos r (by linarith)
  have he : Real.exp (-2*r) ≤ Real.exp (-r/2) :=
    Real.exp_le_exp.mpr (by linarith)
  have hsum := norm_add_le (shift r f) (shift (-r) f)
  rw [V10B8d.shift_norm,V10B8d.shift_norm] at hsum
  have h := norm_sub_le ((2*Real.exp (-2*r)) • f)
    (Real.exp (-r/2) • (shift r f+shift (-r) f))
  simp only [norm_smul,Real.norm_eq_abs,abs_of_nonneg (show 0 ≤ 2*Real.exp (-2*r) by positivity),
    abs_of_pos (Real.exp_pos _)] at h
  have h₁ := mul_le_mul_of_nonneg_right he (show 0 ≤ 2*‖f‖ by positivity)
  have h₂ := mul_le_mul_of_nonneg_left hsum (Real.exp_pos (-r/2)).le
  unfold actionTerm numerator
  rw [norm_smul,Real.norm_eq_abs,abs_of_pos (inv_pos.mpr hd),inv_mul_eq_div]
  apply (div_le_iff₀ hd).mpr
  have h₃ := mul_le_mul_of_nonneg_left (denominator_far r hr)
    (show 0 ≤ 6*‖f‖*Real.exp (-r/2) by positivity)
  nlinarith only [h,h₁,h₂,h₃]

end WeilDefect.MasterRecon.V10B21c

#print axioms WeilDefect.MasterRecon.V10B21c.denominator_lower
#print axioms WeilDefect.MasterRecon.V10B21c.denominator_pos
#print axioms WeilDefect.MasterRecon.V10B21c.denominator_near
#print axioms WeilDefect.MasterRecon.V10B21c.denominator_far
#print axioms WeilDefect.MasterRecon.V10B21c.coefficient_near
#print axioms WeilDefect.MasterRecon.V10B21c.numerator_split
#print axioms WeilDefect.MasterRecon.V10B21c.opposite_shift_norm
#print axioms WeilDefect.MasterRecon.V10B21c.numerator_near
#print axioms WeilDefect.MasterRecon.V10B21c.action_near
#print axioms WeilDefect.MasterRecon.V10B21c.action_far
