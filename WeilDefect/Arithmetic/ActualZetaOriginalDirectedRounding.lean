import WeilDefect.Arithmetic.ActualZetaOriginalRationalIntervalKernel

namespace WeilDefect
noncomputable section

/-! NF591: directed rounding at a positive integer scale.
The proof uses exact rational floor/ceil inequalities only. -/

def NF591Ball.round (a : NF591Ball) (Q : ℕ) : NF591Ball :=
  ⟨(⌊a.mid*Q⌋:ℚ)/Q,((⌈a.rad*Q⌉:ℚ)+1)/Q⟩

theorem NF591Ball.round_widens (a : NF591Ball) (Q : ℕ) (hQ : 0 < Q) :
    a.Widens (a.round Q) := by
  have hq : (0:ℚ)<Q := by exact_mod_cast hQ
  have hl := Int.floor_le (a.mid*(Q:ℚ))
  have hu := Int.lt_floor_add_one (a.mid*(Q:ℚ))
  have hr := Int.le_ceil (a.rad*(Q:ℚ))
  unfold Widens round
  dsimp
  have h0 : (⌊a.mid*(Q:ℚ)⌋:ℚ)/(Q:ℚ) ≤ a.mid := by
    apply (div_le_iff₀ hq).mpr
    exact hl
  rw [abs_of_nonneg (sub_nonneg.mpr h0)]
  apply (le_div_iff₀ hq).mpr
  have he : (⌊a.mid*(Q:ℚ)⌋:ℚ)/(Q:ℚ)*(Q:ℚ) =
      (⌊a.mid*(Q:ℚ)⌋:ℚ) := div_mul_cancel₀ _ hq.ne'
  rw [add_mul,sub_mul,he]
  linarith

theorem NF591Ball.contains_round {a : NF591Ball} {x : ℝ}
    (hx : a.Contains x) (Q : ℕ) (hQ : 0 < Q) :
    (a.round Q).Contains x :=
  contains_widen hx (round_widens a Q hQ)

theorem NF591Ball.contains_rounded_mul {a b : NF591Ball} {x y : ℝ}
    (hx : a.Contains x) (hy : b.Contains y) (Q : ℕ) (hQ : 0 < Q) :
    ((a.mul b).round Q).Contains (x*y) :=
  contains_round (contains_mul hx hy) Q hQ

theorem NF591Ball.contains_rounded_div {a : NF591Ball} {x : ℝ}
    (hx : a.Contains x) (d : ℚ) (hd : 0 < d) (Q : ℕ) (hQ : 0 < Q) :
    ((a.divPos d).round Q).Contains (x/(d:ℝ)) :=
  contains_round (contains_divPos hx hd) Q hQ

end
end WeilDefect
