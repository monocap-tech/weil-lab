import WeilDefect.Arithmetic.ActualZetaIV074ExponentialInversionGate
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory

/-!
IV075: the source-preserving, general-L¹ Fubini gate.
The input h is arbitrary Integrable (ℝ → ℂ); no Hermitian,
evenness, or moment condition is imposed.
The spectral weight is the actual IV074 Lorentzian Fourier transform.

This module isolates an absolutely integrable two-variable kernel before
making any mixed Weil or full Gamma assertion. The original Phase IV
source remains frozen at 165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- Original inverse-Fourier oscillation with the negative exponent. -/
def neutralIV075Osc (r u : ℝ) : ℂ :=
  Complex.exp (-Complex.I * (r : ℂ) * (u : ℂ))

/-- The actual Lorentzian source weight is even; no property of h
is used or implied. -/
theorem neutralIV075Rational_even (alpha r : ℝ) :
    neutralIV074Rational alpha (-r) = neutralIV074Rational alpha r := by
  simp only [neutralIV074Rational, neg_sq]

/-- The inverse-Fourier oscillation has unit complex norm. -/
theorem neutralIV075Osc_norm_one (r u : ℝ) :
    ‖neutralIV075Osc r u‖ = 1 := by
  have hre : (-Complex.I * (r : ℂ) * (u : ℂ)).re = 0 := by
    simp [Complex.mul_re]
  simp [neutralIV075Osc, Complex.norm_exp, hre]

/-- Complex-valued joint original-resolvent integrand is genuinely L¹
on ℝ×ℝ under exactly h∈L¹, by the product-integrability theorem.
The exponential factor contributes no norm growth. -/
theorem neutralIV075Joint_integrable
    (alpha : ℝ) (ha : 0 < alpha)
    (h : ℝ → ℂ) (hh : Integrable h) :
    Integrable (fun p : ℝ × ℝ =>
      (neutralIV074Rational alpha p.1 : ℂ) *
        h p.2 * neutralIV075Osc p.1 p.2)
      (volume.prod volume) := by
  have hR : Integrable (fun r : ℝ => (neutralIV074Rational alpha r : ℂ)) :=
    Complex.ofRealCLM.integrable_comp
      (neutralIV074Rational_integrable alpha ha)
  have hbase : Integrable (fun p : ℝ × ℝ =>
      (neutralIV074Rational alpha p.1 : ℂ) * h p.2)
      (volume.prod volume) := hR.mul_prod hh
  have hosc : Continuous (fun p : ℝ × ℝ =>
      neutralIV075Osc p.1 p.2) := by
    unfold neutralIV075Osc
    fun_prop
  refine hbase.mono'
    (hbase.aestronglyMeasurable.mul hosc.aestronglyMeasurable) ?_
  filter_upwards [] with p
  rw [norm_mul, neutralIV075Osc_norm_one, mul_one]

/-- Authentic Fubini swap for the original complex exponential pair:
the two iterated integrals agree without any mixed-correlation symmetry. -/
theorem neutralIV075Fubini_swap
    (alpha : ℝ) (ha : 0 < alpha)
    (h : ℝ → ℂ) (hh : Integrable h) :
    (∫ r : ℝ, ∫ u : ℝ,
      (neutralIV074Rational alpha r : ℂ) * h u *
        neutralIV075Osc r u) =
      ∫ u : ℝ, ∫ r : ℝ,
        (neutralIV074Rational alpha r : ℂ) * h u *
          neutralIV075Osc r u := by
  exact integral_integral_swap (neutralIV075Joint_integrable alpha ha h hh)

/-- Negative-frequency `paperFT` is exactly the physical inverse
oscillation; this is a dictionary equality, not an assumption of parity. -/
theorem neutralIV075PaperFT_neg (h : ℝ → ℂ) (r : ℝ) :
    Zeta23.paperFT h ((-r : ℝ) : ℂ) =
      ∫ u : ℝ, h u * neutralIV075Osc r u := by
  unfold Zeta23.paperFT
  apply integral_congr_ae
  filter_upwards [] with u
  congr 1
  unfold neutralIV075Osc
  congr 1
  push_cast
  ring

/-- General-L¹ finite resolvent Fubini in its source-exact negative
frequency form; no Fourier-sign substitution has yet been invoked. -/
theorem neutralIV075Fubini_raw
    (alpha : ℝ) (ha : 0 < alpha)
    (h : ℝ → ℂ) (hh : Integrable h) :
    (∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
      Zeta23.paperFT h ((-r : ℝ) : ℂ)) =
      ∫ u : ℝ, h u *
        (∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
          neutralIV075Osc r u) := by
  calc
    _ = ∫ r : ℝ, ∫ u : ℝ,
        (neutralIV074Rational alpha r : ℂ) * h u *
          neutralIV075Osc r u := by
        apply integral_congr_ae
        filter_upwards [] with r
        rw [neutralIV075PaperFT_neg, ← integral_const_mul]
        apply integral_congr_ae
        filter_upwards [] with u
        ring
    _ = ∫ u : ℝ, ∫ r : ℝ,
        (neutralIV074Rational alpha r : ℂ) * h u *
          neutralIV075Osc r u := neutralIV075Fubini_swap alpha ha h hh
    _ = _ := by
      apply integral_congr_ae
      filter_upwards [] with u
      rw [← integral_const_mul]
      apply integral_congr_ae
      filter_upwards [] with r
      ring

#print axioms neutralIV075Rational_even
#print axioms neutralIV075Osc_norm_one
#print axioms neutralIV075Joint_integrable
#print axioms neutralIV075Fubini_swap
#print axioms neutralIV075PaperFT_neg
#print axioms neutralIV075Fubini_raw

end
end WeilDefect
