import WeilDefect.Arithmetic.ActualZetaOriginalCollarGammaLower
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
IV071 — frozen original NF599 finite-Gamma source prelude.

This module deliberately asserts no infinite Laplace/Fourier interchange,
no physical mixed Gamma kernel equality, no original Weil positivity,
and no RH implication. It isolates only finite algebra attached to the
actual imported `Zeta23.EF.gammaBracket` and `neutralNF599Gain`.

The true continuum receiving goal is the separated-support resolvent
Fourier identity documented in the IV/CR Transfer VI report.
-/

/-- Literal NF599 zeroth gain plus its first N tail terms. The
constant is the true original Zeta23 Gamma symbol at zero. -/
def neutralIV071GammaFinite (N : ℕ) (r : ℝ) : ℝ :=
  Zeta23.EF.gammaBracket 0 +
    neutralNF599Gain (1/4) r +
    ∑ n ∈ Finset.range N,
      neutralNF599Gain ((n : ℝ) + 1 + 1/4) r

/-- Each finite original digamma-gain truncation lies below the
authentic original Gamma symbol; no alternative symbol is made. -/
theorem neutralIV071GammaFinite_le (N : ℕ) (r : ℝ) :
    neutralIV071GammaFinite N r ≤ Zeta23.EF.gammaBracket r :=
  neutralNF599GammaLower_partial r N

/-- Adding one genuine NF599 mode is an exact finite identity. -/
theorem neutralIV071GammaFinite_succ (N : ℕ) (r : ℝ) :
    neutralIV071GammaFinite (N+1) r =
      neutralIV071GammaFinite N r +
        neutralNF599Gain ((N : ℝ)+1+1/4) r := by
  simp only [neutralIV071GammaFinite, Finset.sum_range_succ]
  ring

/-- The finite original Gamma symbols are pointwise monotone. -/
theorem neutralIV071GammaFinite_mono (N : ℕ) (r : ℝ) :
    neutralIV071GammaFinite N r ≤
      neutralIV071GammaFinite (N+1) r := by
  rw [neutralIV071GammaFinite_succ]
  have hp : 0 ≤ neutralNF599Gain ((N : ℝ)+1+1/4) r :=
    neutralNF599Gain_nonneg _ _ (by positivity)
  linarith

/-- Pure ring/field identity used at the authentic crossed-pole /
Gamma first-mode boundary. This identity does NOT assert that
the original arch integral has already been spatially inverted. -/
theorem neutralIV071PoleGammaFirstMode_algebra
    (u v q : ℝ) (hq : 1-q ≠ 0) :
    u + v - v/(1-q) = u - (v*q)/(1-q) := by
  field_simp [hq]
  ring

/-- Source gain as a finite real rational resolvent multiplier.
A *separate* Fourier theorem is still required before reading
this as an identity of the original mixed physical Gamma form. -/
theorem neutralIV071GammaGain_rationalResolvent
    (a r : ℝ) (ha : 0 < a) :
    neutralNF599Gain a r =
      1/a - (4*a)/(4*a^2+r^2) := by
  unfold neutralNF599Gain
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hd0 : a^2 + (r/2)^2 ≠ 0 := ne_of_gt (by positivity)
  have he0 : 4*a^2+r^2 ≠ 0 := ne_of_gt (by positivity)
  field_simp [ha0,hd0,he0]
  <;> ring

/-- The exact original NF599 Gamma symbol is the pointwise limit of
the finite *source-defined* rational-resolvent truncations. This
uses the imported proven HasSum, not an alternative multiplier.
It is only pointwise: physical Fourier-integral interchange remains
a separate IV obligation. -/
theorem neutralIV071GammaFinite_tendsto (r : ℝ) :
    Filter.Tendsto (fun N : ℕ => neutralIV071GammaFinite N r)
      Filter.atTop (nhds (Zeta23.EF.gammaBracket r)) := by
  have hs := (neutralNF599GammaGainSeries r).tendsto_sum_nat
  have ht := (tendsto_const_nhds
    (x := Zeta23.EF.gammaBracket 0 +
      neutralNF599Gain (1/4) r)).add hs
  convert ht using 1
  · funext N
    rfl
  · ring

#print axioms neutralNF599GammaGainSeries
#print axioms neutralIV071GammaFinite_tendsto
#print axioms neutralIV071GammaFinite_le
#print axioms neutralIV071GammaFinite_succ
#print axioms neutralIV071GammaFinite_mono
#print axioms neutralIV071PoleGammaFirstMode_algebra
#print axioms neutralIV071GammaGain_rationalResolvent

end
end WeilDefect
