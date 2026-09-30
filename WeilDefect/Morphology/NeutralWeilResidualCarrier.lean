import WeilDefect.Morphology.NeutralWeilMultiplier
import Mathlib.Analysis.Distribution.Distribution
import Mathlib.MeasureTheory.Function.LocallyIntegrable

namespace WeilDefect

noncomputable section

open MeasureTheory TopologicalSpace
open scoped Distributions SchwartzMap

/--
Corrected whole-line physical carrier for the full pole-restored Weil residual.

The full residual is represented as an actual locally integrable function with
a fixed exponential-growth bound.  This is deliberately broader than
`TemperedDistribution`: the pole/evaluation term may contain fixed real
exponentials.
-/
structure NeutralExponentialResidualCarrier (c : ℝ) where
  a : ℝ
  strict : c < a
  q : ℝ → ℂ
  q_locallyIntegrable : LocallyIntegrable q volume
  growthConstant : ℝ
  growthRate : ℝ
  growthConstant_nonneg : 0 ≤ growthConstant
  growthRate_nonneg : 0 ≤ growthRate
  growth_bound :
    ∀ x : ℝ,
      ‖q x‖ ≤ growthConstant * Real.exp (growthRate * |x|)
  vanishes_ae :
    ∀ᵐ x ∂volume,
      x ∈ Set.Ioo (-a) a → q x = 0

namespace NeutralExponentialResidualCarrier

variable {c : ℝ}

/--
The locally integrable physical residual defines an ordinary distribution on
the whole real line, tested only against compactly supported smooth functions.
-/
noncomputable def ordinaryDistribution
    (d : NeutralExponentialResidualCarrier c) :
    Distribution (⊤ : Opens ℝ) ℂ ⊤ :=
  Distribution.ofFun (Ω := (⊤ : Opens ℝ)) d.q volume ⊤

/--
Equivalent restricted-measure form of the strict central a.e. vanishing field.
-/
theorem vanishes_ae_on_strict_interval
    (d : NeutralExponentialResidualCarrier c) :
    d.q =ᵐ[volume.restrict (Set.Ioo (-d.a) d.a)] 0 := by
  rw [Filter.EventuallyEq, MeasureTheory.ae_restrict_iff' measurableSet_Ioo]
  exact d.vanishes_ae

end NeutralExponentialResidualCarrier

/--
Target weak-realization interface for the remaining F-2 operator bridge.

No constructor theorem is supplied here.  In a future F-2 pass, EXT-4 must
instantiate this structure with the actual scalar-multiplier core and the
explicit pole/evaluation term.

The weak identity is required only for compactly supported Schwartz tests,
which is the common test class on which the physical residual, the tempered
core, and the locally integrable pole function can all be compared without
assuming that the full residual is tempered.
-/
structure NeutralWeilResidualWeakRealization (c : ℝ) where
  residual : NeutralExponentialResidualCarrier c
  multiplierCore : RealComplexTempered
  pole : ℝ → ℂ
  pole_locallyIntegrable : LocallyIntegrable pole volume
  weakIdentity :
    ∀ u : SchwartzMap ℝ ℂ,
      HasCompactSupport u →
        (∫ x : ℝ, u x * residual.q x ∂volume)
          =
        multiplierCore u
          + ∫ x : ℝ, u x * pole x ∂volume


/--
Explicit imported EXT-4 premise tying the certified F-1 physical mode to the
actual strict-right compact-window Weil residual.

The identity is stated only on compactly supported Schwartz tests.  Its
multiplier term is the certified conditional tempered multiplier core at the
strict-right radius stored by the residual carrier.

This premise contains exactly the external compact-window operator
identification needed to finish F-2.  It does not contain any Gaussian
support-gap estimate or downstream WD-T40 conclusion.
-/
structure RightLimitWeilWeakRealizationPremise
    (c : ℝ)
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (pole : ℝ → ℂ) : Prop where
  pole_locallyIntegrable : LocallyIntegrable pole volume
  weakIdentity :
    ∀ u : SchwartzMap ℝ ℂ,
      HasCompactSupport u →
        (∫ x : ℝ, u x * residual.q x ∂volume)
          =
        rightLimitWeilMultiplierCore
            residual.a hSymbol carrier.temperedMode u
          + ∫ x : ℝ, u x * pole x ∂volume

/--
F-2 packaging theorem: an explicit EXT-4 weak-realization premise produces the
already certified weak-realization target for the actual strict-right mode.

No analytic estimate is proved here; the theorem only transfers the imported
operator identity into the project carrier.
-/
noncomputable def rightLimitWeilWeakRealization
    (c : ℝ)
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (pole : ℝ → ℂ)
    (hEXT4 :
      RightLimitWeilWeakRealizationPremise
        c carrier residual hSymbol pole) :
    NeutralWeilResidualWeakRealization c := by
  exact {
    residual := residual
    multiplierCore :=
      rightLimitWeilMultiplierCore
        residual.a hSymbol carrier.temperedMode
    pole := pole
    pole_locallyIntegrable := hEXT4.pole_locallyIntegrable
    weakIdentity := hEXT4.weakIdentity
  }

end

end WeilDefect
