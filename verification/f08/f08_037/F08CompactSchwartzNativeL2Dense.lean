import WeilDefect.Morphology.NeutralCanonicalFormDomain
import Mathlib.Analysis.Normed.Lp.SmoothApprox
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal SchwartzMap

/-!
F08-037: an explicit compactly supported Schwartz dense class in the
actual original complex Lebesgue L² space RealComplexL2.

Use the actual Mathlib Schwartz-to-Lp continuous linear map, not a
surrogate space or L² formal sum. The frozen Mathlib v4.34.0 route is:
  MeasureTheory.Lp.dense_hasCompactSupport_contDiff
  HasCompactSupport.toSchwartzMap
Both lemmas belong to the actual pinned Mathlib, not newer main.

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
  -- Frozen Mathlib v4.34.0 already proves density of genuinely smooth,
  -- compactly supported Lp representatives. Convert them to actual Schwartz
  -- elements without changing the target L² equivalence class.
  have hbase :
      Dense {f : RealComplexL2 |
        ∃ g : ℝ → ℂ,
          f =ᵐ[volume] g ∧ HasCompactSupport g ∧ ContDiff ℝ ((⊤ : ℕ∞) : WithTop ℕ∞) g} := by
    exact MeasureTheory.Lp.dense_hasCompactSupport_contDiff
      (E := ℝ) (F := ℂ) (μ := (volume : Measure ℝ)) (p := 2) (by simp)
  apply hbase.mono
  intro f hf
  obtain ⟨g, hfg, hcompact, hsmooth⟩ := hf
  let sg : 𝓢(ℝ, ℂ) := hcompact.toSchwartzMap hsmooth
  refine ⟨sg, ?_, ?_⟩
  · change HasCompactSupport (sg : ℝ → ℂ)
    simpa only [sg, HasCompactSupport.toSchwartzMap_toFun] using hcompact
  · apply Lp.ext_iff.mpr
    have hsg := sg.coeFn_toLp 2 (volume : Measure ℝ)
    simpa only [SchwartzMap.toLpCLM_apply] using
      hsg.trans (by simpa only [sg, HasCompactSupport.toSchwartzMap_toFun] using hfg.symm)

#print axioms f08_037_compactSchwartz_denseInOriginalL2

end
end WeilDefect
