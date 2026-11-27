import WeilDefect.Arithmetic.ActualZetaLogCarrierFourierDerivativeWitness
import WeilDefect.Arithmetic.ActualZetaIV096OriginalEffectiveCollarCutoffGate
import Mathlib.MeasureTheory.Function.ConvergenceInMeasure

namespace WeilDefect
noncomputable section
open MeasureTheory Filter FourierTransform
open scoped Topology SchwartzMap FourierTransform

/-- A possibly unbounded pointwise multiplier has a closed graph on L2.
Only two genuine L2 limits are used, with a common almost-everywhere
convergent subsequence; no bounded multiplier hypothesis is inserted. -/
theorem neutralIV106E18SGraph_limit (m : ℝ → ℂ)
    (f g : ℕ → RealComplexL2) (u v : RealComplexL2)
    (hf : Tendsto f atTop (𝓝 u)) (hg : Tendsto g atTop (𝓝 v))
    (h : ∀ n, ∀ᵐ x ∂volume, g n x = m x * f n x) :
    ∀ᵐ x ∂volume, v x = m x*u x := by
  obtain ⟨a,ha,hae⟩ := (tendstoInMeasure_of_tendsto_Lp hf).exists_seq_tendsto_ae
  obtain ⟨b,hb,hbe⟩ :=
    (tendstoInMeasure_of_tendsto_Lp (hg.comp ha.tendsto_atTop)).exists_seq_tendsto_ae
  have hall : ∀ᵐ x ∂volume, ∀ n : ℕ, g n x = m x*f n x := ae_all_iff.mpr h
  filter_upwards [hae,hbe,hall] with x hfx hgx he
  have h1 : Tendsto (fun n => f (a (b n)) x) atTop (𝓝 (u x)) :=
    hfx.comp hb.tendsto_atTop
  have h2 : Tendsto (fun n => g (a (b n)) x) atTop (𝓝 (m x*u x)) := by
    have ht := tendsto_const_nhds.mul h1 (a := m x)
    simpa only [← he] using ht
  exact tendsto_nhds_unique hgx h2

/-- Normalized derivative, matching the frozen NF541 witness convention. -/
def neutralIV106E18SNormalized (s : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  ((2 * (Real.pi:ℂ) * Complex.I)⁻¹ : ℂ) • SchwartzMap.derivCLM ℂ ℂ s

theorem neutralIV106E18SSchwartz_multiplier (s : 𝓢(ℝ,ℂ)) :
    ∀ᵐ ξ ∂volume,
      (𝓕 ((neutralIV106E18SNormalized s).toLp 2 volume) : RealComplexL2) ξ =
      (ξ:ℂ)*(𝓕 (s.toLp 2 volume) : RealComplexL2) ξ := by
  rw [SchwartzMap.toLp_fourier_eq,SchwartzMap.toLp_fourier_eq]
  filter_upwards [(𝓕 (neutralIV106E18SNormalized s) : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume,
    (𝓕 s : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume] with ξ h1 h2
  rw [h1,h2]
  unfold neutralIV106E18SNormalized
  rw [FourierTransform.fourier_smul]
  change ((2*(Real.pi:ℂ)*Complex.I)⁻¹:ℂ) *
    (𝓕 (deriv (s:ℝ→ℂ))) ξ = (ξ:ℂ)*(𝓕 (s:ℝ→ℂ)) ξ
  rw [Real.fourier_deriv s.integrable s.differentiable
    (SchwartzMap.derivCLM ℂ ℂ s).integrable]
  simp only [smul_eq_mul]
  have hπ : (Real.pi:ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr Real.pi_ne_zero
  have hI : Complex.I ≠ 0 := Complex.I_ne_zero
  field_simp [hπ,hI] <;> ring

/-- Closed graph transport to the same physical L2 limits. -/
theorem neutralIV106E18SFourier_limit (s : ℕ → 𝓢(ℝ,ℂ))
    (f df : RealComplexL2)
    (hf : Tendsto (fun n => (s n).toLp 2 volume) atTop (𝓝 f))
    (hd : Tendsto (fun n => (neutralIV106E18SNormalized (s n)).toLp 2 volume)
      atTop (𝓝 df)) :
    ∀ᵐ ξ ∂volume, (𝓕 df : RealComplexL2) ξ =
      (ξ:ℂ)*(𝓕 f : RealComplexL2) ξ := by
  apply neutralIV106E18SGraph_limit (fun ξ => (ξ:ℂ))
    (fun n => 𝓕 ((s n).toLp 2 volume))
    (fun n => 𝓕 ((neutralIV106E18SNormalized (s n)).toLp 2 volume))
  · exact (Lp.fourierTransformₗᵢ ℝ ℂ).continuous.continuousAt.tendsto.comp hf
  · exact (Lp.fourierTransformₗᵢ ℝ ℂ).continuous.continuousAt.tendsto.comp hd
  · exact fun n => neutralIV106E18SSchwartz_multiplier (s n)

theorem neutralIV106E18SWitness_sq (f df : RealComplexL2)
    (h : ∀ᵐ ξ ∂volume, (𝓕 df : RealComplexL2) ξ =
      (ξ:ℂ)*(𝓕 f : RealComplexL2) ξ) :
    ∀ᵐ ξ ∂volume, ‖(𝓕 df : RealComplexL2) ξ‖^2 =
      ξ^2*‖(𝓕 f : RealComplexL2) ξ‖^2 := by
  filter_upwards [h] with ξ hξ
  rw [hξ,norm_mul,Complex.norm_real,Real.norm_eq_abs,mul_pow,sq_abs]

/-- Actual supported rough carrier admission, conditional only on the
simultaneous L2 approximation of the function and normalized derivative. -/
theorem neutralIV106E18SGraph_admission (a : ℝ) (s : ℕ → 𝓢(ℝ,ℂ))
    (f df : RealComplexL2)
    (hf : Tendsto (fun n => (s n).toLp 2 volume) atTop (𝓝 f))
    (hd : Tendsto (fun n => (neutralIV106E18SNormalized (s n)).toLp 2 volume)
      atTop (𝓝 df))
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) :
    ∃ p : NeutralLogHilbertCarrier a, neutralLogPhysical p.val = f := by
  exact neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_derivativeWitness
    a f df hs (neutralIV106E18SWitness_sq f df
      (neutralIV106E18SFourier_limit s f df hf hd))

/-- Exact spectral energy majorant in terms of the normalized derivative
witness; this also applies to differences of graph pairs. -/
theorem neutralIV106E18SLog_bound (f df : RealComplexL2)
    (h : ∀ᵐ ξ ∂volume, (𝓕 df : RealComplexL2) ξ =
      (ξ:ℂ)*(𝓕 f : RealComplexL2) ξ) :
    (∫ ξ, logarithmicFourierWeight ξ * ‖(𝓕 f : RealComplexL2) ξ‖^2) ≤
      (Real.exp 1+1)*(∫ ξ, ‖(𝓕 f : RealComplexL2) ξ‖^2) +
        ∫ ξ, ‖(𝓕 df : RealComplexL2) ξ‖^2 := by
  have hf := (memLp_two_iff_integrable_sq_norm
    (Lp.aestronglyMeasurable (𝓕 f : RealComplexL2))).mp (Lp.memLp _)
  have hd := (memLp_two_iff_integrable_sq_norm
    (Lp.aestronglyMeasurable (𝓕 df : RealComplexL2))).mp (Lp.memLp _)
  have hw := neutralIV106E18SWitness_sq f df h
  have hlog := neutralFiniteLogFourierEnergy_of_quadraticMoment f
    (neutralQuadraticFourierMoment_of_derivativeWitness f df hw)
  calc
    _ ≤ ∫ ξ, (Real.exp 1+1)*‖(𝓕 f : RealComplexL2) ξ‖^2 +
      ‖(𝓕 df : RealComplexL2) ξ‖^2 := by
      apply integral_mono_ae hlog ((hf.const_mul _).add hd)
      filter_upwards [hw] with ξ hξ
      rw [hξ]
      have he := mul_le_mul_of_nonneg_right
        (neutralLogarithmicFourierWeight_le_quadraticMoment ξ)
        (sq_nonneg ‖(𝓕 f : RealComplexL2) ξ‖)
      linarith
    _ = _ := by rw [integral_add (hf.const_mul _) hd,integral_const_mul]

#print axioms neutralIV106E18SGraph_limit
#print axioms neutralIV106E18SSchwartz_multiplier
#print axioms neutralIV106E18SFourier_limit
#print axioms neutralIV106E18SWitness_sq
#print axioms neutralIV106E18SGraph_admission
#print axioms neutralIV106E18SLog_bound
end
end WeilDefect
