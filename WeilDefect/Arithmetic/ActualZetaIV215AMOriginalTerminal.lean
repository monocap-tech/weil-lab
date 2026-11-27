import WeilDefect.Arithmetic.IV160Bank.SymBank
import WeilDefect.Arithmetic.IV160Bank.RowBank
import WeilDefect.Arithmetic.ActualZetaIV160AMTerminalReceiver

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap BigOperators

/-- Consume the complete literal integer and symmetry banks, without
certificate hypotheses. Requires their compiled proof objects. -/
theorem neutralIV215OriginalTerminal (f : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0) :
    ‖∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation 2 f f) n‖ ≤
      (7979648/1000000:ℝ)*∫ x : ℝ, ‖f x‖^2 :=
  neutralIV160Original_bound neutralIV160SymBank neutralIV160RowBank f hs

#print axioms neutralIV215OriginalTerminal
end
end WeilDefect
