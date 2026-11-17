import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualOscillatorHermiteBridge
import WeilDefect.Arithmetic.ActualZetaOriginalJ242HermiteDerivativeMultiplicity
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

/-- Original group at an *actual* one of the 67 frozen rational
NF407 frequency/multiplicity pairs, no reordering. -/
def neutralNF567OriginalGroupAt (g : Fin 67) : ℚ × ℕ :=
  nf545OriginalSelectedFrequencyGroups[g.val]'(by
    simpa only [nf545OriginalFrequencyGroupCount] using g.isLt)

/-- Real angular frequency of the frozen g-th original group. -/
def neutralNF567OriginalGroupOmega (g : Fin 67) : ℝ :=
  2 * Real.pi * ((neutralNF567OriginalGroupAt g).1 : ℝ)

/-- Every frozen source group has strictly positive multiplicity;
this is the exact 67-element original NF407 table, not a
hypothetical collection of blocks. -/
private theorem neutralNF567OriginalAllGroupMultiplicities_pos :
    ∀ g : Fin 67, 0 < (neutralNF567OriginalGroupAt g).2 := by
  decide +kernel

theorem neutralNF567OriginalGroupAt_multiplicity_pos (g : Fin 67) :
    0 < (neutralNF567OriginalGroupAt g).2 :=
  neutralNF567OriginalAllGroupMultiplicities_pos g

/-- Direct exact ORIGINAL 67-block multiplicity budget from the
frozen NF407 table: 241 oscillator directions before the sinh
pole, not an abstract Hermite interpolation dimension. -/
theorem neutralNF567OriginalAll67GroupMultiplicities_sum :
    (∑ g : Fin 67, (neutralNF567OriginalGroupAt g).2) = 241 := by
  decide +kernel

/-- For every genuine frequency group g and EVERY k in its
original range, recover a specific genuine Fin241 oscillator
column carrying exactly (f_g,k). This is the source-index
completeness hypothesis required by the 67-block Hermite argument,
proved rather than assumed. -/
theorem neutralNF567OriginalEveryBlockOrder_isActualSource
    (g : Fin 67) (k : ℕ)
    (hk : k < (neutralNF567OriginalGroupAt g).2) :
    ∃ i : Fin 241,
      nf545OriginalOscillatorNodeAt i =
        ((neutralNF567OriginalGroupAt g).1, k) := by
  have hg :
      neutralNF567OriginalGroupAt g ∈
        nf545OriginalSelectedFrequencyGroups := by
    unfold neutralNF567OriginalGroupAt
    exact List.get_mem _ _
  have hr :
      k ∈ List.range (neutralNF567OriginalGroupAt g).2 :=
    List.mem_range.mpr hk
  have hm :
      ((neutralNF567OriginalGroupAt g).1, k) ∈
        nf545OriginalSelectedOscillatorNodes := by
    unfold nf545OriginalSelectedOscillatorNodes
    apply List.mem_flatMap.mpr
    refine ⟨neutralNF567OriginalGroupAt g, hg, ?_⟩
    apply List.mem_map.mpr
    exact ⟨k, hr, rfl⟩
  obtain ⟨idx, hidx⟩ := List.mem_iff_get.mp hm
  have hbound : idx.val < 241 := by
    simpa only [nf545OriginalSelectedOscillatorNodes_length] using idx.isLt
  refine ⟨⟨idx.val, hbound⟩, ?_⟩
  simpa only [nf545OriginalOscillatorNodeAt, List.get_eq_getElem] using hidx

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

end
end WeilDefect
