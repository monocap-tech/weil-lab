import WeilDefect.Morphology.NeutralLogMetricPhysicalSource

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped Topology

/-- RC24's metric jump density. Analytic use is restricted to r > 0;
convergence of this improper integral is a separate obligation. -/
def neutralLogMetricJumpDensity (r : ℝ) : ℝ :=
  2 * ∫ t in Set.Ioi (0 : ℝ),
    Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)

/-- Exterior tail at positive distance from one endpoint. -/
def neutralLogMetricEndpointTail (d : ℝ) : ℝ :=
  ∫ r in Set.Ioi d, neutralLogMetricJumpDensity r

/-- Both tails of the zero-extended finite interval are retained. -/
def neutralLogMetricExteriorSource (B x : ℝ) : ℝ :=
  neutralLogMetricEndpointTail (B - x) + neutralLogMetricEndpointTail (B + x)

/-- RC24's physical source candidate. Identifying this function with a
physical L2 source requires integrability, endpoint bounds and weak attachment. -/
def neutralLogMetricEndpointCandidate (B : ℝ) (v : ℝ → ℂ) (x : ℝ) : ℂ :=
  v x + (∫ y in Set.Icc (-B) B,
    (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)) +
    v x * (neutralLogMetricExteriorSource B x : ℂ)

theorem neutralLogMetricJumpDensity_nonnegative (r : ℝ) :
    0 ≤ neutralLogMetricJumpDensity r := by
  unfold neutralLogMetricJumpDensity
  apply mul_nonneg (by norm_num)
  apply integral_nonneg
  intro t
  exact div_nonneg (le_of_lt (Real.exp_pos _))
    (add_nonneg (sq_nonneg t)
      (mul_nonneg (mul_nonneg (by norm_num) (sq_nonneg Real.pi)) (sq_nonneg r)))

theorem neutralLogMetricEndpointTail_nonnegative (d : ℝ) :
    0 ≤ neutralLogMetricEndpointTail d :=
  integral_nonneg neutralLogMetricJumpDensity_nonnegative

theorem neutralLogMetricExteriorSource_nonnegative (B x : ℝ) :
    0 ≤ neutralLogMetricExteriorSource B x :=
  add_nonneg (neutralLogMetricEndpointTail_nonnegative _)
    (neutralLogMetricEndpointTail_nonnegative _)

/-- Reflection exchanges the two endpoint contributions. -/
theorem neutralLogMetricExteriorSource_reflection (B x : ℝ) :
    neutralLogMetricExteriorSource B (-x) = neutralLogMetricExteriorSource B x := by
  simp only [neutralLogMetricExteriorSource, sub_neg_eq_add, ← sub_eq_add_neg]
  exact add_comm _ _

/-- The constant trial retains both exterior terms; compression does not
remove them. This identity alone does not establish endpoint divergence. -/
theorem neutralLogMetricEndpointCandidate_constant (B x : ℝ) (z : ℂ) :
    neutralLogMetricEndpointCandidate B (fun _ => z) x =
      z * (1 + (neutralLogMetricExteriorSource B x : ℂ)) := by
  simp only [neutralLogMetricEndpointCandidate, sub_self, zero_mul,
    integral_zero, add_zero]
  ring

/-- Passing whole weak identities through a physical L2 limit does not
require upgrading arbitrary canonical vectors to the spectral operator domain. -/
theorem neutralLogMetric_weak_of_physical_limit
    {D H : Type*} [NormedAddCommGroup D] [InnerProductSpace ℂ D]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (i : D → H) (v : D) (source : H) (sources : ℕ → H)
    (forms : ℕ → D → ℂ)
    (hsources : Tendsto sources atTop (𝓝 source))
    (hattach : ∀ n h, forms n h = inner ℂ (sources n) (i h))
    (hforms : ∀ h, Tendsto (fun n => forms n h) atTop (𝓝 (inner ℂ v h))) :
    ∀ h, inner ℂ v h = inner ℂ source (i h) := by
  intro h
  have hc : Continuous (fun f : H => inner ℂ f (i h)) :=
    continuous_id.inner (𝕜 := ℂ) continuous_const
  have ht : Tendsto (fun n => inner ℂ (sources n) (i h)) atTop
      (𝓝 (inner ℂ source (i h))) := (hc.tendsto source).comp hsources
  have hlimit : Tendsto (fun n => forms n h) atTop
      (𝓝 (inner ℂ source (i h))) := by
    simpa only [hattach] using ht
  exact tendsto_nhds_unique (hforms h) hlimit

end
end WeilDefect
