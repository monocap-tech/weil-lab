import WeilDefect.Arithmetic.ActualZetaIV073PaperFTRationalGate
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_EF_paper_inversion
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped FourierTransform

/-!
IV074 — original-source exponential Fourier inversion instance.
Depends on the strictly verified IV073 paperFT rational theorem.

This module does not assert a Fubini exchange, an NF599 Gamma pairing,
or any claim about the complete signed original Weil form.
Frozen original Phase IV source: 165981950e193a8b6ea219f7b31e379db495befa.
-/

def neutralIV074Kernel (alpha : ℝ) (u : ℝ) : ℂ :=
  Complex.exp (((-alpha * |u| : ℝ) : ℂ))

def neutralIV074Rational (alpha r : ℝ) : ℝ :=
  2 * alpha / (alpha ^ 2 + r ^ 2)

/-- Pointwise continuity of the physical exponential. -/
theorem neutralIV074Kernel_continuous (alpha : ℝ) :
    Continuous (neutralIV074Kernel alpha) := by
  unfold neutralIV074Kernel
  fun_prop

/-- Genuine L¹ on the whole physical line, recovered from IV072's
two integrable half-lines rather than assumed. -/
theorem neutralIV074Kernel_integrable
    (alpha : ℝ) (ha : 0 < alpha) :
    Integrable (neutralIV074Kernel alpha) := by
  have hfull : Integrable (neutralIV072FullLineIntegrand alpha 0) := by
    have hparts : IntegrableOn (neutralIV072FullLineIntegrand alpha 0)
        (Set.Iic 0 ∪ Set.Ioi 0) :=
      integrableOn_union.mpr ⟨
        neutralIV072FullLine_integrable_left alpha 0 ha,
        neutralIV072FullLine_integrable_right alpha 0 ha⟩
    simpa only [Set.Iic_union_Ioi, integrableOn_univ] using hparts
  have heq : neutralIV072FullLineIntegrand alpha 0 = neutralIV074Kernel alpha := by
    funext u
    rw [neutralIV072FullLine_eq_damped_fourier]
    simp [neutralIV074Kernel]
  simpa only [heq] using hfull

/-- Actual real Lorentzian resolvent is L¹. Uses the pinned Mathlib
integrable_inv_one_add_mul_sq with genuine positive scaling. -/
theorem neutralIV074Rational_integrable
    (alpha : ℝ) (ha : 0 < alpha) :
    Integrable (neutralIV074Rational alpha) := by
  have ha0 : alpha ≠ 0 := ne_of_gt ha
  have hscale : (1 / alpha : ℝ) ≠ 0 := by positivity
  have hbase : Integrable (fun r : ℝ => (1 + ((1 / alpha) * r) ^ 2)⁻¹) :=
    integrable_inv_one_add_mul_sq hscale
  have hs := hbase.const_mul (2 / alpha)
  have heq : neutralIV074Rational alpha =
      (fun r : ℝ => (2 / alpha) * (1 + ((1 / alpha) * r) ^ 2)⁻¹) := by
    funext r
    have hd : alpha ^ 2 + r ^ 2 ≠ 0 := ne_of_gt (by positivity)
    have hd' : 1 + ((1 / alpha) * r) ^ 2 ≠ 0 := ne_of_gt (by positivity)
    dsimp [neutralIV074Rational]
    field_simp [ha0, hd, hd']
    <;> ring
  simpa only [heq] using hs

/-- Mathlib's negative-2π Fourier transform of the same physical
kernel is the source-certified rational function at frequency -2πξ. -/
theorem neutralIV074Kernel_fourier_eq_rational
    (alpha xi : ℝ) (ha : 0 < alpha) :
    (𝓕 (neutralIV074Kernel alpha)) xi =
      ((neutralIV074Rational alpha (-2 * Real.pi * xi) : ℝ) : ℂ) := by
  have hdict :=
    Zeta23.EF.paperFT_ofReal_eq_fourier_Zeta23_EF_paper_inversion
      (neutralIV074Kernel alpha) (-2 * Real.pi * xi)
  have hfreq : -(-2 * Real.pi * xi) / (2 * Real.pi) = xi := by
    field_simp
    <;> ring
  have hsource :
      Zeta23.paperFT (neutralIV074Kernel alpha) (((-2 * Real.pi * xi : ℝ) : ℂ)) =
        ((neutralIV074Rational alpha (-2 * Real.pi * xi) : ℝ) : ℂ) := by
    simpa only [neutralIV074Kernel, neutralIV074Rational] using
      neutralIV073PaperFT_exp_eq_rational alpha (-2 * Real.pi * xi) ha
  rw [hsource, hfreq] at hdict
  exact hdict.symm

/-- The source kernel has an L¹ Mathlib Fourier transform, established
from the exact rational formula and a nonzero frequency dilation. -/
theorem neutralIV074Kernel_fourier_integrable
    (alpha : ℝ) (ha : 0 < alpha) :
    Integrable (𝓕 (neutralIV074Kernel alpha)) := by
  have hreal : Integrable (neutralIV074Rational alpha) :=
    neutralIV074Rational_integrable alpha ha
  have hc : Integrable (fun r : ℝ => (neutralIV074Rational alpha r : ℂ)) :=
    Complex.ofRealCLM.integrable_comp hreal
  have hscale : ((-2 * Real.pi : ℝ)) ≠ 0 := by positivity
  have hs : Integrable
      (fun xi : ℝ => (neutralIV074Rational alpha ((-2 * Real.pi) * xi) : ℂ)) :=
    hc.comp_mul_left' hscale
  have heq : (𝓕 (neutralIV074Kernel alpha)) =
      (fun xi : ℝ => (neutralIV074Rational alpha (-2 * Real.pi * xi) : ℂ)) := by
    funext xi
    exact neutralIV074Kernel_fourier_eq_rational alpha xi ha
  simpa only [heq] using hs

/-- Reuse the literal existing paper 1/(2π) inversion theorem.
No reconstructed Fourier inversion or substituted symbol. -/
theorem neutralIV074Kernel_paper_inversion
    (alpha : ℝ) (ha : 0 < alpha) (u : ℝ) :
    neutralIV074Kernel alpha u =
      (1 / (2 * Real.pi) : ℂ) *
        ∫ r : ℝ,
          Zeta23.paperFT (neutralIV074Kernel alpha) (r : ℂ) *
            Complex.exp (-Complex.I * (r : ℂ) * (u : ℂ)) := by
  exact Zeta23.EF.paper_inversion
    (neutralIV074Kernel_continuous alpha)
    (neutralIV074Kernel_integrable alpha ha)
    (neutralIV074Kernel_fourier_integrable alpha ha) u

/-- Direct original paper-convention inversion of the Lorentzian,
with a negative spatial exponential in the inverse transform. -/
theorem neutralIV074Kernel_inversion_rational
    (alpha : ℝ) (ha : 0 < alpha) (u : ℝ) :
    neutralIV074Kernel alpha u =
      (1 / (2 * Real.pi) : ℂ) *
        ∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
          Complex.exp (-Complex.I * (r : ℂ) * (u : ℂ)) := by
  rw [neutralIV074Kernel_paper_inversion alpha ha u]
  congr 1
  apply integral_congr_ae
  filter_upwards [] with r
  congr 1
  simpa only [neutralIV074Kernel, neutralIV074Rational] using
    neutralIV073PaperFT_exp_eq_rational alpha r ha

#print axioms neutralIV074Kernel_continuous
#print axioms neutralIV074Kernel_integrable
#print axioms neutralIV074Rational_integrable
#print axioms neutralIV074Kernel_fourier_eq_rational
#print axioms neutralIV074Kernel_fourier_integrable
#print axioms neutralIV074Kernel_paper_inversion
#print axioms neutralIV074Kernel_inversion_rational

end
end WeilDefect
