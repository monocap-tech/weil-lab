import WeilDefect.Arithmetic.ActualZetaNativeWeilForm

/-!
  Weil-Lab IV066 — original arbitrary C² source pilot.

  SOURCE-TYPED DRAFT; NOT COMPILER-CERTIFIED.
  Uses the existing concrete zeta seam and imported literal explicit formula,
  not a new analytic axiom or an assumption that the Green carrier is surjective.

  This intentionally does not claim that arbitrary f,g have a smooth Weil
  convolution, nor that the digamma atom limit or closed form domain has
  been formalized. Those are separate IV066 obligations.
-/

namespace WeilDefect

noncomputable section
open MeasureTheory Complex
open scoped ArithmeticFunction BigOperators

/-- The physical-correlation ORIENTATION required by IV065, expressed in the
    imported literal source vocabulary. Identifying this with the integral
    `∫ x, conj (f x) * g (x+s)` remains a separate mathematical obligation. -/
def iv066SourceCorrelation (f g : ℝ → ℂ) : ℝ → ℂ :=
  Zeta23.EF.weilTest g f

theorem iv066_sourceCorrelation_orientation (f g : ℝ → ℂ) :
    iv066SourceCorrelation f g = Zeta23.EF.weilTest g f := rfl

/-- The already-imported concrete zeta explicit formula yields actual zero-side
    summability on an ARBITRARY admissible C² source. This is not restricted to
    `NeutralActualZetaGreenCoefficients`. -/
theorem iv066_original_general_source_summable
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k) (hkc : HasCompactSupport k) :
    Summable (fun ρ : (Zeta23.zetaZeros Zeta23.zetaSeam).carrier =>
      ((Zeta23.zetaZeros Zeta23.zetaSeam).mult ρ : ℂ) *
        Zeta23.paperFT k (Zeta23.gammaOf ρ.val)) := by
  exact ((Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam) k hk hkc).1

/-- The full signed source formula, including BOTH poles, BOTH prime shifts,
    and the literal gammaBracket/(2π) term. No source term is truncated.

    This proof invokes the existing concrete zeta theorem, not a newly
    introduced arbitrary equality. It does not yet identify gammaBracket
    with the closed positive-atom quadratic form. -/
theorem iv066_original_general_source_signed
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k) (hkc : HasCompactSupport k) :
    (∑' ρ : (Zeta23.zetaZeros Zeta23.zetaSeam).carrier,
        ((Zeta23.zetaZeros Zeta23.zetaSeam).mult ρ : ℂ) *
          Zeta23.paperFT k (Zeta23.gammaOf ρ.val)) =
      Zeta23.paperFT k (I / 2) + Zeta23.paperFT k (-I / 2)
      - ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
          (k (Real.log n) + k (-Real.log n))
      + (1 / (2 * π) : ℂ) * ∫ r : ℝ,
          Zeta23.paperFT k r * (Zeta23.EF.gammaBracket r : ℂ) := by
  have h := ((Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam) k hk hkc).2
  simpa only [Zeta23.EF.literatureRHS] using h

/-- The literal source theorem specialized to the correctly ordered mixed
    convolution. The C² and support premises are explicitly load-bearing;
    producing them from arbitrary smooth f,g is NOT discharged here. -/
theorem iv066_original_mixed_weilTest_signed
    (f g : ℝ → ℂ)
    (hk : ContDiff ℝ 2 (iv066SourceCorrelation f g))
    (hkc : HasCompactSupport (iv066SourceCorrelation f g)) :
    (∑' ρ : (Zeta23.zetaZeros Zeta23.zetaSeam).carrier,
        ((Zeta23.zetaZeros Zeta23.zetaSeam).mult ρ : ℂ) *
          Zeta23.paperFT (iv066SourceCorrelation f g)
            (Zeta23.gammaOf ρ.val)) =
      Zeta23.EF.literatureRHS (iv066SourceCorrelation f g) := by
  exact ((Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam)
    (iv066SourceCorrelation f g) hk hkc).2

/-- Genuine imported real-place normalization: the exact native symbol is
    the imported zeta gamma bracket, for every real frequency. -/
theorem iv066_gamma_literal_native (r : ℝ) :
    Zeta23.EF.gammaBracket r = compactWindowArchimedeanSymbol r :=
  neutralActualZetaGammaBracket_native r

/-- The native right-limit prime/cutoff conventions in the exact mathlib
    frequency coordinate. This is an imported DEFINITIONAL source equality,
    not a new proof that an arbitrary test has a spectral representation. -/
theorem iv066_native_signed_multiplier (a ξ : ℝ) :
    rightLimitCompactWeilSymbolMathlib a ξ =
      compactWindowArchimedeanSymbol (2 * Real.pi * ξ) -
        Finset.sum (rightLimitPrimePowerFinset a)
          (fun n => compactWindowPrimeCoefficient n *
            Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ))) :=
  rightLimitCompactWeilSymbolMathlib_eq a ξ

end
end WeilDefect
