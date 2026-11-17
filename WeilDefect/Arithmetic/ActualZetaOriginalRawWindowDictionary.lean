import WeilDefect.Arithmetic.ActualZetaOriginalStripLogCarrier

namespace WeilDefect
noncomputable section
open MeasureTheory

/-!
NF581: a genuine compactly supported physical representative has
the same raw transform as its original window evaluation at EVERY
complex sample, not merely the almost-everywhere Fourier equality.
Independent of the endpoint-specific and mollifier proof chains.
-/

/-- Exact full complex sample dictionary for the original physical
L² class of a pointwise supported function. -/
theorem neutralNF581RawTransform_toLp_window
    (a : ℝ) (f : ℝ → ℂ) (hf : MemLp f 2 volume)
    (hs : ∀ x, x ∉ Set.Icc (-a) a → f x = 0)
    (z : ℂ) :
    neutralRawTransform f z =
      neutralWindowEvaluation a z (hf.toLp f) := by
  unfold neutralRawTransform neutralWindowEvaluation
  rw [← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [hf.coeFn_toLp] with x hx
  by_cases h : x ∈ Set.Icc (-a) a
  · rw [Set.indicator_of_mem h, hx]
  · rw [Set.indicator_of_notMem h, hs x h]
    simp

/-- The actual L² realization inherits the supported representative's
physical window, without changing its equivalence class. -/
theorem neutralNF581Raw_toLp_supported
    (a : ℝ) (f : ℝ → ℂ) (hf : MemLp f 2 volume)
    (hs : ∀ x, x ∉ Set.Icc (-a) a → f x = 0) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → (hf.toLp f) x = 0 := by
  filter_upwards [hf.coeFn_toLp] with x hx h
  rw [hx, hs x h]

end
end WeilDefect
