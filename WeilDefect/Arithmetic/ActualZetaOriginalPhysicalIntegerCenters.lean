import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRationalPayments

namespace WeilDefect
open Finset

/-! NF626: common-scale integer center products. The untrusted
matrix product cache is checked by exact dot identities; its
analytic meaning follows from the reference rational definitions.
No floating arithmetic or unchecked product oracle enters Lean. -/

def neutralNF626Dot {n : ℕ} (x y : Fin n → ℤ) : ℤ :=
  ∑ k, x k * y k

theorem neutralNF626ScaledDot {n : ℕ} (x y : Fin n → ℤ) (d e : ℚ) :
    (∑ k, ((x k:ℚ)/d)*((y k:ℚ)/e)) =
      (neutralNF626Dot x y:ℚ)/(d*e) := by
  simp_rw [div_mul_div_comm]
  rw [← Finset.sum_div]
  unfold neutralNF626Dot
  push_cast <;> rfl

structure NF626ScaledInputs where
  D : Fin 242 → Fin 242 → ℤ
  H : Fin 242 → Fin 242 → ℤ
  V : Fin 242 → Fin 4 → ℤ
  y : Fin 242 → ℤ
  w : Fin 4 → ℤ
  S : ℕ
  Q : ℕ
  U : ℕ
  T : ℕ
  eH : ℚ
  eV : ℚ
  r : ℚ

def NF626ScaledInputs.payment (s : NF626ScaledInputs) : NF625PaymentData :=
  ⟨fun i j => (s.D i j:ℚ)/s.S,
   fun i j => (s.H i j:ℚ)/s.Q,
   fun i j => (s.V i j:ℚ)/s.Q,
   fun i => (s.y i:ℚ)/s.U,
   s.eH,s.eV,s.r⟩

def NF626ScaledInputs.wCheck (s : NF626ScaledInputs) : Bool :=
  (List.finRange 4).all (fun j => decide ((s.w j:ℚ)/s.T = neutralNF625W j))

structure NF626CenterCache where
  HD : Fin 242 → Fin 242 → ℤ
  A : Fin 242 → Fin 242 → ℤ
  Vw : Fin 242 → ℤ
  b : Fin 242 → ℤ
  Ay : Fin 242 → ℤ
  Dy : Fin 242 → ℤ

def NF626CenterCache.HDGate (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i j : Fin 242) : Bool :=
  decide (c.HD i j = neutralNF626Dot (s.H i) (fun k => s.D k j))

def NF626CenterCache.AGate (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i j : Fin 242) : Bool :=
  decide (c.A i j = neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j))

def NF626CenterCache.vectorGate (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : Bool :=
  decide (c.Vw i = neutralNF626Dot (s.V i) s.w ∧
    c.b i = neutralNF626Dot (fun k => s.D k i) c.Vw ∧
    c.Ay i = neutralNF626Dot (c.A i) s.y ∧
    c.Dy i = neutralNF626Dot (s.D i) s.y)

def NF626CenterCache.check (c : NF626CenterCache) (s : NF626ScaledInputs) : Bool :=
  s.wCheck &&
  (((List.finRange 242).all (fun i =>
    (List.finRange 242).all (c.HDGate s i))) &&
  (((List.finRange 242).all (fun i =>
    (List.finRange 242).all (c.AGate s i))) &&
  ((List.finRange 242).all (c.vectorGate s))))

def NF626CenterCache.Valid (c : NF626CenterCache) (s : NF626ScaledInputs) : Prop :=
  (∀ j, (s.w j:ℚ)/s.T = neutralNF625W j) ∧
  (∀ i j, c.HD i j = neutralNF626Dot (s.H i) (fun k => s.D k j)) ∧
  (∀ i j, c.A i j = neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j)) ∧
  (∀ i, c.Vw i = neutralNF626Dot (s.V i) s.w ∧
    c.b i = neutralNF626Dot (fun k => s.D k i) c.Vw ∧
    c.Ay i = neutralNF626Dot (c.A i) s.y ∧
    c.Dy i = neutralNF626Dot (s.D i) s.y)

theorem NF626CenterCache.check_sound (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hc : c.check s = true) : c.Valid s := by
  unfold check NF626ScaledInputs.wCheck at hc
  simp only [Bool.and_eq_true] at hc
  refine ⟨?_,?_,?_,?_⟩
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp hc.1) j (by simp))
  · intro i j
    have hi := (List.all_eq_true.mp hc.2.1) i (by simp)
    exact of_decide_eq_true ((List.all_eq_true.mp hi) j (by simp))
  · intro i j
    have hi := (List.all_eq_true.mp hc.2.2.1) i (by simp)
    exact of_decide_eq_true ((List.all_eq_true.mp hi) j (by simp))
  · intro i
    exact of_decide_eq_true ((List.all_eq_true.mp hc.2.2.2) i (by simp))

def NF626ScaledInputs.aden (s : NF626ScaledInputs) : ℚ := (s.Q:ℚ)*s.S*s.S

def NF626ScaledInputs.bden (s : NF626ScaledInputs) : ℚ := (s.Q:ℚ)*s.S*s.T

theorem NF626CenterCache.A_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hc : c.Valid s) (i j : Fin 242) :
    s.payment.A i j = (c.A i j:ℚ)/s.aden := by
  unfold NF625PaymentData.A NF626ScaledInputs.payment
  have hi (k : Fin 242) :
      (∑ l, ((s.H k l:ℚ)/s.Q)*((s.D l j:ℚ)/s.S)) =
        (c.HD k j:ℚ)/((s.Q:ℚ)*s.S) := by
    rw [neutralNF626ScaledDot,← hc.2.1 k j]
  simp only [hi]
  rw [neutralNF626ScaledDot,← hc.2.2.1 i j]
  congr 1
  unfold NF626ScaledInputs.aden
  ring

theorem NF626CenterCache.b_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hc : c.Valid s) (i : Fin 242) :
    s.payment.b i = (c.b i:ℚ)/s.bden := by
  unfold NF625PaymentData.b NF626ScaledInputs.payment
  have hi (k : Fin 242) :
      (∑ j : Fin 4, ((s.V k j:ℚ)/s.Q)*neutralNF625W j) =
        (c.Vw k:ℚ)/((s.Q:ℚ)*s.T) := by
    simp_rw [← hc.1]
    rw [neutralNF626ScaledDot,← (hc.2.2.2 k).1]
  simp only [hi]
  rw [neutralNF626ScaledDot,← (hc.2.2.2 i).2.1]
  congr 1
  unfold NF626ScaledInputs.bden
  ring

theorem NF626CenterCache.Ay_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hc : c.Valid s) (i : Fin 242) :
    (∑ j, s.payment.A i j * s.payment.y0 j) =
      (c.Ay i:ℚ)/(s.aden*s.U) := by
  change (∑ j, s.payment.A i j * ((s.y j:ℚ)/s.U)) = _
  simp only [c.A_eq s hc]
  rw [neutralNF626ScaledDot,← (hc.2.2.2 i).2.2.1]

theorem NF626CenterCache.Dy_eq (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hc : c.Valid s) (i : Fin 242) :
    (∑ j, s.payment.D i j * s.payment.y0 j) =
      (c.Dy i:ℚ)/((s.S:ℚ)*s.U) := by
  simp only [NF626ScaledInputs.payment]
  rw [neutralNF626ScaledDot,← (hc.2.2.2 i).2.2.2]

end WeilDefect
