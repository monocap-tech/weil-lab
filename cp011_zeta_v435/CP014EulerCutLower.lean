module

public import CP013Seam
public import Zeta.Zeros.Count

/-!
CP014 original Euler first-52 source theorem gives a one-sided
source-certifiable N(149.5) >= 52 without any indexed RS zero row,
any new numeric root, the original full 1.748m source split or any
extra global zero hypothesis.

This is an original-v4.35 Lean SOURCE CANDIDATE until compiled
with actual original standard-only #print axioms and .olean receipt.
-/

@[expose] public section

open Zeta.Certificates

namespace CP014EulerCutLower

/-- Rigorous *lower* count at 149.500 from the ORIGINAL published
Euler–Maclaurin 52-root BatchSpec. The upper count is separate and
still requires the full exact source split. -/
theorem fifty_two_le_N_at_original_Euler_seam :
    (52 : ℝ) ≤ riemannZeta.N ((149500 : ℝ) / 1000) := by
  let E : CertifiedZeroIntervals := CP013Seam.first52Euler.bundle
  have hEend : E.height ≤ ((149500 : ℝ) / 1000) := by
    refine E.height_le_of_getLast?_snd
      CP013Seam.first52Euler.bundle_getLast? ?_
    norm_num [Enclosure.sfrac]
  calc
    (52 : ℝ) = (E.intervals.length : ℝ) := by
      simp [E, CP013Seam.first52Euler.bundle_length]
    _ ≤ riemannZeta.N E.height :=
      riemannZeta.le_N_of_certifiedZeroIntervals E
    _ ≤ riemannZeta.N ((149500 : ℝ) / 1000) :=
      riemannZeta.N_mono hEend

end CP014EulerCutLower

#print axioms CP014EulerCutLower.fifty_two_le_N_at_original_Euler_seam
