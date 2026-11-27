import WeilDefect.MasterRecon.V10B24a
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

/-! V10B24b: scalar restricted physical action, split at the support
length. The finite-cutoff identity exposes the only scalar limit needed.
No point evaluation of an L² equivalence class is asserted. -/
namespace WeilDefect.MasterRecon.V10B24b

open MeasureTheory Set Filter
open scoped Topology

noncomputable def den (r : ℝ) := 1-Real.exp (-2*r)
noncomputable def k (r : ℝ) := Real.exp (-r/2)/den r
noncomputable def h (r : ℝ) := k r-1/(2*r)
noncomputable def b (r : ℝ) := 2*Real.exp (-2*r)/den r

noncomputable def zeroExtend (L : ℝ) (p : ℝ → ℂ) : ℝ → ℂ :=
  (Icc 0 L).indicator p

noncomputable def physicalTerm (L : ℝ) (p : ℝ → ℂ) (x r : ℝ) : ℂ :=
  (b r:ℂ)*zeroExtend L p x-
    (k r:ℂ)*(zeroExtend L p (x-r)+zeroExtend L p (x+r))

theorem den_pos (r : ℝ) (hr : 0 < r) : 0 < den r := by
  unfold den
  have hh := Real.exp_lt_exp.mpr (show -2*r<0 by linarith)
  rw [Real.exp_zero] at hh
  linarith

theorem restricted_split (L : ℝ) (p : ℝ → ℂ) (x r : ℝ)
    (hx : x ∈ Ioo 0 L) (hr : 0 < r) :
    physicalTerm L p x r =
      ((b r-1/r:ℝ):ℂ)*p x+
      ((1/(2*r):ℝ):ℂ)*((p x-zeroExtend L p (x-r))+
        (p x-zeroExtend L p (x+r)))-
      (h r:ℂ)*(zeroExtend L p (x-r)+zeroExtend L p (x+r)) := by
  unfold physicalTerm h
  have hx' : zeroExtend L p x = p x := indicator_of_mem ⟨hx.1.le,hx.2.le⟩ _
  rw [hx']
  push_cast
  field_simp [show (r:ℂ) ≠ 0 by exact_mod_cast hr.ne']
  <;> ring

theorem outside_shift_left (L : ℝ) (p : ℝ → ℂ) (x r : ℝ)
    (hx : x ∈ Ioo 0 L) (hr : x < r) :
    zeroExtend L p (x-r) = 0 := by
  apply indicator_of_notMem
  intro hh
  exact (not_le_of_gt (sub_neg.mpr hr)) hh.1

theorem outside_shift_right (L : ℝ) (p : ℝ → ℂ) (x r : ℝ)
    (hx : x ∈ Ioo 0 L) (hr : L-x < r) :
    zeroExtend L p (x+r) = 0 := by
  apply indicator_of_notMem
  intro hh
  linarith [hh.2]

theorem far_action (L : ℝ) (p : ℝ → ℂ) (x r : ℝ)
    (hx : x ∈ Ioo 0 L) (hr : L ≤ r) :
    physicalTerm L p x r = (b r:ℂ)*p x := by
  unfold physicalTerm
  rw [outside_shift_left L p x r hx (by linarith [hx.2]),
    outside_shift_right L p x r hx (by linarith [hx.1])]
  simp only [add_zero,mul_zero,sub_zero]
  rw [zeroExtend,indicator_of_mem (show x ∈ Icc 0 L from ⟨hx.1.le,hx.2.le⟩)]

theorem log_den_deriv (r : ℝ) (hr : 0 < r) :
    HasDerivAt (fun s => Real.log (den s)) (b r) r := by
  have he := (Real.hasDerivAt_exp (-2*r)).comp r
    ((hasDerivAt_const r (-2:ℝ)).mul (hasDerivAt_id r))
  have hd : HasDerivAt den (2*Real.exp (-2*r)) r := by
    unfold den
    convert (hasDerivAt_const r (1:ℝ)).sub he using 1 <;> ring
  have hh := (Real.hasDerivAt_log (den_pos r hr).ne').comp r hd
  convert hh using 1
  unfold b
  ring

theorem b_integral (a c : ℝ) (ha : 0 < a) (hac : a ≤ c) :
    (∫ r in a..c, b r) = Real.log (den c)-Real.log (den a) := by
  have hd : ∀ r ∈ uIcc a c, 0 < r := by
    rw [uIcc_of_le hac]
    intro r hr
    exact ha.trans_le hr.1
  apply intervalIntegral.integral_eq_sub_of_hasDerivAt
    (fun r hr => log_den_deriv r (hd r hr))
  apply ContinuousOn.intervalIntegrable
  unfold b
  have he : Continuous den := by unfold den; fun_prop
  exact (by fun_prop : Continuous (fun r : ℝ => 2*Real.exp (-2*r))).continuousOn.div
    he.continuousOn (fun r hr => (den_pos r (hd r hr)).ne')

theorem finite_constant (a L T : ℝ) (ha : 0 < a) (haL : a ≤ L) (hLT : L ≤ T) :
    (∫ r in a..L, b r-1/r)+(∫ r in L..T, b r) =
      Real.log (den T)-Real.log (den a/a)-Real.log L := by
  have hL := ha.trans_le haL
  have hd : ∀ r ∈ uIcc a L, 0 < r := by
    rw [uIcc_of_le haL]
    intro r hr
    exact ha.trans_le hr.1
  have hb : IntervalIntegrable b volume a L := by
    apply ContinuousOn.intervalIntegrable
    unfold b
    have he : Continuous den := by unfold den; fun_prop
    exact (by fun_prop : Continuous (fun r : ℝ => 2*Real.exp (-2*r))).continuousOn.div
      he.continuousOn (fun r hr => (den_pos r (hd r hr)).ne')
  have hi : IntervalIntegrable (fun r : ℝ => 1/r) volume a L := by
    apply ContinuousOn.intervalIntegrable
    exact continuousOn_const.div continuous_id.continuousOn (fun r hr => (hd r hr).ne')
  rw [intervalIntegral.integral_sub hb hi,b_integral a L ha haL,b_integral L T hL hLT]
  simp only [one_div]
  rw [integral_inv_of_pos ha hL,Real.log_div hL.ne' ha.ne',
    Real.log_div (den_pos a ha).ne' ha.ne']
  ring

end WeilDefect.MasterRecon.V10B24b

#print axioms WeilDefect.MasterRecon.V10B24b.den_pos
#print axioms WeilDefect.MasterRecon.V10B24b.restricted_split
#print axioms WeilDefect.MasterRecon.V10B24b.outside_shift_left
#print axioms WeilDefect.MasterRecon.V10B24b.outside_shift_right
#print axioms WeilDefect.MasterRecon.V10B24b.far_action
#print axioms WeilDefect.MasterRecon.V10B24b.log_den_deriv
#print axioms WeilDefect.MasterRecon.V10B24b.b_integral
#print axioms WeilDefect.MasterRecon.V10B24b.finite_constant
