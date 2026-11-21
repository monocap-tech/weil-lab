import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace WeilDefect

noncomputable section

open scoped BigOperators

/-!
PI007 independent finite Gamma physical-kernel pilot.

This module deliberately imports NO Phase IV source and asserts NO inverse
Fourier theorem. It packages elementary finite-kernel identities with only
Mathlib dependencies. The actual Zeta23 source-specific Gamma equivalence
requires a separate companion on the active IV source stack.

COMPILER STATUS: candidate, no compiled .olean or axiom audit attached.
-/

/-- Finite truncated real-place kernel associated to the exact
    Zeta23 digamma partial fractions a_n = n+1/4. -/
def pi007FiniteGammaKernel (N : ℕ) (u : ℝ) : ℝ :=
  ∑ n ∈ Finset.range N, Real.exp (-(2 * (n : ℝ) + 1 / 2) * |u|)

/-- No terms at truncation level zero. -/
theorem pi007FiniteGammaKernel_zero (u : ℝ) :
    pi007FiniteGammaKernel 0 u = 0 := by
  simp [pi007FiniteGammaKernel]

/-- Every new term in the truncated physical kernel is the exact
    exponential corresponding to the next digamma partial fraction. -/
theorem pi007FiniteGammaKernel_succ (N : ℕ) (u : ℝ) :
    pi007FiniteGammaKernel (N + 1) u =
      pi007FiniteGammaKernel N u +
        Real.exp (-(2 * (N : ℝ) + 1 / 2) * |u|) := by
  simp [pi007FiniteGammaKernel, Finset.sum_range_succ]

/-- Finite physical kernels are nonnegative. -/
theorem pi007FiniteGammaKernel_nonneg (N : ℕ) (u : ℝ) :
    0 ≤ pi007FiniteGammaKernel N u := by
  unfold pi007FiniteGammaKernel
  exact Finset.sum_nonneg (fun n _ => le_of_lt (Real.exp_pos _))

/-- The physical kernel is even even for complex non-even mixed tests. -/
theorem pi007FiniteGammaKernel_even (N : ℕ) (u : ℝ) :
    pi007FiniteGammaKernel N (-u) =
      pi007FiniteGammaKernel N u := by
  simp [pi007FiniteGammaKernel]

/-- Increasing the truncation level preserves pointwise nonnegativity. -/
theorem pi007FiniteGammaKernel_le_succ (N : ℕ) (u : ℝ) :
    pi007FiniteGammaKernel N u ≤
      pi007FiniteGammaKernel (N + 1) u := by
  rw [pi007FiniteGammaKernel_succ]
  exact le_add_of_nonneg_right (le_of_lt (Real.exp_pos _))

#print axioms pi007FiniteGammaKernel_zero
#print axioms pi007FiniteGammaKernel_succ
#print axioms pi007FiniteGammaKernel_nonneg
#print axioms pi007FiniteGammaKernel_even
#print axioms pi007FiniteGammaKernel_le_succ

end

end WeilDefect
