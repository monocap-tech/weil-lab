import WeilDefect.MasterRecon.V09A
import Mathlib.Analysis.Calculus.ParametricIntegral
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

/-! V09B: entire analyticity and exponential type of the original
Mellin integral on the actual supported physical carrier. -/
namespace WeilDefect.MasterRecon.V09B

open MeasureTheory Set Filter Metric
open scoped Topology FourierTransform

noncomputable abbrev FullL2 := V08I.FullL2

theorem kernel_norm_bound (t : ℝ) (ht : 0 ≤ t) (x : ℝ) (hx : |x| ≤ t)
    (z : ℂ) :
    ‖Complex.exp (z * (x : ℂ))‖ ≤ Real.exp (‖z‖ * t) := by
  apply (Complex.norm_exp_le_exp_norm _).trans
  apply Real.exp_le_exp.mpr
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs]
  exact mul_le_mul_of_nonneg_left hx (norm_nonneg _)

theorem mellin_integrand_bound (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0) (z : ℂ) :
    ∀ᵐ x ∂volume, ‖Complex.exp (z * (x : ℂ)) * f x‖ ≤
      Real.exp (‖z‖ * t) * ‖f x‖ := by
  filter_upwards [hs] with x hx
  by_cases hm : x ∈ Icc (-t) t
  · rw [norm_mul]
    exact mul_le_mul_of_nonneg_right (kernel_norm_bound t ht x (abs_le.mpr hm) z)
      (norm_nonneg _)
  · simp [hx hm]

theorem mellin_integrand_measurable (f : ℝ → ℂ) (hf : Integrable f) (z : ℂ) :
    AEStronglyMeasurable (fun x : ℝ => Complex.exp (z * (x : ℂ)) * f x) volume := by
  have h : Continuous (fun x : ℝ => Complex.exp (z * (x : ℂ))) := by fun_prop
  exact h.aestronglyMeasurable.mul hf.aestronglyMeasurable

theorem mellin_integrand_integrable (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hf : Integrable f) (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0)
    (z : ℂ) :
    Integrable (fun x : ℝ => Complex.exp (z * (x : ℂ)) * f x) := by
  exact (hf.norm.const_mul (Real.exp (‖z‖ * t))).mono'
    (mellin_integrand_measurable f hf z) (mellin_integrand_bound t ht f hs z)

theorem mellin_derivative_bound (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0) (z : ℂ) :
    ∀ᵐ x ∂volume, ∀ w ∈ ball z 1,
      ‖Complex.exp (w * (x : ℂ)) * (x : ℂ) * f x‖ ≤
        (Real.exp ((‖z‖ + 1) * t) * t) * ‖f x‖ := by
  filter_upwards [hs] with x hx
  intro w hw
  by_cases hm : x ∈ Icc (-t) t
  · have hdist : ‖w - z‖ < 1 := by simpa [dist_eq_norm] using hw
    have hn : ‖w‖ ≤ ‖z‖ + 1 := by
      calc
        ‖w‖ = ‖w - z + z‖ := by rw [sub_add_cancel]
        _ ≤ ‖w - z‖ + ‖z‖ := norm_add_le _ _
        _ ≤ _ := by linarith
    have hk := (kernel_norm_bound t ht x (abs_le.mpr hm) w).trans
      (Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_right hn ht))
    rw [norm_mul, norm_mul, Complex.norm_real, Real.norm_eq_abs]
    exact mul_le_mul_of_nonneg_right
      (mul_le_mul hk (abs_le.mpr hm) (abs_nonneg _) (Real.exp_pos _).le)
      (norm_nonneg _)
  · simp [hx hm]

theorem mellin_hasDerivAt (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hf : Integrable f) (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0)
    (z : ℂ) :
    HasDerivAt (V07A.mellin f)
      (∫ x : ℝ, Complex.exp (z * (x : ℂ)) * (x : ℂ) * f x) z := by
  let F : ℂ → ℝ → ℂ := fun w x => Complex.exp (w * (x : ℂ)) * f x
  let D : ℂ → ℝ → ℂ := fun w x => Complex.exp (w * (x : ℂ)) * (x : ℂ) * f x
  let b : ℝ → ℝ := fun x => (Real.exp ((‖z‖ + 1) * t) * t) * ‖f x‖
  have hm : ∀ᶠ w in 𝓝 z, AEStronglyMeasurable (F w) volume :=
    Eventually.of_forall (mellin_integrand_measurable f hf)
  have hd : AEStronglyMeasurable (D z) volume := by
    have h : Continuous (fun x : ℝ => Complex.exp (z * (x : ℂ)) * (x : ℂ)) := by fun_prop
    exact h.aestronglyMeasurable.mul hf.aestronglyMeasurable
  have hb : Integrable b := hf.norm.const_mul _
  have hdiff : ∀ᵐ x ∂volume, ∀ w ∈ ball z 1,
      HasDerivAt (F · x) (D w x) w := by
    filter_upwards with x
    intro w _
    have hlin : HasDerivAt (fun v : ℂ => v * (x : ℂ)) (x : ℂ) w := by
      simpa using (hasDerivAt_id w).mul_const (x : ℂ)
    have he := (Complex.hasDerivAt_exp (w * (x : ℂ))).comp w hlin
    exact he.mul_const (f x)
  exact (hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (F := F) (F' := D) (bound := b) (ball_mem_nhds z (by norm_num))
    hm (mellin_integrand_integrable t ht f hf hs z) hd
    (mellin_derivative_bound t ht f hs z) hb hdiff).2

theorem mellin_entire (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hf : Integrable f) (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0)
    (z : ℂ) : AnalyticAt ℂ (V07A.mellin f) z := by
  have h : Differentiable ℂ (V07A.mellin f) :=
    fun w => (mellin_hasDerivAt t ht f hf hs w).differentiableAt
  exact h.analyticAt z

theorem mellin_exponential_type (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hf : Integrable f) (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0)
    (z : ℂ) :
    ‖V07A.mellin f z‖ ≤ Real.exp ((∫ x : ℝ, ‖f x‖) + t * ‖z‖) := by
  let A := ∫ x : ℝ, ‖f x‖
  have hA : A ≤ Real.exp A := by linarith [Real.add_one_le_exp A]
  unfold V07A.mellin
  calc
    _ ≤ ∫ x : ℝ, Real.exp (‖z‖ * t) * ‖f x‖ :=
      norm_integral_le_of_norm_le (hf.norm.const_mul _) (mellin_integrand_bound t ht f hs z)
    _ = Real.exp (‖z‖ * t) * A := integral_const_mul _ _
    _ ≤ Real.exp (‖z‖ * t) * Real.exp A :=
      mul_le_mul_of_nonneg_left hA (Real.exp_pos _).le
    _ = _ := by rw [← Real.exp_add]; congr 1; unfold A; ring

theorem mellin_imaginary_axis (f : ℝ → ℂ) (u : ℝ) :
    V07A.mellin f (-(u : ℂ) * Complex.I) = V08H.angularFourier f u := by
  unfold V07A.mellin V08H.angularFourier
  apply integral_congr_ae
  filter_upwards with x
  rw [V08D.fourierKernel]
  congr 2
  ring

theorem physical_zero_of_mellin_zero (f : FullL2) (hf : Integrable (fun x : ℝ => f x))
    (hz : V07A.mellin (f : ℝ → ℂ) = 0) : f = 0 := by
  have h : ‖f‖ ^ 2 = 0 := by
    rw [V08H.angularFourier_plancherel f hf]
    have ha (u : ℝ) : V08H.angularFourier (f : ℝ → ℂ) u = 0 := by
      rw [← mellin_imaginary_axis, hz]
      rfl
    simp [ha]
  exact norm_eq_zero.mp (by nlinarith [norm_nonneg f])

theorem carrier_zero_of_mellin_zero (t : ℝ) (g : V08I.logCarrier t)
    (hz : V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ) = 0) : g = 0 := by
  apply V08J.physicalInclusion_injective t
  rw [map_zero]
  exact physical_zero_of_mellin_zero _ (V08K.supported_integrable t _
    (V08I.physicalInclusion_support t g)) hz

end WeilDefect.MasterRecon.V09B

#print axioms WeilDefect.MasterRecon.V09B.kernel_norm_bound
#print axioms WeilDefect.MasterRecon.V09B.mellin_integrand_bound
#print axioms WeilDefect.MasterRecon.V09B.mellin_integrand_measurable
#print axioms WeilDefect.MasterRecon.V09B.mellin_integrand_integrable
#print axioms WeilDefect.MasterRecon.V09B.mellin_derivative_bound
#print axioms WeilDefect.MasterRecon.V09B.mellin_hasDerivAt
#print axioms WeilDefect.MasterRecon.V09B.mellin_entire
#print axioms WeilDefect.MasterRecon.V09B.mellin_exponential_type
#print axioms WeilDefect.MasterRecon.V09B.mellin_imaginary_axis
#print axioms WeilDefect.MasterRecon.V09B.physical_zero_of_mellin_zero
#print axioms WeilDefect.MasterRecon.V09B.carrier_zero_of_mellin_zero
