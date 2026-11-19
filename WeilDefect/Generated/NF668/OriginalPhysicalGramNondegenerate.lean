import WeilDefect.Generated.NF665.OriginalPhysicalCoercivity
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramPositiveDefinite

namespace WeilDefect

/-!
NF668: certified consequences for the authentic original NF606
physical integral Gram block on indices 0,...,13 and pole 241.

The decisive premise is the unconditional, Lean-audited NF665
10^-60 theorem. No new numerical matrix, solver or hypothesis is used.
The result concerns this 15-source subspace, not all 242 sources.
-/

noncomputable section
open Finset

/-- The actual symmetric original physical matrix, not the NF659
integer center or the transformed/rounded numerical surrogate. -/
def nf668OriginalPhysicalGram : Matrix (Fin 15) (Fin 15) ℝ :=
  neutralNF661PhysicalH

theorem nf668OriginalPhysicalGram_symmetric (i j : Fin 15) :
    nf668OriginalPhysicalGram i j =
      nf668OriginalPhysicalGram j i :=
  neutralNF661PhysicalH_symm i j

/-- The exact coercivity statement is available in this stable
source-specific module without a generic change-of-basis hypothesis. -/
theorem nf668OriginalPhysical_lowerBound (x : Fin 15 → ℝ) :
    ((1 : ℝ) / (10 ^ 60 : ℝ)) * neutralNF661SqNorm x ≤
      neutralNF661Quadratic nf668OriginalPhysicalGram x :=
  nf665OriginalPhysical_coercivity x

/-- Nonzero original physical source coefficients have strictly
positive original physical quadratic energy. -/
theorem nf668OriginalPhysical_positiveDefinite
    (x : Fin 15 → ℝ) (hx : x ≠ 0) :
    0 < neutralNF661Quadratic nf668OriginalPhysicalGram x := by
  exact neutralNF668Quadratic_pos_of_coercivity
    nf668OriginalPhysicalGram
    ((1 : ℝ) / (10 ^ 60 : ℝ)) (by positivity)
    nf668OriginalPhysical_lowerBound x hx

/-- The exact original 15-dimensional physical Gram map has no
nonzero null vector. -/
theorem nf668OriginalPhysical_kernelZero
    (x : Fin 15 → ℝ)
    (hzero : ∀ i : Fin 15,
      neutralNF668GramApply nf668OriginalPhysicalGram x i = 0) :
    x = 0 :=
  neutralNF668GramKernel_trivial
    nf668OriginalPhysicalGram
    ((1 : ℝ) / (10 ^ 60 : ℝ)) (by positivity)
    nf668OriginalPhysical_lowerBound x hzero

/-- Injectivity is proved for the original integral-defined
physical 15-source moment operator itself. -/
theorem nf668OriginalPhysical_applyInjective :
    Function.Injective
      (neutralNF668GramApply nf668OriginalPhysicalGram) :=
  neutralNF668GramApply_injective
    nf668OriginalPhysicalGram
    ((1 : ℝ) / (10 ^ 60 : ℝ)) (by positivity)
    nf668OriginalPhysical_lowerBound

/-- A prescribed right-hand side cannot have two distinct original
15-source physical Gram solutions. No 242-source solve is claimed. -/
theorem nf668OriginalPhysical_solveUnique
    (b x y : Fin 15 → ℝ)
    (hx : neutralNF668GramApply nf668OriginalPhysicalGram x = b)
    (hy : neutralNF668GramApply nf668OriginalPhysicalGram y = b) :
    x = y :=
  nf668OriginalPhysical_applyInjective (hx.trans hy.symm)

/-- Re-express the certified row action using the genuine original
integral H, preserving the original oscillator and pole source IDs. -/
theorem nf668OriginalPhysical_actionIsIntegral
    (x : Fin 15 → ℝ) (i : Fin 15) :
    neutralNF668GramApply nf668OriginalPhysicalGram x i =
      ∑ j : Fin 15,
        neutralNF606PhysicalH (neutralNF661Source i)
          (neutralNF661Source j) * x j := rfl

#print axioms nf668OriginalPhysical_lowerBound
#print axioms nf668OriginalPhysical_positiveDefinite
#print axioms nf668OriginalPhysical_kernelZero
#print axioms nf668OriginalPhysical_applyInjective
#print axioms nf668OriginalPhysical_solveUnique
#print axioms nf668OriginalPhysical_actionIsIntegral

end
end WeilDefect
