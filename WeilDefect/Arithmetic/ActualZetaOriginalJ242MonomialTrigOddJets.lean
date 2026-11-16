import WeilDefect.Arithmetic.ActualZetaOriginalJ242OscillatorTrigJets
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
NF562 — exact closed frequency-and-parity formulas for all oscillator
building blocks in the historical NF407 241-mode original source.

The even monomial source is x^(2r)*sin(omega*x).
The odd monomial source is x^(2r+1)*cos(omega*x).
These are not arbitrary proxies: they are precisely the NF545
selected source forms. The finite original index/source-frequency
attachment appears separately in ActualOscillatorOddDerivatives.

Each theorem directly differentiates its actual smooth real function
to odd order 2n+1; it uses NF561's initial-point higher-order
Leibniz rule and scaled trig derivative identities. No numerical
omega specialization, Gram invertibility, independence axiom,
or model substitution occurs.
-/

/-- The exact genuine even-monomial *sine* oscillator odd jet,
valid for every nonzero or zero real omega and n>=r. -/
theorem neutralNF562EvenMonomialSine_originalOddJet
    (ω : ℝ) (n r : ℕ) (hr : r ≤ n) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r) * Real.sin (ω * x))) 0 =
        ((2 * n + 1).choose (2 * r) : ℝ) *
        ((2 * r).factorial : ℝ) *
        ((-1 : ℝ) ^ (n - r) * ω ^ (2 * (n - r) + 1)) := by
  have hle : 2 * r ≤ 2 * n + 1 := by omega
  have hsub : 2 * n + 1 - 2 * r = 2 * (n - r) + 1 := by omega
  rw [neutralNF561MonomialTimesSmooth_jetAtZero
    (fun x : ℝ => Real.sin (ω * x)) (by fun_prop)
    (2 * n + 1) (2 * r)]
  simp only [if_pos hle]
  rw [hsub, neutralNF561ScaledSin_oddJet]

/-- The exact genuine odd-monomial *cosine* oscillator odd jet.
This covers all odd-k original selected generators with k=2r+1. -/
theorem neutralNF562OddMonomialCosine_originalOddJet
    (ω : ℝ) (n r : ℕ) (hr : r ≤ n) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r + 1) * Real.cos (ω * x))) 0 =
        ((2 * n + 1).choose (2 * r + 1) : ℝ) *
        ((2 * r + 1).factorial : ℝ) *
        ((-1 : ℝ) ^ (n - r) * ω ^ (2 * (n - r))) := by
  have hle : 2 * r + 1 ≤ 2 * n + 1 := by omega
  have hsub : 2 * n + 1 - (2 * r + 1) = 2 * (n - r) := by omega
  rw [neutralNF561MonomialTimesSmooth_jetAtZero
    (fun x : ℝ => Real.cos (ω * x)) (by fun_prop)
    (2 * n + 1) (2 * r + 1)]
  simp only [if_pos hle]
  rw [hsub, neutralNF561ScaledCos_evenJet]

/-- Exact factorial normalization of the genuine source's
higher Leibniz coefficient, over the REAL field. This is the
identity connecting the closed binomial jet to the original
NF554 factorial-ratio odd-jet certificate. -/
theorem neutralNF562ChooseFactorial_eq_factorialRatio
    (m k : ℕ) (hk : k ≤ m) :
    (m.choose k : ℝ) * (k.factorial : ℝ) =
      (m.factorial : ℝ) / ((m - k).factorial : ℝ) := by
  have hden : (0 : ℝ) < ((m - k).factorial : ℝ) := by
    exact_mod_cast Nat.factorial_pos (m - k)
  apply (eq_div_iff (ne_of_gt hden)).2
  exact_mod_cast (Nat.choose_mul_factorial_mul_factorial hk)

/-- The exact REAL factorial-ratio closed odd jet for the even-k
sine branch of each source oscillator, with no numerical pi. -/
theorem neutralNF562EvenMonomialSine_originalOddJet_factorial
    (ω : ℝ) (n r : ℕ) (hr : r ≤ n) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r) * Real.sin (ω * x))) 0 =
        ((2 * n + 1).factorial : ℝ) /
        ((2 * (n - r) + 1).factorial : ℝ) *
        ((-1 : ℝ) ^ (n - r) * ω ^ (2 * (n - r) + 1)) := by
  have hle : 2 * r ≤ 2 * n + 1 := by omega
  have hsub : 2 * n + 1 - 2 * r = 2 * (n - r) + 1 := by omega
  rw [neutralNF562EvenMonomialSine_originalOddJet ω n r hr]
  rw [neutralNF562ChooseFactorial_eq_factorialRatio
    (2 * n + 1) (2 * r) hle, hsub]

/-- The exact REAL factorial-ratio closed odd jet for the odd-k
cosine branch of each source oscillator, with no numerical pi. -/
theorem neutralNF562OddMonomialCosine_originalOddJet_factorial
    (ω : ℝ) (n r : ℕ) (hr : r ≤ n) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r + 1) * Real.cos (ω * x))) 0 =
        ((2 * n + 1).factorial : ℝ) /
        ((2 * (n - r)).factorial : ℝ) *
        ((-1 : ℝ) ^ (n - r) * ω ^ (2 * (n - r))) := by
  have hle : 2 * r + 1 ≤ 2 * n + 1 := by omega
  have hsub : 2 * n + 1 - (2 * r + 1) = 2 * (n - r) := by omega
  rw [neutralNF562OddMonomialCosine_originalOddJet ω n r hr]
  rw [neutralNF562ChooseFactorial_eq_factorialRatio
    (2 * n + 1) (2 * r + 1) hle, hsub]

/-- The original sine source vanishes at odd order below its
even monomial degree, independent of frequency. -/
theorem neutralNF562EvenMonomialSine_originalOddJet_below
    (ω : ℝ) (n r : ℕ) (hr : n < r) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r) * Real.sin (ω * x))) 0 = 0 := by
  rw [neutralNF561MonomialTimesSmooth_jetAtZero
    (fun x : ℝ => Real.sin (ω * x)) (by fun_prop)
    (2 * n + 1) (2 * r)]
  have hnot : ¬ (2 * r ≤ 2 * n + 1) := by omega
  simp [hnot]

/-- The original cosine source vanishes at odd order below its
odd monomial degree, independent of frequency. -/
theorem neutralNF562OddMonomialCosine_originalOddJet_below
    (ω : ℝ) (n r : ℕ) (hr : n < r) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r + 1) * Real.cos (ω * x))) 0 = 0 := by
  rw [neutralNF561MonomialTimesSmooth_jetAtZero
    (fun x : ℝ => Real.cos (ω * x)) (by fun_prop)
    (2 * n + 1) (2 * r + 1)]
  have hnot : ¬ (2 * r + 1 ≤ 2 * n + 1) := by omega
  simp [hnot]

end
end WeilDefect
