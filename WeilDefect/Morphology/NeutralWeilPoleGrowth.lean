import WeilDefect.Morphology.NeutralGaussianAdmissibility

namespace WeilDefect

noncomputable section

open MeasureTheory

/-- The two fixed real exponentials in the source's pole sector.
The coefficients are explicit; no claim about an arbitrary EXT-4 pole is implicit. -/
def neutralWeilExponentialPole (aPlus aMinus : ℂ) (x : ℝ) : ℂ :=
  aPlus * (Real.exp (x / 2) : ℂ) +
    aMinus * (Real.exp (-x / 2) : ℂ)

theorem neutralWeilExponentialPole_continuous (aPlus aMinus : ℂ) :
    Continuous (neutralWeilExponentialPole aPlus aMinus) := by
  unfold neutralWeilExponentialPole
  fun_prop

/-- The source pole has fixed growth rate one half. -/
theorem neutralWeilExponentialPole_norm_le (aPlus aMinus : ℂ) (x : ℝ) :
    ‖neutralWeilExponentialPole aPlus aMinus x‖ ≤
      (‖aPlus‖ + ‖aMinus‖) * Real.exp ((1 / 2 : ℝ) * |x|) := by
  have hp : Real.exp (x / 2) ≤ Real.exp ((1 / 2 : ℝ) * |x|) := by
    apply Real.exp_le_exp.mpr
    nlinarith [le_abs_self x]
  have hm : Real.exp (-x / 2) ≤ Real.exp ((1 / 2 : ℝ) * |x|) := by
    apply Real.exp_le_exp.mpr
    nlinarith [neg_le_abs x]
  calc
    ‖neutralWeilExponentialPole aPlus aMinus x‖ ≤
        ‖aPlus * (Real.exp (x / 2) : ℂ)‖ +
          ‖aMinus * (Real.exp (-x / 2) : ℂ)‖ := norm_add_le _ _
    _ = ‖aPlus‖ * Real.exp (x / 2) + ‖aMinus‖ * Real.exp (-x / 2) := by
      simp [norm_mul, Complex.norm_real, Real.norm_eq_abs, Real.exp_pos]
    _ ≤ ‖aPlus‖ * Real.exp ((1 / 2 : ℝ) * |x|) +
          ‖aMinus‖ * Real.exp ((1 / 2 : ℝ) * |x|) :=
      add_le_add (mul_le_mul_of_nonneg_left hp (norm_nonneg _))
        (mul_le_mul_of_nonneg_left hm (norm_nonneg _))
    _ = _ := by ring

def neutralWeilExponentialPole_growthData (aPlus aMinus : ℂ) :
    NeutralPoleExponentialGrowthData (neutralWeilExponentialPole aPlus aMinus) where
  pole_locallyIntegrable := (neutralWeilExponentialPole_continuous aPlus aMinus).locallyIntegrable
  growthConstant := ‖aPlus‖ + ‖aMinus‖
  growthRate := 1 / 2
  growthConstant_nonneg := add_nonneg (norm_nonneg _) (norm_nonneg _)
  growthRate_nonneg := by norm_num
  growth_bound := neutralWeilExponentialPole_norm_le aPlus aMinus

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Compact carrier moment against a real exponential. -/
def neutralWeilPoleMoment
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (s : ℝ) : ℂ :=
  ∫ y in Set.Icc (-c) c, carrier.h y * (Real.exp (s * y) : ℂ)

theorem neutralWeilPoleMoment_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (s : ℝ) :
    IntegrableOn (fun y : ℝ => carrier.h y * (Real.exp (s * y) : ℂ))
      (Set.Icc (-c) c) volume := by
  exact (neutralPhysicalRepresentative_integrableOn carrier).mul_continuousOn
    (by fun_prop) isCompact_Icc

/-- Concrete source pole operator: the minus moment multiplies exp(x/2),
and the plus moment multiplies exp(-x/2). Its attachment to the imported
weak realization must be supplied explicitly. -/
def neutralWeilSourcePole
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) : ℝ → ℂ :=
  neutralWeilExponentialPole
    (neutralWeilPoleMoment carrier (-(1 / 2 : ℝ)))
    (neutralWeilPoleMoment carrier (1 / 2))

def neutralWeilSourcePole_growthData
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    NeutralPoleExponentialGrowthData (neutralWeilSourcePole carrier) :=
  neutralWeilExponentialPole_growthData _ _

/-- Explicit equality transports the concrete pole growth bound. This theorem
never infers a finite-exponential decomposition from local integrability. -/
def neutralWeilPoleGrowth_of_source_eq
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (pole : ℝ → ℂ) (hpole : pole = neutralWeilSourcePole carrier) :
    NeutralPoleExponentialGrowthData pole := by
  subst pole
  exact neutralWeilSourcePole_growthData carrier

end

end WeilDefect
