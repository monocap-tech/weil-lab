import WeilDefect.Morphology.NeutralLogMetricTimeActionBounds
import WeilDefect.Morphology.NeutralLogMetricSpectralL2
import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import WeilDefect.Morphology.NeutralLogMetricTruncatedLimit
import WeilDefect.Morphology.NeutralCanonicalFormDomain
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

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
  apply h.congr'
  filter_upwards [] with n
  exact neutralLogMetricTimeAction_fourierInv_eq_physical
    (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound hp

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
    rw [hx]
    change C x - E x = 0
    rw [hc, indicator_of_notMem hxc, he hxc, sub_self]
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


set_option maxHeartbeats 1000000 in
/-- A cap-supported Schwartz trial has the endpoint compression identity
 with its spectral-domain witness derived from smooth rapid decay. -/
theorem neutralLogMetricEndpointSource_compression_eq_of_schwartz
    (B L M : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (f : 𝓢(ℝ, ℂ)) (hs : ∀ x, x ∉ Icc (-B) B → f x = 0)
    (hbound : ∀ x ∈ Icc (-B) B, ‖f x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖f x - f y‖ ≤ L * |x - y|) :
    (let hp := neutralLogMetricTrialZeroExtension_weighted_memLp_of_schwartz B f hs
     let S : RealComplexL2 := 𝓕⁻ (hp.toLp (fun ξ : ℝ =>
      (𝓕 (neutralLogMetricTrialZeroExtension B f)) ξ *
        (logarithmicFourierWeight ξ : ℂ)))
     ((Lp.memLp S).indicator measurableSet_Icc).toLp
       ((Icc (-B) B).indicator (S : ℝ → ℂ))) =
      neutralLogMetricEndpointCandidateL2 B M L hB hL f f.continuous.measurable hbound hmod := by
  exact neutralLogMetricEndpointSource_spectral_compression_eq
    B L M hB hL hM f f.continuous.measurable hbound hmod
    (neutralLogMetricTrialZeroExtension_weighted_memLp_of_schwartz B f hs)


set_option maxHeartbeats 1000000 in
/-- The spectral source agrees almost everywhere inside the cap with the
 endpoint candidate, retaining its independent exterior action. -/
theorem neutralLogMetricEndpointSource_spectral_ae_on_cap
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
     ∀ᵐ x ∂volume, x ∈ Icc (-B) B → S x = neutralLogMetricEndpointCandidate B v x) := by
  let S : RealComplexL2 := 𝓕⁻ (hp.toLp (fun ξ : ℝ =>
    (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ * (logarithmicFourierWeight ξ : ℂ)))
  let C : RealComplexL2 := ((Lp.memLp S).indicator measurableSet_Icc).toLp
    ((Icc (-B) B).indicator (S : ℝ → ℂ))
  have he : C = neutralLogMetricEndpointCandidateL2 B M L hB hL v hv hbound hmod :=
    neutralLogMetricEndpointSource_spectral_compression_eq
      B L M hB hL hM v hv hbound hmod hp
  have hc : (C : ℝ → ℂ) =ᵐ[volume] (Icc (-B) B).indicator (S : ℝ → ℂ) :=
    ((Lp.memLp S).indicator measurableSet_Icc).coeFn_toLp
  filter_upwards [hc, neutralLogMetricEndpointCandidateL2_coe
    B M L hB hL v hv hbound hmod] with x hcx hex
  intro hx
  have h := hcx.symm.trans
    ((congrArg (fun u : RealComplexL2 => u x) he).trans hex)
  simpa only [neutralLogMetricEndpointZeroExtension, indicator_of_mem hx] using h


/-- Any positive shifted fractional-frequency moment in L2 supplies the
 full logarithmic domain; no first-frequency-moment premise is needed. -/
theorem neutralLogMetricWeighted_memLp_of_fractionalMoment
    (σ : ℝ) (hσ : 0 < σ) (G : ℝ → ℂ)
    (hG : AEStronglyMeasurable G volume)
    (hfrac : MemLp (fun ξ : ℝ =>
      ((Real.exp 1 + |ξ|) ^ σ : ℂ) * G ξ) 2 volume) :
    MemLp (fun ξ : ℝ => G ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume := by
  have hm : AEStronglyMeasurable
      (fun ξ : ℝ => G ξ * (logarithmicFourierWeight ξ : ℂ)) volume :=
    hG.mul (Complex.continuous_ofReal.comp
      logarithmicFourierWeight_continuous).aestronglyMeasurable
  apply (hfrac.norm.const_mul (1 / σ)).mono' hm
  filter_upwards [] with ξ
  change ‖G ξ * (logarithmicFourierWeight ξ : ℂ)‖ ≤
    (1 / σ) * ‖((Real.exp 1 + |ξ|) ^ σ : ℂ) * G ξ‖
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have hx : 0 ≤ Real.exp 1 + |ξ| := by positivity
  have hp : 0 ≤ (Real.exp 1 + |ξ|) ^ σ := Real.rpow_nonneg hx σ
  have hb : logarithmicFourierWeight ξ ≤ (Real.exp 1 + |ξ|) ^ σ / σ :=
    Real.log_le_rpow_div hx hσ
  simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg hw, abs_of_nonneg hp]
  calc
    ‖G ξ‖ * logarithmicFourierWeight ξ ≤
        ‖G ξ‖ * ((Real.exp 1 + |ξ|) ^ σ / σ) :=
      mul_le_mul_of_nonneg_left hb (norm_nonneg _)
    _ = (1 / σ) * ((Real.exp 1 + |ξ|) ^ σ * ‖G ξ‖) := by ring

/-- Quarter-frequency regularity is a concrete fractional-domain criterion. -/
theorem neutralLogMetricWeighted_memLp_of_quarterMoment
    (G : ℝ → ℂ) (hG : AEStronglyMeasurable G volume)
    (hfrac : MemLp (fun ξ : ℝ =>
      ((Real.exp 1 + |ξ|) ^ (1 / 4 : ℝ) : ℂ) * G ξ) 2 volume) :
    MemLp (fun ξ : ℝ => G ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume := by
  exact neutralLogMetricWeighted_memLp_of_fractionalMoment
    (1 / 4) (by norm_num) G hG hfrac


/-- A reciprocal Fourier tail has an integrable squared fractional moment
 on the positive tail whenever the exponent is below one half. -/
theorem neutralLogMetricFractionalReciprocalTail_integrableOn
    (σ : ℝ) (hσ : σ < 1 / 2) :
    IntegrableOn (fun ξ : ℝ => (ξ ^ σ / ξ) ^ 2) (Ioi 1) := by
  have hi := integrableOn_Ioi_rpow_of_lt
    (a := (σ - 1) * 2) (by linarith) (by norm_num : (0 : ℝ) < 1)
  apply hi.congr_fun _ measurableSet_Ioi
  intro ξ hξ
  have hx : 0 < ξ := lt_trans (by norm_num : (0 : ℝ) < 1) hξ
  have he : ξ ^ σ / ξ = ξ ^ (σ - 1) := by
    calc
      ξ ^ σ / ξ = ξ ^ σ / ξ ^ (1 : ℝ) := by rw [Real.rpow_one]
      _ = ξ ^ (σ - 1) := (Real.rpow_sub hx σ 1).symm
  rw [he, ← Real.rpow_natCast (ξ ^ (σ - 1)) 2, ← Real.rpow_mul hx.le]

/-- The quarter-frequency squared reciprocal tail is integrable. -/
theorem neutralLogMetricQuarterReciprocalTail_integrableOn :
    IntegrableOn (fun ξ : ℝ => (ξ ^ (1 / 4 : ℝ) / ξ) ^ 2) (Ioi 1) := by
  exact neutralLogMetricFractionalReciprocalTail_integrableOn (1 / 4) (by norm_num)


/-- The logarithmic criterion's shifted quarter-frequency reciprocal tail
 has an integrable square on the positive tail. -/
theorem neutralLogMetricShiftedQuarterReciprocalTail_integrableOn :
    IntegrableOn (fun ξ : ℝ =>
      ((Real.exp 1 + ξ) ^ (1 / 4 : ℝ) / ξ) ^ 2) (Ioi 1) := by
  let c : ℝ := (Real.exp 1 + 1) ^ (1 / 4 : ℝ)
  have hc : 0 ≤ c := Real.rpow_nonneg (by positivity) _
  apply (neutralLogMetricQuarterReciprocalTail_integrableOn.const_mul (c ^ 2)).mono'
    (by fun_prop)
  filter_upwards [ae_restrict_mem measurableSet_Ioi] with ξ hξ
  have hx : 0 < ξ := lt_trans (by norm_num : (0 : ℝ) < 1) hξ
  have hshift : Real.exp 1 + ξ ≤ (Real.exp 1 + 1) * ξ := by
    nlinarith [Real.exp_pos (1 : ℝ)]
  have hp : (Real.exp 1 + ξ) ^ (1 / 4 : ℝ) ≤ c * ξ ^ (1 / 4 : ℝ) := by
    have h := Real.rpow_le_rpow
      (by positivity : 0 ≤ Real.exp 1 + ξ) hshift (by norm_num : 0 ≤ (1 / 4 : ℝ))
    rw [Real.mul_rpow (by positivity : 0 ≤ Real.exp 1 + 1) hx.le] at h
    exact h
  have hq : (Real.exp 1 + ξ) ^ (1 / 4 : ℝ) / ξ ≤
      c * (ξ ^ (1 / 4 : ℝ) / ξ) := by
    have h := (div_le_div_iff_of_pos_right hx).mpr hp
    simpa only [mul_div_assoc] using h
  change ‖((Real.exp 1 + ξ) ^ (1 / 4 : ℝ) / ξ) ^ 2‖ ≤
    c ^ 2 * (ξ ^ (1 / 4 : ℝ) / ξ) ^ 2
  rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _)]
  calc
    ((Real.exp 1 + ξ) ^ (1 / 4 : ℝ) / ξ) ^ 2 ≤
        (c * (ξ ^ (1 / 4 : ℝ) / ξ)) ^ 2 :=
      (sq_le_sq₀ (by positivity) (by positivity)).mpr hq
    _ = c ^ 2 * (ξ ^ (1 / 4 : ℝ) / ξ) ^ 2 := by ring

end
end WeilDefect
