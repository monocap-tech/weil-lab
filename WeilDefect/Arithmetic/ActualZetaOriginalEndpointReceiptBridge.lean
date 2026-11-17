import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks
import WeilDefect.Arithmetic.ActualZetaOriginalSharedPiCertified
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointSignCheck

namespace WeilDefect
noncomputable section

/-! NF602: local equality gates imply the original endpoint checker.
The aggregate never assumes independently rounded source coefficients. -/

theorem neutralNF602Assembly_eq
    (hs : ∀ j : Fin 242, neutralNF602SelectedCheck j = true)
    (hc : ∀ j : Fin 32, neutralNF602CriticalCheck j = true)
    (hp : neutralNF602PoleCheck = true) :
    neutralNF592OriginalJetBall 0 = neutralNF602Assembly := by
  have hsel (j : Fin 242) :
      neutralNF592SelectedJetBall neutralNF597PiReceipt neutralNF592Q 220 j 0 =
        neutralNF602Selected j := by
    have h := neutralNF602Equal_sound _ _ (hs j)
    change neutralNF593ReadBall (neutralNF593SelectedTable neutralNF597PiReceipt
      neutralNF592Q 220 1 j) 0 = _ at h
    rw [neutralNF593SelectedTable_read _ _ _ _ _ _ (by decide : 0<1)] at h
    exact h
  have hcrit (j : Fin 32) :
      neutralNF592OscillatorBall neutralNF597PiReceipt
        neutralNF587CriticalFrequencies[j.val]! neutralNF592Q 220 0 0 =
        neutralNF602Critical j := by
    have h := neutralNF602Equal_sound _ _ (hc j)
    change neutralNF593ReadBall (neutralNF593OscillatorTable neutralNF597PiReceipt
      neutralNF587CriticalFrequencies[j.val]! neutralNF592Q 220 0 1) 0 = _ at h
    rw [neutralNF593OscillatorTable_read _ _ _ _ _ _ _ (by decide : 0<1)] at h
    exact h
  have hpole : neutralNF592PoleBall neutralNF592Q 220 0 = neutralNF602Pole := by
    have h := neutralNF602Equal_sound _ _ hp
    change neutralNF593ReadBall (neutralNF593PoleTable neutralNF592Q 220 1) 0 = _ at h
    rw [neutralNF593PoleTable_read _ _ _ _ (by decide : 0<1)] at h
    exact h
  unfold neutralNF592OriginalJetBall neutralNF592SourceBall neutralNF602Assembly
  rw [neutralNF598PiReceipt_eq]
  simp only [neutralNF592CriticalContribution,neutralNF602CriticalAssembly,hsel,hcrit,hpole]

theorem neutralNF602EndpointCheck_of_receipts
    (hs : ∀ j : Fin 242, neutralNF602SelectedCheck j = true)
    (hc : ∀ j : Fin 32, neutralNF602CriticalCheck j = true)
    (hp : neutralNF602PoleCheck = true)
    (ha : neutralNF602AssemblyCheck = true)
    (hn : neutralNF602ReceiptSignCheck = true) :
    neutralNF597EndpointCheck = true := by
  have he := neutralNF602Assembly_eq hs hc hp
  have hagg : neutralNF602Assembly = neutralNF602Ball neutralNF602EndpointReceipt :=
    neutralNF602Equal_sound _ _ ha
  unfold neutralNF597EndpointCheck
  rw [neutralNF593SourceTable_read _ _ _ _ _ (by decide : 0<1)]
  change decide ((neutralNF592OriginalJetBall 0).mid+
    (neutralNF592OriginalJetBall 0).rad < -(1/10^11:ℚ)) = true
  rw [he,hagg]
  exact hn

end
end WeilDefect
