import WeilDefect.Arithmetic.ActualZetaThetaGrowth
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity

namespace WeilDefect
noncomputable section
open Set MeasureTheory
open scoped Topology

/-- Actual theta tail with an arbitrary complex Mellin exponent. -/
def neutralActualZetaThetaMellinTailIntegrand (s : ℂ) (t : ℝ) : ℂ :=
  (t : ℂ) ^ (s - 1) * (neutralActualZetaThetaRemainder t : ℂ)

/-- Complex Mellin weights above one are dominated by an integer moment. -/
theorem neutralActualZetaThetaMellinTail_norm_le
    (s : ℂ) (n : ℕ) (hs : s.re - 1 ≤ (n : ℝ))
    {t : ℝ} (ht : 1 ≤ t) :
    ‖neutralActualZetaThetaMellinTailIntegrand s t‖ ≤
      t ^ n * |neutralActualZetaThetaRemainder t| := by
  have ht0 : 0 < t := zero_lt_one.trans_le ht
  rw [neutralActualZetaThetaMellinTailIntegrand, norm_mul,
    Complex.norm_cpow_eq_rpow_re_of_pos ht0,
    Complex.norm_real, Real.norm_eq_abs]
  apply mul_le_mul_of_nonneg_right _ (abs_nonneg _)
  simpa only [Complex.sub_re, Complex.one_re, Real.rpow_natCast] using
    (Real.rpow_le_rpow_of_exponent_le ht hs)

/-- Same actual decay constants bound every complex Mellin tail dominated
by moment n; no zero-count or operator-domain premise is used. -/
theorem neutralActualZetaThetaMellinTail_bound :
    ∃ p C : ℝ, 0 < p ∧ 0 < C ∧ ∀ (n : ℕ) (s : ℂ),
      s.re - 1 ≤ (n : ℝ) →
      IntegrableOn (neutralActualZetaThetaMellinTailIntegrand s) (Ioi 1) ∧
      ‖∫ t : ℝ in Ioi 1, neutralActualZetaThetaMellinTailIntegrand s t‖ ≤
        C * ((n.factorial : ℝ) / (p / 2) ^ n) *
          (Real.exp (-(p / 2)) / (p / 2)) := by
  obtain ⟨p, C, hp, hC, hm⟩ := neutralActualZetaThetaRemainder_moments
  refine ⟨p, C, hp, hC, fun n s hs => ?_⟩
  have hc : ContinuousOn (neutralActualZetaThetaMellinTailIntegrand s) (Ioi 1) := by
    apply ContinuousOn.mul
    · apply continuousOn_of_forall_continuousAt
      intro t ht
      exact Complex.continuousAt_ofReal_cpow_const t (s - 1)
        (Or.inr (ne_of_gt (zero_lt_one.trans ht)))
    · exact Complex.continuous_ofReal.comp_continuousOn
        (neutralActualZetaThetaRemainder_continuousOn.mono
          (Ioi_subset_Ioi (show (0 : ℝ) ≤ 1 by norm_num)))
  have hi : IntegrableOn (neutralActualZetaThetaMellinTailIntegrand s) (Ioi 1) := by
    apply (hm n).1.mono' (hc.aestronglyMeasurable measurableSet_Ioi)
    filter_upwards [ae_restrict_mem measurableSet_Ioi] with t ht
    exact neutralActualZetaThetaMellinTail_norm_le s n hs ht.le
  refine ⟨hi, ?_⟩
  calc
    _ ≤ ∫ t : ℝ in Ioi 1, t ^ n * |neutralActualZetaThetaRemainder t| := by
      apply norm_integral_le_of_norm_le (hm n).1
      filter_upwards [ae_restrict_mem measurableSet_Ioi] with t ht
      exact neutralActualZetaThetaMellinTail_norm_le s n hs ht.le
    _ ≤ _ := (hm n).2

/-- The two completed-zeta Mellin exponents share a moment bound on a
natural-radius disk. This includes every point of its boundary circle. -/
theorem neutralActualZetaThetaMellinTail_disk_exponents
    (n : ℕ) {z : ℂ} (hz : ‖z‖ ≤ (n : ℝ)) :
    (z / 2).re - 1 ≤ (n : ℝ) ∧
      ((1 - z) / 2).re - 1 ≤ (n : ℝ) := by
  have hr := Complex.re_le_norm z
  have hl : -z.re ≤ ‖z‖ := by
    simpa only [Complex.neg_re, norm_neg] using Complex.re_le_norm (-z)
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  constructor <;> simp only [Complex.div_ofNat_re, Complex.sub_re,
    Complex.one_re] <;> linarith

end
end WeilDefect
