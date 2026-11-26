import WeilDefect.Arithmetic.ActualZetaIV157AMOriginalDictionary
import WeilDefect.Arithmetic.ActualZetaIV157AMReflection
import WeilDefect.Arithmetic.ActualZetaIV159AMRowReceiver

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap BigOperators

/-- This receiver requires actual block proof terms, not external
receipts, and makes no claim that the blocks have all been produced. -/
theorem neutralIV160Full_rows
    (hs : ∀ b : ℕ, b < 128 → neutralIV157SymBlock b = true)
    (hr : ∀ b : ℕ, b < 1024 → neutralIV159RowBlock b = true)
    (i : ℕ) (hi : i < 16384) :
    0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ) :=
  neutralIV157Half_bank (neutralIV158Symmetry hs) (neutralIV159HalfRows hr) i hi

theorem neutralIV160Original_bound
    (hsym : ∀ b : ℕ, b < 128 → neutralIV157SymBlock b = true)
    (hrows : ∀ b : ℕ, b < 1024 → neutralIV159RowBlock b = true)
    (f : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0) :
    ‖∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation 2 f f) n‖ ≤
      (7979648/1000000:ℝ)*∫ x : ℝ, ‖f x‖^2 :=
  neutralIV157Original_prime_bound f hs (neutralIV160Full_rows hsym hrows)

#print axioms neutralIV160Full_rows
#print axioms neutralIV160Original_bound
end
end WeilDefect
