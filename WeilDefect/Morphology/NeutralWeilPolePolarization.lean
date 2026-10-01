import WeilDefect.Morphology.NeutralWeilPoleGrowth

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped ComplexConjugate

/-- Whole-line exponential moment of a test function. -/
def neutralWeilTestMoment (u : ℝ → ℂ) (s : ℝ) : ℂ :=
  ∫ x : ℝ, u x * (Real.exp (s * x) : ℂ)

/-- Compactly supported Schwartz tests have both source pole moments. -/
theorem neutralWeilTestMoment_integrable_of_compact
    (u : SchwartzMap ℝ ℂ)
    (hu : HasCompactSupport u)
    (s : ℝ) :
    Integrable (fun x : ℝ => u x * (Real.exp (s * x) : ℂ)) volume := by
  apply Continuous.integrable_of_hasCompactSupport
  · exact u.continuous.mul (by fun_prop)
  · exact hu.mul_right

/-- Pairing with the explicit two-exponential pole is exactly the symmetric
cross-moment polarization. -/
theorem integral_mul_neutralWeilExponentialPole
    (u : ℝ → ℂ)
    (aPlus aMinus : ℂ)
    (hplus : Integrable (fun x : ℝ => u x * (Real.exp ((1 / 2 : ℝ) * x) : ℂ)) volume)
    (hminus : Integrable (fun x : ℝ => u x * (Real.exp ((-(1 / 2 : ℝ)) * x) : ℂ)) volume) :
    (∫ x : ℝ, u x * neutralWeilExponentialPole aPlus aMinus x ∂volume)
      =
    aPlus * neutralWeilTestMoment u (1 / 2)
      + aMinus * neutralWeilTestMoment u (-(1 / 2)) := by
  have hplus' :
      Integrable
        (fun x : ℝ =>
          aPlus * (u x * (Real.exp ((1 / 2 : ℝ) * x) : ℂ))) volume :=
    hplus.const_mul aPlus
  have hminus' :
      Integrable
        (fun x : ℝ =>
          aMinus * (u x * (Real.exp ((-(1 / 2 : ℝ)) * x) : ℂ))) volume :=
    hminus.const_mul aMinus
  calc
    (∫ x : ℝ, u x * neutralWeilExponentialPole aPlus aMinus x ∂volume)
        =
      ∫ x : ℝ,
        (aPlus * (u x * (Real.exp ((1 / 2 : ℝ) * x) : ℂ)))
          + (aMinus * (u x * (Real.exp ((-(1 / 2 : ℝ)) * x) : ℂ)))
        ∂volume := by
          apply integral_congr_ae
          filter_upwards with x
          unfold neutralWeilExponentialPole
          congr 1 <;> ring_nf
    _ =
      (∫ x : ℝ,
        aPlus * (u x * (Real.exp ((1 / 2 : ℝ) * x) : ℂ)) ∂volume)
        +
      (∫ x : ℝ,
        aMinus * (u x * (Real.exp ((-(1 / 2 : ℝ)) * x) : ℂ)) ∂volume) := by
          rw [integral_add hplus' hminus']
    _ =
      aPlus * neutralWeilTestMoment u (1 / 2)
        + aMinus * neutralWeilTestMoment u (-(1 / 2)) := by
          simp [neutralWeilTestMoment, integral_const_mul]

/-- The concrete source pole pairs with a compact test by the exact symmetric
polarization of the two source evaluation moments. -/
theorem neutralWeilSourcePole_pairing
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ)
    (hu : HasCompactSupport u) :
    (∫ x : ℝ, u x * neutralWeilSourcePole carrier x ∂volume)
      =
    neutralWeilPoleMoment carrier (-(1 / 2 : ℝ))
        * neutralWeilTestMoment u (1 / 2)
      +
    neutralWeilPoleMoment carrier (1 / 2)
        * neutralWeilTestMoment u (-(1 / 2)) := by
  unfold neutralWeilSourcePole
  exact integral_mul_neutralWeilExponentialPole
    u _ _
    (neutralWeilTestMoment_integrable_of_compact u hu (1 / 2))
    (neutralWeilTestMoment_integrable_of_compact u hu (-(1 / 2)))

/-- The compact carrier's set moment agrees with its whole-line moment because
the representative vanishes outside [-c,c]. -/
theorem neutralWeilPoleMoment_eq_testMoment
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (s : ℝ) :
    neutralWeilPoleMoment carrier s = neutralWeilTestMoment carrier.h s := by
  unfold neutralWeilPoleMoment neutralWeilTestMoment
  apply setIntegral_eq_integral_of_forall_compl_eq_zero
  intro x hx
  rw [carrier.representative_eq_zero_of_not_mem hx, zero_mul]

/-- On the carrier diagonal, the concrete source pole reproduces exactly the
rank-one source pole quadratic term 2 M_- M_+. -/
theorem neutralWeilSourcePole_self_pairing
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    (∫ x : ℝ, carrier.h x * neutralWeilSourcePole carrier x ∂volume)
      =
    2 * neutralWeilPoleMoment carrier (-(1 / 2 : ℝ))
      * neutralWeilPoleMoment carrier (1 / 2) := by
  have hplusOn :=
    neutralWeilPoleMoment_integrable carrier (1 / 2)
  have hminusOn :=
    neutralWeilPoleMoment_integrable carrier (-(1 / 2))
  have hplus :
      Integrable
        (fun x : ℝ => carrier.h x * (Real.exp ((1 / 2 : ℝ) * x) : ℂ))
        volume :=
    hplusOn.integrable_of_forall_notMem_eq_zero
      (fun x hx => by
        rw [carrier.representative_eq_zero_of_not_mem hx, zero_mul])
  have hminus :
      Integrable
        (fun x : ℝ => carrier.h x * (Real.exp ((-(1 / 2 : ℝ)) * x) : ℂ))
        volume :=
    hminusOn.integrable_of_forall_notMem_eq_zero
      (fun x hx => by
        rw [carrier.representative_eq_zero_of_not_mem hx, zero_mul])
  rw [neutralWeilSourcePole]
  rw [integral_mul_neutralWeilExponentialPole carrier.h _ _ hplus hminus]
  rw [← neutralWeilPoleMoment_eq_testMoment carrier (1 / 2),
    ← neutralWeilPoleMoment_eq_testMoment carrier (-(1 / 2))]
  ring

/-- Complex bilinear diagonal scaling is phase-sensitive: multiplication by I
reverses the sign of a square. -/
theorem complex_bilinear_phase_square (z : ℂ) :
    (Complex.I * z) * (Complex.I * z) = -(z * z) := by
  calc
    (Complex.I * z) * (Complex.I * z)
        = (Complex.I * Complex.I) * (z * z) := by ring
    _ = -(z * z) := by simp

/-- Hermitian magnitude is phase-insensitive under multiplication by I. -/
theorem complex_hermitian_phase_normSq (z : ℂ) :
    ‖Complex.I * z‖ ^ 2 = ‖z‖ ^ 2 := by
  rw [norm_mul]
  simp

end

end WeilDefect
