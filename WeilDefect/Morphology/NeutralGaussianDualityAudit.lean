import WeilDefect.Morphology.NeutralGaussianAssembly

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap

/-- Complex conjugation preserves Schwartz class because it is real-linear and isometric. -/
def conjugateSchwartz (f : SchwartzMap ℝ ℂ) : SchwartzMap ℝ ℂ :=
  f.postcompCLM Complex.conjCLE.toContinuousLinearMap

@[simp]
theorem conjugateSchwartz_apply (f : SchwartzMap ℝ ℂ) (x : ℝ) :
    conjugateSchwartz f x = Complex.conj (f x) := by
  rw [conjugateSchwartz, SchwartzMap.postcompCLM_apply]
  rfl

/--
The conjugated moving filtered mode is the test required by the Hermitian
energy pairing.  It is a Schwartz function with no additional regularity
assumption on the physical carrier.
-/
def movingGaussianFilteredModeDualTest
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    SchwartzMap ℝ ℂ :=
  conjugateSchwartz
    (movingGaussianFilteredModeSchwartz Ck R hR carrier)

@[simp]
theorem movingGaussianFilteredModeDualTest_apply
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (x : ℝ) :
    movingGaussianFilteredModeDualTest Ck R hR carrier x =
      Complex.conj (movingGaussianFilteredMode Ck R carrier x) := by
  simp [movingGaussianFilteredModeDualTest,
    movingGaussianFilteredModeSchwartz_apply]

/-- The compact carrier moment can be written as a whole-line integral. -/
theorem neutralWeilPoleMoment_eq_integral
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (s : ℝ) :
    neutralWeilPoleMoment carrier s =
      ∫ y : ℝ, carrier.h y * (Real.exp (s * y) : ℂ) := by
  unfold neutralWeilPoleMoment
  apply setIntegral_eq_integral_of_forall_compl_eq_zero
  intro y hy
  rw [carrier.representative_eq_zero_of_not_mem hy]
  simp

/-- The compact exponential moment is globally integrable after zero extension. -/
theorem neutralWeilPoleMoment_integrable_global
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (s : ℝ) :
    Integrable
      (fun y : ℝ =>
        carrier.h y * (Real.exp (s * y) : ℂ)) volume := by
  exact
    (neutralWeilPoleMoment_integrable carrier s).integrable_of_forall_notMem_eq_zero
      (fun y hy => by
        rw [carrier.representative_eq_zero_of_not_mem hy]
        simp)

/--
The named two-exponential pole reproduces the exact quadratic pole factor
from the source: twice the product of the two exponential moments.
-/
theorem neutralWeilSourcePole_pairing_eq
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    (∫ x : ℝ, carrier.h x * neutralWeilSourcePole carrier x ∂volume)
      =
    2 *
      neutralWeilPoleMoment carrier (-(1 / 2 : ℝ)) *
      neutralWeilPoleMoment carrier (1 / 2) := by
  let A : ℂ := neutralWeilPoleMoment carrier (-(1 / 2 : ℝ))
  let B : ℂ := neutralWeilPoleMoment carrier (1 / 2)
  have hplus :
      Integrable
        (fun x : ℝ => carrier.h x * (Real.exp ((1 / 2 : ℝ) * x) : ℂ))
        volume :=
    neutralWeilPoleMoment_integrable_global carrier (1 / 2)
  have hminus :
      Integrable
        (fun x : ℝ => carrier.h x * (Real.exp (-(1 / 2 : ℝ) * x) : ℂ))
        volume :=
    neutralWeilPoleMoment_integrable_global carrier (-(1 / 2))
  have hfun :
      (fun x : ℝ => carrier.h x * neutralWeilSourcePole carrier x)
        =
      (fun x : ℝ =>
        A * (carrier.h x * (Real.exp ((1 / 2 : ℝ) * x) : ℂ))
          +
        B * (carrier.h x * (Real.exp (-(1 / 2 : ℝ) * x) : ℂ))) := by
    funext x
    simp [neutralWeilSourcePole, neutralWeilExponentialPole, A, B]
    ring
  rw [hfun, integral_add (hplus.const_mul A) (hminus.const_mul B),
    integral_const_mul, integral_const_mul]
  rw [← neutralWeilPoleMoment_eq_integral carrier (1 / 2)]
  rw [← neutralWeilPoleMoment_eq_integral carrier (-(1 / 2))]
  simp [A, B]
  ring

/--
A bilinear complex pairing changes by the square of a global phase.
At phase i this flips sign.
-/
theorem complex_bilinear_phase_I (z w : ℂ) :
    (Complex.I * z) * (Complex.I * w) = -(z * w) := by
  ring_nf

/--
A Hermitian pairing is invariant under a common unit phase.
At phase i the conjugation cancels the square-phase sign.
-/
theorem complex_hermitian_phase_I (z w : ℂ) :
    Complex.conj (Complex.I * z) * (Complex.I * w)
      =
    Complex.conj z * w := by
  simp [Complex.conj_mul]
  ring

end

end WeilDefect
