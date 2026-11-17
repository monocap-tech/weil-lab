import WeilDefect.Arithmetic.ActualZetaOriginalJ242WeightedListRootBudget
import WeilDefect.Arithmetic.ActualZetaOriginalJ242Exact68NodeBudget
import WeilDefect.Arithmetic.ActualZetaOriginalJ242FrequencyBlockHermiteMultiplicity
import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualPoleOddDerivatives
import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialCoefficient
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF566 — THE EXACT ORIGINAL 242-SOURCE FINITE-DIMENSIONAL LEFT
KERNEL, not an assumed independent generator family.

Given a real row-vector a in the left kernel of the authentic
242-by-242 matrix A[n,j] = (d/dx)^(2n+1) j_j(0):
* all 241 true oscillators give all original 67 frequency block
  Hermite derivatives, by the source-indexed NF564/NF565 bridge;
* the index-241 true j_241=sinh(x/2) gives p_a(-1/4)=0, by
  the independently Lean-accepted NF560 source theorem;
* the 68 original distinct real nodes demand total root
  multiplicity 242, while deg p_a ≤241;
* Mathlib's actual roots multiset yields p_a=0;
* NF558 exact original coefficient injectivity yields a=0.

This closes the mathematical dependency graph AT THE SOURCE
level as a candidate Lean theorem. It depends on NF561–NF565
compiler-pending analytic/aggregate results. It must NOT be
described as compiler-accepted until the new focused Actions
job succeeds.

This is a finite original J242 independence result ONLY;
the full RH-facing signed Weil inequality remains separate.
-/

/-- All 68 exact ORIGINAL weighted source nodes satisfy their
individual multiplicity demands if the genuine analytic
242-by-242 original odd-jet matrix has a left-kernel vector a,
provided the original dual polynomial p_a is nonzero. -/
theorem neutralNF566ActualOriginal68Nodes_rootDemands
    (a : Fin 242 → ℝ)
    (hp : neutralNF557OriginalDualPolynomial a ≠ 0)
    (hkernel : ∀ j : Fin 242,
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n j) = 0) :
    ∀ q ∈ neutralNF565Actual68WeightedNodes,
      q.2 ≤ rootMultiplicity q.1
        (neutralNF557OriginalDualPolynomial a) := by
  intro q hq
  have hosc : ∀ i : Fin 241,
      (∑ n : Fin 242,
        a n * (iteratedDeriv (2 * n.val + 1)
          (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) = 0 := by
    intro i
    exact hkernel ⟨i.val, by omega⟩
  have hpole :
      (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) = 0 :=
    neutralNF560OriginalMatrixPoleKernelForcesRoot a
      (hkernel ⟨241, by omega⟩)
  unfold neutralNF565Actual68WeightedNodes at hq
  rcases List.mem_append.mp hq with hoscNode | hpoleNode
  · unfold neutralNF565Actual67WeightedSquaredNodes at hoscNode
    obtain ⟨g, hg, hqg⟩ := List.mem_map.mp hoscNode
    subst q
    have hm :=
      neutralNF565OriginalFrequencyBlock_squaredRootMultiplicity
        a hp g hg hosc
    have hcast : (((g.1 ^ 2 : ℚ) : ℝ)) = (g.1 : ℝ) ^ 2 := by
      norm_cast
    have hnode :
        (2 * Real.pi) ^ 2 * ((g.1 ^ 2 : ℚ) : ℝ) =
          (2 * Real.pi * (g.1 : ℝ)) ^ 2 := by
      rw [hcast]
      ring
    simpa only [Prod.fst, Prod.snd, hnode] using hm
  · have hpair : q = (-(1 / 4 : ℝ),1) := by
      simpa only [List.mem_singleton] using hpoleNode
    subst q
    have hmult : 0 <
        rootMultiplicity (-(1 / 4 : ℝ))
          (neutralNF557OriginalDualPolynomial a) :=
      Polynomial.rootMultiplicity_pos'.mpr ⟨hp, hpole⟩
    change 1 ≤ rootMultiplicity (-(1 / 4 : ℝ))
      (neutralNF557OriginalDualPolynomial a)
    omega

/-- Original 242×242 REAL odd-jet left-kernel theorem.

Every coordinate of the ORIGINAL source (241 exact
sine/cosine monomials + one real sinh pole) participates.
No sampled determinant, surrogate frequency, generic
assumed matrix rank or arbitrary Gram basis is substituted. -/
theorem neutralNF566ActualOriginalOddJet_leftKernel_eq_zero
    (a : Fin 242 → ℝ)
    (hkernel : ∀ j : Fin 242,
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n j) = 0) :
    a = 0 := by
  by_cases hp : neutralNF557OriginalDualPolynomial a = 0
  · exact neutralNF558OriginalDualPolynomial_eq_zero a hp
  · have hroots :=
      neutralNF566ActualOriginal68Nodes_rootDemands a hp hkernel
    have hdegree :
        (neutralNF557OriginalDualPolynomial a).natDegree <
          (neutralNF565Actual68WeightedNodes.map Prod.snd).sum := by
      rw [neutralNF565Actual68WeightedNodes_budget]
      exact neutralNF557OriginalDualPolynomial_natDegree_lt a
    have hzero :=
      neutralNF566WeightedNodeListDegreeStop
        (neutralNF557OriginalDualPolynomial a)
        neutralNF565Actual68WeightedNodes
        neutralNF565Actual68WeightedNodes_nodup
        hroots hdegree
    exact False.elim (hp hzero)

end
end WeilDefect
