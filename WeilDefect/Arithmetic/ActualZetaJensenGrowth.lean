import WeilDefect.Arithmetic.ActualZetaDivisorWindows
import Mathlib.Analysis.Complex.JensenFormula

namespace WeilDefect

noncomputable section

open Filter MeromorphicOn Metric
open scoped Topology BigOperators ENat

/-- Pole-cleared completed zeta, with its entire values at both endpoints.
The normalization is twice the usual xi function. -/
def neutralActualZetaEntire (z : ℂ) : ℂ :=
  z * (z - 1) * completedRiemannZeta₀ z + 1

theorem neutralActualZetaEntire_differentiable :
    Differentiable ℂ neutralActualZetaEntire := by
  unfold neutralActualZetaEntire
  fun_prop (disch := exact differentiable_completedZeta₀)

theorem neutralActualZetaEntire_analytic (z : ℂ) :
    AnalyticAt ℂ neutralActualZetaEntire z :=
  neutralActualZetaEntire_differentiable.analyticAt z

theorem neutralActualZetaEntire_zero : neutralActualZetaEntire 0 = 1 := by
  simp [neutralActualZetaEntire]

theorem neutralActualZetaEntire_eq_completed {z : ℂ} (h0 : z ≠ 0) (h1 : z ≠ 1) :
    neutralActualZetaEntire z = z * (z - 1) * completedRiemannZeta z := by
  rw [completedRiemannZeta_eq]
  unfold neutralActualZetaEntire
  field_simp
  <;> ring

/-- Pole clearing preserves every actual open-strip analytic multiplicity. -/
theorem neutralActualZetaEntire_order (ρ : NeutralActualZetaZeroPoint) :
    analyticOrderAt neutralActualZetaEntire ρ.val =
      analyticOrderAt riemannZeta ρ.val := by
  have heq : neutralActualZetaEntire =ᶠ[𝓝 ρ.val]
      (fun z : ℂ => z * (z - 1)) * completedRiemannZeta := by
    have h0 : {0}ᶜ ∈ 𝓝 ρ.val := isOpen_compl_singleton.mem_nhds
      (by simpa using neutralActualZetaZeroPoint_ne_zero ρ)
    have h1 : {1}ᶜ ∈ 𝓝 ρ.val := isOpen_compl_singleton.mem_nhds
      (by simpa using neutralActualZetaZeroPoint_ne_one ρ)
    filter_upwards [h0, h1] with z hz0 hz1
    exact neutralActualZetaEntire_eq_completed (by simpa using hz0) (by simpa using hz1)
  rw [analyticOrderAt_congr heq,
    analyticOrderAt_mul (by fun_prop) (neutralActualZetaCompleted_analytic ρ)]
  have hp : analyticOrderAt (fun z : ℂ => z * (z - 1)) ρ.val = 0 :=
    analyticOrderAt_eq_zero.mpr (.inr (mul_ne_zero
      (neutralActualZetaZeroPoint_ne_zero ρ)
      (sub_ne_zero.mpr (neutralActualZetaZeroPoint_ne_one ρ))))
  rw [hp, zero_add, neutralActualZetaOrder_completed]

/-- The analytic divisor of the entire function retains the exact actual
integer multiplicity at every retained point. -/
theorem neutralActualZetaEntire_divisor {r : ℝ}
    (ρ : NeutralActualZetaZeroPoint) (hρ : ρ.val ∈ closedBall (0 : ℂ) |r|) :
    divisor neutralActualZetaEntire (closedBall (0 : ℂ) |r|) ρ.val =
      (neutralActualZetaMultiplicity ρ : ℤ) := by
  have ha : AnalyticOnNhd ℂ neutralActualZetaEntire (closedBall (0 : ℂ) |r|) :=
    fun z _ => neutralActualZetaEntire_analytic z
  rw [ha.divisor_apply hρ, neutralActualZetaEntire_order,
    ← neutralActualZetaMultiplicity_order]
  simp

/-- Concrete Jensen mass: the divisor is that of actual pole-cleared zeta,
not an independent packet count or shell hypothesis. -/
def neutralActualZetaJensenMass (r : ℝ) : ℤ :=
  ∑ᶠ z, divisor neutralActualZetaEntire (closedBall (0 : ℂ) |r|) z

theorem neutralActualZetaJensenMass_nonnegative (r : ℝ) :
    0 ≤ neutralActualZetaJensenMass r := by
  have ha : AnalyticOnNhd ℂ neutralActualZetaEntire (closedBall (0 : ℂ) |r|) :=
    fun z _ => neutralActualZetaEntire_analytic z
  exact finsum_nonneg (fun z => ha.divisor_nonneg z)

/-- Quantitative actual divisor mass bound from the actual entire-function
growth on an enclosing circle. No spectral operator domain is invoked. -/
theorem neutralActualZetaJensenMass_le {r R M : ℝ}
    (hr : 0 < |r|) (hrR : |r| < |R|) (hM : 1 ≤ M)
    (hbound : ∀ z ∈ sphere (0 : ℂ) |R|, ‖neutralActualZetaEntire z‖ ≤ M) :
    (neutralActualZetaJensenMass r : ℝ) ≤ Real.log M / Real.log (R / r) := by
  have ha : AnalyticOnNhd ℂ neutralActualZetaEntire (closedBall (0 : ℂ) |R|) :=
    fun z _ => neutralActualZetaEntire_analytic z
  simpa only [neutralActualZetaJensenMass, neutralActualZetaEntire_zero,
    norm_one, div_one] using
    ha.sum_divisor_le hr hrR hM (by rw [neutralActualZetaEntire_zero]; norm_num) hbound

end

end WeilDefect
