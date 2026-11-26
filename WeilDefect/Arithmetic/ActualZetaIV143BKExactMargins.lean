import WeilDefect.Arithmetic.ActualZetaIV142BKData
import Mathlib.Tactic

namespace WeilDefect

/-- Exact arithmetic on the stored BK comparator fraction only.
The comparison with the physical operator is a distinct obligation. -/
theorem neutralIV143Even_stored_margin :
    (BKData.evenBetaNum : ℚ) / (BKData.evenBetaDen : ℚ) < 1-2*(17/10000:ℚ) := by
  norm_num [BKData.evenBetaNum,BKData.evenBetaDen]

theorem neutralIV143Odd_stored_margin :
    (BKData.oddBetaNum : ℚ) / (BKData.oddBetaDen : ℚ) < 1-2*(53/10000:ℚ) := by
  norm_num [BKData.oddBetaNum,BKData.oddBetaDen]

#print axioms neutralIV143Even_stored_margin
#print axioms neutralIV143Odd_stored_margin

end WeilDefect
