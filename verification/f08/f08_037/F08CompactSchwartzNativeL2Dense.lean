import WeilDefect.Morphology.NeutralCanonicalFormDomain
import Mathlib.Analysis.Distribution.SchwartzSpace.CompactSupport

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal

/-!
F08-037: an explicit compactly supported Schwartz dense class in the
actual original complex Lebesgue L² space RealComplexL2.

Use the actual Mathlib Schwartz-to-Lp continuous linear map, not a
surrogate space or L² formal sum. Two independently proved Mathlib
theorems provide the exact density composition:
  SchwartzMap.dense_hasCompactSupport
  SchwartzMap.denseRange_toLpCLM

This is the candidate core for F08 native L² dilation strong continuity.
Frequency compact support is NOT physical support after Fourier
transformation and NOT the original supported logarithmic form core.
The density theorem does not prove dilation strong continuity.
-/

/-- Compactly supported complex Schwartz functions are dense in the
true Lebesgue-measure source RealComplexL2 after the native toLp map. -/
theorem f08_037_compactSchwartz_denseInOriginalL2 :
    Dense
      ((SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ)) ''
        {g : 𝓢(ℝ, ℂ) | HasCompactSupport (g : ℝ → ℂ)}) := by
  have hLp :
      DenseRange (SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ)) := by
    exact SchwartzMap.denseRange_toLpCLM (E := ℝ) (F := ℂ)
      (p := 2) (μ := (volume : Measure ℝ)) (by simp)
  have hcompact :
      Dense {g : 𝓢(ℝ, ℂ) | HasCompactSupport (g : ℝ → ℂ)} :=
    SchwartzMap.dense_hasCompactSupport
  exact hLp.dense_image
    (SchwartzMap.toLpCLM ℝ ℂ 2 (volume : Measure ℝ)).continuous hcompact

#print axioms f08_037_compactSchwartz_denseInOriginalL2

end
end WeilDefect
