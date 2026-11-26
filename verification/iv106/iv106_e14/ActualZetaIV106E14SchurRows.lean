import WeilDefect.Arithmetic.ActualZetaIV106E13TerminalSchur
import Mathlib.LinearAlgebra.Finsupp.LinearCombination

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate BigOperators

/-- Riesz representatives of the literal constraint rows, in the logarithmic
Hilbert metric rather than in an unrelated physical trial metric. -/
def neutralIV106E14Row (k : ℕ) (hk : 0 < k)
    (j : neutralIV106C3Index 665 k) : neutralIV106E13H :=
  (InnerProductSpace.toDual ℂ neutralIV106E13H).symm
    ((ContinuousLinearMap.proj j).comp (neutralIV106C3Constraints 665 k hk))

theorem neutralIV106E14Row_pair (k : ℕ) (hk : 0 < k)
    (j : neutralIV106C3Index 665 k) (q : neutralIV106E13H) :
    inner ℂ (neutralIV106E14Row k hk j) q =
      neutralIV106C3Constraints 665 k hk q j := by
  simp [neutralIV106E14Row, InnerProductSpace.toDual_symm_apply]

def neutralIV106E14Span (k : ℕ) (hk : 0 < k) : Submodule ℂ neutralIV106E13H :=
  Submodule.span ℂ (Set.range (neutralIV106E14Row k hk))

/-- Exact annihilator identity for all constraint rows. -/
theorem neutralIV106E14Kernel_eq (k : ℕ) (hk : 0 < k) :
    neutralIV106E12Kernel k hk = (neutralIV106E14Span k hk)ᗮ := by
  ext q
  constructor
  · intro hq
    have hz : neutralIV106C3Constraints 665 k hk q = 0 := hq
    have hs : neutralIV106E14Span k hk ≤ (innerSL ℂ q).ker := by
      apply Submodule.span_le.mpr
      rintro _ ⟨j,rfl⟩
      change inner ℂ q (neutralIV106E14Row k hk j) = 0
      apply inner_eq_zero_symm.mpr
      rw [neutralIV106E14Row_pair, hz]
      rfl
    apply (Submodule.mem_orthogonal _ _).mpr
    intro r hr
    have h : inner ℂ q r = 0 := hs hr
    exact inner_eq_zero_symm.mp h
  · intro hq
    change neutralIV106C3Constraints 665 k hk q = 0
    funext j
    change neutralIV106C3Constraints 665 k hk q j = 0
    rw [← neutralIV106E14Row_pair]
    exact (Submodule.mem_orthogonal _ _).mp hq _
      (Submodule.subset_span ⟨j,rfl⟩)

/-- No independence premise: the receiving sector is exactly the row span. -/
theorem neutralIV106E14Finite_eq (k : ℕ) (hk : 0 < k) :
    neutralIV106E13Finite k hk = neutralIV106E14Span k hk := by
  unfold neutralIV106E13Finite
  rw [neutralIV106E14Kernel_eq]
  letI : FiniteDimensional ℂ (neutralIV106E14Span k hk) :=
    FiniteDimensional.span_of_finite ℂ (Set.finite_range _)
  exact (neutralIV106E14Span k hk).orthogonal_orthogonal

def neutralIV106E14LiftedRow (k : ℕ) (hk : 0 < k)
    (j : neutralIV106C3Index 665 k) : neutralIV106E13Finite k hk :=
  ⟨neutralIV106E14Row k hk j, by
    rw [neutralIV106E14Finite_eq]
    exact Submodule.subset_span ⟨j,rfl⟩⟩

/-- Surjectivity of the possibly redundant row synthesis map. -/
theorem neutralIV106E14Synthesis (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) :
    ∃ c : neutralIV106C3Index 665 k → ℂ,
      (∑ j, c j • neutralIV106E14LiftedRow k hk j) = y := by
  have hy : y.val ∈ neutralIV106E14Span k hk := by
    rw [← neutralIV106E14Finite_eq]
    exact y.property
  obtain ⟨c,hc⟩ := Submodule.mem_span_range_iff_exists_fun.mp hy
  refine ⟨c,Subtype.ext ?_⟩
  simpa [neutralIV106E14LiftedRow] using hc

/-- A general exact complex coefficient expansion, including conjugation. -/
theorem neutralIV106E14Gram {H J : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [Fintype J]
    (W : H →L[ℂ] H) (r : J → H) (c : J → ℂ) :
    inner ℂ (∑ j, c j • r j) (W (∑ j, c j • r j)) =
      ∑ i, ∑ j, conj (c i)*c j*inner ℂ (r i) (W (r j)) := by
  classical
  simp only [map_sum, map_smul, sum_inner, inner_sum, inner_smul_left,
    inner_smul_right]
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  simp only [Complex.star_def]
  ring

/-- The response is continuous linear, with exactly the same inverse as E13. -/
def neutralIV106E14ResponseMap (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk) :
    neutralIV106E13Finite k hk →L[ℂ] neutralIV106E12Kernel k hk :=
  e.symm.toContinuousLinearMap ∘L
    (ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL) ∘L
    (neutralActualZetaLogWeilFormOperator (11/10)) ∘L
    (neutralIV106E13Finite k hk).subtypeL

def neutralIV106E14SchurMatrix (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (i j : neutralIV106C3Index 665 k) : ℂ :=
  inner ℂ (neutralIV106E14Row k hk i)
    (neutralActualZetaLogWeilFormOperator (11/10) (neutralIV106E14Row k hk j)) -
  inner ℂ (neutralIV106E14ResponseMap k hk e (neutralIV106E14LiftedRow k hk i)).val
    (neutralActualZetaLogWeilFormOperator (11/10)
      (neutralIV106E14ResponseMap k hk e (neutralIV106E14LiftedRow k hk j)).val)

/-- Exact Schur matrix representation of the actual receiving sector. -/
theorem neutralIV106E14Matrix_energy (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (c : neutralIV106C3Index 665 k → ℂ) :
    neutralIV106E13Schur k hk e (∑ j, c j • neutralIV106E14LiftedRow k hk j) =
      (∑ i, ∑ j, conj (c i)*c j*neutralIV106E14SchurMatrix k hk e i j).re := by
  classical
  let W := neutralActualZetaLogWeilFormOperator (11/10)
  let r := neutralIV106E14Row k hk
  let u (j : neutralIV106C3Index 665 k) :=
    (neutralIV106E14ResponseMap k hk e (neutralIV106E14LiftedRow k hk j)).val
  let y := ∑ j, c j • neutralIV106E14LiftedRow k hk j
  have hy : y.val = ∑ j, c j • r j := by
    change (neutralIV106E13Finite k hk).subtypeL y = _
    simp only [y, map_sum, map_smul]
    rfl
  have hu : (neutralIV106E13Response k hk e y).val = ∑ j, c j • u j := by
    change (neutralIV106E12Kernel k hk).subtypeL
      (neutralIV106E14ResponseMap k hk e y) = _
    simp only [y, map_sum, map_smul]
    rfl
  change neutralIV106E13Schur k hk e y = _
  unfold neutralIV106E13Schur neutralIV106E13Energy
  rw [hy,hu,neutralIV106E14Gram,neutralIV106E14Gram,← Complex.sub_re]
  congr 1
  simp only [neutralIV106E14SchurMatrix, mul_sub, Finset.sum_sub_distrib]
  rfl

/-- The literal (possibly singular) row-coordinate matrix is sufficient and
necessary for the finite Schur positivity obligation. -/
theorem neutralIV106E14Matrix_iff (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk) :
    (∀ y : neutralIV106E13Finite k hk, 0 ≤ neutralIV106E13Schur k hk e y) ↔
    (∀ c : neutralIV106C3Index 665 k → ℂ,
      0 ≤ (∑ i, ∑ j, conj (c i)*c j*neutralIV106E14SchurMatrix k hk e i j).re) := by
  constructor
  · intro h c
    rw [← neutralIV106E14Matrix_energy]
    exact h _
  · intro h y
    obtain ⟨c,hc⟩ := neutralIV106E14Synthesis k hk y
    rw [← hc, neutralIV106E14Matrix_energy]
    exact h c

#print axioms neutralIV106E14Row_pair
#print axioms neutralIV106E14Kernel_eq
#print axioms neutralIV106E14Finite_eq
#print axioms neutralIV106E14Synthesis
#print axioms neutralIV106E14Gram
#print axioms neutralIV106E14Matrix_energy
#print axioms neutralIV106E14Matrix_iff
end
end WeilDefect
