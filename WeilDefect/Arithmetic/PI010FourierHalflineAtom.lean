import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set

/-!
PI010 source-specific half-line Fourier atom bridge.

Genuine Lean proof candidate using Mathlib v4.34.0 theorems
integral_exp_mul_complex_Ioi and integral_exp_mul_complex_Iic,
with the positive angular Fourier sign of Zeta23.paperFT.

The whole-real-line split, rational simplification and connection to
the authentic IV011 source remain separate proof obligations.

COMPILER STATUS: pending direct-target CI and axiom receipt.
-/

/-- Positive-half-line exponent in source positive-Fourier convention. -/
def pi010PositiveExponent (α r : ℝ) : ℂ :=
  -(α : ℂ) + Complex.I * (r : ℂ)

/-- Negative-half-line exponent after removing absolute value. -/
def pi010NegativeExponent (α r : ℝ) : ℂ :=
  (α : ℂ) + Complex.I * (r : ℂ)

/-- The positive-half-line exponent has real part -α. -/
theorem pi010PositiveExponent_re (α r : ℝ) :
    (pi010PositiveExponent α r).re = -α := by
  simp [pi010PositiveExponent, Complex.mul_re]

/-- The negative-half-line exponent has real part α. -/
theorem pi010NegativeExponent_re (α r : ℝ) :
    (pi010NegativeExponent α r).re = α := by
  simp [pi010NegativeExponent, Complex.mul_re]

/-- Exact complex integral over (0,∞), with positive Fourier sign. -/
theorem pi010PositiveHalflineIntegral (α r : ℝ) (hα : 0 < α) :
    (∫ u : ℝ in Ioi (0 : ℝ),
      Complex.exp (pi010PositiveExponent α r * (u : ℂ))) =
      -(1 : ℂ) / pi010PositiveExponent α r := by
  have hneg : (pi010PositiveExponent α r).re < 0 := by
    rw [pi010PositiveExponent_re]
    exact neg_lt_zero.mpr hα
  simpa using
    (integral_exp_mul_complex_Ioi
      (a := pi010PositiveExponent α r) hneg (0 : ℝ))

/-- Exact complex integral over (-∞,0], with positive Fourier sign. -/
theorem pi010NegativeHalflineIntegral (α r : ℝ) (hα : 0 < α) :
    (∫ u : ℝ in Iic (0 : ℝ),
      Complex.exp (pi010NegativeExponent α r * (u : ℂ))) =
      (1 : ℂ) / pi010NegativeExponent α r := by
  have hpos : 0 < (pi010NegativeExponent α r).re := by
    rw [pi010NegativeExponent_re]
    exact hα
  simpa using
    (integral_exp_mul_complex_Iic
      (a := pi010NegativeExponent α r) hpos (0 : ℝ))

/-- Genuine half-line integrals evaluated using accepted Mathlib theorems.
The full-real-line assembly is not included in this assertion. -/
theorem pi010HalflineIntegralPair (α r : ℝ) (hα : 0 < α) :
    (∫ u : ℝ in Ioi (0 : ℝ),
      Complex.exp (pi010PositiveExponent α r * (u : ℂ))) +
    (∫ u : ℝ in Iic (0 : ℝ),
      Complex.exp (pi010NegativeExponent α r * (u : ℂ))) =
      -(1 : ℂ) / pi010PositiveExponent α r +
      (1 : ℂ) / pi010NegativeExponent α r := by
  rw [pi010PositiveHalflineIntegral α r hα,
    pi010NegativeHalflineIntegral α r hα]

#print axioms pi010PositiveExponent_re
#print axioms pi010NegativeExponent_re
#print axioms pi010PositiveHalflineIntegral
#print axioms pi010NegativeHalflineIntegral
#print axioms pi010HalflineIntegralPair

end
end WeilDefect
