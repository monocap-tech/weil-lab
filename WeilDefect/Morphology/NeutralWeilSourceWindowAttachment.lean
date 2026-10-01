import WeilDefect.Morphology.NeutralWeilPrimeShellTranslation

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/--
A compact Schwartz test fits inside some larger symmetric open window whose
radius is at least any prescribed base radius.
-/
theorem compactSchwartz_support_in_symmetric_window
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) (a : ℝ) :
    ∃ b : ℝ, a ≤ b ∧ Function.support u ⊆ Set.Ioo (-b) b := by
  obtain ⟨r, hr, hsub⟩ :=
    hu.isBounded.subset_closedBall_lt (max a 0) (0 : ℝ)
  let b : ℝ := r + 1
  refine ⟨b, ?_, ?_⟩
  · dsimp [b]
    have ha : a ≤ max a 0 := le_max_left _ _
    linarith
  · intro x hx
    have hts : x ∈ tsupport u := subset_tsupport u hx
    have hball := hsub hts
    rw [Real.closedBall_eq_Icc, zero_sub, zero_add] at hball
    dsimp [b]
    exact ⟨by linarith, by linarith⟩

/--
For an arbitrary Schwartz test, the base frozen action equals the larger-window
action plus the exact physical prime shell added between the two radii.

Unlike the old-window compression theorem, this statement imposes no support
restriction on the test.  The shell term is precisely what is lost when the
test leaves the old window.
-/
theorem frozenWeilCompactAction_eq_larger_add_shell
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b : ℝ} (hab : a ≤ b)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hb : RightLimitWeilSymbolTemperatePremise b)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    frozenWeilCompactAction carrier a ha u hu =
      frozenWeilCompactAction carrier b hb u hu +
        ∫ x : ℝ, u x * frozenWeilPrimeShellPhysical carrier a b x ∂volume := by
  have hdiff :=
    frozenWeilCompactAction_radius_correction carrier hab ha hb u hu
  rw [frozenWeilPrimeShell_fourier_physical_pairing] at hdiff
  linear_combination hdiff

/--
Source-facing shell-corrected local-window premise.

For every enlarged finite source window, the source-side realization must
identify the selected frozen residual with the larger-window compact action
plus the explicit finite prime shell needed to return to the fixed base
cutoff.

This is the lawful replacement for the invalid statement that a larger-window
action can be compressed to the base action on an arbitrary larger-support
test.  On tests already supported in the base window, the shell pairing
vanishes by the certified support theorem and this reduces to ordinary
compression.
-/
structure RightLimitWeilCorrectedSourceWindowPremise
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c) : Prop where
  symbolAt :
    ∀ b : ℝ, residual.a ≤ b →
      RightLimitWeilSymbolTemperatePremise b
  weakIdentityOnWindow :
    ∀ (b : ℝ) (hab : residual.a ≤ b)
      (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      Function.support u ⊆ Set.Ioo (-b) b →
      (∫ x : ℝ, u x * residual.q x ∂volume) =
        frozenWeilCompactAction carrier b (symbolAt b hab) u hu +
          ∫ x : ℝ,
            u x * frozenWeilPrimeShellPhysical carrier residual.a b x
            ∂volume

/--
Shell-corrected finite-window source identities globalize to the exact
all-compact-test frozen weak-realization premise.

The compact support of each test is used only to choose a large enough source
window.  The return from that window to the fixed base cutoff carries the
finite prime-shell correction explicitly.
-/
theorem rightLimitWeilWeakRealizationPremise_of_correctedSourceWindows
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hBase : RightLimitWeilSymbolTemperatePremise residual.a)
    (hSource :
      RightLimitWeilCorrectedSourceWindowPremise carrier residual) :
    RightLimitWeilWeakRealizationPremise
      c carrier residual hBase (neutralWeilSourcePole carrier) := by
  refine ⟨(neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable, ?_⟩
  intro u hu
  obtain ⟨b, hab, huWindow⟩ :=
    compactSchwartz_support_in_symmetric_window u hu residual.a
  let hb := hSource.symbolAt b hab
  have hlocal :
      (∫ x : ℝ, u x * residual.q x ∂volume) =
        frozenWeilCompactAction carrier b hb u hu +
          ∫ x : ℝ,
            u x * frozenWeilPrimeShellPhysical carrier residual.a b x
            ∂volume := by
    exact hSource.weakIdentityOnWindow b hab u hu huWindow
  have hreturn :
      frozenWeilCompactAction carrier residual.a hBase u hu =
        frozenWeilCompactAction carrier b hb u hu +
          ∫ x : ℝ,
            u x * frozenWeilPrimeShellPhysical carrier residual.a b x
            ∂volume :=
    frozenWeilCompactAction_eq_larger_add_shell
      carrier hab hBase hb u hu
  exact hlocal.trans hreturn.symm

/--
The certified Hermitian Gaussian bridge consumes the shell-corrected
finite-window source premise after globalization.  No new Gaussian identity is
assumed.
-/
theorem rightLimitWeilGaussianHermitian_of_correctedSourceWindows
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hBase : RightLimitWeilSymbolTemperatePremise residual.a)
    (hSource :
      RightLimitWeilCorrectedSourceWindowPremise carrier residual)
    (Ck : ℂ) {R : ℝ} (hc : 0 ≤ c) (hR : 0 < R)
    (hqLarge :
      8 * residual.growthRate ≤ R * (residual.a - c))
    (hpLarge :
      8 * (neutralWeilSourcePole_growthData carrier).growthRate
        ≤ R * (residual.a - c)) :
    Integrable
        (fun x : ℝ =>
          movingGaussianFilteredModeDualTest Ck R hR carrier x * residual.q x)
        volume ∧
    Integrable
        (fun x : ℝ =>
          movingGaussianFilteredModeDualTest Ck R hR carrier x *
            neutralWeilSourcePole carrier x)
        volume ∧
    (∫ x : ℝ,
        movingGaussianFilteredModeDualTest Ck R hR carrier x * residual.q x
        ∂volume) =
      rightLimitWeilMultiplierCore residual.a hBase carrier.temperedMode
        (movingGaussianFilteredModeDualTest Ck R hR carrier)
      +
      ∫ x : ℝ,
        movingGaussianFilteredModeDualTest Ck R hR carrier x *
          neutralWeilSourcePole carrier x
        ∂volume := by
  let hEXT4 :=
    rightLimitWeilWeakRealizationPremise_of_correctedSourceWindows
      carrier residual hBase hSource
  exact
    rightLimitWeilGaussianHermitian_of_growth
      carrier residual hBase
      (neutralWeilSourcePole carrier)
      (neutralWeilSourcePole_growthData carrier)
      hEXT4 Ck hc hR hqLarge hpLarge

end

end WeilDefect
