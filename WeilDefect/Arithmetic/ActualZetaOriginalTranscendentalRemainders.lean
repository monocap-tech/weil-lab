import Mathlib

namespace WeilDefect
noncomputable section
open Finset MeasureTheory Set
open scoped Interval

/-! NF591: analytic error bounds for the exact integer-only phase
and pole evaluation. Neither theorem is an axiom about external
interval software. -/

theorem neutralNF591FactorialTail (N : ℕ) (hN : 1 ≤ N) (n : ℕ) :
    (N.factorial:ℝ)*2^n ≤ ((n+N).factorial:ℝ) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have he : n+1+N = n+N+1 := by omega
    rw [he,Nat.factorial_succ,Nat.cast_mul,pow_succ]
    have h2 : (2:ℝ) ≤ (n+N+1:ℕ) := by exact_mod_cast (show 2 ≤ n+N+1 by omega)
    calc
      (N.factorial:ℝ)*(2^n*2) = 2*((N.factorial:ℝ)*2^n) := by ring
      _ ≤ 2*((n+N).factorial:ℝ) := mul_le_mul_of_nonneg_left ih (by norm_num)
      _ ≤ ((n+N+1:ℕ):ℝ)*((n+N).factorial:ℝ) :=
        mul_le_mul_of_nonneg_right h2 (Nat.cast_nonneg _)

theorem neutralNF591SmallExp_tail (z : ℂ) (hz : ‖z‖ ≤ 1)
    (N : ℕ) (hN : 1 ≤ N) :
    ‖Complex.exp z-∑ n ∈ range N, z^n/(n.factorial:ℂ)‖ ≤ 2/(N.factorial:ℝ) := by
  let f := fun n : ℕ => z^n/(n.factorial:ℂ)
  have hf : HasSum f (Complex.exp z) := by
    simpa only [f,Complex.exp_eq_exp_ℂ] using NormedSpace.expSeries_div_hasSum_exp z
  have hs := hf.summable.sum_add_tsum_nat_add N
  rw [hf.tsum_eq] at hs
  have he : Complex.exp z-(∑ n ∈ range N, f n) = ∑' n : ℕ, f (n+N) := by
    rw [← hs]
    ring
  change ‖Complex.exp z-∑ n ∈ range N, f n‖ ≤ _
  rw [he]
  have hg := (hasSum_geometric_of_lt_one (show (0:ℝ)≤1/2 by norm_num)
    (show (1/2:ℝ)<1 by norm_num)).mul_left ((N.factorial:ℝ)⁻¹)
  have hb := tsum_of_norm_bounded hg (f := fun n => f (n+N)) (fun n => by
    have hfact := neutralNF591FactorialTail N hN n
    have h0 : 0 < (N.factorial:ℝ)*2^n := by positivity
    have h1 : 0 < ((n+N).factorial:ℝ) := by positivity
    have hp : ‖z‖^(n+N) ≤ 1 := pow_le_one₀ (norm_nonneg _) hz
    change ‖z^(n+N)/((n+N).factorial:ℂ)‖ ≤ _
    rw [norm_div,norm_pow,Complex.norm_natCast]
    calc
      _ ≤ 1/((n+N).factorial:ℝ) := div_le_div_of_nonneg_right hp h1.le
      _ ≤ 1/((N.factorial:ℝ)*2^n) := one_div_le_one_div_of_le h0 hfact
      _ = _ := by rw [one_div,mul_inv_rev,← inv_pow]; norm_num; ring)
  convert hb using 1 <;> norm_num <;> ring

def neutralNF591AtanPoly (N : ℕ) (x : ℝ) : ℝ :=
  ∑ n ∈ range N, (-1:ℝ)^n*x^(2*n+1)/(2*n+1:ℝ)

theorem neutralNF591AtanGeometric (t : ℝ) (N : ℕ) :
    (1+t^2)⁻¹ = (∑ n ∈ range N, (-1:ℝ)^n*t^(2*n))+
      (-1:ℝ)^N*t^(2*N)/(1+t^2) := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [sum_range_succ, show (-1:ℝ)^(N+1)=(-1)^N*(-1) by rw [pow_succ],
      show 2*(N+1)=2*N+2 by omega,pow_add]
    calc
      _ = (∑ n ∈ range N, (-1:ℝ)^n*t^(2*n))+
          (-1:ℝ)^N*t^(2*N)/(1+t^2) := ih
      _ = _ := by
        have hh : (1+t^2:ℝ) ≠ 0 := by positivity
        field_simp
        ring

/-- Integrate the finite geometric identity, paying the entire
remainder through its absolute value. This is a non-asymptotic
bound for every N and every nonnegative real argument. -/
theorem neutralNF591Atan_tail (x : ℝ) (hx : 0 ≤ x) (N : ℕ) :
    |Real.arctan x-neutralNF591AtanPoly N x| ≤ x^(2*N+1)/(2*N+1:ℝ) := by
  let p : ℝ → ℝ := fun t => ∑ n ∈ range N, (-1:ℝ)^n*t^(2*n)
  let r : ℝ → ℝ := fun t => (-1:ℝ)^N*t^(2*N)/(1+t^2)
  have hp : Continuous p := by
    unfold p
    fun_prop
  have hr : Continuous r := by
    unfold r
    exact (by fun_prop : Continuous (fun t : ℝ => (-1:ℝ)^N*t^(2*N))).div
      (by fun_prop) (fun t => by positivity)
  have hi : (∫ t in (0:ℝ)..x, p t) = neutralNF591AtanPoly N x := by
    unfold p neutralNF591AtanPoly
    rw [intervalIntegral.integral_finsetSum (fun n _ =>
      (by fun_prop : Continuous (fun t : ℝ => (-1:ℝ)^n*t^(2*n))).intervalIntegrable 0 x)]
    apply sum_congr rfl
    intro n _
    rw [intervalIntegral.integral_const_mul,integral_pow]
    have hn : 2*n+1 ≠ 0 := by omega
    simp [zero_pow hn]
    push_cast
    ring
  have h := calc
    Real.arctan x = ∫ t in (0:ℝ)..x, (1+t^2)⁻¹ := by
      rw [integral_inv_one_add_sq,Real.arctan_zero,sub_zero]
    _ = ∫ t in (0:ℝ)..x, p t+r t := by
      apply intervalIntegral.integral_congr
      intro t _
      exact neutralNF591AtanGeometric t N
    _ = neutralNF591AtanPoly N x + ∫ t in (0:ℝ)..x, r t := by
      rw [intervalIntegral.integral_add (hp.intervalIntegrable 0 x)
        (hr.intervalIntegrable 0 x),hi]
  rw [h,add_sub_cancel_left,← Real.norm_eq_abs]
  calc
    _ ≤ ∫ t in (0:ℝ)..x, t^(2*N) := by
      apply intervalIntegral.norm_integral_le_of_norm_le hx ?_
        ((by fun_prop : Continuous (fun t : ℝ => t^(2*N))).intervalIntegrable 0 x)
      filter_upwards [] with t ht
      have ht0 : 0 ≤ t := ht.1.le
      unfold r
      rw [Real.norm_eq_abs,abs_div,abs_mul,abs_pow,abs_neg,abs_one,one_pow,one_mul,
        abs_of_nonneg (pow_nonneg ht0 _),abs_of_pos (by positivity : 0<1+t^2)]
      exact div_le_self (pow_nonneg ht0 _) (by nlinarith [sq_nonneg t])
    _ = _ := by rw [integral_pow]; push_cast; simp

theorem neutralNF591Machin_approx (N : ℕ) :
    |Real.pi-(16*neutralNF591AtanPoly N (1/5)-
      4*neutralNF591AtanPoly N (1/239))| ≤
      16*(1/5:ℝ)^(2*N+1)/(2*N+1:ℝ)+
      4*(1/239:ℝ)^(2*N+1)/(2*N+1:ℝ) := by
  have h := Real.four_mul_arctan_inv_5_sub_arctan_inv_239
  have hπ : Real.pi = 16*Real.arctan (1/5)-4*Real.arctan (1/239) := by
    simp only [one_div] at *
    linarith
  rw [hπ,show 16*Real.arctan (1/5)-4*Real.arctan (1/239)-
    (16*neutralNF591AtanPoly N (1/5)-4*neutralNF591AtanPoly N (1/239)) =
      16*(Real.arctan (1/5)-neutralNF591AtanPoly N (1/5))+
      (-4)*(Real.arctan (1/239)-neutralNF591AtanPoly N (1/239)) by ring]
  apply (abs_add_le _ _).trans
  rw [abs_mul,abs_mul]
  norm_num only [abs_of_nonneg (by norm_num : (0:ℝ)≤16),abs_neg,abs_of_nonneg (by norm_num : (0:ℝ)≤4)]
  have h1 := neutralNF591Atan_tail (1/5) (by norm_num) N
  have h2 := neutralNF591Atan_tail (1/239) (by norm_num) N
  rw [mul_div_assoc,mul_div_assoc]
  exact add_le_add (mul_le_mul_of_nonneg_left h1 (by norm_num))
    (mul_le_mul_of_nonneg_left h2 (by norm_num))

end
end WeilDefect
