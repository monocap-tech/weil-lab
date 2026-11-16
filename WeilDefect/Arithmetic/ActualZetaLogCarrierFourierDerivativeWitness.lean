import WeilDefect.Arithmetic.ActualZetaLogCarrierQuadraticMoment
import Mathlib.MeasureTheory.Function.LpSpace.Indicator

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform

/-!
NF541: the exact L² Fourier-derivative witness needed to discharge the
NF540 quadratic-moment hypothesis without postulating weighted-domain
membership. The scalar derivative is normalized by 1/(2*pi).

The final bridge from an actual compact C² test to the witness is a
separate Fourier integral -> Fourier L² identification obligation.
-/

/-- An actual L² frequency-derivative witness discharges the full
quadratic Fourier moment for the SAME physical vector. The witness
has squared Fourier norm ξ² times the original squared Fourier norm,
as supplied by the usual 2π-normalized derivative identity. -/
theorem neutralQuadraticFourierMoment_of_derivativeWitness
    (f df : RealComplexL2)
    (hDerivative : ∀ᵐ ξ ∂volume,
      ‖(𝓕 df : RealComplexL2) ξ‖ ^ 2 =
        ξ ^ 2 * ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) :
    Integrable (fun ξ : ℝ =>
      (Real.exp 1 + 1 + ξ ^ 2) *
        ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume := by
  have hf : Integrable (fun ξ : ℝ =>
      ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume :=
    (memLp_two_iff_integrable_sq_norm
      (Lp.aestronglyMeasurable (𝓕 f : RealComplexL2))).mp (Lp.memLp _)
  have hd : Integrable (fun ξ : ℝ =>
      ‖(𝓕 df : RealComplexL2) ξ‖ ^ 2) volume :=
    (memLp_two_iff_integrable_sq_norm
      (Lp.aestronglyMeasurable (𝓕 df : RealComplexL2))).mp (Lp.memLp _)
  have hsum : Integrable (fun ξ : ℝ =>
      (Real.exp 1 + 1) * ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2 +
        ‖(𝓕 df : RealComplexL2) ξ‖ ^ 2) volume :=
    (hf.const_mul (Real.exp 1 + 1)).add hd
  apply hsum.congr
  filter_upwards [hDerivative] with ξ hξ
  rw [hξ]
  ring

/-- Same physical source, exact support and original logarithmic Hilbert
reconstruction, replacing NF540's assumed quadratic moment by an L²
Fourier-derivative witness. This theorem does not assume a synthesized
Green packet or change any original arithmetic source. -/
theorem neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_derivativeWitness
    (a : ℝ) (f df : RealComplexL2)
    (hsupport : ∀ᵐ x ∂volume,
      x ∉ Set.Icc (-a) a → f x = 0)
    (hDerivative : ∀ᵐ ξ ∂volume,
      ‖(𝓕 df : RealComplexL2) ξ‖ ^ 2 =
        ξ ^ 2 * ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) :
    ∃ k : NeutralLogHilbertCarrier a, neutralLogPhysical k.val = f := by
  exact neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
    a f hsupport (neutralQuadraticFourierMoment_of_derivativeWitness f df hDerivative)

/-- For a genuine compact C² physical representative, exact inclusion in
the original supported log Hilbert carrier follows from its genuine L²
Fourier differentiation identity. The representative is inserted into
L² a.e.; no claim is made that all representatives are pointwise smooth.
The outstanding formal step is to PRODUCE df and hDerivative from ψ'. -/
theorem neutralCompactSmoothL2_hasOriginalLogHilbertCarrier_of_derivativeWitness
    (a : ℝ) (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ 2 ψ) (hc : HasCompactSupport ψ)
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → ψ x = 0)
    (df : RealComplexL2)
    (hDerivative : ∀ᵐ ξ ∂volume,
      ‖(𝓕 df : RealComplexL2) ξ‖ ^ 2 =
        ξ ^ 2 * ‖(𝓕
          ((hψ.continuous.memLp_of_hasCompactSupport hc).toLp ψ :
            RealComplexL2) : RealComplexL2) ξ‖ ^ 2) :
    ∃ k : NeutralLogHilbertCarrier a,
      neutralLogPhysical k.val =
        (hψ.continuous.memLp_of_hasCompactSupport hc).toLp ψ := by
  let hmem : MemLp ψ 2 volume :=
    hψ.continuous.memLp_of_hasCompactSupport hc
  let g : RealComplexL2 := hmem.toLp ψ
  have hsource : (g : ℝ → ℂ) =ᵐ[volume] ψ := hmem.coeFn_toLp
  have hsupport : ∀ᵐ x ∂volume,
      x ∉ Set.Icc (-a) a → g x = 0 := by
    filter_upwards [hsource] with x hx hout
    rw [hx]
    exact hs x hout
  exact neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_derivativeWitness
    a g df hsupport hDerivative

end
end WeilDefect
