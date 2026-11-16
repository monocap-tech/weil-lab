import WeilDefect.Arithmetic.ActualZetaSmoothLiteralFormulaAutomatic
import Mathlib.Analysis.Calculus.ContDiff.Convolution

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped Convolution ComplexConjugate

/-!
NF534: isolate physical-window correlation regularity from the choice of
a representative of an L² equivalence class. Strictly collar-supported
smooth-test identification remains a separate a.e.-representation theorem.
-/

/-- The genuine L² window correlation is the real-bilinear convolution.
Using ℝ-linearity matters: the spatial variable is real, even though the
complex-valued Fourier samples are genuinely complex. -/
theorem neutralWindowCorrelation_eq_realBilinearConvolution
    (a : ℝ) (f g : RealComplexL2) :
    neutralWindowCorrelation a f g =
      (neutralWindowRepresentative a g ⋆[ContinuousLinearMap.mul ℝ ℂ]
        fun x : ℝ => conj (neutralWindowRepresentative a f (-x))) := by
  funext t
  simp only [neutralWindowCorrelation, convolution, ContinuousLinearMap.mul_apply', neg_sub]

/-- Reflection and conjugation of any finite-window L² representative have
compact support. No pointwise smoothness is assumed or claimed. -/
theorem neutralWindowReflectedRepresentative_hasCompactSupport
    (a : ℝ) (f : RealComplexL2) :
    HasCompactSupport
      (fun x : ℝ => conj (neutralWindowRepresentative a f (-x))) := by
  apply HasCompactSupport.intro isCompact_Icc
  intro x hx
  have hn : -x ∉ Set.Icc (-a) a := by
    intro hin
    apply hx
    exact ⟨by linarith [hin.2], by linarith [hin.1]⟩
  simp [neutralWindowRepresentative, hn]

/-- If an actual window L² representative is C² pointwise, its literal
compact correlation is C² by the genuine convolution regularity theorem.
A separate a.e.-representative theorem is required to apply this to an
abstract physical L² class coming from a smooth collar test. -/
theorem neutralWindowCorrelation_contDiff_of_windowRepresentative_contDiff
    (a : ℝ) (f g : RealComplexL2)
    (hf : ContDiff ℝ 2 (neutralWindowRepresentative a f)) :
    ContDiff ℝ 2 (neutralWindowCorrelation a f g) := by
  have hwin : Integrable (neutralWindowRepresentative a g) := by
    simpa using neutralWindowRepresentative_twist_integrable a g 0
  have hrefl : ContDiff ℝ 2
      (fun x : ℝ => conj (neutralWindowRepresentative a f (-x))) := by
    exact Complex.conjCLE.contDiff.comp (hf.comp contDiff_neg)
  rw [neutralWindowCorrelation_eq_realBilinearConvolution]
  exact (neutralWindowReflectedRepresentative_hasCompactSupport a f)
    .contDiff_convolution_right (ContinuousLinearMap.mul ℝ ℂ)
      hwin.locallyIntegrable hrefl

/-- Combine the true unconditional literal zeta explicit formula with the
C² convolution theorem. The only admissibility hypothesis here is the
specific *pointwise* C² window representative, not merely L² membership. -/
theorem neutralActualZetaWindowCorrelation_literature_of_smoothRepresentative
    (a : ℝ) (f g : RealComplexL2)
    (hf : ContDiff ℝ 2 (neutralWindowRepresentative a f)) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) g) =
      Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g) :=
  neutralActualZetaWindowCorrelation_literature_of_contDiff a f g
    (neutralWindowCorrelation_contDiff_of_windowRepresentative_contDiff a f g hf)

end
end WeilDefect
