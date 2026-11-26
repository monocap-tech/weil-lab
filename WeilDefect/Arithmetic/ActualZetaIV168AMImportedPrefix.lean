import WeilDefect.Arithmetic.IV160Bank.SymBank
import WeilDefect.Arithmetic.IV160Bank.RowPrefix0032
import WeilDefect.Arithmetic.ActualZetaIV157AMReflection
import WeilDefect.Arithmetic.ActualZetaIV159AMRowReceiver
import WeilDefect.Arithmetic.ActualZetaIV156AMPhysicalForm

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap BigOperators

/-- The actual zero-extended weight symmetry, with no bank hypothesis. -/
theorem neutralIV168Symmetry (k : ℤ) :
    neutralIV146Value (16383-k) = neutralIV146Value k :=
  neutralIV158Symmetry neutralIV160SymBank k

/-- The first 256 literal rows, supplied by the imported prefix. -/
theorem neutralIV168Prefix (i : ℕ) (hi : i < 256) :
    0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ) := by
  have h := neutralIV159Row_at (i/8) (i%8) (by omega)
    (neutralIV160RowPrefix0032 (i/8) (by omega))
  rw [show 8*(i/8)+i%8=i by omega] at h
  exact h

/-- Reflection also supplies the 256 opposite-end rows without
another literal row evaluation. -/
theorem neutralIV168Opposite (i : ℕ) (hl : 16128 ≤ i) (hi : i < 16384) :
    0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ) := by
  have h := neutralIV168Prefix (16383-i) (by omega)
  have he : ((16383-i:ℕ):ℤ) = 16383-(i:ℤ) := by omega
  rw [he, neutralIV168Symmetry, neutralIV157Mirror_row i hi neutralIV168Symmetry] at h
  exact h

/-- Only the uncomputed suffix of the half-bank remains as a premise. -/
theorem neutralIV168Remaining_rows
    (hr : ∀ b : ℕ, 32 ≤ b → b < 1024 → neutralIV159RowBlock b = true)
    (i : ℕ) (hi : i < 16384) :
    0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ) := by
  apply neutralIV157Half_bank neutralIV168Symmetry _ i hi
  apply neutralIV159HalfRows
  intro b hb
  by_cases h : b < 32
  · exact neutralIV160RowPrefix0032 b h
  · exact hr b (by omega) hb

theorem neutralIV168Physical_remaining
    (hr : ∀ b : ℕ, 32 ≤ b → b < 1024 → neutralIV159RowBlock b = true)
    (f : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0) :
    ‖∑ n ∈ neutralIV156P, (neutralIV151Weight n:ℂ) *
      ((∫ x : ℝ, f x * star (f (x+Real.log (n:ℝ)))) +
       (∫ x : ℝ, f x * star (f (x-Real.log (n:ℝ)))))‖ ≤
      (7979648/1000000:ℝ)*∫ x : ℝ, ‖f x‖^2 :=
  neutralIV156Physical_form f hs (neutralIV168Remaining_rows hr)

#print axioms neutralIV168Symmetry
#print axioms neutralIV168Prefix
#print axioms neutralIV168Opposite
#print axioms neutralIV168Remaining_rows
#print axioms neutralIV168Physical_remaining
end
end WeilDefect
