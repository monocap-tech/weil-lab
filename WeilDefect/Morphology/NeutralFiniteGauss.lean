import WeilDefect.Morphology.NeutralWeilCoreSplit
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Algebra.Ring.GeomSum

namespace WeilDefect

noncomputable section

open Filter
open scoped BigOperators Topology

def neutralDigammaLine (t : ℝ) : ℂ := (1/4 : ℂ) + Complex.I * ((t : ℂ)/2)

/-- The source line avoids every digamma recurrence pole. -/
theorem neutralDigammaLine_ne_neg_nat (t : ℝ) (m : ℕ) :
    neutralDigammaLine t ≠ -(m : ℂ) := by
  intro h
  have hr := congrArg Complex.re h
  simp [neutralDigammaLine] at hr
  have hm : (0 : ℝ) ≤ m := Nat.cast_nonneg m
  linarith

/-- Exact real reciprocal coefficient in the finite digamma recurrence. -/
def neutralGaussReciprocal (n : ℕ) (t : ℝ) : ℝ :=
  ((n : ℝ) + 1/4) / (((n : ℝ) + 1/4)^2 + (t/2)^2)

theorem neutralDigammaLine_inv_re (n : ℕ) (t : ℝ) :
    ((neutralDigammaLine t + (n : ℂ))⁻¹).re = neutralGaussReciprocal n t := by
  simp [neutralDigammaLine, neutralGaussReciprocal, Complex.inv_re,
    Complex.normSq_apply, pow_two, add_comm, add_left_comm, add_assoc]

/-- Actual source symbol split, derived solely from the proved recurrence. -/
theorem neutralArchimedeanSymbol_finite_tail (N : ℕ) (t : ℝ) :
    compactWindowArchimedeanSymbol t =
      (Complex.digamma (neutralDigammaLine t + (N : ℂ))).re - Real.log Real.pi -
        ∑ n ∈ Finset.range N, neutralGaussReciprocal n t := by
  have h := congrArg Complex.re
    (Complex.digamma_apply_add_nat (neutralDigammaLine_ne_neg_nat t) N)
  have hsum : (∑ n ∈ Finset.range N, (neutralDigammaLine t + (n : ℂ))⁻¹).re =
      ∑ n ∈ Finset.range N, neutralGaussReciprocal n t := by
    induction N with
    | zero => simp
    | succ N ih =>
      simp only [Finset.sum_range_succ, Complex.add_re, ih, neutralDigammaLine_inv_re]
  simp only [Complex.add_re, hsum] at h
  change (Complex.digamma (neutralDigammaLine t)).re - Real.log Real.pi = _
  rw [h]
  ring

/-- Positive finite half-density; its negative is the signed kernel candidate. -/
def neutralFiniteGaussKernel (N : ℕ) (z : ℝ) : ℝ :=
  Real.exp (-|z|/2) * ∑ n ∈ Finset.range N, (Real.exp (-2*|z|))^n

theorem neutralFiniteGaussKernel_nonneg (N : ℕ) (z : ℝ) :
    0 ≤ neutralFiniteGaussKernel N z := by
  unfold neutralFiniteGaussKernel
  positivity

/-- The exact geometric remainder away from the singular diagonal. -/
theorem neutralFiniteGaussKernel_eq (N : ℕ) {z : ℝ} (hz : z ≠ 0) :
    neutralFiniteGaussKernel N z =
      archimedeanGapKernel |z| z * (1 - (Real.exp (-2*|z|))^N) := by
  have hd : 1 - Real.exp (-2*|z|) ≠ 0 := by
    have h := archimedeanGapKernel_denominator_pos (abs_pos.mpr hz) z
    simpa only [max_self] using ne_of_gt h
  unfold neutralFiniteGaussKernel archimedeanGapKernel
  simp only [max_self]
  rw [div_mul_eq_mul_div, eq_div_iff hd, mul_assoc, geom_sum_mul_neg]

/-- Actual pointwise convergence of the finite kernel, not an operator limit. -/
theorem neutralFiniteGaussKernel_tendsto {z : ℝ} (hz : z ≠ 0) :
    Tendsto (fun N : ℕ => neutralFiniteGaussKernel N z) atTop
      (𝓝 (archimedeanGapKernel |z| z)) := by
  have hr : Real.exp (-2*|z|) < 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_lt_exp.mpr
    nlinarith [abs_pos.mpr hz]
  have hp := tendsto_pow_atTop_nhds_zero_of_lt_one (Real.exp_nonneg (-2*|z|)) hr
  simp_rw [neutralFiniteGaussKernel_eq _ hz]
  have hc : Tendsto (fun _ : ℕ => archimedeanGapKernel |z| z) atTop
      (𝓝 (archimedeanGapKernel |z| z)) := tendsto_const_nhds
  have h1 : Tendsto (fun _ : ℕ => (1 : ℝ)) atTop (𝓝 (1 : ℝ)) := tendsto_const_nhds
  simpa using hc.mul (h1.sub hp)

end

end WeilDefect
