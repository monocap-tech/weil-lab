import WeilDefect.MasterRecon.V10B34a
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-! V10B47a: ordinary beta integrals, independently of the centered
two-index moment recurrence in V10B36a. -/
namespace WeilDefect.MasterRecon.V10B47a
open MeasureTheory Set

noncomputable def beta (n m : ℕ) : ℝ :=
  ∫ x in (0:ℝ)..1, x^n*(1-x)^m

theorem beta_zero (n : ℕ) : beta n 0=1/((n:ℝ)+1) := by
  unfold beta
  simp only [pow_zero,mul_one]
  rw [intervalIntegral.integral_pow] <;> simp

theorem beta_step (n m : ℕ) :
    ((n:ℝ)+1)*beta n (m+1)=((m:ℝ)+1)*beta (n+1) m := by
  let u : ℝ → ℝ := fun x => (1-x)^(m+1)
  let v : ℝ → ℝ := fun x => x^(n+1)
  let du : ℝ → ℝ := fun x => -((m:ℝ)+1)*(1-x)^m
  let dv : ℝ → ℝ := fun x => ((n:ℝ)+1)*x^n
  have hu (x : ℝ) : HasDerivAt u (du x) x := by
    have h := ((hasDerivAt_const x (1:ℝ)).sub (hasDerivAt_id x)).fun_pow (m+1)
    convert h using 1 <;> first | rfl | (simp [du,u] <;> ring)
  have hv (x : ℝ) : HasDerivAt v (dv x) x := by
    simpa [v,dv] using hasDerivAt_pow (n+1) x
  have hdu : Continuous du := by unfold du; fun_prop
  have hdv : Continuous dv := by unfold dv; fun_prop
  have h := intervalIntegral.integral_mul_deriv_eq_deriv_mul
    (a := (0:ℝ)) (b := 1) (fun x _ => hu x) (fun x _ => hv x)
      (hdu.intervalIntegrable 0 1) (hdv.intervalIntegrable 0 1)
  have hL : (fun x : ℝ => u x*dv x) =
      fun x => ((n:ℝ)+1)*(x^n*(1-x)^(m+1)) := by
    funext x
    dsimp [u,dv]
    ring
  have hR : (fun x : ℝ => du x*v x) =
      fun x => (-((m:ℝ)+1))*(x^(n+1)*(1-x)^m) := by
    funext x
    dsimp [du,v]
    ring
  rw [hL,hR,intervalIntegral.integral_const_mul,intervalIntegral.integral_const_mul] at h
  have h₀ : v 0=0 := by simp [v]
  have h₁ : u 1=0 := by simp [u]
  rw [h₀,h₁,zero_mul,mul_zero,sub_self,zero_sub] at h
  unfold beta
  linarith only [h]

theorem beta_closed (n m : ℕ) :
    beta n m = (n.factorial:ℝ)*(m.factorial:ℝ)/((n+m+1).factorial:ℝ) := by
  induction m generalizing n with
  | zero =>
    rw [beta_zero]
    simp only [Nat.factorial_zero,Nat.cast_one,mul_one,add_zero,Nat.factorial_succ,Nat.cast_mul,Nat.cast_add]
    have hn : (n.factorial:ℝ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero n
    field_simp [hn] <;> ring
  | succ m ih =>
    have h := beta_step n m
    rw [ih (n+1)] at h
    have hn : (0:ℝ)<(n:ℝ)+1 := by positivity
    apply mul_left_cancel₀ hn.ne'
    calc
      _ = ((m:ℝ)+1)*(( (n+1).factorial:ℝ)*(m.factorial:ℝ)/
          ((n+1+m+1).factorial:ℝ)) := h
      _ = _ := by
        rw [show n+1+m+1=n+(m+1)+1 by omega,
          Nat.factorial_succ n,Nat.factorial_succ m]
        push_cast
        ring

end WeilDefect.MasterRecon.V10B47a

#print axioms WeilDefect.MasterRecon.V10B47a.beta_zero
#print axioms WeilDefect.MasterRecon.V10B47a.beta_step
#print axioms WeilDefect.MasterRecon.V10B47a.beta_closed
