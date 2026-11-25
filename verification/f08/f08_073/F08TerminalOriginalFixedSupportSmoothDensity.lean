import WeilDefect.Generated.F08.TerminalOriginalWeightedDilation
import WeilDefect.Generated.F08.OriginalSupportedSmoothingReceiver
import WeilDefect.Generated.F08.OriginalFixedWindowAssemblyReceiver

namespace WeilDefect
noncomputable section

open MeasureTheory Filter FourierTransform
open scoped FourierTransform Topology

set_option maxHeartbeats 2000000 in
/-- Fixed-support smooth form-core approximation in the original canonical
logarithmic domain. Both approximations are actual native physical L²
classes, with an explicit compactly supported smooth representative in the
strict interior and arbitrary weighted-coordinate error. -/
theorem f08_073_original_fixedSupport_smooth_approx
    {a : ℝ} (ha : 0 < a) (f : neutralCanonicalLogFormDomain a)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ g : neutralCanonicalLogFormDomain a, ∃ h : ℝ → ℂ,
      ContDiff ℝ (↑(⊤ : ℕ∞)) h ∧ HasCompactSupport h ∧
      tsupport h ⊆ Set.Ioo (-a) a ∧
      (g.val : ℝ → ℂ) =ᵐ[volume] h ∧
      ‖neutralLogWeightedL2 g - neutralLogWeightedL2 f‖ < ε := by
  have he : 0 < ε / 2 := by linarith
  obtain ⟨lam, hlam, hd⟩ :=
    f08_069_strictInward_exists_of_tendsto
      (fun lam : f08_059_inwardScale =>
        neutralLogWeightedL2 (f08_067_physicalDilation f lam))
      (neutralLogWeightedL2 f) (f08_067_weightedPhysicalDilation_tendsto f)
      (ε / 2) he
  let b := lam.1 * a
  let d : neutralCanonicalLogFormDomain b := f08_067_physicalDilation f lam
  have hb : b < a := by
    dsimp [b]
    simpa only [one_mul] using mul_lt_mul_of_pos_right hlam ha
  obtain ⟨n, hn, hs⟩ :=
    f08_069_eventualCollar_choice
      (fun n : ℕ => neutralLogWeightedL2
        (f08_068_smoothedDomain d (f08_017_shrinkingBump n)))
      (neutralLogWeightedL2 d) (fun n => (f08_017_shrinkingBump n).rOut)
      (f08_068_weightedSmoothing_tendsto d)
      f08_017_shrinkingBump_radius_tendsto_zero
      (a - b) (ε / 2) (sub_pos.mpr hb) he
  let φ := f08_017_shrinkingBump n
  have hc : b + φ.rOut < a := by
    change (f08_017_shrinkingBump n).rOut < a - b at hn
    dsimp [φ]
    linarith
  let s := f08_068_smoothedDomain d φ
  let g := f08_069_canonicalWiden hc.le s
  let h := f08_019_originalSmoothedWindow b d.val φ
  refine ⟨g, h, f08_019_original_smoothed_window_smooth b d.val φ,
    f08_019_original_smoothed_window_hasCompactSupport b d.val φ, ?_, ?_, ?_⟩
  · have hclosed : tsupport h ⊆ Set.Icc (-(b + φ.rOut)) (b + φ.rOut) := by
      change closure (Function.support h) ⊆ _
      exact closure_minimal
        (f08_019_original_smoothed_window_support_radius b d.val φ) isClosed_Icc
    exact hclosed.trans (f08_069_strictCollar_subset hc)
  · exact f08_021_original_smoothed_window_native_ae b d.val φ
  · change ‖neutralLogWeightedL2 (f08_069_canonicalWiden hc.le s) -
      neutralLogWeightedL2 f‖ < ε
    rw [f08_069_canonicalWiden_weighted_eq]
    have htri : ‖neutralLogWeightedL2 s - neutralLogWeightedL2 f‖ ≤
        ‖neutralLogWeightedL2 s - neutralLogWeightedL2 d‖ +
        ‖neutralLogWeightedL2 d - neutralLogWeightedL2 f‖ := by
      calc
        _ = ‖(neutralLogWeightedL2 s - neutralLogWeightedL2 d) +
              (neutralLogWeightedL2 d - neutralLogWeightedL2 f)‖ := by
                congr 1
                abel
        _ ≤ _ := norm_add_le _ _
    change ‖neutralLogWeightedL2 d - neutralLogWeightedL2 f‖ < ε / 2 at hd
    change ‖neutralLogWeightedL2 s - neutralLogWeightedL2 d‖ < ε / 2 at hs
    linarith

#print axioms f08_073_original_fixedSupport_smooth_approx

end
end WeilDefect
