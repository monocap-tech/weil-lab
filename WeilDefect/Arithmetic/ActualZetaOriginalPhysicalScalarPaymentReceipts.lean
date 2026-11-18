import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentCore
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerPayments

namespace WeilDefect

def NF639PaymentRow.Valid (v : NF639PaymentRow) (c : NF626CenterCache)
    (s : NF626ScaledInputs) (i : Fin 242) : Prop :=
  v.defect=c.defectNum s i ∧ v.col=s.col i ∧ v.total=s.total ∧
  v.wMass=s.wMass ∧ v.yMass=s.yMass ∧ v.rowMass=s.rowMass i ∧
  v.b=c.b i ∧ v.Ay=c.Ay i ∧ v.Dy=c.Dy i

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
