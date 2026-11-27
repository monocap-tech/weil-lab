import WeilDefect.MasterRecon.V10B27a
import WeilDefect.MasterRecon.V10B26b

/-! One-sided restricted action: split the endpoint logarithm from the
polynomial difference and transport a uniform regular-kernel enclosure
to a physical convolution error. The remaining pointwise/Bochner
identification is not asserted here. -/
namespace WeilDefect.MasterRecon.V10B27b

open MeasureTheory Set
open V10B24b (zeroExtend h)

theorem left_difference_inside (L x r : ℝ) (p : ℝ → ℂ)
    (hx : x ∈ Ioo 0 L) (hr : r ∈ Ioc 0 x) :
    p x-zeroExtend L p (x-r) = p x-p (x-r) := by
  have hm : x-r ∈ Icc 0 L := ⟨by linarith [hr.2],by linarith [hr.1,hx.2]⟩
  unfold zeroExtend
  rw [indicator_of_mem hm]

theorem left_difference_outside (L x r : ℝ) (p : ℝ → ℂ)
    (hx : x ∈ Ioo 0 L) (hr : r ∈ Ioc x L) :
    p x-zeroExtend L p (x-r) = p x := by
  rw [V10B24b.outside_shift_left L p x r hx hr.1,sub_zero]

theorem left_log_piece (L x : ℝ) (p : ℝ → ℂ) (hx : x ∈ Ioo 0 L) :
    (∫ r in Ioc x L, ((1/(2*r):ℝ):ℂ)*(p x-zeroExtend L p (x-r))) =
      ((Real.log L-Real.log x:ℝ):ℂ)*p x/2 := by
  calc
    _ = ∫ r in Ioc x L, ((1/r:ℝ):ℂ)*(p x/2) := by
      apply setIntegral_congr_fun measurableSet_Ioc
      intro r hr
      rw [left_difference_outside L x r p hx hr]
      push_cast
      ring
    _ = _ := by
      rw [integral_mul_const,integral_complex_ofReal,
        ← intervalIntegral.integral_of_le hx.2.le]
      simp only [one_div]
      rw [integral_inv_of_pos hx.1 (hx.1.trans hx.2),Real.log_div (hx.1.trans hx.2).ne' hx.1.ne']
      ring

theorem convolution_error (x B e : ℝ) (hx : 0 ≤ x) (hB : 0 ≤ B) (he : 0 ≤ e)
    (p : ℝ → ℂ) (q : ℝ → ℝ)
    (hp : ∀ r ∈ Ioc 0 x, ‖p (x-r)‖ ≤ B)
    (hq : ∀ r ∈ Ioc 0 x, |h r-q r| ≤ e)
    (hi : IntegrableOn (fun r => ((h r-q r:ℝ):ℂ)*p (x-r)) (Ioc 0 x)) :
    ‖∫ r in Ioc (0:ℝ) x, ((h r-q r:ℝ):ℂ)*p (x-r)‖ ≤ x*e*B := by
  have hc : IntegrableOn (fun _ : ℝ => e*B) (Ioc 0 x) :=
    integrableOn_const measure_Ioc_lt_top.ne
  refine (norm_integral_le_integral_norm _).trans ?_
  calc
    _ ≤ ∫ r in Ioc (0:ℝ) x, e*B := by
      apply setIntegral_mono_on hi.norm hc measurableSet_Ioc
      intro r hr
      rw [norm_mul,Complex.norm_real,Real.norm_eq_abs]
      exact mul_le_mul (hq r hr) (hp r hr) (norm_nonneg _) he
    _ = _ := by
      rw [setIntegral_const,Measure.real,Real.volume_Ioc,sub_zero,ENNReal.toReal_ofReal hx,smul_eq_mul]
      ring

theorem frozen_convolution_error (x B : ℝ) (hx : 0 ≤ x) (hxL : x ≤ 1/2)
    (hB : 0 ≤ B) (p : ℝ → ℂ)
    (hp : ∀ r ∈ Ioc 0 x, ‖p (x-r)‖ ≤ B)
    (hi : IntegrableOn (fun r => ((h r-V10B27a.q r:ℝ):ℂ)*p (x-r)) (Ioc 0 x)) :
    ‖∫ r in Ioc (0:ℝ) x, ((h r-V10B27a.q r:ℝ):ℂ)*p (x-r)‖ ≤ x*(1/(2:ℝ)^28)*B :=
  convolution_error x B _ hx hB (by positivity) p V10B27a.q hp
    (fun r hr => V10B27a.frozen_kernel_bound r hr.1 (hr.2.trans hxL)) hi

end WeilDefect.MasterRecon.V10B27b

#print axioms WeilDefect.MasterRecon.V10B27b.left_difference_inside
#print axioms WeilDefect.MasterRecon.V10B27b.left_difference_outside
#print axioms WeilDefect.MasterRecon.V10B27b.left_log_piece
#print axioms WeilDefect.MasterRecon.V10B27b.convolution_error
#print axioms WeilDefect.MasterRecon.V10B27b.frozen_convolution_error
