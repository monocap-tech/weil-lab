import Mathlib

namespace WeilDefect
noncomputable section
open Filter

/-! NF582: the literal NF528 compression sequence and its shrinking
positive mollifier radius. No abstract choice of convergent sequence. -/

def neutralNF582Scale (n : ℕ) : ℝ :=
  1 - (1 / ((n : ℝ)+1))/2

theorem neutralNF582Scale_half_le (n : ℕ) :
    1/2 ≤ neutralNF582Scale n := by
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hp : 0 < (n : ℝ)+1 := by positivity
  have hd : 1 / ((n : ℝ)+1) ≤ 1 :=
    (div_le_iff₀ hp).mpr (by linarith)
  unfold neutralNF582Scale
  linarith

theorem neutralNF582Scale_pos (n : ℕ) :
    0 < neutralNF582Scale n :=
  lt_of_lt_of_le (by norm_num) (neutralNF582Scale_half_le n)

theorem neutralNF582Scale_lt_one (n : ℕ) :
    neutralNF582Scale n < 1 := by
  have hp : 0 < 1 / ((n : ℝ)+1) := by positivity
  unfold neutralNF582Scale
  linarith

theorem neutralNF582Scale_tendsto :
    Tendsto neutralNF582Scale atTop (nhds 1) := by
  have hd : Tendsto (fun n : ℕ => 1/((n : ℝ)+1)) atTop (nhds 0) :=
    tendsto_one_div_add_atTop_nhds_zero_nat
  have h2 : Tendsto (fun _ : ℕ => (2:ℝ)) atTop (nhds 2) := tendsto_const_nhds
  have h1 : Tendsto (fun _ : ℕ => (1:ℝ)) atTop (nhds 1) := tendsto_const_nhds
  have h := h1.sub (hd.div h2 (by norm_num))
  simpa [neutralNF582Scale] using h

end
end WeilDefect
