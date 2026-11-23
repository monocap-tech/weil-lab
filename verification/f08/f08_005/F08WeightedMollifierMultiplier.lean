import WeilDefect.Morphology.NeutralCanonicalFormDomain
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped Topology

/-!
F08-005: real source logarithmic Fourier energy and a dominated-convergence
gate for norm-one complex spectral multipliers approaching 1.

This proves convergence of weighted Fourier-coordinate energy under the
stated multiplier hypotheses. A separate theorem must still identify the
actual compact physical mollifier's Fourier multiplier and preserve support.
No claim about sharp physical cutoffs, native source identity or positivity.
-/

/-- Uniform error envelope under the genuine source weight w = log(e+|ξ|).
The factor 4 is exact for arbitrary complex contractions, including phase. -/
theorem f08_005_log_multiplier_error_pointwise
    (F : ℝ → ℂ) (m : ℝ → ℂ)
    (hm : ∀ ξ : ℝ, ‖m ξ‖ ≤ 1) (ξ : ℝ) :
    logarithmicFourierWeight ξ * ‖(m ξ - 1) * F ξ‖ ^ 2 ≤
      4 * (logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) := by
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have hnorm : ‖(m ξ - 1) * F ξ‖ ≤ 2 * ‖F ξ‖ := by
    calc
      ‖(m ξ - 1) * F ξ‖ = ‖m ξ - 1‖ * ‖F ξ‖ := norm_mul _ _
      _ ≤ (‖m ξ‖ + ‖(1 : ℂ)‖) * ‖F ξ‖ :=
        mul_le_mul_of_nonneg_right (norm_sub_le _ _) (norm_nonneg _)
      _ ≤ 2 * ‖F ξ‖ := by
        have hh : ‖m ξ‖ + ‖(1 : ℂ)‖ ≤ 2 := by
          simpa only [norm_one] using add_le_add_right (hm ξ) 1
        exact mul_le_mul_of_nonneg_right hh (norm_nonneg _)
  have hdiff : 0 ≤ 2 * ‖F ξ‖ - ‖(m ξ - 1) * F ξ‖ :=
    sub_nonneg.mpr hnorm
  have hsum : 0 ≤ 2 * ‖F ξ‖ + ‖(m ξ - 1) * F ξ‖ := by positivity
  have hproduct := mul_nonneg hdiff hsum
  have hsq : ‖(m ξ - 1) * F ξ‖ ^ 2 ≤ 4 * ‖F ξ‖ ^ 2 := by
    nlinarith
  calc
    _ ≤ logarithmicFourierWeight ξ * (4 * ‖F ξ‖ ^ 2) :=
      mul_le_mul_of_nonneg_left hsq hw
    _ = _ := by ring

/-- Norm-one measurable complex multipliers preserve integrability of
the weighted *error energy* with explicit original source weight. -/
theorem f08_005_log_multiplier_error_integrable
    (F : RealComplexL2)
    (hF : Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) volume)
    (m : ℝ → ℂ)
    (hm : AEStronglyMeasurable m volume)
    (hbound : ∀ ξ : ℝ, ‖m ξ‖ ≤ 1) :
    Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖(m ξ - 1) * F ξ‖ ^ 2) volume := by
  have hbase : Integrable (fun ξ : ℝ =>
      4 * (logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2)) volume :=
    hF.const_mul 4
  apply hbase.mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      ((((hm.sub aestronglyMeasurable_const).mul
        (Lp.aestronglyMeasurable F)).norm).pow 2)
  · filter_upwards [] with ξ
    have hw : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    have hleft : 0 ≤ logarithmicFourierWeight ξ *
        ‖(m ξ - 1) * F ξ‖ ^ 2 := mul_nonneg hw (sq_nonneg _)
    have hright : 0 ≤ 4 *
        (logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) := by positivity
    simpa only [Real.norm_eq_abs, abs_of_nonneg hleft,
      abs_of_nonneg hright] using
      f08_005_log_multiplier_error_pointwise F m hbound ξ

/-- Strong weighted-energy convergence for measurable unit-bounded
Fourier multipliers approaching one pointwise. This is the spectral
dominated-convergence theorem needed by the physical mollifier interface. -/
theorem f08_005_log_multiplier_error_tendsto_zero
    (F : RealComplexL2)
    (hF : Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) volume)
    (m : ℕ → ℝ → ℂ)
    (hm : ∀ n, AEStronglyMeasurable (m n) volume)
    (hbound : ∀ n ξ, ‖m n ξ‖ ≤ 1)
    (hlim : ∀ ξ : ℝ, Tendsto (fun n => m n ξ) atTop (𝓝 (1 : ℂ))) :
    Tendsto (fun n => ∫ ξ : ℝ,
      logarithmicFourierWeight ξ * ‖(m n ξ - 1) * F ξ‖ ^ 2 ∂volume)
      atTop (𝓝 (0 : ℝ)) := by
  have hb : Integrable (fun ξ : ℝ =>
      4 * (logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2)) volume :=
    hF.const_mul 4
  have hmeas (n : ℕ) : AEStronglyMeasurable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖(m n ξ - 1) * F ξ‖ ^ 2) volume :=
    logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      (((((hm n).sub aestronglyMeasurable_const).mul
        (Lp.aestronglyMeasurable F)).norm).pow 2)
  have hdom (n : ℕ) : ∀ᵐ ξ ∂volume,
      ‖logarithmicFourierWeight ξ * ‖(m n ξ - 1) * F ξ‖ ^ 2‖ ≤
      4 * (logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) := by
    filter_upwards [] with ξ
    have hw : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    have hnonneg : 0 ≤ logarithmicFourierWeight ξ *
        ‖(m n ξ - 1) * F ξ‖ ^ 2 := mul_nonneg hw (sq_nonneg _)
    simpa only [Real.norm_eq_abs, abs_of_nonneg hnonneg] using
      f08_005_log_multiplier_error_pointwise F (m n) (hbound n) ξ
  have hpoint : ∀ᵐ ξ ∂volume,
      Tendsto (fun n =>
        logarithmicFourierWeight ξ * ‖(m n ξ - 1) * F ξ‖ ^ 2)
        atTop (𝓝 (0 : ℝ)) := by
    filter_upwards [] with ξ
    have hsub : Tendsto (fun n => m n ξ - (1 : ℂ))
        atTop (𝓝 (0 : ℂ)) := by
      convert (hlim ξ).sub_const (1 : ℂ) using 1 <;> simp
    have hprod : Tendsto (fun n => (m n ξ - 1) * F ξ)
        atTop (𝓝 (0 : ℂ)) := by
      convert hsub.mul_const (F ξ) using 1 <;> simp
    have hsq : Tendsto (fun n =>
        ‖(m n ξ - 1) * F ξ‖ ^ 2) atTop (𝓝 (0 : ℝ)) := by
      simpa using (hprod.norm.pow 2)
    simpa using (tendsto_const_nhds.mul hsq :
      Tendsto (fun n =>
        logarithmicFourierWeight ξ * ‖(m n ξ - 1) * F ξ‖ ^ 2)
        atTop (𝓝 (logarithmicFourierWeight ξ * (0 : ℝ))))
  have h := tendsto_integral_of_dominated_convergence
    (μ := volume)
    (F := fun (n : ℕ) (ξ : ℝ) => logarithmicFourierWeight ξ *
      ‖(m n ξ - 1) * F ξ‖ ^ 2)
    (f := fun _ : ℝ => (0 : ℝ))
    (fun ξ : ℝ => 4 * (logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2))
    hmeas hb hdom hpoint
  simpa using h

#print axioms f08_005_log_multiplier_error_pointwise
#print axioms f08_005_log_multiplier_error_integrable
#print axioms f08_005_log_multiplier_error_tendsto_zero

end
end WeilDefect
