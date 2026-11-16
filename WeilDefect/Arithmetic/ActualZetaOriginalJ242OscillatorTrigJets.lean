import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

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
real oscillator frequency ω, including all ω=2πf from NF407. -/
theorem neutralNF561ScaledSin_oddJet (ω : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => Real.sin (ω * x))) 0 =
      (-1 : ℝ) ^ n * ω ^ (2 * n + 1) := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_sin (n := 2 * n + 1)) ω]
  simp [Real.iteratedDeriv_odd_sin, mul_comm]

/-- Every even initial derivative of cosine at any positive original
oscillator ω_f=2πf. The theorem is actually valid for all real ω. -/
theorem neutralNF561ScaledCos_evenJet (ω : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n)
      (fun x : ℝ => Real.cos (ω * x))) 0 =
      (-1 : ℝ) ^ n * ω ^ (2 * n) := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_cos (n := 2 * n)) ω]
  simp [Real.iteratedDeriv_even_cos, mul_comm]

/-- The other parity jets of sine at the origin vanish. -/
theorem neutralNF561ScaledSin_evenJet_zero (ω : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n)
      (fun x : ℝ => Real.sin (ω * x))) 0 = 0 := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_sin (n := 2 * n)) ω]
  simp [Real.iteratedDeriv_even_sin]

/-- The other parity jets of cosine at the origin vanish. -/
theorem neutralNF561ScaledCos_oddJet_zero (ω : ℝ) (n : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => Real.cos (ω * x))) 0 = 0 := by
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_cos (n := 2 * n + 1)) ω]
  simp [Real.iteratedDeriv_odd_cos]

/-- The original monomial source x^k has exactly one nonzero
initial higher derivative: derivative order k, value k!. This
is the precise source-relevant Leibniz selection mechanism. -/
theorem neutralNF561MonomialJet_zero_except (k m : ℕ) :
    (iteratedDeriv m (fun x : ℝ => x ^ k)) 0 =
      if m = k then (k.factorial : ℝ) else 0 := by
  exact iteratedDeriv_fun_pow_zero

end
end WeilDefect
