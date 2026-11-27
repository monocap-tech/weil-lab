import WeilDefect.MasterRecon.V10B33a
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

/-! V10B34a: discharge Rodrigues boundary conditions using the native
power-divisibility lemma. The exponential projection is literal, not an
assumed series identity. Infinite expansion and normalized load attachment
remain separate. -/
namespace WeilDefect.MasterRecon.V10B34a

open MeasureTheory Set Polynomial
open scoped BigOperators
open WeilDefect.MasterRecon.V10B33a

theorem power_root_iterate_zero (q : ℤ[X]) (j k : ℕ) (x : ℝ)
    (hk : k < j) (hx : aeval x q = 0) :
    aeval x ((Polynomial.derivative^[k]) (q^j)) = 0 := by
  obtain ⟨r, hr⟩ := Polynomial.pow_sub_dvd_iterate_derivative_pow q j k
  rw [hr, map_mul, map_pow, hx, zero_pow (Nat.sub_ne_zero_of_lt hk), zero_mul]

theorem rodrigues_endpoints (j k : ℕ) (hk : k < j) :
    aeval (0:ℝ) ((Polynomial.derivative^[k])
      ((Polynomial.X:ℤ[X])^j*(1-Polynomial.X)^j)) = 0 ∧
    aeval (1:ℝ) ((Polynomial.derivative^[k])
      ((Polynomial.X:ℤ[X])^j*(1-Polynomial.X)^j)) = 0 := by
  rw [← mul_pow]
  constructor
  · exact power_root_iterate_zero (Polynomial.X*(1-Polynomial.X)) j k 0 hk (by simp)
  · exact power_root_iterate_zero (Polynomial.X*(1-Polynomial.X)) j k 1 hk (by simp)

theorem exp_projection_scaled (j : ℕ) (a b : ℝ) :
    (j.factorial:ℝ)*(∫ x in (0:ℝ)..1, Real.exp (a*x+b)*legendre j x) =
      a^j*(∫ x in (0:ℝ)..1, Real.exp (a*x+b)*x^j*(1-x)^j) := by
  let p : ℤ[X] := Polynomial.X^j*(1-Polynomial.X)^j
  let v : ℕ → ℝ → ℝ := fun k x => aeval x ((Polynomial.derivative^[k]) p)
  have hv (k : ℕ) : Continuous (v k) :=
    ((Polynomial.derivative^[k]) p).differentiable_aeval.continuous
  have hdv (k : ℕ) (x : ℝ) : HasDerivAt (v k) (v (k+1) x) x := by
    dsimp only [v]
    rw [Function.iterate_succ_apply']
    exact ((Polynomial.derivative^[k]) p).hasDerivAt_aeval x
  have hz (k : ℕ) (hk : k < j) : v k 0=0 ∧ v k 1=0 :=
    rodrigues_endpoints j k hk
  have hp := exp_parts j a b v hv hdv hz
  have hfun : (fun x : ℝ => (j.factorial:ℝ)*(Real.exp (a*x+b)*legendre j x)) =
      fun x => (-1:ℝ)^j*(Real.exp (a*x+b)*v j x) := by
    funext x
    calc
      _ = Real.exp (a*x+b)*((j.factorial:ℝ)*legendre j x) := by ring
      _ = Real.exp (a*x+b)*((-1:ℝ)^j*v j x) := by rw [rodrigues_eval]; rfl
      _ = _ := by ring
  have h0 : (fun x : ℝ => Real.exp (a*x+b)*v 0 x) =
      fun x => Real.exp (a*x+b)*x^j*(1-x)^j := by
    funext x
    simp [v,p,Function.iterate_zero_apply,mul_assoc]
  have hs : (-1:ℝ)^j*(-a)^j = a^j := by
    rw [← mul_pow]
    congr 1
    ring
  calc
    _ = ∫ x in (0:ℝ)..1, (j.factorial:ℝ)*(Real.exp (a*x+b)*legendre j x) :=
      (intervalIntegral.integral_const_mul _ _).symm
    _ = ∫ x in (0:ℝ)..1, (-1:ℝ)^j*(Real.exp (a*x+b)*v j x) :=
      congrArg (fun f : ℝ → ℝ => ∫ x in (0:ℝ)..1, f x) hfun
    _ = (-1:ℝ)^j*(∫ x in (0:ℝ)..1, Real.exp (a*x+b)*v j x) :=
      intervalIntegral.integral_const_mul _ _
    _ = _ := by rw [hp, ← mul_assoc, hs, h0]

theorem exp_projection (j : ℕ) (a b : ℝ) :
    (∫ x in (0:ℝ)..1, Real.exp (a*x+b)*legendre j x) =
      (a^j/(j.factorial:ℝ))*(∫ x in (0:ℝ)..1, Real.exp (a*x+b)*x^j*(1-x)^j) := by
  have hf : (j.factorial:ℝ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero j
  have h := exp_projection_scaled j a b
  field_simp [hf]
  linarith only [h]

theorem exp_projection_pos (j : ℕ) (a b : ℝ) (ha : 0 < a) :
    0 < ∫ x in (0:ℝ)..1, Real.exp (a*x+b)*legendre j x := by
  rw [exp_projection]
  have hf : 0 < (j.factorial:ℝ) := by exact_mod_cast Nat.factorial_pos j
  apply mul_pos (div_pos (pow_pos ha _) hf)
  apply intervalIntegral.integral_pos (by norm_num : (0:ℝ)<1)
  · apply Continuous.continuousOn
    fun_prop
  · intro x hx
    exact mul_nonneg (mul_nonneg (Real.exp_pos _).le (pow_nonneg hx.1.le _))
      (pow_nonneg (sub_nonneg.mpr hx.2) _)
  · refine ⟨1/2, by constructor <;> norm_num, ?_⟩
    exact mul_pos (mul_pos (Real.exp_pos _) (pow_pos (by norm_num) _))
      (pow_pos (by norm_num) _)

end WeilDefect.MasterRecon.V10B34a

#print axioms WeilDefect.MasterRecon.V10B34a.power_root_iterate_zero
#print axioms WeilDefect.MasterRecon.V10B34a.rodrigues_endpoints
#print axioms WeilDefect.MasterRecon.V10B34a.exp_projection_scaled
#print axioms WeilDefect.MasterRecon.V10B34a.exp_projection
#print axioms WeilDefect.MasterRecon.V10B34a.exp_projection_pos
