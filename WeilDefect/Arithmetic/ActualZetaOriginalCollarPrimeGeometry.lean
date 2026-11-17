import WeilDefect.Arithmetic.ActualZetaOriginalCollar242Correction
import Mathlib.Analysis.Complex.ExponentialBounds

namespace WeilDefect
noncomputable section
open Set MeasureTheory
open scoped ENNReal

/-! NF600: exact support geometry, including all integers in
the actual prime sum. No prime-power enumeration is needed:
every integer n>=2 except 9 is excluded geometrically. -/

theorem neutralNF600Collars_measurable : MeasurableSet neutralNF543OriginalCollars := by
  unfold neutralNF543OriginalCollars
  exact measurableSet_Ioo.union measurableSet_Ioo

theorem neutralNF600Collars_volume :
    volume neutralNF543OriginalCollars = ENNReal.ofReal (1/250:ℝ) := by
  unfold neutralNF543OriginalCollars
  rw [measure_union (by
    rw [Set.disjoint_left]
    intro x hx hy
    linarith [hx.2,hy.1]) measurableSet_Ioo,Real.volume_Ioo,Real.volume_Ioo,
    ← ENNReal.ofReal_add (by norm_num) (by norm_num)]
  congr 1
  norm_num

theorem neutralNF600Collar_difference (x y : ℝ)
    (hx : x ∈ neutralNF543OriginalCollars) (hy : y ∈ neutralNF543OriginalCollars) :
    |y-x| < 1/500 ∨ (549/250:ℝ) < |y-x| ∧ |y-x| < 11/5 := by
  rcases hx with hx|hx <;> rcases hy with hy|hy
  · left
    exact abs_lt.mpr ⟨by linarith [hx.2,hy.1],by linarith [hx.1,hy.2]⟩
  · right
    rw [abs_of_pos (by linarith [hx.2,hy.1] : 0 < y-x)]
    exact ⟨by linarith [hx.2,hy.1],by linarith [hx.1,hy.2]⟩
  · right
    rw [abs_of_neg (by linarith [hx.1,hy.2] : y-x<0)]
    exact ⟨by linarith [hx.1,hy.2],by linarith [hx.2,hy.1]⟩
  · left
    exact abs_lt.mpr ⟨by linarith [hx.2,hy.1],by linarith [hx.1,hy.2]⟩

theorem neutralNF600Log8_upper : Real.log 8 < (549/250:ℝ) := by
  rw [show (8:ℝ)=2^3 by norm_num,Real.log_pow]
  linarith [Real.log_two_lt_d9]

theorem neutralNF600Log10_lower : (11/5:ℝ) < Real.log 10 := by
  have h0 : Real.exp 1 < 11/4 := Real.exp_one_lt_d9.trans (by norm_num)
  have h1 : Real.exp 11 < (10:ℝ)^5 := by
    rw [show (11:ℝ)=(11:ℕ)*1 by norm_num,Real.exp_nat_mul]
    exact (pow_lt_pow_left₀ h0 (Real.exp_pos 1).le (by decide : 11≠0)).trans (by norm_num)
  have h2 : Real.exp (11/5) < 10 := by
    by_contra! h
    have hp := pow_le_pow_left₀ (by norm_num : (0:ℝ)≤10) h 5
    rw [← Real.exp_nat_mul,show (5:ℝ)*(11/5)=11 by norm_num] at hp
    exact (not_le_of_gt h1) hp
  exact (Real.lt_log_iff_exp_lt (by norm_num)).mpr h2

theorem neutralNF600NoPrimeOverlap (n : ℕ) (hn : 2 ≤ n) (h9 : n ≠ 9)
    (x y : ℝ) (hx : x ∈ neutralNF543OriginalCollars)
    (hy : y ∈ neutralNF543OriginalCollars) :
    |y-x| ≠ Real.log n := by
  intro he
  have h2 : Real.log 2 ≤ Real.log (n:ℝ) :=
    Real.log_le_log (by norm_num) (by exact_mod_cast hn)
  rcases neutralNF600Collar_difference x y hx hy with hs|hs
  · rw [he] at hs
    linarith [Real.log_two_gt_d9]
  · rw [he] at hs
    by_cases h8 : n ≤ 8
    · have h := Real.log_le_log (by positivity : 0<(n:ℝ)) (by exact_mod_cast h8 : (n:ℝ)≤8)
      linarith [neutralNF600Log8_upper,hs.1]
    · have h10 : 10 ≤ n := by omega
      have h := Real.log_le_log (by norm_num : (0:ℝ)<10) (by exact_mod_cast h10 : (10:ℝ)≤n)
      linarith [neutralNF600Log10_lower,hs.2]

theorem neutralNF600Log9_cross (x y : ℝ)
    (hx : x ∈ neutralNF543OriginalCollars)
    (hy : y ∈ neutralNF543OriginalCollars)
    (h : y-x=Real.log 9) :
    x ∈ Ioo (-(11/10:ℝ)) (-(11/10:ℝ)+1/500) ∧
      y ∈ Ioo ((11/10:ℝ)-1/500) (11/10:ℝ) := by
  have hl : Real.log 2 ≤ Real.log 9 := Real.log_le_log (by norm_num) (by norm_num)
  have hp := Real.log_two_gt_d9
  rcases hx with hx|hx <;> rcases hy with hy|hy
  · exfalso
    linarith [hx.1,hy.2]
  · exact ⟨hx,hy⟩
  · exfalso
    linarith [hx.1,hy.2]
  · exfalso
    linarith [hx.1,hy.2]

end
end WeilDefect
