import WeilDefect.Generated.NF669.OriginalPhysicalComplementDictionary
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramSchurAlgebra

namespace WeilDefect

/-!
NF670: exact full 242-original-source physical quadratic form, reindexed
through the NF669 genuine 15+227 original generator equivalence.

This is not a change of generators and not the rational NF658 Gram
preconditioner: every entry is the actual original NF606 integral.
-/

noncomputable section
open Finset

/-- A sum over the original 242 entries is unchanged when written
in exact certified-15 ⊕ other-227 source coordinates. -/
theorem nf670FullSource_sum (f : Fin 242 → ℝ) :
    (∑ i : Fin 242, f i) =
      ∑ s : (Fin 15 ⊕ Fin 227), f (nf669SourceSum s) := by
  symm
  exact Fintype.sum_equiv nf669OriginalSourceEquiv
    (fun s => f (nf669SourceSum s)) f (fun s => rfl)

/-- The unweighted original 242-source Gram quadratic form is
exactly the double sum over the unchanged original source labels. -/
theorem nf670FullSource_quadratic_reindex (z : Fin 242 → ℝ) :
    neutralNF661Quadratic neutralNF606PhysicalH z =
      ∑ s : (Fin 15 ⊕ Fin 227),
        ∑ t : (Fin 15 ⊕ Fin 227),
          neutralNF606PhysicalH (nf669SourceSum s)
            (nf669SourceSum t) *
            z (nf669SourceSum s) * z (nf669SourceSum t) := by
  unfold neutralNF661Quadratic
  calc
    (∑ i : Fin 242, ∑ j : Fin 242,
        neutralNF606PhysicalH i j * z i * z j) =
      ∑ s : (Fin 15 ⊕ Fin 227), ∑ j : Fin 242,
        neutralNF606PhysicalH (nf669SourceSum s) j *
          z (nf669SourceSum s) * z j :=
        nf670FullSource_sum
          (fun i => ∑ j : Fin 242,
            neutralNF606PhysicalH i j * z i * z j)
    _ = ∑ s : (Fin 15 ⊕ Fin 227),
          ∑ t : (Fin 15 ⊕ Fin 227),
            neutralNF606PhysicalH
              (nf669SourceSum s) (nf669SourceSum t) *
                z (nf669SourceSum s) * z (nf669SourceSum t) := by
        apply Finset.sum_congr rfl
        intro s _
        exact nf670FullSource_sum
          (fun j => neutralNF606PhysicalH
            (nf669SourceSum s) j * z (nf669SourceSum s) * z j)

/-- Reconstruct an arbitrary original 242-coefficient vector from its
15 certified-source entries and 227 complementary oscillator entries. -/
def nf670AssembleOriginal (x : Fin 15 → ℝ)
    (y : Fin 227 → ℝ) (k : Fin 242) : ℝ :=
  match nf669OriginalSourceEquiv.symm k with
  | Sum.inl i => x i
  | Sum.inr j => y j

theorem nf670AssembleOriginal_source (x : Fin 15 → ℝ)
    (y : Fin 227 → ℝ) (s : Fin 15 ⊕ Fin 227) :
    nf670AssembleOriginal x y (nf669SourceSum s) =
      match s with
      | Sum.inl i => x i
      | Sum.inr j => y j := by
  unfold nf670AssembleOriginal
  have h : nf669OriginalSourceEquiv.symm (nf669SourceSum s) = s :=
    nf669OriginalSourceEquiv.symm_apply_apply s
  rw [h]

/-- Extract the original selected and complementary vectors back out
of a full original source coefficient array. -/
theorem nf670AssembleOriginal_roundtrip (z : Fin 242 → ℝ) :
    nf670AssembleOriginal
      (fun i => z (neutralNF661Source i))
      (fun j => z (nf669ComplementSource j)) = z := by
  funext k
  have hk := nf669OriginalSourceEquiv.apply_symm_apply k
  unfold nf670AssembleOriginal
  cases h : nf669OriginalSourceEquiv.symm k with
  | inl i =>
    change z (nf669SourceSum (Sum.inl i)) = z k
    have hi : nf669SourceSum (Sum.inl i) = k := by
      simpa [h] using hk
    rw [hi]
  | inr j =>
    change z (nf669SourceSum (Sum.inr j)) = z k
    have hj : nf669SourceSum (Sum.inr j) = k := by
      simpa [h] using hk
    rw [hj]

theorem nf670Mixed_physicalTransposed (x : Fin 15 → ℝ)
    (y : Fin 227 → ℝ) :
    (∑ j : Fin 227, ∑ i : Fin 15,
      neutralNF606PhysicalH
        (nf669ComplementSource j) (neutralNF661Source i) *
          y j * x i) =
      neutralNF669Mixed nf669OriginalB x y := by
  unfold neutralNF669Mixed
  calc
    (∑ j : Fin 227, ∑ i : Fin 15,
        neutralNF606PhysicalH
          (nf669ComplementSource j) (neutralNF661Source i) *
          y j * x i) =
      ∑ i : Fin 15, ∑ j : Fin 227,
        neutralNF606PhysicalH
          (nf669ComplementSource j) (neutralNF661Source i) *
          y j * x i := Finset.sum_comm
    _ = ∑ i : Fin 15, ∑ j : Fin 227,
        nf669OriginalB i j * x i * y j := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      rw [← nf669OriginalB_transpose i j]
      ring

/-- Complete exact 242-source physical quadratic energy
decomposition, with genuine integral A,B,C. -/
theorem nf670FullPhysicalGram_blockEnergy
    (x : Fin 15 → ℝ) (y : Fin 227 → ℝ) :
    neutralNF661Quadratic neutralNF606PhysicalH
      (nf670AssembleOriginal x y) =
    neutralNF669BlockEnergy
      nf669OriginalA nf669OriginalB nf669OriginalC x y := by
  rw [nf670FullSource_quadratic_reindex]
  simp only [nf670AssembleOriginal_source, Fintype.sum_sum_type,
    Finset.sum_add_distrib]
  change
    ((∑ i : Fin 15, ∑ j : Fin 15,
        nf669OriginalA i j * x i * x j) +
      (∑ i : Fin 15, ∑ j : Fin 227,
        nf669OriginalB i j * x i * y j)) +
    ((∑ j : Fin 227, ∑ i : Fin 15,
        neutralNF606PhysicalH
          (nf669ComplementSource j) (neutralNF661Source i) *
            y j * x i) +
      (∑ i : Fin 227, ∑ j : Fin 227,
        nf669OriginalC i j * y i * y j)) =
      neutralNF669BlockEnergy
        nf669OriginalA nf669OriginalB nf669OriginalC x y
  rw [nf670Mixed_physicalTransposed]
  unfold neutralNF669BlockEnergy neutralNF669Mixed
    neutralNF661Quadratic
  ring

/-- The original full 242-source H quadratic form is a physical
block energy for the explicitly extracted original coordinates. -/
theorem nf670FullPhysicalGram_allCoefficients (z : Fin 242 → ℝ) :
    neutralNF661Quadratic neutralNF606PhysicalH z =
      neutralNF669BlockEnergy
        nf669OriginalA nf669OriginalB nf669OriginalC
        (fun i => z (neutralNF661Source i))
        (fun j => z (nf669ComplementSource j)) := by
  rw [← nf670AssembleOriginal_roundtrip z]
  exact nf670FullPhysicalGram_blockEnergy
    (fun i => z (neutralNF661Source i))
    (fun j => z (nf669ComplementSource j))

#print axioms nf670FullSource_sum
#print axioms nf670FullSource_quadratic_reindex
#print axioms nf670AssembleOriginal_source
#print axioms nf670AssembleOriginal_roundtrip
#print axioms nf670Mixed_physicalTransposed
#print axioms nf670FullPhysicalGram_blockEnergy
#print axioms nf670FullPhysicalGram_allCoefficients

end
end WeilDefect
