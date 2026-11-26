import WeilDefect.Arithmetic.ActualZetaIV106E18ESeparatedPairing
import WeilDefect.Arithmetic.ActualZetaIV105COriginalProjectedPhysicalResponse
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Filter FourierTransform InnerProductSpace
open scoped SchwartzMap FourierTransform ComplexConjugate BigOperators

/-- Real-linear postcomposition, preserving genuine Schwartz regularity. -/
def neutralIV106E18GConj (u : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  SchwartzMap.postcompCLM (Complex.conjCLE.toContinuousLinearMap) u

theorem neutralIV106E18GConj_apply (u : 𝓢(ℝ,ℂ)) (x : ℝ) :
    neutralIV106E18GConj u x = conj (u x) := rfl

/-- The inverse transform of the conjugated test has the required sign. -/
theorem neutralIV106E18GConj_fourier (u : 𝓢(ℝ,ℂ)) (ξ : ℝ) :
    (𝓕⁻ (neutralIV106E18GConj u)) ξ = conj ((𝓕 u) ξ) := by
  rw [SchwartzMap.fourierInv_coe, Real.fourierInv_eq_fourier_neg,
    SchwartzMap.fourier_coe, Real.fourier_real_eq_integral_exp_smul,
    Real.fourier_real_eq_integral_exp_smul, ← integral_conj]
  apply integral_congr_ae
  filter_upwards [] with x
  simp only [neutralIV106E18GConj_apply, smul_eq_mul, map_mul,
    ← Complex.exp_conj, map_mul, Complex.conj_ofReal, Complex.conj_I]
  congr 2
  push_cast
  ring

theorem neutralIV106E18GSpectrum_ae (u v : 𝓢(ℝ,ℂ)) :
    neutralIV103Spectrum u v =ᵐ[volume]
      (fun ξ => (𝓕⁻ (neutralIV106E18GConj u)) ξ * 𝓕 (v : ℝ → ℂ) ξ) := by
  unfold neutralIV103Spectrum
  rw [SchwartzMap.toLp_fourier_eq u, SchwartzMap.toLp_fourier_eq v]
  filter_upwards [((𝓕 u : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume),
    ((𝓕 v : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume)] with ξ hξu hξv
  rw [hξu, hξv, neutralIV106E18GConj_fourier, SchwartzMap.fourier_coe v]

/-- Mixed physical correlation; the first argument is conjugated. -/
theorem neutralIV106E18GCorrelation (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x ∉ Set.Icc (-a) a, u x = 0)
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0) (t : ℝ) :
    neutralIV103Correlation a u v t =
      ∫ x : ℝ, v x * conj (u (x-t)) := by
  unfold neutralIV103Correlation neutralWindowCorrelation
  have h := neutralIV006Schwartz_window_ae a u hu
  have ht := (measurePreserving_add_right (volume : Measure ℝ) (-t)).quasiMeasurePreserving.ae h
  apply integral_congr_ae
  filter_upwards [neutralIV006Schwartz_window_ae a v hv, ht] with x hx hxt
  rw [hx, sub_eq_add_neg, hxt]

/-- All finite prime contributions vanish when both shifted products vanish. -/
theorem neutralIV106E18GPrime_zero (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x ∉ Set.Icc (-a) a, u x = 0)
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset a, ∀ x : ℝ, v x ≠ 0 →
      u (x-Real.log n) = 0 ∧ u (x+Real.log n) = 0) :
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation a u v) n) = 0 := by
  rw [neutralIV103Prime_finite]
  apply Finset.sum_eq_zero
  intro n hn
  unfold neutralIV085PrimeSummand
  have hp : neutralIV103Correlation a u v (Real.log n) = 0 := by
    rw [neutralIV106E18GCorrelation a u v hu hv]
    have hz : (fun x : ℝ => v x * conj (u (x-Real.log n))) = fun _ => 0 := by
      funext x
      by_cases hx : v x = 0
      · simp [hx]
      · simp [(hshift n hn x hx).1]
    rw [hz]
    simp
  have hm : neutralIV103Correlation a u v (-Real.log n) = 0 := by
    rw [neutralIV106E18GCorrelation a u v hu hv]
    have hz : (fun x : ℝ => v x * conj (u (x- -Real.log n))) = fun _ => 0 := by
      funext x
      by_cases hx : v x = 0
      · simp [hx]
      · simp [sub_neg_eq_add, (hshift n hn x hx).2]
    rw [hz]
    simp
  rw [hp, hm]
  simp

theorem neutralIV106E18GPole_zero (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x ∉ Set.Icc (-a) a, u x = 0)
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0)
    (hm : sourceWindowMoment a (-(1/2)) (v.toLp 2 volume) = 0)
    (hp : sourceWindowMoment a (1/2) (v.toLp 2 volume) = 0) :
    inner ℂ (neutralIV102Lift a u hu)
      (neutralLogPoleOperator a (neutralIV102Lift a v hv)) = 0 := by
  rw [neutralLogPoleOperator_mixed, neutralIV102Lift_physical,
    neutralIV102Lift_physical, hm, hp]
  simp

/-- Remove the constant gamma contact and preserve the exact IV103 spectrum. -/
theorem neutralIV106E18GArch_literal (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x ∉ Set.Icc (-a) a, u x = 0)
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0)
    {δ : ℝ} (hδ : 0 < δ)
    (hsep : ∀ x y, u x ≠ 0 → v y ≠ 0 → δ ≤ |x-y|) :
    (∫ ξ, (compactWindowArchimedeanSymbol (2*Real.pi*ξ) : ℂ) *
      neutralIV103Spectrum u v ξ) =
    ∫ x, conj (u x) * (∫ y, v y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  let F := neutralIV103Spectrum u v
  have hF := neutralIV103Spectrum_integrable a ha u v hu hv
  have hM := neutralActualZetaCanonical_mixed_integrable a
    (neutralIV102Canonical a u hu) (neutralIV102Canonical a v hv)
  have hM' : Integrable (fun ξ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) * F ξ) := by
    apply hM.congr
    filter_upwards [] with ξ
    unfold F neutralIV103Spectrum
    change conj ((𝓕 (u.toLp 2 volume) : RealComplexL2) ξ) *
      (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
      (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ = _
    ring
  have hP (n : ℕ) : Integrable (fun ξ => ((compactWindowPrimeCoefficient n *
      Real.cos ((2*Real.pi*ξ)*Real.log n) : ℝ) : ℂ) * F ξ) := by
    have h := hF.mul_bdd (c := |compactWindowPrimeCoefficient n|)
      (show Continuous (fun ξ : ℝ => ((compactWindowPrimeCoefficient n *
        Real.cos ((2*Real.pi*ξ)*Real.log n) : ℝ) : ℂ)) from by fun_prop).aestronglyMeasurable
      (by
        filter_upwards [] with ξ
        rw [Complex.norm_real, Real.norm_eq_abs, abs_mul]
        simpa using mul_le_mul_of_nonneg_left (Real.abs_cos_le_one _) (abs_nonneg _))
    apply h.congr
    filter_upwards [] with ξ
    exact mul_comm _ _
  have hP' : Integrable (fun ξ => (rightLimitPrimeSymbol a (2*Real.pi*ξ) : ℂ) * F ξ) := by
    apply (integrable_finset_sum (rightLimitPrimePowerFinset a) (fun n _ => hP n)).congr
    filter_upwards [] with ξ
    simp only [rightLimitPrimeSymbol, Complex.ofReal_sum, Finset.sum_mul]
  have hA : Integrable (fun ξ => (compactWindowArchimedeanSymbol (2*Real.pi*ξ) : ℂ) * F ξ) := by
    apply (hM'.add hP').congr
    filter_upwards [] with ξ
    simp only [Pi.add_apply, rightLimitCompactWeilSymbolMathlib,
      rightLimitCompactWeilSymbol, Complex.ofReal_sub]
    ring
  have hzero : (∫ ξ, F ξ) = 0 := by
    calc
      _ = ∫ ξ, (𝓕⁻ (neutralIV106E18GConj u)) ξ * 𝓕 (v : ℝ → ℂ) ξ :=
        integral_congr_ae (neutralIV106E18GSpectrum_ae u v)
      _ = ∫ x, neutralIV106E18GConj u x * v x :=
        (neutralIV106E18EFlip v v.integrable (neutralIV106E18GConj u)).symm
      _ = 0 := by
        have hz : (fun x : ℝ => neutralIV106E18GConj u x * v x) = fun _ => 0 := by
          funext x
          by_cases hx : u x = 0
          · simp [neutralIV106E18GConj_apply, hx]
          by_cases hy : v x = 0
          · simp [hy]
          have hh := hsep x x hx hy
          simp at hh
          linarith
        rw [hz]
        simp
  have hcenter :
      (∫ ξ, (compactWindowArchimedeanSymbol (2*Real.pi*ξ) : ℂ) * F ξ) =
      ∫ ξ, ((compactWindowArchimedeanSymbol (2*Real.pi*ξ) -
        compactWindowArchimedeanSymbol 0 : ℝ) : ℂ) * F ξ := by
    simp only [Complex.ofReal_sub, sub_mul]
    rw [integral_sub hA (hF.const_mul _), integral_const_mul, hzero, mul_zero, sub_zero]
  rw [hcenter]
  calc
    _ = ∫ ξ, (𝓕⁻ (neutralIV106E18GConj u)) ξ * (𝓕 (v : ℝ → ℂ) ξ *
      ((compactWindowArchimedeanSymbol (2*Real.pi*ξ) -
        compactWindowArchimedeanSymbol 0 : ℝ) : ℂ)) := by
      apply integral_congr_ae
      filter_upwards [neutralIV106E18GSpectrum_ae u v] with ξ hξ
      change _ * neutralIV103Spectrum u v ξ = _
      rw [hξ]
      ring
    _ = _ := by
      have hs : ∀ x y, neutralIV106E18GConj u x ≠ 0 → v y ≠ 0 → δ ≤ |x-y| := by
        intro x y hx hy
        apply hsep x y _ hy
        intro hz
        exact hx (by simp [neutralIV106E18GConj_apply, hz])
      simpa only [neutralIV106E18GConj_apply] using
        neutralIV106E18ELiteral v v.integrable (neutralIV106E18GConj u) hδ hs

/-- Literal full original mixed action, with physical prime and moment
cancellation conditions, not an assumed equality of actions. -/
theorem neutralIV106E18GMixed_literal (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x ∉ Set.Icc (-a) a, u x = 0)
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0)
    {δ : ℝ} (hδ : 0 < δ)
    (hsep : ∀ x y, u x ≠ 0 → v y ≠ 0 → δ ≤ |x-y|)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset a, ∀ x : ℝ, v x ≠ 0 →
      u (x-Real.log n) = 0 ∧ u (x+Real.log n) = 0)
    (hm : sourceWindowMoment a (-(1/2)) (v.toLp 2 volume) = 0)
    (hp : sourceWindowMoment a (1/2) (v.toLp 2 volume) = 0) :
    neutralIV101Mixed a u v =
    ∫ x, conj (u x) * (∫ y, v y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  unfold neutralIV101Mixed Zeta23.EF.literatureRHS
  change Zeta23.paperFT (neutralIV103Correlation a u v) (Complex.I / 2) +
    Zeta23.paperFT (neutralIV103Correlation a u v) (-Complex.I / 2) -
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation a u v) n) +
    (1 / (2 * Real.pi) : ℂ) * (∫ r : ℝ,
      Zeta23.paperFT (neutralIV103Correlation a u v) (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ)) = _
  rw [neutralIV103Pole_operator a u v hu hv,
    neutralIV106E18GPole_zero a u v hu hv hm hp,
    neutralIV106E18GPrime_zero a u v hu hv hshift,
    neutralIV103Arch_spectral a u v hu hv,
    neutralIV106E18GArch_literal a ha u v hu hv hδ hsep]
  simp

/-- Actual IV105B action, on supported Schwartz tests only. -/
theorem neutralIV106E18GAction_literal (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x ∉ Set.Icc (-a) a, u x = 0)
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0)
    {δ : ℝ} (hδ : 0 < δ)
    (hsep : ∀ x y, u x ≠ 0 → v y ≠ 0 → δ ≤ |x-y|)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset a, ∀ x : ℝ, v x ≠ 0 →
      u (x-Real.log n) = 0 ∧ u (x+Real.log n) = 0)
    (hm : sourceWindowMoment a (-(1/2)) (v.toLp 2 volume) = 0)
    (hp : sourceWindowMoment a (1/2) (v.toLp 2 volume) = 0) :
    inner ℂ (neutralIV105BAction a u) (v.toLp 2 volume) =
    ∫ x, conj (u x) * (∫ y, v y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  rw [← neutralIV105BAction_pair a ha u v hu hv]
  exact neutralIV106E18GMixed_literal a ha u v hu hv hδ hsep hshift hm hp

/-- Actual IV105C row, still on a supported Schwartz mass-complement test. -/
theorem neutralIV106E18GResponse_literal (k : ℕ) (hk : 0 < k) (i : Fin k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), v x = 0)
    (horth : neutralIV101MassComplement k hk v)
    {δ : ℝ} (hδ : 0 < δ)
    (hsep : ∀ x y, neutralIV100Carrier k hk i x ≠ 0 → v y ≠ 0 → δ ≤ |x-y|)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset (11/10:ℝ), ∀ x : ℝ, v x ≠ 0 →
      neutralIV100Carrier k hk i (x-Real.log n) = 0 ∧
      neutralIV100Carrier k hk i (x+Real.log n) = 0)
    (hm : sourceWindowMoment (11/10:ℝ) (-(1/2)) (v.toLp 2 volume) = 0)
    (hp : sourceWindowMoment (11/10:ℝ) (1/2) (v.toLp 2 volume) = 0) :
    inner ℂ (neutralIV105CResponse k hk i) (v.toLp 2 volume) =
    ∫ x, conj (neutralIV100Carrier k hk i x) * (∫ y, v y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  rw [← neutralIV105CResponse_pair k hk i v hv horth]
  exact neutralIV106E18GMixed_literal (11/10:ℝ) (by norm_num) _ v
    (neutralIV009OriginalCollars_supported_window _
      (neutralIV100Carrier_collars k hk i)) hv hδ hsep hshift hm hp

#print axioms neutralIV106E18GConj_apply
#print axioms neutralIV106E18GConj_fourier
#print axioms neutralIV106E18GSpectrum_ae
#print axioms neutralIV106E18GCorrelation
#print axioms neutralIV106E18GPrime_zero
#print axioms neutralIV106E18GPole_zero
#print axioms neutralIV106E18GArch_literal
#print axioms neutralIV106E18GMixed_literal
#print axioms neutralIV106E18GAction_literal
#print axioms neutralIV106E18GResponse_literal
end
end WeilDefect
