import WeilDefect.Morphology.NeutralFourierCarrier
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Analysis.Distribution.FourierMultiplier
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt

namespace WeilDefect

noncomputable section

open scoped BigOperators ArithmeticFunction SchwartzMap FourierTransform

/--
Finite prime-power set for the strict-right compact-window operator.

Unlike `activePrimePowerFinset`, this uses the right-limit convention
`log n ≤ 2a`, so an equality-threshold prime power is retained.
-/
def rightLimitPrimePowerFinset (a : ℝ) : Finset ℕ :=
  (wd_t38_p3_u3_right_limit_prime_support_finite a).1.toFinset

@[simp]
theorem mem_rightLimitPrimePowerFinset
    (a : ℝ) (n : ℕ) :
    n ∈ rightLimitPrimePowerFinset a ↔
      IsPrimePow n ∧ Real.log (n : ℝ) ≤ 2 * a := by
  simp [rightLimitPrimePowerFinset, rightLimitPrimePowers]

/--
Archimedean scalar part of the compact-window Weil symbol:
`Re ψ(1/4 + it/2) - log π`.
-/
def compactWindowArchimedeanSymbol (t : ℝ) : ℝ :=
  (Complex.digamma
    (((1 : ℂ) / 4) + Complex.I * ((t : ℂ) / 2))).re
    - Real.log Real.pi

/-- Exact von Mangoldt coefficient `2 Λ(n) / sqrt(n)`. -/
def compactWindowPrimeCoefficient (n : ℕ) : ℝ :=
  2 * ArithmeticFunction.vonMangoldt n / Real.sqrt (n : ℝ)

/--
Threshold-corrected finite prime trigonometric part of the strict-right
compact-window symbol.
-/
def rightLimitPrimeSymbol (a t : ℝ) : ℝ :=
  Finset.sum (rightLimitPrimePowerFinset a)
    (fun n =>
      compactWindowPrimeCoefficient n
        * Real.cos (t * Real.log (n : ℝ)))

/--
Exact scalar symbol used by the strict-right compact-window Weil operator,
with the finite-rank pole/evaluation contribution kept separate.

This is only the scalar multiplier component.  It does not identify a
compressed-window kernel vector with a pointwise zero of this symbol.
-/
def rightLimitCompactWeilSymbol (a t : ℝ) : ℝ :=
  compactWindowArchimedeanSymbol t - rightLimitPrimeSymbol a t

theorem rightLimitCompactWeilSymbol_eq
    (a t : ℝ) :
    rightLimitCompactWeilSymbol a t =
      compactWindowArchimedeanSymbol t
        - Finset.sum (rightLimitPrimePowerFinset a)
            (fun n =>
              compactWindowPrimeCoefficient n
                * Real.cos (t * Real.log (n : ℝ))) := by
  rfl


/--
Strict-right compact-window Weil symbol in mathlib's real Fourier coordinate.

The pinned source symbol uses the source frequency `t`, while mathlib's
Fourier transform uses `exp (-2 * pi * i * x * xi)`. Hence physical
translations at shifts `± log n` require the coordinate map

`t = 2 * pi * xi`.
-/
def rightLimitCompactWeilSymbolMathlib (a ξ : ℝ) : ℝ :=
  rightLimitCompactWeilSymbol a (2 * Real.pi * ξ)

theorem rightLimitCompactWeilSymbolMathlib_eq
    (a ξ : ℝ) :
    rightLimitCompactWeilSymbolMathlib a ξ =
      compactWindowArchimedeanSymbol (2 * Real.pi * ξ)
        - Finset.sum (rightLimitPrimePowerFinset a)
            (fun n =>
              compactWindowPrimeCoefficient n
                * Real.cos
                    ((2 * Real.pi * ξ) * Real.log (n : ℝ))) := by
  rfl

/-- Every strict-active prime power is retained by the right-limit symbol. -/
theorem active_mem_rightLimitPrimePowerFinset
    {a : ℝ} {n : ℕ}
    (hn : n ∈ activePrimePowerFinset a) :
    n ∈ rightLimitPrimePowerFinset a := by
  rw [mem_activePrimePowerFinset] at hn
  rw [mem_rightLimitPrimePowerFinset]
  exact ⟨hn.1, le_of_lt hn.2⟩

/-- An equality-threshold prime power is retained by the right-limit symbol. -/
theorem threshold_mem_rightLimitPrimePowerFinset
    {a : ℝ} {n : ℕ}
    (hn : n ∈ primePowerThreshold a) :
    n ∈ rightLimitPrimePowerFinset a := by
  change IsPrimePow n ∧ Real.log (n : ℝ) = 2 * a at hn
  rw [mem_rightLimitPrimePowerFinset]
  exact ⟨hn.1, le_of_eq hn.2⟩


/--
Explicit imported F-2 premise for the exact strict-right scalar symbol in
mathlib Fourier coordinates.

Mathlib's `HasTemperateGrowth` requires smoothness and polynomial control of
every iterated derivative.  EXT-5 gives the zeroth-order digamma asymptotic;
EXT-5D (DLMF 5.15.9) supplies the corresponding polygamma derivative
asymptotics.  The project keeps that special-function input explicit rather
than reconstructing it internally in this pass.
-/
structure RightLimitWeilSymbolTemperatePremise (a : ℝ) : Prop where
  hasTemperateGrowth :
    Function.HasTemperateGrowth
      (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ))

/--
Canonical tempered-distribution realization of the exact strict-right scalar
multiplier in mathlib Fourier coordinates, conditional on the explicit
EXT-5D temperate-growth premise.

The proof parameter is semantically load-bearing: it certifies that mathlib's
Schwartz multiplication branch is the genuine pointwise multiplier rather
than the fallback zero map.
-/
noncomputable def rightLimitWeilMultiplierCore
    (a : ℝ)
    (_hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (f : RealComplexTempered) :
    RealComplexTempered :=
  TemperedDistribution.fourierMultiplierCLM ℂ
    (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ))
    f


end

end WeilDefect
