import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerPayments
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentCore

namespace WeilDefect

/-! NF678: the scalar mass and Dy receipts use only the original
frame D and original vectors y,w. They can be certified before the
H,HD,A,V matrices are attached. No numerical equality is assumed. -/

theorem neutralNF678MassProjection
    (s t : NF626ScaledInputs)
    (hD : s.D = t.D) (hy : s.y = t.y) (hw : s.w = t.w) :
    s.col = t.col ∧ s.rowMass = t.rowMass ∧
      s.total = t.total ∧ s.wMass = t.wMass ∧ s.yMass = t.yMass := by
  have hc : s.col = t.col := by
    funext i
    unfold NF626ScaledInputs.col
    rw [hD]
  have hm : s.rowMass = t.rowMass := by
    funext i
    unfold NF626ScaledInputs.rowMass
    rw [hD]
  refine ⟨hc, hm, ?_, ?_, ?_⟩
  · unfold NF626ScaledInputs.total
    rw [hc]
  · unfold NF626ScaledInputs.wMass
    rw [hw]
  · unfold NF626ScaledInputs.yMass
    rw [hy, hc]

theorem neutralNF678DyProjection
    (s t : NF626ScaledInputs) (i : Fin 242)
    (hD : s.D = t.D) (hy : s.y = t.y) :
    neutralNF626Dot (s.D i) s.y = neutralNF626Dot (t.D i) t.y := by
  rw [hD, hy]

/-- Derive the global column total and y-weighted column mass from
the column-wise exact identities. These are not 242 independent
recalculations of the full original 242 by 242 frame. -/
theorem neutralNF678Totals_of_columns
    (s : NF626ScaledInputs) (cols : Fin 242 → ℤ)
    (hcols : ∀ i, cols i = s.col i)
    (T Y : ℤ)
    (hT : T = ∑ j, cols j)
    (hY : Y = neutralNF626Dot (fun j => |s.y j|) cols) :
    T = s.total ∧ Y = s.yMass := by
  have hc : cols = s.col := funext hcols
  rw [hc] at hT hY
  exact ⟨hT, hY⟩

#print axioms neutralNF678MassProjection
#print axioms neutralNF678DyProjection
#print axioms neutralNF678Totals_of_columns

end WeilDefect
