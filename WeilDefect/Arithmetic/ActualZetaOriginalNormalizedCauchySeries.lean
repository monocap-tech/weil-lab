import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped ENNReal NNReal Interval

/-! NF588: canonical normalized Cauchy coefficients, with the
same analytic function used in the value and derivative sums.
Complex-disc normalization maps the old radius 1/25 to radius 20.
No arbitrary choice of Taylor coefficients. -/

def neutralNF588NormalizedCoefficient (F : ℂ → ℂ) (n : ℕ) : ℝ :=
  ((cauchyPowerSeries F 0 20).coeff n).re

theorem neutralNF588NormalizedCoefficient_bound (F : ℂ → ℂ)
    (hF : Differentiable ℂ F) (M : ℝ)
    (hM : ∀ z : ℂ, ‖z‖ = 20 → ‖F z‖ ≤ M) (n : ℕ) :
    ‖neutralNF588NormalizedCoefficient F n‖ ≤ M*(1/20:ℝ)^n := by
  have hc : Continuous (fun θ : ℝ => ‖F (circleMap 0 20 θ)‖) :=
    (hF.continuous.comp (continuous_circleMap _ _)).norm
  have hi : (∫ θ in (0:ℝ)..2*Real.pi, ‖F (circleMap 0 20 θ)‖) ≤
      (2*Real.pi)*M := by
    calc
      _ ≤ ∫ _ in (0:ℝ)..2*Real.pi, M := by
        apply intervalIntegral.integral_mono_on Real.two_pi_pos.le
          (hc.intervalIntegrable 0 (2*Real.pi)) intervalIntegrable_const
        intro θ _
        apply hM
        rw [norm_circleMap_zero]
        norm_num
      _ = _ := by rw [intervalIntegral.integral_const]; simp [smul_eq_mul]
  have havg : (2*Real.pi)⁻¹*(∫ θ in (0:ℝ)..2*Real.pi,
      ‖F (circleMap 0 20 θ)‖) ≤ M := by
    calc
      _ ≤ (2*Real.pi)⁻¹*((2*Real.pi)*M) :=
        mul_le_mul_of_nonneg_left hi (inv_nonneg.mpr Real.two_pi_pos.le)
      _ = _ := by rw [← mul_assoc,inv_mul_cancel₀ Real.two_pi_pos.ne',one_mul]
  unfold neutralNF588NormalizedCoefficient
  rw [Real.norm_eq_abs]
  apply (Complex.abs_re_le_norm _).trans
  rw [← FormalMultilinearSeries.norm_apply_eq_norm_coef]
  have hb := norm_cauchyPowerSeries_le F 0 20 n
  refine hb.trans ?_
  norm_num only [abs_of_nonneg (by norm_num : (0:ℝ)≤20), one_div]
  exact mul_le_mul_of_nonneg_right havg (by positivity)

theorem neutralNF588NormalizedCoefficient_value (F : ℂ → ℂ)
    (hF : Differentiable ℂ F) (w : ℝ) :
    HasSum (fun n : ℕ => neutralNF588NormalizedCoefficient F n*w^n)
      (F (w:ℂ)).re := by
  let p := cauchyPowerSeries F 0 20
  have hp : HasFPowerSeriesOnBall F p 0 ∞ :=
    hF.hasFPowerSeriesOnBall 0 (R := 20) (by norm_num)
  have hw : (w:ℂ) ∈ Metric.eball (0:ℂ) ∞ := by simp
  have hc := hp.hasSum hw
  have h := Complex.reCLM.hasSum hc
  convert h using 1
  · funext n
    change neutralNF588NormalizedCoefficient F n*w^n =
      (p n (fun _ => (w:ℂ))).re
    rw [FormalMultilinearSeries.apply_eq_pow_smul_coeff]
    simp [neutralNF588NormalizedCoefficient,p,smul_eq_mul,← Complex.ofReal_pow,
      Complex.mul_re,mul_comm]
  · simp

/-- The derivative coefficients are from the actual differentiated
Cauchy series, not an independent numerical approximation. -/
theorem neutralNF588NormalizedCoefficient_derivative (F : ℂ → ℂ)
    (hF : Differentiable ℂ F) (w : ℝ) :
    HasSum (fun n : ℕ => (n:ℝ)*neutralNF588NormalizedCoefficient F n*w^(n-1))
      (deriv F (w:ℂ)).re := by
  let p := cauchyPowerSeries F 0 20
  have hp : HasFPowerSeriesOnBall F p 0 ∞ :=
    hF.hasFPowerSeriesOnBall 0 (R := 20) (by norm_num)
  have hw : (w:ℂ) ∈ Metric.eball (0:ℂ) ∞ := by simp
  have hc := hp.fderiv.hasSum hw
  let E : (ℂ →L[ℂ] ℂ) →L[ℝ] ℝ :=
    Complex.reCLM.comp ((ContinuousLinearMap.apply ℂ ℂ (1:ℂ)).restrictScalars ℝ)
  have h := E.hasSum hc
  have hs : HasSum (fun n : ℕ =>
      ((n+1:ℕ):ℝ)*neutralNF588NormalizedCoefficient F (n+1)*w^n)
        (deriv F (w:ℂ)).re := by
    convert h using 1
    · funext n
      change _ = (p.derivSeries n (fun _ => (w:ℂ)) 1).re
      rw [FormalMultilinearSeries.apply_eq_pow_smul_coeff]
      simp only [ContinuousLinearMap.smul_apply,
        FormalMultilinearSeries.derivSeries_coeff_one, smul_eq_mul,
        nsmul_eq_mul]
      simp [neutralNF588NormalizedCoefficient,p,← Complex.ofReal_pow,
        Complex.mul_re,mul_comm,mul_left_comm,mul_assoc]
    · change (deriv F (w:ℂ)).re = (fderiv ℂ F (0+(w:ℂ)) 1).re
      rw [zero_add,fderiv_apply_one_eq_deriv]
  apply (hasSum_nat_add_iff' 1).mp
  simpa only [Finset.sum_range_one,Nat.cast_zero,zero_mul,Nat.zero_sub,zero_sub,
    Nat.add_sub_cancel,sub_zero] using hs

end
end WeilDefect
