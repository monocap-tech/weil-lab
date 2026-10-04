import WeilDefect.Arithmetic.ActualZetaGreenGraphAnalysis

namespace WeilDefect
noncomputable section
open ContinuousLinearMap InnerProductSpace
open scoped InnerProduct
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false
local instance : DecidableEq NeutralActualZetaDivisorCoordinate := Classical.decEq _

/-- A unit coefficient synthesizes exactly the actual endpoint-corrected
Green column, not a new representative. -/
theorem neutralActualZetaGreenSynthesis_single (a : ℝ)
    (q : NeutralActualZetaDivisorCoordinate) (c : ℂ) :
    neutralActualZetaGreenSynthesis a (lp.single 2 q c) =
      c • neutralActualZetaGreenColumn a q := by
  simp [neutralActualZetaGreenSynthesis, lp.single_apply, Pi.single_apply]

/-- Physical L2 custody of each actual unit graph packet. -/
theorem neutralActualZetaGreenPacketColumn_l2 (a : ℝ) (ha : 0 < a)
    (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaHilbertSourceL2 a (neutralActualZetaGreenPacketColumn a ha q) =
      neutralActualZetaGreenColumn a q := by
  rw [neutralActualZetaGreenPacketColumn, neutralActualZetaGreenHilbertSourceL2,
    neutralActualZetaGreenSynthesis_single, one_smul]

/-- Copies with the same ordinate have the same whole graph packet, including
both full source coordinates. Multiplicity indices are not extra observations. -/
theorem neutralActualZetaGreenPacketColumn_eq_of_ordinate
    (a : ℝ) (ha : 0 < a) (q r : NeutralActualZetaDivisorCoordinate)
    (h : neutralActualZetaDivisorOrdinate q = neutralActualZetaDivisorOrdinate r) :
    neutralActualZetaGreenPacketColumn a ha q =
      neutralActualZetaGreenPacketColumn a ha r := by
  apply neutralActualZetaHilbertSourceL2_injective a
  rw [neutralActualZetaGreenPacketColumn_l2, neutralActualZetaGreenPacketColumn_l2]
  simp only [neutralActualZetaGreenColumn, h]

/-- Exact finite collision vector in the actual synthesis kernel. This
does not assert that actual zeta has a repeated zero. -/
theorem neutralActualZetaGreenHilbertSource_collision
    (a : ℝ) (ha : 0 < a) (q r : NeutralActualZetaDivisorCoordinate)
    (h : neutralActualZetaDivisorOrdinate q = neutralActualZetaDivisorOrdinate r) :
    neutralActualZetaGreenHilbertSourceContinuous a ha
      (lp.single 2 q 1 - lp.single 2 r 1) = 0 := by
  rw [map_sub]
  change neutralActualZetaGreenPacketColumn a ha q -
    neutralActualZetaGreenPacketColumn a ha r = 0
  rw [neutralActualZetaGreenPacketColumn_eq_of_ordinate a ha q r h, sub_self]

/-- Distinct multiplicity coordinates give a nonzero finite coefficient
difference even when their actual Green packets coincide. -/
theorem neutralActualZetaGreenCoefficient_collision_ne_zero
    (q r : NeutralActualZetaDivisorCoordinate) (h : q ≠ r) :
    (lp.single 2 q 1 - lp.single 2 r 1 : NeutralActualZetaGreenCoefficients) ≠ 0 := by
  intro hz
  have hv := congrArg (fun v : NeutralActualZetaGreenCoefficients => v q) hz
  simp [lp.coeFn_sub, lp.single_apply, Pi.single_apply, h, h.symm] at hv

/-- Each adjoint graph-analysis coordinate is the inner product with that
same whole graph packet; no physical-only sampling substitution is made. -/
theorem neutralActualZetaGreenGraphAnalysis_coordinate
    (a : ℝ) (ha : 0 < a) (f : NeutralActualZetaHilbertSourceDomain a)
    (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaGreenGraphAnalysis a ha f q =
      inner ℂ (neutralActualZetaGreenPacketColumn a ha q) f := by
  have h := (neutralActualZetaGreenHilbertSourceContinuous a ha).adjoint_inner_right
    (lp.single 2 q 1) f
  simpa [neutralActualZetaGreenGraphAnalysis, lp.inner_single_left,
    RCLike.inner_apply', neutralActualZetaGreenPacketColumn] using h

/-- Actual analysis observations are constant across copies at the same
ordinate, although every copy remains in the coefficient-energy sums. -/
theorem neutralActualZetaGreenGraphAnalysis_same_ordinate
    (a : ℝ) (ha : 0 < a) (f : NeutralActualZetaHilbertSourceDomain a)
    (q r : NeutralActualZetaDivisorCoordinate)
    (h : neutralActualZetaDivisorOrdinate q = neutralActualZetaDivisorOrdinate r) :
    neutralActualZetaGreenGraphAnalysis a ha f q =
      neutralActualZetaGreenGraphAnalysis a ha f r := by
  rw [neutralActualZetaGreenGraphAnalysis_coordinate,
    neutralActualZetaGreenGraphAnalysis_coordinate,
    neutralActualZetaGreenPacketColumn_eq_of_ordinate a ha q r h]

end
end WeilDefect
