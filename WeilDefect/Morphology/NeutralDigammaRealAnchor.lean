import WeilDefect.Morphology.NeutralDigammaPairingLimit
import Mathlib.NumberTheory.Harmonic.EulerMascheroni

namespace WeilDefect

noncomputable section

open Filter
open scoped BigOperators Topology

/-- Positive real arguments avoid the actual Gamma/digamma poles. -/
theorem neutralPositiveReal_ne_neg_nat {x : ℝ} (hx : 0 < x) (n : ℕ) :
    (x : ℂ) ≠ -(n : ℂ) := by
  intro h
  have hr := congrArg Complex.re h
  simp only [Complex.ofReal_re, Complex.neg_re, Complex.natCast_re] at hr
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  linarith

/-- Independent actual positive-real normalization, from log-convexity. -/
theorem neutralDigamma_real_shift_sub_log_tendsto {x : ℝ} (hx : 0 < x) :
    Tendsto (fun N : ℕ => (Complex.digamma (((N : ℝ)+x : ℝ) : ℂ)).re -
      Real.log (N : ℝ)) atTop (𝓝 0) := by
  have hl := (Real.tendsto_log_comp_add_sub_log (x-1)).comp
    tendsto_natCast_atTop_atTop
  have hu := (Real.tendsto_log_comp_add_sub_log x).comp
    tendsto_natCast_atTop_atTop
  apply tendsto_of_tendsto_of_tendsto_of_le_of_le' hl hu
  · filter_upwards [eventually_ge_atTop (2 : ℕ)] with N hN
    have hn : (2 : ℝ) ≤ N := by exact_mod_cast hN
    have h := neutralDigamma_log_sub_one_le (x := (N : ℝ)+x) (by linarith)
    have he : (N : ℝ)+(x-1) = (N : ℝ)+x-1 := by ring
    change Real.log ((N : ℝ)+(x-1)) - Real.log (N : ℝ) ≤ _
    rw [he]
    linarith
  · filter_upwards with N
    have h := neutralDigamma_real_le_log (x := (N : ℝ)+x) (by positivity)
    change _ ≤ Real.log ((N : ℝ)+x) - Real.log (N : ℝ)
    linarith

theorem neutralDigamma_real_finite_recurrence {x : ℝ} (hx : 0 < x) (N : ℕ) :
    (Complex.digamma (((N : ℝ)+x : ℝ) : ℂ)).re =
      (Complex.digamma (x : ℂ)).re +
        ∑ n ∈ Finset.range N, 1 / (x+(n : ℝ)) := by
  have h := congrArg Complex.re
    (Complex.digamma_apply_add_nat (neutralPositiveReal_ne_neg_nat hx) N)
  have hs : (∑ n ∈ Finset.range N, ((x : ℂ)+(n : ℂ))⁻¹).re =
      ∑ n ∈ Finset.range N, 1 / (x+(n : ℝ)) := by
    rw [Complex.re_sum]
    apply Finset.sum_congr rfl
    intro n _
    rw [← Complex.ofReal_natCast, ← Complex.ofReal_add, ← Complex.ofReal_inv,
      Complex.ofReal_re, one_div]
  simp only [Complex.add_re, hs] at h
  convert h using 1 <;> simp only [Complex.ofReal_add, Complex.ofReal_natCast, add_comm]

/-- Actual Euler normalization on the whole positive real axis. -/
theorem neutralDigamma_real_euler_partial_tendsto {x : ℝ} (hx : 0 < x) :
    Tendsto (fun N : ℕ => ∑ n ∈ Finset.range N,
      (1 / ((n : ℝ)+1) - 1 / (x+(n : ℝ)))) atTop
        (𝓝 ((Complex.digamma (x : ℂ)).re + Real.eulerMascheroniConstant)) := by
  have hh : ∀ N : ℕ, (harmonic N : ℝ) =
      ∑ n ∈ Finset.range N, 1 / ((n : ℝ)+1) := by
    intro N
    simp [harmonic, one_div]
  have h := (Real.tendsto_harmonic_sub_log.sub
    (neutralDigamma_real_shift_sub_log_tendsto hx)).add_const
      (Complex.digamma (x : ℂ)).re
  simp only [sub_zero] at h
  convert h using 1
  · funext N
    rw [hh, neutralDigamma_real_finite_recurrence hx N, Finset.sum_sub_distrib]
    ring
  · ring

/-- A summable bound for the real regularized Euler terms, independent of
any digamma representation formula. -/
theorem neutralDigamma_real_euler_term_bound {x : ℝ} (hx : 0 < x) (n : ℕ) :
    ‖1 / ((n : ℝ)+1) - 1 / (x+(n : ℝ))‖ ≤
      (|x-1| / min x 1) * (1 / ((n : ℝ)+1)^2) := by
  let d := min x 1
  have hd : 0 < d := lt_min hx zero_lt_one
  have hdx : d ≤ x := min_le_left _ _
  have hd1 : d ≤ 1 := min_le_right _ _
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hs : 0 < (n : ℝ)+1 := by positivity
  have ht : 0 < x+(n : ℝ) := by positivity
  have hst : d*((n : ℝ)+1) ≤ x+(n : ℝ) := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hd1) hn]
  have hden : d*((n : ℝ)+1)^2 ≤ ((n : ℝ)+1)*(x+(n : ℝ)) := by
    nlinarith [mul_le_mul_of_nonneg_left hst hs.le]
  have he : 1 / ((n : ℝ)+1) - 1 / (x+(n : ℝ)) =
      (x-1) / (((n : ℝ)+1)*(x+(n : ℝ))) := by
    field_simp
    ring
  rw [he, Real.norm_eq_abs, abs_div, abs_of_pos (mul_pos hs ht)]
  calc
    |x-1| / (((n : ℝ)+1)*(x+(n : ℝ))) ≤ |x-1| / (d*((n : ℝ)+1)^2) :=
      div_le_div_of_nonneg_left (abs_nonneg _) (by positivity) hden
    _ = (|x-1| / min x 1) * (1 / ((n : ℝ)+1)^2) := by
      dsimp [d]
      field_simp [ne_of_gt (lt_min hx zero_lt_one), ne_of_gt hs]
      ring

theorem neutralDigamma_real_euler_summable {x : ℝ} (hx : 0 < x) :
    Summable (fun n : ℕ => 1 / ((n : ℝ)+1) - 1 / (x+(n : ℝ))) := by
  have hs : Summable (fun n : ℕ => 1 / ((n : ℝ)+1)^2) := by
    simpa only [Nat.cast_add, Nat.cast_one] using
      (summable_nat_add_iff (f := fun n : ℕ => 1 / (n : ℝ)^2) 1).mpr
        (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < (2 : ℕ)))
  exact (hs.mul_left (|x-1| / min x 1)).of_norm_bounded
    (fun n => neutralDigamma_real_euler_term_bound hx n)

/-- Certified actual real-axis series anchor for the later complex identity
argument. No complex source-line cancellation is claimed here. -/
theorem neutralDigamma_real_euler_hasSum {x : ℝ} (hx : 0 < x) :
    HasSum (fun n : ℕ => 1 / ((n : ℝ)+1) - 1 / (x+(n : ℝ)))
      ((Complex.digamma (x : ℂ)).re + Real.eulerMascheroniConstant) :=
  ((neutralDigamma_real_euler_summable hx).hasSum_iff_tendsto_nat).mpr
    (neutralDigamma_real_euler_partial_tendsto hx)

theorem neutralDigamma_real_eq_euler_series {x : ℝ} (hx : 0 < x) :
    (Complex.digamma (x : ℂ)).re = -Real.eulerMascheroniConstant +
      ∑' n : ℕ, (1 / ((n : ℝ)+1) - 1 / (x+(n : ℝ))) := by
  rw [(neutralDigamma_real_euler_hasSum hx).tsum_eq]
  ring

end

end WeilDefect
