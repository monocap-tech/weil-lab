import WeilDefect.Arithmetic.ActualZetaWeilZeroForm

namespace WeilDefect
noncomputable section
open InnerProductSpace
open scoped ComplexConjugate
set_option maxHeartbeats 800000

/-- Exact positive-source sampling on the already constructed physical vector. -/
theorem neutralActualZetaGreenCanonical_positiveSource_sampling (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) (q : NeutralActualZetaDivisorCoordinate) :
    inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v)) =
    ((Real.sqrt 2)⁻¹ : ℂ) *
      (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
          (neutralActualZetaGreenSynthesis a v) +
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralActualZetaGreenSynthesis a v)) := by
  rw [neutralLogPositivePairSource_inner, neutralActualZetaGreenCanonical_physical]

/-- Full-divisor positive-source analysis is square summable on this same vector. -/
theorem neutralActualZetaGreenCanonical_positiveSource_sq_summable
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2) := by
  let c : ℂ := ((Real.sqrt 2)⁻¹ : ℂ)
  apply Summable.of_norm_bounded
    (((neutralActualZetaGreenSynthesis_partner_sq_summable a ha v).add
      (neutralActualZetaGreenSynthesis_window_sq_summable a ha v)).mul_left
        (‖c‖ ^ 2 * 2))
  intro q
  rw [neutralActualZetaGreenCanonical_positiveSource_sampling,
    Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _), norm_mul, mul_pow]
  have h := norm_add_le
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
        (neutralActualZetaGreenSynthesis a v) +
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a v)‖ ^ 2 ≤
      2 * (‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
          (neutralActualZetaGreenSynthesis a v)‖ ^ 2 +
        ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralActualZetaGreenSynthesis a v)‖ ^ 2) := by
    nlinarith only [hs, ht]
  simpa only [c, mul_assoc] using mul_le_mul_of_nonneg_left hb (sq_nonneg ‖c‖)

private theorem sourceMixedSummable {ι : Type*} (f g : ι → ℂ)
    (hf : Summable (fun q => ‖f q‖ ^ 2)) (hg : Summable (fun q => ‖g q‖ ^ 2)) :
    Summable (fun q => conj (f q) * g q) := by
  apply Summable.of_norm_bounded (hf.add hg)
  intro q
  rw [norm_mul, Complex.norm_conj]
  nlinarith only [sq_nonneg (‖f q‖ - ‖g q‖)]

theorem neutralActualZetaGreenCanonical_positiveSource_mixed_summable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) *
      inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) :=
  sourceMixedSummable _ _
    (neutralActualZetaGreenCanonical_positiveSource_sq_summable a ha v)
    (neutralActualZetaGreenCanonical_positiveSource_sq_summable a ha w)

theorem neutralActualZetaGreenCanonical_negativeSource_mixed_summable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) *
      inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) :=
  sourceMixedSummable _ _
    (neutralActualZetaGreenCanonical_negativeSource_sq_summable a ha v)
    (neutralActualZetaGreenCanonical_negativeSource_sq_summable a ha w)

/-- These forms sum every actual multiplicity copy. Thus each two-point
partner orbit is counted twice, which explains the later factor of one half. -/
def neutralActualZetaGreenPositiveForm (a : ℝ) (ha : 0 < a)
    (v w : NeutralActualZetaGreenCoefficients) : ℂ :=
  ∑' q : NeutralActualZetaDivisorCoordinate,
    conj (inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) *
    inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))

def neutralActualZetaGreenNegativeForm (a : ℝ) (ha : 0 < a)
    (v w : NeutralActualZetaGreenCoefficients) : ℂ :=
  ∑' q : NeutralActualZetaDivisorCoordinate,
    conj (inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) *
    inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))

/-- Pointwise source diagonalization, retaining both cross terms. -/
theorem neutralLogPairSource_mixed_difference (a : ℝ) (z : ℂ)
    (f g : NeutralLogHilbertCarrier a) :
    conj (inner ℂ (neutralLogPositivePairSource a z) f) *
        inner ℂ (neutralLogPositivePairSource a z) g -
      conj (inner ℂ (neutralLogNegativePairSource a z) f) *
        inner ℂ (neutralLogNegativePairSource a z) g =
    conj (neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val)) *
        neutralWindowEvaluation a z (neutralLogPhysical g.val) +
      conj (neutralWindowEvaluation a z (neutralLogPhysical f.val)) *
        neutralWindowEvaluation a (conj z) (neutralLogPhysical g.val) := by
  let c : ℂ := ((Real.sqrt 2)⁻¹ : ℂ)
  have hc : c ^ 2 = (1 / 2 : ℂ) := by
    dsimp [c]
    rw [← Complex.ofReal_pow, inv_pow, Real.sq_sqrt (by norm_num)]
    norm_num
  rw [neutralLogPositivePairSource_inner, neutralLogPositivePairSource_inner,
    neutralLogNegativePairSource_inner, neutralLogNegativePairSource_inner]
  simp only [map_mul, map_add, map_sub, Complex.conj_ofReal]
  calc
    _ = c ^ 2 * (2 *
      (conj (neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val)) *
          neutralWindowEvaluation a z (neutralLogPhysical g.val) +
        conj (neutralWindowEvaluation a z (neutralLogPhysical f.val)) *
          neutralWindowEvaluation a (conj z) (neutralLogPhysical g.val))) := by
            dsimp [c]; ring
    _ = _ := by rw [hc]; ring

/-- The exact convergent source decomposition on the same constructed vector.
This is zero-side diagonalization; arithmetic explicit-formula transport is separate. -/
theorem neutralActualZetaGreenZeroForm_source_decomposition
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    2 * neutralActualZetaGreenZeroForm a v w =
      neutralActualZetaGreenPositiveForm a ha v w -
        neutralActualZetaGreenNegativeForm a ha v w := by
  let F : NeutralActualZetaDivisorCoordinate → ℂ := fun q =>
    conj (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
      (neutralActualZetaGreenSynthesis a v)) *
    neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralActualZetaGreenSynthesis a w)
  let R : NeutralActualZetaDivisorCoordinate → ℂ := fun q =>
    conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralActualZetaGreenSynthesis a v)) *
    neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
      (neutralActualZetaGreenSynthesis a w)
  have hf : Summable F := neutralActualZetaGreenSynthesis_partner_mixed_summable a ha v w
  have hr : Summable R := sourceMixedSummable _ _
    (neutralActualZetaGreenSynthesis_window_sq_summable a ha v)
    (neutralActualZetaGreenSynthesis_partner_sq_summable a ha w)
  have hRF (q) : R q = F (neutralActualZetaDivisorPairEquiv q) := by
    change _ = conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate (neutralActualZetaDivisorPair q)))
      (neutralActualZetaGreenSynthesis a v)) *
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate (neutralActualZetaDivisorPair q))
        (neutralActualZetaGreenSynthesis a w)
    rw [neutralActualZetaDivisorOrdinate_pair]
    simp only [starRingEnd_apply, star_star]
    rfl
  have ht : (∑' q, R q) = ∑' q, F q := by
    rw [tsum_congr hRF]
    exact neutralActualZetaDivisorPairEquiv.tsum_eq F
  unfold neutralActualZetaGreenPositiveForm neutralActualZetaGreenNegativeForm
  rw [← (neutralActualZetaGreenCanonical_positiveSource_mixed_summable a ha v w).tsum_sub
    (neutralActualZetaGreenCanonical_negativeSource_mixed_summable a ha v w)]
  have he : (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) *
        inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w)) -
      conj (inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) *
        inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) =
      ∑' q, (F q + R q) := by
    apply tsum_congr
    intro q
    rw [neutralLogPairSource_mixed_difference,
      neutralActualZetaGreenCanonical_physical, neutralActualZetaGreenCanonical_physical]
    rfl
  rw [he, hf.tsum_add hr, ht]
  change 2 * (∑' q, F q) = (∑' q, F q) + (∑' q, F q)
  ring

/-- Real diagonal energy identity with both complete, convergent source energies. -/
theorem neutralActualZetaGreenZeroForm_source_energy
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    2 * (neutralActualZetaGreenZeroForm a v v).re =
      (∑' q : NeutralActualZetaDivisorCoordinate,
        ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2) -
      (∑' q : NeutralActualZetaDivisorCoordinate,
        ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2) := by
  have h := neutralActualZetaGreenZeroForm_source_decomposition a ha v v
  simp only [neutralActualZetaGreenPositiveForm, neutralActualZetaGreenNegativeForm,
    Complex.conj_mul', ← Complex.ofReal_pow, ← Complex.ofReal_tsum] at h
  have hr := congrArg Complex.re h
  simpa using hr

end
end WeilDefect
