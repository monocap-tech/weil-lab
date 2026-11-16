import WeilDefect.Arithmetic.ActualZetaSmoothLiteralFormulaAutomatic

namespace WeilDefect
noncomputable section
open scoped ComplexConjugate

/-!
NF536: A genuinely real odd physical test has its conjugate-frequency
samples determined by its original samples. For such tests, the absolute
zero-side convergence supplied by the genuine zeta explicit formula
already supplies l² summability of the raw actual-divisor samples.

This is a source-family statement with its physical oddness symmetry
EXPLICIT; the a.e. odd/real -> Fourier symmetry lemma remains separate.
No simplicity, RH, or artificial zero bound is used.
-/

/-- Elementary square-summability consequence of the odd-conjugation law.
Each actual divisor coordinate, including all repeated copies, is kept. -/
theorem neutralOddPairSample_sq_summable
    (A B : NeutralActualZetaDivisorCoordinate → ℂ)
    (hodd : ∀ q, A q = -conj (B q))
    (hsum : Summable (fun q => conj (A q) * B q)) :
    Summable (fun q => ‖B q‖ ^ 2) := by
  have hnorm := hsum.norm
  apply hnorm.congr
  intro q
  rw [norm_mul, Complex.norm_conj, hodd q, norm_neg, Complex.norm_conj]
  ring

/-- The complementary conjugate-frequency sample family is also l²,
without an additional zero-count estimate. -/
theorem neutralOddPairPartner_sq_summable
    (A B : NeutralActualZetaDivisorCoordinate → ℂ)
    (hodd : ∀ q, A q = -conj (B q))
    (hsum : Summable (fun q => conj (A q) * B q)) :
    Summable (fun q => ‖A q‖ ^ 2) := by
  have hB := neutralOddPairSample_sq_summable A B hodd hsum
  apply hB.congr
  intro q
  rw [hodd q, norm_neg, Complex.norm_conj]

/-- On the unchanged genuine multiplicity divisor, C² regularity of
the ACTUAL physical autocorrelation plus the exact real-odd frequency
reflection forces square-summability of the actual raw zeta samples.
The reflection premise will be discharged by the real odd smooth
representative; it is not inferred from arbitrary complex L² data. -/
theorem neutralActualZetaOddPhysicalWindowSample_sq_summable
    (a : ℝ) (f : RealComplexL2)
    (hreg : ContDiff ℝ 2 (neutralWindowCorrelation a f f))
    (hodd : ∀ q : NeutralActualZetaDivisorCoordinate,
      neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q)) f =
        -conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) f)) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) f‖ ^ 2) := by
  have hraw : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralRawTransform (neutralWindowCorrelation a f f)
        (neutralActualZetaDivisorOrdinate q)) :=
    neutralActualZetaDivisor_rawTransform_summable_of_contDiff
      (neutralWindowCorrelation a f f) hreg
      (neutralWindowCorrelation_hasCompactSupport a f f)
  have hEF : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) f) := by
    convert hraw using 1
    funext q
    exact (neutralWindowCorrelation_rawTransform a f f
      (neutralActualZetaDivisorOrdinate q)).symm
  exact neutralOddPairSample_sq_summable
    (fun q => neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q)) f)
    (fun q => neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) f)
    hodd hEF

end
end WeilDefect
