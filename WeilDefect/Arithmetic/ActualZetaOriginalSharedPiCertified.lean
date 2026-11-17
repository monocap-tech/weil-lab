import WeilDefect.Arithmetic.ActualZetaOriginalSharedPiReceipt
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointPhase

namespace WeilDefect

/-! NF598: promote the exact successful NF597 kernel-only experiment.
Run 44174249972, job 134361223655 checked both original gate and
equality using decide +kernel, with only propext, Classical.choice,
Quot.sound in its printed axiom list. This module still needs its
own compilation on the new head. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

theorem neutralNF598PiReceipt_check : neutralNF597PiReceiptCheck = true := by
  decide +kernel

theorem neutralNF598PiReceipt_eq :
    neutralNF592PiBall neutralNF592Q 200 = neutralNF597PiReceipt :=
  neutralNF597PiReceipt_of_check neutralNF598PiReceipt_check

theorem neutralNF598PiReceipt_sound : neutralNF597PiReceipt.Contains Real.pi := by
  rw [← neutralNF598PiReceipt_eq]
  exact neutralNF592PiBall_sound neutralNF592Q 200 neutralNF592Q_pos
    neutralNF592Atan5Fee neutralNF592Atan239Fee

#print axioms neutralNF598PiReceipt_eq
#print axioms neutralNF598PiReceipt_sound

end WeilDefect
