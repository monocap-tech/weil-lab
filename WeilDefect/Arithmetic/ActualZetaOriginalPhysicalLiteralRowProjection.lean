import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalShardedEntryCustody

namespace WeilDefect

/-!
NF675: source-preserving row-projection bridge for literal original
physical H/V numerical receipts. This theorem allows a small
NF631-pinned Lean row proposal to certify the SAME row of the eventual
complete NF626 payment, once the exact row projection is attached.

No source-specific Boolean is asserted true here. The original full
bank and 242-row frozen-box payment gates remain separate.
-/

/-- Every original row checker reads exactly its own H center row,
its H center column (for symmetry), its four V centers, and global
H/V error radii. It DOES NOT read D, y0, r or other physical rows. -/
theorem neutralNF675OriginalRow_eq_of_projection
    (M : NF622Moments) (p q : NF625PaymentData)
    (i : Fin 242)
    (hrow : ∀ j : Fin 242, p.H0 i j = q.H0 i j)
    (hcol : ∀ j : Fin 242, p.H0 j i = q.H0 j i)
    (hV : ∀ j : Fin 4, p.V0 i j = q.V0 i j)
    (hEH : p.eH = q.eH) (hEV : p.eV = q.eV) :
    neutralNF674OriginalRowCheck M p i =
      neutralNF674OriginalRowCheck M q i := by
  unfold neutralNF674OriginalRowCheck
    neutralNF674LowerRow neutralNF674CenterRow neutralNF674MixedRow
  have hcheckH (j : Fin 242) :
      neutralNF625EntryHCheck M p i j =
        neutralNF625EntryHCheck M q i j := by
    simp only [neutralNF625EntryHCheck, hrow j, hEH]
  have hcheckV (j : Fin 4) :
      neutralNF625EntryVCheck M p i j =
        neutralNF625EntryVCheck M q i j := by
    simp only [neutralNF625EntryVCheck, hV j, hEV]
  have hcenter (j : Fin 242) :
      decide (p.H0 i j = p.H0 j i) =
        decide (q.H0 i j = q.H0 j i) := by
    rw [hrow j, hcol j]
  have hl : (fun j : Fin 242 =>
      if j.val ≤ i.val then neutralNF625EntryHCheck M p i j else true) =
      (fun j : Fin 242 =>
      if j.val ≤ i.val then neutralNF625EntryHCheck M q i j else true) := by
    funext j
    rw [hcheckH j]
  have hs : (fun j : Fin 242 => decide (p.H0 i j = p.H0 j i)) =
      (fun j : Fin 242 => decide (q.H0 i j = q.H0 j i)) :=
    funext hcenter
  have hv : neutralNF625EntryVCheck M p i =
      neutralNF625EntryVCheck M q i := funext hcheckV
  rw [hl, hs, hv]

/-- An explicitly checked small original source row is a valid
certificate for that row of the COMPLETE original payment, provided
the exactly stated projection fields are kernel-equated. The proof
never treats equality of outside-row placeholders as an assumption. -/
theorem neutralNF675OriginalRow_true_of_projection
    (M : NF622Moments) (p q : NF625PaymentData)
    (i : Fin 242)
    (hrow : ∀ j : Fin 242, p.H0 i j = q.H0 i j)
    (hcol : ∀ j : Fin 242, p.H0 j i = q.H0 j i)
    (hV : ∀ j : Fin 4, p.V0 i j = q.V0 i j)
    (hEH : p.eH = q.eH) (hEV : p.eV = q.eV)
    (hpilot : neutralNF674OriginalRowCheck M p i = true) :
    neutralNF674OriginalRowCheck M q i = true := by
  rw [← neutralNF675OriginalRow_eq_of_projection
    M p q i hrow hcol hV hEH hEV]
  exact hpilot

#print axioms neutralNF675OriginalRow_eq_of_projection
#print axioms neutralNF675OriginalRow_true_of_projection

end WeilDefect
