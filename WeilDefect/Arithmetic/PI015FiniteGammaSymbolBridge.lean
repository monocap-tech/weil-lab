import WeilDefect.Arithmetic.PI014KernelCharacterBridge
import WeilDefect.Arithmetic.PI008FiniteDigammaSymbol
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open scoped BigOperators

/-!
PI015 local finite-Gamma multiplier decomposition.

This is an ACTUAL source-typed PI008 + PI014 proof candidate on Weil-Lab's
Lean v4.34.0 / Mathlib v4.34.0 stack. No external Zeta23 package is
imported here (upstream uses Lean v4.33.0-rc2/Mathlib v4.33.0-rc2).

The separate compat/pi015/PI015ExternalPaperFT.lean imports the genuine
external Zeta23.Defs under the original upstream compiler.

NO LEAN PASS: this file needs actual direct compiler, .olean and
#print axioms receipts, and it does not prove inverse Fourier pairing.
-/

/-- Finite harmonic constant attached to the literal PI008 Gamma symbol. -/
def pi015FiniteHarmonic (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.range N, (1 / ((n : ℝ) + 1))

/-- The empty harmonic constant really vanishes. -/
theorem pi015FiniteHarmonic_zero :
    pi015FiniteHarmonic 0 = 0 := by
  simp [pi015FiniteHarmonic]

/-- Exact successive harmonic-contact coefficient. -/
theorem pi015FiniteHarmonic_succ (N : ℕ) :
    pi015FiniteHarmonic (N + 1) =
      pi015FiniteHarmonic N + 1 / ((N : ℝ) + 1) := by
  simp [pi015FiniteHarmonic, Finset.sum_range_succ]

/-- Pure finite algebra in the **literal** PI008 real Gamma multiplier:
no inverse transform, limit, or missing contact constant is assumed. -/
theorem pi015FiniteSymbol_split (N : ℕ) (r : ℝ) :
    pi008FiniteDigammaSymbol N r =
      pi015FiniteHarmonic N - Real.eulerMascheroniConstant -
        Real.log Real.pi -
          ∑ n ∈ Finset.range N, pi008GammaRationalAtom n r := by
  simp only [pi008FiniteDigammaSymbol, pi015FiniteHarmonic,
    Finset.sum_sub_distrib]
  ring

/-- The same finite decomposition in ℂ, now using the **actual PI014
local paper-FT model**, not a fictitious imported Zeta23 theorem. -/
theorem pi015FiniteSymbol_eq_localFourier (N : ℕ) (r : ℝ) :
    (pi008FiniteDigammaSymbol N r : ℂ) =
      (pi015FiniteHarmonic N : ℂ) -
        (Real.eulerMascheroniConstant : ℂ) -
        (Real.log Real.pi : ℂ) -
        pi014PaperFTModel N r := by
  rw [pi015FiniteSymbol_split, pi014PaperFTModel_finite]
  simp only [Complex.ofReal_sub, Complex.ofReal_sum]

/-- Multiplying by any complex scalar still RETAINS the finite harmonic
and Gamma contact coefficient; this is algebra, NOT the integral pairing
with h(0), which remains an independent inverse Fourier obligation. -/
theorem pi015FiniteSymbol_scalar (N : ℕ) (r : ℝ) (c : ℂ) :
    (pi008FiniteDigammaSymbol N r : ℂ) * c =
      ((pi015FiniteHarmonic N : ℂ) -
        (Real.eulerMascheroniConstant : ℂ) -
        (Real.log Real.pi : ℂ)) * c -
      (pi014PaperFTModel N r) * c := by
  rw [pi015FiniteSymbol_eq_localFourier]
  ring

#print axioms pi015FiniteHarmonic_zero
#print axioms pi015FiniteHarmonic_succ
#print axioms pi015FiniteSymbol_split
#print axioms pi015FiniteSymbol_eq_localFourier
#print axioms pi015FiniteSymbol_scalar

end
end WeilDefect
