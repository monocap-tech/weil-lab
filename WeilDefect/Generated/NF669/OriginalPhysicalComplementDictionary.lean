import WeilDefect.Generated.NF665.OriginalPhysicalCoercivity

namespace WeilDefect

/-!
NF669: exact 15+227 index dictionary for the original 242 selected
physical generators. The protected block is original oscillators
0..13 and original sinh pole source 241; its complement is exactly
the remaining oscillator sources 14..240, not a surrogate basis.

This module is purely structural. It makes NO assertion that the
227-dimensional complement or Schur operator is coercive.
-/

noncomputable section
open Finset

/-- The 227 original selected oscillators omitted by the certified
15-source local Gram block, in their original source ordering. -/
def nf669ComplementSource (j : Fin 227) : Fin 242 :=
  ⟨j.val + 14, by omega⟩

theorem nf669ComplementSource_range (j : Fin 227) :
    14 ≤ (nf669ComplementSource j).val ∧
      (nf669ComplementSource j).val < 241 := by
  change 14 ≤ j.val + 14 ∧ j.val + 14 < 241
  omega

theorem nf669SelectedSource_injective :
    Function.Injective neutralNF661Source := by
  intro a b hab
  apply Fin.ext
  have hv := congrArg Fin.val hab
  change (if a.val = 14 then 241 else a.val) =
    (if b.val = 14 then 241 else b.val) at hv
  by_cases ha : a.val = 14
  · by_cases hb : b.val = 14
    · omega
    · simp [ha, hb] at hv
      have hb_lt := b.isLt
      omega
  · by_cases hb : b.val = 14
    · simp [ha, hb] at hv
      have ha_lt := a.isLt
      omega
    · simpa [ha, hb] using hv

theorem nf669ComplementSource_injective :
    Function.Injective nf669ComplementSource := by
  intro a b hab
  apply Fin.ext
  have hv := congrArg Fin.val hab
  change a.val + 14 = b.val + 14 at hv
  omega

/-- The two original source sets are disjoint, including the genuine
pole. There is no source relabelling or numerical frame change. -/
theorem nf669Source_disjoint
    (i : Fin 15) (j : Fin 227) :
    neutralNF661Source i ≠ nf669ComplementSource j := by
  intro h
  have hv := congrArg Fin.val h
  change (if i.val = 14 then 241 else i.val) = j.val + 14 at hv
  by_cases hi : i.val = 14
  · simp [hi] at hv
    have hj := j.isLt
    omega
  · simp [hi] at hv
    have hii := i.isLt
    omega

/-- Every one of the original 242 generator indices is selected
exactly once, either by the certified 15-source system or by the
227-source complementary oscillator set. -/
theorem nf669Source_cover (k : Fin 242) :
    (∃ i : Fin 15, neutralNF661Source i = k) ∨
      (∃ j : Fin 227, nf669ComplementSource j = k) := by
  by_cases hsmall : k.val < 14
  · left
    refine ⟨⟨k.val, by omega⟩, ?_⟩
    apply Fin.ext
    change (if k.val = 14 then 241 else k.val) = k.val
    simp [Nat.ne_of_lt hsmall]
  · by_cases hpole : k.val = 241
    · left
      refine ⟨(14 : Fin 15), ?_⟩
      apply Fin.ext
      change 241 = k.val
      omega
    · right
      have hj : k.val - 14 < 227 := by
        have hk := k.isLt
        omega
      refine ⟨⟨k.val - 14, hj⟩, ?_⟩
      apply Fin.ext
      change k.val - 14 + 14 = k.val
      omega

/-- Exact additive-index model of the original 242 source directions. -/
def nf669SourceSum (s : (Fin 15 ⊕ Fin 227)) : Fin 242 :=
  match s with
  | Sum.inl i => neutralNF661Source i
  | Sum.inr j => nf669ComplementSource j

theorem nf669SourceSum_injective :
    Function.Injective nf669SourceSum := by
  intro s t h
  cases s with
  | inl i =>
    cases t with
    | inl j =>
      have hij : neutralNF661Source i = neutralNF661Source j := h
      exact congrArg Sum.inl (nf669SelectedSource_injective hij)
    | inr j =>
      exact False.elim (nf669Source_disjoint i j h)
  | inr i =>
    cases t with
    | inl j =>
      exact False.elim (nf669Source_disjoint j i h.symm)
    | inr j =>
      have hij : nf669ComplementSource i = nf669ComplementSource j := h
      exact congrArg Sum.inr (nf669ComplementSource_injective hij)

theorem nf669SourceSum_surjective :
    Function.Surjective nf669SourceSum := by
  intro k
  rcases nf669Source_cover k with ⟨i, hi⟩ | ⟨j, hj⟩
  · exact ⟨Sum.inl i, hi⟩
  · exact ⟨Sum.inr j, hj⟩

/-- Genuine 242-index equivalence used to reindex future physical
quadratic and cross terms without changing their generators. -/
noncomputable def nf669OriginalSourceEquiv :
    (Fin 15 ⊕ Fin 227) ≃ Fin 242 :=
  Equiv.ofBijective nf669SourceSum
    ⟨nf669SourceSum_injective, nf669SourceSum_surjective⟩

/-- The certified 15-by-15 block is exactly the same integral-defined
original physical H submatrix used in NF665. -/
def nf669OriginalA (i j : Fin 15) : ℝ :=
  neutralNF606PhysicalH (neutralNF661Source i)
    (neutralNF661Source j)

def nf669OriginalB (i : Fin 15) (j : Fin 227) : ℝ :=
  neutralNF606PhysicalH (neutralNF661Source i)
    (nf669ComplementSource j)

def nf669OriginalC (i j : Fin 227) : ℝ :=
  neutralNF606PhysicalH (nf669ComplementSource i)
    (nf669ComplementSource j)

/-- The original 242-by-242 physical Gram matrix, transported solely
by the exact source-index bijection; there is no numerical
preconditioner or approximate basis change in this identity. -/
def nf669OriginalReindexedH
    (s t : Fin 15 ⊕ Fin 227) : ℝ :=
  neutralNF606PhysicalH (nf669SourceSum s) (nf669SourceSum t)

theorem nf669OriginalReindexed_selected
    (i j : Fin 15) :
    nf669OriginalReindexedH (Sum.inl i) (Sum.inl j) =
      nf669OriginalA i j := rfl

theorem nf669OriginalReindexed_mixed
    (i : Fin 15) (j : Fin 227) :
    nf669OriginalReindexedH (Sum.inl i) (Sum.inr j) =
      nf669OriginalB i j := rfl

theorem nf669OriginalReindexed_complement
    (i j : Fin 227) :
    nf669OriginalReindexedH (Sum.inr i) (Sum.inr j) =
      nf669OriginalC i j := rfl

/-- Every full original physical H entry is preserved by the exact
15+227 reindexing, not merely the selected block entries. -/
theorem nf669OriginalReindexed_preservesH
    (i j : Fin 242) :
    neutralNF606PhysicalH i j =
      nf669OriginalReindexedH
        (nf669OriginalSourceEquiv.symm i)
        (nf669OriginalSourceEquiv.symm j) := by
  have hi :
      nf669SourceSum (nf669OriginalSourceEquiv.symm i) = i :=
    nf669OriginalSourceEquiv.apply_symm_apply i
  have hj :
      nf669SourceSum (nf669OriginalSourceEquiv.symm j) = j :=
    nf669OriginalSourceEquiv.apply_symm_apply j
  change neutralNF606PhysicalH i j =
    neutralNF606PhysicalH
      (nf669SourceSum (nf669OriginalSourceEquiv.symm i))
      (nf669SourceSum (nf669OriginalSourceEquiv.symm j))
  rw [hi, hj]

theorem nf669OriginalA_eq_certified :
    nf669OriginalA = neutralNF661PhysicalH := rfl

theorem nf669OriginalA_coercivity (x : Fin 15 → ℝ) :
    ((1 : ℝ) / (10 ^ 60 : ℝ)) * neutralNF661SqNorm x ≤
      neutralNF661Quadratic nf669OriginalA x := by
  exact nf665OriginalPhysical_coercivity x

theorem nf669OriginalA_symm (i j : Fin 15) :
    nf669OriginalA i j = nf669OriginalA j i :=
  neutralNF606PhysicalH_symm _ _

theorem nf669OriginalC_symm (i j : Fin 227) :
    nf669OriginalC i j = nf669OriginalC j i :=
  neutralNF606PhysicalH_symm _ _

theorem nf669OriginalB_transpose (i : Fin 15) (j : Fin 227) :
    nf669OriginalB i j =
      neutralNF606PhysicalH (nf669ComplementSource j)
        (neutralNF661Source i) :=
  neutralNF606PhysicalH_symm _ _

#print axioms nf669SelectedSource_injective
#print axioms nf669Source_disjoint
#print axioms nf669Source_cover
#print axioms nf669SourceSum_injective
#print axioms nf669SourceSum_surjective
#print axioms nf669OriginalReindexed_preservesH
#print axioms nf669OriginalA_coercivity
#print axioms nf669OriginalB_transpose

end
end WeilDefect
