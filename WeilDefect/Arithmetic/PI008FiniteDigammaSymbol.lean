import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open scoped BigOperators

/-!
PI008: finite rational digamma/Gamma symbol pilot.
This is only the finite partial-fraction object; it is not a proof of its
convergence to the genuine Zeta23 gammaBracket, the Fourier-atom identity,
or the archimedean integral. It does NOT import the original IV011 module
from the independent IV branch. All declarations are real Lean candidates;
compilation and strict axiom audit are required before claiming acceptance.
-/

/-- Real part of one inverse-frequency digamma atom at r/2, with a=n+1/4. -/
def pi008GammaRationalAtom (n : ℕ) (r : ℝ) : ℝ :=
  let a : ℝ := (n : ℝ) + 1 / 4
  a / (a ^ 2 + (r / 2) ^ 2)

/-- The exact real finite partial-fraction symbol, including constant terms. -/
def pi008FiniteDigammaSymbol (N : ℕ) (r : ℝ) : ℝ :=
  - Real.eulerMascheroniConstant - Real.log Real.pi +
    ∑ n ∈ Finset.range N,
      (1 / ((n : ℝ) + 1) - pi008GammaRationalAtom n r)

/-- The individual real-frequency rational atom is nonnegative. -/
theorem pi008GammaRationalAtom_nonneg (n : ℕ) (r : ℝ) :
    0 ≤ pi008GammaRationalAtom n r := by
  dsimp [pi008GammaRationalAtom]
  positivity

/-- A rational digamma atom is an even function of angular frequency. -/
theorem pi008GammaRationalAtom_even (n : ℕ) (r : ℝ) :
    pi008GammaRationalAtom n (-r) = pi008GammaRationalAtom n r := by
  simp [pi008GammaRationalAtom]

/-- N=0 gives just the source's constant Gamma bracket subtraction. -/
theorem pi008FiniteDigammaSymbol_zero (r : ℝ) :
    pi008FiniteDigammaSymbol 0 r =
      - Real.eulerMascheroniConstant - Real.log Real.pi := by
  simp [pi008FiniteDigammaSymbol]

/-- Each new finite stage adds exactly one explicit digamma fraction. -/
theorem pi008FiniteDigammaSymbol_succ (N : ℕ) (r : ℝ) :
    pi008FiniteDigammaSymbol (N + 1) r =
      pi008FiniteDigammaSymbol N r +
        (1 / ((N : ℝ) + 1) - pi008GammaRationalAtom N r) := by
  simp only [pi008FiniteDigammaSymbol, Finset.sum_range_succ]
  ring

/-- The finite symbol is even, consistent with the original Gamma bracket. -/
theorem pi008FiniteDigammaSymbol_even (N : ℕ) (r : ℝ) :
    pi008FiniteDigammaSymbol N (-r) =
      pi008FiniteDigammaSymbol N r := by
  simp [pi008FiniteDigammaSymbol, pi008GammaRationalAtom_even]

#print axioms pi008GammaRationalAtom_nonneg
#print axioms pi008GammaRationalAtom_even
#print axioms pi008FiniteDigammaSymbol_zero
#print axioms pi008FiniteDigammaSymbol_succ
#print axioms pi008FiniteDigammaSymbol_even

end
end WeilDefect
