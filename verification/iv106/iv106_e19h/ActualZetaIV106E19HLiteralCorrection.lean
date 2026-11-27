import WeilDefect.Arithmetic.ActualZetaIV106E19HInfiniteCramer

namespace WeilDefect
noncomputable section
open Matrix Finset
open scoped BigOperators

def neutralIV106E19HPrevious (k : ℕ) (hk : 0 < k) (s : ℕ) : Fin k → ℝ :=
  fun i => (neutralIV106E18OEntry k hk i (s-1)).re

def neutralIV106E19HCoeff (k : ℕ) (hk : 0 < k) (s : ℕ) (j : Fin k) : ℝ :=
  let A := neutralIV106E19EShifted k hk s
  (A.updateCol j (neutralIV106E19HPrevious k hk s)).det/A.det

theorem neutralIV106E19HX_ge_one (n : ℕ) : 1 ≤ neutralIV106E18OX n := by
  unfold neutralIV106E18OX neutralIV106E18NRate neutralIV106E18LWidth
  rw [← Real.exp_zero]
  apply Real.exp_le_exp.mpr
  positivity

theorem neutralIV106E19HLiteral_bounds (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hs : neutralIV106E18LEligible s)
    (hel : ∀ j : Fin k, neutralIV106E18LEligible (s+j.val+1))
    (j : Fin k) :
    0 ≤ (-1:ℝ)^j.val*neutralIV106E19HCoeff k hk s j ∧
      (-1:ℝ)^j.val*neutralIV106E19HCoeff k hk s j ≤
        (Nat.choose k (j.val+1):ℝ) := by
  unfold neutralIV106E19HCoeff
  dsimp only
  apply neutralIV106E19HInfinite_bounds k (neutralIV106E19EWeight k hk s)
    neutralIV106E18OX (neutralIV106E18OY k)
  · intro n
    unfold neutralIV106E19EWeight
    apply mul_nonneg _ (pow_nonneg (Real.exp_pos _).le _)
    by_cases hn : n=0
    · rw [hn,neutralIV106E18OW_zero]
    · exact (neutralIV106E18OW_pos k hk n (Nat.pos_of_ne_zero hn)).le
  · intro n hn
    exact mul_pos (neutralIV106E18OW_pos k hk n hn) (pow_pos (Real.exp_pos _) _)
  · exact neutralIV106E18OX_strict
  · exact neutralIV106E18OY_strict k hk
  · exact neutralIV106E19HX_ge_one
  · exact neutralIV106E19EShifted_series k hk s hel
  · intro i
    exact neutralIV106E19EPrevious_series k hk s (by have h := hs.1; omega) hs i

theorem neutralIV106E19HLiteral_solve (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hel : ∀ j : Fin k, neutralIV106E18LEligible (s+j.val+1)) :
    neutralIV106E19EShifted k hk s *ᵥ neutralIV106E19HCoeff k hk s =
      neutralIV106E19HPrevious k hk s := by
  have hd := neutralIV106E19EShifted_det k hk s hel
  have hn : (neutralIV106E19EShifted k hk s).det ≠ 0 := by
    intro hz
    rw [hz,mul_zero] at hd
    exact (lt_irrefl 0) hd
  exact neutralIV106E19HSolve _ _ hn

/-- The real part is not a surrogate: each literal eligible IV105C entry
is the complex coercion of its real part, by its positive series. -/
theorem neutralIV106E19HEntry_real (k : ℕ) (hk : 0 < k) (i : Fin k)
    (j : ℕ) (hj : neutralIV106E18LEligible (j+1)) :
    neutralIV106E18OEntry k hk i j =
      ((neutralIV106E18OEntry k hk i j).re:ℂ) := by
  have h := neutralIV106E18OEntry_series k hk i j hj
  have hr := Complex.hasSum_re h
  have hc := Complex.hasSum_ofReal.mpr (show HasSum
    (fun n : ℕ => neutralIV106E18OW k hk n*
      neutralIV106E18OY k n^i.val*neutralIV106E18OX n^j)
    (neutralIV106E18OEntry k hk i j).re by simpa using hr)
  apply h.unique
  simpa only [Complex.ofReal_mul,Complex.ofReal_pow] using hc

/-- Exact cancellation in the original complex response coordinates.
This is the receiving identity needed for E19C kernel correction. -/
theorem neutralIV106E19HLiteral_response (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hs : neutralIV106E18LEligible s)
    (hel : ∀ j : Fin k, neutralIV106E18LEligible (s+j.val+1))
    (i : Fin k) :
    neutralIV106E18OEntry k hk i (s-1) =
      ∑ j, (neutralIV106E19HCoeff k hk s j:ℂ) *
        neutralIV106E18OEntry k hk i (s+j.val) := by
  have h := congrFun (neutralIV106E19HLiteral_solve k hk s hel) i
  change (∑ j, (neutralIV106E18OEntry k hk i (s+j.val)).re *
    neutralIV106E19HCoeff k hk s j) =
    (neutralIV106E18OEntry k hk i (s-1)).re at h
  have hs' : s-1+1=s := by have hh := hs.1; omega
  rw [neutralIV106E19HEntry_real k hk i (s-1) (by rwa [hs'])]
  calc
    _ = ((∑ j, (neutralIV106E18OEntry k hk i (s+j.val)).re *
        neutralIV106E19HCoeff k hk s j : ℝ):ℂ) := by rw [h]
    _ = _ := by
      push_cast
      apply Finset.sum_congr rfl
      intro j hj
      rw [neutralIV106E19HEntry_real k hk i (s+j.val) (hel j)]
      ring

#print axioms neutralIV106E19HX_ge_one
#print axioms neutralIV106E19HLiteral_bounds
#print axioms neutralIV106E19HLiteral_solve
#print axioms neutralIV106E19HEntry_real
#print axioms neutralIV106E19HLiteral_response
end
end WeilDefect
