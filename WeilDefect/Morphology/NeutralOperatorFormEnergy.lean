import WeilDefect.Morphology.NeutralCanonicalFormDomain

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped FourierTransform

/-- A retained positive shifted lower comparison bounds one logarithmic
weight by a quadratic symbol weight. No actual comparison is proved here. -/
theorem logarithmicWeight_le_symbol_square
    (m : ℝ → ℝ) (L shift : ℝ) (hL : 0 < L)
    (hlower : ∀ ξ, L * logarithmicFourierWeight ξ ≤ m ξ + shift) (ξ : ℝ) :
    logarithmicFourierWeight ξ ≤ (1 / L) * (m ξ ^ 2 + (1 + |shift|)) := by
  have hm : m ξ ≤ m ξ ^ 2 + 1 := by nlinarith [sq_nonneg (m ξ - 1 / 2)]
  have hnum : L * logarithmicFourierWeight ξ ≤ m ξ ^ 2 + (1 + |shift|) := by
    linarith [hlower ξ, le_abs_self shift]
  calc
    logarithmicFourierWeight ξ ≤ (m ξ ^ 2 + (1 + |shift|)) / L :=
      (le_div_iff₀ hL).2 (by nlinarith)
    _ = _ := by ring

/-- Operator-domain spectral L2 plus a retained positive comparison implies
finite form energy. The base spectral mass also genuinely converges. -/
theorem finiteLogEnergy_of_spectralProduct
    (m : ℝ → ℝ) (F : ℝ → ℂ) (hF : MemLp F 2 volume)
    (hp : MemLp (fun ξ => (m ξ : ℂ) * F ξ) 2 volume)
    (L shift : ℝ) (hL : 0 < L)
    (hlower : ∀ ξ, L * logarithmicFourierWeight ξ ≤ m ξ + shift) :
    Integrable (fun ξ => logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) volume := by
  have hmass := (memLp_two_iff_integrable_sq_norm hF.aestronglyMeasurable).mp hF
  have hprod := (memLp_two_iff_integrable_sq_norm hp.aestronglyMeasurable).mp hp
  apply ((hprod.add (hmass.const_mul (1 + |shift|))).const_mul (1 / L)).mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      (hF.aestronglyMeasurable.norm.pow 2)
  · filter_upwards with ξ
    have hw : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hw (sq_nonneg _))]
    simp only [Pi.add_apply]
    calc
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2 ≤
          ((1 / L) * (m ξ ^ 2 + (1 + |shift|))) * ‖F ξ‖ ^ 2 :=
        mul_le_mul_of_nonneg_right
          (logarithmicWeight_le_symbol_square m L shift hL hlower ξ) (sq_nonneg _)
      _ = (1 / L) * (‖(m ξ : ℂ) * F ξ‖ ^ 2 + (1 + |shift|) * ‖F ξ‖ ^ 2) := by
        simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs, mul_pow, sq_abs]
        ring

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Transfer the exact carrier's spectral operator criterion to normalized
logarithmic Fourier energy, retaining the source's positive lower comparison. -/
theorem neutralCarrier_logEnergy_of_operatorDomain
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (a : ℝ)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (L shift : ℝ) (hL : 0 < L)
    (hlower : ∀ ξ, L * logarithmicFourierWeight ξ ≤
      rightLimitCompactWeilSymbolMathlib a ξ + shift) :
    Integrable (fun ξ => logarithmicFourierWeight ξ *
      ‖(𝓕 carrier.l2Mode : RealComplexL2) ξ‖ ^ 2) volume :=
  finiteLogEnergy_of_spectralProduct (rightLimitCompactWeilSymbolMathlib a)
    (𝓕 carrier.l2Mode : RealComplexL2) (Lp.memLp _) hp L shift hL hlower

/-- The spectral route now constructs the canonical form-domain attachment
without an additional carrier log-energy premise. Source identity is separate. -/
def neutralCanonicalSourceFormDomain_of_operatorDomain
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c ≤ a)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (L shift : ℝ) (hL : 0 < L)
    (hlower : ∀ ξ, L * logarithmicFourierWeight ξ ≤
      rightLimitCompactWeilSymbolMathlib a ξ + shift) :
    NeutralSourceFormDomainAttachment carrier a :=
  neutralCanonicalSourceFormDomainAttachment carrier hca
    (neutralCarrier_logEnergy_of_operatorDomain carrier a hp L shift hL hlower)

end

end WeilDefect
