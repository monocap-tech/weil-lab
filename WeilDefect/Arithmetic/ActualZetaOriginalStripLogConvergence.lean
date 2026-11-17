import WeilDefect.Arithmetic.ActualZetaOriginalStripLogCarrier

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform Filter InnerProductSpace
open scoped FourierTransform ComplexConjugate

/-!
NF575 — the SAME strip bound also upgrades ordinary physical L²
convergence to convergence in the original weighted log carrier.
Sequential theorem: no general Sobolev embedding, H¹ or extra
log-norm hypothesis, and no zeta divisor or Gram hypothesis.
-/

/-- Every fixed literal window sample is continuous on physical L².
This uses the exact existing exponential column, not arbitrary
point evaluation of an L² Fourier equivalence class. -/
theorem neutralNF575WindowEvaluation_continuous (a : ℝ) (z : ℂ) :
    Continuous (fun f : RealComplexL2 => neutralWindowEvaluation a z f) := by
  have h : Continuous (fun f : RealComplexL2 =>
      inner ℂ (neutralExponentialColumnL2 a (conj z)) f) :=
    continuous_const.inner continuous_id
  simpa only [neutralExponentialColumnL2_inner, starRingEnd_apply, star_star] using h

/-- The original raw window strip envelope and L² convergence suffice
for finite log-energy admission and convergence in the actual
logarithmic Hilbert carrier, preserving every physical vector. -/
theorem neutralNF575PhysicalSequence_logLimit_of_strip
    (a : ℝ) (f : RealComplexL2) (g : ℕ → RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0)
    (hg : ∀ n, ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → g n x = 0)
    (hconv : Tendsto g atTop (nhds f))
    (M : ℝ) (hM : 0 ≤ M)
    (hft : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation a z f‖ ≤ M*neutralNF575StripEnvelope z.re)
    (hgt : ∀ n (z : ℂ), |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation a z (g n)‖ ≤ M*neutralNF575StripEnvelope z.re) :
    ∃ (k : NeutralLogHilbertCarrier a) (G : ℕ → NeutralLogHilbertCarrier a),
      neutralLogPhysical k.val = f ∧
      (∀ n, neutralLogPhysical (G n).val = g n) ∧
      Tendsto G atTop (nhds k) := by
  let k := neutralNF575StripLogCarrier a f hf M hM hft
  let G := fun n => neutralNF575StripLogCarrier a (g n) (hg n) M hM (hgt n)
  have hk : neutralLogPhysical k.val = f :=
    neutralNF575StripLogCarrier_physical a f hf M hM hft
  have hG (n : ℕ) : neutralLogPhysical (G n).val = g n :=
    neutralNF575StripLogCarrier_physical a (g n) (hg n) M hM (hgt n)
  let V := fun (v : RealComplexL2) (ξ : ℝ) =>
    neutralWindowEvaluation a ((-2*Real.pi*ξ : ℝ):ℂ) v
  let F := fun (n : ℕ) (ξ : ℝ) =>
    logarithmicFourierWeight ξ * ‖V (g n) ξ - V f ξ‖^2
  let W := fun ξ : ℝ =>
    (neutralNF575LogConstant * ((2*M)*neutralNF575StripConstant)^2) *
      neutralNF575ContinuumWeight ξ
  have hW : Integrable W volume :=
    neutralNF575ContinuumWeight_integrable.const_mul _
  have hfour (n : ℕ) :
      (fun ξ => (𝓕 (g n) : RealComplexL2) ξ) =ᵐ[volume] V (g n) :=
    neutralNF575SupportedFourier_ae a (g n) (hg n)
  have hfourf : (fun ξ => (𝓕 f : RealComplexL2) ξ) =ᵐ[volume] V f :=
    neutralNF575SupportedFourier_ae a f hf
  have hmeas (n : ℕ) : AEStronglyMeasurable (F n) volume := by
    have hm : AEStronglyMeasurable (fun ξ =>
        logarithmicFourierWeight ξ *
          ‖(𝓕 (g n) : RealComplexL2) ξ - (𝓕 f : RealComplexL2) ξ‖^2)
        volume :=
      logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
        (((Lp.aestronglyMeasurable (𝓕 (g n) : RealComplexL2)).sub
          (Lp.aestronglyMeasurable (𝓕 f : RealComplexL2))).norm.pow 2)
    apply hm.congr
    filter_upwards [hfour n,hfourf] with ξ h1 h2
    change logarithmicFourierWeight ξ *
      ‖(𝓕 (g n) : RealComplexL2) ξ - (𝓕 f : RealComplexL2) ξ‖^2 =
      logarithmicFourierWeight ξ * ‖V (g n) ξ - V f ξ‖^2
    rw [h1,h2]
  have hbound (n : ℕ) : ∀ᵐ ξ ∂volume, ‖F n ξ‖ ≤ W ξ := by
    filter_upwards [] with ξ
    let z : ℂ := ((-2*Real.pi*ξ : ℝ):ℂ)
    have hz : |z.im| ≤ 1/2 := by simp [z]
    have h1 := hgt n z hz
    have h2 := hft z hz
    change ‖V (g n) ξ‖ ≤ M*neutralNF575StripEnvelope (-2*Real.pi*ξ) at h1
    change ‖V f ξ‖ ≤ M*neutralNF575StripEnvelope (-2*Real.pi*ξ) at h2
    have hd : ‖V (g n) ξ - V f ξ‖ ≤
        (2*M)*neutralNF575StripEnvelope (-2*Real.pi*ξ) := by
      calc
        _ ≤ ‖V (g n) ξ‖ + ‖V f ξ‖ := norm_sub_le _ _
        _ ≤ M*neutralNF575StripEnvelope (-2*Real.pi*ξ) +
            M*neutralNF575StripEnvelope (-2*Real.pi*ξ) := add_le_add h1 h2
        _ = _ := by ring
    change ‖logarithmicFourierWeight ξ * ‖V (g n) ξ - V f ξ‖^2‖ ≤ W ξ
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg
      (zero_le_one.trans (one_le_logarithmicFourierWeight ξ)) (sq_nonneg _))]
    exact neutralNF575EnergyEnvelope_le (2*M) (by positivity) ξ _ hd
  have hlim : ∀ᵐ ξ ∂volume,
      Tendsto (fun n => F n ξ) atTop (nhds (0:ℝ)) := by
    filter_upwards [] with ξ
    have hv : Tendsto (fun n => V (g n) ξ) atTop (nhds (V f ξ)) :=
      (neutralNF575WindowEvaluation_continuous a
        ((-2*Real.pi*ξ : ℝ):ℂ)).continuousAt.tendsto.comp hconv
    have h := (((hv.sub tendsto_const_nhds).norm).pow 2).const_mul
      (logarithmicFourierWeight ξ)
    simpa [F] using h
  have hint : Tendsto (fun n => ∫ ξ, F n ξ ∂volume) atTop (nhds (0:ℝ)) := by
    simpa only [integral_zero] using
      (tendsto_integral_of_dominated_convergence W hmeas hW hbound hlim)
  have hnorm (n : ℕ) : ‖G n-k‖^2 = ∫ ξ, F n ξ ∂volume := by
    rw [neutralLogHilbertCarrier_norm_sq]
    have hphys : neutralLogPhysical (G n-k).val = g n-f := by
      change neutralLogPhysical ((G n).val-k.val) = _
      rw [map_sub,hG n,hk]
    rw [hphys, show (𝓕 (g n-f) : RealComplexL2) =
        (𝓕 (g n) : RealComplexL2)-(𝓕 f : RealComplexL2) from
      (Lp.fourierTransformₗᵢ ℝ ℂ).map_sub (g n) f]
    apply integral_congr_ae
    filter_upwards [Lp.coeFn_sub (𝓕 (g n) : RealComplexL2)
      (𝓕 f : RealComplexL2), hfour n,hfourf] with ξ hd h1 h2
    change logarithmicFourierWeight ξ *
      ‖((𝓕 (g n) : RealComplexL2)-(𝓕 f : RealComplexL2)) ξ‖^2 =
      logarithmicFourierWeight ξ * ‖V (g n) ξ - V f ξ‖^2
    rw [hd,Pi.sub_apply,h1,h2]
  have hn : Tendsto (fun n => ‖G n-k‖^2) atTop (nhds (0:ℝ)) := by
    simpa only [hnorm] using hint
  refine ⟨k,G,hk,hG,?_⟩
  apply tendsto_iff_norm_sub_tendsto_zero.mpr
  have h := Real.continuous_sqrt.continuousAt.tendsto.comp hn
  simpa only [Function.comp_def, Real.sqrt_sq_eq_abs,
    abs_of_nonneg (norm_nonneg _), Real.sqrt_zero] using h

end
end WeilDefect
