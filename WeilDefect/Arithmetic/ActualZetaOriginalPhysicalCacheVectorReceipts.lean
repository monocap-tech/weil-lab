import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerPayments
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentCore

namespace WeilDefect

/-! NF680: exact local scalar numerator formulas.  The full cache
matrix-product identities are independent obligations. -/

def neutralNF680DefectRow (i : Fin 242) (den : ℤ)
    (a : Fin 242 → ℤ) : ℤ :=
  ∑ j, |(if i = j then den else 0) - a j|

theorem neutralNF680DefectRow_eq (c : NF626CenterCache)
    (s : NF626ScaledInputs) (i : Fin 242) (a : Fin 242 → ℤ)
    (den : ℤ) (ha : a = c.A i) (hd : den = s.adenZ) :
    neutralNF680DefectRow i den a = c.defectNum s i := by
  rw [ha, hd]
  rfl

/-- Convert local exact proofs to the complete cache's vector gate.
The full cache has to agree with the local row data; no such
agreement is asserted by this generic theorem. -/
theorem neutralNF680VectorGate_of_receipts
    (c : NF626CenterCache) (s : NF626ScaledInputs) (i : Fin 242)
    (v : NF639PaymentRow)
    (hb : v.b = c.b i) (hay : v.Ay = c.Ay i)
    (hdy : v.Dy = c.Dy i)
    (hVw : c.Vw i = neutralNF626Dot (s.V i) s.w)
    (hB : v.b = neutralNF626Dot (fun j => s.D j i) c.Vw)
    (hAy : v.Ay = neutralNF626Dot (c.A i) s.y)
    (hDy : v.Dy = neutralNF626Dot (s.D i) s.y) :
    c.vectorGate s i = true := by
  unfold NF626CenterCache.vectorGate
  apply decide_eq_true
  exact ⟨hVw, hb.symm.trans hB, hay.symm.trans hAy, hdy.symm.trans hDy⟩

#print axioms neutralNF680DefectRow_eq
#print axioms neutralNF680VectorGate_of_receipts

end WeilDefect
