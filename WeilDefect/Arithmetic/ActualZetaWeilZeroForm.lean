import WeilDefect.Arithmetic.ActualZetaRawGreenSampling

namespace WeilDefect
noncomputable section
open InnerProductSpace
open scoped ComplexConjugate
set_option maxHeartbeats 800000

/-- The actual multiplicity-preserving conjugate-ordinate involution. -/
def neutralActualZetaDivisorPairEquiv :
    NeutralActualZetaDivisorCoordinate ≃ NeutralActualZetaDivisorCoordinate :=
  ⟨neutralActualZetaDivisorPair, neutralActualZetaDivisorPair,
    neutralActualZetaDivisorPair_involutive, neutralActualZetaDivisorPair_involutive⟩

/-- Partner sampling is square summable by the actual divisor involution. -/
theorem neutralActualZetaGreenSynthesis_partner_sq_summable (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaGreenSynthesis a v)‖ ^ 2) := by
  have h := neutralActualZetaDivisorPairEquiv.summable_iff.mpr
    (neutralActualZetaGreenSynthesis_window_sq_summable a ha v)
  change Summable (fun q : NeutralActualZetaDivisorCoordinate =>
    ‖neutralWindowEvaluation a
      (neutralActualZetaDivisorOrdinate (neutralActualZetaDivisorPair q))
      (neutralActualZetaGreenSynthesis a v)‖ ^ 2) at h
  simpa only [neutralActualZetaDivisorOrdinate_pair] using h

/-- The Weil zero-side pairing, with the partner in the first slot, converges
absolutely for the constructed Green vectors. No critical-line assumption occurs. -/
theorem neutralActualZetaGreenSynthesis_partner_mixed_summable (a : ℝ) (ha : 0 < a)
    (v w : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaGreenSynthesis a v)) *
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a w)) := by
  apply Summable.of_norm_bounded
    ((neutralActualZetaGreenSynthesis_partner_sq_summable a ha v).add
      (neutralActualZetaGreenSynthesis_window_sq_summable a ha w))
  intro q
  rw [norm_mul, Complex.norm_conj]
  nlinarith only [sq_nonneg
    (‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaGreenSynthesis a v)‖ -
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a w)‖)]

/-- Actual divisor zero-side form on the constructed coefficient carrier.
Identification with the arithmetic Weil form is a separate, still open transport. -/
def neutralActualZetaGreenZeroForm (a : ℝ)
    (v w : NeutralActualZetaGreenCoefficients) : ℂ :=
  ∑' q : NeutralActualZetaDivisorCoordinate,
    conj (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
      (neutralActualZetaGreenSynthesis a v)) *
    neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralActualZetaGreenSynthesis a w)

/-- Actual partner reindexing gives Hermitian symmetry, without positivity. -/
theorem neutralActualZetaGreenZeroForm_hermitian (a : ℝ)
    (v w : NeutralActualZetaGreenCoefficients) :
    conj (neutralActualZetaGreenZeroForm a v w) =
      neutralActualZetaGreenZeroForm a w v := by
  unfold neutralActualZetaGreenZeroForm
  rw [Complex.conj_tsum]
  rw [← neutralActualZetaDivisorPairEquiv.tsum_eq
    (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaGreenSynthesis a w)) *
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a v))]
  apply tsum_congr
  intro q
  change conj (conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate q)) (neutralActualZetaGreenSynthesis a v)) *
    neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralActualZetaGreenSynthesis a w)) =
    conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate (neutralActualZetaDivisorPair q)))
      (neutralActualZetaGreenSynthesis a w)) *
    neutralWindowEvaluation a
      (neutralActualZetaDivisorOrdinate (neutralActualZetaDivisorPair q))
      (neutralActualZetaGreenSynthesis a v)
  rw [neutralActualZetaDivisorOrdinate_pair]
  simp only [map_mul, starRingEnd_apply, star_star]
  exact mul_comm _ _

/-- The diagonal zero-side value is real; it need not be nonnegative. -/
theorem neutralActualZetaGreenZeroForm_diagonal_im (a : ℝ)
    (v : NeutralActualZetaGreenCoefficients) :
    (neutralActualZetaGreenZeroForm a v v).im = 0 := by
  have h := congrArg Complex.im (neutralActualZetaGreenZeroForm_hermitian a v v)
  simp only [Complex.conj_im] at h
  linarith

/-- Exact same-vector negative source dictionary on the constructed carrier. -/
theorem neutralActualZetaGreenCanonical_negativeSource_sampling (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) (q : NeutralActualZetaDivisorCoordinate) :
    inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v)) =
    ((Real.sqrt 2)⁻¹ : ℂ) *
      (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
          (neutralActualZetaGreenSynthesis a v) -
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralActualZetaGreenSynthesis a v)) := by
  rw [neutralLogNegativePairSource_inner,
    neutralActualZetaGreenCanonical_physical]

/-- The actual negative-source analysis is square summable on this same vector. -/
theorem neutralActualZetaGreenCanonical_negativeSource_sq_summable
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2) := by
  let c : ℂ := ((Real.sqrt 2)⁻¹ : ℂ)
  apply Summable.of_norm_bounded
    (((neutralActualZetaGreenSynthesis_partner_sq_summable a ha v).add
      (neutralActualZetaGreenSynthesis_window_sq_summable a ha v)).mul_left
        (‖c‖ ^ 2 * 2))
  intro q
  rw [neutralActualZetaGreenCanonical_negativeSource_sampling,
    Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _), norm_mul, mul_pow]
  have h := norm_sub_le
    (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
      (neutralActualZetaGreenSynthesis a v))
    (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralActualZetaGreenSynthesis a v))
  have hs := pow_le_pow_left₀ (norm_nonneg _) h 2
  have ht := sq_nonneg
    (‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaGreenSynthesis a v)‖ -
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a v)‖)
  have hb : ‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaGreenSynthesis a v) -
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a v)‖ ^ 2 ≤
      2 * (‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
          (neutralActualZetaGreenSynthesis a v)‖ ^ 2 +
        ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralActualZetaGreenSynthesis a v)‖ ^ 2) := by
    nlinarith only [hs, ht]
  simpa only [c, mul_assoc] using
    mul_le_mul_of_nonneg_left hb (sq_nonneg ‖c‖)

end
end WeilDefect
