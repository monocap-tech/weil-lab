import WeilDefect.Arithmetic.PI010FourierHalflineAtom
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set

/-!
PI011 genuine full-real-line Fourier-atom proof CANDIDATES.

Actual prior PI010 half-line integral results and the pinned Mathlib theorem
integral_Iic_add_Ioi provide a direct path from genuine improper complex
integrals to the source-positive angular Fourier transform.

The final rational simplification to 2*alpha/(alpha^2+r^2), PI008 atom
identification, finite Gamma inversion, and IV011 original-source transport
are distinct, unresolved Lean obligations.

NO LEAN PASS CLAIM: this file must produce a genuine .olean, complete
#print axioms output, and direct CI receipt before any theorem is certified.
-/

/-- A piecewise presentation of the two source-positive Fourier halves.
The negative half-line includes zero; the positive half-line excludes it. -/
def pi011PiecewiseFourierAtom (α r : ℝ) (u : ℝ) : ℂ :=
  if u ≤ 0 then
    Complex.exp (pi010NegativeExponent α r * (u : ℂ))
  else
    Complex.exp (pi010PositiveExponent α r * (u : ℂ))

/-- The original source-positive Fourier integrand with the physical
absolute-value damping factor. -/
def pi011PhysicalFourierAtom (α r : ℝ) (u : ℝ) : ℂ :=
  Complex.exp (-(α : ℂ) * (|u| : ℂ) +
    Complex.I * (r : ℂ) * (u : ℂ))

/-- The piecewise integrand is integrable on the negative half-line. -/
theorem pi011Piecewise_integrableOn_Iic (α r : ℝ) (hα : 0 < α) :
    IntegrableOn (pi011PiecewiseFourierAtom α r) (Iic (0 : ℝ)) := by
  have hpos : 0 < (pi010NegativeExponent α r).re := by
    rw [pi010NegativeExponent_re]
    exact hα
  refine IntegrableOn.congr_fun
    (integrableOn_exp_mul_complex_Iic
      (a := pi010NegativeExponent α r) hpos (0 : ℝ)) ?_ measurableSet_Iic
  intro u hu
  simp [pi011PiecewiseFourierAtom, (mem_Iic.mp hu)]

/-- The piecewise integrand is integrable on the positive half-line. -/
theorem pi011Piecewise_integrableOn_Ioi (α r : ℝ) (hα : 0 < α) :
    IntegrableOn (pi011PiecewiseFourierAtom α r) (Ioi (0 : ℝ)) := by
  have hneg : (pi010PositiveExponent α r).re < 0 := by
    rw [pi010PositiveExponent_re]
    exact neg_lt_zero.mpr hα
  refine IntegrableOn.congr_fun
    (integrableOn_exp_mul_complex_Ioi
      (a := pi010PositiveExponent α r) hneg (0 : ℝ)) ?_ measurableSet_Ioi
  intro u hu
  have hu' : ¬ u ≤ 0 := not_le.mpr (mem_Ioi.mp hu)
  simp [pi011PiecewiseFourierAtom, hu']

/-- Direct whole-line assembly of the two genuine PI010 complex integrals.
The sum is intentionally not replaced by an unproved algebraic identity. -/
theorem pi011Piecewise_whole_integral (α r : ℝ) (hα : 0 < α) :
    (∫ u : ℝ, pi011PiecewiseFourierAtom α r u) =
      -(1 : ℂ) / pi010PositiveExponent α r +
        (1 : ℂ) / pi010NegativeExponent α r := by
  have hleft := pi011Piecewise_integrableOn_Iic α r hα
  have hright := pi011Piecewise_integrableOn_Ioi α r hα
  have hleft_eq :
      (∫ u : ℝ in Iic (0 : ℝ), pi011PiecewiseFourierAtom α r u) =
      (∫ u : ℝ in Iic (0 : ℝ),
        Complex.exp (pi010NegativeExponent α r * (u : ℂ))) := by
    refine setIntegral_congr_fun measurableSet_Iic ?_
    intro u hu
    simp [pi011PiecewiseFourierAtom, (mem_Iic.mp hu)]
  have hright_eq :
      (∫ u : ℝ in Ioi (0 : ℝ), pi011PiecewiseFourierAtom α r u) =
      (∫ u : ℝ in Ioi (0 : ℝ),
        Complex.exp (pi010PositiveExponent α r * (u : ℂ))) := by
    refine setIntegral_congr_fun measurableSet_Ioi ?_
    intro u hu
    have hu' : ¬ u ≤ 0 := not_le.mpr (mem_Ioi.mp hu)
    simp [pi011PiecewiseFourierAtom, hu']
  calc
    (∫ u : ℝ, pi011PiecewiseFourierAtom α r u) =
      (∫ u : ℝ in Iic (0 : ℝ), pi011PiecewiseFourierAtom α r u) +
      (∫ u : ℝ in Ioi (0 : ℝ), pi011PiecewiseFourierAtom α r u) := by
        exact (integral_Iic_add_Ioi hleft hright).symm
    _ = (∫ u : ℝ in Iic (0 : ℝ),
            Complex.exp (pi010NegativeExponent α r * (u : ℂ))) +
        (∫ u : ℝ in Ioi (0 : ℝ),
            Complex.exp (pi010PositiveExponent α r * (u : ℂ))) := by
        rw [hleft_eq, hright_eq]
    _ = -(1 : ℂ) / pi010PositiveExponent α r +
          (1 : ℂ) / pi010NegativeExponent α r := by
        rw [pi010PositiveHalflineIntegral α r hα,
          pi010NegativeHalflineIntegral α r hα]

/-- The physical damped complex exponential is exactly the piecewise source
integrand, with NO reversal of the Fourier frequency. -/
theorem pi011Physical_eq_piecewise (α r u : ℝ) :
    pi011PhysicalFourierAtom α r u =
      pi011PiecewiseFourierAtom α r u := by
  by_cases hu : u ≤ 0
  · simp only [pi011PhysicalFourierAtom, pi011PiecewiseFourierAtom,
      if_pos hu]
    congr 1
    rw [abs_of_nonpos hu]
    simp only [pi010NegativeExponent]
    push_cast
    ring
  · have hu0 : 0 ≤ u := le_of_lt (lt_of_not_ge hu)
    simp only [pi011PhysicalFourierAtom, pi011PiecewiseFourierAtom,
      if_neg hu]
    congr 1
    rw [abs_of_nonneg hu0]
    simp only [pi010PositiveExponent]
    push_cast
    ring

/-- The actual whole-line source-positive Fourier exponential has now been
reduced to the genuine Mathlib-backed complex half-line fractions.
Further rational simplification is an independent Lean obligation. -/
theorem pi011Physical_whole_integral (α r : ℝ) (hα : 0 < α) :
    (∫ u : ℝ, pi011PhysicalFourierAtom α r u) =
      -(1 : ℂ) / pi010PositiveExponent α r +
        (1 : ℂ) / pi010NegativeExponent α r := by
  have heq : pi011PhysicalFourierAtom α r =
    pi011PiecewiseFourierAtom α r := by
      funext u
      exact pi011Physical_eq_piecewise α r u
  rw [heq]
  exact pi011Piecewise_whole_integral α r hα

#print axioms pi011Piecewise_integrableOn_Iic
#print axioms pi011Piecewise_integrableOn_Ioi
#print axioms pi011Piecewise_whole_integral
#print axioms pi011Physical_eq_piecewise
#print axioms pi011Physical_whole_integral

end
end WeilDefect
