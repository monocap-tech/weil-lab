import WeilDefect.Arithmetic.ActualZetaOriginalJ242Actual67BlockCoverage
import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualOscillatorHermiteBridge
import WeilDefect.Arithmetic.ActualZetaOriginalJ242HermiteDerivativeMultiplicity
import WeilDefect.Arithmetic.ActualZetaOriginalJ242QuadraticRootMultiplicity
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF567 — source-indexed completeness of ALL 67 genuine NF407
oscillator frequency blocks, with precisely their original
contiguous monomial-order ranges 0..m_f-1.

Earlier NF545 checked the original source count 67, positivity,
pairwise distinct rational frequencies and total multiplicity 241,
and established that the actual 241 oscillator source is literally
the flatMap of those original frequency blocks and List.range m_f.

This file closes the *index extraction* gate: for EACH of the 67
frozen source frequency blocks and EACH k<m_f, there is a
literal original Fin241 source index with the exact same frequency
and monomial order. The proof uses List.mem_flatMap,
List.mem_map, List.mem_range and List.mem_iff_get, not
assumed block coverage or a substitute interpolation family.

Together with NF566's true analytic left-kernel to Hermite
frequency derivative theorem this constructs the exact
m_f derivative-zero obligations at ALL original frequencies.
The subsequent 68-node simultaneous degree contradiction
remains a separate source-global polynomial obligation.
-/

/-- The original source contains ALL formal-frequency derivative
orders k=0,...,m_g-1 at every g-th frozen frequency.

The input hzeros is the exact full genuine oscillator-index
conclusion from NF566, with no new function or source premise. -/
theorem neutralNF567OriginalBlockHermiteJets_fromActualOscillators
    (a : Fin 242 → ℝ)
    (hzeros : ∀ i : Fin 241,
      ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
        (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
          (neutralNF562OriginalOscillatorOmega i) = 0)
    (g : Fin 67) :
    ∀ k : ℕ, k < (neutralNF567OriginalGroupAt g).2 →
      ((Polynomial.derivative^[k])
        (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
          (neutralNF567OriginalGroupOmega g) = 0 := by
  intro k hk
  obtain ⟨i, hi⟩ :=
    neutralNF567OriginalEveryBlockOrder_isActualSource g k hk
  have horder : neutralNF562OriginalOscillatorOrder i = k := by
    simp only [neutralNF562OriginalOscillatorOrder, hi]
  have homega :
      neutralNF562OriginalOscillatorOmega i =
        neutralNF567OriginalGroupOmega g := by
    simp only [neutralNF562OriginalOscillatorOmega,
      neutralNF567OriginalGroupOmega, hi]
  simpa only [horder, homega] using hzeros i

/-- All 67 true source blocks simultaneously force their
EXACT original multiplicities as roots of the frequency-side
polynomial F_a, provided it is nonzero.

This is not merely a symbolic-source audit: its prerequisite
is the source-indexed ACTUAL real analytic oscillator derivative
kernel theorem from NF566. -/
theorem neutralNF567OriginalAll67HermiteRootMultiplicities
    (a : Fin 242 → ℝ)
    (hp : neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0)
    (hzeros : ∀ i : Fin 241,
      ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
        (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
          (neutralNF562OriginalOscillatorOmega i) = 0) :
    ∀ g : Fin 67,
      (neutralNF567OriginalGroupAt g).2 ≤
        Polynomial.rootMultiplicity
          (neutralNF567OriginalGroupOmega g)
          (neutralNF565OriginalFrequencyHermitePolynomial a) := by
  intro g
  apply neutralNF554HermiteRootMultiplicity_of_vanishingJets
    (neutralNF565OriginalFrequencyHermitePolynomial a)
    (neutralNF567OriginalGroupOmega g)
    (neutralNF567OriginalGroupAt g).2 hp
  intro k hk
  change ((Polynomial.derivative^[k])
    (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
      (neutralNF567OriginalGroupOmega g) = 0
  exact neutralNF567OriginalBlockHermiteJets_fromActualOscillators
    a hzeros g k hk

/-- Exact NF556 transfer: once the original genuine oscillator
analytic derivative equations force multiplicities in F_a, each
source frequency block g contributes its ORIGINAL m_g root
multiplicity to the real p_a polynomial at the true squared
frequency (2π f_g)².

Both nonzero assumptions are explicitly exposed. This does
not assert source independence or conceal the still-needed
proof that p_a≠0 entails F_a≠0. -/
theorem neutralNF567OriginalAll67SquaredDualRootMultiplicities
    (a : Fin 242 → ℝ)
    (hp : neutralNF557OriginalDualPolynomial a ≠ 0)
    (hF : neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0)
    (hzeros : ∀ i : Fin 241,
      ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
        (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
          (neutralNF562OriginalOscillatorOmega i) = 0) :
    ∀ g : Fin 67,
      (neutralNF567OriginalGroupAt g).2 ≤
        Polynomial.rootMultiplicity
          (neutralNF567OriginalGroupOmega g ^ 2)
          (neutralNF557OriginalDualPolynomial a) := by
  intro g
  have hmult :=
    neutralNF567OriginalAll67HermiteRootMultiplicities a hF hzeros g
  rw [neutralNF565OriginalFrequencyHermitePolynomial_eq_comp] at hmult
  rwa [neutralNF556OriginalDualQuadraticRootMultiplicity
    (neutralNF557OriginalDualPolynomial a) hp
    (neutralNF567OriginalGroupOmega g)
    (neutralNF567OriginalGroupOmega_pos g)] at hmult

/-- The literal complete 242×242 ORIGINAL analytic odd-jet
left kernel now implies, at EACH of the 67 original frequencies,
ALL derivative orders up to its authentic m_g-1, and also the
separate genuine sinh negative node p_a(-1/4)=0.

This packages every source-specific jet into real analytic
polynomial-root obligations; it does NOT yet establish p_a=0
or assume source independence. -/
theorem neutralNF567OriginalFull242Kernel_all67BlocksAndPole
    (a : Fin 242 → ℝ)
    (hker : ∀ j : Fin 242,
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n j) = 0) :
    (∀ g : Fin 67, ∀ k : ℕ,
      k < (neutralNF567OriginalGroupAt g).2 →
      ((Polynomial.derivative^[k])
        (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
          (neutralNF567OriginalGroupOmega g) = 0) ∧
      (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) = 0 := by
  obtain ⟨hzeros, hpole⟩ :=
    neutralNF566OriginalFullActualOddJetKernel_rootObligations a hker
  exact ⟨fun g =>
    neutralNF567OriginalBlockHermiteJets_fromActualOscillators a hzeros g,
    hpole⟩

/-- The same full original analytic left kernel forces all 67
positive-frequency Hermite root multiplicities simultaneously,
conditional only on F_a ≠ 0, plus the true negative sinh-pole root. -/
theorem neutralNF567OriginalFull242Kernel_rootMultiplicities
    (a : Fin 242 → ℝ)
    (hker : ∀ j : Fin 242,
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n j) = 0)
    (hp : neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0) :
    (∀ g : Fin 67,
      (neutralNF567OriginalGroupAt g).2 ≤
        Polynomial.rootMultiplicity
          (neutralNF567OriginalGroupOmega g)
          (neutralNF565OriginalFrequencyHermitePolynomial a)) ∧
      (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) = 0 := by
  obtain ⟨hzeros, hpole⟩ :=
    neutralNF566OriginalFullActualOddJetKernel_rootObligations a hker
  exact ⟨neutralNF567OriginalAll67HermiteRootMultiplicities
    a hp hzeros, hpole⟩

/-- Complete authentic source 242×242 real left kernel forces
67 correctly indexed positive SQUARED-frequency multiplicity
bounds in p_a, plus the genuine negative sinh-pole root.

This is the exact ORIGINAL 68-node setup for NF553's
degree-242 Hermite obstruction; the simultaneous divisor and
nonzero F_a implications are the remaining global algebraic
gates. -/
theorem neutralNF567OriginalFull242Kernel_squaredDualRootMultiplicities
    (a : Fin 242 → ℝ)
    (hker : ∀ j : Fin 242,
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n j) = 0)
    (hp : neutralNF557OriginalDualPolynomial a ≠ 0)
    (hF : neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0) :
    (∀ g : Fin 67,
      (neutralNF567OriginalGroupAt g).2 ≤
        Polynomial.rootMultiplicity
          (neutralNF567OriginalGroupOmega g ^ 2)
          (neutralNF557OriginalDualPolynomial a)) ∧
      (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) = 0 := by
  obtain ⟨hzeros, hpole⟩ :=
    neutralNF566OriginalFullActualOddJetKernel_rootObligations a hker
  exact ⟨neutralNF567OriginalAll67SquaredDualRootMultiplicities
    a hp hF hzeros, hpole⟩

end
end WeilDefect
