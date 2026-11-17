import WeilDefect.Arithmetic.ActualZetaOriginalJ242RealOddJetLeftKernel
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
NF566 — Transfer from the fully original real 242×242 analytic
odd-jet left-kernel certificate to actual square-matrix
invertibility over ℝ.

This file does not assume a matrix with generic independent
columns. It uses the literal NF560 analytic matrix whose entries
are the initial odd derivatives of the unchanged original NF407
241 trigonometric oscillators and genuine last sinh(x/2) source.

The proof must first obtain actual compiler acceptance of the
NF566 original-root degree contradiction; do not claim
independence or Gram strictness from an unverified candidate.
-/

/-- If a real row vector annihilates the authentic original
242×242 odd-jet matrix, that row vector is zero.
This is the matrix representation of the original real
left-kernel theorem, without numerical rank evaluation. -/
theorem neutralNF566OriginalOddJetMatrix_vecMul_kernel_trivial
    (a : Fin 242 → ℝ)
    (ha : a ᵥ* neutralNF560ActualOriginalOddJetMatrix = 0) :
    a = 0 := by
  apply neutralNF566ActualOriginalOddJet_leftKernel_eq_zero a
  intro j
  have hj := congrArg (fun v : Fin 242 → ℝ => v j) ha
  simpa only [Matrix.vecMul, dotProduct, Pi.zero_apply] using hj

/-- The real vecMul map for the authentic ORIGINAL odd-jet matrix
is injective; this follows from the just-established actual
242-source Hermite left-kernel contradiction, not a numerical
determinant or independent basis axiom. -/
theorem neutralNF566OriginalOddJetMatrix_vecMul_injective :
    Function.Injective neutralNF560ActualOriginalOddJetMatrix.vecMul := by
  intro a b hab
  have hzero :
      (a - b) ᵥ* neutralNF560ActualOriginalOddJetMatrix = 0 := by
    rw [Matrix.sub_vecMul, hab, sub_self]
  exact sub_eq_zero.mp
    (neutralNF566OriginalOddJetMatrix_vecMul_kernel_trivial
      (a - b) hzero)

/-- ORIGINAL real odd-jet matrix invertibility: the complete
analytic NF407 242 source has a square nonsingular initial-odd-jet
matrix. This is a source-conditional compilation target whose
upstream source Hermite chain must pass Lean first. -/
theorem neutralNF566OriginalOddJetMatrix_isUnit :
    IsUnit neutralNF560ActualOriginalOddJetMatrix := by
  exact Matrix.vecMul_injective_iff_isUnit.mp
    neutralNF566OriginalOddJetMatrix_vecMul_injective

end
end WeilDefect
