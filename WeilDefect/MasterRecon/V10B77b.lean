import WeilDefect.MasterRecon.V10B8f
import Zeta23.GammaFacts.StirlingVert

/-! V10B77b: exact vertical Stirling supplier specialized to the original
quarter-line and threshold. No change in numerical constants. -/
namespace WeilDefect.MasterRecon.V10B77b

theorem vertical_stirling : V10B8f.VerticalStirling := by
  intro v hv
  have h := Zeta23.StirlingVert.re_digamma_stirling' (a := 1/4)
    (by norm_num) (by norm_num) hv
  simpa only [Complex.ofReal_div,Complex.ofReal_one,Complex.ofReal_ofNat] using h

end WeilDefect.MasterRecon.V10B77b

#print axioms WeilDefect.MasterRecon.V10B77b.vertical_stirling
