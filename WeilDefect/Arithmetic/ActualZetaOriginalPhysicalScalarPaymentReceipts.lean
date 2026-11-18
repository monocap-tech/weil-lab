import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerPayments

namespace WeilDefect

/-! NF639: scalar payment receipts on the exact widened data.
The mass and product numerators are proposals. A local payment proof
can be checked before the large dot-product and mass custody proofs;
it is attached only when these exact identities are supplied. -/

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

def NF639PaymentRow.Valid (v : NF639PaymentRow) (c : NF626CenterCache)
    (s : NF626ScaledInputs) (i : Fin 242) : Prop :=
  v.defect=c.defectNum s i ∧ v.col=s.col i ∧ v.total=s.total ∧
  v.wMass=s.wMass ∧ v.yMass=s.yMass ∧ v.rowMass=s.rowMass i ∧
  v.b=c.b i ∧ v.Ay=c.Ay i ∧ v.Dy=c.Dy i

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
  decide (v.rowFee S Q eH≤1/100 ∧
    v.residualFee S Q T U eH eV≤r ∧
    v.selectedFee S U r i≤neutralNF625Rad i)

theorem NF639PaymentRow.gate_to_ref (v : NF639PaymentRow)
    (c : NF626CenterCache) (s : NF626ScaledInputs) (i : Fin 242)
    (hv : v.Valid c s i) :
    v.gate s.S s.Q s.T s.U s.eH s.eV s.r i=c.fastPayGate s i := by
  rcases hv with ⟨hd,hc,ht,hw,hy,hr,hb,ha,hdy⟩
  simp only [NF639PaymentRow.gate,NF639PaymentRow.rowFee,
    NF639PaymentRow.residualFee,NF639PaymentRow.selectedFee,
    NF626CenterCache.fastPayGate,NF626CenterCache.fastRow,
    NF626CenterCache.fastResidual,NF626CenterCache.fastPayment,
    NF626ScaledInputs.aden,NF626ScaledInputs.bden,
    hd,hc,ht,hw,hy,hr,hb,ha,hdy]

theorem neutralNF639Payments_of_receipts (c : NF626CenterCache)
    (s : NF626ScaledInputs) (v : Fin 242 → NF639PaymentRow)
    (hp : decide (0 < s.S ∧ 0 < s.Q ∧ 0 < s.T ∧ 0 < s.U ∧
      0 ≤ s.r ∧ 0 ≤ s.eH ∧ 0 ≤ s.eV)=true)
    (hv : ∀ i, (v i).Valid c s i)
    (hg : ∀ i, (v i).gate s.S s.Q s.T s.U s.eH s.eV s.r i=true) :
    c.fastPayCheck s=true := by
  unfold NF626CenterCache.fastPayCheck
  simp only [Bool.and_eq_true]
  refine ⟨hp,List.all_eq_true.mpr ?_⟩
  intro i _
  rw [← (v i).gate_to_ref c s i (hv i)]
  exact hg i

end WeilDefect
