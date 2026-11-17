import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointComputationalCore

namespace WeilDefect

/-! NF597: one shared subcomputation, not a whole-source kernel trial.
The literal integer receipt was independently reconstructed from the
NF591 exact directed rounding recurrence. No equality is assumed.
Kernel proof of this equality would allow every subsequent phase
certificate to rewrite the shared Machin computation once. -/

def neutralNF597PiReceipt : NF591Ball :=
  ⟨(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712017872:ℚ)/neutralNF592Q,(3958:ℚ)/neutralNF592Q⟩

def neutralNF597PiReceiptCheck : Bool :=
  let p := neutralNF592PiBall neutralNF592Q 200
  decide (p.mid = neutralNF597PiReceipt.mid ∧ p.rad = neutralNF597PiReceipt.rad)

theorem neutralNF597PiReceipt_of_check
    (h : neutralNF597PiReceiptCheck = true) :
    neutralNF592PiBall neutralNF592Q 200 = neutralNF597PiReceipt := by
  have hh : (neutralNF592PiBall neutralNF592Q 200).mid = neutralNF597PiReceipt.mid ∧
      (neutralNF592PiBall neutralNF592Q 200).rad = neutralNF597PiReceipt.rad :=
    of_decide_eq_true h
  have he (a b : NF591Ball) (hm : a.mid = b.mid) (hr : a.rad = b.rad) : a = b := by
    cases a
    cases b
    simp_all
  exact he _ _ hh.1 hh.2

end WeilDefect
