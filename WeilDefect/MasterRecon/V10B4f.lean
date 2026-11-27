import WeilDefect.MasterRecon.V10B4e
import WeilDefect.MasterRecon.V09B
import WeilDefect.MasterRecon.V08K

/-! V10B4f: literal Mellin moment and carrier attachment.
All support conditions are almost everywhere. No zero count is used. -/
namespace WeilDefect.MasterRecon.V10B4f

open Set MeasureTheory Filter
open scoped FourierTransform ENNReal ContDiff

noncomputable def momentInput (f : ℝ → ℂ) (j : ℕ) (x : ℝ) : ℂ :=
  (x : ℂ)^j * f x

theorem momentInput_support (t : ℝ) (f : ℝ → ℂ) (j : ℕ)
    (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0) :
    ∀ᵐ x ∂volume, x ∉ Icc (-t) t → momentInput f j x = 0 := by
  filter_upwards [hs] with x hx
  intro ho
  simp [momentInput, hx ho]

theorem momentInput_integrable (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hf : Integrable f) (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0)
    (j : ℕ) : Integrable (momentInput f j) := by
  apply (hf.norm.const_mul (t^j)).mono'
  · exact (show Continuous (fun x : ℝ => (x : ℂ)^j) by fun_prop).aestronglyMeasurable.mul hf.aestronglyMeasurable
  · filter_upwards [hs] with x hx
    by_cases hm : x ∈ Icc (-t) t
    · rw [momentInput, norm_mul, norm_pow, Complex.norm_real, Real.norm_eq_abs]
      exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (abs_nonneg x) (abs_le.mpr hm) j) (norm_nonneg _)
    · simp [momentInput, hx hm]

theorem moment_derivative (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hf : Integrable f) (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0)
    (j : ℕ) (z : ℂ) :
    HasDerivAt (V07A.mellin (momentInput f j))
      (V07A.mellin (momentInput f (j+1)) z) z := by
  have h := V09B.mellin_hasDerivAt t ht (momentInput f j)
    (momentInput_integrable t ht f hf hs j) (momentInput_support t f j hs) z
  convert h using 1
  unfold V07A.mellin
  apply integral_congr_ae
  filter_upwards with x
  unfold momentInput
  rw [pow_succ]
  ring

theorem mellin_moment_fourier (t : ℝ) (ht : 0 ≤ t) (f : ℝ → ℂ)
    (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0)
    (j : ℕ) (s u : ℝ) :
    V07A.mellin (momentInput f j) ((s : ℂ) - (2*Real.pi*u : ℝ) * Complex.I) =
      𝓕 (fun x => V10B4d.multiplier t ht j (s,x) * f x) u := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  unfold V07A.mellin
  simp only [smul_eq_mul]
  apply integral_congr_ae
  filter_upwards [hs] with x hx
  by_cases hm : x ∈ Icc (-t) t
  · rw [V10B4d.multiplier_on_support t ht j s x hm]
    unfold momentInput
    have he : ((s : ℂ) - (2*Real.pi*u : ℝ) * Complex.I) * (x : ℂ) =
        ↑(-2 * Real.pi * x * u) * Complex.I + ↑(s*x) := by
      push_cast
      ring
    rw [he, Complex.exp_add]
    ring
  · simp [momentInput, hx hm]

theorem weight_le_carrier (u : ℝ) :
    V10B3a.weight u ≤ V08I.logWeight u := by
  unfold V10B3a.weight V08I.logWeight
  apply Real.log_le_log (by positivity)
  rw [abs_mul, abs_of_nonneg (by positivity : 0 ≤ 2*Real.pi)]
  have h : 1 ≤ 2*Real.pi := by linarith [Real.pi_gt_three]
  nlinarith [abs_nonneg u, mul_nonneg (sub_nonneg.mpr h) (abs_nonneg u)]

theorem carrier_le_weight (u : ℝ) :
    V08I.logWeight u ≤ (1 + Real.log (2*Real.pi)/Real.log 2) * V10B3a.weight u := by
  have hc : 0 < 2*Real.pi := by positivity
  have hc1 : 1 ≤ 2*Real.pi := by linarith [Real.pi_gt_three]
  have hl : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hlog : 0 ≤ Real.log (2*Real.pi) := Real.log_nonneg hc1
  have hratio : 0 ≤ Real.log (2*Real.pi)/Real.log 2 := div_nonneg hlog hl.le
  calc
    V08I.logWeight u ≤ Real.log ((2*Real.pi)*(2+|u|)) := by
      unfold V08I.logWeight
      apply Real.log_le_log (by positivity)
      rw [abs_mul, abs_of_pos hc]
      linarith
    _ = Real.log (2*Real.pi) + V10B3a.weight u := by
      rw [Real.log_mul hc.ne' (by positivity : 2+|u| ≠ 0)]
      rfl
    _ ≤ (1 + Real.log (2*Real.pi)/Real.log 2) * V10B3a.weight u := by
      have hm := mul_le_mul_of_nonneg_left (V10B3a.weight_lower u) hratio
      have he : Real.log (2*Real.pi)/Real.log 2 * Real.log 2 = Real.log (2*Real.pi) :=
        div_mul_cancel₀ _ hl.ne'
      rw [he] at hm
      linarith

theorem weightedNorm_square (F : ℝ → ℂ) (u : ℝ) :
    V10B3c.weightedNorm F u ^ (2 : ℝ) =
      ENNReal.ofReal (V10B3a.weight u * ‖F u‖^2) := by
  unfold V10B3c.weightedNorm
  rw [ENNReal.ofReal_rpow_of_nonneg
    (mul_nonneg (V10B3c.rootWeight_nonneg u) (norm_nonneg _)) (by norm_num)]
  rw [show (2:ℝ) = ((2:ℕ):ℝ) by norm_num, Real.rpow_natCast, mul_pow]
  unfold V10B3c.rootWeight
  rw [Real.sq_sqrt (V10B3a.weight_pos u).le]

theorem carrier_fourier_energy (t : ℝ) (g : V08I.logCarrier t) :
    (∫⁻ u, V10B3c.weightedNorm (𝓕 (V08I.physicalInclusion t g : ℝ → ℂ)) u ^ (2 : ℝ)) ≤
      ENNReal.ofReal (‖g‖^2) := by
  let f := V08I.physicalInclusion t g
  have hf := V08K.supported_integrable t f (V08I.physicalInclusion_support t g)
  have ha := V08H.l2_fourier_integral_ae f hf
  have hi := V08I.logCarrier_energy_integrable t g
  rw [V08I.logCarrier_energy t g, ofReal_integral_eq_lintegral_ofReal hi
    (ae_of_all _ fun u => mul_nonneg (V08I.logWeight_pos u).le (sq_nonneg _))]
  apply lintegral_mono_ae
  filter_upwards [ha] with u hu
  rw [weightedNorm_square, hu]
  exact ENNReal.ofReal_le_ofReal (mul_le_mul_of_nonneg_right (weight_le_carrier u) (sq_nonneg _))

theorem carrier_multiplier_energy (t : ℝ) (ht : 0 ≤ t) (j : ℕ) :
    ∃ D : ℝ≥0∞, D ≠ ⊤ ∧ ∀ s ∈ Icc (-(1/2):ℝ) (1/2),
      ∀ g : V08I.logCarrier t,
      (∫⁻ u, V10B3c.weightedNorm
        (fun u => V07A.mellin (momentInput (V08I.physicalInclusion t g : ℝ → ℂ) j)
          ((s : ℂ) - (2*Real.pi*u : ℝ) * Complex.I)) u ^ (2 : ℝ)) ≤
        D * ENNReal.ofReal (‖g‖^2) := by
  obtain ⟨D,hD,hall⟩ := V10B4e.uniform_multiplier_energy t ht j
  refine ⟨D,hD,?_⟩
  intro s hs g
  let f := V08I.physicalInclusion t g
  have hf := V08K.supported_integrable t f (V08I.physicalInclusion_support t g)
  have he : (fun u : ℝ => V07A.mellin (momentInput (f : ℝ → ℂ) j)
      ((s : ℂ) - (2*Real.pi*u : ℝ) * Complex.I)) =
      𝓕 (fun x => V10B4d.multiplier t ht j (s,x) * f x) :=
    funext (mellin_moment_fourier t ht _ (V08I.physicalInclusion_support t g) j s)
  rw [he]
  exact (hall s hs (f : ℝ → ℂ) hf).trans
    (mul_le_mul_of_nonneg_left (carrier_fourier_energy t g) hD)

end WeilDefect.MasterRecon.V10B4f

#print axioms WeilDefect.MasterRecon.V10B4f.momentInput_support
#print axioms WeilDefect.MasterRecon.V10B4f.momentInput_integrable
#print axioms WeilDefect.MasterRecon.V10B4f.moment_derivative
#print axioms WeilDefect.MasterRecon.V10B4f.mellin_moment_fourier
#print axioms WeilDefect.MasterRecon.V10B4f.weight_le_carrier
#print axioms WeilDefect.MasterRecon.V10B4f.carrier_le_weight
#print axioms WeilDefect.MasterRecon.V10B4f.weightedNorm_square
#print axioms WeilDefect.MasterRecon.V10B4f.carrier_fourier_energy
#print axioms WeilDefect.MasterRecon.V10B4f.carrier_multiplier_energy
