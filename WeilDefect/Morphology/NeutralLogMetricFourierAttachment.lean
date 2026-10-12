import WeilDefect.Morphology.NeutralLogMetricTimeActionBounds
import WeilDefect.Morphology.NeutralLogMetricSpectralL2
import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import WeilDefect.Morphology.NeutralLogMetricTruncatedLimit
import WeilDefect.Morphology.NeutralCanonicalFormDomain
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology FourierTransform
open scoped FourierTransform SchwartzMap

/-- Ordinary Fourier integrals and L2 Fourier vectors agree for an
 integrable L2 function, using the existing repo's L1/L2 agreement theorem. -/
theorem neutralLogMetricIntegrableL2_fourier_toLp_eq
    (f : ℝ → ℂ) (hfi : Integrable f) (hf : MemLp f 2 volume)
    (hF : MemLp (𝓕 f) 2 volume) :
    (𝓕 (hf.toLp f) : RealComplexL2) = hF.toLp (𝓕 f) := by
  have hi : Integrable (hf.toLp f : ℝ → ℂ) := hfi.congr hf.coeFn_toLp.symm
  have ha := neutralIntegrableL2_fourier_ae (hf.toLp f) hi
  apply Lp.ext
  filter_upwards [ha, hF.coeFn_toLp] with ξ hξ hFξ
  exact (hξ.trans (Real.fourier_congr_ae hf.coeFn_toLp ξ)).trans hFξ.symm

/-- The inverse transform of the ordinary-Fourier L2 representative
 is the actual physical L2 representative, not a separately postulated source. -/
theorem neutralLogMetricIntegrableL2_fourierInv_toLp_eq
    (f : ℝ → ℂ) (hfi : Integrable f) (hf : MemLp f 2 volume)
    (hF : MemLp (𝓕 f) 2 volume) :
    (𝓕⁻ (hF.toLp (𝓕 f)) : RealComplexL2) = hf.toLp f := by
  have h := congrArg (fun u : RealComplexL2 => (𝓕⁻ u : RealComplexL2))
    (neutralLogMetricIntegrableL2_fourier_toLp_eq f hfi hf hF)
  simpa only [fourierInv_fourier_eq] using h.symm

set_option maxHeartbeats 1000000 in
/-- The constructed inverse-transformed finite-action spectral vector
 equals the actual full-line physical action vector, retaining exterior action. -/
theorem neutralLogMetricTimeAction_fourierInv_eq_physical
    (ε R M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    (𝓕⁻ ((neutralLogMetricTimeAction_fourier_memLp_two ε R M hε hM
      v hv hvi hbound hp).toLp
      (𝓕 (fun x : ℝ => v x + ∫ t in Icc ε R,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))))) :
            RealComplexL2) =
      (neutralLogMetricTimeAction_memLp_two ε R M hε hM v hv hvi hbound).toLp
        (fun x : ℝ => v x + ∫ t in Icc ε R,
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) := by
  exact neutralLogMetricIntegrableL2_fourierInv_toLp_eq _
    (neutralLogMetricTimeAction_integrable ε R M hε hM v hv hvi hbound)
    (neutralLogMetricTimeAction_memLp_two ε R M hε hM v hv hvi hbound)
    (neutralLogMetricTimeAction_fourier_memLp_two ε R M hε hM v hv hvi hbound hp)


set_option maxHeartbeats 1000000 in
/-- The actual full-line physical action vectors converge to the inverse
 Fourier transform of the weighted product, under its explicit L2 domain premise. -/
theorem neutralLogMetricTimeAction_physical_toLp_tendsto
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    Tendsto (fun n : ℕ =>
      (neutralLogMetricTimeAction_memLp_two
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound).toLp
        (fun x : ℝ => v x +
          ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
            ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
              (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))))
      atTop (𝓝 (𝓕⁻ (hp.toLp
        (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ))) : RealComplexL2)) := by
  have h := neutralLogMetricTimeAction_fourierInv_toLp_tendsto M hM v hv hvi hbound hp
  simp_rw [neutralLogMetricTimeAction_fourierInv_eq_physical] at h
  exact h

set_option maxHeartbeats 1000000 in
/-- Actual physical-vector pairings converge against every physical L2 test. -/
theorem neutralLogMetricTimeAction_physical_inner_tendsto
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume)
    (φ : RealComplexL2) :
    Tendsto (fun n : ℕ => inner ℂ
      ((neutralLogMetricTimeAction_memLp_two
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound).toLp
        (fun x : ℝ => v x +
          ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
            ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
              (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) φ)
      atTop (𝓝 (inner ℂ (𝓕⁻ (hp.toLp
        (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)))) φ)) := by
  have hc : Continuous (fun u : RealComplexL2 => inner ℂ u φ) :=
    continuous_id.inner (𝕜 := ℂ) continuous_const
  exact (hc.tendsto _).comp
    (neutralLogMetricTimeAction_physical_toLp_tendsto M hM v hv hvi hbound hp)


set_option maxHeartbeats 1000000 in
/-- The full-line spectral source and endpoint source agree weakly on
 cap-supported tests. Exterior action is retained outside this comparison. -/
theorem neutralLogMetricEndpointSource_spectral_inner_eq
    (B L M : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|)
    (hp : MemLp (fun ξ : ℝ => (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
      (logarithmicFourierWeight ξ : ℂ)) 2 volume)
    (φ : RealComplexL2) (hφ : ∀ᵐ x ∂volume, x ∉ Icc (-B) B → φ x = 0) :
    inner ℂ (𝓕⁻ (hp.toLp (fun ξ : ℝ =>
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        (logarithmicFourierWeight ξ : ℂ))) : RealComplexL2) φ =
      inner ℂ (neutralLogMetricEndpointCandidateL2 B M L hB hL
        v hv hbound hmod) φ := by
  let u := neutralLogMetricTrialZeroExtension B v
  have hu : Measurable u := neutralLogMetricTrialZeroExtension_measurable B v hv
  have hui : Integrable u := neutralLogMetricTrialZeroExtension_integrable B M v hv hbound
  have hub : ∀ x, ‖u x‖ ≤ M := neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound
  let A : ℕ → ℝ → ℂ := fun n x => u x +
    ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (u x - ∫ y : ℝ, u y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))
  let T : ℕ → ℝ → ℂ := fun n => (Icc (-B) B).indicator (fun x : ℝ => v x +
    ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, u y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))
  have hmem (n : ℕ) : MemLp (A n) 2 volume :=
    neutralLogMetricTimeAction_memLp_two _ _ M (by positivity) hM u hu hui hub
  have he (n : ℕ) : inner ℂ ((hmem n).toLp (A n)) φ =
      ∫ x : ℝ, inner ℂ (T n x) (φ x) := by
    rw [L2.inner_def]
    apply integral_congr_ae
    filter_upwards [(hmem n).coeFn_toLp, hφ] with x hx hφx
    rw [hx]
    by_cases hxc : x ∈ Icc (-B) B
    · have hux : u x = v x := by
        simp [u, neutralLogMetricTrialZeroExtension, hxc]
      simp only [A, T, indicator_of_mem hxc, hux]
    · simp only [T, indicator_of_notMem hxc, hφx hxc, inner_zero_right]
  have hc : inner ℂ (neutralLogMetricEndpointCandidateL2 B M L hB hL
      v hv hbound hmod) φ =
      ∫ x : ℝ, inner ℂ (neutralLogMetricEndpointZeroExtension B v x) (φ x) := by
    rw [L2.inner_def]
    apply integral_congr_ae
    filter_upwards [neutralLogMetricEndpointCandidateL2_coe
      B M L hB hL v hv hbound hmod] with x hx
    rw [hx]
  have hs := neutralLogMetricTimeAction_physical_inner_tendsto M hM u hu hui hub hp φ
  change Tendsto (fun n => inner ℂ ((hmem n).toLp (A n)) φ) atTop
    (𝓝 (inner ℂ (𝓕⁻ (hp.toLp (fun ξ : ℝ =>
      (𝓕 u) ξ * (logarithmicFourierWeight ξ : ℂ)))) φ)) at hs
  simp_rw [he] at hs
  have ht := neutralLogMetricPoissonTrialAction_integral_inner_tendsto
    B L M hB hL hM v hv hbound hmod φ
  change Tendsto (fun n => ∫ x : ℝ, inner ℂ (T n x) (φ x)) atTop
    (𝓝 (∫ x : ℝ, inner ℂ (neutralLogMetricEndpointZeroExtension B v x) (φ x))) at ht
  rw [← hc] at ht
  exact tendsto_nhds_unique hs ht


/-- Supported-test agreement determines the cap compression as an L2 vector. -/
theorem neutralLogMetricSupported_inner_eq_indicator_toLp_eq
    (B : ℝ) (S E : RealComplexL2)
    (hE : ∀ᵐ x ∂volume, x ∉ Icc (-B) B → E x = 0)
    (hweak : ∀ φ : RealComplexL2,
      (∀ᵐ x ∂volume, x ∉ Icc (-B) B → φ x = 0) →
        inner ℂ S φ = inner ℂ E φ) :
    ((Lp.memLp S).indicator measurableSet_Icc).toLp
      ((Icc (-B) B).indicator (S : ℝ → ℂ)) = E := by
  let C : RealComplexL2 := ((Lp.memLp S).indicator measurableSet_Icc).toLp
    ((Icc (-B) B).indicator (S : ℝ → ℂ))
  have hC : (C : ℝ → ℂ) =ᵐ[volume] (Icc (-B) B).indicator (S : ℝ → ℂ) :=
    ((Lp.memLp S).indicator measurableSet_Icc).coeFn_toLp
  have hD : ∀ᵐ x ∂volume, x ∉ Icc (-B) B → (C - E) x = 0 := by
    filter_upwards [Lp.coeFn_sub C E, hC, hE] with x hx hc he
    intro hxc
    rw [hx, hc, indicator_of_notMem hxc, he hxc, sub_self]
  have hpair : inner ℂ C (C - E) = inner ℂ S (C - E) := by
    rw [L2.inner_def, L2.inner_def]
    apply integral_congr_ae
    filter_upwards [hC, hD] with x hc hd
    rw [hc]
    by_cases hx : x ∈ Icc (-B) B
    · rw [indicator_of_mem hx]
    · simp only [indicator_of_notMem hx, hd hx, inner_zero_right]
  have hz : inner ℂ (C - E) (C - E) = 0 := by
    rw [inner_sub_left, hpair, hweak (C - E) hD, sub_self]
  exact sub_eq_zero.mp ((inner_self_eq_zero (𝕜 := ℂ)).mp hz)

set_option maxHeartbeats 1000000 in
/-- The cap compression of the actual spectral source is exactly the
 constructed endpoint L2 vector, conditional on the full spectral domain. -/
theorem neutralLogMetricEndpointSource_spectral_compression_eq
    (B L M : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|)
    (hp : MemLp (fun ξ : ℝ => (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
      (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    (let S : RealComplexL2 := 𝓕⁻ (hp.toLp (fun ξ : ℝ =>
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        (logarithmicFourierWeight ξ : ℂ)))
     ((Lp.memLp S).indicator measurableSet_Icc).toLp
       ((Icc (-B) B).indicator (S : ℝ → ℂ))) =
      neutralLogMetricEndpointCandidateL2 B M L hB hL v hv hbound hmod := by
  apply neutralLogMetricSupported_inner_eq_indicator_toLp_eq
  · filter_upwards [neutralLogMetricEndpointCandidateL2_coe
      B M L hB hL v hv hbound hmod] with x hx
    intro hxc
    rw [hx]
    exact neutralLogMetricEndpointZeroExtension_eq_zero B v x hxc
  · intro φ hφ
    exact neutralLogMetricEndpointSource_spectral_inner_eq
      B L M hB hL hM v hv hbound hmod hp φ hφ


/-- An L2 spectral function with an L2 first frequency moment belongs
 to the full logarithmic multiplier domain. This is stronger than form energy. -/
theorem neutralLogMetricWeighted_memLp_of_frequencyMoment
    (G : ℝ → ℂ) (hG : MemLp G 2 volume)
    (hξG : MemLp (fun ξ : ℝ => (ξ : ℂ) * G ξ) 2 volume) :
    MemLp (fun ξ : ℝ => G ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume := by
  have hm : AEStronglyMeasurable
      (fun ξ : ℝ => G ξ * (logarithmicFourierWeight ξ : ℂ)) volume :=
    hG.aestronglyMeasurable.mul
      (Complex.continuous_ofReal.comp logarithmicFourierWeight_continuous).aestronglyMeasurable
  apply ((hG.norm.const_mul (Real.exp 1)).add hξG.norm).mono' hm
  filter_upwards [] with ξ
  change ‖G ξ * (logarithmicFourierWeight ξ : ℂ)‖ ≤
    Real.exp 1 * ‖G ξ‖ + ‖(ξ : ℂ) * G ξ‖
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have hb : logarithmicFourierWeight ξ ≤ Real.exp 1 + |ξ| := by
    have h := Real.log_le_sub_one_of_pos
      (show 0 < Real.exp 1 + |ξ| from by positivity)
    dsimp only [logarithmicFourierWeight]
    linarith
  simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hw]
  calc
    ‖G ξ‖ * logarithmicFourierWeight ξ ≤ ‖G ξ‖ * (Real.exp 1 + |ξ|) :=
      mul_le_mul_of_nonneg_left hb (norm_nonneg _)
    _ = Real.exp 1 * ‖G ξ‖ + |ξ| * ‖G ξ‖ := by ring

set_option maxHeartbeats 1000000 in
/-- First-frequency-moment regularity supplies the domain premise in
 the spectral/endpoint compression identity. -/
theorem neutralLogMetricEndpointSource_compression_eq_of_frequencyMoment
    (B L M : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|)
    (hF : MemLp (𝓕 (neutralLogMetricTrialZeroExtension B v)) 2 volume)
    (hξF : MemLp (fun ξ : ℝ => (ξ : ℂ) *
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ) 2 volume) :
    (let hp := neutralLogMetricWeighted_memLp_of_frequencyMoment _ hF hξF
     let S : RealComplexL2 := 𝓕⁻ (hp.toLp (fun ξ : ℝ =>
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        (logarithmicFourierWeight ξ : ℂ)))
     ((Lp.memLp S).indicator measurableSet_Icc).toLp
       ((Icc (-B) B).indicator (S : ℝ → ℂ))) =
      neutralLogMetricEndpointCandidateL2 B M L hB hL v hv hbound hmod := by
  exact neutralLogMetricEndpointSource_spectral_compression_eq
    B L M hB hL hM v hv hbound hmod
    (neutralLogMetricWeighted_memLp_of_frequencyMoment _ hF hξF)


/-- Schwartz spectral functions have an actual L2 first frequency moment. -/
theorem neutralLogMetricSchwartz_frequencyMoment_memLp (G : 𝓢(ℝ, ℂ)) :
    MemLp (fun ξ : ℝ => (ξ : ℂ) * G ξ) 2 volume := by
  have hg : (fun ξ : ℝ => (ξ : ℂ)).HasTemperateGrowth := by fun_prop
  have hm := (SchwartzMap.smulLeftCLM ℂ (fun ξ : ℝ => (ξ : ℂ)) G).memLp 2 volume
  have he : (SchwartzMap.smulLeftCLM ℂ (fun ξ : ℝ => (ξ : ℂ)) G : ℝ → ℂ) =
      (fun ξ : ℝ => (ξ : ℂ) * G ξ) := by
    funext ξ
    rw [SchwartzMap.smulLeftCLM_apply_apply hg]
    rfl
  rw [he] at hm
  exact hm

/-- Schwartz spectral functions belong to the full logarithmic domain. -/
theorem neutralLogMetricSchwartz_weighted_memLp (G : 𝓢(ℝ, ℂ)) :
    MemLp (fun ξ : ℝ => G ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume := by
  exact neutralLogMetricWeighted_memLp_of_frequencyMoment G (G.memLp 2 volume)
    (neutralLogMetricSchwartz_frequencyMoment_memLp G)

/-- Every physical Schwartz trial supplies the weighted Fourier domain
 condition, with no weighted-domain hypothesis. -/
theorem neutralLogMetricSchwartz_fourier_weighted_memLp (f : 𝓢(ℝ, ℂ)) :
    MemLp (fun ξ : ℝ => (𝓕 (f : ℝ → ℂ)) ξ *
      (logarithmicFourierWeight ξ : ℂ)) 2 volume := by
  have h := neutralLogMetricSchwartz_weighted_memLp (𝓕 f)
  simpa only [SchwartzMap.fourier_coe] using h

/-- A cap-supported physical Schwartz trial is unchanged by zero extension,
 so the actual zero extension supplies the full weighted Fourier domain. -/
theorem neutralLogMetricTrialZeroExtension_weighted_memLp_of_schwartz
    (B : ℝ) (f : 𝓢(ℝ, ℂ))
    (hs : ∀ x, x ∉ Icc (-B) B → f x = 0) :
    MemLp (fun ξ : ℝ => (𝓕 (neutralLogMetricTrialZeroExtension B f)) ξ *
      (logarithmicFourierWeight ξ : ℂ)) 2 volume := by
  have he : neutralLogMetricTrialZeroExtension B f = (f : ℝ → ℂ) := by
    funext x
    by_cases hx : x ∈ Icc (-B) B
    · simp [neutralLogMetricTrialZeroExtension, hx]
    · simp [neutralLogMetricTrialZeroExtension, hx, hs x hx]
  rw [he]
  exact neutralLogMetricSchwartz_fourier_weighted_memLp f

end
end WeilDefect
