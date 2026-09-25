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

end WeilDefect
