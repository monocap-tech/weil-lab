import WeilDefect.Arithmetic.ActualZetaCorrelationInverseAttachment
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_WeilEF_EF_lit_zeta
import Mathlib.Topology.Algebra.InfiniteSum.Constructions

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped ContDiff

/-- The imported actual-zero carrier is the same open-strip point subtype. -/
def neutralActualZetaLiteraturePointEquiv :
    NeutralActualZetaZeroPoint ≃ (Zeta23.zetaZeros Zeta23.zetaSeam).carrier :=
  Equiv.refl _

theorem neutralActualZetaLiterature_multiplicity (ρ : NeutralActualZetaZeroPoint) :
    (Zeta23.zetaZeros Zeta23.zetaSeam).mult
      (neutralActualZetaLiteraturePointEquiv ρ) = neutralActualZetaMultiplicity ρ := rfl

theorem neutralActualZetaLiterature_ordinate (ρ : NeutralActualZetaZeroPoint) :
    Zeta23.gammaOf (neutralActualZetaLiteraturePointEquiv ρ).val =
      neutralActualZetaOrdinate ρ := by
  change (ρ.val - 1 / 2) / Complex.I = -Complex.I * (ρ.val - 1 / 2)
  apply (div_eq_iff Complex.I_ne_zero).2
  calc
    ρ.val - 1 / 2 = -(Complex.I * Complex.I) * (ρ.val - 1 / 2) := by
      rw [Complex.I_mul_I]
      ring
    _ = (-Complex.I * (ρ.val - 1 / 2)) * Complex.I := by ring

theorem neutralRawTransform_eq_paperFT (k : ℝ → ℂ) (z : ℂ) :
    neutralRawTransform k z = Zeta23.paperFT k z := rfl

/-- Collapse actual multiplicity copies to the imported distinct-zero weighted sum. -/
theorem neutralActualZetaDivisor_tsum_literature (k : ℝ → ℂ)
    (hk : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralRawTransform k (neutralActualZetaDivisorOrdinate q))) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      neutralRawTransform k (neutralActualZetaDivisorOrdinate q)) =
    ∑' ρ : (Zeta23.zetaZeros Zeta23.zetaSeam).carrier,
      ((Zeta23.zetaZeros Zeta23.zetaSeam).mult ρ : ℂ) *
        Zeta23.paperFT k (Zeta23.gammaOf ρ.val) := by
  have hcopy :
      (∑' q : NeutralActualZetaDivisorCoordinate,
        neutralRawTransform k (neutralActualZetaDivisorOrdinate q)) =
      ∑' ρ : NeutralActualZetaZeroPoint, (neutralActualZetaMultiplicity ρ : ℂ) *
        neutralRawTransform k (neutralActualZetaOrdinate ρ) := by
    rw [hk.tsum_sigma]
    congr 1
    funext ρ
    simp [neutralActualZetaDivisorOrdinate, tsum_fintype, nsmul_eq_mul]
  rw [hcopy]
  change (∑' ρ : NeutralActualZetaZeroPoint, (neutralActualZetaMultiplicity ρ : ℂ) *
    neutralRawTransform k (neutralActualZetaOrdinate ρ)) =
    ∑' ρ : NeutralActualZetaZeroPoint, (neutralActualZetaMultiplicity ρ : ℂ) *
      Zeta23.paperFT k (Zeta23.gammaOf ρ.val)
  apply tsum_congr
  intro ρ
  rw [neutralRawTransform_eq_paperFT]
  have hγ := neutralActualZetaLiterature_ordinate ρ
  change Zeta23.gammaOf ρ.val = neutralActualZetaOrdinate ρ at hγ
  rw [hγ]

/-- Exact prime term of the literal formula on the already constructed C² correlation. -/
def neutralActualZetaGreenPrimeForm (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) : ℂ :=
  ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
    (neutralActualZetaGreenCorrelationInverse a v w (Real.log n) +
      neutralActualZetaGreenCorrelationInverse a v w (-Real.log n))

/-- Exact digamma term, retaining the imported literal normalization. -/
def neutralActualZetaGreenArchimedeanForm
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) : ℂ :=
  (1 / (2 * Real.pi) : ℂ) * ∫ r : ℝ,
    neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w) (r : ℂ) *
      (Zeta23.EF.gammaBracket r : ℂ)

/-- The certified explicit formula is applied directly, with admissibility already proved. -/
theorem neutralActualZetaGreenZeroForm_literature
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenZeroForm a v w =
      Zeta23.EF.literatureRHS (neutralActualZetaGreenCorrelationInverse a v w) := by
  have hEF := (Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam)
    (neutralActualZetaGreenCorrelationInverse a v w)
    (neutralActualZetaGreenCorrelationInverse_contDiff a ha v w)
    (neutralActualZetaGreenCorrelationInverse_hasCompactSupport a ha v w)
  rw [← neutralActualZetaGreenCorrelationInverse_zeroForm a ha v w,
    neutralActualZetaDivisor_tsum_literature _
      (neutralActualZetaGreenCorrelationInverse_samples_summable a ha v w)]
  exact hEF.2

/-- Zero form, poles, prime term and digamma term now belong to this same Green carrier. -/
theorem neutralActualZetaGreenZeroForm_arithmetic
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenZeroForm a v w =
      inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
        (neutralLogPoleOperator a
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) -
      neutralActualZetaGreenPrimeForm a v w + neutralActualZetaGreenArchimedeanForm a v w := by
  rw [← neutralActualZetaGreenCorrelationInverse_poleOperator a ha v w]
  simpa only [Zeta23.EF.literatureRHS, neutralActualZetaGreenPrimeForm,
    neutralActualZetaGreenArchimedeanForm, neutralRawTransform_eq_paperFT,
    Complex.ofReal_div, Complex.ofReal_one, Complex.ofReal_ofNat,
    Complex.ofReal_neg, mul_div_assoc, mul_one, mul_neg, neg_div,
    div_eq_mul_inv, one_mul] using
      neutralActualZetaGreenZeroForm_literature a ha v w

end
end WeilDefect
