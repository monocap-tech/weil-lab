import WeilDefect.MasterRecon.V10B15a
import Zeta23.GammaFacts.Series

/-! V10B77a: exact scalar series attachment from the pinned Apache-2.0
Zeta23 source. The original receiver is unchanged. -/
namespace WeilDefect.MasterRecon.V10B77a

theorem quarter_not_integer (v : ℝ) :
    (1/4 + Complex.I * (v:ℂ) : ℂ) ∈ Complex.integerComplement := by
  rw [Complex.mem_integerComplement_iff]
  rintro ⟨n,hn⟩
  have hr : (n:ℝ) = 1/4 := by
    have h := congrArg Complex.re hn
    simpa using h
  have hi : 4*n = (1:ℤ) := by
    exact_mod_cast (show (4:ℝ)*(n:ℝ)=1 by linarith)
  omega

theorem central_series : V10B15a.CentralSeries := by
  intro v hv
  exact Zeta23.DigammaSeries.hasSum_digamma_series (quarter_not_integer v)

end WeilDefect.MasterRecon.V10B77a

#print axioms WeilDefect.MasterRecon.V10B77a.quarter_not_integer
#print axioms WeilDefect.MasterRecon.V10B77a.central_series
