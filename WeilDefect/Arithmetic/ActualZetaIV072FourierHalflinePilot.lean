import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set

/-!
IV072: original positive-exponent Fourier resolvent, strictly finite prelude.

These lemmas evaluate the TWO separate exponential halfline integrals.
They use real complex Lebesgue integrals from the pinned Mathlib package.
No assertion about the true original mixed Zeta23 Gamma integral is made
here. The full-line Fourier pair, physical Schwartz inversion, and
spectral/physical limits remain subsequent obligations.

Frozen original Weil source: 165981950e193a8b6ea219f7b31e379db495befa
-/

/-- Exact Mathlib-supported integrability of the right halfline
exponential with negative real exponent. -/
theorem neutralIV072Exp_right_integrable (z : ℂ) (hz : z.re < 0) :
    IntegrableOn (fun x : ℝ => Complex.exp (z * (x : ℂ))) (Ioi 0) :=
  integrableOn_exp_mul_complex_Ioi hz 0

/-- Exact Mathlib-supported integrability of the left halfline
exponential with positive real exponent. -/
theorem neutralIV072Exp_left_integrable (z : ℂ) (hz : 0 < z.re) :
    IntegrableOn (fun x : ℝ => Complex.exp (z * (x : ℂ))) (Iic 0) :=
  integrableOn_exp_mul_complex_Iic hz 0

/-- Right halfline resolvent is the source-normalized improper integral. -/
theorem neutralIV072Exp_right_integral (z : ℂ) (hz : z.re < 0) :
    (∫ x : ℝ in Ioi 0, Complex.exp (z * (x : ℂ))) = -1 / z := by
  simpa using (integral_exp_mul_complex_Ioi (a := z) hz 0)

/-- Left halfline resolvent uses the complementary sign. -/
theorem neutralIV072Exp_left_integral (z : ℂ) (hz : 0 < z.re) :
    (∫ x : ℝ in Iic 0, Complex.exp (z * (x : ℂ))) = 1 / z := by
  simpa using (integral_exp_mul_complex_Iic (a := z) hz 0)

/-- The original *positive-exponent* Fourier convention, with
physical decay exp(-alpha |u|), has these two coefficients. -/
def neutralIV072RightCoefficient (alpha r : ℝ) : ℂ :=
  -(alpha : ℂ) + Complex.I * (r : ℂ)

def neutralIV072LeftCoefficient (alpha r : ℝ) : ℂ :=
  (alpha : ℂ) + Complex.I * (r : ℂ)

/-- Positive physical decay forces the correct right halfline sign. -/
theorem neutralIV072RightCoefficient_re_neg
    (alpha r : ℝ) (ha : 0 < alpha) :
    (neutralIV072RightCoefficient alpha r).re < 0 := by
  simpa [neutralIV072RightCoefficient, Complex.mul_re] using ha

/-- Positive physical decay forces the correct left halfline sign. -/
theorem neutralIV072LeftCoefficient_re_pos
    (alpha r : ℝ) (ha : 0 < alpha) :
    0 < (neutralIV072LeftCoefficient alpha r).re := by
  simpa [neutralIV072LeftCoefficient, Complex.mul_re] using ha

/-- Right original Fourier exponential evaluated from genuine Mathlib
Bochner integral, no unproved original Weil/Fourier source identity. -/
theorem neutralIV072RightFourierResolvent
    (alpha r : ℝ) (ha : 0 < alpha) :
    (∫ x : ℝ in Ioi 0,
      Complex.exp (neutralIV072RightCoefficient alpha r * (x : ℂ))) =
      -1 / neutralIV072RightCoefficient alpha r :=
  neutralIV072Exp_right_integral _
    (neutralIV072RightCoefficient_re_neg alpha r ha)

/-- Left original Fourier exponential in the same positive-exponent
convention, with positive physical decay on the negative halfline. -/
theorem neutralIV072LeftFourierResolvent
    (alpha r : ℝ) (ha : 0 < alpha) :
    (∫ x : ℝ in Iic 0,
      Complex.exp (neutralIV072LeftCoefficient alpha r * (x : ℂ))) =
      1 / neutralIV072LeftCoefficient alpha r :=
  neutralIV072Exp_left_integral _
    (neutralIV072LeftCoefficient_re_pos alpha r ha)

/-- A single full-line source built from the two pinned Mathlib
complex exponential halfline integrands. The original Fourier sign
is +i r x. At x=0 the left branch is used, but this is immaterial
to the real Lebesgue integral. -/
def neutralIV072FullLineIntegrand (alpha r : ℝ) (x : ℝ) : ℂ :=
  if 0 < x then
    Complex.exp (neutralIV072RightCoefficient alpha r * (x : ℂ))
  else
    Complex.exp (neutralIV072LeftCoefficient alpha r * (x : ℂ))

/-- Physical full-line resolvent is integrable on the LEFT region:
this is an actual source function, not an abstract matrix entry. -/
theorem neutralIV072FullLine_integrable_left
    (alpha r : ℝ) (ha : 0 < alpha) :
    IntegrableOn (neutralIV072FullLineIntegrand alpha r) (Iic 0) := by
  apply (neutralIV072Exp_left_integrable _
    (neutralIV072LeftCoefficient_re_pos alpha r ha)).congr_fun
      (s := Iic (0 : ℝ)) ?_ measurableSet_Iic
  intro x hx
  have hnot : ¬ (0 : ℝ) < x := not_lt.mpr hx
  simp [neutralIV072FullLineIntegrand, hnot]

/-- Physical full-line resolvent is integrable on the RIGHT region. -/
theorem neutralIV072FullLine_integrable_right
    (alpha r : ℝ) (ha : 0 < alpha) :
    IntegrableOn (neutralIV072FullLineIntegrand alpha r) (Ioi 0) := by
  apply (neutralIV072Exp_right_integrable _
    (neutralIV072RightCoefficient_re_neg alpha r ha)).congr_fun
      (s := Ioi (0 : ℝ)) ?_ measurableSet_Ioi
  intro x hx
  simp [neutralIV072FullLineIntegrand, hx]

/-- The authentic whole-real-line complex Bochner integral equals
the sum of the two pinned halfline rational resolvents.
It uses the pinned real Lebesgue decomposition
`integral_Iic_add_Ioi`, and does NOT assert a zeta source theorem. -/
theorem neutralIV072FullLine_integral_eq_halves
    (alpha r : ℝ) (ha : 0 < alpha) :
    (∫ x : ℝ, neutralIV072FullLineIntegrand alpha r x) =
      1 / neutralIV072LeftCoefficient alpha r +
        (-1 / neutralIV072RightCoefficient alpha r) := by
  have hL := neutralIV072FullLine_integrable_left alpha r ha
  have hR := neutralIV072FullLine_integrable_right alpha r ha
  have hsplit := integral_Iic_add_Ioi hL hR
  have hleft :
      (∫ x : ℝ in Iic (0 : ℝ),
        neutralIV072FullLineIntegrand alpha r x) =
      (∫ x : ℝ in Iic (0 : ℝ),
        Complex.exp (neutralIV072LeftCoefficient alpha r * (x : ℂ))) := by
    apply setIntegral_congr_fun measurableSet_Iic
    intro x hx
    have hnot : ¬ (0 : ℝ) < x := not_lt.mpr hx
    simp [neutralIV072FullLineIntegrand, hnot]
  have hright :
      (∫ x : ℝ in Ioi (0 : ℝ),
        neutralIV072FullLineIntegrand alpha r x) =
      (∫ x : ℝ in Ioi (0 : ℝ),
        Complex.exp (neutralIV072RightCoefficient alpha r * (x : ℂ))) := by
    apply setIntegral_congr_fun measurableSet_Ioi
    intro x hx
    simp [neutralIV072FullLineIntegrand, hx]
  calc
    (∫ x : ℝ, neutralIV072FullLineIntegrand alpha r x) =
      (∫ x : ℝ in Iic (0 : ℝ), neutralIV072FullLineIntegrand alpha r x) +
      (∫ x : ℝ in Ioi (0 : ℝ), neutralIV072FullLineIntegrand alpha r x) :=
        hsplit.symm
    _ = (∫ x : ℝ in Iic (0 : ℝ),
            Complex.exp (neutralIV072LeftCoefficient alpha r * (x : ℂ))) +
        (∫ x : ℝ in Ioi (0 : ℝ),
            Complex.exp (neutralIV072RightCoefficient alpha r * (x : ℂ))) := by
          rw [hleft, hright]
    _ = _ := by
          rw [neutralIV072LeftFourierResolvent alpha r ha,
            neutralIV072RightFourierResolvent alpha r ha]

/-- This is the actual positive-frequency, exponentially damped
physical Fourier kernel. It is an *integrand equality*, before any
full original Zeta23 correlation or Gamma symbol is attached. -/
theorem neutralIV072FullLine_eq_damped_fourier
    (alpha r x : ℝ) :
    neutralIV072FullLineIntegrand alpha r x =
      Complex.exp (((-alpha * |x| : ℝ) : ℂ) +
        Complex.I * (r : ℂ) * (x : ℂ)) := by
  by_cases hx : 0 < x
  · have habs : |x| = x := abs_of_pos hx
    simp only [neutralIV072FullLineIntegrand, if_pos hx, habs,
      neutralIV072RightCoefficient]
    congr 1
    push_cast
    ring
  · have hle : x ≤ 0 := le_of_not_gt hx
    have habs : |x| = -x := abs_of_nonpos hle
    simp only [neutralIV072FullLineIntegrand, if_neg hx, habs,
      neutralIV072LeftCoefficient]
    congr 1
    push_cast
    ring

/-- Direct physical whole-line positive-exponent Fourier transform,
already reduced to the TWO rigorous Mathlib resolvent integrals.
The algebraic simplification to 2α/(α²+r²), and the attachment to
`Zeta23.paperFT`, are separate named kernel obligations. -/
theorem neutralIV072DampedFourier_integral_eq_halves
    (alpha r : ℝ) (ha : 0 < alpha) :
    (∫ x : ℝ,
      Complex.exp (((-alpha * |x| : ℝ) : ℂ) +
        Complex.I * (r : ℂ) * (x : ℂ))) =
      1 / neutralIV072LeftCoefficient alpha r +
        (-1 / neutralIV072RightCoefficient alpha r) := by
  simpa only [← neutralIV072FullLine_eq_damped_fourier] using
    neutralIV072FullLine_integral_eq_halves alpha r ha

#print axioms neutralIV072Exp_right_integrable
#print axioms neutralIV072Exp_left_integrable
#print axioms neutralIV072Exp_right_integral
#print axioms neutralIV072Exp_left_integral
#print axioms neutralIV072RightCoefficient_re_neg
#print axioms neutralIV072LeftCoefficient_re_pos
#print axioms neutralIV072RightFourierResolvent
#print axioms neutralIV072LeftFourierResolvent
#print axioms neutralIV072FullLine_integrable_left
#print axioms neutralIV072FullLine_integrable_right
#print axioms neutralIV072FullLine_integral_eq_halves
#print axioms neutralIV072FullLine_eq_damped_fourier
#print axioms neutralIV072DampedFourier_integral_eq_halves

end
end WeilDefect
