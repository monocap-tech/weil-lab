import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-! V10B24a: exact polynomial moments for the restricted action.
Use the native scaled beta identity for regular convolution, and
a polynomial divided difference (including its removable endpoint). -/
namespace WeilDefect.MasterRecon.V10B24a

open MeasureTheory Set Complex
open scoped BigOperators

noncomputable def dd (n : ℕ) (z s : ℝ) : ℝ :=
  ∑ j ∈ Finset.range n, z^(n-1-j)*(z-s)^j

noncomputable def harmonic (n : ℕ) : ℝ :=
  ∑ j ∈ Finset.range n, 1/((j:ℝ)+1)

theorem dd_mul (n : ℕ) (z s : ℝ) :
    s*dd n z s = z^n-(z-s)^n := by
  induction n with
  | zero => simp [dd]
  | succ n ih =>
    have he : dd (n+1) z s = z*dd n z s+(z-s)^n := by
      unfold dd
      rw [Finset.sum_range_succ,Finset.mul_sum]
      congr 1
      · apply Finset.sum_congr rfl
        intro j hj
        have hj' : j<n := Finset.mem_range.mp hj
        rw [show n+1-1-j = (n-1-j)+1 by omega,pow_succ]
        ring
      · simp
    rw [he]
    calc
      _ = z*(s*dd n z s)+s*(z-s)^n := by ring
      _ = _ := by rw [ih,pow_succ,pow_succ]; ring

theorem dd_eq (n : ℕ) (z s : ℝ) (hs : s ≠ 0) :
    dd n z s = (z^n-(z-s)^n)/s := by
  apply (eq_div_iff hs).mpr
  rw [mul_comm,dd_mul]

theorem convolution_monomial (j k : ℕ) (z : ℝ) (hz : 0 < z) :
    (∫ s in 0..z, (s:ℂ)^j*((z:ℂ)-(s:ℂ))^k) =
      (z:ℂ)^(j+k+1)*(j.factorial:ℂ)*(k.factorial:ℂ)/((j+k+1).factorial:ℂ) := by
  have hj : 0 < ((j:ℂ)+1).re := by simp; positivity
  have hk : 0 < ((k:ℂ)+1).re := by simp; positivity
  have h := Complex.betaIntegral_scaled ((j:ℂ)+1) ((k:ℂ)+1) hz
  rw [Complex.betaIntegral_eq_Gamma_mul_div _ _ hj hk] at h
  have hj' : (j:ℂ)+1 = ((j+1:ℕ):ℂ) := by push_cast; rfl
  have hk' : (k:ℂ)+1 = ((k+1:ℕ):ℂ) := by push_cast; rfl
  have hjk : (j:ℂ)+1+((k:ℂ)+1) = ((j+k+1:ℕ):ℂ)+1 := by push_cast; ring
  rw [show (j:ℂ)+1-1=(j:ℂ) by ring,show (k:ℂ)+1-1=(k:ℂ) by ring,
    show (j:ℂ)+1+((k:ℂ)+1)-1=((j+k+1:ℕ):ℂ) by push_cast; ring,
    Complex.cpow_natCast,Complex.Gamma_nat_eq_factorial,
    Complex.Gamma_nat_eq_factorial,hjk,Complex.Gamma_nat_eq_factorial] at h
  simpa only [Complex.cpow_natCast,mul_div_assoc,mul_assoc] using h

theorem reflected_power_integral (z : ℝ) (hz : 0 < z) (j : ℕ) :
    (∫ s in 0..z, (z-s)^j) = z^(j+1)/((j:ℝ)+1) := by
  have h := convolution_monomial 0 j z hz
  simp only [pow_zero,one_mul,zero_add,Nat.factorial_zero,Nat.cast_one] at h
  rw [Nat.factorial_succ,Nat.cast_mul,Nat.cast_add,Nat.cast_one] at h
  have hf : (j.factorial:ℂ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero j
  have hden : (j:ℂ)+1 ≠ 0 := by exact_mod_cast (show (j:ℝ)+1 ≠ 0 by positivity)
  have hr : (z:ℂ)^(j+1)*(j.factorial:ℂ)/(((j:ℂ)+1)*(j.factorial:ℂ)) =
      (z:ℂ)^(j+1)/((j:ℂ)+1) := by field_simp [hf,hden]
  rw [hr] at h
  have he : (fun s : ℝ => ((z:ℂ)-(s:ℂ))^j) =
      fun s => (( (z-s)^j : ℝ):ℂ) := by
    funext s
    push_cast
    rfl
  rw [he,intervalIntegral.integral_ofReal] at h
  exact_mod_cast h

theorem dd_integral (n : ℕ) (z : ℝ) (hz : 0 < z) :
    (∫ s in 0..z, dd n z s) = harmonic n*z^n := by
  unfold dd harmonic
  rw [intervalIntegral.integral_finsetSum]
  · rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro j hj
    rw [intervalIntegral.integral_const_mul,reflected_power_integral z hz]
    have hn : n-1-j+(j+1)=n := by have := Finset.mem_range.mp hj; omega
    rw [← mul_div_assoc,← pow_add,hn]
    ring
  · intro j _
    exact (by fun_prop : Continuous (fun s : ℝ => z^(n-1-j)*(z-s)^j)).intervalIntegrable _ _

end WeilDefect.MasterRecon.V10B24a

#print axioms WeilDefect.MasterRecon.V10B24a.dd_mul
#print axioms WeilDefect.MasterRecon.V10B24a.dd_eq
#print axioms WeilDefect.MasterRecon.V10B24a.convolution_monomial
#print axioms WeilDefect.MasterRecon.V10B24a.reflected_power_integral
#print axioms WeilDefect.MasterRecon.V10B24a.dd_integral
