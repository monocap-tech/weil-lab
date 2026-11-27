import Mathlib.Analysis.Complex.Exponential
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

/-! V10B36b: a finite Taylor enclosure independent of termwise infinite
integration. The uniform remainder is transported through any continuous
nonnegative weight on [0,1]. -/
namespace WeilDefect.MasterRecon.V10B36b
open MeasureTheory Set
open scoped BigOperators

noncomputable def taylor (n : ℕ) (x : ℝ) : ℝ :=
  ∑ m ∈ Finset.range n, x^m/(m.factorial:ℝ)

noncomputable def reserve (n : ℕ) : ℝ :=
  (1/8:ℝ)^n*((n.succ:ℝ)/((n.factorial:ℝ)*(n:ℝ)))

theorem centered_taylor (n : ℕ) (hn : 0<n) (x : ℝ) (hx : x ∈ Icc (0:ℝ) 1) :
    |Real.exp ((2*x-1)/8)-taylor n ((2*x-1)/8)| ≤ reserve n := by
  have h : |(2*x-1)/8| ≤ (1/8:ℝ) := abs_le.mpr ⟨by linarith [hx.1],by linarith [hx.2]⟩
  have ht := Real.exp_bound (x := (2*x-1)/8) (h.trans (by norm_num)) hn
  unfold taylor reserve
  exact ht.trans (mul_le_mul_of_nonneg_right
    (pow_le_pow_left₀ (abs_nonneg _) h _) (by positivity))

theorem weighted_taylor (n : ℕ) (hn : 0<n) (w : ℝ → ℝ) (hc : Continuous w)
    (hw : ∀ x ∈ Icc (0:ℝ) 1, 0 ≤ w x) :
    |(∫ x in (0:ℝ)..1, Real.exp ((2*x-1)/8)*w x) -
      (∫ x in (0:ℝ)..1, taylor n ((2*x-1)/8)*w x)| ≤
      reserve n*(∫ x in (0:ℝ)..1, w x) := by
  have ht : Continuous (fun x : ℝ => taylor n ((2*x-1)/8)) := by
    unfold taylor
    fun_prop
  have h1 : Continuous (fun x : ℝ => Real.exp ((2*x-1)/8)*w x) := by fun_prop
  have h2 : Continuous (fun x : ℝ => taylor n ((2*x-1)/8)*w x) := ht.mul hc
  have hd := h1.sub h2
  have hr : Continuous (fun x => reserve n*w x) := continuous_const.mul hc
  rw [← intervalIntegral.integral_sub (h1.intervalIntegrable 0 1)
    (h2.intervalIntegrable 0 1)]
  calc
    _ ≤ ∫ x in (0:ℝ)..1, |Real.exp ((2*x-1)/8)*w x-taylor n ((2*x-1)/8)*w x| :=
      intervalIntegral.abs_integral_le_integral_abs (by norm_num)
    _ ≤ ∫ x in (0:ℝ)..1, reserve n*w x := by
      apply intervalIntegral.integral_mono_on (by norm_num)
        (hd.abs.intervalIntegrable 0 1) (hr.intervalIntegrable 0 1)
      intro x hx
      change |Real.exp ((2*x-1)/8)*w x-taylor n ((2*x-1)/8)*w x| ≤ reserve n*w x
      rw [← sub_mul,abs_mul,abs_of_nonneg (hw x hx)]
      exact mul_le_mul_of_nonneg_right (centered_taylor n hn x hx) (hw x hx)
    _ = _ := intervalIntegral.integral_const_mul _ _

theorem frozen_reserve_32 : reserve 32 < 1/(10:ℝ)^64 := by
  norm_num [reserve, Nat.factorial]

theorem frozen_reserve_34 : reserve 34 < 1/(10:ℝ)^69 := by
  norm_num [reserve, Nat.factorial]

end WeilDefect.MasterRecon.V10B36b

#print axioms WeilDefect.MasterRecon.V10B36b.centered_taylor
#print axioms WeilDefect.MasterRecon.V10B36b.weighted_taylor
#print axioms WeilDefect.MasterRecon.V10B36b.frozen_reserve_32
#print axioms WeilDefect.MasterRecon.V10B36b.frozen_reserve_34
