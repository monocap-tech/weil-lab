import WeilDefect.MasterRecon.V10B9b
import WeilDefect.MasterRecon.V10B8h
import WeilDefect.MasterRecon.V10B7e

/-! V10B9c: density, signed defect and positive-channel coercivity.
The three external attachments are not axioms: they remain theorem
parameters, together with critical-line supply. -/
namespace WeilDefect.MasterRecon.V10B9c

open scoped InnerProduct NNReal
open V08I (logCarrier physicalInclusion)
open V10B6c (signedGram analysisChannel)

theorem literal_core_dense (hOld : V10B9b.OldApproximation)
    (t : ℝ) (ht : 0 < t) : Dense (V10B8h.SmoothCore t) :=
  V10B9b.core_dense_of_old hOld t ht

theorem arithmetic_coercivity (t : ℝ) (ht : 0 < t)
    (hOld : V10B9b.OldApproximation)
    (hStirling : V10B8f.VerticalStirling)
    (hEF : V10B8b.LiteralEF)
    (hSupply : V09C.SuperlinearSupply V09C.CriticalSample) :
    ∃ T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index,
      V10B6d.LiteralCoordinates t T ∧
      (∃ K : logCarrier t →L[ℂ] logCarrier t,
        IsCompactOperator K ∧ signedGram T = 1+K) ∧
      (∃ b : ℝ≥0, 0 < b ∧ ∀ g : logCarrier t,
        ‖g‖^2*(b:ℝ) ≤ ‖analysisChannel true T g‖^2) := by
  obtain ⟨T,hT⟩ := V10B7e.arithmetic_analysis t ht.le
  obtain ⟨hd,C,hC0,hC⟩ := V10B8f.residual_of_stirling hStirling
  have hcore := literal_core_dense hOld t ht
  have hid := V10B8h.arithmetic_operator_identity t ht.le hd C hC T hT hEF hcore
  obtain ⟨K,hK,hKeq⟩ := V10B8h.arithmetic_compact_perturbation t ht.le hd C hC
  obtain ⟨M,hM,hdef⟩ := V10B8h.signed_defect t ht.le hd C hC hC0 T hT hEF hcore
  exact ⟨T,hT,⟨K,hK,hid.trans hKeq⟩,
    V10B6i.positive_coercivity t ht.le T hT hSupply M hM hdef⟩

end WeilDefect.MasterRecon.V10B9c

#print axioms WeilDefect.MasterRecon.V10B9c.literal_core_dense
#print axioms WeilDefect.MasterRecon.V10B9c.arithmetic_coercivity
