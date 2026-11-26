import WeilDefect.Arithmetic.ActualZetaIV106D1ReciprocalTangent
import WeilDefect.Arithmetic.ActualZetaIV106D6ActualPrimitive
import WeilDefect.Arithmetic.ActualZetaIV106E1ScalarBudget
import WeilDefect.Arithmetic.ActualZetaIV106E2GammaEnvelope
import WeilDefect.Arithmetic.ActualZetaIV106E9GroupedPrimeEnergy

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace FourierTransform
open scoped FourierTransform SchwartzMap InnerProduct ComplexConjugate

def neutralIV106E10Density (q : NeutralLogHilbertCarrier (11/10:ℝ)) (ξ : ℝ) : ℝ :=
  ‖(𝓕 (neutralLogPhysical q.val) : RealComplexL2) ξ‖^2

def neutralIV106E10Gamma (q : NeutralLogHilbertCarrier (11/10:ℝ)) : ℝ :=
  ∫ ξ : ℝ, compactWindowArchimedeanSymbol (2*Real.pi*ξ)*neutralIV106E10Density q ξ

def neutralIV106E10Prime (q : NeutralLogHilbertCarrier (11/10:ℝ)) : ℝ :=
  ∫ ξ : ℝ, rightLimitPrimeSymbol (11/10) (2*Real.pi*ξ)*neutralIV106E10Density q ξ

theorem neutralIV106E10Mass (q : NeutralLogHilbertCarrier (11/10:ℝ)) :
    Integrable (neutralIV106E10Density q) ∧
    (∫ ξ, neutralIV106E10Density q ξ) = ‖neutralLogPhysical q.val‖^2 := by
  constructor
  · exact (memLp_two_iff_integrable_sq_norm
      (Lp.aestronglyMeasurable (𝓕 (neutralLogPhysical q.val) : RealComplexL2))).mp (Lp.memLp _)
  · unfold neutralIV106E10Density
    rw [← neutralPhysicalL2_norm_sq, Lp.norm_fourier_eq]

theorem neutralIV106E10Prime_integrable (q : NeutralLogHilbertCarrier (11/10:ℝ)) :
    Integrable (fun ξ => rightLimitPrimeSymbol (11/10) (2*Real.pi*ξ)*neutralIV106E10Density q ξ) := by
  have hm := (neutralIV106E10Mass q).1
  apply (hm.const_mul (neutralActualZetaPrimeSymbolBound (11/10))).mono'
  · apply AEStronglyMeasurable.mul
    · apply Continuous.aestronglyMeasurable
      unfold rightLimitPrimeSymbol
      fun_prop
    · exact hm.aestronglyMeasurable
  · filter_upwards [] with ξ
    rw [Real.norm_eq_abs, abs_mul, abs_of_nonneg (sq_nonneg _)]
    exact mul_le_mul_of_nonneg_right (neutralActualZetaPrimeSymbol_abs_le _ _) (sq_nonneg _)

theorem neutralIV106E10Gamma_integrable (q : NeutralLogHilbertCarrier (11/10:ℝ)) :
    Integrable (fun ξ => compactWindowArchimedeanSymbol (2*Real.pi*ξ)*neutralIV106E10Density q ξ) := by
  have hi := neutralActualZetaCanonical_signedEnergy_integrable (11/10)
    (neutralLogHilbertToCanonical q)
  change Integrable (fun ξ => rightLimitCompactWeilSymbolMathlib (11/10) ξ *
    neutralIV106E10Density q ξ) at hi
  apply (hi.add (neutralIV106E10Prime_integrable q)).congr
  filter_upwards [] with ξ
  simp only [Pi.add_apply, rightLimitCompactWeilSymbolMathlib, rightLimitCompactWeilSymbol]
  ring

theorem neutralIV106E10Point (ξ : ℝ) (hξ : ξ ≠ 0) :
    Real.log 118+1/2-(118^2/2+25/(8*Real.pi^2))/ξ^2 ≤
      compactWindowArchimedeanSymbol (2*Real.pi*ξ) := by
  have ht := neutralIV106D1Log_tangent 118 |ξ| (by norm_num) (abs_pos.mpr hξ)
  have hg := neutralIV106E2Global ξ hξ
  rw [sq_abs] at ht
  have he : (118^2/2+25/(8*Real.pi^2))/ξ^2 =
      (118:ℝ)^2/(2*ξ^2)+25/(8*Real.pi^2*ξ^2) := by
    field_simp [hξ,Real.pi_pos.ne']
    <;> ring
  rw [he]
  linarith only [ht,hg]

/-- Integrate the actual archimedean density using the certified reciprocal moment. -/
theorem neutralIV106E10Gamma_bound (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (Real.log 118+1/2-(118^2*Real.pi^2/3+25/12)*(11/3325)^2)*
      ‖neutralLogPhysical q.val‖^2 ≤ neutralIV106E10Gamma q := by
  obtain ⟨hr,hj⟩ := neutralIV106D6Actual_reciprocal k hk q hq hd
  obtain ⟨hf,hm⟩ := neutralIV106E10Mass q
  have he := neutralIV106D1Energy_receiver
    (fun ξ => compactWindowArchimedeanSymbol (2*Real.pi*ξ)*neutralIV106E10Density q ξ)
    (neutralIV106E10Density q) (fun ξ => neutralIV106E10Density q ξ / ξ^2)
    (Real.log 118+1/2) (118^2/2+25/(8*Real.pi^2))
    (‖neutralLogPhysical q.val‖^2) ((2*Real.pi^2/3)*(11/3325)^2)
    (neutralIV106E10Gamma_integrable q) hf hr (by positivity) hm hj
    (by
      have hz : ∀ᵐ ξ : ℝ ∂volume, ξ ≠ 0 := by
        simpa using (measure_singleton (0:ℝ) : volume ({0}:Set ℝ) = 0)
      filter_upwards [hz] with ξ hξ
      have hp := mul_le_mul_of_nonneg_right (neutralIV106E10Point ξ hξ)
        (show 0 ≤ neutralIV106E10Density q ξ from sq_nonneg _)
      convert hp using 1 <;> ring)
  change _ ≤ neutralIV106E10Gamma q at he
  have hc : (118^2/2+25/(8*Real.pi^2))*((2*Real.pi^2/3)*(11/3325)^2) =
      (118^2*Real.pi^2/3+25/12)*(11/3325)^2 := by
    field_simp [Real.pi_pos.ne']
    <;> ring
  rwa [hc] at he

/-- Transfer the original prime-energy bound back to the native spectral integral. -/
theorem neutralIV106E10Prime_bound (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    neutralIV106E10Prime q ≤ (471031/125000:ℝ)*‖neutralLogPhysical q.val‖^2 := by
  rcases hd with ⟨v,hv,hphys⟩
  have h := neutralIV106E9Original_prime v hv
  have hp := neutralIV103Prime_spectral (11/10) (by norm_num) v v hv hv
  have he : (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) n) =
      (neutralIV106E10Prime q : ℂ) := by
    rw [hp, neutralIV106E10Prime, ← integral_complex_ofReal]
    apply integral_congr_ae
    filter_upwards [] with ξ
    unfold neutralIV103Spectrum neutralIV106E10Density
    rw [hphys, Complex.conj_mul']
    simp only [Complex.ofReal_mul, Complex.ofReal_pow]
  rw [he, Complex.ofReal_re] at h
  have hm : neutralIV106E9Mass v = ‖neutralLogPhysical q.val‖^2 := by
    rw [hphys, neutralIV106E9Mass, ← neutralPhysicalL2_norm_sq]
    apply integral_congr_ae
    filter_upwards [v.coeFn_toLp 2 volume] with x hx
    rw [hx]
  rwa [hm] at h

/-- The actual pole-moment row forces a nonnegative cross-pole term. -/
theorem neutralIV106E10Pole (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0) :
    0 ≤ 2*(conj (sourceWindowMoment (11/10) (-(1/2)) (neutralLogPhysical q.val)) *
      sourceWindowMoment (11/10) (1/2) (neutralLogPhysical q.val)).re := by
  have h := ((neutralIV106C3Constraints_zero_iff 665 k hk q).mp hq).2.1
  rw [h, Complex.conj_mul', Complex.ofReal_re]
  positivity

/-- Actual form coercivity on the constrained supported core. -/
theorem neutralIV106E10Core_margin (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (5003/5000:ℝ)*‖neutralLogPhysical q.val‖^2 ≤
      (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  apply neutralIV106E1Budget_receiver _ (neutralIV106E10Gamma q) (neutralIV106E10Prime q)
    (2*(conj (sourceWindowMoment (11/10) (-(1/2)) (neutralLogPhysical q.val)) *
      sourceWindowMoment (11/10) (1/2) (neutralLogPhysical q.val)).re) _
    (sq_nonneg _) (neutralIV106E10Gamma_bound k hk q hq hd)
    (neutralIV106E10Prime_bound q hd) (neutralIV106E10Pole k hk q hq)
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re]
  unfold neutralActualZetaCanonicalNativeQuadratic
  change (∫ ξ, rightLimitCompactWeilSymbolMathlib (11/10) ξ * neutralIV106E10Density q ξ) + _ = _
  unfold neutralIV106E10Gamma neutralIV106E10Prime
  rw [← integral_sub (neutralIV106E10Gamma_integrable q) (neutralIV106E10Prime_integrable q)]
  congr 1
  apply integral_congr_ae
  filter_upwards [] with ξ
  simp only [Pi.sub_apply, rightLimitCompactWeilSymbolMathlib, rightLimitCompactWeilSymbol]
  ring

#print axioms neutralIV106E10Mass
#print axioms neutralIV106E10Prime_integrable
#print axioms neutralIV106E10Gamma_integrable
#print axioms neutralIV106E10Point
#print axioms neutralIV106E10Gamma_bound
#print axioms neutralIV106E10Prime_bound
#print axioms neutralIV106E10Pole
#print axioms neutralIV106E10Core_margin
end
end WeilDefect
