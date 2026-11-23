import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import Mathlib.Analysis.Calculus.BumpFunction.Normed
import Mathlib.Analysis.Fourier.FourierTransform

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped FourierTransform

/-!
F08-011: actual positive, compactly supported, normalized smooth complex
mollifier from pinned Mathlib's ContDiffBump.normed (not an assumed
multiplier). The ambient physical variable is the source's real log coordinate.

The target is the spectral contraction and physical support components for
a genuine mollifier. Fourier convergence as rOut → 0, physical smoothing
of an arbitrary L² window and log-Hilbert density remain separate gates.
-/

/-- A real, nonnegative, L¹-mass-one smooth bump as a complex function.
It lives on the same real physical coordinate used by the original Weil
window representative. -/
def f08_011_complexMollifier (φ : ContDiffBump (0 : ℝ)) : ℝ → ℂ :=
  fun x => (φ.normed volume x : ℂ)

/-- The actual normalized complex mollifier is pointwise a nonnegative real. -/
theorem f08_011_complexMollifier_nonneg
    (φ : ContDiffBump (0 : ℝ)) (x : ℝ) :
    0 ≤ (f08_011_complexMollifier φ x).re := by
  simpa [f08_011_complexMollifier] using
    (φ.nonneg_normed (μ := volume) x)

/-- The true physical mollifier is integrable, not only an abstract
pointwise multiplier. -/
theorem f08_011_complexMollifier_integrable
    (φ : ContDiffBump (0 : ℝ)) :
    Integrable (f08_011_complexMollifier φ) volume := by
  simpa [f08_011_complexMollifier, Function.comp_def] using
    Complex.ofRealCLM.integrable_comp (φ.integrable_normed (μ := volume))

/-- Normalization in the actual complex Fourier/convolution scalar field. -/
theorem f08_011_complexMollifier_integral
    (φ : ContDiffBump (0 : ℝ)) :
    (∫ x : ℝ, f08_011_complexMollifier φ x ∂volume) = (1 : ℂ) := by
  simp [f08_011_complexMollifier, integral_ofReal,
    φ.integral_normed (μ := volume)]

/-- The complex norm equals the underlying positive real bump. -/
theorem f08_011_complexMollifier_norm
    (φ : ContDiffBump (0 : ℝ)) (x : ℝ) :
    ‖f08_011_complexMollifier φ x‖ = φ.normed volume x := by
  rw [f08_011_complexMollifier, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (φ.nonneg_normed (μ := volume) x)]

/-- The Fourier L¹ majorant of the actual complex mollifier is exactly one. -/
theorem f08_011_complexMollifier_integral_norm
    (φ : ContDiffBump (0 : ℝ)) :
    (∫ x : ℝ, ‖f08_011_complexMollifier φ x‖ ∂volume) = 1 := by
  simp_rw [f08_011_complexMollifier_norm]
  exact φ.integral_normed (μ := volume)

/-- The actual mollifier lives strictly within the original physical
ball of radius φ.rOut, hence in its closed interval. -/
theorem f08_011_complexMollifier_support
    (φ : ContDiffBump (0 : ℝ)) :
    Function.support (f08_011_complexMollifier φ) ⊆
      Set.Icc (-φ.rOut) φ.rOut := by
  intro x hx
  have hp : φ.normed volume x ≠ 0 := by
    intro hz
    apply hx
    simp [f08_011_complexMollifier, hz]
  have hb : x ∈ Metric.ball (0 : ℝ) φ.rOut := by
    rw [← φ.support_normed_eq (μ := volume)]
    exact hp
  have habs : |x| ≤ φ.rOut := by
    have hd : |x| < φ.rOut := by
      simpa [Metric.mem_ball, Real.dist_eq] using hb
    exact hd.le
  exact (abs_le.mp habs)

/-- Physical compact support; this does not assume smoothness or
logarithmic-energy boundedness of any sharp cutoff. -/
theorem f08_011_complexMollifier_hasCompactSupport
    (φ : ContDiffBump (0 : ℝ)) :
    HasCompactSupport (f08_011_complexMollifier φ) := by
  apply HasCompactSupport.intro
    (K := Set.Icc (-φ.rOut) φ.rOut) isCompact_Icc
  intro x hx
  have hn : x ∉ Function.support (f08_011_complexMollifier φ) := by
    intro h
    exact hx (f08_011_complexMollifier_support φ h)
  exact Function.notMem_support.mp hn

/-- The true normalized mollifier is C-infinity, not only an L¹ test. -/
theorem f08_011_complexMollifier_smooth
    (φ : ContDiffBump (0 : ℝ)) :
    ContDiff ℝ ⊤ (f08_011_complexMollifier φ) := by
  simpa [f08_011_complexMollifier, Function.comp_def] using
    (Complex.ofRealCLM.contDiff.comp
      (φ.contDiff_normed (n := ⊤) (μ := volume)))

/-- Source-physical support parameter: any bump radius below ε yields
an actual normalized smooth mollifier supported in [-ε,ε]. -/
theorem f08_011_complexMollifier_support_epsilon
    (φ : ContDiffBump (0 : ℝ)) (ε : ℝ)
    (hφ : φ.rOut ≤ ε) :
    Function.support (f08_011_complexMollifier φ) ⊆
      Set.Icc (-ε) ε := by
  intro x hx
  obtain ⟨hl, hu⟩ := f08_011_complexMollifier_support φ hx
  exact ⟨by linarith, by linarith⟩

/-- True Fourier contraction: no unproved spectral multiplier assumption.
Uses the actual source-normalized complex physical bump and exact Mathlib
negative-2π ordinary Fourier transform convention. -/
theorem f08_011_complexMollifier_fourier_norm_le_one
    (φ : ContDiffBump (0 : ℝ)) (ξ : ℝ) :
    ‖(𝓕 (f08_011_complexMollifier φ)) ξ‖ ≤ 1 := by
  calc
    ‖(𝓕 (f08_011_complexMollifier φ)) ξ‖ ≤
        ∫ x : ℝ, ‖f08_011_complexMollifier φ x‖ ∂volume :=
      Real.norm_fourier_le_integral_norm _ _
    _ = 1 := f08_011_complexMollifier_integral_norm φ

#print axioms f08_011_complexMollifier_nonneg
#print axioms f08_011_complexMollifier_integrable
#print axioms f08_011_complexMollifier_integral
#print axioms f08_011_complexMollifier_norm
#print axioms f08_011_complexMollifier_integral_norm
#print axioms f08_011_complexMollifier_support
#print axioms f08_011_complexMollifier_hasCompactSupport
#print axioms f08_011_complexMollifier_smooth
#print axioms f08_011_complexMollifier_support_epsilon
#print axioms f08_011_complexMollifier_fourier_norm_le_one

end
end WeilDefect
