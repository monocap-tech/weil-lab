import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptBridge

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! NF603 promotes the exact successful NF602 kernel experiments.
The other selected and critical modes and independent pole check
remain explicit premises. -/

theorem neutralNF603ReceiptSign : neutralNF602ReceiptSignCheck = true := by
  decide +kernel

theorem neutralNF603ReceiptAssembly : neutralNF602AssemblyCheck = true := by
  decide +kernel

theorem neutralNF603SelectedZero : neutralNF602SelectedCheck (0:Fin 242) = true := by
  decide +kernel

theorem neutralNF603EndpointCheck_of_modes
    (hs : ∀ j : Fin 242, neutralNF602SelectedCheck j = true)
    (hc : ∀ j : Fin 32, neutralNF602CriticalCheck j = true)
    (hp : neutralNF602PoleCheck = true) :
    neutralNF597EndpointCheck = true :=
  neutralNF602EndpointCheck_of_receipts hs hc hp
    neutralNF603ReceiptAssembly neutralNF603ReceiptSign

#print axioms neutralNF603ReceiptSign
#print axioms neutralNF603ReceiptAssembly
#print axioms neutralNF603SelectedZero

end WeilDefect
