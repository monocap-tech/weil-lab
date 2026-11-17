import WeilDefect.Arithmetic.ActualZetaOriginalEndpointModeReceipts
import WeilDefect.Arithmetic.ActualZetaOriginalSharedPiReceipt

namespace WeilDefect
open Finset

/-! The executable checker uses the same cached order-zero mode
 evaluator and exact primitive arithmetic as NF593. No transcendental
 evaluation is repeated during aggregate receipt verification. -/

def neutralNF602Ball (p : ℤ × ℤ) : NF591Ball :=
  ⟨(p.1:ℚ)/neutralNF592Q,(p.2:ℚ)/neutralNF592Q⟩

def neutralNF602Equal (a b : NF591Ball) : Bool :=
  decide (a.mid=b.mid ∧ a.rad=b.rad)

theorem neutralNF602Equal_sound (a b : NF591Ball)
    (h : neutralNF602Equal a b = true) : a=b := by
  have h' : a.mid=b.mid ∧ a.rad=b.rad := of_decide_eq_true h
  cases a
  cases b
  simp_all

def neutralNF602Selected (j : Fin 242) : NF591Ball :=
  neutralNF602Ball neutralNF602SelectedReceipts[j.val]!

def neutralNF602Critical (j : Fin 32) : NF591Ball :=
  neutralNF602Ball neutralNF602CriticalReceipts[j.val]!

def neutralNF602Pole : NF591Ball := neutralNF602Ball neutralNF602PoleReceipt

def neutralNF602SelectedCheck (j : Fin 242) : Bool :=
  neutralNF602Equal
    (neutralNF593ReadBall (neutralNF593SelectedTable
      neutralNF597PiReceipt neutralNF592Q 220 1 j) 0)
    (neutralNF602Selected j)

def neutralNF602CriticalCheck (j : Fin 32) : Bool :=
  neutralNF602Equal
    (neutralNF593ReadBall (neutralNF593OscillatorTable
      neutralNF597PiReceipt neutralNF587CriticalFrequencies[j.val]!
      neutralNF592Q 220 0 1) 0)
    (neutralNF602Critical j)

def neutralNF602PoleCheck : Bool :=
  neutralNF602Equal
    (neutralNF593ReadBall (neutralNF593PoleTable neutralNF592Q 220 1) 0)
    neutralNF602Pole

def neutralNF602CriticalAssembly (b : NF591Ball) (j : Fin 4) : NF591Ball :=
  (neutralNF592BallSum univ (fun k : Fin 32 =>
    ((((b.mul (NF591Ball.exactQ ((neutralNF587CriticalSines[j.val]!)[k.val]!)
      neutralNF592Q)).round neutralNF592Q).mul (neutralNF602Critical k)).round neutralNF592Q))).add
    ((((b.mul (NF591Ball.exactQ neutralNF587CriticalPoles[j.val]! neutralNF592Q)).round
      neutralNF592Q).mul neutralNF602Pole).round neutralNF592Q)

def neutralNF602Assembly : NF591Ball :=
  (neutralNF592BallSum univ (fun j : Fin 242 =>
    ((neutralNF592PrimitiveBox neutralNF587SelectedDyads[j.val]! neutralNF592Q).mul
      (neutralNF602Selected j)).round neutralNF592Q)).add
    (neutralNF592BallSum univ (fun j : Fin 4 =>
      neutralNF602CriticalAssembly
        (neutralNF592PrimitiveBox neutralNF587CriticalDyads[j.val]! neutralNF592Q) j))

def neutralNF602AssemblyCheck : Bool :=
  neutralNF602Equal neutralNF602Assembly (neutralNF602Ball neutralNF602EndpointReceipt)

def neutralNF602ReceiptSignCheck : Bool :=
  decide ((neutralNF602Ball neutralNF602EndpointReceipt).mid +
    (neutralNF602Ball neutralNF602EndpointReceipt).rad < -(1/10^11:ℚ))

end WeilDefect
