import WeilDefect.Morphology.NeutralArchimedeanExterior

namespace WeilDefect

noncomputable section

open MeasureTheory

/-- Any rate strictly above the named pole's half-rate gives genuine weighted
norm mass. No source attachment is used for this analytic fact. -/
theorem neutralPole_weightedNorm_integrable
    (pole : ℝ → ℂ) (hp : NeutralPoleExponentialGrowthData pole)
    {κ : ℝ} (hκ : hp.growthRate < κ) :
    Integrable (fun x => ‖pole x‖ * Real.exp (-κ * |x|)) volume := by
  apply ((integrable_exp_neg_rate_abs (sub_pos.mpr hκ)).const_mul
    hp.growthConstant).mono'
  · exact hp.pole_locallyIntegrable.aestronglyMeasurable.norm.mul
      (by fun_prop : Continuous (fun x : ℝ => Real.exp (-κ * |x|))).aestronglyMeasurable
  · filter_upwards [] with x
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    calc
      _ ≤ (hp.growthConstant * Real.exp (hp.growthRate * |x|)) *
          Real.exp (-κ * |x|) := mul_le_mul_of_nonneg_right
            (hp.growth_bound x) (Real.exp_nonneg _)
      _ = _ := by
        rw [mul_assoc, ← Real.exp_add]
        congr 2
        ring

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Actual exterior ingredients with the right-limit prime cutoff and source
pole. The archimedean continuation at small displacements is auxiliary. -/
def neutralExteriorResidualIngredients
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (x : ℝ) : ℂ :=
  neutralArchimedeanGapFunction carrier (a-c) x -
    neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x +
      neutralWeilSourcePole carrier x

theorem neutralExteriorResidualIngredients_locallyIntegrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) :
    LocallyIntegrable (neutralExteriorResidualIngredients carrier a) volume :=
  ((neutralArchimedeanGapFunction_continuous carrier
    (sub_pos.mpr hca)).locallyIntegrable.sub
    (neutralFinitePrimePhysical_locallyIntegrable carrier _)).add
      (neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable

theorem neutralExteriorResidualIngredients_weightedNorm_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a κ : ℝ} (hca : c < a) (hκ : (1/2 : ℝ) < κ) :
    Integrable (fun x => ‖neutralExteriorResidualIngredients carrier a x‖ *
      Real.exp (-κ * |x|)) volume := by
  have ha := neutralArchimedeanGapFunction_weightedNorm_integrable carrier
    (sub_pos.mpr hca) (show 0 < κ by linarith)
  have hf := neutralFinitePrimePhysical_weightedNorm_integrable_all carrier
    (rightLimitPrimePowerFinset a) (-κ)
  have hp := neutralPole_weightedNorm_integrable _
    (neutralWeilSourcePole_growthData carrier) hκ
  apply ((ha.add hf).add hp).mono'
  · exact (neutralExteriorResidualIngredients_locallyIntegrable carrier hca).aestronglyMeasurable.norm.mul
      (by fun_prop : Continuous (fun x : ℝ => Real.exp (-κ * |x|))).aestronglyMeasurable
  · filter_upwards [] with x
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    have hn : ‖neutralExteriorResidualIngredients carrier a x‖ ≤
        ‖neutralArchimedeanGapFunction carrier (a-c) x‖ +
        ‖neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x‖ +
        ‖neutralWeilSourcePole carrier x‖ :=
      (norm_add_le _ _).trans (add_le_add (norm_sub_le _ _) le_rfl)
    simpa only [add_mul] using mul_le_mul_of_nonneg_right hn (Real.exp_nonneg (-κ * |x|))

/-- Zero continuation of the actual exterior ingredients. Source cancellation
and representation of the multiplier distribution are not asserted. -/
def neutralExteriorResidualCandidate
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) : ℝ → ℂ :=
  (Set.Ioo (-a) a)ᶜ.indicator (neutralExteriorResidualIngredients carrier a)

theorem neutralExteriorResidualCandidate_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a x : ℝ} (hx : x ∈ Set.Ioo (-a) a) :
    neutralExteriorResidualCandidate carrier a x = 0 := by
  simp [neutralExteriorResidualCandidate, hx]

theorem neutralExteriorResidualCandidate_eq_exterior
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a x : ℝ} (hx : x ∉ Set.Ioo (-a) a) :
    neutralExteriorResidualCandidate carrier a x =
      neutralExteriorResidualIngredients carrier a x := by
  simp [neutralExteriorResidualCandidate, hx]

theorem neutralExteriorResidualCandidate_locallyIntegrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) :
    LocallyIntegrable (neutralExteriorResidualCandidate carrier a) volume :=
  (neutralExteriorResidualIngredients_locallyIntegrable carrier hca).indicator
    measurableSet_Ioo.compl

theorem neutralExteriorResidualCandidate_weightedNorm_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a κ : ℝ} (hca : c < a) (hκ : (1/2 : ℝ) < κ) :
    Integrable (fun x => ‖neutralExteriorResidualCandidate carrier a x‖ *
      Real.exp (-κ * |x|)) volume := by
  apply (neutralExteriorResidualIngredients_weightedNorm_integrable carrier hca hκ).mono'
  · exact (neutralExteriorResidualCandidate_locallyIntegrable carrier hca).aestronglyMeasurable.norm.mul
      (by fun_prop : Continuous (fun x : ℝ => Real.exp (-κ * |x|))).aestronglyMeasurable
  · filter_upwards [] with x
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    by_cases hx : x ∈ Set.Ioo (-a) a
    · rw [neutralExteriorResidualCandidate_zero carrier hx, norm_zero, zero_mul]
      positivity
    · rw [neutralExteriorResidualCandidate_eq_exterior carrier hx]

/-- The concrete candidate supplies every analytic residual field at rate one.
The compact weak source realization remains a separate Prop. -/
def neutralExteriorIntegralGrowthResidual
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) : NeutralIntegralGrowthResidual c where
  a := a
  strict := hca
  q := neutralExteriorResidualCandidate carrier a
  locallyIntegrable := neutralExteriorResidualCandidate_locallyIntegrable carrier hca
  rate := 1
  rate_nonneg := by norm_num
  weightedIntegrable := neutralExteriorResidualCandidate_weightedNorm_integrable
    carrier hca (by norm_num)
  vanishes_ae := Filter.Eventually.of_forall fun _ hx =>
    neutralExteriorResidualCandidate_zero carrier hx

end

end WeilDefect
