import WeilDefect.Arithmetic.ActualZetaIV102OriginalSchwartzMetricTransport
import WeilDefect.Arithmetic.ActualZetaArchimedeanTransport
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory InnerProductSpace FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- Exact original mixed correlation, with unchanged window and input vectors. -/
def neutralIV103Correlation (a : ℝ) (u v : 𝓢(ℝ,ℂ)) : ℝ → ℂ :=
  neutralWindowCorrelation a (u.toLp 2 volume) (v.toLp 2 volume)

def neutralIV103Spectrum (u v : 𝓢(ℝ,ℂ)) (ξ : ℝ) : ℂ :=
  conj ((𝓕 (u.toLp 2 volume) : RealComplexL2) ξ) *
    (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ

/-- No Green synthesis needed for this pointwise evaluation dictionary. -/
theorem neutralIV103Evaluation_fourier (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) (ξ : ℝ) :
    neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) (s.toLp 2 volume) =
      (𝓕 s : 𝓢(ℝ,ℂ)) ξ := by
  rw [neutralNF573WindowEvaluation_eq_raw_of_ae a _ _
    (neutralIV006Schwartz_window_ae a s hs), ← neutralRawTransform_fourier,
    ← SchwartzMap.fourier_coe]

/-- Exact real-frequency raw transform on the genuine physical L² pair. -/
theorem neutralIV103Raw_spectrum_ae (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    (fun ξ : ℝ => neutralRawTransform (neutralIV103Correlation a u v)
      ((-2 * Real.pi * ξ : ℝ) : ℂ)) =ᵐ[volume] neutralIV103Spectrum u v := by
  unfold neutralIV103Correlation neutralIV103Spectrum
  rw [SchwartzMap.toLp_fourier_eq u, SchwartzMap.toLp_fourier_eq v]
  filter_upwards [((𝓕 u : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume),
    ((𝓕 v : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume)] with ξ hξu hξv
  rw [neutralWindowCorrelation_rawTransform, Complex.conj_ofReal,
    neutralIV103Evaluation_fourier a u hu, neutralIV103Evaluation_fourier a v hv,
    hξu, hξv]

/-- Full Gamma term, with exactly the original normalization and sign. -/
theorem neutralIV103Arch_spectral (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    (1 / (2 * Real.pi) : ℂ) * (∫ r : ℝ,
      Zeta23.paperFT (neutralIV103Correlation a u v) (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ)) =
      ∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
        neutralIV103Spectrum u v ξ := by
  let F : ℝ → ℂ := fun r => Zeta23.paperFT (neutralIV103Correlation a u v)
    (r : ℂ) * (Zeta23.EF.gammaBracket r : ℂ)
  have h := Measure.integral_comp_mul_left F (-2 * Real.pi)
  have habs : |(-2 * Real.pi)⁻¹| = 1 / (2 * Real.pi) := by
    rw [show -2 * Real.pi = -(2 * Real.pi) by ring,
      inv_neg, abs_neg, abs_of_pos (inv_pos.mpr (by positivity))]
    simp only [one_div]
  rw [habs, Complex.real_smul] at h
  have he : (∫ ξ : ℝ, F ((-2 * Real.pi) * ξ)) =
      ∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
        neutralIV103Spectrum u v ξ := by
    apply integral_congr_ae
    filter_upwards [neutralIV103Raw_spectrum_ae a u v hu hv] with ξ hξ
    dsimp only [F]
    rw [← neutralRawTransform_eq_paperFT, hξ, neutralActualZetaGammaBracket_mathlib]
    exact mul_comm _ _
  have hc : (1 / (2 * Real.pi) : ℂ) = ((1 / (2 * Real.pi) : ℝ) : ℂ) := by
    push_cast
    rfl
  change (1 / (2 * Real.pi) : ℂ) * (∫ r : ℝ, F r) = _
  rw [hc]
  exact h.symm.trans he

/-- Both pole interactions transfer to the existing native carrier operator. -/
theorem neutralIV103Pole_operator (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    Zeta23.paperFT (neutralIV103Correlation a u v) (Complex.I / 2) +
      Zeta23.paperFT (neutralIV103Correlation a u v) (-Complex.I / 2) =
      inner ℂ (neutralIV102Lift a u hu)
        (neutralLogPoleOperator a (neutralIV102Lift a v hv)) := by
  have h := neutralLogHilbertCorrelation_poleOperator a
    (neutralIV102Lift a u hu) (neutralIV102Lift a v hv)
  rw [neutralIV102Lift_physical, neutralIV102Lift_physical] at h
  unfold neutralIV103Correlation
  rw [← neutralRawTransform_eq_paperFT, ← neutralRawTransform_eq_paperFT]
  convert h using 2 <;> push_cast <;> ring

/-- Original correlation regularity and both L1 conditions for inversion. -/
theorem neutralIV103Correlation_data (a : ℝ) (ha : 0 ≤ a) (u v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    ContDiff ℝ 2 (neutralIV103Correlation a u v) ∧
      Integrable (neutralIV103Correlation a u v) ∧
      Integrable (𝓕 (neutralIV103Correlation a u v)) := by
  have hk : ContDiff ℝ 2 (neutralIV103Correlation a u v) :=
    neutralWindowCorrelation_contDiff_of_ae_smoothSecond a
      (u.toLp 2 volume) (v.toLp 2 volume) (fun x => v x)
      (v.smooth 2) (neutralIV008SchwartzWindow_hasCompactSupport a v hv)
      (neutralIV006Schwartz_window_ae a v hv)
  exact ⟨hk, neutralWindowCorrelation_integrable a _ _,
    neutralIV082Fourier_integrable_compactC2 _ hk (by linarith)
      (neutralIV087WindowCorrelation_support_abs a _ _)⟩

theorem neutralIV103Spectrum_integrable (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    Integrable (neutralIV103Spectrum u v) := by
  apply (neutralIV103Correlation_data a ha u v hv).2.2.congr
  filter_upwards [neutralIV103Raw_spectrum_ae a u v hu hv] with ξ hξ
  rw [neutralRawTransform_fourier]
  exact hξ

private theorem iv103Phase_integrable (F : ℝ → ℂ) (hF : Integrable F) (t : ℝ) :
    Integrable (fun ξ : ℝ => F ξ *
      Complex.exp (Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ))) := by
  apply hF.mul_bdd (c := 1)
    (show Continuous (fun ξ : ℝ =>
      Complex.exp (Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ))) from by
        fun_prop).aestronglyMeasurable
  filter_upwards [] with ξ
  simp [Complex.norm_exp, Complex.mul_re, Complex.mul_im]

/-- Exact pointwise inversion, not merely an almost-everywhere prime sample. -/
theorem neutralIV103Correlation_inverse (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) (t : ℝ) :
    neutralIV103Correlation a u v t = ∫ ξ : ℝ, neutralIV103Spectrum u v ξ *
      Complex.exp (Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ)) := by
  obtain ⟨hk, hi, hf⟩ := neutralIV103Correlation_data a ha u v hv
  have h := congrFun (hk.continuous.fourierInv_fourier_eq hi hf) t
  rw [← h, Real.fourierInv_eq_fourier_neg, neutralRawTransform_fourier]
  unfold neutralRawTransform
  apply integral_congr_ae
  filter_upwards [neutralIV103Raw_spectrum_ae a u v hu hv] with ξ hξ
  rw [neutralRawTransform_fourier, hξ]
  congr 2
  push_cast
  ring

private theorem iv103Phase_pair (F : ℂ) (t ξ : ℝ) :
    F * Complex.exp (Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ)) +
    F * Complex.exp (Complex.I * ((2 * Real.pi * (-t) : ℝ) : ℂ) * (ξ : ℂ)) =
    F * ((2 : ℂ) * (Real.cos ((2 * Real.pi * ξ) * t) : ℂ)) := by
  have hp : Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ) =
      Complex.I * (((2 * Real.pi * ξ) * t : ℝ) : ℂ) := by push_cast; ring
  have hm : Complex.I * ((2 * Real.pi * (-t) : ℝ) : ℂ) * (ξ : ℂ) =
      Complex.I * ((-((2 * Real.pi * ξ) * t) : ℝ) : ℂ) := by push_cast; ring
  rw [hp, hm, ← mul_add]
  congr 1
  simp only [Complex.ofReal_neg, mul_neg, mul_comm Complex.I]
  rw [Complex.ofReal_cos, Complex.cos]
  ring

theorem neutralIV103PrimeSummand_spectral (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) (n : ℕ) :
    neutralIV085PrimeSummand (neutralIV103Correlation a u v) n =
      ∫ ξ : ℝ, ((compactWindowPrimeCoefficient n *
        Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ) *
        neutralIV103Spectrum u v ξ := by
  have hF := neutralIV103Spectrum_integrable a ha u v hu hv
  unfold neutralIV085PrimeSummand
  rw [neutralIV103Correlation_inverse a ha u v hu hv,
    neutralIV103Correlation_inverse a ha u v hu hv,
    ← integral_add (iv103Phase_integrable _ hF _) (iv103Phase_integrable _ hF _),
    ← integral_const_mul]
  apply integral_congr_ae
  filter_upwards [] with ξ
  rw [iv103Phase_pair]
  unfold compactWindowPrimeCoefficient
  push_cast
  ring

private theorem iv103Prime_integrand (u v : 𝓢(ℝ,ℂ)) (n : ℕ)
    (hF : Integrable (neutralIV103Spectrum u v)) :
    Integrable (fun ξ : ℝ => ((compactWindowPrimeCoefficient n *
      Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ) *
      neutralIV103Spectrum u v ξ) := by
  have h := hF.mul_bdd (c := |compactWindowPrimeCoefficient n|)
    (show Continuous (fun ξ : ℝ => ((compactWindowPrimeCoefficient n *
      Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ)) from by
        fun_prop).aestronglyMeasurable (by
    filter_upwards [] with ξ
    rw [Complex.norm_real, Real.norm_eq_abs, abs_mul]
    simpa using mul_le_mul_of_nonneg_left (Real.abs_cos_le_one _) (abs_nonneg _))
  apply h.congr
  filter_upwards [] with ξ
  exact mul_comm _ _

/-- The original finite right-limit prime-power set, including threshold terms. -/
theorem neutralIV103Prime_finite (a : ℝ) (u v : 𝓢(ℝ,ℂ)) :
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation a u v) n) =
      ∑ n ∈ rightLimitPrimePowerFinset a,
        neutralIV085PrimeSummand (neutralIV103Correlation a u v) n := by
  apply tsum_eq_sum
  intro n hn
  by_cases hpp : IsPrimePow n
  · have hlog : 2 * a < Real.log (n : ℝ) := by
      apply lt_of_not_ge
      intro h
      exact hn ((mem_rightLimitPrimePowerFinset a n).2 ⟨hpp, h⟩)
    exact neutralIV085PrimeSummand_logFar _
      (neutralIV087WindowCorrelation_support_abs a _ _) n hlog
  · exact neutralIV085PrimeSummand_nonPrimePower _ n hpp

theorem neutralIV103Prime_spectral (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation a u v) n) =
      ∫ ξ : ℝ, (rightLimitPrimeSymbol a (2 * Real.pi * ξ) : ℂ) *
        neutralIV103Spectrum u v ξ := by
  rw [neutralIV103Prime_finite]
  simp_rw [neutralIV103PrimeSummand_spectral a ha u v hu hv]
  rw [← integral_finset_sum _ (fun n _ =>
    iv103Prime_integrand u v n (neutralIV103Spectrum_integrable a ha u v hu hv))]
  apply integral_congr_ae
  filter_upwards [] with ξ
  simp only [rightLimitPrimeSymbol, Complex.ofReal_sum, Finset.sum_mul]

/-- Terminal source identity: the full original signed form on all supported
Schwartz pairs, without assuming Green representability or positivity. -/
theorem neutralIV103Mixed_native (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Mixed a u v = inner ℂ (neutralIV102Lift a u hu)
      (neutralActualZetaLogWeilFormOperator a (neutralIV102Lift a v hv)) := by
  let F := neutralIV103Spectrum u v
  have hF := neutralIV103Spectrum_integrable a ha u v hu hv
  have hp := integrable_finset_sum (rightLimitPrimePowerFinset a)
    (fun n _ => iv103Prime_integrand u v n hF)
  have hp' : Integrable (fun ξ : ℝ => (rightLimitPrimeSymbol a (2 * Real.pi * ξ) : ℂ) * F ξ) := by
    apply hp.congr
    filter_upwards [] with ξ
    simp only [F, rightLimitPrimeSymbol, Complex.ofReal_sum, Finset.sum_mul]
  have hm := neutralActualZetaCanonical_mixed_integrable a
    (neutralIV102Canonical a u hu) (neutralIV102Canonical a v hv)
  have hm' : Integrable (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) * F ξ) := by
    apply hm.congr
    filter_upwards [] with ξ
    unfold F neutralIV103Spectrum
    change _ * _ * _ = _
    ring
  have hA : Integrable (fun ξ : ℝ =>
    (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) * F ξ) := by
    apply (hm'.add hp').congr
    filter_upwards [] with ξ
    simp only [Pi.add_apply, rightLimitCompactWeilSymbolMathlib,
      rightLimitCompactWeilSymbol, Complex.ofReal_sub]
    ring
  have hs : (∫ ξ : ℝ, (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) * F ξ) =
      (∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) * F ξ) -
        (∫ ξ : ℝ, (rightLimitPrimeSymbol a (2 * Real.pi * ξ) : ℂ) * F ξ) := by
    rw [← integral_sub hA hp']
    apply integral_congr_ae
    filter_upwards [] with ξ
    simp only [Pi.sub_apply, rightLimitCompactWeilSymbolMathlib,
      rightLimitCompactWeilSymbol, Complex.ofReal_sub, sub_mul]
  rw [neutralActualZetaLogWeilFormOperator_mixed, neutralIV102Lift_physical,
    neutralIV102Lift_physical]
  have hmul : (∫ ξ : ℝ, conj ((𝓕 (u.toLp 2 volume) : RealComplexL2) ξ) *
      (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ) =
      ∫ ξ : ℝ, (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) * F ξ := by
    apply integral_congr_ae
    filter_upwards [] with ξ
    unfold F neutralIV103Spectrum
    ring
  rw [hmul, hs]
  unfold neutralIV101Mixed Zeta23.EF.literatureRHS
  change Zeta23.paperFT (neutralIV103Correlation a u v) (Complex.I / 2) +
    Zeta23.paperFT (neutralIV103Correlation a u v) (-Complex.I / 2) -
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation a u v) n) +
    (1 / (2 * Real.pi) : ℂ) * (∫ r : ℝ,
      Zeta23.paperFT (neutralIV103Correlation a u v) (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ)) = _
  rw [neutralIV103Pole_operator a u v hu hv, neutralIV103Prime_spectral a ha u v hu hv,
    neutralIV103Arch_spectral a u v hu hv]
  dsimp only [F]
  ring


#print axioms neutralIV103Evaluation_fourier
#print axioms neutralIV103Raw_spectrum_ae
#print axioms neutralIV103Arch_spectral
#print axioms neutralIV103Pole_operator

#print axioms neutralIV103Correlation_data
#print axioms neutralIV103Spectrum_integrable
#print axioms neutralIV103Correlation_inverse
#print axioms neutralIV103PrimeSummand_spectral
#print axioms neutralIV103Prime_finite
#print axioms neutralIV103Prime_spectral
#print axioms neutralIV103Mixed_native

end
end WeilDefect
