import WeilDefect.Morphology.NeutralLogMetricTimeActionLimit
import Mathlib.MeasureTheory.Function.UniformIntegrable

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology
open scoped FourierTransform ENNReal

/-- Under the full weighted-product L2 domain condition, the Fourier
 transforms of the actual cutoff actions converge in spectral L2.
 The domain condition is retained, not inferred from form energy. -/
theorem neutralLogMetricTimeAction_fourier_tendsto_L2
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    Tendsto (fun n : ℕ => eLpNorm (fun ξ : ℝ =>
      (𝓕 (fun x : ℝ => v x +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ -
      (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume)
      atTop (𝓝 0) := by
  let A : ℕ → ℝ → ℂ := fun n => 𝓕 (fun x : ℝ => v x +
    ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))
  let G : ℝ → ℂ := fun ξ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)
  have hAmeas (n : ℕ) : AEStronglyMeasurable (A n) volume := by
    have hc : Continuous (A n) :=
      VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar
        (innerSL ℝ).continuous₂
        (neutralLogMetricTimeAction_integrable
          (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound)
    exact hc.aestronglyMeasurable
  have hGnorm (ξ : ℝ) : ‖G ξ‖ = ‖(𝓕 v) ξ‖ * logarithmicFourierWeight ξ := by
    have hw : 0 ≤ logarithmicFourierWeight ξ := by
      linarith [one_le_logarithmicFourierWeight ξ]
    dsimp only [G]
    rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hw]
  have hAbound (n : ℕ) (ξ : ℝ) : ‖A n ξ‖ ≤ ‖G ξ‖ := by
    rw [hGnorm]
    exact neutralLogMetricTimeAction_fourier_norm_le
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M ξ (by positivity) hM v hv hvi hbound
  have hui : UnifIntegrable A 2 volume := by
    apply (unifIntegrable_const (ι := ℕ) (by norm_num : (1 : ℝ≥0∞) ≤ 2)
      (by norm_num : (2 : ℝ≥0∞) ≠ ∞) hp).ae_mono hAmeas
    intro n
    filter_upwards [] with ξ
    change ‖A n ξ‖ₑ ≤ ‖G ξ‖ₑ
    simp only [← ofReal_norm]
    exact ENNReal.ofReal_le_ofReal (hAbound n ξ)
  have hpoint : ∀ᵐ ξ ∂volume, Tendsto (fun n => A n ξ) atTop (𝓝 (G ξ)) :=
    Filter.Eventually.of_forall (fun ξ =>
      neutralLogMetricTimeAction_fourier_natural_tendsto M ξ hM v hv hvi hbound)
  exact tendsto_Lp_finite_of_tendsto_ae (by norm_num) (by norm_num)
    hAmeas hp hui hpoint

/-- Spectral L2 convergence for actual cap-bounded zero extensions,
 conditional on their full weighted-product L2 membership. -/
theorem neutralLogMetricTimeAction_zeroExtension_fourier_tendsto_L2
    (B M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
      (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    Tendsto (fun n : ℕ => eLpNorm (fun ξ : ℝ =>
      (𝓕 (fun x : ℝ => neutralLogMetricTrialZeroExtension B v x +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (neutralLogMetricTrialZeroExtension B v x - ∫ y : ℝ,
              neutralLogMetricTrialZeroExtension B v y *
                (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ -
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        (logarithmicFourierWeight ξ : ℂ)) 2 volume) atTop (𝓝 0) := by
  exact neutralLogMetricTimeAction_fourier_tendsto_L2 M hM _
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound) hp


/-- Every actual finite-action Fourier transform belongs to spectral
 L2 under the full weighted-product domain condition. -/
theorem neutralLogMetricTimeAction_fourier_memLp_two
    (ε R M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    MemLp (𝓕 (fun x : ℝ => v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) 2 volume := by
  have hc : Continuous (𝓕 (fun x : ℝ => v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) :=
    VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar
      (innerSL ℝ).continuous₂
      (neutralLogMetricTimeAction_integrable ε R M hε hM v hv hvi hbound)
  apply hp.norm.mono' hc.aestronglyMeasurable
  filter_upwards [] with ξ
  have hw : 0 ≤ logarithmicFourierWeight ξ := by
    linarith [one_le_logarithmicFourierWeight ξ]
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hw]
  exact neutralLogMetricTimeAction_fourier_norm_le ε R M ξ hε hM v hv hvi hbound

/-- The actual spectral L2 vectors of the finite-action Fourier
 transforms converge to the full weighted-product representative. -/
theorem neutralLogMetricTimeAction_fourier_toLp_tendsto
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    Tendsto (fun n : ℕ =>
      (neutralLogMetricTimeAction_fourier_memLp_two
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound hp).toLp
      (𝓕 (fun x : ℝ => v x +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))))
      atTop (𝓝 (hp.toLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)))) := by
  let : Fact ((1 : ℝ≥0∞) ≤ 2) := ⟨by norm_num⟩
  apply (Lp.tendsto_Lp_iff_tendsto_eLpNorm'' _ _ _ _).mpr
  exact neutralLogMetricTimeAction_fourier_tendsto_L2 M hM v hv hvi hbound hp

end
end WeilDefect
