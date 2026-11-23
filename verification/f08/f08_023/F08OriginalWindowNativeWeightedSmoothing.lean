import WeilDefect.Generated.F08.OriginalSmoothedWindowNativeFourier

namespace WeilDefect
noncomputable section
open MeasureTheory Filter FourierTransform
open scoped FourierTransform Topology

/-!
F08-023: original sharp physical window itself defines a source native
RealComplexL2 class. Under the *explicit* hypothesis that the Fourier
coordinate of THAT native sharp window has finite original log(e+|xi|)
energy, the genuinely smoothed source physical windows constructed and
attached to RealComplexL2 in F08-019/021 converge in the real source
logarithmic Fourier energy.

No hypothesis is silently transported from a full-line function to its
sharp cutoff: the window finite-energy assumption is independent.
This result gives weighted smoothing approximation of an already finite
energy WINDOW; it is NOT a proof that sharp cutoff preserves the log form
domain, and NOT a fixed-support smooth-core density proof. Mollifying
enlarges the physical support. Inward dilation remains open.
-/

/-- The original literal physical sharp-window indicator representative is
an actual L2 function, since indicator restriction cannot increase L2 norm. -/
theorem f08_023_original_window_memLp_two
    (a : ℝ) (f : RealComplexL2) :
    MemLp (neutralWindowRepresentative a f) 2 volume := by
  change MemLp ((Set.Icc (-a) a).indicator (f : ℝ → ℂ)) 2 volume
  exact MemLp.indicator measurableSet_Icc.nullMeasurableSet (Lp.memLp f)

/-- The genuine original sharp-window native L2 class; no artificial
frequency carrier is introduced. -/
def f08_023_originalWindowL2 (a : ℝ) (f : RealComplexL2) :
    RealComplexL2 :=
  (f08_023_original_window_memLp_two a f).toLp
    (neutralWindowRepresentative a f)

/-- The Lp representative is a.e. the original source literal indicator. -/
theorem f08_023_original_window_native_ae
    (a : ℝ) (f : RealComplexL2) :
    (f08_023_originalWindowL2 a f : ℝ → ℂ) =ᵐ[volume]
      neutralWindowRepresentative a f := by
  exact (f08_023_original_window_memLp_two a f).coeFn_toLp

/-- Native original sharp-window representative is also L1 by finite
physical source support, without assuming any smoothness. -/
theorem f08_023_original_window_native_integrable
    (a : ℝ) (f : RealComplexL2) :
    Integrable (f08_023_originalWindowL2 a f : ℝ → ℂ) volume := by
  exact (f08_007_original_window_representative_integrable a f).congr
    (f08_023_original_window_native_ae a f).symm

/-- Native Fourier of the original *sharp-window L2 class* equals exactly
the original -2pi evaluation almost everywhere, by the genuine source
L1/L2 Fourier agreement theorem. -/
theorem f08_023_original_window_native_fourier_ae
    (a : ℝ) (f : RealComplexL2) :
    (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) =ᵐ[volume]
      (fun ξ : ℝ =>
        neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) f) := by
  have hnative :=
    neutralIntegrableL2_fourier_ae
      (f08_023_originalWindowL2 a f)
      (f08_023_original_window_native_integrable a f)
  filter_upwards [hnative] with ξ hξ
  have hraw :=
    Real.fourier_congr_ae (f08_023_original_window_native_ae a f) ξ
  exact (hξ.trans hraw).trans (neutralWindowRepresentative_fourier a f ξ)

/-- The native Fourier difference between the actual smoothed and
unsmoothed original-window L2 classes is exactly the actual mollifier
symbol's difference times the native original-window Fourier coordinate,
almost everywhere, at each fixed physical bump. -/
theorem f08_023_original_window_native_mollifier_fourier_difference_ae
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    (fun ξ : ℝ =>
      (𝓕 (f08_021_originalSmoothedWindowL2 a f φ) : RealComplexL2) ξ -
      (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ)
      =ᵐ[volume]
    (fun ξ : ℝ =>
      (f08_015_originalMollifierMultiplier φ ξ - 1) *
      (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ) := by
  filter_upwards
    [f08_021_original_smoothed_window_native_fourier_product_ae a f φ,
      f08_023_original_window_native_fourier_ae a f]
    with ξ hs hw
  rw [hs, hw]
  ring

/-- The exact original logarithmic frequency-energy integral for the
native smoothed-minus-unsmoothed window equals the already-certified
true physical mollifier multiplier error, with no false pointwise
equality of arbitrary L2 representatives. -/
theorem f08_023_original_window_native_log_error_integral_eq
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    (∫ ξ : ℝ, logarithmicFourierWeight ξ *
      ‖(𝓕 (f08_021_originalSmoothedWindowL2 a f φ) : RealComplexL2) ξ -
        (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ‖ ^ 2 ∂volume) =
    (∫ ξ : ℝ, logarithmicFourierWeight ξ *
      ‖(f08_015_originalMollifierMultiplier φ ξ - 1) *
        (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ‖ ^ 2 ∂volume) := by
  apply integral_congr_ae
  filter_upwards
    [f08_023_original_window_native_mollifier_fourier_difference_ae a f φ]
    with ξ hξ
  rw [hξ]

/-- True original physical-window smooth mollifier regularization converges
in the logarithmic Fourier energy of its NATIVE L2 difference. The one
remaining energy premise is explicitly on the original SHARP WINDOW
itself, not improperly transferred from an arbitrary global form element.
The source-physical smoothed functions are C-infinity and compactly
supported but have support collars [-a-r_n,a+r_n], not strict [-a,a]. -/
theorem f08_023_original_window_native_weighted_smoothing_tendsto_zero
    (a : ℝ) (f : RealComplexL2)
    (hwindow : Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ *
        ‖(𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ‖ ^ 2)
      volume) :
    Tendsto (fun n : ℕ =>
      ∫ ξ : ℝ, logarithmicFourierWeight ξ *
        ‖(𝓕 (f08_021_originalSmoothedWindowL2 a f
            (f08_017_shrinkingBump n)) : RealComplexL2) ξ -
          (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ‖ ^ 2 ∂volume)
      atTop (𝓝 (0 : ℝ)) := by
  have heq :
      (fun n : ℕ =>
        ∫ ξ : ℝ, logarithmicFourierWeight ξ *
          ‖(𝓕 (f08_021_originalSmoothedWindowL2 a f
              (f08_017_shrinkingBump n)) : RealComplexL2) ξ -
            (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ‖ ^ 2 ∂volume) =
      (fun n : ℕ =>
        ∫ ξ : ℝ, logarithmicFourierWeight ξ *
          ‖(f08_015_originalMollifierMultiplier
              (f08_017_shrinkingBump n) ξ - 1) *
            (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) ξ‖ ^ 2 ∂volume) := by
    funext n
    exact f08_023_original_window_native_log_error_integral_eq
      a f (f08_017_shrinkingBump n)
  rw [heq]
  exact f08_017_explicit_mollifier_weighted_error_tendsto_zero
    (𝓕 (f08_023_originalWindowL2 a f) : RealComplexL2) hwindow

#print axioms f08_023_original_window_memLp_two
#print axioms f08_023_original_window_native_ae
#print axioms f08_023_original_window_native_integrable
#print axioms f08_023_original_window_native_fourier_ae
#print axioms f08_023_original_window_native_mollifier_fourier_difference_ae
#print axioms f08_023_original_window_native_log_error_integral_eq
#print axioms f08_023_original_window_native_weighted_smoothing_tendsto_zero

end
end WeilDefect
