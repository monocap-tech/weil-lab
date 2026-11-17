import Mathlib

namespace WeilDefect

/-! NF599: sharpen the historical 1/10 support-only margin.
This is the scalar budget, not a claim that its analytic
mass, prime or pole hypotheses have already been discharged. -/

theorem neutralNF599CollarBudget
    (m low high arch prime pole : ℝ)
    (hlo : 0 ≤ low) (hmass : low+high=m) (hlow : low ≤ m/25)
    (harch : -(28/5)*low+(11/10)*high ≤ arch)
    (hprime : |prime| ≤ (2/5)*m)
    (hpole : |pole| ≤ (4/125)*m) :
    (2/5)*m ≤ arch-prime+pole := by
  have hp := (le_abs_self prime).trans hprime
  have hq := (neg_abs_le pole)
  linarith only [hmass,hlow,harch,hp,hpole,hq]

theorem neutralNF599GammaConstant_arithmetic :
    (2/3:ℚ)+11/7+21/10+6/5 < 28/5 := by decide +kernel

theorem neutralNF599ArchConstant_arithmetic :
    (11/10:ℚ)*(24/25)-(28/5)*(1/25)=104/125 := by decide +kernel

theorem neutralNF599MarginConstant_arithmetic :
    (104/125:ℚ)-2/5-4/125=2/5 := by decide +kernel

end WeilDefect
