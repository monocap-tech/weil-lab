import WeilDefect.Morphology.NeutralExteriorResidual

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped BigOperators SchwartzMap FourierTransform Real

/-- Finite prime symbol in the exact mathlib frequency coordinate. -/
def neutralFinitePrimeSymbol (S : Finset ℕ) (ξ : ℝ) : ℝ :=
  ∑ n ∈ S, compactWindowPrimeCoefficient n *
    Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ))

theorem neutralFinitePrimeSymbol_temperate (S : Finset ℕ) :
    Function.HasTemperateGrowth (fun ξ : ℝ => (neutralFinitePrimeSymbol S ξ : ℂ)) := by
  simp only [neutralFinitePrimeSymbol, Complex.ofReal_sum, Complex.ofReal_mul]
  fun_prop

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Full finite prime action, not only a difference shell, on every Schwartz test. -/
theorem neutralFinitePrime_fourier_physical_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) (u : SchwartzMap ℝ ℂ) :
    TemperedDistribution.fourierMultiplierCLM ℂ
        (fun ξ : ℝ => (neutralFinitePrimeSymbol S ξ : ℂ))
        carrier.temperedMode u =
      ∫ x : ℝ, u x * neutralFinitePrimePhysical carrier S x ∂volume := by
  let g (n : ℕ) (ξ : ℝ) : ℂ :=
    (compactWindowPrimeCoefficient n : ℂ) *
      (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)
  have hg (n : ℕ) : Function.HasTemperateGrowth (g n) := by
    dsimp [g]
    fun_prop
  have heq : (fun ξ : ℝ => (neutralFinitePrimeSymbol S ξ : ℂ)) =
      (fun ξ : ℝ => ∑ n ∈ S, g n ξ) := by
    ext ξ
    simp [neutralFinitePrimeSymbol, g]
  rw [heq, TemperedDistribution.fourierMultiplierCLM_sum ℂ (fun n _ => hg n)]
  simp only [sum_apply]
  have hterm (n : ℕ) :
      TemperedDistribution.fourierMultiplierCLM ℂ (g n) carrier.temperedMode u =
        ∫ x : ℝ, u x * ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
          (carrier.h (x - Real.log (n : ℝ)) + carrier.h (x + Real.log (n : ℝ)))
          ∂volume := by
    have hc : Function.HasTemperateGrowth
        (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)) := by
      fun_prop
    change TemperedDistribution.fourierMultiplierCLM ℂ
      ((compactWindowPrimeCoefficient n : ℂ) •
        (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)))
      carrier.temperedMode u = _
    rw [TemperedDistribution.fourierMultiplierCLM_smul hc]
    simp only [smul_apply, smul_eq_mul]
    rw [cosineFourierMultiplier_physical_pairing]
    have hm : Integrable (fun x : ℝ => u x * carrier.h (x - Real.log (n : ℝ))) volume := by
      simpa only [sub_eq_add_neg] using
        neutralPhysical_shift_pairing_integrable carrier u (-Real.log (n : ℝ))
    have hp := neutralPhysical_shift_pairing_integrable carrier u (Real.log (n : ℝ))
    have hf : (fun x : ℝ => u x * ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
        (carrier.h (x - Real.log (n : ℝ)) + carrier.h (x + Real.log (n : ℝ)))) =
        (fun x : ℝ => ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
          (u x * carrier.h (x - Real.log (n : ℝ)) + u x * carrier.h (x + Real.log (n : ℝ)))) := by
      ext x
      ring
    rw [hf, integral_const_mul, integral_add hm hp]
    push_cast
    ring
  simp_rw [hterm]
  rw [← integral_finsetSum (S)
    (fun n _ => frozenWeilPrimeShell_term_pairing_integrable carrier u n)]
  apply integral_congr_ae
  filter_upwards with x
  simp [neutralFinitePrimePhysical, Finset.mul_sum, mul_assoc]


/-- The actual full finite prime pairing genuinely converges. -/
theorem neutralFinitePrime_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) (u : SchwartzMap ℝ ℂ) :
    Integrable (fun x : ℝ => u x * neutralFinitePrimePhysical carrier S x) volume := by
  have h := integrable_finsetSum S
    (fun n _ => frozenWeilPrimeShell_term_pairing_integrable carrier u n)
  simpa [neutralFinitePrimePhysical, Finset.mul_sum, mul_assoc] using h

/-- The exact archimedean multiplier action. Its physical kernel attachment
remains open; this definition does not assert a Gauss representation. -/
def neutralArchimedeanMultiplierCore (f : RealComplexTempered) : RealComplexTempered :=
  TemperedDistribution.fourierMultiplierCLM ℂ
    (fun ξ : ℝ => (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ)) f

theorem neutralArchimedeanSymbol_eq_core_add_prime (a : ℝ) :
    (fun ξ : ℝ => (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ)) =
      (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ)) +
      (fun ξ : ℝ => (neutralFinitePrimeSymbol (rightLimitPrimePowerFinset a) ξ : ℂ)) := by
  ext ξ
  simp only [Pi.add_apply, rightLimitCompactWeilSymbolMathlib,
    rightLimitCompactWeilSymbol, rightLimitPrimeSymbol, neutralFinitePrimeSymbol,
    Complex.ofReal_sub]
  ring

/-- Archimedean temperate growth is derived from the retained actual full-symbol
premise and the proved finite prime growth; no additional source premise. -/
theorem neutralArchimedeanSymbol_temperate
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a) :
    Function.HasTemperateGrowth
      (fun ξ : ℝ => (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ)) := by
  rw [neutralArchimedeanSymbol_eq_core_add_prime a]
  exact hSymbol.hasTemperateGrowth.add (neutralFinitePrimeSymbol_temperate _)

/-- Exact actual multiplier-core split with the full physical prime part.
The only unidentified physical multiplier part is now archimedean. -/
theorem neutralWeilMultiplierCore_eq_archimedean_sub_prime
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) :
    rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode u =
      neutralArchimedeanMultiplierCore carrier.temperedMode u -
        ∫ x, u x * neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x := by
  have hadd :
      neutralArchimedeanMultiplierCore carrier.temperedMode u =
        rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode u +
          TemperedDistribution.fourierMultiplierCLM ℂ
            (fun ξ : ℝ => (neutralFinitePrimeSymbol (rightLimitPrimePowerFinset a) ξ : ℂ))
            carrier.temperedMode u := by
    unfold neutralArchimedeanMultiplierCore rightLimitWeilMultiplierCore
    rw [neutralArchimedeanSymbol_eq_core_add_prime a]
    simp only [TemperedDistribution.fourierMultiplierCLM_apply_apply,
      SchwartzMap.smulLeftCLM_add hSymbol.hasTemperateGrowth
        (neutralFinitePrimeSymbol_temperate _),
      ContinuousLinearMap.add_apply, FourierTransform.fourier_add, map_add]
  rw [neutralFinitePrime_fourier_physical_pairing] at hadd
  rw [hadd]
  ring

end

end WeilDefect
