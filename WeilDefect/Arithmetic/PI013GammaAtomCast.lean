import WeilDefect.Arithmetic.PI008FiniteDigammaSymbol
import WeilDefect.Arithmetic.PI012SourceFourierAtom
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
PI013 exact PI012 Fourier closed-form ↔ literal PI008 Gamma rational atom.

All source names are real imports from the independent PI### stack. This
module does not import or assert a theorem about the IV011 source on the
separate IV### branch.

CANDIDATE only: Lean build and strict #print axioms receipts pending.
-/

/-- Exact exponential damping for the nth source Gamma partial fraction. -/
def pi013GammaDamping (n : ℕ) : ℝ :=
  2 * ((n : ℝ) + 1 / 4)

/-- The positive damping hypothesis needed by PI012's Fourier integral. -/
theorem pi013GammaDamping_pos (n : ℕ) :
    0 < pi013GammaDamping n := by
  unfold pi013GammaDamping
  positivity

/-- Match PI007's physical exponent without changing its normalization. -/
theorem pi013GammaDamping_eq (n : ℕ) :
    pi013GammaDamping n = 2 * (n : ℝ) + 1 / 2 := by
  unfold pi013GammaDamping
  ring

/-- Positive source Gamma Fourier atom, as an exact REAL rational identity. -/
theorem pi013RealGammaAtom (n : ℕ) (r : ℝ) :
    (2 * pi013GammaDamping n) /
        ((pi013GammaDamping n) ^ 2 + r ^ 2) =
      pi008GammaRationalAtom n r := by
  have ha : 0 < (n : ℝ) + 1 / 4 := by positivity
  have hd1 :
      (2 * ((n : ℝ) + 1 / 4)) ^ 2 + r ^ 2 ≠ 0 := by
    have hpos : 0 < (2 * ((n : ℝ) + 1 / 4)) ^ 2 + r ^ 2 := by
      positivity
    exact ne_of_gt hpos
  have hd2 :
      ((n : ℝ) + 1 / 4) ^ 2 + (r / 2) ^ 2 ≠ 0 := by
    have hpos : 0 < ((n : ℝ) + 1 / 4) ^ 2 + (r / 2) ^ 2 := by
      positivity
    exact ne_of_gt hpos
  dsimp [pi013GammaDamping, pi008GammaRationalAtom]
  field_simp
  <;> ring

/-- The Fourier transform of each genuine physical exponential is REAL,
and equals PI008's exact digamma rational atom, with positive Fourier sign. -/
theorem pi013ComplexGammaAtom (n : ℕ) (r : ℝ) :
    (2 * (pi013GammaDamping n : ℂ)) /
        ((pi013GammaDamping n : ℂ) ^ 2 + (r : ℂ) ^ 2) =
      (pi008GammaRationalAtom n r : ℂ) := by
  exact_mod_cast pi013RealGammaAtom n r

/-- The source-positive whole-line Fourier integral equals the authentic
PI008 Gamma atom, retaining its complex coercion explicitly. -/
theorem pi013FourierIntegralGammaAtom (n : ℕ) (r : ℝ) :
    (∫ u : ℝ, pi011PhysicalFourierAtom (pi013GammaDamping n) r u) =
      (pi008GammaRationalAtom n r : ℂ) := by
  rw [pi012WholeLineFourierClosed (pi013GammaDamping n) r
    (pi013GammaDamping_pos n)]
  exact pi013ComplexGammaAtom n r

#print axioms pi013GammaDamping_pos
#print axioms pi013GammaDamping_eq
#print axioms pi013RealGammaAtom
#print axioms pi013ComplexGammaAtom
#print axioms pi013FourierIntegralGammaAtom

end
end WeilDefect
