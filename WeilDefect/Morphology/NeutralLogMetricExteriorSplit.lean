import WeilDefect.Morphology.NeutralLogMetricEndpointBounds
import Mathlib.MeasureTheory.Group.Measure

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- Genuine convergence of the right exterior spatial kernel integral. -/
theorem neutralLogMetricJump_right_exterior_integrable
    (B x : ℝ) (hx : x < B) :
    IntegrableOn (fun y : ℝ => neutralLogMetricJumpDensity |x - y|) (Ioi B) := by
  have hs : (fun y : ℝ => y + (-x)) ⁻¹' Ioi (B - x) = Ioi B := by
    ext y
    simp only [mem_preimage, mem_Ioi]
    constructor <;> intro h <;> linarith
  have hp := (measurePreserving_add_right (volume : Measure ℝ) (-x)).restrict_preimage
    (measurableSet_Ioi : MeasurableSet (Ioi (B - x)))
  rw [hs] at hp
  have hi := hp.integrable_comp_of_integrable
    (neutralLogMetricEndpointTail_integrable (B - x) (by linarith))
  apply hi.congr_fun _ measurableSet_Ioi
  intro y hy
  change neutralLogMetricJumpDensity (y + (-x)) = neutralLogMetricJumpDensity |x - y|
  congr 1
  rw [abs_of_neg (by linarith [hy] : x - y < 0)]
  ring

/-- Genuine convergence of the left exterior spatial kernel integral. -/
theorem neutralLogMetricJump_left_exterior_integrable
    (B x : ℝ) (hx : -B < x) :
    IntegrableOn (fun y : ℝ => neutralLogMetricJumpDensity |x - y|) (Iio (-B)) := by
  have hs : (fun y : ℝ => x - y) ⁻¹' Ioi (B + x) = Iio (-B) := by
    ext y
    simp only [mem_preimage, mem_Ioi, mem_Iio]
    constructor <;> intro h <;> linarith
  have hp := (measurePreserving_sub_left (volume : Measure ℝ) x).restrict_preimage
    (measurableSet_Ioi : MeasurableSet (Ioi (B + x)))
  rw [hs] at hp
  have hi := hp.integrable_comp_of_integrable
    (neutralLogMetricEndpointTail_integrable (B + x) (by linarith))
  apply hi.congr_fun _ measurableSet_Iio
  intro y hy
  change neutralLogMetricJumpDensity (x - y) = neutralLogMetricJumpDensity |x - y|
  rw [abs_of_pos (by linarith [hy] : 0 < x - y)]

/-- The actual right exterior kernel integral is the distance-to-right tail. -/
theorem neutralLogMetricJump_right_exterior_integral
    (B x : ℝ) (hx : x < B) :
    (∫ y in Ioi B, neutralLogMetricJumpDensity |x - y|) =
      neutralLogMetricEndpointTail (B - x) := by
  have hs : (fun y : ℝ => y + (-x)) ⁻¹' Ioi (B - x) = Ioi B := by
    ext y
    simp only [mem_preimage, mem_Ioi]
    constructor <;> intro h <;> linarith
  have he := (measurePreserving_add_right (volume : Measure ℝ) (-x)).setIntegral_preimage_emb
    (MeasurableEquiv.addRight (-x)).measurableEmbedding
    neutralLogMetricJumpDensity (Ioi (B - x))
  rw [hs] at he
  calc
    (∫ y in Ioi B, neutralLogMetricJumpDensity |x - y|) =
        ∫ y in Ioi B, neutralLogMetricJumpDensity (y + (-x)) := by
      apply setIntegral_congr_fun measurableSet_Ioi
      intro y hy
      change neutralLogMetricJumpDensity |x - y| = neutralLogMetricJumpDensity (y + (-x))
      congr 1
      rw [abs_of_neg (by linarith [hy] : x - y < 0)]
      ring
    _ = neutralLogMetricEndpointTail (B - x) := he

/-- The actual left exterior kernel integral is the distance-to-left tail. -/
theorem neutralLogMetricJump_left_exterior_integral
    (B x : ℝ) (hx : -B < x) :
    (∫ y in Iio (-B), neutralLogMetricJumpDensity |x - y|) =
      neutralLogMetricEndpointTail (B + x) := by
  have hs : (fun y : ℝ => x - y) ⁻¹' Ioi (B + x) = Iio (-B) := by
    ext y
    simp only [mem_preimage, mem_Ioi, mem_Iio]
    constructor <;> intro h <;> linarith
  have hm : MeasurableEmbedding (fun y : ℝ => x - y) := by
    simpa only [sub_eq_add_neg, Function.comp_def] using
      (MeasurableEquiv.addLeft x).measurableEmbedding.comp
        (MeasurableEquiv.neg ℝ).measurableEmbedding
  have he := (measurePreserving_sub_left (volume : Measure ℝ) x).setIntegral_preimage_emb
    hm neutralLogMetricJumpDensity (Ioi (B + x))
  rw [hs] at he
  calc
    (∫ y in Iio (-B), neutralLogMetricJumpDensity |x - y|) =
        ∫ y in Iio (-B), neutralLogMetricJumpDensity (x - y) := by
      apply setIntegral_congr_fun measurableSet_Iio
      intro y hy
      change neutralLogMetricJumpDensity |x - y| = neutralLogMetricJumpDensity (x - y)
      rw [abs_of_pos (by linarith [hy] : 0 < x - y)]
    _ = neutralLogMetricEndpointTail (B + x) := he

end
end WeilDefect
