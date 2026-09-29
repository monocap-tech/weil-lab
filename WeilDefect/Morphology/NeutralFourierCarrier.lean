import WeilDefect.Morphology.Neutral
import Mathlib.Analysis.Fourier.LpSpace
import Mathlib.Analysis.Distribution.Support

namespace WeilDefect

open MeasureTheory Distribution
open scoped FourierTransform Topology

/-- Concrete complex L2 carrier on the physical real line used by WD-T40. -/
abbrev RealComplexL2 := MeasureTheory.Lp (α := ℝ) ℂ 2 volume

/-- Concrete tempered-distribution carrier on the physical real line. -/
abbrev RealComplexTempered := TemperedDistribution ℝ ℂ

/--
F-1 / RPB-68 physical Fourier carrier lift.

This refines the abstract WD-T38 null-extension interface by attaching an
actual real-line representative in L2, compact support in [-c,c], and an exact
identification of the abstract physical vector with the representative's L2
class.

No definition of the actual Weil multiplier is included here; that is F-2.
-/
structure NeutralPhysicalFourierCarrier
    (c : ℝ)
    (EndpointObs RightObs : Type*)
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs] where
  h : ℝ → ℂ
  h_memLp : MemLp h 2 volume
  support_subset : Function.support h ⊆ Set.Icc (-c) c
  interface :
    NeutralNullExtensionInterface
      c RealComplexL2 EndpointObs RightObs
  kExt_eq_toLp :
    interface.kExt = h_memLp.toLp h

namespace NeutralPhysicalFourierCarrier

variable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The concrete L2 mode attached to the carrier representative. -/
noncomputable def l2Mode
    (d : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    RealComplexL2 :=
  d.h_memLp.toLp d.h

/-- Forget the concrete Fourier carrier and recover the original WD-T38 interface. -/
def toNeutralNullExtensionInterface
    (d : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    NeutralNullExtensionInterface c RealComplexL2 EndpointObs RightObs :=
  d.interface

@[simp]
theorem interface_kExt_eq_l2Mode
    (d : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    d.interface.kExt = d.l2Mode := by
  unfold l2Mode
  exact d.kExt_eq_toLp

/-- The physical L2 mode is nonzero because the attached WD-T38 mode is nonzero. -/
theorem l2Mode_ne_zero
    (d : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    d.l2Mode ≠ 0 := by
  intro hzero
  exact d.interface.kExt_ne ((interface_kExt_eq_l2Mode d).trans hzero)

/-- The chosen representative vanishes pointwise outside the certified support interval. -/
theorem representative_eq_zero_of_not_mem
    (d : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {x : ℝ} (hx : x ∉ Set.Icc (-c) c) :
    d.h x = 0 := by
  by_contra hne
  exact hx (d.support_subset hne)

/-- The concrete L2 mode viewed as a tempered distribution. -/
noncomputable def temperedMode
    (d : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    RealComplexTempered :=
  (d.l2Mode : RealComplexTempered)

/--
The mathlib L2 Fourier transform agrees with the tempered-distribution Fourier
transform for the lifted physical mode.
-/
theorem fourier_temperedMode_eq
    (d : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    𝓕 d.temperedMode =
      ((𝓕 d.l2Mode : RealComplexL2) : RealComplexTempered) := by
  change
    𝓕 (d.l2Mode : RealComplexTempered) =
      ((𝓕 d.l2Mode : RealComplexL2) : RealComplexTempered)
  exact MeasureTheory.Lp.fourier_toTemperedDistribution_eq d.l2Mode

end NeutralPhysicalFourierCarrier

/--
Typed strict-enlargement residual data for the physical Fourier carrier.

The residual is deliberately not yet identified with the actual Weil
multiplier applied to the mode; that equality belongs to F-2.  What is fixed
here is the strict support radius and the semantic distributional statement
that the residual vanishes on the enlarged interval.
-/
structure NeutralStrictResidualData (c : ℝ) where
  a : ℝ
  strict : c < a
  residual : RealComplexTempered
  residual_vanishes :
    Distribution.IsVanishingOn residual (Set.Ioo (-a) a)

namespace NeutralStrictResidualData

variable {c : ℝ}

/-- A strict residual vanishing on (-a,a) also vanishes on the old open support interval. -/
theorem vanishes_on_old_interval
    (d : NeutralStrictResidualData c) :
    Distribution.IsVanishingOn d.residual (Set.Ioo (-c) c) := by
  exact Distribution.IsVanishingOn.mono
    (s₁ := Set.Ioo (-d.a) d.a)
    (s₂ := Set.Ioo (-c) c)
    (fun _ hx =>
      ⟨lt_trans (neg_lt_neg d.strict) hx.1, lt_trans hx.2 d.strict⟩)
    d.residual_vanishes

end NeutralStrictResidualData

end WeilDefect
