import WeilDefect.Arithmetic.PI012ComplexRationalIdentity
import WeilDefect.Arithmetic.PI011WholeLineFourierAtom
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
PI012 source-oriented whole-line Fourier atom closure CANDIDATES.

The PI011 integral and PI010 exponent definitions remain actual dependencies.
This file does not import IV011, which only exists on the independent IV lane.

Theorems require completed direct-target Lean/.olean/#print axioms receipts
before being marked accepted. No claims about Masullo's operator trace.
-/

/-- Source half-line fractions coincide with the exact real-denominator
Fourier rational expression, including the original positive frequency sign. -/
theorem pi012SourceFractionsClosed (α r : ℝ) (hα : 0 < α) :
    -(1 : ℂ) / pi010PositiveExponent α r +
      (1 : ℂ) / pi010NegativeExponent α r =
        (2 * (α : ℂ)) / ((α : ℂ) ^ 2 + (r : ℂ) ^ 2) := by
  have hm :
      pi010PositiveExponent α r =
        -((α : ℂ) - Complex.I * (r : ℂ)) := by
    unfold pi010PositiveExponent
    ring
  calc
    _ = (1 : ℂ) / ((α : ℂ) - Complex.I * (r : ℂ)) +
        (1 : ℂ) / ((α : ℂ) + Complex.I * (r : ℂ)) := by
      rw [hm]
      simp [pi010NegativeExponent, div_neg]
    _ = (2 * (α : ℂ)) / ((α : ℂ) ^ 2 + (r : ℂ) ^ 2) :=
      pi012FourierReciprocalClosed α r hα

/-- Complete original-positive-sign Fourier exponential atom:
the integral is evaluated, not merely identified with two half-line integrals. -/
theorem pi012WholeLineFourierClosed (α r : ℝ) (hα : 0 < α) :
    (∫ u : ℝ, pi011PhysicalFourierAtom α r u) =
      (2 * (α : ℂ)) / ((α : ℂ) ^ 2 + (r : ℂ) ^ 2) := by
  calc
    (∫ u : ℝ, pi011PhysicalFourierAtom α r u) =
        -(1 : ℂ) / pi010PositiveExponent α r +
          (1 : ℂ) / pi010NegativeExponent α r :=
      pi011Physical_whole_integral α r hα
    _ = (2 * (α : ℂ)) / ((α : ℂ) ^ 2 + (r : ℂ) ^ 2) :=
      pi012SourceFractionsClosed α r hα

#print axioms pi012SourceFractionsClosed
#print axioms pi012WholeLineFourierClosed

end
end WeilDefect
