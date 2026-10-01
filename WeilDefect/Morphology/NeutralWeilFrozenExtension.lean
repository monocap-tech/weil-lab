import WeilDefect.Morphology.NeutralGaussianHermitianBridge

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped BigOperators SchwartzMap FourierTransform

/-- Compact Schwartz tests pair integrably with any locally integrable function. -/
theorem compactSchwartz_mul_locallyIntegrable
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u)
    (p : ℝ → ℂ) (hp : LocallyIntegrable p volume) :
    Integrable (fun x : ℝ => u x * p x) volume := by
  have hpOn : IntegrableOn p (tsupport u) volume :=
    hp.integrableOn_isCompact hu
  have hOn : IntegrableOn (fun x : ℝ => p x * u x) (tsupport u) volume :=
    hpOn.mul_continuousOn u.continuous.continuousOn hu
  have hglobal : Integrable (fun x : ℝ => p x * u x) volume :=
    hOn.integrable_of_forall_notMem_eq_zero (fun x hx => by
      rw [image_eq_zero_of_notMem_tsupport hx, mul_zero])
  simpa only [mul_comm] using hglobal

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The selected whole-line extension evaluated only on compact Schwartz tests.
The prime cutoff a is independent of the test support. This definition asserts
neither a pointwise residual representative nor equality with the imported form. -/
def frozenWeilCompactAction
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (_hu : HasCompactSupport u) : ℂ :=
  rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode u +
    ∫ x : ℝ, u x * neutralWeilSourcePole carrier x ∂volume

theorem frozenWeilCompactAction_pole_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    Integrable (fun x : ℝ => u x * neutralWeilSourcePole carrier x) volume :=
  compactSchwartz_mul_locallyIntegrable u hu _
    (neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable

/-- Additivity is proved with genuine pole integrability, not total-integral defaults. -/
theorem frozenWeilCompactAction_add
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u v : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u)
    (hv : HasCompactSupport v) :
    frozenWeilCompactAction carrier a hSymbol (u + v) (hu.add hv) =
      frozenWeilCompactAction carrier a hSymbol u hu +
      frozenWeilCompactAction carrier a hSymbol v hv := by
  unfold frozenWeilCompactAction
  simp only [map_add, SchwartzMap.add_apply, add_mul]
  rw [integral_add
    (frozenWeilCompactAction_pole_integrable carrier u hu)
    (frozenWeilCompactAction_pole_integrable carrier v hv)]
  ring

/-- Exact attachment characterization. This equivalence does not construct the
residual: its left side is the still-required representation of this action. -/
theorem frozenWeilCompactAction_represents_iff
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a) :
    (∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      (∫ x : ℝ, u x * residual.q x ∂volume) =
        frozenWeilCompactAction carrier residual.a hSymbol u hu) ↔
    RightLimitWeilWeakRealizationPremise c carrier residual hSymbol
      (neutralWeilSourcePole carrier) := by
  constructor
  · intro h
    exact ⟨(neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable, h⟩
  · intro h u hu
    exact h.weakIdentity u hu

/-- The threshold-corrected prime sets are monotone in the cutoff radius. -/
theorem rightLimitPrimePowerFinset_mono {a b : ℝ} (hab : a ≤ b) :
    rightLimitPrimePowerFinset a ⊆ rightLimitPrimePowerFinset b := by
  intro n hn
  rw [mem_rightLimitPrimePowerFinset] at hn ⊢
  exact ⟨hn.1, hn.2.trans (by linarith)⟩

/-- Finite prime shell added when the chosen cutoff changes from a to b. -/
def frozenWeilPrimeShell (a b : ℝ) : Finset ℕ :=
  rightLimitPrimePowerFinset b \ rightLimitPrimePowerFinset a

/-- Positive shell trigonometric sum in the already fixed mathlib frequency. -/
def frozenWeilPrimeShellSymbol (a b ξ : ℝ) : ℝ :=
  ∑ n ∈ frozenWeilPrimeShell a b,
    compactWindowPrimeCoefficient n *
      Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ))

/-- Exact cutoff bookkeeping, including equality thresholds. The archimedean
part cancels; the difference consists of precisely the newly added primes. -/
theorem frozenWeilPrimeShellSymbol_eq {a b : ℝ} (hab : a ≤ b) (ξ : ℝ) :
    frozenWeilPrimeShellSymbol a b ξ =
      rightLimitCompactWeilSymbolMathlib a ξ -
      rightLimitCompactWeilSymbolMathlib b ξ := by
  unfold frozenWeilPrimeShellSymbol frozenWeilPrimeShell
  rw [Finset.sum_sdiff_eq_sub (rightLimitPrimePowerFinset_mono hab)]
  simp only [rightLimitCompactWeilSymbolMathlib_eq]
  ring

/-- Linearity in the multiplier symbol, derived on the actual test action. -/
theorem temperedFourierMultiplier_sub
    (g₁ g₂ : ℝ → ℂ) (h₁ : Function.HasTemperateGrowth g₁)
    (h₂ : Function.HasTemperateGrowth g₂) (f : RealComplexTempered) :
    TemperedDistribution.fourierMultiplierCLM ℂ (g₁ - g₂) f =
      TemperedDistribution.fourierMultiplierCLM ℂ g₁ f -
      TemperedDistribution.fourierMultiplierCLM ℂ g₂ f := by
  ext u
  simp [TemperedDistribution.fourierMultiplierCLM_apply_apply,
    SchwartzMap.smulLeftCLM_sub h₁ h₂]

/-- The frozen multiplier core is recovered from a larger cutoff by adding
back exactly the shell multiplier. No global equality of the two cores is used. -/
theorem frozenWeilMultiplier_radius_correction
    {a b : ℝ} (hab : a ≤ b)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hb : RightLimitWeilSymbolTemperatePremise b)
    (f : RealComplexTempered) :
    rightLimitWeilMultiplierCore a ha f - rightLimitWeilMultiplierCore b hb f =
      TemperedDistribution.fourierMultiplierCLM ℂ
        (fun ξ : ℝ => (frozenWeilPrimeShellSymbol a b ξ : ℂ)) f := by
  have heq : (fun ξ : ℝ => (frozenWeilPrimeShellSymbol a b ξ : ℂ)) =
      (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ)) -
      (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib b ξ : ℂ)) := by
    funext ξ
    simp [frozenWeilPrimeShellSymbol_eq hab]
  rw [heq, temperedFourierMultiplier_sub _ _ ha.hasTemperateGrowth hb.hasTemperateGrowth]
  rfl

/-- Exact compact-test correction. The named pole is independent of the
auxiliary source window and therefore cancels in the radius difference. -/
theorem frozenWeilCompactAction_radius_correction
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b : ℝ} (hab : a ≤ b)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hb : RightLimitWeilSymbolTemperatePremise b)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    frozenWeilCompactAction carrier a ha u hu -
        frozenWeilCompactAction carrier b hb u hu =
      TemperedDistribution.fourierMultiplierCLM ℂ
        (fun ξ : ℝ => (frozenWeilPrimeShellSymbol a b ξ : ℂ))
        carrier.temperedMode u := by
  have h := congrArg (fun T : RealComplexTempered => T u)
    (frozenWeilMultiplier_radius_correction hab ha hb carrier.temperedMode)
  simp only [frozenWeilCompactAction]
  simpa only [ContinuousLinearMap.sub_apply, add_sub_add_right_eq_sub] using h

/-- Physical finite-translation shell with the source coefficient Lambda/sqrt.
Fourier compatibility with the shell multiplier is a separate obligation. -/
def frozenWeilPrimeShellPhysical
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a b x : ℝ) : ℂ :=
  ∑ n ∈ frozenWeilPrimeShell a b,
    ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
      (carrier.h (x - Real.log (n : ℝ)) + carrier.h (x + Real.log (n : ℝ)))

/-- New shell shifts have log n > 2a. They cannot meet the old open window
when the physical input is supported within [-c,c], c <= a. -/
theorem frozenWeilPrimeShellPhysical_zero_on_window
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b x : ℝ} (hca : c ≤ a) (hx : x ∈ Set.Ioo (-a) a) :
    frozenWeilPrimeShellPhysical carrier a b x = 0 := by
  unfold frozenWeilPrimeShellPhysical
  apply Finset.sum_eq_zero
  intro n hn
  have hn' := Finset.mem_sdiff.mp hn
  have hnPrime := (mem_rightLimitPrimePowerFinset b n).mp hn'.1
  have hlog : 2 * a < Real.log (n : ℝ) := by
    by_contra h
    apply hn'.2
    exact (mem_rightLimitPrimePowerFinset a n).mpr
      ⟨hnPrime.1, le_of_not_gt h⟩
  have hm : carrier.h (x - Real.log (n : ℝ)) = 0 :=
    carrier.representative_eq_zero_of_not_mem (by
      intro hmem
      have := hmem.1
      linarith [hx.2])
  have hp : carrier.h (x + Real.log (n : ℝ)) = 0 :=
    carrier.representative_eq_zero_of_not_mem (by
      intro hmem
      have := hmem.2
      linarith [hx.1])
  rw [hm, hp, zero_add, mul_zero]

/-- Every test supported in the old open window annihilates the physical shell.
The integral is zero because the integrand is pointwise zero. -/
theorem frozenWeilPrimeShellPhysical_pairing_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b : ℝ} (hca : c ≤ a) (u : ℝ → ℂ)
    (hu : Function.support u ⊆ Set.Ioo (-a) a) :
    (∫ x : ℝ, u x * frozenWeilPrimeShellPhysical carrier a b x ∂volume) = 0 := by
  have heq : (fun x : ℝ => u x * frozenWeilPrimeShellPhysical carrier a b x) = 0 := by
    funext x
    by_cases hx : u x = 0
    · simp [hx]
    · rw [frozenWeilPrimeShellPhysical_zero_on_window carrier hca (hu hx), mul_zero]
      rfl
  rw [heq]
  simp

end

end WeilDefect
