import WeilDefect.Arithmetic.ActualZetaGreenClosedSubspace
import Mathlib.Analysis.Normed.Operator.Banach

namespace WeilDefect
noncomputable section
open ContinuousLinearMap InnerProductSpace
open scoped InnerProduct ComplexConjugate ENNReal
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false
local instance : DecidableEq NeutralActualZetaDivisorCoordinate := Classical.decEq _

/-- Fixed physical test samples at every actual multiplicity copy. The
certified square summability makes this an actual coefficient vector. -/
def neutralActualZetaGreenPhysicalSamples (a : ℝ) (ha : 0 < a)
    (f : RealComplexL2) : NeutralActualZetaGreenCoefficients :=
  ⟨fun q => inner ℂ (neutralActualZetaGreenColumn a q) f,
    memℓp_gen (by simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
      neutralActualZetaGreenSample_sq_summable a ha f)⟩

theorem neutralActualZetaGreenSynthesis_sample_duality (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) (f : RealComplexL2) :
    inner ℂ f (neutralActualZetaGreenSynthesis a v) =
      inner ℂ (neutralActualZetaGreenPhysicalSamples a ha f) v := by
  rw [neutralActualZetaGreenSynthesis_inner a ha v f, lp.inner_eq_tsum]
  apply tsum_congr
  intro q
  change v q * inner ℂ f (neutralActualZetaGreenColumn a q) =
    inner ℂ (inner ℂ (neutralActualZetaGreenColumn a q) f) (v q)
  simp only [RCLike.inner_apply', inner_conj_symm, mul_comm]

/-- Same physical Green synthesis, with its already proved linearity. -/
def neutralActualZetaGreenPhysicalLinear (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenCoefficients →ₗ[ℂ] RealComplexL2 where
  toFun := neutralActualZetaGreenSynthesis a
  map_add' := neutralActualZetaGreenSynthesis_add a ha
  map_smul' := neutralActualZetaGreenSynthesis_smul a ha

/-- All fixed-test sample equations characterize the physical graph. Each
equation is closed even before continuity of synthesis has been established. -/
theorem neutralActualZetaGreenPhysicalLinear_graph_closed (a : ℝ) (ha : 0 < a) :
    IsClosed ((neutralActualZetaGreenPhysicalLinear a ha).graph :
      Set (NeutralActualZetaGreenCoefficients × RealComplexL2)) := by
  have he : ((neutralActualZetaGreenPhysicalLinear a ha).graph :
      Set (NeutralActualZetaGreenCoefficients × RealComplexL2)) =
      {x | ∀ f : RealComplexL2, inner ℂ f x.2 =
        inner ℂ (neutralActualZetaGreenPhysicalSamples a ha f) x.1} := by
    ext x
    change (x.2 = neutralActualZetaGreenSynthesis a x.1) ↔ _
    constructor
    · intro h f
      rw [h]
      exact neutralActualZetaGreenSynthesis_sample_duality a ha x.1 f
    · intro h
      apply ext_inner_left ℂ
      intro f
      exact (h f).trans (neutralActualZetaGreenSynthesis_sample_duality a ha x.1 f).symm
  rw [he]
  simp only [Set.ofPred_forall]
  apply isClosed_iInter
  intro f
  have hl : Continuous (fun x : NeutralActualZetaGreenCoefficients × RealComplexL2 =>
      inner ℂ f x.2) := continuous_const.inner (𝕜 := ℂ) continuous_snd
  have hr : Continuous (fun x : NeutralActualZetaGreenCoefficients × RealComplexL2 =>
      inner ℂ (neutralActualZetaGreenPhysicalSamples a ha f) x.1) :=
    continuous_const.inner (𝕜 := ℂ) continuous_fst
  exact isClosed_eq hl hr

/-- Bounded physical synthesis follows from the proved closed graph between
the actual complete coefficient and physical spaces. -/
def neutralActualZetaGreenPhysicalContinuous (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenCoefficients →L[ℂ] RealComplexL2 :=
  ContinuousLinearMap.ofIsClosedGraph (neutralActualZetaGreenPhysicalLinear_graph_closed a ha)

/-- Ordinary physical L2 coordinate of the Hilbert source graph. -/
def neutralActualZetaHilbertSourceL2 (a : ℝ) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] RealComplexL2 :=
  neutralLogPhysical.comp
    (((neutralLogHilbertSubmodule a).toSubmodule.subtypeL).comp
      (neutralActualZetaHilbertSourcePhysical a))

theorem neutralActualZetaHilbertSourceL2_injective (a : ℝ) :
    Function.Injective (neutralActualZetaHilbertSourceL2 a) := by
  intro f g h
  apply neutralActualZetaHilbertSourcePhysical_injective a
  apply (neutralLogHilbertCanonicalLinearEquiv a).injective
  apply Subtype.ext
  exact h

theorem neutralActualZetaGreenHilbertSourceL2 (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaHilbertSourceL2 a (neutralActualZetaGreenHilbertSourceLift a ha v) =
      neutralActualZetaGreenSynthesis a v := by
  change neutralLogPhysical
    (neutralActualZetaHilbertSourcePhysical a
      (neutralActualZetaGreenHilbertSourceLift a ha v)).val = _
  rw [neutralActualZetaGreenHilbertSourcePhysical, neutralActualZetaGreenCanonical_physical]

/-- Source physical uniqueness identifies this graph with a closed equality
set of two continuous physical maps. Both source coordinates are retained. -/
theorem neutralActualZetaGreenHilbertSourceLinear_graph_closed (a : ℝ) (ha : 0 < a) :
    IsClosed ((neutralActualZetaGreenHilbertSourceLinear a ha).graph :
      Set (NeutralActualZetaGreenCoefficients × NeutralActualZetaHilbertSourceDomain a)) := by
  have he : ((neutralActualZetaGreenHilbertSourceLinear a ha).graph :
      Set (NeutralActualZetaGreenCoefficients × NeutralActualZetaHilbertSourceDomain a)) =
      {x | neutralActualZetaHilbertSourceL2 a x.2 =
        neutralActualZetaGreenPhysicalContinuous a ha x.1} := by
    ext x
    change (x.2 = neutralActualZetaGreenHilbertSourceLift a ha x.1) ↔
      (neutralActualZetaHilbertSourceL2 a x.2 =
        neutralActualZetaGreenPhysicalContinuous a ha x.1)
    constructor
    · intro h
      rw [h]
      exact neutralActualZetaGreenHilbertSourceL2 a ha x.1
    · intro h
      apply neutralActualZetaHilbertSourceL2_injective a
      exact h.trans (neutralActualZetaGreenHilbertSourceL2 a ha x.1).symm
  rw [he]
  exact isClosed_eq
    ((neutralActualZetaHilbertSourceL2 a).continuous.comp continuous_snd)
    ((neutralActualZetaGreenPhysicalContinuous a ha).continuous.comp continuous_fst)

/-- The unchanged full-divisor Green lift is bounded into the full source
graph norm, proved by closed graph rather than stipulated as a premise. -/
def neutralActualZetaGreenHilbertSourceContinuous (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenCoefficients →L[ℂ] NeutralActualZetaHilbertSourceDomain a :=
  ContinuousLinearMap.ofIsClosedGraph
    (neutralActualZetaGreenHilbertSourceLinear_graph_closed a ha)

theorem neutralActualZetaGreenHilbertSource_norm_le (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    ‖neutralActualZetaGreenHilbertSourceLift a ha v‖ ≤
      ‖neutralActualZetaGreenHilbertSourceContinuous a ha‖ * ‖v‖ :=
  (neutralActualZetaGreenHilbertSourceContinuous a ha).le_opNorm v

/-- Finite actual-coordinate packets converge to every Green lift in the
full graph topology. This controls both source vectors and the physical
logarithmic coordinate, not just physical L2 convergence. -/
theorem neutralActualZetaGreenHilbertSource_hasSum_packets (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    HasSum (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralActualZetaGreenHilbertSourceLift a ha (lp.single 2 q (v q)))
      (neutralActualZetaGreenHilbertSourceLift a ha v) :=
  (lp.hasSum_single ENNReal.ofNat_ne_top v).mapL
    (neutralActualZetaGreenHilbertSourceContinuous a ha)

end
end WeilDefect
