import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRationalPayments

namespace WeilDefect

/-! NF653: unchanged scalar arithmetic, isolated from the integer-cache
transfer proof. Literal row gates can build independently of that proof.
A passing gate does not assert that its proposed numerators are valid. -/

structure NF639PaymentRow where
  defect : ℤ
  col : ℤ
  total : ℤ
  wMass : ℤ
  yMass : ℤ
  rowMass : ℤ
  b : ℤ
  Ay : ℤ
  Dy : ℤ

def NF639PaymentRow.rowFee (v : NF639PaymentRow) (S Q : ℕ) (eH : ℚ) : ℚ :=
  (v.defect:ℚ)/((Q:ℚ)*S*S) + ((v.col:ℚ)/S)*(((v.total:ℚ)/S)*eH)

def NF639PaymentRow.residualFee (v : NF639PaymentRow)
    (S Q T U : ℕ) (eH eV : ℚ) : ℚ :=
  |(v.b:ℚ)/((Q:ℚ)*S*T)-(v.Ay:ℚ)/((Q:ℚ)*S*S*U)| +
    ((v.col:ℚ)/S)*(((v.wMass:ℚ)/T)*eV) +
    ((v.col:ℚ)/S)*(((v.yMass:ℚ)/((U:ℚ)*S))*eH)

def NF639PaymentRow.selectedFee (v : NF639PaymentRow)
    (S U : ℕ) (r : ℚ) (i : Fin 242) : ℚ :=
  |(v.Dy:ℚ)/((S:ℚ)*U)-neutralNF625Mid i| +
    ((v.rowMass:ℚ)/S)*(2*r)

def NF639PaymentRow.gate (v : NF639PaymentRow)
    (S Q T U : ℕ) (eH eV r : ℚ) (i : Fin 242) : Bool :=
  decide (v.rowFee S Q eH ≤ 1/100 ∧
    v.residualFee S Q T U eH eV ≤ r ∧
    v.selectedFee S U r i ≤ neutralNF625Rad i)

end WeilDefect
