import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMetadataCoverage

namespace WeilDefect

/-! NF679: the exact original frequency/degree coverage check
is an independently executable Boolean per source row. Metadata
contains dummy values only; the numerical bank's shape and analytic
truth remain independent proof obligations. -/

def neutralNF679SelectedRow (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i : Fin 242) : Bool :=
  (List.finRange 242).all (fun j =>
    neutralNF624Signs.all (fun s =>
      neutralNF624Signs.all (neutralNF624SelectedCoverageRow bank idx i j s)))

def neutralNF679MixedRow (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i : Fin 242) : Bool :=
  (List.finRange 4).all (fun j =>
    (List.finRange 33).all (fun k =>
      neutralNF624Signs.all (fun s =>
        neutralNF624Signs.all (neutralNF624MixedCoverageRow bank idx i j k s))))

def neutralNF679CoverageRow (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i : Fin 242) : Bool :=
  neutralNF679SelectedRow bank idx i &&
    neutralNF679MixedRow bank idx i

theorem neutralNF679Coverage_of_rows
    (bank : Array NF624KeyTable) (idx : NF616Frequency → ℕ)
    (hrows : ∀ i : Fin 242, neutralNF679CoverageRow bank idx i = true) :
    neutralNF624CoverageCheck bank idx = true := by
  have hr (i : Fin 242) :
      neutralNF679SelectedRow bank idx i = true ∧
        neutralNF679MixedRow bank idx i = true := by
    simpa only [neutralNF679CoverageRow, Bool.and_eq_true] using hrows i
  unfold neutralNF624CoverageCheck
  simp only [Bool.and_eq_true]
  exact ⟨List.all_eq_true.mpr (fun i _ => (hr i).1),
    List.all_eq_true.mpr (fun i _ => (hr i).2)⟩

theorem neutralNF679Rows_iff_coverage
    (bank : Array NF624KeyTable) (idx : NF616Frequency → ℕ) :
    (∀ i : Fin 242, neutralNF679CoverageRow bank idx i = true) ↔
      neutralNF624CoverageCheck bank idx = true := by
  constructor
  · exact neutralNF679Coverage_of_rows bank idx
  · intro h i
    unfold neutralNF624CoverageCheck at h
    simp only [Bool.and_eq_true] at h
    unfold neutralNF679CoverageRow
    simp only [Bool.and_eq_true]
    exact ⟨(List.all_eq_true.mp h.1) i (by simp),
      (List.all_eq_true.mp h.2) i (by simp)⟩

/-- The original numerical bank, not its placeholder metadata, is
the object of analytic soundness. Exact shape and bank truth are
still explicit hypotheses. -/
theorem neutralNF679AllMoments_of_metadata_rows
    (bank metadata : Array NF624KeyTable)
    (hbank : neutralNF624BankCheck bank = true)
    (hshape : neutralNF627ShapeCheck bank metadata = true)
    (hrows : ∀ i : Fin 242,
      neutralNF679CoverageRow metadata (neutralNF624Index metadata) i = true) :
    neutralNF624AllMomentsSound
      (neutralNF624Lookup bank (neutralNF624Index metadata)) :=
  neutralNF627AllMoments_of_metadata bank metadata hbank hshape
    (neutralNF679Coverage_of_rows metadata (neutralNF624Index metadata) hrows)

#print axioms neutralNF679Coverage_of_rows
#print axioms neutralNF679Rows_iff_coverage
#print axioms neutralNF679AllMoments_of_metadata_rows

end WeilDefect
