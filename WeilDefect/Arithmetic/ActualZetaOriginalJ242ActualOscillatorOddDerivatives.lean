import WeilDefect.Arithmetic.ActualZetaOriginalJ242SourceFunctions
import WeilDefect.Arithmetic.ActualZetaOriginalJ242OscillatorTrigJets
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
NF562 — first ACTUAL source-indexed analytic differentiation theorem
for all 241 oscillator columns of the frozen NF407 242-generator
source. This is not a separate chosen family or generic matrix:
the function on the left is literally nf545OriginalSelectedRealGenerator,
and its source index is the original Fin 241 row.

For node i:Fin 241 the original source stores a rational frequency
f_i and integer order k_i, with genuine omega_i=2*pi*f_i. The
original parity condition selects x^k_i*sin(omega_i*x) for EVEN k_i
and x^k_i*cos(omega_i*x) for ODD k_i.

The generic NF561 higher Leibniz theorem says ONLY the k_i-th
derivative of x^k_i survives at x=0, so the source's (2n+1)-st
initial derivative is precisely a binomial/factorial times the
frequency-scaled trig derivative of order (2n+1-k_i), or zero if
k_i>2n+1. No assumed source uniqueness / Gram positivity is used.

The explicit (-1)^(n+floor(k_i/2)) closed form and
the ω-derivatives of ω*p(ω²) are further formalization gates.
-/

/-- Exact original NF407 row order, without reindexing. -/
def neutralNF562OriginalOscillatorOrder (i : Fin 241) : ℕ :=
  (nf545OriginalOscillatorNodeAt i).2

/-- Exact real oscillator frequency 2*pi*f_i for the original source. -/
def neutralNF562OriginalOscillatorOmega (i : Fin 241) : ℝ :=
  2 * Real.pi * ((nf545OriginalOscillatorNodeAt i).1 : ℝ)

/-- Source-selected trig factor: sine iff original monomial order even,
cosine otherwise. -/
def neutralNF562OriginalOscillatorTrig (i : Fin 241) (x : ℝ) : ℝ :=
  if Even (neutralNF562OriginalOscillatorOrder i) then
    Real.sin (neutralNF562OriginalOscillatorOmega i * x)
  else
    Real.cos (neutralNF562OriginalOscillatorOmega i * x)

/-- This is a definitional equality to the authentic NF545 source
generator, not an assumed new model of the oscillator. -/
theorem neutralNF562OriginalOscillator_exactSource (i : Fin 241) :
    nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩ =
      (fun x : ℝ => x ^ (neutralNF562OriginalOscillatorOrder i) *
         neutralNF562OriginalOscillatorTrig i x) := by
  funext x
  simp only [nf545OriginalSelectedRealGenerator, dif_pos i.isLt]
  rfl

/-- Every individual authentic oscillator's trig factor is C-infty.
This uses the literal 2*pi*f_i source frequency, not pi=1. -/
theorem neutralNF562OriginalOscillatorTrig_smooth (i : Fin 241) :
    ContDiff ℝ ∞ (neutralNF562OriginalOscillatorTrig i) := by
  unfold neutralNF562OriginalOscillatorTrig
  by_cases h : Even (neutralNF562OriginalOscillatorOrder i)
  · simp only [if_pos h]
    fun_prop
  · simp only [if_neg h]
    fun_prop

/-- The actual (2n+1)-st analytic initial jet of EACH of the
241 historical source oscillators. Every original rational frequency,
monomial order and even/odd sine/cosine choice is preserved.

This is the exact Leibniz reduction of a true source derivative.
The parity simplification to the source-audited signed factorial
closed form is deliberately a subsequent theorem, not an axiom. -/
theorem neutralNF562OriginalOscillator_actualOddJet
    (i : Fin 241) (n : Fin 242) :
    (iteratedDeriv (2 * n.val + 1)
      (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0 =
      if neutralNF562OriginalOscillatorOrder i ≤ 2 * n.val + 1 then
        ((2 * n.val + 1).choose
          (neutralNF562OriginalOscillatorOrder i) : ℝ) *
        ((neutralNF562OriginalOscillatorOrder i).factorial : ℝ) *
        (iteratedDeriv
          (2 * n.val + 1 - neutralNF562OriginalOscillatorOrder i)
          (neutralNF562OriginalOscillatorTrig i)) 0
      else 0 := by
  rw [neutralNF562OriginalOscillator_exactSource i]
  exact neutralNF561MonomialTimesSmooth_jetAtZero
    (neutralNF562OriginalOscillatorTrig i)
    (neutralNF562OriginalOscillatorTrig_smooth i)
    (2 * n.val + 1) (neutralNF562OriginalOscillatorOrder i)

/-- The source row is exactly zero whenever its original monomial
order exceeds the requested odd derivative order, before any
frequency expansion or numerical approximation. -/
theorem neutralNF562OriginalOscillator_actualOddJet_highOrderZero
    (i : Fin 241) (n : Fin 242)
    (hk : 2 * n.val + 1 < neutralNF562OriginalOscillatorOrder i) :
    (iteratedDeriv (2 * n.val + 1)
      (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0 = 0 := by
  rw [neutralNF562OriginalOscillator_actualOddJet]
  simp [Nat.not_le.mpr hk]

end
end WeilDefect
