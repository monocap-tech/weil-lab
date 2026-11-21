module

public import Zeta.Zeros.HardyZ

/-!
CP014: independent local-rank exclusion route. A genuinely proved
StrictMonoOn Zeta.hardyZ on the short 149.5..150.05353 interval
would prohibit multiple critical-line zeros there; original published
bounded-height RH then excludes any off-line zeros. These are explicitly
SEPARATE missing hypotheses; numerical samples of HardyZ' do NOT prove
StrictMonoOn.

This module proves only the conditional original-HardyZ uniqueness
statement in authentic upstream notation. Kernel status pending.
-/

@[expose] public section

namespace CP014HardyRank
open Set

/-- Two original critical-line zeta zeros STRICTLY within a closed
interval on which original HardyZ is strictly increasing must coincide.
No numerical derivative positivity or zero existence is asserted. -/
theorem unique_critical_zero_of_hardy_strictMonoOn
    (a b : ℝ) (ha : 0 ≤ a)
    (hmono : StrictMonoOn Zeta.hardyZ (Icc a b))
    {x y : ℝ} (hx : x ∈ Ioo a b) (hy : y ∈ Ioo a b)
    (hzx : riemannZeta (1 / 2 + Complex.I * (x : ℂ)) = 0)
    (hzy : riemannZeta (1 / 2 + Complex.I * (y : ℂ)) = 0) : x = y := by
  have hax : 0 ≤ x := ha.trans hx.1.le
  have hay : 0 ≤ y := ha.trans hy.1.le
  have hzx0 : Zeta.hardyZ x = 0 :=
    (hardyZ_eq_zero_iff_riemannZeta hax).mpr hzx
  have hzy0 : Zeta.hardyZ y = 0 :=
    (hardyZ_eq_zero_iff_riemannZeta hay).mpr hzy
  have hxc : x ∈ Icc a b := ⟨hx.1.le, hx.2.le⟩
  have hyc : y ∈ Icc a b := ⟨hy.1.le, hy.2.le⟩
  rcases lt_trichotomy x y with hlt | heq | hgt
  · have h := hmono hxc hyc hlt
    rw [hzx0, hzy0] at h
    exact False.elim ((lt_irrefl (0 : ℝ)) h)
  · exact heq
  · have h := hmono hyc hxc hgt
    rw [hzx0, hzy0] at h
    exact False.elim ((lt_irrefl (0 : ℝ)) h)

end CP014HardyRank

#print axioms CP014HardyRank.unique_critical_zero_of_hardy_strictMonoOn
