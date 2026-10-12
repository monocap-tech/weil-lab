import WeilDefect.Morphology.NeutralLogMetricTimeActionLimit
import Mathlib.MeasureTheory.Function.UniformIntegrable

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology FourierTransform
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
  let D : ℕ → ℝ → ℝ := fun n ξ => ‖A n ξ - G ξ‖ ^ 2
  have hDmeas (n : ℕ) : AEStronglyMeasurable (D n) volume := by
    have hm := ((hAmeas n).sub hp.aestronglyMeasurable).norm
    have hm2 := hm.mul hm
    change AEStronglyMeasurable (fun ξ : ℝ =>
      ‖A n ξ - G ξ‖ * ‖A n ξ - G ξ‖) volume at hm2
    simpa only [D, pow_two] using hm2
  have hdom : Integrable (fun ξ : ℝ => 4 * ‖G ξ‖ ^ 2) volume :=
    hp.norm.integrable_sq.const_mul 4
  have hDdom (n : ℕ) : ∀ᵐ ξ ∂volume, ‖D n ξ‖ ≤ 4 * ‖G ξ‖ ^ 2 := by
    filter_upwards [] with ξ
    have hd : ‖A n ξ - G ξ‖ ≤ 2 * ‖G ξ‖ :=
      (norm_sub_le _ _).trans (by linarith [hAbound n ξ])
    dsimp only [D]
    rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _)]
    nlinarith [norm_nonneg (A n ξ - G ξ), norm_nonneg (G ξ)]
  have hDpoint : ∀ᵐ ξ ∂volume, Tendsto (fun n => D n ξ) atTop (𝓝 (0 : ℝ)) := by
    filter_upwards [] with ξ
    have h := neutralLogMetricTimeAction_fourier_natural_tendsto M ξ hM v hv hvi hbound
    change Tendsto (fun n => A n ξ) atTop (𝓝 (G ξ)) at h
    have hd := (h.sub (tendsto_const_nhds :
      Tendsto (fun _ : ℕ => G ξ) atTop (𝓝 (G ξ)))).norm
    simpa only [D, Function.comp_def, sub_self, norm_zero, zero_pow (by norm_num : (2 : ℕ) ≠ 0)]
      using hd.pow 2
  have ht := tendsto_lintegral_norm_of_dominated_convergence
    hDmeas hdom.2 hDdom hDpoint
  have ht' : Tendsto (fun n : ℕ => ∫⁻ ξ : ℝ,
      ENNReal.ofReal (‖A n ξ - G ξ‖ ^ 2)) atTop (𝓝 (0 : ℝ≥0∞)) := by
    have hn (n : ℕ) (ξ : ℝ) : ‖‖A n ξ - G ξ‖ ^ 2‖ = ‖A n ξ - G ξ‖ ^ 2 := by
      exact Real.norm_of_nonneg (sq_nonneg _)
    simpa only [D, sub_zero, hn] using ht
  have he (n : ℕ) : eLpNorm (fun ξ : ℝ => A n ξ - G ξ) 2 volume =
      (∫⁻ ξ : ℝ, ENNReal.ofReal (‖A n ξ - G ξ‖ ^ 2)) ^ (1 / (2 : ℝ)) := by
    rw [eLpNorm_eq_lintegral_rpow_enorm_toReal (by norm_num) (by norm_num)
      (show AEStronglyMeasurable (fun ξ : ℝ => A n ξ - G ξ) volume from by
        exact (hAmeas n).sub hp.aestronglyMeasurable)]
    simp only [ENNReal.toReal_ofNat]
    congr 1
    apply lintegral_congr_ae
    filter_upwards [] with ξ
    rw [← ofReal_norm, pow_two, pow_two]
    exact (ENNReal.ofReal_mul (norm_nonneg _)).symm
  have hc : Continuous (fun z : ℝ≥0∞ => z ^ (1 / (2 : ℝ))) :=
    ENNReal.continuous_rpow_const
  change Tendsto (fun n : ℕ => eLpNorm (fun ξ : ℝ => A n ξ - G ξ) 2 volume)
    atTop (𝓝 (0 : ℝ≥0∞))
  simp_rw [he]
  simpa only [Function.comp_def, ENNReal.zero_rpow_of_pos (by norm_num : 0 < 1 / (2 : ℝ))] using
    (hc.tendsto 0).comp ht'

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

set_option maxHeartbeats 1000000 in
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


set_option maxHeartbeats 1000000 in
/-- Inverse Fourier transformation transports the actual spectral-vector
 limit into physical L2. Identification with the original time-action
 functions is a separate obligation. -/
theorem neutralLogMetricTimeAction_fourierInv_toLp_tendsto
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    Tendsto (fun n : ℕ => (𝓕⁻
      ((neutralLogMetricTimeAction_fourier_memLp_two
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound hp).toLp
      (𝓕 (fun x : ℝ => v x +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))))) :
        RealComplexL2))
      atTop (𝓝 (𝓕⁻ (hp.toLp
        (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ))) : RealComplexL2)) := by
  have hc : Continuous (fun u : RealComplexL2 => (𝓕⁻ u : RealComplexL2)) :=
    continuous_fourierInv
  exact (hc.tendsto _).comp
    (neutralLogMetricTimeAction_fourier_toLp_tendsto M hM v hv hvi hbound hp)

set_option maxHeartbeats 1000000 in
/-- Pairings of the inverse-transformed spectral representatives
 converge against every physical L2 test vector. The full weighted-product
 domain condition remains explicit. -/
theorem neutralLogMetricTimeAction_fourierInv_inner_tendsto
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume)
    (φ : RealComplexL2) :
    Tendsto (fun n : ℕ => inner ℂ (𝓕⁻
      ((neutralLogMetricTimeAction_fourier_memLp_two
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound hp).toLp
      (𝓕 (fun x : ℝ => v x +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))))) φ)
      atTop (𝓝 (inner ℂ (𝓕⁻ (hp.toLp
        (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)))) φ)) := by
  have hc : Continuous (fun u : RealComplexL2 => inner ℂ u φ) :=
    continuous_id.inner (𝕜 := ℂ) continuous_const
  exact (hc.tendsto _).comp
    (neutralLogMetricTimeAction_fourierInv_toLp_tendsto M hM v hv hvi hbound hp)

end
end WeilDefect
