import WeilDefect.MasterRecon.V10B3b
import Mathlib.MeasureTheory.Group.LIntegral
import Mathlib.Analysis.Convolution

/-! V10B3c: attach the logarithmic weight to the nonnegative Young
receiver. Translation invariance is supplied by Lebesgue measure;
the complex convolution-to-physical-product identity remains separate. -/
namespace WeilDefect.MasterRecon.V10B3c

open MeasureTheory
open scoped ENNReal

noncomputable def rootWeight (y : ℝ) : ℝ :=
  Real.sqrt (V10B3a.weight y)

noncomputable def weightConstant : ℝ :=
  Real.sqrt (2 / Real.log 2)

theorem weightConstant_nonneg : 0 ≤ weightConstant :=
  Real.sqrt_nonneg _

theorem rootWeight_nonneg (y : ℝ) : 0 ≤ rootWeight y :=
  Real.sqrt_nonneg _

theorem rootWeight_continuous : Continuous rootWeight := by
  unfold rootWeight V10B3a.weight
  apply Real.continuous_sqrt.comp
  apply Continuous.log (by fun_prop)
  intro y
  linarith [abs_nonneg y]

theorem rootWeight_split (y u : ℝ) :
    rootWeight y ≤ weightConstant * rootWeight u * rootWeight (y-u) := by
  have h := V10B3a.weight_product u (y-u)
  rw [show u + (y-u) = y by ring] at h
  have h' := Real.sqrt_le_sqrt h
  have hc : 0 ≤ 2 / Real.log 2 := by
    exact div_nonneg (by norm_num) (Real.log_pos (by norm_num)).le
  have hu := (V10B3a.weight_pos u).le
  unfold rootWeight weightConstant
  rw [Real.sqrt_mul (mul_nonneg hc hu), Real.sqrt_mul hc] at h'
  exact h'

noncomputable def weightedNorm (F : ℝ → ℂ) (y : ℝ) : ℝ≥0∞ :=
  ENNReal.ofReal (rootWeight y * ‖F y‖)

noncomputable def weightedKernel (K : ℝ → ℂ) (u : ℝ) : ℝ≥0∞ :=
  ENNReal.ofReal (weightConstant * rootWeight u * ‖K u‖)

theorem weightedNorm_measurable (F : ℝ → ℂ) (hF : Measurable F) :
    Measurable (weightedNorm F) := by
  unfold weightedNorm
  exact (rootWeight_continuous.measurable.mul hF.norm).ennreal_ofReal

theorem weightedKernel_measurable (K : ℝ → ℂ) (hK : Measurable K) :
    Measurable (weightedKernel K) := by
  unfold weightedKernel
  exact ((measurable_const.mul rootWeight_continuous.measurable).mul hK.norm).ennreal_ofReal

theorem weightedNorm_translate (F : ℝ → ℂ) (u : ℝ) :
    (∫⁻ y, weightedNorm F (y-u) ^ (2 : ℝ)) =
      ∫⁻ y, weightedNorm F y ^ (2 : ℝ) := by
  exact lintegral_sub_right_eq_self (μ := volume)
    (fun y => weightedNorm F y ^ (2 : ℝ)) u

theorem weighted_integrand_bound (K F : ℝ → ℂ) (y u : ℝ) :
    ENNReal.ofReal (rootWeight y * ‖K u * F (y-u)‖) ≤
      weightedKernel K u * weightedNorm F (y-u) := by
  unfold weightedKernel weightedNorm
  have hk : 0 ≤ weightConstant * rootWeight u * ‖K u‖ :=
    mul_nonneg (mul_nonneg weightConstant_nonneg (rootWeight_nonneg u)) (norm_nonneg _)
  rw [← ENNReal.ofReal_mul hk]
  apply ENNReal.ofReal_le_ofReal
  rw [norm_mul]
  calc
    rootWeight y * (‖K u‖ * ‖F (y-u)‖) ≤
        (weightConstant * rootWeight u * rootWeight (y-u)) *
          (‖K u‖ * ‖F (y-u)‖) :=
      mul_le_mul_of_nonneg_right (rootWeight_split y u) (by positivity)
    _ = _ := by ring

theorem weighted_convolution_receiver (K F G : ℝ → ℂ)
    (hK : Measurable K) (hF : Measurable F)
    (hdom : ∀ y, weightedNorm G y ≤
      ∫⁻ u, ENNReal.ofReal (rootWeight y * ‖K u * F (y-u)‖)) :
    (∫⁻ y, weightedNorm G y ^ (2 : ℝ)) ≤
      (∫⁻ u, weightedKernel K u) ^ (2 : ℝ) *
        (∫⁻ y, weightedNorm F y ^ (2 : ℝ)) := by
  apply V10B3b.dominated_convolution_square
    (weightedNorm G) (weightedKernel K) (weightedNorm F)
    (weightedKernel_measurable K hK) (weightedNorm_measurable F hF)
    (weightedNorm_translate F)
  intro y
  exact (hdom y).trans (lintegral_mono (weighted_integrand_bound K F y))

end WeilDefect.MasterRecon.V10B3c

#print axioms WeilDefect.MasterRecon.V10B3c.weightConstant_nonneg
#print axioms WeilDefect.MasterRecon.V10B3c.rootWeight_nonneg
#print axioms WeilDefect.MasterRecon.V10B3c.rootWeight_continuous
#print axioms WeilDefect.MasterRecon.V10B3c.rootWeight_split
#print axioms WeilDefect.MasterRecon.V10B3c.weightedNorm_measurable
#print axioms WeilDefect.MasterRecon.V10B3c.weightedKernel_measurable
#print axioms WeilDefect.MasterRecon.V10B3c.weightedNorm_translate
#print axioms WeilDefect.MasterRecon.V10B3c.weighted_integrand_bound
#print axioms WeilDefect.MasterRecon.V10B3c.weighted_convolution_receiver
