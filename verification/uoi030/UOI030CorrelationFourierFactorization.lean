import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import Mathlib.Analysis.Fourier.Inversion

/-!
Weil-Lab UOI030: a NARROW, SOURCE-MATCHED LEAN 4.34 PROOF CANDIDATE.

Scope:
 * exact ordinary Fourier factorization of arbitrary windowed L2 correlation,
   using already-present original-source theorems, with NO density hypothesis;
 * conditional pointwise inversion, with its two genuine analytic prerequisites
   (continuity and Fourier integrability) left EXPLICIT.

This file has NOT been run through Lean/Lake and is NOT kernel certified.
No `sorry`, new axiom, RH claim or positivity theorem is introduced.
Pinned source: IV023 commit 614ba879f7389fdb620c474adaee273b00eac71c.
-/

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate

/-- First standalone compile target: an exact COMPLEX Fourier factorization,
including the conjugated FIRST source argument. It is merely a composition
of three previously present source theorems, now stated for arbitrary L2
physical inputs and their actual window representatives. -/
theorem neutralUOI030_windowCorrelation_fourier_factorization
    (a : ℝ) (f g : RealComplexL2) (ξ : ℝ) :
    (𝓕 (neutralWindowCorrelation a f g)) ξ =
      conj ((𝓕 (neutralWindowRepresentative a f)) ξ) *
      (𝓕 (neutralWindowRepresentative a g)) ξ := by
  calc
    (𝓕 (neutralWindowCorrelation a f g)) ξ =
        neutralRawTransform (neutralWindowCorrelation a f g)
          ((-2 * Real.pi * ξ : ℝ) : ℂ) :=
      neutralRawTransform_fourier _ _
    _ = conj (neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) f) *
        neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) g := by
      rw [neutralWindowCorrelation_rawTransform]
      simp only [Complex.conj_ofReal]
    _ = conj ((𝓕 (neutralWindowRepresentative a f)) ξ) *
        (𝓕 (neutralWindowRepresentative a g)) ξ := by
      rw [neutralWindowRepresentative_fourier a f ξ,
          neutralWindowRepresentative_fourier a g ξ]

/-- Second standalone compiler target: exact inversion of the ORIGINAL
complex windowed correlation at every physical shift, IF continuity and
integrability of the ordinary Fourier transform are supplied. Both
hypotheses are mathematically valid for compact-window L2 correlations,
but their Lean proofs are NOT supplied here. -/
theorem neutralUOI030_windowCorrelation_inversion_of
    (a : ℝ) (f g : RealComplexL2)
    (hcont : Continuous (neutralWindowCorrelation a f g))
    (hFint : Integrable (𝓕 (neutralWindowCorrelation a f g)))
    (τ : ℝ) :
    (𝓕⁻ (𝓕 (neutralWindowCorrelation a f g))) τ =
      neutralWindowCorrelation a f g τ := by
  exact congrFun
    (hcont.fourierInv_fourier_eq
      (neutralWindowCorrelation_integrable a f g) hFint) τ

#print axioms neutralUOI030_windowCorrelation_fourier_factorization
#print axioms neutralUOI030_windowCorrelation_inversion_of

end
end WeilDefect
