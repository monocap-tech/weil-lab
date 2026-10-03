import WeilDefect.Arithmetic.ActualZetaMultiplicitySymmetry
import WeilDefect.Morphology.NeutralLogBackgroundSourceAttachment

namespace WeilDefect

noncomputable section

open ContinuousLinearMap InnerProductSpace
open scoped ComplexConjugate BigOperators

/-- The actual sqrt(m) source weight uses the first-antilinear convention. -/
theorem neutralActualZetaWeightedNegativeSource_inner_factor
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralActualZetaWeightedNegativeSource a ρ) f =
      (Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ) : ℂ) *
        inner ℂ (neutralLogNegativePairSource a (neutralActualZetaOrdinate ρ)) f := by
  simpa only [neutralActualZetaWeightedNegativeSource, Complex.conj_ofReal] using
    (_root_.inner_smul_left (𝕜 := ℂ) (E := NeutralLogHilbertCarrier a)
      (neutralLogNegativePairSource a (neutralActualZetaOrdinate ρ)) f
      (Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ) : ℂ))

/-- Concrete window sampling at the two actual partner ordinates. -/
theorem neutralActualZetaWeightedNegativeSource_sampling
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralActualZetaWeightedNegativeSource a ρ) f =
      (Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ) : ℂ) *
        ((Real.sqrt 2)⁻¹ : ℂ) *
        (neutralWindowEvaluation a
            (neutralActualZetaOrdinate (neutralActualZetaZeroPair ρ))
            (neutralLogPhysical f.val) -
          neutralWindowEvaluation a (neutralActualZetaOrdinate ρ)
            (neutralLogPhysical f.val)) := by
  rw [neutralActualZetaWeightedNegativeSource_inner_factor,
    neutralLogNegativePairSource_inner, neutralActualZetaOrdinate_pair]
  ring

/-- The same actual sampling identity on the canonical supported logarithmic
form domain; no operator-domain L2 witness is used. -/
theorem neutralActualZetaWeightedNegativeSource_canonicalSampling
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) (f : neutralCanonicalLogFormDomain a) :
    inner ℂ (neutralActualZetaWeightedNegativeSource a ρ)
        (neutralCanonicalToLogHilbert f) =
      (Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ) : ℂ) *
        ((Real.sqrt 2)⁻¹ : ℂ) *
        (neutralWindowEvaluation a
            (neutralActualZetaOrdinate (neutralActualZetaZeroPair ρ)) f.val -
          neutralWindowEvaluation a (neutralActualZetaOrdinate ρ) f.val) := by
  rw [neutralActualZetaWeightedNegativeSource_sampling]
  have hp := congrArg Subtype.val (neutralLogHilbertToCanonical_leftInverse f)
  change neutralLogPhysical (neutralCanonicalToLogHilbert f).val = f.val at hp
  rw [hp]

/-- The actual integer multiplicity operator is exactly the rank-one of its
sqrt(m)-weighted normalized source, not a separately stipulated operator. -/
theorem neutralActualZetaWeightedSelectedOperator_rankOne
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaWeightedSelectedOperator a ρ =
      rankOne ℂ (neutralActualZetaWeightedNegativeSource a ρ)
        (neutralActualZetaWeightedNegativeSource a ρ) := by
  have hs : (Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ) : ℂ) *
      (Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ) : ℂ) =
        (neutralActualZetaMultiplicity ρ : ℂ) := by
    rw [← Complex.ofReal_mul, Real.mul_self_sqrt (Nat.cast_nonneg _)]
    simp only [Complex.ofReal_natCast]
  apply ContinuousLinearMap.ext
  intro f
  simp only [neutralActualZetaWeightedSelectedOperator,
    neutralActualZetaWeightedNegativeSource, neutralLogSelectedPairOperator,
    _root_.smul_apply, rankOne_apply, _root_.inner_smul_left,
    Complex.conj_ofReal, smul_smul]
  rw [mul_right_comm (Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ) : ℂ), hs]

theorem neutralActualZetaWeightedSelectedOperator_mixed
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaWeightedSelectedOperator a ρ g) =
      conj (inner ℂ (neutralActualZetaWeightedNegativeSource a ρ) f) *
        inner ℂ (neutralActualZetaWeightedNegativeSource a ρ) g := by
  rw [neutralActualZetaWeightedSelectedOperator_rankOne,
    inner_right_rankOne_apply,
    ← inner_conj_symm f (neutralActualZetaWeightedNegativeSource a ρ)]

theorem neutralActualZetaWeightedSelectedOperator_diagonal
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaWeightedSelectedOperator a ρ f) =
      ((‖inner ℂ (neutralActualZetaWeightedNegativeSource a ρ) f‖ ^ 2 : ℝ) : ℂ) := by
  simp only [neutralActualZetaWeightedSelectedOperator_mixed,
    Complex.conj_mul', Complex.ofReal_pow]

/-- Exact compression of the actual multiplicity fiber, including m copies. -/
theorem neutralActualZetaWeightedSelectedOperator_copies
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    neutralLogFiniteSelectedOperator a
        (fun _ : Fin (neutralActualZetaMultiplicity ρ) => neutralActualZetaOrdinate ρ) =
      neutralActualZetaWeightedSelectedOperator a ρ := by
  classical
  simp only [neutralLogFiniteSelectedOperator, Finset.sum_const,
    Finset.card_univ, Fintype.card_fin, neutralActualZetaWeightedSelectedOperator]
  exact (Nat.cast_smul_eq_nsmul (R := ℂ) (neutralActualZetaMultiplicity ρ)
    (neutralLogSelectedPairOperator a (neutralActualZetaOrdinate ρ))).symm

/-- Repeated actual divisor copies and weighted analysis give the same mixed
energy on the same logarithmic carrier. -/
theorem neutralActualZetaWeightedSelectedOperator_copyEnergy
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) (f g : NeutralLogHilbertCarrier a) :
    (∑ _ : Fin (neutralActualZetaMultiplicity ρ),
      conj (inner ℂ (neutralLogNegativePairSource a (neutralActualZetaOrdinate ρ)) f) *
        inner ℂ (neutralLogNegativePairSource a (neutralActualZetaOrdinate ρ)) g) =
      conj (inner ℂ (neutralActualZetaWeightedNegativeSource a ρ) f) *
        inner ℂ (neutralActualZetaWeightedNegativeSource a ρ) g := by
  rw [← neutralLogFiniteSelectedOperator_mixed a
    (fun _ : Fin (neutralActualZetaMultiplicity ρ) => neutralActualZetaOrdinate ρ),
    neutralActualZetaWeightedSelectedOperator_copies,
    neutralActualZetaWeightedSelectedOperator_mixed]

/-- Actual weighted finite selection; duplicates in the finite index remain
explicit. No infinite divisor enumeration or convergence is asserted. -/
def neutralActualZetaWeightedFiniteSelectedOperator {ι : Type*} [Fintype ι]
    (a : ℝ) (ρ : ι → NeutralActualZetaZeroPoint) :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  ∑ i, neutralActualZetaWeightedSelectedOperator a (ρ i)

theorem neutralActualZetaWeightedFiniteSelectedOperator_mixed {ι : Type*} [Fintype ι]
    (a : ℝ) (ρ : ι → NeutralActualZetaZeroPoint) (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaWeightedFiniteSelectedOperator a ρ g) =
      ∑ i, conj (inner ℂ (neutralActualZetaWeightedNegativeSource a (ρ i)) f) *
        inner ℂ (neutralActualZetaWeightedNegativeSource a (ρ i)) g := by
  classical
  simp only [neutralActualZetaWeightedFiniteSelectedOperator, _root_.sum_apply,
    _root_.inner_sum, neutralActualZetaWeightedSelectedOperator_mixed]

theorem neutralActualZetaWeightedFiniteSelectedOperator_diagonal {ι : Type*} [Fintype ι]
    (a : ℝ) (ρ : ι → NeutralActualZetaZeroPoint) (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaWeightedFiniteSelectedOperator a ρ f) =
      ((∑ i, ‖inner ℂ (neutralActualZetaWeightedNegativeSource a (ρ i)) f‖ ^ 2 : ℝ) : ℂ) := by
  classical
  simp only [neutralActualZetaWeightedFiniteSelectedOperator, _root_.sum_apply,
    _root_.inner_sum, neutralActualZetaWeightedSelectedOperator_diagonal, Complex.ofReal_sum]

theorem neutralActualZetaWeightedFiniteSelectedOperator_nonnegative {ι : Type*} [Fintype ι]
    (a : ℝ) (ρ : ι → NeutralActualZetaZeroPoint) (f : NeutralLogHilbertCarrier a) :
    0 ≤ (inner ℂ f (neutralActualZetaWeightedFiniteSelectedOperator a ρ f)).re := by
  rw [neutralActualZetaWeightedFiniteSelectedOperator_diagonal, Complex.ofReal_re]
  exact Finset.sum_nonneg (fun i _ => sq_nonneg _)

end

end WeilDefect
