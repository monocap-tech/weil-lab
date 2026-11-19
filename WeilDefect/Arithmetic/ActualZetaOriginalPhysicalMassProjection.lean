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
  simp only [NF626ScaledInputs.col, NF626ScaledInputs.rowMass,
    NF626ScaledInputs.total, NF626ScaledInputs.wMass,
    NF626ScaledInputs.yMass, hD, hy, hw] <;>
    exact ⟨rfl, rfl, rfl, rfl, rfl⟩

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
