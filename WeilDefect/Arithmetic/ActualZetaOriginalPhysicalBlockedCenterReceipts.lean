import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentReceipts

namespace WeilDefect
open Finset

/-! NF640: split long dot products into independently checked blocks.
No probabilistic matrix-product check or unchecked cache is used.
The list of block index lists must partition the exact full index list. -/

def neutralNF640DotBlock {n : ℕ} (x y : Fin n → ℤ) (is : List (Fin n)) : ℤ :=
  (is.map (fun i => x i*y i)).sum

theorem neutralNF640DotBlock_append {n : ℕ} (x y : Fin n → ℤ)
    (a b : List (Fin n)) :
    neutralNF640DotBlock x y (a++b)=
      neutralNF640DotBlock x y a+neutralNF640DotBlock x y b := by
  simp [neutralNF640DotBlock,List.sum_append]

theorem neutralNF640DotBlock_join {n : ℕ} (x y : Fin n → ℤ)
    (blocks : List (List (Fin n))) :
    neutralNF640DotBlock x y blocks.flatten =
      (blocks.map (neutralNF640DotBlock x y)).sum := by
  induction blocks with
  | nil => rfl
  | cons a bs ih =>
    simp only [List.flatten_cons,List.map_cons,List.sum_cons,
      neutralNF640DotBlock_append,ih]

theorem neutralNF640DotBlock_full {n : ℕ} (x y : Fin n → ℤ) :
    neutralNF640DotBlock x y (List.finRange n)=neutralNF626Dot x y := by
  unfold neutralNF640DotBlock neutralNF626Dot
  rw [← List.sum_toFinset (List.nodup_finRange n)]
  congr 1
  ext i
  simp

def neutralNF640DotGate {n : ℕ} (x y : Fin n → ℤ)
    (is : List (Fin n)) (v : ℤ) : Bool :=
  decide (neutralNF640DotBlock x y is=v)

theorem neutralNF640Dot_of_blocks {n : ℕ} (x y : Fin n → ℤ)
    (blocks : List (List (Fin n))) (vs : List ℤ) (v : ℤ)
    (hparts : blocks.flatten=List.finRange n)
    (hvals : blocks.map (neutralNF640DotBlock x y)=vs)
    (hsum : vs.sum=v) :
    neutralNF626Dot x y=v := by
  rw [← neutralNF640DotBlock_full,← hparts,
    neutralNF640DotBlock_join,hvals,hsum]

/-- Keep the two expensive matrix products as exact column/row
identities; this gate is independent of scalar pay inequalities. -/
theorem neutralNF640HD_of_dot (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i j : Fin 242)
    (h : neutralNF626Dot (s.H i) (fun k => s.D k j)=c.HD i j) :
    c.HDGate s i j=true :=
  decide_eq_true h.symm

theorem neutralNF640A_of_dot (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i j : Fin 242)
    (h : neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j)=c.A i j) :
    c.AGate s i j=true :=
  decide_eq_true h.symm

structure NF640Masses where
  col : Fin 242 → ℤ
  row : Fin 242 → ℤ
  total : ℤ
  w : ℤ
  y : ℤ

def NF640Masses.Valid (m : NF640Masses) (s : NF626ScaledInputs) : Prop :=
  (∀ i,m.col i=s.col i) ∧ (∀ i,m.row i=s.rowMass i) ∧
    m.total=s.total ∧ m.w=s.wMass ∧ m.y=s.yMass

def NF640Masses.colGate (m : NF640Masses) (s : NF626ScaledInputs)
    (i : Fin 242) : Bool :=
  decide (m.col i=s.col i)

def NF640Masses.rowGate (m : NF640Masses) (s : NF626ScaledInputs)
    (i : Fin 242) : Bool :=
  decide (m.row i=s.rowMass i)

def NF640Masses.scalarGate (m : NF640Masses) (s : NF626ScaledInputs) : Bool :=
  decide (m.total=(∑ j,m.col j) ∧ m.w=s.wMass ∧
    m.y=neutralNF626Dot (fun j => |s.y j|) m.col)

theorem NF640Masses.valid_of_gates (m : NF640Masses) (s : NF626ScaledInputs)
    (hc : ∀ i,m.colGate s i=true)
    (hr : ∀ i,m.rowGate s i=true)
    (hg : m.scalarGate s=true) : m.Valid s := by
  have hcol : m.col=s.col := funext (fun i => of_decide_eq_true (hc i))
  have hrow : ∀ i,m.row i=s.rowMass i := fun i => of_decide_eq_true (hr i)
  have h : m.total=(∑ j,m.col j) ∧ m.w=s.wMass ∧
    m.y=neutralNF626Dot (fun j => |s.y j|) m.col := of_decide_eq_true hg
  rw [hcol] at h
  exact ⟨fun i => congrFun hcol i,hrow,h.1,h.2.1,h.2.2⟩

def neutralNF640BindRow (v : NF639PaymentRow) (m : NF640Masses)
    (c : NF626CenterCache) (s : NF626ScaledInputs) (i : Fin 242) : Bool :=
  decide (v.defect=c.defectNum s i ∧ v.col=m.col i ∧ v.total=m.total ∧
    v.wMass=m.w ∧ v.yMass=m.y ∧ v.rowMass=m.row i ∧
    v.b=c.b i ∧ v.Ay=c.Ay i ∧ v.Dy=c.Dy i)

theorem neutralNF640BindRow_sound (v : NF639PaymentRow) (m : NF640Masses)
    (c : NF626CenterCache) (s : NF626ScaledInputs) (i : Fin 242)
    (hm : m.Valid s) (hc : neutralNF640BindRow v m c s i=true) :
    v.Valid c s i := by
  have h : v.defect=c.defectNum s i ∧ v.col=m.col i ∧ v.total=m.total ∧
    v.wMass=m.w ∧ v.yMass=m.y ∧ v.rowMass=m.row i ∧
    v.b=c.b i ∧ v.Ay=c.Ay i ∧ v.Dy=c.Dy i := of_decide_eq_true hc
  rcases hm with ⟨hcol,hrow,ht,hw,hy⟩
  simpa only [NF639PaymentRow.Valid,hcol,hrow,ht,hw,hy] using h

def neutralNF640AbsGate {n : ℕ} (x : Fin n → ℤ) (v : ℤ) : Bool :=
  decide (v=∑ i, |x i|)

theorem neutralNF640AbsGate_sound {n : ℕ} (x : Fin n → ℤ) (v : ℤ)
    (h : neutralNF640AbsGate x v=true) : v=∑ i, |x i| :=
  of_decide_eq_true h

def neutralNF640TotalsGate (col y : Fin 242 → ℤ) (w : Fin 4 → ℤ)
    (total wm ym : ℤ) : Bool :=
  decide (total=(∑ j,col j) ∧ wm=(∑ j, |w j|) ∧
    ym=neutralNF626Dot (fun j => |y j|) col)

theorem neutralNF640TotalsGate_sound (col y : Fin 242 → ℤ) (w : Fin 4 → ℤ)
    (total wm ym : ℤ) (h : neutralNF640TotalsGate col y w total wm ym=true) :
    total=(∑ j,col j) ∧ wm=(∑ j, |w j|) ∧
      ym=neutralNF626Dot (fun j => |y j|) col :=
  of_decide_eq_true h

end WeilDefect
