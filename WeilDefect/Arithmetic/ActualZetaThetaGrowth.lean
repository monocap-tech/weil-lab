import WeilDefect.Arithmetic.ActualZetaJensenGrowth
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

namespace WeilDefect

noncomputable section

open Filter Asymptotics Set
open scoped Topology

/-- The actual theta remainder used by the completed-zeta Mellin construction. -/
def neutralActualZetaThetaRemainder (t : ℝ) : ℝ :=
  HurwitzZeta.evenKernel 0 t - 1

theorem neutralActualZetaThetaRemainder_continuousOn :
    ContinuousOn neutralActualZetaThetaRemainder (Ioi 0) :=
  (HurwitzZeta.continuousOn_evenKernel 0).sub continuousOn_const

/-- Extend actual theta exponential decay across the finite initial interval.
The constants come from the actual kernel, not divisor-count data. -/
theorem neutralActualZetaThetaRemainder_exponential_bound :
    ∃ p C : ℝ, 0 < p ∧ 0 < C ∧
      ∀ t : ℝ, 1 ≤ t →
        |neutralActualZetaThetaRemainder t| ≤ C * Real.exp (-p * t) := by
  obtain ⟨p, hp, hdecay⟩ := HurwitzZeta.isBigO_atTop_evenKernel_sub (0 : UnitAddCircle)
  have hd : neutralActualZetaThetaRemainder =O[atTop]
      (fun t : ℝ => Real.exp (-p * t)) := by
    simpa only [neutralActualZetaThetaRemainder, ite_true] using hdecay
  obtain ⟨c, hc, hcb⟩ := hd.exists_pos
  have he : ∀ᶠ t : ℝ in atTop,
      |neutralActualZetaThetaRemainder t| ≤ c * Real.exp (-p * t) := by
    simpa only [Asymptotics.IsBigOWith, Real.norm_eq_abs,
      abs_of_pos (Real.exp_pos _)] using hcb
  obtain ⟨a, ha⟩ := eventually_atTop.mp he
  let b : ℝ := max a 1
  let F : ℝ → ℝ := fun t =>
    |neutralActualZetaThetaRemainder t| * Real.exp (p * t)
  have hF : ContinuousOn F (Icc 1 b) := by
    exact (neutralActualZetaThetaRemainder_continuousOn.mono
      (fun t ht => lt_of_lt_of_le zero_lt_one ht.1)).abs.mul
      (by fun_prop)
  obtain ⟨B, hB⟩ := (isCompact_Icc.image_of_continuousOn hF).bddAbove
  refine ⟨p, max c (B + 1), hp, hc.trans_le (le_max_left _ _), ?_⟩
  intro t ht
  by_cases hat : a ≤ t
  · exact (ha t hat).trans (mul_le_mul_of_nonneg_right
      (le_max_left _ _) (Real.exp_pos _).le)
  · have htb : t ≤ b := (le_of_not_ge hat).trans (le_max_left _ _)
    have hsmall : F t ≤ B := hB ⟨t, ⟨ht, htb⟩, rfl⟩
    have hFC : F t ≤ max c (B + 1) :=
      hsmall.trans ((le_add_of_nonneg_right zero_le_one).trans (le_max_right _ _))
    have hm := mul_le_mul_of_nonneg_right hFC (Real.exp_pos (-p * t)).le
    simpa only [F, mul_assoc, ← Real.exp_add,
      (by ring : p * t + -p * t = 0), Real.exp_zero, mul_one] using hm

/-- Explicit factorial majorant for each polynomial moment of actual theta.
Half of the exponential decay is retained for integration. -/
theorem neutralActualZetaThetaRemainder_polynomial_bound
    {p C : ℝ} (hp : 0 < p)
    (hbound : ∀ t : ℝ, 1 ≤ t →
      |neutralActualZetaThetaRemainder t| ≤ C * Real.exp (-p * t))
    (n : ℕ) {t : ℝ} (ht : 1 ≤ t) :
    t ^ n * |neutralActualZetaThetaRemainder t| ≤
      C * ((n.factorial : ℝ) / (p / 2) ^ n) * Real.exp (-(p / 2) * t) := by
  have ht0 : 0 ≤ t := zero_le_one.trans ht
  have hq : 0 < p / 2 := by positivity
  have hf : (0 : ℝ) < n.factorial := by positivity
  have hx := Real.pow_div_factorial_le_exp
    (show 0 ≤ (p / 2) * t by positivity) n
  have hpow : t ^ n ≤ ((n.factorial : ℝ) / (p / 2) ^ n) *
      Real.exp ((p / 2) * t) := by
    rw [mul_pow, div_le_iff₀ hf] at hx
    apply (mul_le_mul_left (pow_pos hq n)).mp
    convert hx using 1 <;> field_simp <;> ring
  calc
    _ ≤ t ^ n * (C * Real.exp (-p * t)) :=
      mul_le_mul_of_nonneg_left (hbound t ht) (pow_nonneg ht0 n)
    _ = C * (t ^ n * Real.exp (-p * t)) := by ring
    _ ≤ C * ((((n.factorial : ℝ) / (p / 2) ^ n) *
        Real.exp ((p / 2) * t)) * Real.exp (-p * t)) := by
      have hC : 0 ≤ C := by
        have h := hbound 1 (le_refl 1)
        have : 0 ≤ C * Real.exp (-p * 1) := (abs_nonneg _).trans h
        nlinarith [Real.exp_pos (-p * 1)]
      exact mul_le_mul_of_nonneg_left
        (mul_le_mul_of_nonneg_right hpow (Real.exp_pos _).le) hC
    _ = _ := by
      rw [mul_assoc, mul_assoc, ← Real.exp_add]
      congr 2
      ring


/-- The actual theta polynomial moments are integrable, with an explicit
factorial bound uniform in the moment order. -/
theorem neutralActualZetaThetaRemainder_moments :
    ∃ p C : ℝ, 0 < p ∧ 0 < C ∧ ∀ n : ℕ,
      MeasureTheory.IntegrableOn
        (fun t : ℝ => t ^ n * |neutralActualZetaThetaRemainder t|) (Ioi 1) ∧
      (∫ t : ℝ in Ioi 1, t ^ n * |neutralActualZetaThetaRemainder t|) ≤
        C * ((n.factorial : ℝ) / (p / 2) ^ n) *
          (Real.exp (-(p / 2)) / (p / 2)) := by
  obtain ⟨p, C, hp, hC, hb⟩ := neutralActualZetaThetaRemainder_exponential_bound
  refine ⟨p, C, hp, hC, fun n => ?_⟩
  let K : ℝ := C * ((n.factorial : ℝ) / (p / 2) ^ n)
  have hm : MeasureTheory.IntegrableOn
      (fun t : ℝ => K * Real.exp (-(p / 2) * t)) (Ioi 1) :=
    (integrableOn_exp_mul_Ioi (by linarith : -(p / 2) < 0) 1).const_mul K
  have hc : ContinuousOn
      (fun t : ℝ => t ^ n * |neutralActualZetaThetaRemainder t|) (Ioi 1) :=
    (by fun_prop : ContinuousOn (fun t : ℝ => t ^ n) (Ioi 1)).mul
      (neutralActualZetaThetaRemainder_continuousOn.mono
        (fun t ht => zero_lt_one.trans ht)).abs
  have hi : MeasureTheory.IntegrableOn
      (fun t : ℝ => t ^ n * |neutralActualZetaThetaRemainder t|) (Ioi 1) := by
    apply hm.mono' (hc.aestronglyMeasurable measurableSet_Ioi)
    filter_upwards [MeasureTheory.ae_restrict_mem measurableSet_Ioi] with t ht
    have ht0 : 0 ≤ t := zero_le_one.trans ht.le
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    exact neutralActualZetaThetaRemainder_polynomial_bound hp hb n ht.le
  refine ⟨hi, ?_⟩
  calc
    _ ≤ ∫ t : ℝ in Ioi 1, K * Real.exp (-(p / 2) * t) := by
      apply MeasureTheory.integral_mono_ae hi hm
      filter_upwards [MeasureTheory.ae_restrict_mem measurableSet_Ioi] with t ht
      exact neutralActualZetaThetaRemainder_polynomial_bound hp hb n ht.le
    _ = K * (Real.exp (-(p / 2)) / (p / 2)) := by
      rw [MeasureTheory.integral_const_mul,
        integral_exp_mul_Ioi (by linarith : -(p / 2) < 0) 1]
      simp
    _ = _ := rfl

end
end WeilDefect
