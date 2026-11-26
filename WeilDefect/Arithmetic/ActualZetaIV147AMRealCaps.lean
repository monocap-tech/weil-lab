import Mathlib

namespace WeilDefect
noncomputable section

/-- Attach the two strict exponential endpoint comparisons to a signed
translation. The comparisons for each concrete n remain separate inputs. -/
theorem neutralIV147Log_endpoints (n : ℝ) (j : ℤ)
    (hn : 0 < n)
    (hl : Real.exp ((j:ℝ)/4096) < n)
    (hu : n < Real.exp (((j:ℝ)+1)/4096)) :
    (j:ℝ) < 4096 * Real.log n ∧
      4096 * Real.log n < (j:ℝ)+1 := by
  rw [← Real.exp_log hn] at hl hu
  have hl' := Real.exp_lt_exp.mp hl
  have hu' := Real.exp_lt_exp.mp hu
  constructor <;> linarith

/-- Both signs are fixed by the strict endpoint comparisons; no rounding
at integer boundaries is allowed. -/
theorem neutralIV147Signed_floor (n : ℝ) (j : ℤ)
    (hn : 0 < n)
    (hl : Real.exp ((j:ℝ)/4096) < n)
    (hu : n < Real.exp (((j:ℝ)+1)/4096)) :
    Int.floor (Real.log n * 4096) = j ∧
      Int.floor (-Real.log n * 4096) = -j-1 := by
  obtain ⟨h₁,h₂⟩ := neutralIV147Log_endpoints n j hn hl hu
  constructor
  · apply Int.floor_eq_iff.mpr
    constructor <;> push_cast <;> linarith
  · apply Int.floor_eq_iff.mpr
    constructor <;> push_cast <;> linarith

/-- A rational lower bracket for sqrt(n) and a strict exponential
lower comparison imply the physical weight cap. The actual von Mangoldt
identity at each prime power must be supplied separately. -/
theorem neutralIV147Weight_cap (n p r u : ℝ)
    (hn : 0 < n) (hp : 0 < p) (hr : 0 ≤ r) (hu : 0 ≤ u)
    (hsq : r^2 ≤ n)
    (he : p < Real.exp (u*r)) :
    Real.log p / Real.sqrt n < u := by
  have hs := Real.sqrt_pos.2 hn
  have hs2 := Real.sq_sqrt hn.le
  have hroot : r ≤ Real.sqrt n := by
    by_contra! hbad
    have hpos := mul_pos (sub_pos.mpr hbad) (add_pos_of_nonneg_of_pos hr hs)
    nlinarith
  have hlog : Real.log p < u*r := by
    rw [← Real.exp_log hp] at he
    exact Real.exp_lt_exp.mp he
  apply (div_lt_iff₀ hs).2
  exact hlog.trans_le (mul_le_mul_of_nonneg_left hroot hu)

#print axioms neutralIV147Log_endpoints
#print axioms neutralIV147Signed_floor
#print axioms neutralIV147Weight_cap

end
end WeilDefect
