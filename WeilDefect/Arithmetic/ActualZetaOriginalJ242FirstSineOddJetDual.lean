import WeilDefect.Arithmetic.ActualZetaOriginalJ242OscillatorTrigJets
import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialSourceNodes
import WeilDefect.Arithmetic.ActualZetaOriginalJ242SourceFunctions
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF563 — FIRST positive-frequency original-source odd-jet to dual
polynomial bridge, starting at the genuine k=0 oscillator column.

The unique original source at index 0 is the ORIGINAL first
frequency f=37/64 with monomial order k=0. Its selected generator
is exactly sin(2π*(37/64)*x). All even powers and odd powers
required for other source columns remain intact in NF545/NF562;
none are replaced with other test generators.

For arbitrary real coefficient a : Fin 242 → ℝ, its true odd
dual polynomial is p_a(T)=Σ_n (-1)^n a_n T^n. The k=0 identity
is the exact positive-frequency evaluation

  Σ_n a_n D^(2n+1) sin(freqx)|_(x=0)
    = freq * p_a(freq²).

This is the first source-analytic instance of the 67-node Hermite
bridge, not a global 241-oscillator independence theorem.
-/

/-- Exact algebraic dual evaluation of all 242 odd sine jets
at any real frequency. This uses the ORIGINAL 242 coefficient
sign convention, not a replacement polynomial family. -/
theorem neutralNF563DualPolynomial_sineZeroOrder
    (a : Fin 242 → ℝ) (freq : ℝ) :
    (∑ n : Fin 242, a n * ((-1 : ℝ) ^ n.val * freq ^ (2 * n.val + 1))) =
      freq * (neutralNF557OriginalDualPolynomial a).eval (freq ^ 2) := by
  unfold neutralNF557OriginalDualPolynomial
  rw [Polynomial.eval_finsetSum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n hn
  rw [Polynomial.eval_monomial]
  have hp : freq ^ (2 * n.val + 1) = (freq ^ 2) ^ n.val * freq := by
    rw [pow_add, pow_mul]
    ring
  rw [hp]
  ring

/-- The dual finite sum is the ACTUAL analytic odd-derivative
sum of the real sine function, for every nonnegative integer
initial-jet index from the original 242 rows. -/
theorem neutralNF563SineSourceOddJets_dual
    (a : Fin 242 → ℝ) (freq : ℝ) :
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (fun x : ℝ => Real.sin (freq * x))) 0) =
      freq * (neutralNF557OriginalDualPolynomial a).eval (freq ^ 2) := by
  calc
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (fun x : ℝ => Real.sin (freq * x))) 0) =
      ∑ n : Fin 242,
        a n * ((-1 : ℝ) ^ n.val * freq ^ (2 * n.val + 1)) := by
      apply Finset.sum_congr rfl
      intro n hn
      rw [neutralNF561ScaledSin_oddJet]
    _ = freq * (neutralNF557OriginalDualPolynomial a).eval (freq ^ 2) :=
      neutralNF563DualPolynomial_sineZeroOrder a freq

/-- ALL original zero-monomial-order source oscillators, not just
the first: whenever the authentic NF407 source index i carries
k_i=0, its 242 odd-jet left-kernel expression is precisely
the actual source omega_i times the original polynomial at omega_i².

The 67 original frequency blocks each have such a k=0 row in
the unchanged contiguous source list. No source frequency is
selected by numerical sampling or invented here. -/
theorem neutralNF563ActualOriginalZeroOrderOscillator_dual
    (a : Fin 242 → ℝ) (i : Fin 241)
    (hzero : (nf545OriginalOscillatorNodeAt i).2 = 0) :
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) =
      (2 * Real.pi * ((nf545OriginalOscillatorNodeAt i).1 : ℝ)) *
        (neutralNF557OriginalDualPolynomial a).eval
          ((2 * Real.pi * ((nf545OriginalOscillatorNodeAt i).1 : ℝ)) ^ 2) := by
  have hsource :
      nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩ =
        (fun x : ℝ => Real.sin
          ((2 * Real.pi * ((nf545OriginalOscillatorNodeAt i).1 : ℝ)) * x)) := by
    funext x
    simp [nf545OriginalSelectedRealGenerator, hzero,
      show i.val < 241 from i.isLt]
  rw [hsource]
  exact neutralNF563SineSourceOddJets_dual
    a (2 * Real.pi * ((nf545OriginalOscillatorNodeAt i).1 : ℝ))

/-- The frozen ORIGINAL NF407 source's FIRST exact oscillator
node is (37/64, k=0), not an invented sine basis. -/
theorem neutralNF563ActualFirstOriginalOscillatorNode :
    nf545OriginalOscillatorNodeAt ⟨0, by omega⟩ =
      ((37 / 64 : ℚ), 0) := by
  decide +kernel

/-- The literal source generator at original index zero is its
historical sine at 2π*37/64, with no substituted order. -/
theorem neutralNF563ActualFirstOriginalOscillator_eq_sine :
    nf545OriginalSelectedRealGenerator ⟨0, by omega⟩ =
      (fun x : ℝ =>
        Real.sin ((2 * Real.pi * (37 / 64 : ℝ)) * x)) := by
  funext x
  simp only [nf545OriginalSelectedRealGenerator, dif_pos (by omega : 0 < 241),
    neutralNF563ActualFirstOriginalOscillatorNode]
  norm_num

/-- The actual FIRST original oscillator's exact analytic
242-odd-jet left-kernel equation IS evaluation of the true
242-dual polynomial at the first squared node.

The other 66 blocks and their higher-order k>0 jets are still
OPEN for source derivative-to-polynomial transfer in Lean. -/
theorem neutralNF563ActualFirstOriginalOscillator_dual
    (a : Fin 242 → ℝ) :
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨0, by omega⟩)) 0) =
      (2 * Real.pi * (37 / 64 : ℝ)) *
        (neutralNF557OriginalDualPolynomial a).eval
          ((2 * Real.pi * (37 / 64 : ℝ)) ^ 2) := by
  rw [neutralNF563ActualFirstOriginalOscillator_eq_sine]
  exact neutralNF563SineSourceOddJets_dual
    a (2 * Real.pi * (37 / 64 : ℝ))

/-- The first actual NF407 oscillator left-kernel equation forces
a genuine root of the original 242-dual polynomial at the real
positive squared frequency (2*pi*37/64)^2. This is an authentic
first-node Hermite obligation, not numerical root verification. -/
theorem neutralNF563ActualFirstOriginalOscillator_forcesRoot
    (a : Fin 242 → ℝ)
    (hfirst : (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨0, by omega⟩)) 0) = 0) :
    (neutralNF557OriginalDualPolynomial a).eval
      ((2 * Real.pi * (37 / 64 : ℝ)) ^ 2) = 0 := by
  rw [neutralNF563ActualFirstOriginalOscillator_dual] at hfirst
  have hfreq : (2 * Real.pi * (37 / 64 : ℝ)) ≠ 0 := by
    positivity
  exact (mul_eq_zero.mp hfirst).resolve_left hfreq


end
end WeilDefect
