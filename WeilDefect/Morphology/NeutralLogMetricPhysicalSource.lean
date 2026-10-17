import WeilDefect.Morphology.NeutralLogHilbertCarrier
import WeilDefect.Screening.PhysicalResidualTransport

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate

/-- The full logarithmic spectral product. Its L2 membership is an operator
 domain condition, stronger than membership of the logarithmic form domain. -/
def neutralLogMetricSpectralProduct {a : ℝ}
    (v : NeutralLogHilbertCarrier a) (ξ : ℝ) : ℂ :=
  (logarithmicFourierWeight ξ : ℂ) *
    (𝓕 (neutralLogPhysical v.val) : RealComplexL2) ξ

/-- An actual physical source, constructed only when the full product is L2.
No bounded physical operator on the entire form domain is asserted. -/
def neutralLogMetricPhysicalSource {a : ℝ}
    (v : NeutralLogHilbertCarrier a)
    (hp : MemLp (neutralLogMetricSpectralProduct v) 2 volume) : RealComplexL2 :=
  𝓕⁻ (hp.toLp (neutralLogMetricSpectralProduct v))

theorem neutralLogMetricPhysicalSource_fourier {a : ℝ}
    (v : NeutralLogHilbertCarrier a)
    (hp : MemLp (neutralLogMetricSpectralProduct v) 2 volume) :
    (𝓕 (neutralLogMetricPhysicalSource v hp) : RealComplexL2) =
      hp.toLp (neutralLogMetricSpectralProduct v) := by
  unfold neutralLogMetricPhysicalSource
  exact fourier_fourierInv_eq _

/-- Full-carrier metric pairing, with the exact existing Fourier weight. -/
theorem neutralLogHilbertCarrier_inner_metric {a : ℝ}
    (v h : NeutralLogHilbertCarrier a) :
    inner ℂ v h = ∫ ξ, conj ((𝓕 (neutralLogPhysical v.val) : RealComplexL2) ξ) *
      (logarithmicFourierWeight ξ : ℂ) *
      (𝓕 (neutralLogPhysical h.val) : RealComplexL2) ξ := by
  have ev : neutralLogWeightedL2 (neutralLogHilbertToCanonical v) = v.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse v)
  have eh : neutralLogWeightedL2 (neutralLogHilbertToCanonical h) = h.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse h)
  have hm := neutralLogWeightedL2_inner
    (neutralLogHilbertToCanonical v) (neutralLogHilbertToCanonical h)
  rw [ev, eh] at hm
  exact hm

/-- The constructed source represents the metric against every canonical
 test vector. The spectral membership premise is not inferred from form energy. -/
theorem neutralLogMetricPhysicalSource_weak {a : ℝ}
    (v : NeutralLogHilbertCarrier a)
    (hp : MemLp (neutralLogMetricSpectralProduct v) 2 volume)
    (h : NeutralLogHilbertCarrier a) :
    inner ℂ v h =
      inner ℂ (neutralLogMetricPhysicalSource v hp) (neutralLogPhysical h.val) := by
  rw [neutralLogHilbertCarrier_inner_metric,
    ← Lp.inner_fourier_eq (neutralLogMetricPhysicalSource v hp)
      (neutralLogPhysical h.val), neutralLogMetricPhysicalSource_fourier,
    L2.inner_def]
  apply integral_congr_ae
  filter_upwards [hp.coeFn_toLp] with ξ hξ
  rw [RCLike.inner_apply', hξ]
  simp only [neutralLogMetricSpectralProduct, map_mul, Complex.conj_ofReal]
  ring

/-- Consume the constructed trial action, rather than an assumed action identity.
The moment representative remains attached by its whole source identity. -/
theorem neutralLogMetricPhysicalSource_riesz_residual {a : ℝ}
    (r v : NeutralLogHilbertCarrier a) (p : RealComplexL2)
    (hp : MemLp (neutralLogMetricSpectralProduct v) 2 volume)
    (hsource : ∀ h : NeutralLogHilbertCarrier a,
      inner ℂ r h = inner ℂ p (neutralLogPhysical h.val)) :
    ∀ h : NeutralLogHilbertCarrier a,
      inner ℂ (r - v) h =
        inner ℂ (p - neutralLogMetricPhysicalSource v hp) (neutralLogPhysical h.val) :=
  CanonicalCertificate.weak_residual_of_source_and_action
    (fun h : NeutralLogHilbertCarrier a => neutralLogPhysical h.val)
    r v p (neutralLogMetricPhysicalSource v hp) hsource
    (neutralLogMetricPhysicalSource_weak v hp)

end
end WeilDefect
