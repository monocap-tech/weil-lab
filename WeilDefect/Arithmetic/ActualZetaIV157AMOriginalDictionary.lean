import WeilDefect.Arithmetic.ActualZetaIV156AMPhysicalForm
import WeilDefect.Arithmetic.ActualZetaIV144BKOriginalArithmetic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

theorem neutralIV157Dictionary :
    neutralIV156P = rightLimitPrimePowerFinset 2 := by
  rw [neutralIV144Prime_bank]
  exact neutralIV152Prime_bank

/-- Compare the literal finite arithmetic form to the existing original
mixed source, retaining the original sign and normalization. -/
theorem neutralIV157Mixed_identity (f : 𝓢(ℝ,ℂ)) :
    neutralIV144PrimeMixed f f =
      ∑ n ∈ neutralIV156P, (neutralIV151Weight n:ℂ) *
        ((∫ x : ℝ, f x * star (f (x+Real.log (n:ℝ)))) +
         (∫ x : ℝ, f x * star (f (x-Real.log (n:ℝ))))) := by
  have hp : neutralIV156P = neutralIV144PrimeBank := neutralIV152Prime_bank
  unfold neutralIV144PrimeMixed
  rw [hp]
  apply Finset.sum_congr rfl
  intro n hn
  unfold neutralIV151Weight
  congr 1
  exact add_comm _ _

/-- The actual original arithmetic summand, conditional only on the
literal integer certificate and the original supported Schwartz core. -/
theorem neutralIV157Original_prime_bound (f : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0)
    (hbank : ∀ i : ℕ, i < 16384 →
      0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ)) :
    ‖∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation 2 f f) n‖ ≤
      (7979648/1000000:ℝ)*∫ x : ℝ, ‖f x‖^2 := by
  rw [neutralIV144Prime_literal f f hs hs, neutralIV157Mixed_identity]
  exact neutralIV156Physical_form f hs hbank

#print axioms neutralIV157Dictionary
#print axioms neutralIV157Mixed_identity
#print axioms neutralIV157Original_prime_bound
end
end WeilDefect
