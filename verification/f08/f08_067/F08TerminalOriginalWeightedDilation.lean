import WeilDefect.Generated.F08.OriginalLogCorrectedDilationConvergence
import WeilDefect.Generated.F08.OriginalNativePhysicalFourierIdentity
import WeilDefect.Generated.F08.OriginalWeightedCoordinateIdentity
import WeilDefect.Generated.F08.OriginalFormDomainEnergyReceiver

namespace WeilDefect
noncomputable section

open MeasureTheory FourierTransform Filter
open scoped FourierTransform Topology

theorem f08_067_scale_pos (lam : f08_059_inwardScale) : 0 < lam.1 :=
  lt_of_lt_of_le (by norm_num) lam.2.1

/-- The inward physical dilation belongs to the actual smaller canonical
domain. The target finite energy is derived, not assumed. -/
theorem f08_067_physicalDilation_mem {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) (lam : f08_059_inwardScale) :
    f08_060_originalPhysicalDilation lam.1 (f08_067_scale_pos lam) f.val ∈
      neutralCanonicalLogFormDomain (lam.1 * a) := by
  let g := f08_060_originalPhysicalDilation lam.1 (f08_067_scale_pos lam) f.val
  have hfour := f08_062_originalPhysicalDilation_fourier a lam.1
    (f08_067_scale_pos lam) f.val f.property.1
  have hae := f08_063_weightedCoordinate_ae f lam.1 (f08_067_scale_pos lam) g hfour
  have hm := f08_063_correctedNative_memLp lam.1 lam.2.1 lam.2.2
    (f08_030_nativeFrequencyDilation lam.1 (ne_of_gt (f08_067_scale_pos lam))
      (neutralLogWeightedL2 f))
  exact f08_064_originalDomain_mem_of_weighted_memLp (lam.1 * a) g
    (f08_060_originalPhysicalDilation_supported a lam.1 (f08_067_scale_pos lam)
      f.val f.property.1) ((memLp_congr_ae hae).mpr hm)

def f08_067_physicalDilation {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) (lam : f08_059_inwardScale) :
    neutralCanonicalLogFormDomain (lam.1 * a) :=
  ⟨_, f08_067_physicalDilation_mem f lam⟩

/-- Exact original weighted Hilbert distance equals the corrected native
error integral, with the genuine target domain coordinate. -/
theorem f08_067_weightedDifference_sq {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) (lam : f08_059_inwardScale) :
    ‖neutralLogWeightedL2 (f08_067_physicalDilation f lam) -
        neutralLogWeightedL2 f‖ ^ 2 =
      ∫ xi : ℝ, ‖f08_059_correctedError lam (neutralLogWeightedL2 f) xi‖ ^ 2 ∂volume := by
  let g := f08_067_physicalDilation f lam
  have hfour : (𝓕 g.val : RealComplexL2) =
      f08_030_nativeFrequencyDilation lam.1 (ne_of_gt (f08_067_scale_pos lam))
        (𝓕 f.val : RealComplexL2) :=
    f08_062_originalPhysicalDilation_fourier a lam.1
      (f08_067_scale_pos lam) f.val f.property.1
  have hae := f08_063_weightedCoordinate_ae f lam.1 (f08_067_scale_pos lam) g.val hfour
  rw [f08_064_originalWeightedDifference_norm_sq]
  apply integral_congr_ae
  filter_upwards [hae, neutralLogWeightedL2_coe f] with xi hx hf
  change (Real.sqrt (logarithmicFourierWeight xi) : ℂ) *
    (𝓕 g.val : RealComplexL2) xi = f08_025_logDilationFactor lam.1 xi •
      f08_030_nativeFrequencyDilation lam.1 (ne_of_gt (f08_067_scale_pos lam))
        (neutralLogWeightedL2 f) xi at hx
  change ‖neutralLogWeightedFourier g xi - neutralLogWeightedFourier f xi‖ ^ 2 =
    ‖f08_059_correctedError lam (neutralLogWeightedL2 f) xi‖ ^ 2
  rw [← hf]
  change ‖(Real.sqrt (logarithmicFourierWeight xi) : ℂ) *
    (𝓕 g.val : RealComplexL2) xi - neutralLogWeightedL2 f xi‖ ^ 2 = _
  rw [hx]
  rfl

set_option maxHeartbeats 2000000 in
/-- Strong weighted convergence on the actual original canonical domains,
with support radius depending on the inward scale. -/
theorem f08_067_weightedPhysicalDilation_tendsto {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    Tendsto (fun lam : f08_059_inwardScale =>
      neutralLogWeightedL2 (f08_067_physicalDilation f lam))
      (𝓝 (⟨1, by constructor <;> norm_num⟩ : f08_059_inwardScale))
      (𝓝 (neutralLogWeightedL2 f)) := by
  let oneScale : f08_059_inwardScale := ⟨1, by constructor <;> norm_num⟩
  let l := 𝓝 oneScale
  have he : Tendsto (fun lam : f08_059_inwardScale =>
      ∫ xi : ℝ, ‖f08_059_correctedError lam (neutralLogWeightedL2 f) xi‖ ^ 2 ∂volume)
      l (𝓝 (0 : ℝ)) := f08_059_correctedError_integral_tendsto _
  change Tendsto _ l _
  rw [Metric.tendsto_nhds]
  intro ε hε
  filter_upwards [(Metric.tendsto_nhds.mp he) (ε ^ 2) (sq_pos_of_pos hε)] with lam hh
  rw [Real.dist_eq, sub_zero] at hh
  rw [dist_eq_norm]
  have hsq := f08_067_weightedDifference_sq f lam
  have hlt : ‖neutralLogWeightedL2 (f08_067_physicalDilation f lam) -
      neutralLogWeightedL2 f‖ ^ 2 < ε ^ 2 :=
    hsq.trans_lt (lt_of_le_of_lt (le_abs_self _) hh)
  nlinarith [norm_nonneg (neutralLogWeightedL2 (f08_067_physicalDilation f lam) -
    neutralLogWeightedL2 f)]

#print axioms f08_067_scale_pos
#print axioms f08_067_physicalDilation_mem
#print axioms f08_067_weightedDifference_sq
#print axioms f08_067_weightedPhysicalDilation_tendsto

end
end WeilDefect
