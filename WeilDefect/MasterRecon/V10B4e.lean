import WeilDefect.MasterRecon.V10B3c
import WeilDefect.MasterRecon.V10B4d
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

/-! V10B4e: actual Fourier product energy in cycles frequency.
The weight in this receiver is log(2+|u|); the comparison with the
carrier's log(2+2π|u|) and Mellin derivative identification are separate. -/
namespace WeilDefect.MasterRecon.V10B4e

open Set MeasureTheory
open scoped FourierTransform ENNReal ContDiff

theorem convolution_pointwise (K F G : ℝ → ℂ)
    (hG : ∀ y, G y = ∫ u, K u * F (y-u)) (y : ℝ) :
    V10B3c.weightedNorm G y ≤
      ∫⁻ u, ENNReal.ofReal (V10B3c.rootWeight y * ‖K u * F (y-u)‖) := by
  let c : ℝ := V10B3c.rootWeight y
  have hc : 0 ≤ c := V10B3c.rootWeight_nonneg y
  unfold V10B3c.weightedNorm
  change ENNReal.ofReal (c * ‖G y‖) ≤ _
  rw [hG y]
  calc
    ENNReal.ofReal (c * ‖∫ u, K u * F (y-u)‖) =
        ‖∫ u, (c : ℂ) * (K u * F (y-u))‖ₑ := by
      rw [integral_const_mul, ← ofReal_norm, norm_mul,
        Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hc]
    _ ≤ ∫⁻ u, ‖(c : ℂ) * (K u * F (y-u))‖ₑ :=
      enorm_integral_le_lintegral_enorm _
    _ = _ := by
      apply lintegral_congr
      intro u
      rw [← ofReal_norm, norm_mul, Complex.norm_real,
        Real.norm_eq_abs, abs_of_nonneg hc]

theorem fourier_product_energy (p f : ℝ → ℂ)
    (hp : Integrable p) (hpc : Continuous p) (hK : Integrable (𝓕 p))
    (hf : Integrable f) :
    (∫⁻ y, V10B3c.weightedNorm (𝓕 (fun x => p x * f x)) y ^ (2 : ℝ)) ≤
      (∫⁻ u, V10B3c.weightedKernel (𝓕 p) u) ^ (2 : ℝ) *
        (∫⁻ y, V10B3c.weightedNorm (𝓕 f) y ^ (2 : ℝ)) := by
  apply V10B3c.weighted_convolution_receiver (𝓕 p) (𝓕 f)
    (𝓕 (fun x => p x * f x))
    (V08H.classical_fourier_continuous p hp).measurable
    (V08H.classical_fourier_continuous f hf).measurable
  exact convolution_pointwise _ _ _ (V10B4a.fourier_product p f hp hpc hK hf)

theorem multiplier_slice_smooth (t : ℝ) (ht : 0 ≤ t) (j : ℕ) (s : ℝ) :
    ContDiff ℝ ∞ (fun x => V10B4d.multiplier t ht j (s,x)) :=
  (V10B4d.multiplier_smooth t ht j).comp (contDiff_const.prodMk contDiff_id)

theorem multiplier_first_integrable (t : ℝ) (ht : 0 ≤ t) (j : ℕ) (s : ℝ) :
    Integrable (deriv (fun x => V10B4d.multiplier t ht j (s,x))) := by
  have hs : HasCompactSupport (fun x => V10B4d.multiplier t ht j (s,x)) :=
    (isCompact_closedBall (0:ℝ) (t+2)).of_isClosed_subset
      isClosed_closure (V10B4d.multiplier_support t ht j s)
  exact ((multiplier_slice_smooth t ht j s).continuous_deriv (by simp)).integrable_of_hasCompactSupport hs.deriv

theorem multiplier_uniform_kernel_decay (t : ℝ) (ht : 0 ≤ t) (j : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ s ∈ Icc (-(1/2):ℝ) (1/2),
      ∀ u : ℝ, ‖𝓕 (fun x => V10B4d.multiplier t ht j (s,x)) u‖ ≤ C/(1+u^2) := by
  obtain ⟨A,hA,hA'⟩ := V10B4d.multiplier_uniform_L1 t ht j
  obtain ⟨B,hB,hB'⟩ := V10B4d.multiplier_uniform_second_L1 t ht j
  refine ⟨A+B/(2*Real.pi)^2, by positivity, ?_⟩
  intro s hs u
  let p : ℝ → ℂ := fun x => V10B4d.multiplier t ht j (s,x)
  have hp : ContDiff ℝ ∞ p := multiplier_slice_smooth t ht j s
  exact V10B4b.fourier_quadratic_decay p (hA' s hs).1
    (multiplier_first_integrable t ht j s) (hB' s hs).1
    (hp.differentiable (by simp))
    ((hp.of_le (show (2 : ℕ∞ω) ≤ (⊤ : ℕ∞ω) by simp)).differentiable_deriv_two)
    A B (hA' s hs).2 (hB' s hs).2 u

theorem kernel_integrable_of_decay (K : ℝ → ℂ) (hK : Measurable K)
    (C : ℝ) (hC : 0 ≤ C) (hbound : ∀ u, ‖K u‖ ≤ C/(1+u^2)) :
    Integrable K := by
  apply (integrable_inv_one_add_sq.const_mul C).mono' hK.aestronglyMeasurable
  filter_upwards with u
  simpa only [div_eq_mul_inv] using hbound u

theorem weighted_kernel_mass_of_decay (K : ℝ → ℂ) (hK : Measurable K)
    (C : ℝ) (hC : 0 ≤ C) (hbound : ∀ u, ‖K u‖ ≤ C/(1+u^2)) :
    (∫⁻ u, V10B3c.weightedKernel K u) ≤
      ENNReal.ofReal (V10B3c.weightConstant * C * ∫ u, V10B4c.majorant 1 u) := by
  let g : ℝ → ℝ := fun u => Real.sqrt (Real.log (2+1*|u|)) * ‖K u‖
  have hg : Integrable g := V10B4c.weighted_kernel_integrable K hK 1 C (by norm_num) hC hbound
  have hh := V10B4c.weighted_kernel_mass_bound K hK 1 C (by norm_num) hC hbound
  change (∫ u, g u) ≤ _ at hh
  have hi : Integrable (fun u => V10B3c.weightConstant * g u) :=
    hg.const_mul _
  calc
    (∫⁻ u, V10B3c.weightedKernel K u) =
        ENNReal.ofReal (∫ u, V10B3c.weightConstant * g u) := by
      rw [ofReal_integral_eq_lintegral_ofReal hi]
      · apply lintegral_congr
        intro u
        unfold V10B3c.weightedKernel V10B3c.rootWeight V10B3a.weight g
        congr 1
        rw [one_mul, mul_assoc]
      · exact ae_of_all _ fun u => mul_nonneg V10B3c.weightConstant_nonneg (by dsimp [g]; positivity)
    _ ≤ _ := by
      rw [integral_const_mul, mul_assoc]
      exact ENNReal.ofReal_le_ofReal (mul_le_mul_of_nonneg_left hh V10B3c.weightConstant_nonneg)

theorem uniform_multiplier_energy (t : ℝ) (ht : 0 ≤ t) (j : ℕ) :
    ∃ D : ℝ≥0∞, D ≠ ⊤ ∧ ∀ s ∈ Icc (-(1/2):ℝ) (1/2),
      ∀ f : ℝ → ℂ, Integrable f →
      (∫⁻ y, V10B3c.weightedNorm
        (𝓕 (fun x => V10B4d.multiplier t ht j (s,x) * f x)) y ^ (2 : ℝ)) ≤
        D * (∫⁻ y, V10B3c.weightedNorm (𝓕 f) y ^ (2 : ℝ)) := by
  obtain ⟨C,hC,hbound⟩ := multiplier_uniform_kernel_decay t ht j
  obtain ⟨A,hA,hphys⟩ := V10B4d.multiplier_uniform_L1 t ht j
  let M := ENNReal.ofReal (V10B3c.weightConstant * C * ∫ u, V10B4c.majorant 1 u)
  refine ⟨M ^ (2 : ℝ), ?_, ?_⟩
  · rw [show (2:ℝ) = ((2:ℕ):ℝ) by norm_num, ENNReal.rpow_natCast]
    exact ENNReal.pow_ne_top ENNReal.ofReal_ne_top
  intro s hs f hf
  let p : ℝ → ℂ := fun x => V10B4d.multiplier t ht j (s,x)
  have hp := (hphys s hs).1
  have hk := (V08H.classical_fourier_continuous p hp).measurable
  have hki := kernel_integrable_of_decay (𝓕 p) hk C hC (hbound s hs)
  have hmass := weighted_kernel_mass_of_decay (𝓕 p) hk C hC (hbound s hs)
  refine (fourier_product_energy p f hp
    (multiplier_slice_smooth t ht j s).continuous hki hf).trans ?_
  exact mul_le_mul_of_nonneg_right (ENNReal.rpow_le_rpow hmass (by norm_num)) (zero_le _)

end WeilDefect.MasterRecon.V10B4e

#print axioms WeilDefect.MasterRecon.V10B4e.convolution_pointwise
#print axioms WeilDefect.MasterRecon.V10B4e.fourier_product_energy
#print axioms WeilDefect.MasterRecon.V10B4e.multiplier_slice_smooth
#print axioms WeilDefect.MasterRecon.V10B4e.multiplier_first_integrable
#print axioms WeilDefect.MasterRecon.V10B4e.multiplier_uniform_kernel_decay
#print axioms WeilDefect.MasterRecon.V10B4e.kernel_integrable_of_decay
#print axioms WeilDefect.MasterRecon.V10B4e.weighted_kernel_mass_of_decay
#print axioms WeilDefect.MasterRecon.V10B4e.uniform_multiplier_energy
