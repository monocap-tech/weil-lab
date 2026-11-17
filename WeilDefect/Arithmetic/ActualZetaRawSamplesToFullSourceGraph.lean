import WeilDefect.Arithmetic.ActualZetaFullSourceLiftOfSquareSummable

namespace WeilDefect
noncomputable section

open InnerProductSpace
open scoped ComplexConjugate ENNReal

/-!
NF537 — full literal divisor sample-to-positive/negative-source transport.

The complete zeta divisor has copies Sigma rho (Fin (mult rho)), not
distinct zeros without multiplicity. This argument uses lp addition/
subtraction, NOT a Green approximation or an unspecified source model.
-/

/-- If the two original raw physical Fourier sample families are ℓ²,
then BOTH unnormalized authentic source analyses are ℓ². This preserves
the exact sqrt(2) P/N source definitions, including every zeta-zero copy. -/
theorem neutralActualZetaRawSamples_toSourcePN_sq_summable
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hA : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val)‖ ^ 2))
    (hB : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralLogPhysical f.val)‖ ^ 2)) :
    (Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2)) ∧
    (Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2)) := by
  let A : NeutralActualZetaGreenCoefficients := ⟨
    (fun q => neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate q)) (neutralLogPhysical f.val)),
    memℓp_gen (by simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using hA)⟩
  let B : NeutralActualZetaGreenCoefficients := ⟨
    (fun q => neutralWindowEvaluation a
      (neutralActualZetaDivisorOrdinate q) (neutralLogPhysical f.val)),
    memℓp_gen (by simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using hB)⟩
  let P : NeutralActualZetaGreenCoefficients :=
    (((Real.sqrt 2)⁻¹ : ℂ) • (A + B))
  let N : NeutralActualZetaGreenCoefficients :=
    (((Real.sqrt 2)⁻¹ : ℂ) • (A - B))
  have hP : Summable (fun q : NeutralActualZetaDivisorCoordinate => ‖P q‖ ^ 2) := by
    simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
      (lp.hasSum_norm (by norm_num : 0 < (2 : ℝ≥0∞).toReal) P).summable
  have hN : Summable (fun q : NeutralActualZetaDivisorCoordinate => ‖N q‖ ^ 2) := by
    simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
      (lp.hasSum_norm (by norm_num : 0 < (2 : ℝ≥0∞).toReal) N).summable
  constructor
  · apply hP.congr
    intro q
    simp only [P, lp.coeFn_smul, Pi.smul_apply, smul_eq_mul,
      lp.coeFn_add, Pi.add_apply]
    change ‖((Real.sqrt 2)⁻¹ : ℂ) *
      (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val) +
       neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralLogPhysical f.val))‖ ^ 2 = _
    rw [neutralLogPositivePairSource_inner]
  · apply hN.congr
    intro q
    simp only [N, lp.coeFn_smul, Pi.smul_apply, smul_eq_mul,
      lp.coeFn_sub, Pi.sub_apply]
    change ‖((Real.sqrt 2)⁻¹ : ℂ) *
      (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val) -
       neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralLogPhysical f.val))‖ ^ 2 = _
    rw [neutralLogNegativePairSource_inner]

/-- Generic non-Green full graph entry from square-summable actual raw
window samples. Its physical coordinate is exactly the original f.
The two ℓ² premises are genuine obligations, not asserted universally. -/
def neutralActualZetaFullSourceLiftOfRawSamples
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hA : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val)‖ ^ 2))
    (hB : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralLogPhysical f.val)‖ ^ 2)) :
    NeutralActualZetaSourceDomain a :=
  let hp := neutralActualZetaRawSamples_toSourcePN_sq_summable a f hA hB
  neutralActualZetaFullSourceLiftOfSquareSummable a f hp.1 hp.2

theorem neutralActualZetaFullSourceLiftOfRawSamples_physical
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hA : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val)‖ ^ 2))
    (hB : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralLogPhysical f.val)‖ ^ 2)) :
    neutralActualZetaSourcePhysical a
      (neutralActualZetaFullSourceLiftOfRawSamples a f hA hB) = f := by
  unfold neutralActualZetaFullSourceLiftOfRawSamples
  apply neutralActualZetaFullSourceLiftOfSquareSummable_physical


/-- Compose genuine explicit-formula absolute convergence, real-odd raw
sample conjugation, ℓ² P/N transport, and the unchanged complete
source-graph graph equations. The REAL-ODD symmetry and C² correlation
are explicit input obligations; logarithmic physical membership is the
type of f. No Green synthesis or density estimate is used. -/
def neutralActualZetaRealOddSmoothLogFullSourceLift
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hreg : ContDiff ℝ 2
      (neutralWindowCorrelation a (neutralLogPhysical f.val) (neutralLogPhysical f.val)))
    (hodd : ∀ q : NeutralActualZetaDivisorCoordinate,
      neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val) =
        -conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralLogPhysical f.val))) :
    NeutralActualZetaSourceDomain a := by
  have hB : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralLogPhysical f.val)‖ ^ 2) :=
    neutralActualZetaOddPhysicalWindowSample_sq_summable a
      (neutralLogPhysical f.val) hreg hodd
  have hA : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val)‖ ^ 2) := by
    apply hB.congr
    intro q
    rw [hodd q, norm_neg, Complex.norm_conj]
  exact neutralActualZetaFullSourceLiftOfRawSamples a f hA hB

/-- Exact original physical custody for any real-odd smooth full-graph
lift. This is not a newly synthesized physical approximation. -/
theorem neutralActualZetaRealOddSmoothLogFullSourceLift_physical
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hreg : ContDiff ℝ 2
      (neutralWindowCorrelation a (neutralLogPhysical f.val) (neutralLogPhysical f.val)))
    (hodd : ∀ q : NeutralActualZetaDivisorCoordinate,
      neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical f.val) =
        -conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralLogPhysical f.val))) :
    neutralActualZetaSourcePhysical a
      (neutralActualZetaRealOddSmoothLogFullSourceLift a f hreg hodd) = f := by
  unfold neutralActualZetaRealOddSmoothLogFullSourceLift
  apply neutralActualZetaFullSourceLiftOfRawSamples_physical

end
end WeilDefect
