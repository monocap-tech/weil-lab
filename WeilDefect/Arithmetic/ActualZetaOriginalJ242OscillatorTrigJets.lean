import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open scoped ContDiff

/-!
NF561 — prove the frequency-scaled sine/cosine initial jets used by
the ACTUAL 241 oscillator generators. The unchanged original source
has omega_f=2*pi*f at each of 67 frequency blocks.

Mathlib already proves the exact iterated derivatives of unscaled
sin/cos and the higher-derivative constant-scaling chain rule.
The next step, to multiply by the original x^k factors, is a
Leibniz rule using iteratedDeriv_fun_pow_zero (whose standalone
kernel is isolated below).

No substituted source, new frequency, or original independence
premise is introduced. These Lean statements are compiler
candidates until GitHub Actions accepts them.
-/

/-- Every odd initial derivative of sine at an arbitrary genuine
real oscillator frequency freq, including all freq=2πf from NF407. -/
theorem neutralNF561ScaledSin_oddJet (freq : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => Real.sin (freq * x))) 0 =
      (-1 : ℝ) ^ n * freq ^ (2 * n + 1) := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_sin (n := 2 * n + 1)) freq]
  rw [Real.iteratedDeriv_odd_sin]
  simp only [mul_zero, Real.cos_zero, mul_one]
  ring

/-- Every even initial derivative of cosine at any positive original
oscillator freq_f=2πf. The theorem is actually valid for all real freq. -/
theorem neutralNF561ScaledCos_evenJet (freq : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n)
      (fun x : ℝ => Real.cos (freq * x))) 0 =
      (-1 : ℝ) ^ n * freq ^ (2 * n) := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_cos (n := 2 * n)) freq]
  rw [Real.iteratedDeriv_even_cos]
  simp only [mul_zero, Real.cos_zero, mul_one]
  ring

/-- The other parity jets of sine at the origin vanish. -/
theorem neutralNF561ScaledSin_evenJet_zero (freq : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n)
      (fun x : ℝ => Real.sin (freq * x))) 0 = 0 := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_sin (n := 2 * n)) freq]
  simp [Real.iteratedDeriv_even_sin]

/-- The other parity jets of cosine at the origin vanish. -/
theorem neutralNF561ScaledCos_oddJet_zero (freq : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => Real.cos (freq * x))) 0 = 0 := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_cos (n := 2 * n + 1)) freq]
  simp [Real.iteratedDeriv_odd_cos]

/-- The original monomial source x^k has exactly one nonzero
initial higher derivative: derivative order k, value k!. This
is the precise source-relevant Leibniz selection mechanism. -/
theorem neutralNF561MonomialJet_zero_except (k m : ℕ) :
    (iteratedDeriv m (fun x : ℝ => x ^ k)) 0 =
      if m = k then (k.factorial : ℝ) else 0 := by
  simpa only [Nat.cast_ite, Nat.cast_zero] using
    (iteratedDeriv_fun_pow_zero (𝕜 := ℝ) (n := m) (m := k))

/-- Source-ready high-order product rule at the analytic initial
point. Multiplication by x^k selects ONLY derivative order k
of that monomial; every other Leibniz term vanishes at zero.
This is the generic mechanism for the unchanged NF407
x^k*sin(omega*x)/x^k*cos(omega*x) source families. -/
theorem neutralNF561MonomialTimesSmooth_jetAtZero
    (g : ℝ → ℝ) (hg : ContDiff ℝ ∞ g) (m k : ℕ) :
    (iteratedDeriv m (fun x : ℝ => x ^ k * g x)) 0 =
      if k ≤ m then (m.choose k : ℝ) * (k.factorial : ℝ) *
        (iteratedDeriv (m - k) g) 0 else 0 := by
  have hpow : ContDiffAt ℝ m (fun x : ℝ => x ^ k) 0 := by fun_prop
  have hg' : ContDiffAt ℝ m g 0 :=
    hg.contDiffAt.of_le (by simp)
  change iteratedDeriv m ((fun x : ℝ => x ^ k) * g) 0 = _
  rw [iteratedDeriv_mul hpow hg']
  simp only [iteratedDeriv_fun_pow_zero, Nat.cast_ite, Nat.cast_zero]
  simp only [mul_ite, mul_zero, zero_mul, ite_mul]
  simp only [Finset.sum_ite_eq', Finset.mem_range, Nat.lt_succ_iff]
  split_ifs <;> simp_all

end
end WeilDefect
