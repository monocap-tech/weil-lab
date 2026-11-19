import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTriangularEntryCustody

namespace WeilDefect

/-!
NF674: turn the NF673 original 242-source H/V triangular receipt into
independently compilable *per-source-row* Boolean obligations.

This does not assert the source-specific literal rows true. It proves
that 242 true row obligations recover EXACTLY the NF673 full receipt.
The five independent original-source predicates hbank/hcov/htri/hcache/
hpay remain genuine numerical verification targets.
-/

def neutralNF674LowerRow (M : NF622Moments) (p : NF625PaymentData)
    (i : Fin 242) : Bool :=
  (List.finRange 242).all (fun j =>
    if j.val ≤ i.val then neutralNF625EntryHCheck M p i j else true)

def neutralNF674CenterRow (p : NF625PaymentData)
    (i : Fin 242) : Bool :=
  (List.finRange 242).all (fun j => decide (p.H0 i j = p.H0 j i))

def neutralNF674MixedRow (M : NF622Moments) (p : NF625PaymentData)
    (i : Fin 242) : Bool :=
  (List.finRange 4).all (neutralNF625EntryVCheck M p i)

/-- The total certified numerical receipt is implemented as one
bounded row per original physical source, not a monolithic 242×242
Boolean normal form. -/
def neutralNF674OriginalRowCheck (M : NF622Moments)
    (p : NF625PaymentData) (i : Fin 242) : Bool :=
  (neutralNF674LowerRow M p i &&
    neutralNF674CenterRow p i) &&
    neutralNF674MixedRow M p i

/-- A fully authenticated array of 242 independent original rows
implies the exact NF673 lower-triangle, center-symmetry and mixed-V
check; no original source-analytic condition is weakened. -/
theorem neutralNF674Rows_imply_original_entry
    (M : NF622Moments) (p : NF625PaymentData)
    (hrows : ∀ i : Fin 242,
      neutralNF674OriginalRowCheck M p i = true) :
    neutralNF673EntryCheck M p = true := by
  unfold neutralNF673EntryCheck
  simp only [Bool.and_eq_true]
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · unfold neutralNF673LowerHEntryCheck
    apply List.all_eq_true.mpr
    intro i _
    have hi := hrows i
    simp only [neutralNF674OriginalRowCheck, Bool.and_eq_true] at hi
    simpa only [neutralNF674LowerRow] using hi.1.1
  · unfold neutralNF673CenterSymmetryCheck
    apply List.all_eq_true.mpr
    intro i _
    have hi := hrows i
    simp only [neutralNF674OriginalRowCheck, Bool.and_eq_true] at hi
    simpa only [neutralNF674CenterRow] using hi.1.2
  · unfold neutralNF673MixedVEntryCheck
    apply List.all_eq_true.mpr
    intro i _
    have hi := hrows i
    simp only [neutralNF674OriginalRowCheck, Bool.and_eq_true] at hi
    simpa only [neutralNF674MixedRow] using hi.2

/-- The row-wise checker is *equivalent* to the old global check;
it is not a new independent analytic assumption. -/
theorem neutralNF674Rows_iff_original_entry
    (M : NF622Moments) (p : NF625PaymentData) :
    (∀ i : Fin 242,
       neutralNF674OriginalRowCheck M p i = true) ↔
      neutralNF673EntryCheck M p = true := by
  constructor
  · exact neutralNF674Rows_imply_original_entry M p
  · intro h i
    unfold neutralNF673EntryCheck at h
    simp only [Bool.and_eq_true] at h
    unfold neutralNF674OriginalRowCheck
    simp only [Bool.and_eq_true]
    refine ⟨⟨?_, ?_⟩, ?_⟩
    · change neutralNF674LowerRow M p i = true
      unfold neutralNF674LowerRow neutralNF673LowerHEntryCheck at *
      exact (List.all_eq_true.mp h.1.1) i (by simp)
    · change neutralNF674CenterRow p i = true
      unfold neutralNF674CenterRow neutralNF673CenterSymmetryCheck at *
      exact (List.all_eq_true.mp h.1.2) i (by simp)
    · change neutralNF674MixedRow M p i = true
      unfold neutralNF674MixedRow neutralNF673MixedVEntryCheck at *
      exact (List.all_eq_true.mp h.2) i (by simp)

/-- Reuse the already validated analytic original interval attachment
unchanged after literal per-row checks. -/
theorem neutralNF674Rows_sound
    (M : NF622Moments) (p : NF625PaymentData)
    (hM : neutralNF624AllMomentsSound M)
    (hrows : ∀ i : Fin 242,
      neutralNF674OriginalRowCheck M p i = true) :
    (∀ i j,
      |neutralNF606PhysicalH i j - p.HR i j| ≤ (p.eH : ℝ)) ∧
    (∀ i j,
      |neutralNF606PhysicalV i j - p.VR i j| ≤ (p.eV : ℝ)) :=
  neutralNF673EntryCheck_sound M p hM
    (neutralNF674Rows_imply_original_entry M p hrows)

#print axioms neutralNF674Rows_imply_original_entry
#print axioms neutralNF674Rows_iff_original_entry
#print axioms neutralNF674Rows_sound

end WeilDefect
