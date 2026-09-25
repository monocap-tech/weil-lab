import Mathlib.Analysis.Normed.Lp.lpHolder
import Mathlib.Tactic

namespace WeilDefect

open Filter
open scoped Topology ENNReal lp

/-- The coordinate gains for the WD-X02 discrete critical-screening witness. -/
noncomputable def wdX02Weight (n : ℕ) : ℝ :=
  1 - 1 / ((n : ℝ) + 2)

theorem wd_x02_weight_nonneg (n : ℕ) :
    0 ≤ wdX02Weight n := by
  unfold wdX02Weight
  have hn : 2 ≤ (n : ℝ) + 2 := by positivity
  have hden : 0 < (n : ℝ) + 2 := by positivity
  have hinv : 1 / ((n : ℝ) + 2) ≤ 1 := by
    exact (div_le_one hden).2 (by linarith)
  linarith

theorem wd_x02_weight_lt_one (n : ℕ) :
    wdX02Weight n < 1 := by
  unfold wdX02Weight
  have hden : 0 < (n : ℝ) + 2 := by positivity
  have hinv : 0 < 1 / ((n : ℝ) + 2) := one_div_pos.mpr hden
  linarith

theorem wd_x02_weight_tendsto_one :
    Tendsto wdX02Weight atTop (𝓝 1) := by
  have hden :
      Tendsto (fun n : ℕ => (n : ℝ) + 2) atTop atTop :=
    tendsto_atTop_add_const_right _ _ tendsto_natCast_atTop_atTop
  have hinv :
      Tendsto (fun n : ℕ => (((n : ℝ) + 2)⁻¹)) atTop (𝓝 0) :=
    tendsto_inv_atTop_zero.comp hden
  simpa [wdX02Weight, div_eq_mul_inv] using
    (tendsto_const_nhds.sub hinv)

/-- The Hilbert carrier used for the discrete WD-X02 realization. -/
abbrev WDX02Space :=
  lp (fun _ : ℕ => ℂ) 2

/-- Coordinatewise scalar contraction with gain approaching one. -/
noncomputable def wdX02Coord (n : ℕ) : ℂ →L[ℂ] ℂ :=
  (wdX02Weight n : ℂ) • ContinuousLinearMap.id ℂ ℂ

theorem wd_x02_coord_norm_le_one (n : ℕ) :
    ‖wdX02Coord n‖ ≤ 1 := by
  have h0 := wd_x02_weight_nonneg n
  have h1 := (wd_x02_weight_lt_one n).le
  simp [wdX02Coord, norm_smul, abs_of_nonneg h0, h1]

/-- The infinite-dimensional critical screening operator. -/
noncomputable def wdX02Operator : WDX02Space →L[ℂ] WDX02Space :=
  lp.mapCLM 2 wdX02Coord zero_le_one wd_x02_coord_norm_le_one

theorem wd_x02_operator_norm_le_one :
    ‖wdX02Operator‖ ≤ 1 := by
  exact lp.norm_mapCLM_le
    2 wdX02Coord zero_le_one wd_x02_coord_norm_le_one


theorem wd_x02_operator_apply
    (x : WDX02Space) (n : ℕ) :
    (wdX02Operator x) n = (wdX02Weight n : ℂ) * x n := by
  rfl

theorem wd_x02_operator_single
    (n : ℕ) :
    wdX02Operator (lp.single 2 n (1 : ℂ))
      =
    (wdX02Weight n : ℂ) • lp.single 2 n (1 : ℂ) := by
  ext i
  by_cases h : n = i
  · subst i
    simp [wd_x02_operator_apply]
  · simp [wd_x02_operator_apply, lp.single_apply, h]

theorem wd_x02_operator_single_norm
    (n : ℕ) :
    ‖wdX02Operator (lp.single 2 n (1 : ℂ))‖ = wdX02Weight n := by
  rw [wd_x02_operator_single]
  simp [wd_x02_weight_nonneg]

theorem wd_x02_weight_le_operator_norm (n : ℕ) :
    wdX02Weight n ≤ ‖wdX02Operator‖ := by
  calc
    wdX02Weight n
        = ‖wdX02Operator (lp.single 2 n (1 : ℂ))‖ :=
          (wd_x02_operator_single_norm n).symm
    _ ≤ ‖wdX02Operator‖ * ‖lp.single 2 n (1 : ℂ)‖ :=
      wdX02Operator.le_opNorm _
    _ = ‖wdX02Operator‖ := by simp

theorem wd_x02_operator_norm_eq_one :
    ‖wdX02Operator‖ = 1 := by
  apply le_antisymm wd_x02_operator_norm_le_one
  exact le_of_tendsto wd_x02_weight_tendsto_one
    (Eventually.of_forall wd_x02_weight_le_operator_norm)



theorem wd_x02_operator_coord_norm
    (x : WDX02Space) (n : ℕ) :
    ‖(wdX02Operator x) n‖
      = wdX02Weight n * ‖x n‖ := by
  rw [wd_x02_operator_apply, norm_mul]
  simp [wd_x02_weight_nonneg]

theorem wd_x02_operator_coord_sq_le
    (x : WDX02Space) (n : ℕ) :
    ‖(wdX02Operator x) n‖ ^ (2 : ℝ)
      ≤ ‖x n‖ ^ (2 : ℝ) := by
  rw [wd_x02_operator_coord_norm]
  rw [Real.rpow_two, Real.rpow_two]
  have h0 := wd_x02_weight_nonneg n
  have h1 := (wd_x02_weight_lt_one n).le
  have hx := norm_nonneg (x n)
  nlinarith

theorem wd_x02_operator_coord_sq_lt
    (x : WDX02Space) (n : ℕ)
    (hx0 : x n ≠ 0) :
    ‖(wdX02Operator x) n‖ ^ (2 : ℝ)
      < ‖x n‖ ^ (2 : ℝ) := by
  rw [wd_x02_operator_coord_norm]
  rw [Real.rpow_two, Real.rpow_two]
  have h0 := wd_x02_weight_nonneg n
  have h1 := wd_x02_weight_lt_one n
  have hx : 0 < ‖x n‖ := norm_pos_iff.mpr hx0
  nlinarith

theorem wd_x02_nonzero_has_coordinate
    (x : WDX02Space) (hx : x ≠ 0) :
    ∃ n : ℕ, x n ≠ 0 := by
  by_contra h
  push_neg at h
  apply hx
  ext n
  simpa using h n

theorem wd_x02_strict_norm_loss
    (x : WDX02Space) (hx : x ≠ 0) :
    ‖wdX02Operator x‖ < ‖x‖ := by
  rcases wd_x02_nonzero_has_coordinate x hx with ⟨i, hi⟩
  have hsummable :
      Summable (fun n : ℕ => ‖x n‖ ^ (2 : ℝ)) :=
    (lp.hasSum_norm (p := (2 : ℝ≥0∞)) (by norm_num) x).summable
  have hsum :
      (∑' n : ℕ, ‖(wdX02Operator x) n‖ ^ (2 : ℝ))
        <
      ∑' n : ℕ, ‖x n‖ ^ (2 : ℝ) := by
    exact Summable.tsum_lt_tsum_of_nonneg
      (fun n => Real.rpow_nonneg (norm_nonneg _) _)
      (fun n => wd_x02_operator_coord_sq_le x n)
      (wd_x02_operator_coord_sq_lt x i hi)
      hsummable
  rw [← lp.norm_rpow_eq_tsum (p := (2 : ℝ≥0∞)) (by norm_num)
        (wdX02Operator x),
      ← lp.norm_rpow_eq_tsum (p := (2 : ℝ≥0∞)) (by norm_num) x] at hsum
  rw [Real.rpow_two, Real.rpow_two] at hsum
  nlinarith [norm_nonneg (wdX02Operator x), norm_nonneg x]

theorem wd_x02_no_nonzero_norm_attainer :
    ¬ ∃ x : WDX02Space, x ≠ 0 ∧ ‖wdX02Operator x‖ = ‖x‖ := by
  rintro ⟨x, hx, heq⟩
  exact (ne_of_lt (wd_x02_strict_norm_loss x hx)) heq

/--
WD-X02 discrete critical screening witness:
the contraction has norm exactly one, every nonzero vector loses norm
strictly, while standard basis directions approach the critical value.
-/
theorem wd_x02_critical_nonattainment :
    ‖wdX02Operator‖ = 1
      ∧ (∀ x : WDX02Space, x ≠ 0 →
          ‖wdX02Operator x‖ < ‖x‖)
      ∧ Tendsto
          (fun n : ℕ =>
            ‖wdX02Operator (lp.single 2 n (1 : ℂ))‖)
          atTop (𝓝 1) := by
  refine ⟨wd_x02_operator_norm_eq_one, wd_x02_strict_norm_loss, ?_⟩
  simpa [wd_x02_operator_single_norm] using wd_x02_weight_tendsto_one


end WeilDefect
