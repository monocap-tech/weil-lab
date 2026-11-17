import Mathlib

namespace WeilDefect
noncomputable section
open Finset

/-! NF588: exact normalized Taylor head/tail transfer.
The analytic identities (including the differentiated sum) and the
first 400 coefficient enclosures are explicit premises. The infinite
tail is paid once, from the same coefficient sequence, not from a
distinct polynomial fit. -/

theorem neutralNF588HasSum_head_tail {v : ℕ → ℝ} {V : ℝ}
    (hv : HasSum v V) (N : ℕ) (b : ℕ → ℝ) (T : ℝ)
    (hb : ∀ n < N, ‖v n‖ ≤ b n)
    (ht : ‖∑' n : ℕ, v (n+N)‖ ≤ T) :
    ‖V‖ ≤ (∑ n ∈ range N, b n)+T := by
  have hs := hv.summable.sum_add_tsum_nat_add N
  rw [hv.tsum_eq] at hs
  rw [← hs]
  apply (norm_add_le _ _).trans
  apply add_le_add _ ht
  exact (norm_sum_le _ _).trans (sum_le_sum fun n hn => hb n (mem_range.mp hn))

/-- The same proof handles any radius q < 1 and any cutoff. -/
theorem neutralNF588GeometricTail
    (v : ℕ → ℝ) (M q : ℝ) (N : ℕ)
    (hq : 0 ≤ q) (hq' : q < 1)
    (hv : ∀ n, ‖v n‖ ≤ M*q^n) :
    ‖∑' n : ℕ, v (n+N)‖ ≤ M*q^N/(1-q) := by
  have hg := (hasSum_geometric_of_lt_one hq hq').mul_left (M*q^N)
  have h := tsum_of_norm_bounded hg (f := fun n => v (n+N)) (fun n => by
    calc
      ‖v (n+N)‖ ≤ M*q^(n+N) := hv _
      _ = (M*q^N)*q^n := by rw [pow_add]; ring)
  simpa only [div_eq_mul_inv] using h

/-- Exact weighted tail majorant: differentiation shifts degree
but does not create a separate choice of coefficient uncertainty. -/
theorem neutralNF588WeightedGeometricTail
    (v : ℕ → ℝ) (M q : ℝ) (N : ℕ)
    (hq : 0 ≤ q) (hq' : q < 1)
    (hv : ∀ n, ‖v (n+N)‖ ≤ (M*q^N)*((n:ℝ)+N)*q^n) :
    ‖∑' n : ℕ, v (n+N)‖ ≤
      (M*q^N)*((N:ℝ)/(1-q)+q/(1-q)^2) := by
  have hqnorm : ‖q‖ < 1 := by rw [Real.norm_eq_abs,abs_of_nonneg hq]; exact hq'
  have hG := (hasSum_geometric_of_lt_one hq hq').mul_left (N:ℝ)
  have hW := hasSum_coe_mul_geometric_of_norm_lt_one hqnorm
  have h := (hW.add hG).mul_left (M*q^N)
  have he : ∀ n : ℕ,
      ‖v (n+N)‖ ≤ (M*q^N)*((n:ℝ)*q^n+(N:ℝ)*q^n) := by
    intro n
    calc
      _ ≤ (M*q^N)*((n:ℝ)+N)*q^n := hv n
      _ = _ := by ring
  have hb := tsum_of_norm_bounded h (f := fun n => v (n+N)) he
  convert hb using 1 <;> ring

def neutralNF588ValueTail : ℝ :=
  (10:ℝ)^400*(1/20:ℝ)^400/(1-1/20)

def neutralNF588ScaledDerivativeTail : ℝ :=
  (10:ℝ)^400*(1/20:ℝ)^400*
    (400/(1-1/20)+(1/20)/(1-1/20)^2)

def neutralNF588DerivativeTail : ℝ :=
  500*neutralNF588ScaledDerivativeTail

/-- Exact rational overcharges (only used to simplify the finite
arithmetic receipt, never in place of the first 400 coefficients). -/
theorem neutralNF588Tail_budget :
    neutralNF588ValueTail < (10:ℝ)^(-120:ℤ) ∧
      neutralNF588DerivativeTail < (10:ℝ)^(-115:ℤ) := by
  unfold neutralNF588ValueTail neutralNF588DerivativeTail neutralNF588ScaledDerivativeTail
  constructor <;> norm_num1 <;> norm_num [← mul_pow]

/-- Normalized Taylor terms and the simultaneously differentiated
terms represent the SAME source.  The derivative is in the d
coordinate (not the normalized w coordinate), and has the minus
sign of x=B-d. -/
theorem neutralNF588OriginalNormalizedSeries_bounds
    (U U' : ℝ → ℝ) (v : ℕ → ℝ) (b : ℕ → ℝ)
    (hv : ∀ n, ‖v n‖ ≤ (10:ℝ)^400*(1/20:ℝ)^n)
    (hb : ∀ n < 400, ‖v n‖ ≤ b n)
    (hval : ∀ w ∈ Set.Icc (0:ℝ) 1,
      HasSum (fun n : ℕ => v n*w^n) (U (11/10-w/500)))
    (hder : ∀ w ∈ Set.Icc (0:ℝ) 1,
      HasSum (fun n : ℕ => (n:ℝ)*v n*w^(n-1))
        (-(U' (11/10-w/500))/500))
    (hbudget0 : (∑ n ∈ range 400, b n)+neutralNF588ValueTail ≤ 2/10^7)
    (hbudget1 : 500*(∑ n ∈ range 400, (n:ℝ)*b n)+neutralNF588DerivativeTail ≤ 7/10^4) :
    (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |U x| ≤ 2/10^7) ∧
      (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |U' x| ≤ 7/10^4) := by
  have hw (x : ℝ) (hx : x ∈ Set.Icc (549/500:ℝ) (11/10)) :
      500*(11/10-x) ∈ Set.Icc (0:ℝ) 1 :=
    ⟨by linarith [hx.2],by linarith [hx.1]⟩
  have hx' (x : ℝ) : (11/10:ℝ)-(500*(11/10-x))/500 = x := by ring
  have hp (w : ℝ) (hw : w ∈ Set.Icc (0:ℝ) 1) (n : ℕ) : ‖w^n‖ ≤ 1 := by
    rw [Real.norm_eq_abs, abs_of_nonneg (pow_nonneg hw.1 _)]
    exact pow_le_one₀ hw.1 hw.2
  constructor
  · intro x hx
    let w := 500*(11/10-x)
    have hw' : w ∈ Set.Icc (0:ℝ) 1 := hw x hx
    have h := hval w hw'
    have he : (11/10:ℝ)-w/500 = x := hx' x
    rw [he] at h
    have htail : ‖∑' n : ℕ, v (n+400)*w^(n+400)‖ ≤ neutralNF588ValueTail := by
      apply neutralNF588GeometricTail (fun k : ℕ => v k*w^k) ((10:ℝ)^400) (1/20) 400 (by norm_num) (by norm_num)
      intro n
      rw [norm_mul]
      exact (mul_le_mul_of_nonneg_left (hp w hw' n) (norm_nonneg _)).trans
        (by simpa only [mul_one] using hv n)
    have hf : ∀ n < 400, ‖v n*w^n‖ ≤ b n := by
      intro n hn
      rw [norm_mul]
      exact (mul_le_mul_of_nonneg_left (hp w hw' n) (norm_nonneg _)).trans
        (by simpa only [mul_one] using hb n hn)
    exact (Real.norm_eq_abs (U x)) ▸ ((neutralNF588HasSum_head_tail h 400 b _
      hf htail).trans hbudget0)
  · intro x hx
    let w := 500*(11/10-x)
    have hw' : w ∈ Set.Icc (0:ℝ) 1 := hw x hx
    have h := hder w hw'
    have he : (11/10:ℝ)-w/500 = x := hx' x
    rw [he] at h
    have htail : ‖∑' n : ℕ, ((n+400:ℕ):ℝ)*v (n+400)*w^(n+400-1)‖ ≤
        neutralNF588ScaledDerivativeTail := by
      apply neutralNF588WeightedGeometricTail (fun k : ℕ => (k:ℝ)*v k*w^(k-1)) ((10:ℝ)^400) (1/20) 400
        (by norm_num) (by norm_num)
      intro n
      rw [norm_mul,norm_mul,Real.norm_eq_abs,abs_of_nonneg (Nat.cast_nonneg _)]
      calc
        _ ≤ ((n+400:ℕ):ℝ)*‖v (n+400)‖ := by
          simpa only [mul_one] using mul_le_mul_of_nonneg_left (hp w hw' _) (by positivity :
            0 ≤ ((n+400:ℕ):ℝ)*‖v (n+400)‖)
        _ ≤ ((n+400:ℕ):ℝ)*((10:ℝ)^400*(1/20:ℝ)^(n+400)) :=
          mul_le_mul_of_nonneg_left (hv _) (Nat.cast_nonneg _)
        _ = _ := by push_cast; rw [pow_add]; ring
    have hf : ∀ n : ℕ, n < 400 → ‖(n:ℝ)*v n*w^(n-1)‖ ≤ (n:ℝ)*b n := by
      intro n hn
      rw [norm_mul,norm_mul,Real.norm_eq_abs,abs_of_nonneg (Nat.cast_nonneg _)]
      calc
        _ ≤ (n:ℝ)*‖v n‖ := by
          simpa only [mul_one] using mul_le_mul_of_nonneg_left (hp w hw' _) (by positivity :
            0 ≤ (n:ℝ)*‖v n‖)
        _ ≤ _ := mul_le_mul_of_nonneg_left (hb n hn) (Nat.cast_nonneg _)
    have hh := neutralNF588HasSum_head_tail h 400 (fun n => (n:ℝ)*b n)
      neutralNF588ScaledDerivativeTail hf htail
    rw [Real.norm_eq_abs,abs_div,abs_neg,show |(500:ℝ)| = 500 by norm_num] at hh
    have hh' := (div_le_iff₀ (by norm_num : (0:ℝ)<500)).mp hh
    unfold neutralNF588DerivativeTail at hbudget1
    linarith

end
end WeilDefect
