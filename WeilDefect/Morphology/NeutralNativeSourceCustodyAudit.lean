import WeilDefect.Morphology.NeutralNativeLogFormAttachment
import WeilDefect.Morphology.NeutralLogBackgroundSourceAttachment

namespace WeilDefect

noncomputable section

open scoped ComplexConjugate BigOperators

/-- Custody countercheck only: the current shell record accepts an
arithmetic grid for every count function, without checking a zeta-zero
equation, exhaustive enumeration, or multiplicity/reflection dictionary.
This definition is not asserted to enumerate zeta zeros. -/
def nativeShellArithmeticGrid (count : ℕ → ℕ) :
    ActualProblemOneShellData count where
  gamma g := (((g.1 : ℝ) + 1 : ℝ) : ℂ)
  strip g := by simp
  shell_height g := by
    simp only [Complex.ofReal_re]
    rw [abs_of_nonneg (by positivity : 0 ≤ (g.1 : ℝ) + 1)]

/-- Every arithmetic-grid ordinate is fixed by conjugation. -/
theorem nativeShellArithmeticGrid_conjugate
    (count : ℕ → ℕ) (g : ZetaShellIndex count) :
    conj ((nativeShellArithmeticGrid count).gamma g) =
      (nativeShellArithmeticGrid count).gamma g := by
  simp only [nativeShellArithmeticGrid, Complex.conj_ofReal]

/-- The concrete negative pair source vanishes for each grid ordinate.
This is an actual source calculation, not an assumed representation. -/
theorem nativeShellArithmeticGrid_negativeSource
    (count : ℕ → ℕ) (a : ℝ) (g : ZetaShellIndex count) :
    neutralLogNegativePairSource a
      ((nativeShellArithmeticGrid count).gamma g) = 0 := by
  simp only [neutralLogNegativePairSource,
    nativeShellArithmeticGrid_conjugate, sub_self, smul_zero]

/-- Its actual selected negative rank-one operator also vanishes. -/
theorem nativeShellArithmeticGrid_selectedOperator
    (count : ℕ → ℕ) (a : ℝ) (g : ZetaShellIndex count) :
    neutralLogSelectedPairOperator a
      ((nativeShellArithmeticGrid count).gamma g) = 0 := by
  simp [neutralLogSelectedPairOperator, nativeShellArithmeticGrid_negativeSource]

/-- Any finite packet chosen from this admissible shell record has zero
actual negative operator. Shell estimates alone do not encode a selected
negative divisor or its reduced compensator. -/
theorem nativeShellArithmeticGrid_finiteSelectedOperator
    (count : ℕ → ℕ) (a : ℝ) {ι : Type*} [Fintype ι]
    (packet : ι → ZetaShellIndex count) :
    neutralLogFiniteSelectedOperator a
      (fun i => (nativeShellArithmeticGrid count).gamma (packet i)) = 0 := by
  simp [neutralLogFiniteSelectedOperator, nativeShellArithmeticGrid_selectedOperator]

end

end WeilDefect
