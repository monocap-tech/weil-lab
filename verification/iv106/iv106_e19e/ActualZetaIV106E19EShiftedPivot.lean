import WeilDefect.Arithmetic.ActualZetaIV106E18QLiteralRank

namespace WeilDefect
noncomputable section
open Filter
open scoped Topology BigOperators

/-- The pivot after cell s has columns at actual cells s+1,...,s+k. -/
def neutralIV106E19EShifted (k : ℕ) (hk : 0 < k) (s : ℕ) :
    Matrix (Fin k) (Fin k) ℝ :=
  fun i j => (neutralIV106E18OEntry k hk i (s+j.val)).re

def neutralIV106E19EWeight (k : ℕ) (hk : 0 < k) (s n : ℕ) : ℝ :=
  neutralIV106E18OW k hk n * neutralIV106E18OX n ^ s

/-- The shifted literal matrix has exactly the same positive moment
representation as the original pivot, with a new positive weight. -/
theorem neutralIV106E19EShifted_series (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hel : ∀ j : Fin k, neutralIV106E18LEligible (s+j.val+1))
    (i j : Fin k) :
    HasSum (fun n : ℕ => neutralIV106E19EWeight k hk s n *
      neutralIV106E18OY k n ^ i.val * neutralIV106E18OX n ^ j.val)
      (neutralIV106E19EShifted k hk s i j) := by
  have hs := Complex.hasSum_re (neutralIV106E18OEntry_series k hk i
    (s+j.val) (hel j))
  simpa [neutralIV106E19EShifted,neutralIV106E19EWeight,pow_add,
    mul_assoc,mul_left_comm,mul_comm] using hs

theorem neutralIV106E19EShifted_det (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hel : ∀ j : Fin k, neutralIV106E18LEligible (s+j.val+1)) :
    0 < neutralIV106E18POrient k*(neutralIV106E19EShifted k hk s).det := by
  have hx (n : ℕ) : 0 < neutralIV106E18OX n := Real.exp_pos _
  apply neutralIV106E18PInfinite k (neutralIV106E19EWeight k hk s)
    neutralIV106E18OX (neutralIV106E18OY k)
  · intro n
    unfold neutralIV106E19EWeight
    apply mul_nonneg _ (pow_nonneg (hx n).le _)
    by_cases hn : n = 0
    · rw [hn,neutralIV106E18OW_zero]
    · exact (neutralIV106E18OW_pos k hk n (Nat.pos_of_ne_zero hn)).le
  · intro n hn
    exact mul_pos (neutralIV106E18OW_pos k hk n hn) (pow_pos (hx n) _)
  · exact neutralIV106E18OX_strict
  · exact neutralIV106E18OY_strict k hk
  · exact neutralIV106E19EShifted_series k hk s hel

/-- The preceding cell has exponent -1 relative to the shifted pivot. -/
theorem neutralIV106E19EPrevious_series (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hs : 0 < s) (hel : neutralIV106E18LEligible s) (i : Fin k) :
    HasSum (fun n : ℕ => neutralIV106E19EWeight k hk s n *
      neutralIV106E18OY k n ^ i.val / neutralIV106E18OX n)
      (neutralIV106E18OEntry k hk i (s-1)).re := by
  have hs' : s-1+1=s := by omega
  have he : neutralIV106E18LEligible (s-1+1) := by rwa [hs']
  have hsum := Complex.hasSum_re (neutralIV106E18OEntry_series k hk i (s-1) he)
  have hfun : (fun n : ℕ => neutralIV106E19EWeight k hk s n *
      neutralIV106E18OY k n ^ i.val / neutralIV106E18OX n) =
      (fun n : ℕ => neutralIV106E18OW k hk n *
        neutralIV106E18OY k n ^ i.val * neutralIV106E18OX n ^ (s-1)) := by
    funext n
    have hn : neutralIV106E18OX n ≠ 0 := (Real.exp_pos _).ne'
    unfold neutralIV106E19EWeight
    have hp : neutralIV106E18OX n ^ s =
        neutralIV106E18OX n ^ (s-1)*neutralIV106E18OX n := by
      rw [← pow_succ,hs']
    rw [hp]
    field_simp [hn] <;> ring
  rw [hfun]
  simpa using hsum

/-- A nonnegative tuple expansion transports a bounded signed Cramer
coefficient without estimating the determinant away from zero numerically. -/
theorem neutralIV106E19EWeighted {I : Type*} [Fintype I]
    (w a : I → ℝ) (B : ℝ)
    (hw : ∀ i, 0 ≤ w i) (ha : ∀ i, 0 ≤ a i ∧ a i ≤ B) :
    0 ≤ (∑ i, w i*a i) ∧
      (∑ i, w i*a i) ≤ B*(∑ i, w i) := by
  constructor
  · exact Finset.sum_nonneg fun i _ => mul_nonneg (hw i) (ha i).1
  · rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i hi
    rw [mul_comm B (w i)]
    exact mul_le_mul_of_nonneg_left (ha i).2 (hw i)

/-- Retain the signed coefficient enclosure through an infinite limit
of oriented numerator and denominator, assuming the tuple bounds.
The true denominator is positive by the shifted E18P theorem. -/
theorem neutralIV106E19ERatio_limit
    (D C : ℕ → ℝ) (d c B : ℝ)
    (hd : Tendsto D atTop (𝓝 d)) (hc : Tendsto C atTop (𝓝 c))
    (hdpos : 0 < d)
    (h : ∀ᶠ n in atTop, 0 ≤ C n ∧ C n ≤ B*D n) :
    0 ≤ c/d ∧ c/d ≤ B := by
  have hc0 : 0 ≤ c := ge_of_tendsto hc (h.mono fun n hn => hn.1)
  have hs : c-B*d ≤ 0 := le_of_tendsto
    (hc.sub (tendsto_const_nhds.mul hd))
    (h.mono fun n hn => sub_nonpos.mpr hn.2)
  exact ⟨div_nonneg hc0 hdpos.le,(div_le_iff₀ hdpos).mpr (sub_nonpos.mp hs)⟩

#print axioms neutralIV106E19EShifted_series
#print axioms neutralIV106E19EShifted_det
#print axioms neutralIV106E19EPrevious_series
#print axioms neutralIV106E19EWeighted
#print axioms neutralIV106E19ERatio_limit
end
end WeilDefect
