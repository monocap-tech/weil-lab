import WeilDefect.MasterRecon.V10B24b
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp

/-! V10B25b: rational residual route to the frozen regular-kernel
enclosure. Taylor representation and exact rational residual bounds
are explicit inputs to the receiver; no complex Cauchy bound is needed. -/
namespace WeilDefect.MasterRecon.V10B25b

open V10B24b (h k den)

noncomputable def D (r : ℝ) : ℝ := Real.sinh r/r
noncomputable def N (r : ℝ) : ℝ := (Real.exp (r/2)-D r)/(2*r)

theorem denominator_ge_one (r : ℝ) (hr : 0 < r) : 1 ≤ D r := by
  unfold D
  apply (le_div_iff₀ hr).mpr
  simpa only [one_mul] using (Real.self_le_sinh_iff.mpr hr.le)

theorem quotient_residual (n d q e : ℝ) (hd : 1 ≤ d) (he : |n-d*q| ≤ e) :
    |n/d-q| ≤ e := by
  have hp : 0 < d := by linarith
  rw [show n/d-q=(n-d*q)/d by field_simp [hp.ne'],abs_div,abs_of_pos hp]
  apply (div_le_iff₀ hp).mpr
  have he0 := (abs_nonneg _).trans he
  calc
    |n-d*q| ≤ e := he
    _ = e*1 := by ring
    _ ≤ e*d := mul_le_mul_of_nonneg_left hd he0

theorem residual_budget (n d np dp q an ad B R : ℝ)
    (hn : |n-np| ≤ an) (hd : |d-dp| ≤ ad)
    (hq : |q| ≤ B) (hR : |np-dp*q| ≤ R) :
    |n-d*q| ≤ R+an+ad*B := by
  have he : n-d*q=(np-dp*q)+(n-np)-(d-dp)*q := by ring
  rw [he]
  have had := (abs_nonneg _).trans hd
  have hq0 := abs_nonneg q
  calc
    _ ≤ |(np-dp*q)+(n-np)|+|(d-dp)*q| := by rw [sub_eq_add_neg]; simpa only [abs_neg] using abs_add_le ((np-dp*q)+(n-np)) (-((d-dp)*q))
    _ ≤ (|np-dp*q|+|n-np|)+|(d-dp)*q| :=
      add_le_add_left (abs_add_le _ _) _
    _ ≤ R+an+ad*B := by
      rw [abs_mul]
      exact add_le_add (add_le_add hR hn) (mul_le_mul hd hq hq0 had)

theorem analytic_receiver (r q np dp an ad B R : ℝ)
    (hr : 0 < r)
    (hn : |N r-np| ≤ an) (hd : |D r-dp| ≤ ad)
    (hq : |q| ≤ B) (hR : |np-dp*q| ≤ R) :
    |N r/D r-q| ≤ R+an+ad*B :=
  quotient_residual _ _ _ _ (denominator_ge_one r hr)
    (residual_budget _ _ _ _ _ _ _ _ _ hn hd hq hR)

end WeilDefect.MasterRecon.V10B25b

#print axioms WeilDefect.MasterRecon.V10B25b.denominator_ge_one
#print axioms WeilDefect.MasterRecon.V10B25b.quotient_residual
#print axioms WeilDefect.MasterRecon.V10B25b.residual_budget
#print axioms WeilDefect.MasterRecon.V10B25b.analytic_receiver
