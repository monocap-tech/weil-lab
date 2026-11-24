import WeilDefect.Arithmetic.ActualZetaIV072FourierHalflinePilot
import WeilDefect.External.Zeta23.Definitions.Def_Zeta23_Defs
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory

/-!
IV073: source-faithful attachment of the certified IV072 real-line
positive-frequency exponential integral to the *literal*
`Zeta23.paperFT` and its real rational resolvent.

The source theorem IV072 is kernel-certified on dependent draft #975,
commit 1de455d18d7bdc81b7f979715826cc6a4cc4164c.
The original full signed Weil source is unchanged, frozen at
165981950e193a8b6ea219f7b31e379db495befa.

No Fubini, Gamma series limit, physical mixed Weil identity, or
positivity theorem is asserted in this file.
-/

/-- Algebraic equality of the two signed halfline complex resolvents
and the real rational multiplier, at positive damping parameter. -/
theorem neutralIV073Resolvent_rational
    (alpha r : ℝ) (ha : 0 < alpha) :
    1 / neutralIV072LeftCoefficient alpha r +
      (-1 / neutralIV072RightCoefficient alpha r) =
    (2 * (alpha : ℂ)) / ((alpha : ℂ) ^ 2 + (r : ℂ) ^ 2) := by
  have hleft : (alpha : ℂ) + Complex.I * (r : ℂ) ≠ 0 := by
    intro hz
    have hzre := congrArg Complex.re hz
    have hzero : alpha = 0 := by
      simpa [Complex.add_re, Complex.mul_re] using hzre
    exact (ne_of_gt ha) hzero
  have hright : -(alpha : ℂ) + Complex.I * (r : ℂ) ≠ 0 := by
    intro hz
    have hzre := congrArg Complex.re hz
    have hzero : -alpha = 0 := by
      simpa [Complex.add_re, Complex.mul_re] using hzre
    exact (ne_of_gt ha) (neg_eq_zero.mp hzero)
  have hdenReal : (alpha ^ 2 + r ^ 2 : ℝ) ≠ 0 := by
    have hpos : 0 < alpha ^ 2 + r ^ 2 :=
      add_pos_of_pos_of_nonneg (sq_pos_of_pos ha) (sq_nonneg r)
    exact ne_of_gt hpos
  have hden : (alpha : ℂ) ^ 2 + (r : ℂ) ^ 2 ≠ 0 := by
    exact_mod_cast hdenReal
  change 1 / ((alpha : ℂ) + Complex.I * (r : ℂ)) +
      (-1 / (-(alpha : ℂ) + Complex.I * (r : ℂ))) =
    (2 * (alpha : ℂ)) / ((alpha : ℂ) ^ 2 + (r : ℂ) ^ 2)
  field_simp [hleft, hright, hden]
  <;> ring_nf
  <;> simp [Complex.I_sq]
  <;> ring

/-- The literal original paper-convention Fourier definition evaluates
to the certified IV072 pair of actual complex Lebesgue halfline integrals.
The sign is +i r u and there is no Fourier prefactor. -/
theorem neutralIV073PaperFT_exp_eq_halves
    (alpha r : ℝ) (ha : 0 < alpha) :
    Zeta23.paperFT
        (fun u : ℝ => Complex.exp (((-alpha * |u| : ℝ) : ℂ)))
        (r : ℂ) =
      1 / neutralIV072LeftCoefficient alpha r +
        (-1 / neutralIV072RightCoefficient alpha r) := by
  simpa only [Zeta23.paperFT, Complex.exp_add] using
    neutralIV072DampedFourier_integral_eq_halves alpha r ha

/-- Original positive-frequency `paperFT` of the damped physical
exponential, as the real Lorentzian multiplier 2alpha/(alpha²+r²).
This is a source-definition attachment, not a substitute transform. -/
theorem neutralIV073PaperFT_exp_eq_rational
    (alpha r : ℝ) (ha : 0 < alpha) :
    Zeta23.paperFT
        (fun u : ℝ => Complex.exp (((-alpha * |u| : ℝ) : ℂ)))
        (r : ℂ) =
      ((2 * alpha / (alpha ^ 2 + r ^ 2) : ℝ) : ℂ) := by
  calc
    _ = 1 / neutralIV072LeftCoefficient alpha r +
          (-1 / neutralIV072RightCoefficient alpha r) :=
      neutralIV073PaperFT_exp_eq_halves alpha r ha
    _ = (2 * (alpha : ℂ)) / ((alpha : ℂ) ^ 2 + (r : ℂ) ^ 2) :=
      neutralIV073Resolvent_rational alpha r ha
    _ = ((2 * alpha / (alpha ^ 2 + r ^ 2) : ℝ) : ℂ) := by
      push_cast
      ring

#print axioms neutralIV073Resolvent_rational
#print axioms neutralIV073PaperFT_exp_eq_halves
#print axioms neutralIV073PaperFT_exp_eq_rational

end
end WeilDefect
