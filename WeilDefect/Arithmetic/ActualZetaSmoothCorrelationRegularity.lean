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
  apply HasCompactSupport.intro (K := Set.Icc (-a) a) isCompact_Icc
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
  exact (neutralWindowReflectedRepresentative_hasCompactSupport a f).contDiff_convolution_right
    (ContinuousLinearMap.mul ℝ ℂ)
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


/-- The rigorous admissibility theorem for a genuine smooth test carried as
an L² class: a compactly supported C² function agreeing a.e. with the
window-restricted SECOND input makes the exact correlation C². Unlike a
pointwise smoothness assumption on the selected L² representative, this
hypothesis is invariant under change of representatives. -/
theorem neutralWindowCorrelation_contDiff_of_ae_smoothSecond
    (a : ℝ) (f g : RealComplexL2)
    (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ 2 ψ) (hψc : HasCompactSupport ψ)
    (hψae : neutralWindowRepresentative a g =ᵐ[volume] ψ) :
    ContDiff ℝ 2 (neutralWindowCorrelation a f g) := by
  let H : ℝ → ℂ := fun x => conj (neutralWindowRepresentative a f (-x))
  have hwin : Integrable (neutralWindowRepresentative a f) := by
    simpa using neutralWindowRepresentative_twist_integrable a f 0
  have hH : Integrable H := by
    exact (Complex.conjCLE.toContinuousLinearMap.integrable_comp hwin).comp_neg
  have hsame :
      (neutralWindowRepresentative a g ⋆[ContinuousLinearMap.mul ℝ ℂ] H) =
        (ψ ⋆[ContinuousLinearMap.mul ℝ ℂ] H) := by
    exact convolution_congr (ContinuousLinearMap.mul ℝ ℂ) hψae
      (Filter.EventuallyEq.rfl)
  rw [neutralWindowCorrelation_eq_realBilinearConvolution, hsame]
  exact hψc.contDiff_convolution_left (ContinuousLinearMap.mul ℝ ℂ)
    hψ hH.locallyIntegrable

/-- Actual complete-multiplicity Weil EF for a smooth physical input
represented only a.e. inside the window. NO pointwise smoothness of the
canonical L² representative, and NO separate divisor summability premise. -/
theorem neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond
    (a : ℝ) (f g : RealComplexL2)
    (ψ : ℝ → ℂ) (hψ : ContDiff ℝ 2 ψ)
    (hψc : HasCompactSupport ψ)
    (hψae : neutralWindowRepresentative a g =ᵐ[volume] ψ) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) g) =
      Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g) :=
  neutralActualZetaWindowCorrelation_literature_of_contDiff a f g
    (neutralWindowCorrelation_contDiff_of_ae_smoothSecond a f g ψ hψ hψc hψae)

end
end WeilDefect
