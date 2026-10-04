import WeilDefect.Arithmetic.ActualZetaPrimeTransport
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_WeilEF_digamma_conj

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate
set_option maxHeartbeats 800000

/-- The same C² inverse correlation has the already constructed mixed spectrum. -/
theorem neutralActualZetaGreenCorrelationInverse_fourier_ae
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (𝓕 (neutralActualZetaGreenCorrelationInverse a v w)) =ᵐ[volume]
      neutralActualZetaGreenCorrelationSpectrum a v w := by
  have h : (𝓕 (neutralActualZetaGreenCorrelationInverse a v w)) =
      𝓕 (neutralWindowCorrelation a
        (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w)) := by
    funext ξ
    exact Real.fourier_congr_ae
      (neutralActualZetaGreenCorrelationInverse_ae a ha v w) ξ
  rw [h]
  exact neutralActualZetaGreenCorrelation_fourier_spectrum_ae a ha v w

/-- Absolute integrability is inherited from the same concrete spectrum. -/
theorem neutralActualZetaGreenCorrelationInverse_fourier_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (𝓕 (neutralActualZetaGreenCorrelationInverse a v w)) :=
  (neutralActualZetaGreenCorrelationSpectrum_integrable a v w).congr
    (neutralActualZetaGreenCorrelationInverse_fourier_ae a ha v w).symm

/-- Raw real-frequency samples at the fixed negative 2π coordinate equal
the same spectrum almost everywhere. -/
theorem neutralActualZetaGreenCorrelationInverse_raw_spectrum_ae
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (fun ξ : ℝ => neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w)
      ((-2 * Real.pi * ξ : ℝ) : ℂ)) =ᵐ[volume]
      neutralActualZetaGreenCorrelationSpectrum a v w := by
  filter_upwards [neutralActualZetaGreenCorrelationInverse_fourier_ae a ha v w]
    with ξ hξ
  rw [← neutralRawTransform_fourier]
  exact hξ

/-- Conjugation symmetry of digamma gives an even real gamma bracket. -/
theorem neutralActualZetaGammaBracket_even (r : ℝ) :
    Zeta23.EF.gammaBracket (-r) = Zeta23.EF.gammaBracket r := by
  let z : ℂ := 1 / 4 + Complex.I * (r : ℂ) / 2
  have hz : z ∈ Complex.integerComplement := by
    rintro ⟨k, hk⟩
    have he := congrArg Complex.re hk
    change (k : ℝ) = (1 / 4 + Complex.I * (r : ℂ) / 2).re at he
    simp at he
    have h4 : (4 * k : ℤ) = (1 : ℤ) := by
      have : (4 : ℝ) * k = 1 := by rw [he]; norm_num
      exact_mod_cast this
    omega
  have hc : 1 / 4 + Complex.I * ((-r : ℝ) : ℂ) / 2 = conj z := by
    simp only [z, map_add, map_div₀, map_one, map_ofNat,
      Complex.conj_I, Complex.conj_ofReal, map_mul, Complex.ofReal_neg]
    ring
  unfold Zeta23.EF.gammaBracket
  rw [hc, Zeta23.WeilEF.digamma_conj hz]
  rfl

/-- The external gamma bracket uses exactly the native archimedean symbol. -/
theorem neutralActualZetaGammaBracket_native (r : ℝ) :
    Zeta23.EF.gammaBracket r = compactWindowArchimedeanSymbol r := by
  unfold Zeta23.EF.gammaBracket compactWindowArchimedeanSymbol
  congr 2
  ring

/-- The negative 2π Fourier coordinate has the positive native symbol,
with the sign removed by proved gamma symmetry. -/
theorem neutralActualZetaGammaBracket_mathlib (ξ : ℝ) :
    Zeta23.EF.gammaBracket (-2 * Real.pi * ξ) =
      compactWindowArchimedeanSymbol (2 * Real.pi * ξ) := by
  have h : -2 * Real.pi * ξ = -(2 * Real.pi * ξ) := by ring
  rw [h, neutralActualZetaGammaBracket_even, neutralActualZetaGammaBracket_native]

end
end WeilDefect
