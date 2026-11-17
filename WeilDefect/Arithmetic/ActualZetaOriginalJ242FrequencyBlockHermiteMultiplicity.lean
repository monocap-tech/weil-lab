import WeilDefect.Arithmetic.ActualZetaOriginalJ242SourceIndexedHermiteBridge
import WeilDefect.Arithmetic.ActualZetaOriginalJ242HermiteDerivativeMultiplicity
import WeilDefect.Arithmetic.ActualZetaOriginalJ242QuadraticRootMultiplicity
import Mathlib.Algebra.Polynomial.Expand
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF565 — the first complete EXACT ORIGINAL frequency-BLOCK assembly
between the real NF407 list and the 242-row Hermite polynomial.

Earlier NF564 constructed a candidate true analytic odd-jet
left-kernel → kth derivative equality for every source index
i:Fin 241. Here the important distinction is that each original
rational frequency group (f,m) supplies ALL orders 0,...,m-1
through its historical contiguous List.range source expansion.

This file gives a source-exact theorem producing an actual
Fin 241 source index from every original group and every k<m.
It then transfers all source column left-kernel equations to
Hermite derivative vanishing, and invokes the already-accepted
NF554 and NF556 generic multiplicity theorems to obtain the
full required ORIGINAL m_f multiplicity at each real node
(2*pi*f)^2, when p_a ≠ 0.

No source independence, physical Gram positivity, or fictitious
67th+ oscillator is assumed. True sinh at -1/4 is separate.
-/

/-- Every unchanged ORIGINAL frequency block (f,m), and every
monomial order k<m, occurs as one of the original 241
oscillator rows. This closes the crucial per-block source
multiplicity coverage gap, rather than assuming it. -/
theorem neutralNF565OriginalFrequencyBlock_hasSourceIndex
    (g : ℚ × ℕ)
    (hg : g ∈ nf545OriginalSelectedFrequencyGroups)
    (k : ℕ) (hk : k < g.2) :
    ∃ i : Fin 241, nf545OriginalOscillatorNodeAt i = (g.1,k) := by
  have hmem : (g.1,k) ∈ nf545OriginalSelectedOscillatorNodes := by
    apply List.mem_flatMap.mpr
    refine ⟨g, hg, ?_⟩
    apply List.mem_map.mpr
    exact ⟨k, List.mem_range.mpr hk, rfl⟩
  obtain ⟨i, hi⟩ := List.mem_iff_get.mp hmem
  have hi241 : i.val < 241 := by
    simpa only [nf545OriginalSelectedOscillatorNodes_length] using i.isLt
  refine ⟨⟨i.val,hi241⟩, ?_⟩
  simpa only [nf545OriginalOscillatorNodeAt, List.get_eq_getElem] using hi

/-- One genuine original frequency group forces ALL of its
polynomial Hermite derivative equations, provided the actual
242×241 oscillator columns satisfy the source left-kernel
equations. This is the source-specific premise, not a fabricated
generic 67-node interpolation assumption. -/
theorem neutralNF565OriginalFrequencyBlock_allHermiteJets
    (a : Fin 242 → ℝ)
    (g : ℚ × ℕ)
    (hg : g ∈ nf545OriginalSelectedFrequencyGroups)
    (hcolumns : ∀ i : Fin 241,
      (∑ n : Fin 242,
        a n * (iteratedDeriv (2 * n.val + 1)
          (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) = 0) :
    ∀ k : ℕ, k < g.2 →
      eval (2 * Real.pi * (g.1 : ℝ))
        ((Polynomial.derivative^[k])
          (neutralNF564OriginalDualOddPolynomial a)) = 0 := by
  intro k hk
  obtain ⟨i, hi⟩ :=
    neutralNF565OriginalFrequencyBlock_hasSourceIndex g hg k hk
  have hroot :=
    neutralNF564ActualOriginalOscillator_kernelForcesHermiteRoot
      a i (hcolumns i)
  simpa only [neutralNF562OriginalOscillatorOmega,
    neutralNF562OriginalOscillatorOrder, hi] using hroot

/-- Each *source-actual* rational frequency group is strictly
positive in the original 67-entry signature. -/
theorem neutralNF565OriginalFrequencyBlock_positive
    (g : ℚ × ℕ)
    (hg : g ∈ nf545OriginalSelectedFrequencyGroups) :
    0 < (g.1 : ℝ) := by
  have hpos :=
    nf545OriginalFrequenciesPositive
  have hp : 0 < g.1 := by
    have : g.1 ∈
        nf545OriginalSelectedFrequencyGroups.map Prod.fst :=
      List.mem_map.mpr ⟨g, hg, rfl⟩
    exact (List.forall_iff_forall_mem.mp hpos) _ this
  exact_mod_cast hp

/-- The authentic positive real angular frequency 2πf of
every original oscillator group. -/
theorem neutralNF565OriginalFrequencyBlock_omega_positive
    (g : ℚ × ℕ)
    (hg : g ∈ nf545OriginalSelectedFrequencyGroups) :
    0 < 2 * Real.pi * (g.1 : ℝ) := by
  have hf := neutralNF565OriginalFrequencyBlock_positive g hg
  positivity

/-- F_a=X*p_a(X²) cannot be identically zero when the actual
original signed dual p_a is nonzero. This uses Mathlib's
INJECTIVE quadratic polynomial expansion, not an independence
premise on the original source functions. -/
theorem neutralNF565OriginalOddDual_nonzero
    (a : Fin 242 → ℝ)
    (hp : neutralNF557OriginalDualPolynomial a ≠ 0) :
    neutralNF564OriginalDualOddPolynomial a ≠ 0 := by
  rw [neutralNF564OriginalDualOddPolynomial_eq_quadratic]
  have hcomp :
      (neutralNF557OriginalDualPolynomial a).comp (X ^ 2) ≠ 0 := by
    change Polynomial.expand ℝ 2
      (neutralNF557OriginalDualPolynomial a) ≠ 0
    exact (Polynomial.expand_ne_zero (R := ℝ)
      (by norm_num : 0 < 2)).mpr hp
  exact mul_ne_zero Polynomial.X_ne_zero hcomp

/-- ORIGINAL 67-BLOCK ROOT MULTIPLICITY:
For each historical frequency block g=(f,m), the original
242-row analytic left-kernel equations imply multiplicity
at least m at the TRUE squared frequency (2πf)², for the
nonzero original dual polynomial p_a.

This is the exact source-specific composition of the
NF564 analytic-to-Hermite identity with the already
compiler-accepted NF554 and NF556 algebraic results.
The overall result is CANDIDATE Lean until NF565 CI passes. -/
theorem neutralNF565OriginalFrequencyBlock_squaredRootMultiplicity
    (a : Fin 242 → ℝ)
    (hp : neutralNF557OriginalDualPolynomial a ≠ 0)
    (g : ℚ × ℕ)
    (hg : g ∈ nf545OriginalSelectedFrequencyGroups)
    (hcolumns : ∀ i : Fin 241,
      (∑ n : Fin 242,
        a n * (iteratedDeriv (2 * n.val + 1)
          (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) = 0) :
    g.2 ≤ Polynomial.rootMultiplicity
      ((2 * Real.pi * (g.1 : ℝ)) ^ 2)
        (neutralNF557OriginalDualPolynomial a) := by
  let p := neutralNF557OriginalDualPolynomial a
  let F := neutralNF564OriginalDualOddPolynomial a
  let ω := 2 * Real.pi * (g.1 : ℝ)
  have hF : F ≠ 0 := neutralNF565OriginalOddDual_nonzero a hp
  have hjets : ∀ k : ℕ, k < g.2 →
      ((⇑(Polynomial.derivative : Polynomial ℝ →ₗ[ℝ] Polynomial ℝ))^[k] F).IsRoot ω := by
    intro k hk
    change eval ω ((Polynomial.derivative^[k]) F) = 0
    exact neutralNF565OriginalFrequencyBlock_allHermiteJets a g hg hcolumns k hk
  have hmult : g.2 ≤ rootMultiplicity ω F :=
    neutralNF554HermiteRootMultiplicity_of_vanishingJets
      F ω g.2 hF hjets
  have hquad := neutralNF556OriginalDualQuadraticRootMultiplicity
    p hp ω (neutralNF565OriginalFrequencyBlock_omega_positive g hg)
  rw [← neutralNF564OriginalDualOddPolynomial_eq_quadratic] at hquad
  rw [hquad] at hmult
  exact hmult

end
end WeilDefect
