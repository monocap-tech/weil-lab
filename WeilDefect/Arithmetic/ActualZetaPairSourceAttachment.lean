import WeilDefect.Arithmetic.ActualZetaZeroCoordinates
import WeilDefect.Morphology.NeutralLogSelectedSourceAttachment
import Mathlib.NumberTheory.Harmonic.ZetaAsymp

namespace WeilDefect

noncomputable section

open scoped ComplexConjugate

/-- Actual zeta conjugation on the open-strip point carrier. -/
def neutralActualZetaZeroConjugate (ρ : NeutralActualZetaZeroPoint) :
    NeutralActualZetaZeroPoint :=
  ⟨conj ρ.val, by rw [riemannZeta_conj, ρ.property.1, map_zero],
    by simpa only [Complex.conj_re] using ρ.property.2.1,
    by simpa only [Complex.conj_re] using ρ.property.2.2⟩

theorem neutralActualZetaZeroConjugate_involutive :
    Function.Involutive neutralActualZetaZeroConjugate := by
  intro ρ
  apply Subtype.ext
  change conj (conj ρ.val) = ρ.val
  exact star_star _

/-- Zeta conjugation acts as gamma -> -conj gamma, not conj gamma. -/
theorem neutralActualZetaOrdinate_conjugate (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaOrdinate (neutralActualZetaZeroConjugate ρ) =
      -conj (neutralActualZetaOrdinate ρ) := by
  apply Complex.ext
  · simp only [neutralActualZetaOrdinate_re, Complex.neg_re, Complex.conj_re]
    change (conj ρ.val).im = -ρ.val.im
    exact Complex.conj_im _
  · simp only [neutralActualZetaOrdinate_im, Complex.neg_im, Complex.conj_im]
    change 1 / 2 - (conj ρ.val).re = -(-(1 / 2 - ρ.val.re))
    simp only [Complex.conj_re, neg_neg]

theorem neutralActualZetaZeroConjugate_reflect (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaZeroConjugate (neutralActualZetaZeroReflect ρ) =
      neutralActualZetaZeroReflect (neutralActualZetaZeroConjugate ρ) := by
  apply Subtype.ext
  change conj (1 - ρ.val) = 1 - conj ρ.val
  simp only [map_sub, map_one]

/-- Actual conjugate-ordinate partner: rho -> 1-conj rho.
It is obtained from two certified symmetries, not assumed as packet data. -/
def neutralActualZetaZeroPair (ρ : NeutralActualZetaZeroPoint) :
    NeutralActualZetaZeroPoint :=
  neutralActualZetaZeroReflect (neutralActualZetaZeroConjugate ρ)

theorem neutralActualZetaZeroPair_involutive :
    Function.Involutive neutralActualZetaZeroPair := by
  intro ρ
  apply Subtype.ext
  change 1 - conj (1 - conj ρ.val) = ρ.val
  simp only [map_sub, map_one, starRingEnd_apply, star_star]
  ring

/-- The actual point partner has precisely the required conjugate ordinate. -/
theorem neutralActualZetaOrdinate_pair (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaOrdinate (neutralActualZetaZeroPair ρ) =
      conj (neutralActualZetaOrdinate ρ) := by
  unfold neutralActualZetaZeroPair
  rw [neutralActualZetaOrdinate_reflect, neutralActualZetaOrdinate_conjugate, neg_neg]

/-- Attach the existing positive source symmetry to the actual point pair. -/
theorem neutralActualZetaPair_positiveSource (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    neutralLogPositivePairSource a
      (neutralActualZetaOrdinate (neutralActualZetaZeroPair ρ)) =
      neutralLogPositivePairSource a (neutralActualZetaOrdinate ρ) := by
  rw [neutralActualZetaOrdinate_pair, neutralLogPositivePairSource_conjugate]

/-- The actual negative source changes sign, recording the linear-analysis
convention in the concrete logarithmic carrier. -/
theorem neutralActualZetaPair_negativeSource (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    neutralLogNegativePairSource a
      (neutralActualZetaOrdinate (neutralActualZetaZeroPair ρ)) =
      -neutralLogNegativePairSource a (neutralActualZetaOrdinate ρ) := by
  rw [neutralActualZetaOrdinate_pair, neutralLogNegativePairSource_conjugate]

/-- The actual selected negative rank-one operator is pair-invariant. -/
theorem neutralActualZetaPair_selectedOperator (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    neutralLogSelectedPairOperator a
      (neutralActualZetaOrdinate (neutralActualZetaZeroPair ρ)) =
      neutralLogSelectedPairOperator a (neutralActualZetaOrdinate ρ) := by
  rw [neutralActualZetaOrdinate_pair, neutralLogSelectedPairOperator_conjugate]

end

end WeilDefect
