import WeilDefect.Morphology.NeutralGaussianDualityAudit

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped SchwartzMap Topology ComplexConjugate

/-- Polarization determines a symmetric real bilinear form on its given vector
space. The theorem does not enlarge that space or its support window. -/
theorem realSymmetricBilinear_eq_of_diagonal
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B C : V →ₗ[ℝ] V →ₗ[ℝ] ℝ)
    (hB : ∀ x y, B x y = B y x)
    (hC : ∀ x y, C x y = C y x)
    (hdiag : ∀ x, B x x = C x x) (x y : V) :
    B x y = C x y := by
  have h := hdiag (x + y)
  simp only [map_add, LinearMap.add_apply] at h
  rw [hB y x, hC y x] at h
  linarith [hdiag x, hdiag y]

/-- Antilinear-first complexification, with real and imaginary components
represented explicitly. No analytic domain enlargement is implicit. -/
def realBilinearComplexification
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (z w : V × V) : ℂ :=
  (B z.1 w.1 : ℂ) + (B z.2 w.2 : ℂ) +
    Complex.I * ((B z.1 w.2 : ℂ) - (B z.2 w.1 : ℂ))

theorem realBilinearComplexification_eq_of_diagonal
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B C : V →ₗ[ℝ] V →ₗ[ℝ] ℝ)
    (hB : ∀ x y, B x y = B y x)
    (hC : ∀ x y, C x y = C y x)
    (hdiag : ∀ x, B x x = C x x) (z w : V × V) :
    realBilinearComplexification B z w =
      realBilinearComplexification C z w := by
  unfold realBilinearComplexification
  rw [realSymmetricBilinear_eq_of_diagonal B C hB hC hdiag z.1 w.1,
    realSymmetricBilinear_eq_of_diagonal B C hB hC hdiag z.2 w.2,
    realSymmetricBilinear_eq_of_diagonal B C hB hC hdiag z.1 w.2,
    realSymmetricBilinear_eq_of_diagonal B C hB hC hdiag z.2 w.1]

/-- Conjugating just the Schwartz factor preserves product integrability.
Measurability of the other factor is explicit; it is supplied by the residual
and pole carriers in the application. -/
theorem integrable_conjugateSchwartz_mul
    (f : SchwartzMap ℝ ℂ) (g : ℝ → ℂ)
    (hg : AEStronglyMeasurable g volume)
    (hfg : Integrable (fun x : ℝ => f x * g x) volume) :
    Integrable (fun x : ℝ => conjugateSchwartz f x * g x) volume := by
  apply hfg.mono
  · exact (conjugateSchwartz f).continuous.aestronglyMeasurable.mul hg
  · exact Eventually.of_forall fun x => by simp [norm_mul]

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Extend the existing all-compact-test weak identity to any integrably paired
Schwartz test. The proof uses the already certified generic cutoffs; no new
noncompact identity is assumed. -/
theorem rightLimitWeilWeakIdentity_of_integrableSchwartz
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (pole : ℝ → ℂ)
    (hEXT4 : RightLimitWeilWeakRealizationPremise c carrier residual hSymbol pole)
    (f : SchwartzMap ℝ ℂ)
    (hq : Integrable (fun x : ℝ => f x * residual.q x) volume)
    (hp : Integrable (fun x : ℝ => f x * pole x) volume) :
    (∫ x : ℝ, f x * residual.q x ∂volume) =
      rightLimitWeilMultiplierCore residual.a hSymbol carrier.temperedMode f +
        ∫ x : ℝ, f x * pole x ∂volume := by
  let core := rightLimitWeilMultiplierCore residual.a hSymbol carrier.temperedMode
  let cut : ℕ → SchwartzMap ℝ ℂ :=
    fun N => neutralGaussianSchwartzCutoff ((N : ℝ) + 1) f
  have hcut : Tendsto cut atTop (𝓝 f) := neutralGaussianSchwartzCutoff_tendsto f
  have hcore : Tendsto (fun N => core (cut N)) atTop (𝓝 (core f)) :=
    core.continuous.continuousAt.tendsto.comp hcut
  have hqLimit := neutralGaussianSchwartzCutoff_pairing_tendsto f residual.q hq
  have hpLimit := neutralGaussianSchwartzCutoff_pairing_tendsto f pole hp
  have hright := hcore.add hpLimit
  have hleft :
      Tendsto (fun N => ∫ x : ℝ, cut N x * residual.q x ∂volume)
        atTop (𝓝 (core f + ∫ x : ℝ, f x * pole x ∂volume)) := by
    refine hright.congr' ?_
    exact Eventually.of_forall fun N =>
      (hEXT4.weakIdentity (cut N)
        (neutralGaussianSchwartzCutoff_compact
          (by positivity : (N : ℝ) + 1 ≠ 0) f)).symm
  exact tendsto_nhds_unique hqLimit hleft

/-- The corrected Hermitian Gaussian test has integrable residual and pole
pairings and satisfies the weak identity. The exact all-compact-test witness
remains an explicit imported input, not a consequence of polarization alone. -/
theorem rightLimitWeilGaussianHermitian_of_growth
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (pole : ℝ → ℂ) (hpole : NeutralPoleExponentialGrowthData pole)
    (hEXT4 : RightLimitWeilWeakRealizationPremise c carrier residual hSymbol pole)
    (Ck : ℂ) {R : ℝ} (hc : 0 ≤ c) (hR : 0 < R)
    (hqLarge : 8 * residual.growthRate ≤ R * (residual.a - c))
    (hpLarge : 8 * hpole.growthRate ≤ R * (residual.a - c)) :
    Integrable
        (fun x : ℝ => movingGaussianFilteredModeDualTest Ck R hR carrier x * residual.q x)
        volume ∧
    Integrable
        (fun x : ℝ => movingGaussianFilteredModeDualTest Ck R hR carrier x * pole x)
        volume ∧
    (∫ x : ℝ, movingGaussianFilteredModeDualTest Ck R hR carrier x * residual.q x ∂volume) =
      rightLimitWeilMultiplierCore residual.a hSymbol carrier.temperedMode
        (movingGaussianFilteredModeDualTest Ck R hR carrier) +
      ∫ x : ℝ, movingGaussianFilteredModeDualTest Ck R hR carrier x * pole x ∂volume := by
  let f := movingGaussianFilteredModeSchwartz Ck R hR carrier
  have hq : Integrable (fun x : ℝ => f x * residual.q x) volume := by
    simpa only [f, movingGaussianFilteredModeSchwartz_apply, mul_comm] using
      residualFilteredMode_integrable carrier residual Ck hc hR hqLarge
  have hp : Integrable (fun x : ℝ => f x * pole x) volume := by
    simpa only [f, movingGaussianFilteredModeSchwartz_apply, mul_comm] using
      poleFilteredMode_integrable carrier residual pole hpole Ck hc hR hpLarge
  have hqDual := integrable_conjugateSchwartz_mul f residual.q
    residual.q_locallyIntegrable.aestronglyMeasurable hq
  have hpDual := integrable_conjugateSchwartz_mul f pole
    hpole.pole_locallyIntegrable.aestronglyMeasurable hp
  refine ⟨hqDual, hpDual, ?_⟩
  exact rightLimitWeilWeakIdentity_of_integrableSchwartz
    carrier residual hSymbol pole hEXT4 (conjugateSchwartz f) hqDual hpDual

/-- Conjugated carrier moments are the conjugates of the original moments. -/
theorem neutralWeilPoleMoment_conjugate_integral
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (s : ℝ) :
    (∫ x : ℝ, conj (carrier.h x) * (Real.exp (s * x) : ℂ) ∂volume) =
      conj (neutralWeilPoleMoment carrier s) := by
  rw [neutralWeilPoleMoment_eq_integral]
  simpa only [map_mul, Complex.conj_ofReal] using
    (integral_conj (μ := volume)
      (f := fun x : ℝ => carrier.h x * (Real.exp (s * x) : ℂ)))

/-- The actual Hermitian pole pairing. For complex carriers it is a conjugate
cross-moment sum, not the unconjugated product certified in RPB-107. -/
theorem neutralWeilSourcePole_hermitian_pairing_eq
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    (∫ x : ℝ, conj (carrier.h x) * neutralWeilSourcePole carrier x ∂volume) =
      neutralWeilPoleMoment carrier (-(1 / 2 : ℝ)) *
        conj (neutralWeilPoleMoment carrier (1 / 2)) +
      neutralWeilPoleMoment carrier (1 / 2) *
        conj (neutralWeilPoleMoment carrier (-(1 / 2 : ℝ))) := by
  let A := neutralWeilPoleMoment carrier (-(1 / 2 : ℝ))
  let B := neutralWeilPoleMoment carrier (1 / 2)
  have hint (s : ℝ) : Integrable
      (fun x : ℝ => conj (carrier.h x) * (Real.exp (s * x) : ℂ)) volume := by
    have hconj : Integrable
        (fun x : ℝ => conj (carrier.h x * (Real.exp (s * x) : ℂ))) volume :=
      Complex.conjCLE.toContinuousLinearMap.integrable_comp
        (neutralWeilPoleMoment_integrable_global carrier s)
    simpa only [map_mul, Complex.conj_ofReal] using hconj
  have hfun : (fun x : ℝ => conj (carrier.h x) * neutralWeilSourcePole carrier x) =
      (fun x : ℝ => A * (conj (carrier.h x) * (Real.exp ((1 / 2 : ℝ) * x) : ℂ)) +
        B * (conj (carrier.h x) * (Real.exp (-(1 / 2 : ℝ) * x) : ℂ))) := by
    funext x
    change conj (carrier.h x) *
      (A * (Real.exp (x / 2) : ℂ) + B * (Real.exp (-x / 2) : ℂ)) = _
    rw [show (1 / 2 : ℝ) * x = x / 2 by ring,
      show -(1 / 2 : ℝ) * x = -x / 2 by ring]
    ring
  rw [hfun, integral_add ((hint (1 / 2)).const_mul A)
      ((hint (-(1 / 2))).const_mul B), integral_const_mul, integral_const_mul,
    neutralWeilPoleMoment_conjugate_integral, neutralWeilPoleMoment_conjugate_integral]

end

end WeilDefect
