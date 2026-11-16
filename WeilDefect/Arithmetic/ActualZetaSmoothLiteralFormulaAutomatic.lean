import WeilDefect.Arithmetic.ActualZetaSmoothLiteralFormula
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace WeilDefect
noncomputable section
open scoped ComplexConjugate

/-!
NF533: Multiplicity-aware absolute convergence is a consequence of
the imported certified literal explicit formula, NOT a test hypothesis.
-/

/-- Imported absolute zeta-zero summability lifts to every genuine integer
multiplicity copy of the same actual divisor. No RH or enumeration. -/
theorem neutralActualZetaDivisor_rawTransform_summable_of_contDiff
    (k : ℝ → ℂ) (hreg : ContDiff ℝ 2 k)
    (hcompact : HasCompactSupport k) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralRawTransform k (neutralActualZetaDivisorOrdinate q)) := by
  have hEF := ((Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam) k hreg hcompact).1
  have hlit : Summable (fun ρ : NeutralActualZetaZeroPoint =>
      ((Zeta23.zetaZeros Zeta23.zetaSeam).mult
        (neutralActualZetaLiteraturePointEquiv ρ) : ℂ) *
      Zeta23.paperFT k
        (Zeta23.gammaOf (neutralActualZetaLiteraturePointEquiv ρ).val)) :=
    (neutralActualZetaLiteraturePointEquiv.summable_iff).mpr hEF
  have hw : Summable (fun ρ : NeutralActualZetaZeroPoint =>
      (neutralActualZetaMultiplicity ρ : ℂ) *
        neutralRawTransform k (neutralActualZetaOrdinate ρ)) := by
    convert hlit using 1
    funext ρ
    rw [neutralRawTransform_eq_paperFT,
      neutralActualZetaLiterature_multiplicity ρ,
      neutralActualZetaLiterature_ordinate ρ]
  have hn := hw.norm
  have hc : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralRawTransform k (neutralActualZetaDivisorOrdinate q)‖) := by
    apply (summable_sigma_of_nonneg (fun q : NeutralActualZetaDivisorCoordinate =>
      norm_nonneg (neutralRawTransform k (neutralActualZetaDivisorOrdinate q)))).2
    constructor
    · intro ρ
      exact Summable.of_finite
    · have ht : (fun ρ : NeutralActualZetaZeroPoint =>
        ∑' i : Fin (neutralActualZetaMultiplicity ρ),
          ‖neutralRawTransform k (neutralActualZetaDivisorOrdinate ⟨ρ, i⟩)‖) =
        (fun ρ : NeutralActualZetaZeroPoint =>
          ‖(neutralActualZetaMultiplicity ρ : ℂ) *
            neutralRawTransform k (neutralActualZetaOrdinate ρ)‖) := by
        funext ρ
        simp [neutralActualZetaDivisorOrdinate, tsum_fintype, norm_mul,
          nsmul_eq_mul]
      simpa only [ht] using hn
  exact Summable.of_norm_bounded hc (fun _ => le_rfl)

/-- For an arbitrary physical-window correlation, the actual zeta EF needs
only C² regularity. Compact support is already unconditional, and complete
all-multiplicity divisor convergence follows from the imported theorem. -/
theorem neutralActualZetaWindowCorrelation_literature_of_contDiff
    (a : ℝ) (f g : RealComplexL2)
    (hreg : ContDiff ℝ 2 (neutralWindowCorrelation a f g)) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) g) =
      Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g) := by
  have hs : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) g) := by
    convert neutralActualZetaDivisor_rawTransform_summable_of_contDiff
      (neutralWindowCorrelation a f g) hreg
      (neutralWindowCorrelation_hasCompactSupport a f g) using 1
    funext q
    exact (neutralWindowCorrelation_rawTransform a f g
      (neutralActualZetaDivisorOrdinate q)).symm
  exact neutralActualZetaWindowCorrelation_literature a f g hreg hs

end
end WeilDefect
