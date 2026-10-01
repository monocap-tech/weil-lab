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
Source-facing local-window premise.

For every enlarged finite window, the source supplies:
1. the already explicit temperate-growth witness for that window's symbol;
2. the polarized compact-test identity for tests supported in that same window.

This is deliberately weaker than an all-compact-test whole-line identity at
one frozen cutoff.  The globalization theorem below derives the latter using
the certified finite-prime-shell compression theorem.
-/
structure RightLimitWeilPolarizedSourceWindowPremise
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
        frozenWeilCompactAction carrier b (symbolAt b hab) u hu

/--
Window-local polarized source identities globalize to the exact frozen-cutoff
weak-realization premise.

The proof uses only compactness of the test support and the certified internal
compression equality between the base frozen action and any larger-window
frozen action.
-/
theorem rightLimitWeilWeakRealizationPremise_of_sourceWindows
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hBase : RightLimitWeilSymbolTemperatePremise residual.a)
    (hSource :
      RightLimitWeilPolarizedSourceWindowPremise carrier residual) :
    RightLimitWeilWeakRealizationPremise
      c carrier residual hBase (neutralWeilSourcePole carrier) := by
  refine ⟨(neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable, ?_⟩
  intro u hu
  obtain ⟨b, hab, huWindow⟩ :=
    compactSchwartz_support_in_symmetric_window u hu residual.a
  let hb := hSource.symbolAt b hab
  have hlocal :
      (∫ x : ℝ, u x * residual.q x ∂volume) =
        frozenWeilCompactAction carrier b hb u hu := by
    exact hSource.weakIdentityOnWindow b hab u hu huWindow
  have hcompress :
      frozenWeilCompactAction carrier residual.a hBase u hu =
        frozenWeilCompactAction carrier b hb u hu := by
    exact frozenWeilCompactAction_compression_eq
      carrier hab residual.strict.le hBase hb u hu huWindow
  exact hlocal.trans hcompress.symm

/--
The previously certified Hermitian Gaussian bridge can consume the weaker
source-window premise after globalization.  No new Gaussian identity is
assumed here.
-/
theorem rightLimitWeilGaussianHermitian_of_sourceWindows
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hBase : RightLimitWeilSymbolTemperatePremise residual.a)
    (hSource :
      RightLimitWeilPolarizedSourceWindowPremise carrier residual)
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
    rightLimitWeilWeakRealizationPremise_of_sourceWindows
      carrier residual hBase hSource
  exact
    rightLimitWeilGaussianHermitian_of_growth
      carrier residual hBase
      (neutralWeilSourcePole carrier)
      (neutralWeilSourcePole_growthData carrier)
      hEXT4 Ck hc hR hqLarge hpLarge

end

end WeilDefect
