import WeilDefect.Arithmetic.ActualZetaOriginalJ242FrequencyHermitePolynomial
import WeilDefect.Arithmetic.ActualZetaOriginalJ242HermiteDerivativeMultiplicity
import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF566 — the exact source-signed oscillator coefficients match
EVERY formal frequency derivative of the actual original 242
odd-jet frequency polynomial F_a(X)=X*p_a(X²).

The original 241 sine/cosine monomial oscillator odd-jets were
SHA-audited with coefficient
 (-1)^(n + k/2) (2n+1)!/(2n+1-k)! * omega^(2n+1-k)
when k <= 2n+1, and zero otherwise.

Nat.descFactorial encodes BOTH cases without division or
nonzero-denominator hypotheses. This file proves, in Lean,
the finite signed algebraic relationship between the exact
original 242 odd-jet dual coefficient vector a and the
formal Hermite derivative F_a^[k] for *every* k and real
frequency omega. It does not assume a source uniqueness theorem.

The last source-analytic step — equating the genuine actual
NF545 oscillator iteratedDeriv to this signed coefficient at
each frozen source index — remains a distinct compiler gate.
-/

/-- The exact signed initial-jet coefficient for the unchanged
original even-power sine / odd-power cosine oscillator formula.

It is automatically ZERO when k>2n+1 because the descending
factorial vanishes. No fake normal-form frequency is introduced. -/
def neutralNF566OriginalSignedOscillatorJetCoefficient
    (n k : ℕ) (freq : ℝ) : ℝ :=
  (-1 : ℝ) ^ (n + k / 2) *
    (Nat.descFactorial (2 * n + 1) k : ℝ) *
    freq ^ (2 * n + 1 - k)

/-- Exact integer combinatorics underlying the ORIGINAL source
oscillator derivatives: the general descending factorial equals
k! times the genuine binomial coefficient, including k>m. -/
theorem neutralNF566OriginalDescendingFactorial_choose (m k : ℕ) :
    (Nat.descFactorial m k : ℝ) =
      (k.factorial : ℝ) * (m.choose k : ℝ) := by
  exact_mod_cast Nat.descFactorial_eq_factorial_mul_choose m k

/-- The genuine oscillator signed coefficient is identically zero
when its original monomial degree exceeds the requested jet order. -/
theorem neutralNF566OriginalSignedOscillatorJetCoefficient_highOrder_zero
    (n k : ℕ) (freq : ℝ) (hk : 2 * n + 1 < k) :
    neutralNF566OriginalSignedOscillatorJetCoefficient n k freq = 0 := by
  unfold neutralNF566OriginalSignedOscillatorJetCoefficient
  rw [neutralNF566OriginalDescendingFactorial_choose]
  have hc : (2 * n + 1).choose k = 0 :=
    Nat.choose_eq_zero_of_lt hk
  simp [hc]

/-- The ORIGINAL audited coefficient, retaining its exact
even-sine/odd-cosine parity exponent n+k/2, is the
binomial-times-monomial-factorial form used by the true
NF561 high-order Leibniz derivative engine. -/
theorem neutralNF566OriginalSignedOscillatorJetCoefficient_choose
    (n k : ℕ) (freq : ℝ) :
    neutralNF566OriginalSignedOscillatorJetCoefficient n k freq =
      ((2 * n + 1).choose k : ℝ) * (k.factorial : ℝ) *
        ((-1 : ℝ) ^ (n + k / 2) *
          freq ^ (2 * n + 1 - k)) := by
  unfold neutralNF566OriginalSignedOscillatorJetCoefficient
  rw [neutralNF566OriginalDescendingFactorial_choose]
  ring

/-- The EXACT finite source-audited signed oscillator coefficient
sum is the k-th formal Hermite derivative of the true original
242-parameter frequency polynomial, up to the invertible
source parity factor (-1)^(k/2).

No individual source frequency has been selected here, and
no source independence or Gram positivity is assumed. -/
theorem neutralNF566OriginalSignedOddJets_eq_HermiteDerivative
    (a : Fin 242 → ℝ) (freq : ℝ) (k : ℕ) :
    (∑ n : Fin 242, a n *
      neutralNF566OriginalSignedOscillatorJetCoefficient n.val k freq) =
      (-1 : ℝ) ^ (k / 2) *
        ((Polynomial.derivative^[k])
          (neutralNF565OriginalFrequencyHermitePolynomial a)).eval freq := by
  rw [neutralNF565OriginalFrequencyHermitePolynomial_derivative_eval]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n hn
  unfold neutralNF566OriginalSignedOscillatorJetCoefficient
  rw [pow_add]
  ring

/-- The signed original source coefficient sums vanish iff the
true original 242-row frequency Hermite polynomial's k-th
formal derivative vanishes at that SAME exact frequency. -/
theorem neutralNF566OriginalSignedOddJets_zero_iff_HermiteDerivative_zero
    (a : Fin 242 → ℝ) (freq : ℝ) (k : ℕ) :
    (∑ n : Fin 242, a n *
      neutralNF566OriginalSignedOscillatorJetCoefficient n.val k freq) = 0 ↔
      ((Polynomial.derivative^[k])
        (neutralNF565OriginalFrequencyHermitePolynomial a)).eval freq = 0 := by
  rw [neutralNF566OriginalSignedOddJets_eq_HermiteDerivative]
  have hsign : (-1 : ℝ) ^ (k / 2) ≠ 0 :=
    pow_ne_zero _ (by norm_num)
  constructor
  · intro h
    exact (mul_eq_zero.mp h).resolve_left hsign
  · intro h
    simp [h]

/-- Source-signed finite original oscillator jets at orders
k=0,...,m-1 force at least multiplicity m for the EXACT
frequency Hermite polynomial F_a.

This uses the independently LEAN-PASSED NF554 generic Hermite
root-multiplicity theorem, but does not yet claim the analytic
NF545 sine/cosine derivatives equal the coefficient audit. -/
theorem neutralNF566OriginalSignedOddJets_force_HermiteMultiplicity
    (a : Fin 242 → ℝ) (freq : ℝ) (m : ℕ)
    (hp : neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0)
    (hjets : ∀ k : ℕ, k < m →
      (∑ n : Fin 242, a n *
        neutralNF566OriginalSignedOscillatorJetCoefficient n.val k freq) = 0) :
    m ≤ Polynomial.rootMultiplicity freq
      (neutralNF565OriginalFrequencyHermitePolynomial a) := by
  apply neutralNF554HermiteRootMultiplicity_of_vanishingJets
    (neutralNF565OriginalFrequencyHermitePolynomial a) freq m hp
  intro k hk
  change ((Polynomial.derivative^[k])
    (neutralNF565OriginalFrequencyHermitePolynomial a)).eval freq = 0
  exact (neutralNF566OriginalSignedOddJets_zero_iff_HermiteDerivative_zero
    a freq k).mp (hjets k hk)

/-- Source-ready LEFT KERNEL bridge, with the precise remaining
analytic equality explicitly given as a hypothesis, not smuggled
in as an axiom or as original independence.

Once NF562 establishes that every true NF545 source generator
odd derivative equals this signed jet coefficient, the original
left-kernel equations immediately imply its frequency Hermite
root multiplicities. -/
theorem neutralNF566ActualAnalyticOddJets_force_HermiteMultiplicity
    (a : Fin 242 → ℝ) (freq : ℝ) (m : ℕ)
    (g : ℕ → ℝ → ℝ)
    (hactual : ∀ k : ℕ, k < m → ∀ n : Fin 242,
      (iteratedDeriv (2 * n.val + 1) (g k)) 0 =
        neutralNF566OriginalSignedOscillatorJetCoefficient n.val k freq)
    (hkernel : ∀ k : ℕ, k < m →
      (∑ n : Fin 242, a n *
        (iteratedDeriv (2 * n.val + 1) (g k)) 0) = 0)
    (hp : neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0) :
    m ≤ Polynomial.rootMultiplicity freq
      (neutralNF565OriginalFrequencyHermitePolynomial a) := by
  apply neutralNF566OriginalSignedOddJets_force_HermiteMultiplicity a freq m hp
  intro k hk
  calc
    (∑ n : Fin 242, a n *
      neutralNF566OriginalSignedOscillatorJetCoefficient n.val k freq) =
      ∑ n : Fin 242, a n *
        (iteratedDeriv (2 * n.val + 1) (g k)) 0 := by
      apply Finset.sum_congr rfl
      intro n hn
      rw [hactual k hk n]
    _ = 0 := hkernel k hk

end
end WeilDefect
