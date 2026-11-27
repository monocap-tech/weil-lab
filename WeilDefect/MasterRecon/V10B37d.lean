import WeilDefect.MasterRecon.V10B37a
import WeilDefect.MasterRecon.V10B36b

/-! V10B37d: finite Taylor coefficient attachment using centered
parity and the universal factorial formula. No infinite interchange. -/
namespace WeilDefect.MasterRecon.V10B37d
open MeasureTheory Set
open scoped BigOperators
open WeilDefect.MasterRecon.V10B36a
open WeilDefect.MasterRecon.V10B36b
open WeilDefect.MasterRecon.V10B37a

noncomputable def momentSum (j n : ℕ) : ℝ :=
  ∑ m ∈ Finset.range n, F j m/((8:ℝ)^(2*m)*((2*m).factorial:ℝ))

theorem term_integral (j r : ℕ) :
    (∫ x in (0:ℝ)..1, ((2*x-1)/8)^r/(r.factorial:ℝ)*w x^j) =
      (1/((8:ℝ)^r*(r.factorial:ℝ)))*
        (∫ x in (0:ℝ)..1, y x^r*w x^j) := by
  rw [← intervalIntegral.integral_const_mul]
  apply intervalIntegral.integral_congr
  intro x _
  unfold y
  rw [div_pow]
  ring

theorem taylor_pair (n : ℕ) (u : ℝ) :
    taylor (2*(n+1)) u = taylor (2*n) u +
      u^(2*n)/((2*n).factorial:ℝ)+u^(2*n+1)/((2*n+1).factorial:ℝ) := by
  unfold taylor
  rw [show 2*(n+1)=2*n+1+1 by omega,Finset.sum_range_succ,Finset.sum_range_succ]

theorem weighted_finite_identity (j n : ℕ) :
    (∫ x in (0:ℝ)..1, taylor (2*n) ((2*x-1)/8)*w x^j) = momentSum j n := by
  induction n with
  | zero => simp [taylor,momentSum]
  | succ n ih =>
    have h : (fun x : ℝ => taylor (2*(n+1)) ((2*x-1)/8)*w x^j) =
      fun x => (taylor (2*n) ((2*x-1)/8)*w x^j+
        ((2*x-1)/8)^(2*n)/((2*n).factorial:ℝ)*w x^j)+
        ((2*x-1)/8)^(2*n+1)/((2*n+1).factorial:ℝ)*w x^j := by
      funext x
      rw [taylor_pair]
      ring
    have h₀ : Continuous (fun x : ℝ => taylor (2*n) ((2*x-1)/8)*w x^j) := by
      unfold taylor w
      fun_prop
    have h₁ : Continuous (fun x : ℝ => ((2*x-1)/8)^(2*n)/((2*n).factorial:ℝ)*w x^j) := by
      unfold w
      fun_prop
    have h₂ : Continuous (fun x : ℝ => ((2*x-1)/8)^(2*n+1)/((2*n+1).factorial:ℝ)*w x^j) := by
      unfold w
      fun_prop
    rw [h,intervalIntegral.integral_add ((h₀.add h₁).intervalIntegrable 0 1)
      (h₂.intervalIntegrable 0 1),intervalIntegral.integral_add
      (h₀.intervalIntegrable 0 1) (h₁.intervalIntegrable 0 1),
      ih,term_integral,term_integral,odd_vanish,mul_zero,add_zero]
    change momentSum j n+1/((8:ℝ)^(2*n)*((2*n).factorial:ℝ))*B j n =
      momentSum j (n+1)
    rw [B_closed]
    unfold momentSum
    rw [Finset.sum_range_succ]
    ring

theorem weighted_literal_enclosure (j n : ℕ) (hn : 0<n) :
    |(∫ x in (0:ℝ)..1, Real.exp ((2*x-1)/8)*w x^j)-momentSum j n| ≤
      reserve (2*n)*F j 0 := by
  have hc : Continuous (fun x : ℝ => w x^j) := by unfold w; fun_prop
  have hw : ∀ x ∈ Icc (0:ℝ) 1, 0 ≤ w x^j := by
    intro x hx
    exact pow_nonneg (mul_nonneg hx.1 (sub_nonneg.mpr hx.2)) _
  have h := weighted_taylor (2*n) (by omega) (fun x => w x^j) hc hw
  rw [weighted_finite_identity] at h
  have h₀ : (∫ x in (0:ℝ)..1, w x^j)=B j 0 := by simp [B]
  rw [h₀,B_closed] at h
  exact h

end WeilDefect.MasterRecon.V10B37d

#print axioms WeilDefect.MasterRecon.V10B37d.term_integral
#print axioms WeilDefect.MasterRecon.V10B37d.taylor_pair
#print axioms WeilDefect.MasterRecon.V10B37d.weighted_finite_identity
#print axioms WeilDefect.MasterRecon.V10B37d.weighted_literal_enclosure
