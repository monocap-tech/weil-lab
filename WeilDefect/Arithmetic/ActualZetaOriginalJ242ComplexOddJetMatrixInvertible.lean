import WeilDefect.Arithmetic.ActualZetaOriginalJ242OddJetMatrixInvertible
import WeilDefect.Arithmetic.ActualZetaOriginalJ242PhysicalMomentMap
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Determinant
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
NF567 — EXACT complexification of the original 242×242 REAL
odd-jet matrix of the frozen NF407 source.

The complex matrix has entries obtained by embedding the
actual real analytic derivatives of the original 241
sine/cosine monomial generators and the true sinh(x/2) pole.

This is a *finite matrix* ℝ→ℂ base-change result. It
does not use a newly chosen complex basis or determinant
numerics. Once NF566's real matrix IsUnit is accepted,
the complex matrix IsUnit follows from functoriality
of determinant under Complex.ofRealHom.

Source GLOBAL analytic independence is a further result
requiring differentiation of any globally vanishing complex
linear combination. Do not conflate it with this statement.
-/

/-- The actual original complexified source analytic odd-jet
matrix; entry (n,j) is the ofReal of the genuine real
(2n+1)-st derivative of the j-th original source generator. -/
def neutralNF567OriginalComplexOddJetMatrix :
    Matrix (Fin 242) (Fin 242) ℂ :=
  neutralNF560ActualOriginalOddJetMatrix.map Complex.ofRealHom

/-- Exact map on every original source entry; no
new complex-frequency generator is substituted. -/
theorem neutralNF567OriginalComplexOddJetMatrix_apply
    (n j : Fin 242) :
    neutralNF567OriginalComplexOddJetMatrix n j =
      (neutralNF560ActualOriginalOddJetMatrix n j : ℂ) := by
  rfl

/-- Base-changing the genuine original real source determinant
from ℝ to ℂ preserves its exact value, by the ring homomorphism
for the canonical real embedding. -/
theorem neutralNF567OriginalComplexOddJetMatrix_det :
    neutralNF567OriginalComplexOddJetMatrix.det =
      (neutralNF560ActualOriginalOddJetMatrix.det : ℂ) := by
  exact (RingHom.map_det Complex.ofRealHom
    neutralNF560ActualOriginalOddJetMatrix).symm

/-- The ORIGINAL complex 242×242 odd-jet matrix is invertible
whenever the NF566 actual original real matrix theorem compiles.
The mathematical field-extension argument is exact. -/
theorem neutralNF567OriginalComplexOddJetMatrix_isUnit :
    IsUnit neutralNF567OriginalComplexOddJetMatrix := by
  have hreal : IsUnit neutralNF560ActualOriginalOddJetMatrix :=
    neutralNF566OriginalOddJetMatrix_isUnit
  have hdet : IsUnit neutralNF560ActualOriginalOddJetMatrix.det :=
    (Matrix.isUnit_iff_isUnit_det _).mp hreal
  have hdetComplex :
      IsUnit (neutralNF560ActualOriginalOddJetMatrix.det : ℂ) :=
    hdet.map Complex.ofRealHom
  apply (Matrix.isUnit_iff_isUnit_det _).mpr
  rw [neutralNF567OriginalComplexOddJetMatrix_det]
  exact hdetComplex

/-- Every actual complex coefficient vector annihilating the
authentic original complexified analytic odd-jet matrix is zero.
This is source-exact COMPLEX finite matrix rank, not
a claim of global analytic functional independence. -/
theorem neutralNF567OriginalComplexOddJetMatrix_kernel_trivial
    (d : Fin 242 → ℂ)
    (hd : d ᵥ* neutralNF567OriginalComplexOddJetMatrix = 0) :
    d = 0 := by
  have hinj : Function.Injective
      neutralNF567OriginalComplexOddJetMatrix.vecMul :=
    Matrix.vecMul_injective_iff_isUnit.mpr
      neutralNF567OriginalComplexOddJetMatrix_isUnit
  exact hinj (by simpa using hd)

/-- Historical physical source coefficients evaluated as complex
functions are EXACTLY the original real J242 functions mapped into
complex scalars. This is just the source data identity, not a
regularity or uniqueness hypothesis. -/
theorem neutralNF567OriginalComplexGenerator_eq_real
    (j : Fin 242) (x : ℝ) :
    neutralNF546OriginalComplexGenerator j x =
      (nf545OriginalSelectedRealGenerator j x : ℂ) := by
  rfl

end
end WeilDefect
