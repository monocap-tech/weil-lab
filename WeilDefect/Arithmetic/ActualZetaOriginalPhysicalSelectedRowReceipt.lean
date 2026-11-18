import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerPayments

namespace WeilDefect
open Finset

/-! The selected-box row is independent of the H,V centers and
the HD/A cache. Check the two integer numerators and the scalar
payment, for a proposed residual bound r. This alone does not
establish that r bounds the physical residual. -/

def neutralNF630SelectedRowCheck (d y : Fin 242 → ℤ) (S U : ℕ)
    (r : ℚ) (i : Fin 242) (dy mass : ℤ) : Bool :=
  decide (0<S ∧ 0<U ∧ 0≤r ∧
    dy=neutralNF626Dot d y ∧ mass=(∑ j, |d j|) ∧
    |(dy:ℚ)/((S:ℚ)*U)-neutralNF625Mid i|+
      ((mass:ℚ)/S)*(2*r) ≤ neutralNF625Rad i)

theorem neutralNF630SelectedRow_sound (d y : Fin 242 → ℤ) (S U : ℕ)
    (r : ℚ) (i : Fin 242) (dy mass : ℤ)
    (hc : neutralNF630SelectedRowCheck d y S U r i dy mass=true) :
    |(∑ j, ((d j:ℚ)/S)*((y j:ℚ)/U))-neutralNF625Mid i|+
      (∑ j, |(d j:ℚ)/S|)*(2*r) ≤ neutralNF625Rad i := by
  have h : 0<S ∧ 0<U ∧ 0≤r ∧
      dy=neutralNF626Dot d y ∧ mass=(∑ j, |d j|) ∧
      |(dy:ℚ)/((S:ℚ)*U)-neutralNF625Mid i|+
        ((mass:ℚ)/S)*(2*r) ≤ neutralNF625Rad i :=
    of_decide_eq_true hc
  rw [neutralNF626ScaledDot,neutralNF626AbsSum,← h.2.2.2.1,← h.2.2.2.2.1]
  exact h.2.2.2.2.2

theorem neutralNF630SelectedPayment_of_row (s : NF626ScaledInputs)
    (i : Fin 242) (dy mass : ℤ)
    (hc : neutralNF630SelectedRowCheck (s.D i) s.y s.S s.U s.r i dy mass=true) :
    s.payment.payment i ≤ neutralNF625Rad i := by
  exact neutralNF630SelectedRow_sound (s.D i) s.y s.S s.U s.r i dy mass hc

end WeilDefect
