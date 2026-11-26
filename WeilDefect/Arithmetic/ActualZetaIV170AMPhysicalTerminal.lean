import WeilDefect.Arithmetic.IV160Bank.SymBank
import WeilDefect.Arithmetic.IV160Bank.RowBank
import WeilDefect.Arithmetic.ActualZetaIV157AMReflection
import WeilDefect.Arithmetic.ActualZetaIV159AMRowReceiver
import WeilDefect.Arithmetic.ActualZetaIV156AMPhysicalForm

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Full literal certificate assembled from imported, checked block theorems. -/
theorem neutralIV170FullRows (i : ℕ) (hi : i < 16384) :
    0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ) :=
  neutralIV157Half_bank
    (neutralIV158Symmetry neutralIV160SymBank)
    (neutralIV159HalfRows neutralIV160RowBank) i hi

/-- Physical finite prime form on the supported Schwartz core, without
any numerical certificate premise or original-dictionary dependency. -/
theorem neutralIV170PhysicalTerminal (f : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0) :
    ‖∑ n ∈ neutralIV156P, (neutralIV151Weight n:ℂ) *
      ((∫ x : ℝ, f x * star (f (x+Real.log (n:ℝ)))) +
       (∫ x : ℝ, f x * star (f (x-Real.log (n:ℝ)))))‖ ≤
      (7979648/1000000:ℝ)*∫ x : ℝ, ‖f x‖^2 :=
  neutralIV156Physical_form f hs neutralIV170FullRows

#print axioms neutralIV170FullRows
#print axioms neutralIV170PhysicalTerminal
end
end WeilDefect
