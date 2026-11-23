import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import Mathlib.Analysis.Fourier.Convolution

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped Convolution Pointwise

/-!
F08-009 — Original physical compact-window convolution support control.

This uses the actual `neutralWindowRepresentative` of the source and the
true continuous complex bilinear convolution `ContinuousLinearMap.mul ℂ ℂ`.
No false smoothness of the original L² representative is inferred.

The support statements are pointwise and do not assume any ad hoc sharp
cutoff is bounded in the logarithmic Fourier form norm. The cutoff here
is solely the original physical window's literal indicator representative.

A later theorem must construct actual smooth normalized nonnegative rho,
establish its Fourier contraction/limit, and pass from the ordinary
pointwise Fourier product to the native weighted carrier.
-/

/-- Exact source-physical support of the original window representative. -/
theorem f08_009_original_window_support
    (a : ℝ) (f : RealComplexL2) :
    Function.support (neutralWindowRepresentative a f) ⊆
      Set.Icc (-a) a := by
  intro x hx
  by_contra hn
  have hz : neutralWindowRepresentative a f x = 0 := by
    simp [neutralWindowRepresentative, hn]
  exact hx hz

/-- Convolution support is contained in the Minkowski sum of the original
source physical window and the second function's actual pointwise support. -/
theorem f08_009_original_window_convolution_minkowski
    (a : ℝ) (f : RealComplexL2) (rho : ℝ → ℂ) :
    Function.support
      (neutralWindowRepresentative a f
        ⋆[ContinuousLinearMap.mul ℂ ℂ] rho) ⊆
      Set.Icc (-a) a + Function.support rho := by
  exact (MeasureTheory.support_convolution_subset
    (ContinuousLinearMap.mul ℂ ℂ)).trans
      (Set.add_subset_add (f08_009_original_window_support a f)
        (Set.Subset.rfl))

/-- Concrete support radius for any pointwise-supported rho. In particular,
when epsilon>0 and rho is an actual compact mollifier supported in
[-epsilon,epsilon], the original physical convolution stays inside the
enlarged interval [-a-epsilon,a+epsilon]. -/
theorem f08_009_original_window_convolution_support_radius
    (a epsilon : ℝ) (f : RealComplexL2) (rho : ℝ → ℂ)
    (hrho : Function.support rho ⊆ Set.Icc (-epsilon) epsilon) :
    Function.support
      (neutralWindowRepresentative a f
        ⋆[ContinuousLinearMap.mul ℂ ℂ] rho) ⊆
      Set.Icc (-(a + epsilon)) (a + epsilon) := by
  have hsum :
      Set.Icc (-a) a + Set.Icc (-epsilon) epsilon ⊆
        Set.Icc (-(a + epsilon)) (a + epsilon) := by
    intro x hx
    rcases hx with ⟨u, hu, v, hv, rfl⟩
    exact ⟨by dsimp at *; linarith [hu.1, hv.1],
      by dsimp at *; linarith [hu.2, hv.2]⟩
  calc
    _ ⊆ Set.Icc (-a) a + Function.support rho :=
      f08_009_original_window_convolution_minkowski a f rho
    _ ⊆ Set.Icc (-a) a + Set.Icc (-epsilon) epsilon :=
      Set.add_subset_add (Set.Subset.rfl) hrho
    _ ⊆ _ := hsum

#print axioms f08_009_original_window_support
#print axioms f08_009_original_window_convolution_minkowski
#print axioms f08_009_original_window_convolution_support_radius

end
end WeilDefect
