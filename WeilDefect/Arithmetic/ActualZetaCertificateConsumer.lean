import WeilDefect.Arithmetic.ActualZetaNativeFormOperator
import WeilDefect.Screening.CanonicalCertificateTransport
import WeilDefect.Screening.PhysicalResidualTransport

namespace WeilDefect

noncomputable section

/-- The supported logarithmic carrier's actual physical inclusion is a
contraction. This uses the existing energy comparison, not an extra premise. -/
theorem neutralActualZetaLogPhysical_norm_le
    (a : ℝ) (h : NeutralLogHilbertCarrier a) :
    ‖neutralLogPhysical h.val‖ ≤ ‖h‖ := by
  have hb := neutralActualZetaCanonical_mass_le_log a (neutralLogHilbertToCanonical h)
  have heq : neutralLogWeightedL2 (neutralLogHilbertToCanonical h) = h.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse h)
  rw [heq] at hb
  change ‖neutralLogPhysical h.val‖ ^ 2 ≤ ‖h‖ ^ 2 at hb
  nlinarith [norm_nonneg (neutralLogPhysical h.val), norm_nonneg h]

/-- An attached whole physical residual certifies a canonical Riesz error
on the actual supported carrier. The source identity is quantified over
the whole carrier; finite Galerkin stationarity cannot replace it. -/
theorem neutralActualZetaLogRiesz_error_sq_le_physical
    (a : ℝ) (e : NeutralLogHilbertCarrier a) (f : RealComplexL2)
    (hweak : ∀ h : NeutralLogHilbertCarrier a,
      inner ℂ e h = inner ℂ f (neutralLogPhysical h.val)) :
    ‖e‖ ^ 2 ≤ ‖f‖ ^ 2 := by
  have h := CanonicalCertificate.riesz_error_sq_le_physical_residual
    (fun h : NeutralLogHilbertCarrier a => neutralLogPhysical h.val)
    e f 1 1 (by norm_num) (by norm_num)
    (fun h => by simpa using neutralActualZetaLogPhysical_norm_le a h) hweak
  simpa using h

/-- Pin the Schur consumer to the actual supported logarithmic carrier.
The full native head/tail/mixed lower estimate is an explicit hypothesis. -/
theorem neutralActualZetaLogWeilFormOperator_schur_floor
    (a : ℝ) (f : NeutralLogHilbertCarrier a) (x y m d β δ : ℝ)
    (hm : δ < m)
    (hdet : β ^ 2 ≤ (m - δ) * (d - δ))
    (hnorm : ‖f‖ ^ 2 = x ^ 2 + y ^ 2)
    (hlower : m * x ^ 2 - 2 * β * x * y + d * y ^ 2 ≤
      (inner ℂ f (neutralActualZetaLogWeilFormOperator a f)).re) :
    δ * ‖f‖ ^ 2 ≤
      neutralActualZetaCanonicalNativeQuadratic a (neutralLogHilbertToCanonical f) := by
  have h := CanonicalCertificate.schur_reserve
    (inner ℂ f (neutralActualZetaLogWeilFormOperator a f)).re
    x y m d β δ hm hdet hlower
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re] at h
  rw [hnorm]
  exact h

/-- Transport a full-carrier floor to every member of the original supported
canonical form domain, using the existing exact inverse maps. -/
theorem neutralActualZetaCanonicalNativeQuadratic_floor_of_operator
    (a δ : ℝ)
    (hfloor : ∀ f : NeutralLogHilbertCarrier a,
      δ * ‖f‖ ^ 2 ≤ (inner ℂ f (neutralActualZetaLogWeilFormOperator a f)).re)
    (f : neutralCanonicalLogFormDomain a) :
    δ * ‖neutralCanonicalToLogHilbert f‖ ^ 2 ≤
      neutralActualZetaCanonicalNativeQuadratic a f := by
  have h := hfloor (neutralCanonicalToLogHilbert f)
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re,
    neutralLogHilbertToCanonical_leftInverse f] at h
  exact h

/-- Full canonical positivity implies positivity of the attached actual-zeta
Green zero form. This does not identify Green closure with the source graph. -/
theorem neutralActualZetaGreenZeroForm_nonnegative_of_canonical
    (a : ℝ) (ha : 0 < a)
    (hpositive : ∀ f : neutralCanonicalLogFormDomain a,
      0 ≤ neutralActualZetaCanonicalNativeQuadratic a f)
    (v : NeutralActualZetaGreenCoefficients) :
    0 ≤ (neutralActualZetaGreenZeroForm a v v).re := by
  rw [neutralActualZetaGreenZeroForm_canonical_quadratic a ha v]
  exact hpositive (neutralActualZetaGreenCanonical a ha v)

end
end WeilDefect
