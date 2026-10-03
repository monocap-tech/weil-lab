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
  exact ((differentiable_id.mul (differentiable_id.sub_const 1)).mul
    differentiable_completedZeta₀).add_const 1

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
  ring

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

/-- Actual multiplicity-copy counts are bounded by the analytic divisor
mass in their enclosing disk. Extra zeros only enlarge this bound. -/
theorem neutralActualZetaDivisorHeightWindow_card_le_mass (T : ℝ) :
    (Fintype.card (neutralActualZetaDivisorHeightWindow T) : ℤ) ≤
      neutralActualZetaJensenMass (|T| + 2) := by
  classical
  let D := divisor neutralActualZetaEntire (closedBall (0 : ℂ) ||T| + 2|)
  have ha : AnalyticOnNhd ℂ neutralActualZetaEntire
      (closedBall (0 : ℂ) ||T| + 2|) := fun z _ => neutralActualZetaEntire_analytic z
  have hfinite := D.finiteSupport (isCompact_closedBall (0 : ℂ) ||T| + 2|)
  have hpoint (ρ : neutralActualZetaPointHeightWindow T) :
      ρ.val.val ∈ closedBall (0 : ℂ) (|T| + 2) := by
    have hn := Complex.norm_le_abs_re_add_abs_im ρ.val.val
    rw [abs_of_pos ρ.val.property.2.1] at hn
    have hi : |ρ.val.val.im| ≤ |T| := ρ.property.trans (le_abs_self T)
    have hb : ‖ρ.val.val‖ ≤ |T| + 2 := by linarith [ρ.val.property.2.2]
    simpa only [mem_closedBall, dist_zero_right] using hb
  have hD (ρ : neutralActualZetaPointHeightWindow T) :
      D ρ.val.val = (neutralActualZetaMultiplicity ρ.val : ℤ) := by
    exact neutralActualZetaEntire_divisor (r := |T| + 2) ρ.val
      (by simpa only [abs_of_pos (by positivity : 0 < |T| + 2)] using hpoint ρ)
  rw [neutralActualZetaDivisorHeightWindow_card, Nat.cast_sum]
  change (∑ ρ : neutralActualZetaPointHeightWindow T,
    (neutralActualZetaMultiplicity ρ.val : ℤ)) ≤ ∑ᶠ z, D z
  rw [finsum_eq_sum_of_support_subset D (by
    intro z hz; exact hfinite.mem_toFinset.mpr hz)]
  apply Finset.sum_le_sum_of_injOn (fun ρ : neutralActualZetaPointHeightWindow T => ρ.val.val)
  · intro ρ _ σ _ h
    exact Subtype.ext (Subtype.ext h)
  · intro z hz
    obtain ⟨ρ, _, rfl⟩ := Finset.mem_image.mp hz
    apply hfinite.mem_toFinset.mpr
    rw [Function.mem_support, hD]
    exact_mod_cast (neutralActualZetaMultiplicity_pos ρ.val).ne'
  · intro ρ _
    exact (hD ρ).ge
  · intro z _ _
    exact ha.divisor_nonneg z

/-- A quantitative actual full multiplicity count bound, using growth of
actual pole-cleared zeta rather than an independent shell-count premise. -/
theorem neutralActualZetaDivisorHeightWindow_card_le_jensen (T : ℝ) {M : ℝ}
    (hM : 1 ≤ M)
    (hbound : ∀ z ∈ sphere (0 : ℂ) (2 * (|T| + 2)),
      ‖neutralActualZetaEntire z‖ ≤ M) :
    (Fintype.card (neutralActualZetaDivisorHeightWindow T) : ℝ) ≤
      Real.log M / Real.log 2 := by
  have hc : (Fintype.card (neutralActualZetaDivisorHeightWindow T) : ℝ) ≤
      (neutralActualZetaJensenMass (|T| + 2) : ℝ) := by
    exact_mod_cast neutralActualZetaDivisorHeightWindow_card_le_mass T
  apply hc.trans
  have hr : 0 < |T| + 2 := by positivity
  have hR : 0 < 2 * (|T| + 2) := by positivity
  have hj := neutralActualZetaJensenMass_le
    (r := |T| + 2) (R := 2 * (|T| + 2)) (M := M)
    (by simpa only [abs_of_pos hr] using hr)
    (by simpa only [abs_of_pos hr, abs_of_pos hR] using
      (show |T| + 2 < 2 * (|T| + 2) by linarith))
    hM (by simpa only [abs_of_pos (by positivity : 0 < 2 * (|T| + 2))] using hbound)
  convert hj using 1
  congr 2
  field_simp

/-- Actual enclosing-circle growth envelope, bounded by compactness and
normalized to at least one. No packet count data enters this definition. -/
def neutralActualZetaCircleEnvelope (T : ℝ) : ℝ :=
  max 1 (sSup ((fun z => ‖neutralActualZetaEntire z‖) ''
    sphere (0 : ℂ) (2 * (|T| + 2))))

theorem neutralActualZetaCircleEnvelope_one_le (T : ℝ) :
    1 ≤ neutralActualZetaCircleEnvelope T := le_max_left _ _

theorem neutralActualZetaCircleEnvelope_bound (T : ℝ) :
    ∀ z ∈ sphere (0 : ℂ) (2 * (|T| + 2)),
      ‖neutralActualZetaEntire z‖ ≤ neutralActualZetaCircleEnvelope T := by
  intro z hz
  have hb : BddAbove ((fun z => ‖neutralActualZetaEntire z‖) ''
      sphere (0 : ℂ) (2 * (|T| + 2))) :=
    ((isCompact_sphere (0 : ℂ) (2 * (|T| + 2))).image
      (continuous_norm.comp neutralActualZetaEntire_differentiable.continuous)).bddAbove
  exact (le_csSup hb ⟨z, hz, rfl⟩).trans (le_max_right _ _)

/-- Unconditional actual divisor count bound in terms of actual completed
zeta growth. A rate for this envelope remains a separate analytic theorem. -/
theorem neutralActualZetaDivisorHeightWindow_card_le_envelope (T : ℝ) :
    (Fintype.card (neutralActualZetaDivisorHeightWindow T) : ℝ) ≤
      Real.log (neutralActualZetaCircleEnvelope T) / Real.log 2 :=
  neutralActualZetaDivisorHeightWindow_card_le_jensen T
    (neutralActualZetaCircleEnvelope_one_le T) (neutralActualZetaCircleEnvelope_bound T)

end

end WeilDefect
