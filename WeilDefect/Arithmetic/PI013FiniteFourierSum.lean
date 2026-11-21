import WeilDefect.Arithmetic.PI013GammaAtomCast
import WeilDefect.Arithmetic.PI007FiniteGammaKernel
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Integral.IntegrableOn
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set
open scoped BigOperators

/-!
PI013: finite source-positive Fourier transform of the exponential atoms.

This is a FINITE Bochner integral theorem candidate using actual Mathlib's
integral_finsetSum. Its integrands are the exact PI011PhysicalFourierAtom and
the frequency coefficients are the literal PI008GammaRationalAtom.

The additional pointwise identification with the original PI007 kernel
times the literal Zeta23 paper Fourier character is not asserted here;
it remains a separate source-bound Lean obligation.

No actual .olean/axiom receipt at commit time. No IV011 import.
-/

/-- Finite positive-sign Fourier integrand built from the genuine physical
exponential Gamma atoms. -/
def pi013FiniteDampedFourier (N : ℕ) (r u : ℝ) : ℂ :=
  ∑ n ∈ Finset.range N,
    pi011PhysicalFourierAtom (pi013GammaDamping n) r u

/-- Each physical Gamma Fourier exponential is absolutely integrable.
The half-line integrability is transferred from PI011's genuine sources. -/
theorem pi013PhysicalGammaAtom_integrable (n : ℕ) (r : ℝ) :
    Integrable (pi011PhysicalFourierAtom (pi013GammaDamping n) r) := by
  have hα := pi013GammaDamping_pos n
  have hleft :=
    pi011Piecewise_integrableOn_Iic (pi013GammaDamping n) r hα
  have hright :=
    pi011Piecewise_integrableOn_Ioi (pi013GammaDamping n) r hα
  have hwhole :
      Integrable (pi011PiecewiseFourierAtom (pi013GammaDamping n) r) := by
    rw [← integrableOn_univ, ← Set.Iic_union_Ioi (a := (0 : ℝ)),
      integrableOn_union]
    exact ⟨hleft, hright⟩
  have heq :
      pi011PhysicalFourierAtom (pi013GammaDamping n) r =
      pi011PiecewiseFourierAtom (pi013GammaDamping n) r := by
    funext u
    exact pi011Physical_eq_piecewise (pi013GammaDamping n) r u
  rw [heq]
  exact hwhole

/-- No terms means zero finite Fourier integrand. -/
theorem pi013FiniteDampedFourier_zero (r u : ℝ) :
    pi013FiniteDampedFourier 0 r u = 0 := by
  simp [pi013FiniteDampedFourier]

/-- A genuinely finite Fourier transform: the exact integral of the sum
of source-positive physical exponentials equals the sum of exact PI008
rational Gamma coefficients, with no missing 2pi factor. -/
theorem pi013FiniteFourierIntegral (N : ℕ) (r : ℝ) :
    (∫ u : ℝ, pi013FiniteDampedFourier N r u) =
      ∑ n ∈ Finset.range N, (pi008GammaRationalAtom n r : ℂ) := by
  calc
    (∫ u : ℝ, pi013FiniteDampedFourier N r u) =
        ∑ n ∈ Finset.range N,
          ∫ u : ℝ, pi011PhysicalFourierAtom (pi013GammaDamping n) r u := by
      unfold pi013FiniteDampedFourier
      exact integral_finsetSum (Finset.range N) (fun n _ =>
        pi013PhysicalGammaAtom_integrable n r)
    _ = ∑ n ∈ Finset.range N, (pi008GammaRationalAtom n r : ℂ) := by
      apply Finset.sum_congr rfl
      intro n hn
      exact pi013FourierIntegralGammaAtom n r

#print axioms pi013PhysicalGammaAtom_integrable
#print axioms pi013FiniteDampedFourier_zero
#print axioms pi013FiniteFourierIntegral

end
end WeilDefect
