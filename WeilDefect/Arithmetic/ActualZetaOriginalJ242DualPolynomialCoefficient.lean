import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialSourceNodes
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF558: recover the authentic 242 real left-kernel coefficients from
the ORIGINAL dual odd-jet polynomial p_a(T) = Σ₀²⁴¹(-1)^n a_n T^n.

This is a source-specific finite-dimensional coefficient theorem.
It is not an abstract 242-dimensional Hilbert basis and it does not
assume original J242 generator independence. The real/complex
independence transfer and actual original sine/cosine/sinh derivative
bridge are still separate obligations.
-/

/-- The coefficient at EXACT original odd-jet row index i is precisely
(-1)^i * a_i, with no reshuffling, truncation or numerical source
replacement. Odd derivatives are indexed 2i+1, 1 through 483. -/
theorem neutralNF558OriginalDualPolynomial_coeff
    (a : Fin 242 → ℝ) (i : Fin 242) :
    (neutralNF557OriginalDualPolynomial a).coeff i.val =
      (-1 : ℝ) ^ i.val * a i := by
  classical
  simp [neutralNF557OriginalDualPolynomial, Polynomial.coeff_monomial]

/-- The exact 242-dimensional original odd-jet dual polynomial
is injective. This is the missing reverse implication p_a=0 → a=0,
and involves no postulated original generator independence. -/
theorem neutralNF558OriginalDualPolynomial_injective :
    Function.Injective neutralNF557OriginalDualPolynomial := by
  intro a b hab
  funext i
  have hcoeff := congrArg
    (fun p : Polynomial ℝ => p.coeff i.val) hab
  rw [neutralNF558OriginalDualPolynomial_coeff,
    neutralNF558OriginalDualPolynomial_coeff] at hcoeff
  exact mul_left_cancel₀ (pow_ne_zero _ (by norm_num : (-1 : ℝ) ≠ 0)) hcoeff

/-- If the true original 242 row dual polynomial vanishes
identically, every original real row coefficient vanishes.
This is exactly the last extraction step in the left-kernel
Hermite argument, not a substitute for the still-open source
odd-jet differentiation theorem. -/
theorem neutralNF558OriginalDualPolynomial_eq_zero
    (a : Fin 242 → ℝ)
    (hz : neutralNF557OriginalDualPolynomial a = 0) :
    a = 0 := by
  have hzero :
      neutralNF557OriginalDualPolynomial (0 : Fin 242 → ℝ) = 0 := by
    simp [neutralNF557OriginalDualPolynomial]
  exact neutralNF558OriginalDualPolynomial_injective (hz.trans hzero.symm)

end
end WeilDefect
