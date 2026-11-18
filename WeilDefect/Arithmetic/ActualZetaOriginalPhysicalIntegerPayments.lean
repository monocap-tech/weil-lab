import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerCenters

namespace WeilDefect
open Finset

/-! NF626: compute the common-scale mass and row-defect numerators
using integers, then compare only scalar rational payments.
Correctness does not depend on the cache producer. -/

def NF626ScaledInputs.col (s : NF626ScaledInputs) (i : Fin 242) : ℤ :=
  ∑ k, |s.D k i|

def NF626ScaledInputs.rowMass (s : NF626ScaledInputs) (i : Fin 242) : ℤ :=
  ∑ j, |s.D i j|

def NF626ScaledInputs.total (s : NF626ScaledInputs) : ℤ :=
  ∑ i, s.col i

def NF626ScaledInputs.wMass (s : NF626ScaledInputs) : ℤ :=
  ∑ j, |s.w j|

def NF626ScaledInputs.yMass (s : NF626ScaledInputs) : ℤ :=
  neutralNF626Dot (fun j => |s.y j|) s.col

theorem neutralNF626AbsSum {n : ℕ} (x : Fin n → ℤ) (d : ℕ) :
    (∑ k, |(x k:ℚ)/d|) = ((∑ k, |x k| : ℤ):ℚ)/d := by
  simp_rw [abs_div,abs_of_nonneg (Nat.cast_nonneg d : (0:ℚ)≤d)]
  rw [← Finset.sum_div]
  push_cast <;> rfl

theorem NF626ScaledInputs.col_eq (s : NF626ScaledInputs) (i : Fin 242) :
    s.payment.c i = (s.col i:ℚ)/s.S := by
  unfold NF625PaymentData.c NF626ScaledInputs.payment NF626ScaledInputs.col
  exact neutralNF626AbsSum _ _

theorem NF626ScaledInputs.rowMass_eq (s : NF626ScaledInputs) (i : Fin 242) :
    (∑ j, |s.payment.D i j|) = (s.rowMass i:ℚ)/s.S := by
  exact neutralNF626AbsSum _ _

theorem NF626ScaledInputs.total_eq (s : NF626ScaledInputs) :
    (∑ i, s.payment.c i) = (s.total:ℚ)/s.S := by
  simp only [s.col_eq]
  rw [← Finset.sum_div]
  unfold NF626ScaledInputs.total
  push_cast <;> rfl

theorem NF626ScaledInputs.wMass_eq (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hc : c.Valid s) :
    (∑ j : Fin 4, |neutralNF625W j|) = (s.wMass:ℚ)/s.T := by
  simp_rw [← hc.1]
  exact neutralNF626AbsSum _ _

theorem NF626ScaledInputs.yMass_eq (s : NF626ScaledInputs) :
    (∑ j, |s.payment.y0 j| * s.payment.c j) =
      (s.yMass:ℚ)/((s.U:ℚ)*s.S) := by
  simp only [s.col_eq]
  change (∑ j, |(s.y j:ℚ)/s.U| * ((s.col j:ℚ)/s.S)) = _
  have hU : (0:ℚ) ≤ (s.U:ℚ) := Nat.cast_nonneg _
  simp only [abs_div,abs_of_nonneg hU]
  unfold NF626ScaledInputs.yMass
  simp_rw [← Int.cast_abs]
  exact neutralNF626ScaledDot _ _ _ _

def NF626ScaledInputs.adenZ (s : NF626ScaledInputs) : ℤ :=
  (s.Q:ℤ)*s.S*s.S

def NF626CenterCache.defectNum (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : ℤ :=
  ∑ j, |(if i=j then s.adenZ else 0)-c.A i j|

theorem NF626ScaledInputs.aden_cast (s : NF626ScaledInputs) :
    (s.adenZ:ℚ)=s.aden := by
  unfold NF626ScaledInputs.adenZ NF626ScaledInputs.aden
  push_cast <;> rfl

theorem NF626CenterCache.defect_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hd : 0 < s.aden) (hc : c.Valid s) (i : Fin 242) :
    (∑ j, |(if i=j then (1:ℚ) else 0)-s.payment.A i j|) =
      (c.defectNum s i:ℚ)/s.aden := by
  have ht (j : Fin 242) :
      (if i=j then (1:ℚ) else 0)-s.payment.A i j =
        (((if i=j then s.adenZ else 0)-c.A i j : ℤ):ℚ)/s.aden := by
    rw [c.A_eq s hc i j]
    split_ifs <;> push_cast <;> try rw [s.aden_cast] <;>
      field_simp [ne_of_gt hd] <;> ring
  simp_rw [ht,abs_div,abs_of_pos hd]
  rw [← Finset.sum_div]
  unfold NF626CenterCache.defectNum
  push_cast <;> rfl

def NF626CenterCache.fastRow (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : ℚ :=
  (c.defectNum s i:ℚ)/s.aden +
    ((s.col i:ℚ)/s.S)*(((s.total:ℚ)/s.S)*s.eH)

def NF626CenterCache.fastResidual (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : ℚ :=
  |(c.b i:ℚ)/s.bden-(c.Ay i:ℚ)/(s.aden*s.U)| +
    ((s.col i:ℚ)/s.S)*(((s.wMass:ℚ)/s.T)*s.eV) +
    ((s.col i:ℚ)/s.S)*(((s.yMass:ℚ)/((s.U:ℚ)*s.S))*s.eH)

def NF626CenterCache.fastPayment (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : ℚ :=
  |(c.Dy i:ℚ)/((s.S:ℚ)*s.U)-neutralNF625Mid i| +
    ((s.rowMass i:ℚ)/s.S)*(2*s.r)

theorem NF626CenterCache.fastRow_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hd : 0 < s.aden) (hc : c.Valid s) (i : Fin 242) :
    c.fastRow s i = s.payment.row i := by
  unfold NF626CenterCache.fastRow NF625PaymentData.row
  rw [c.defect_eq s hd hc i,s.total_eq,s.col_eq]
  rfl

theorem NF626CenterCache.fastResidual_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hc : c.Valid s) (i : Fin 242) :
    c.fastResidual s i = s.payment.residual i := by
  unfold NF626CenterCache.fastResidual NF625PaymentData.residual
  rw [c.b_eq s hc i,c.Ay_eq s hc i,s.wMass_eq c hc,s.yMass_eq]
  simp only [s.col_eq]
  rfl

theorem NF626CenterCache.fastPayment_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hc : c.Valid s) (i : Fin 242) :
    c.fastPayment s i = s.payment.payment i := by
  unfold NF626CenterCache.fastPayment NF625PaymentData.payment
  rw [c.Dy_eq s hc i,s.rowMass_eq]
  rfl

def NF626CenterCache.fastPayGate (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : Bool :=
  decide (c.fastRow s i ≤ 1/100 ∧ c.fastResidual s i ≤ s.r ∧
    c.fastPayment s i ≤ neutralNF625Rad i)

def NF626CenterCache.fastPayCheck (c : NF626CenterCache) (s : NF626ScaledInputs) : Bool :=
  decide (0 < s.S ∧ 0 < s.Q ∧ 0 < s.T ∧ 0 < s.U ∧ 0 ≤ s.r ∧ 0 ≤ s.eH ∧ 0 ≤ s.eV) &&
    (List.finRange 242).all (c.fastPayGate s)

theorem NF626CenterCache.payment_of_fast (c : NF626CenterCache)
    (s : NF626ScaledInputs) (hc : c.Valid s)
    (hp : c.fastPayCheck s = true) : s.payment.check = true := by
  unfold NF626CenterCache.fastPayCheck at hp
  simp only [Bool.and_eq_true] at hp
  have hpar : 0 < s.S ∧ 0 < s.Q ∧ 0 < s.T ∧ 0 < s.U ∧ 0 ≤ s.r ∧ 0 ≤ s.eH ∧ 0 ≤ s.eV :=
    of_decide_eq_true hp.1
  have hs : (0:ℚ)<s.S := by exact_mod_cast hpar.1
  have hq : (0:ℚ)<s.Q := by exact_mod_cast hpar.2.1
  have hd : 0 < s.aden := by unfold NF626ScaledInputs.aden; positivity
  unfold NF625PaymentData.check
  simp only [Bool.and_eq_true]
  constructor
  · apply decide_eq_true
    exact hpar.2.2.2.2
  · apply List.all_eq_true.mpr
    intro i hi
    have h := (List.all_eq_true.mp hp.2) i hi
    have he : c.fastRow s i ≤ 1/100 ∧ c.fastResidual s i ≤ s.r ∧
        c.fastPayment s i ≤ neutralNF625Rad i := of_decide_eq_true h
    rw [c.fastRow_eq s hd hc i,c.fastResidual_eq s hc i,c.fastPayment_eq s hc i] at he
    exact decide_eq_true he

end WeilDefect
