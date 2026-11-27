/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
The Dirichlet-series bound below is adapted from
Zeta23/RvM/ZetaGrowth.lean, mirror revision 77f832c86fbb3e5336b949dae0fdcae26baea87c.
The RECON interfaces and elementary half-plane reduction are new.
-/
import WeilDefect.MasterRecon.V10B7a
import Mathlib.NumberTheory.ZetaValues
import Mathlib.Analysis.Real.Pi.Bounds

namespace WeilDefect.MasterRecon.V10B7b

open Complex Set Real

theorem norm_riemannZeta_sub_one_le {s : ℂ} (hs : 2 ≤ s.re) :
    ‖riemannZeta s - 1‖ ≤ Real.pi ^ 2 / 6 - 1 := by
  have hs1 : 1 < s.re := by linarith
  -- the shifted Dirichlet series  f n := 1/(n+1)^s,  ζ s = ∑' f n
  set f : ℕ → ℂ := fun n => 1 / ((n : ℂ) + 1) ^ s with hf
  have hsum : Summable f := by
    have h0 := Complex.summable_one_div_nat_cpow.mpr hs1
    have := (summable_nat_add_iff 1).mpr h0
    simpa [f] using this
  have hzeta : riemannZeta s = ∑' n, f n := zeta_eq_tsum_one_div_nat_add_one_cpow hs1
  have hf0 : f 0 = 1 := by simp [f]
  have hsplit : riemannZeta s - 1 = ∑' n, f (n + 1) := by
    rw [hzeta, hsum.tsum_eq_zero_add, hf0]; ring
  -- termwise comparison with 1/(n+2)^2
  have hle : ∀ n : ℕ, ‖f (n + 1)‖ ≤ 1 / ((n : ℝ) + 2) ^ 2 := by
    intro n
    have hpos : 0 < n + 2 := by omega
    have hf1 : f (n + 1) = 1 / ((n + 2 : ℕ) : ℂ) ^ s := by
      simp only [f]
      congr 2
      push_cast
      ring
    rw [hf1, norm_div, norm_one, Complex.norm_natCast_cpow_of_pos hpos]
    have hbase : (1 : ℝ) ≤ ((n + 2 : ℕ) : ℝ) := by exact_mod_cast hpos
    have hpow : ((n + 2 : ℕ) : ℝ) ^ (2 : ℝ) ≤ ((n + 2 : ℕ) : ℝ) ^ s.re :=
      Real.rpow_le_rpow_of_exponent_le hbase hs
    rw [Real.rpow_two] at hpow
    have h2pos : (0 : ℝ) < ((n + 2 : ℕ) : ℝ) ^ 2 := by positivity
    calc 1 / ((n + 2 : ℕ) : ℝ) ^ s.re ≤ 1 / ((n + 2 : ℕ) : ℝ) ^ 2 :=
          one_div_le_one_div_of_le h2pos hpow
      _ = 1 / ((n : ℝ) + 2) ^ 2 := by push_cast; ring
  have htwo : HasSum (fun n : ℕ => 1 / ((n : ℝ) + 2) ^ 2) (Real.pi ^ 2 / 6 - 1) := by
    have h := (hasSum_nat_add_iff' 2).mpr hasSum_zeta_two
    norm_num [Finset.sum_range_succ] at h
    exact h.congr_fun fun n => by ring
  rw [hsplit]
  have hsum' : Summable (fun n => f (n + 1)) := (summable_nat_add_iff 1).mpr hsum
  calc ‖∑' n, f (n + 1)‖ ≤ ∑' n, ‖f (n + 1)‖ := norm_tsum_le_tsum_norm hsum'.norm
    _ ≤ ∑' n : ℕ, 1 / ((n : ℝ) + 2) ^ 2 := hsum'.norm.tsum_le_tsum hle htwo.summable
    _ = Real.pi ^ 2 / 6 - 1 := htwo.tsum_eq


theorem center_lower : V10B7a.CenterLower := by
  intro t
  have h := norm_riemannZeta_sub_one_le (s := V10B7a.center t)
    (by rw [V10B7a.center_re])
  have h' : ‖(1 : ℂ)‖ - ‖1 - riemannZeta (V10B7a.center t)‖ ≤
      ‖riemannZeta (V10B7a.center t)‖ := by
    simpa using norm_sub_norm_le (1 : ℂ) (1-riemannZeta (V10B7a.center t))
  rw [norm_sub_rev,norm_one] at h'
  have hpi := Real.pi_lt_d2
  have hp := Real.pi_pos
  nlinarith [sq_nonneg (Real.pi-3.15)]

/-- The remaining analytic input is the standard elementary half-plane
bound from one-term Euler summation, rather than a zero-count theorem. -/
def ElementaryZetaBound : Prop :=
  ∀ z : ℂ, 0 < z.re → z ≠ 1 →
    ‖riemannZeta z‖ ≤ 1/2 + 1/‖1-z‖ + ‖z‖/z.re

theorem growth_of_elementary_bound (h : ElementaryZetaBound) :
    V10B7a.HalfPlaneGrowth := by
  refine ⟨5,by norm_num,?_⟩
  intro z hσ hpole
  have hpos : 0 < z.re := by linarith
  have hne : z ≠ 1 := by
    intro hz
    rw [hz,sub_self,norm_zero] at hpole
    norm_num at hpole
  have h0 := h z hpos hne
  have h1 : 1/‖1-z‖ ≤ 1 := by
    rw [norm_sub_rev]
    exact (div_le_one (by linarith)).mpr hpole
  have hnorm := Complex.norm_le_abs_re_add_abs_im z
  rw [abs_of_pos hpos] at hnorm
  have h2 : ‖z‖/z.re ≤ 1 + 5*|z.im| := by
    apply (div_le_iff₀ hpos).mpr
    nlinarith [mul_nonneg (show 0 ≤ 5*z.re-1 by linarith) (abs_nonneg z.im)]
  linarith [abs_nonneg z.im]

theorem local_count_of_elementary_bound (h : ElementaryZetaBound)
    (hr : ∀ z, V09D.stripZero z → V09D.stripZero (V10A.reflect z))
    (hm : ∀ z, V09D.stripZero z → V09D.mult (V10A.reflect z) = V09D.mult z) :
    ∃ A : ℝ, 1 ≤ A ∧ ∀ t : ℝ,
      (V09D.count t (t+1) : ℝ) ≤ A*Real.log (|t|+3) :=
  V10B7a.all_real_local_count (growth_of_elementary_bound h) center_lower hr hm

end WeilDefect.MasterRecon.V10B7b

#print axioms WeilDefect.MasterRecon.V10B7b.norm_riemannZeta_sub_one_le
#print axioms WeilDefect.MasterRecon.V10B7b.center_lower
#print axioms WeilDefect.MasterRecon.V10B7b.growth_of_elementary_bound
#print axioms WeilDefect.MasterRecon.V10B7b.local_count_of_elementary_bound
