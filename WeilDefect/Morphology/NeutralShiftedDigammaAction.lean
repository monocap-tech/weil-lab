import WeilDefect.Morphology.NeutralGaussMultiplier

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped FourierTransform SchwartzMap BigOperators

/-- Actual shifted digamma tail at the fixed mathlib frequency normalization. -/
def neutralShiftedDigammaSymbol (N : ℕ) (ξ : ℝ) : ℂ :=
  ((Complex.digamma (neutralDigammaLine (2*Real.pi*ξ) + (N : ℂ))).re -
    Real.log Real.pi : ℝ)

/-- Finite recurrence as an equality of the actual multiplier functions. -/
theorem neutralShiftedDigammaSymbol_eq_add (N : ℕ) :
    neutralShiftedDigammaSymbol N =
      (fun ξ : ℝ => (compactWindowArchimedeanSymbol (2*Real.pi*ξ) : ℂ)) +
      (fun ξ : ℝ => ((∑ n ∈ Finset.range N,
        neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) : ℂ)) := by
  ext ξ
  have h := neutralArchimedeanSymbol_finite_tail N (2*Real.pi*ξ)
  simp only [Pi.add_apply, neutralShiftedDigammaSymbol]
  have hr : (Complex.digamma (neutralDigammaLine (2*Real.pi*ξ) + (N : ℂ))).re -
      Real.log Real.pi = compactWindowArchimedeanSymbol (2*Real.pi*ξ) +
        ∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) := by
    linarith
  rw [hr, Complex.ofReal_add]

/-- No new growth premise: inherit the retained full-symbol premise and the
proved finite Gauss growth. This does not supply a bound uniform in N. -/
theorem neutralShiftedDigammaSymbol_temperate (N : ℕ) (a : ℝ)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) :
    Function.HasTemperateGrowth (neutralShiftedDigammaSymbol N) := by
  rw [neutralShiftedDigammaSymbol_eq_add]
  exact (neutralArchimedeanSymbol_temperate a hSymbol).add
    (neutralFiniteGaussSymbol_temperate N)

/-- Existing distributional Fourier action of the actual shifted tail. -/
def neutralShiftedDigammaAction (N : ℕ) (f : RealComplexTempered) : RealComplexTempered :=
  TemperedDistribution.fourierMultiplierCLM ℂ (neutralShiftedDigammaSymbol N) f

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Exact finite operator split on every Schwartz test, with the physical
convolution subtracted as required by the actual digamma recurrence. -/
theorem neutralArchimedeanMultiplierCore_eq_shifted_sub_convolution
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (N : ℕ) (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) :
    neutralArchimedeanMultiplierCore carrier.temperedMode u =
      neutralShiftedDigammaAction N carrier.temperedMode u -
        ∫ x, u x * neutralFiniteGaussConvolution carrier N x := by
  have hadd : neutralShiftedDigammaAction N carrier.temperedMode u =
      neutralArchimedeanMultiplierCore carrier.temperedMode u +
        TemperedDistribution.fourierMultiplierCLM ℂ
          (fun ξ : ℝ => ((∑ n ∈ Finset.range N,
            neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) : ℂ)) carrier.temperedMode u := by
    unfold neutralShiftedDigammaAction neutralArchimedeanMultiplierCore
    rw [neutralShiftedDigammaSymbol_eq_add]
    simp only [TemperedDistribution.fourierMultiplierCLM_apply_apply,
      SchwartzMap.smulLeftCLM_add (neutralArchimedeanSymbol_temperate a hSymbol)
        (neutralFiniteGaussSymbol_temperate N), ContinuousLinearMap.add_apply,
      FourierTransform.fourier_add, map_add]
  rw [neutralFiniteGaussMultiplier_physical_pairing] at hadd
  rw [hadd]
  ring

/-- The actual whole multiplier core now has only one unidentified action:
the shifted digamma tail. Both finite physical terms genuinely converge. -/
theorem neutralWeilMultiplierCore_eq_shifted_sub_physical
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (N : ℕ) (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) :
    rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode u =
      neutralShiftedDigammaAction N carrier.temperedMode u -
        (∫ x, u x * neutralFiniteGaussConvolution carrier N x) -
        ∫ x, u x * neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x := by
  rw [neutralWeilMultiplierCore_eq_archimedean_sub_prime carrier a hSymbol u,
    neutralArchimedeanMultiplierCore_eq_shifted_sub_convolution carrier N a hSymbol u]

end

end WeilDefect
