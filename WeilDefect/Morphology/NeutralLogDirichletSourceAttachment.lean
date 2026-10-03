import WeilDefect.Morphology.NeutralLogSelectedSourceAttachment
import WeilDefect.DirichletResolvent

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap InnerProductSpace
open scoped InnerProduct ComplexConjugate

/-- The full native Green column, including both endpoint corrections. -/
def neutralDirichletGreenColumn (a : ℝ) (z : ℂ) (x : ℝ) : ℂ :=
  (Set.Icc (-a) a).indicator (dirichletProblemOneColumn a z) x

theorem neutralDirichletGreenColumn_memLp (a : ℝ) (z : ℂ) :
    MemLp (neutralDirichletGreenColumn a z) 2 volume := by
  have hc : Continuous (dirichletProblemOneColumn a z) := by
    unfold dirichletProblemOneColumn dirichletRightBasis dirichletLeftBasis
      dirichletRightReal dirichletLeftReal realExpMode
    fun_prop
  have hm : AEStronglyMeasurable (neutralDirichletGreenColumn a z) volume :=
    hc.aestronglyMeasurable.indicator measurableSet_Icc
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hi : IntegrableOn (fun x : ℝ => ‖dirichletProblemOneColumn a z x‖ ^ 2)
      (Set.Icc (-a) a) volume := (hc.norm.pow 2).integrableOn_Icc
  apply (hi.integrable_indicator measurableSet_Icc).congr
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;> simp [neutralDirichletGreenColumn, hx]

def neutralDirichletGreenColumnL2 (a : ℝ) (z : ℂ) : RealComplexL2 :=
  (neutralDirichletGreenColumn_memLp a z).toLp (neutralDirichletGreenColumn a z)

theorem neutralDirichletGreenColumnL2_inner (a : ℝ) (z : ℂ)
    (f : RealComplexL2) :
    inner ℂ (neutralDirichletGreenColumnL2 a z) f =
      ∫ x in Set.Icc (-a) a, conj (dirichletProblemOneColumn a z x) * f x := by
  rw [L2.inner_def, ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [(neutralDirichletGreenColumn_memLp a z).coeFn_toLp] with x hx
  change inner ℂ ((neutralDirichletGreenColumn_memLp a z).toLp
    (neutralDirichletGreenColumn a z) x) (f x) = _
  rw [hx]
  by_cases hmem : x ∈ Set.Icc (-a) a
  · simp [neutralDirichletGreenColumn, hmem, RCLike.inner_apply']
  · simp [neutralDirichletGreenColumn, hmem, RCLike.inner_apply']

/-- Form Riesz representative of the actual Green-column functional.
This is not an assumed square-root Green operator. -/
def neutralLogDirichletGreenSource (a : ℝ) (z : ℂ) : NeutralLogHilbertCarrier a :=
  ((neutralLogPhysicalInclusion a)†) (neutralDirichletGreenColumnL2 a z)

theorem neutralLogDirichletGreenSource_inner (a : ℝ) (z : ℂ)
    (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralLogDirichletGreenSource a z) f =
      ∫ x in Set.Icc (-a) a, conj (dirichletProblemOneColumn a z x) *
        neutralLogPhysical f.val x := by
  rw [neutralLogDirichletGreenSource, adjoint_inner_left,
    neutralDirichletGreenColumnL2_inner]
  rfl

/-- Applying the actual differential expression to the full Green column
recovers the raw source. No spectral-domain membership of a test is used. -/
theorem neutralDirichletGreen_differentialSource (a : ℝ) (z : ℂ)
    (hden : problemOneGreenDenom z ≠ 0) :
    (Set.Icc (-a) a).indicator
      (fun x => problemOneL (dirichletProblemOneColumn a z) x) =
        neutralExponentialColumn a z := by
  funext x
  by_cases hx : x ∈ Set.Icc (-a) a
  · simp only [Set.indicator_of_mem hx, neutralExponentialColumn,
      problemOneL_dirichletProblemOneColumn a x z hden]
    simp [realExpMode, problemOneFreq]
  · simp [neutralExponentialColumn, hx]

/-- The native differential source is genuinely L2 because it is the
compact raw exponential column, not because the physical carrier lies
in the Weil operator domain. -/
theorem neutralDirichletGreen_differentialSource_memLp (a : ℝ) (z : ℂ)
    (hden : problemOneGreenDenom z ≠ 0) :
    MemLp ((Set.Icc (-a) a).indicator
      (fun x => problemOneL (dirichletProblemOneColumn a z) x)) 2 volume := by
  rw [neutralDirichletGreen_differentialSource a z hden]
  exact neutralExponentialColumn_memLp a z

/-- Exact same-domain attachment to the retained raw source analysis. -/
theorem neutralLogDirichletGreen_differentialSource_inner (a : ℝ) (z : ℂ)
    (hden : problemOneGreenDenom z ≠ 0) (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralLogExponentialSource a z) f =
      ∫ x in Set.Icc (-a) a,
        conj (problemOneL (dirichletProblemOneColumn a z) x) *
          neutralLogPhysical f.val x := by
  rw [neutralLogExponentialSource_inner]
  unfold neutralWindowEvaluation
  apply integral_congr_ae
  filter_upwards [] with x
  rw [problemOneL_dirichletProblemOneColumn a x z hden]
  simp only [realExpMode, problemOneFreq, ← Complex.exp_conj, map_mul, map_neg,
    Complex.conj_I, Complex.conj_ofReal, neg_neg]
  ring

end

end WeilDefect
