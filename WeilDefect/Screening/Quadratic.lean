import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Tactic

namespace WeilDefect

open scoped InnerProduct

variable {𝕜 H K₊ K₋ B : Type*}
variable [RCLike 𝕜]
variable [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]
variable [NormedAddCommGroup K₊] [InnerProductSpace 𝕜 K₊] [CompleteSpace K₊]
variable [NormedAddCommGroup K₋] [InnerProductSpace 𝕜 K₋] [CompleteSpace K₋]
variable [NormedAddCommGroup B] [InnerProductSpace 𝕜 B] [CompleteSpace B]

/-- The coefficient-space indefinite signature used by the defect calculus. -/
def coeffSignature (a : K₊) (u : K₋) : ℝ :=
  ‖a‖ ^ 2 - ‖u‖ ^ 2

/-- Selected physical quadratic defect written through Hilbert adjoints. -/
def selectedQuadratic
    (S₊ : K₊ →L[𝕜] H)
    (S₋ : K₋ →L[𝕜] H)
    (h : H) : ℝ :=
  ‖(ContinuousLinearMap.adjoint S₊) h‖ ^ 2 -
    ‖(ContinuousLinearMap.adjoint S₋) h‖ ^ 2

/-- Algebraic core of WD-T01: analysis coefficients reproduce the physical defect value. -/
theorem wd_t01_quadratic_identity
    (S₊ : K₊ →L[𝕜] H)
    (S₋ : K₋ →L[𝕜] H)
    (h : H) :
    coeffSignature ((ContinuousLinearMap.adjoint S₊) h)
        ((ContinuousLinearMap.adjoint S₋) h)
      = selectedQuadratic S₊ S₋ h := by
  rfl

/-- Full quadratic defect after adding an unselected negative background channel. -/
def fullQuadratic
    (S₊ : K₊ →L[𝕜] H)
    (S₋ : K₋ →L[𝕜] H)
    (S_B : B →L[𝕜] H)
    (h : H) : ℝ :=
  selectedQuadratic S₊ S₋ h -
    ‖(ContinuousLinearMap.adjoint S_B) h‖ ^ 2

/-- WD-T07 identity: the unselected negative background subtracts a norm square. -/
theorem wd_t07_selected_full_identity
    (S₊ : K₊ →L[𝕜] H)
    (S₋ : K₋ →L[𝕜] H)
    (S_B : B →L[𝕜] H)
    (h : H) :
    fullQuadratic S₊ S₋ S_B h
      = selectedQuadratic S₊ S₋ h -
        ‖(ContinuousLinearMap.adjoint S_B) h‖ ^ 2 := by
  rfl

/-- WD-T07 sign custody: a selected negative witness stays negative after background aggregation. -/
theorem wd_t07_selected_negative_implies_full
    (S₊ : K₊ →L[𝕜] H)
    (S₋ : K₋ →L[𝕜] H)
    (S_B : B →L[𝕜] H)
    (h : H)
    (hneg : selectedQuadratic S₊ S₋ h < 0) :
    fullQuadratic S₊ S₋ S_B h < 0 := by
  unfold fullQuadratic
  have hsquare : 0 ≤ ‖(ContinuousLinearMap.adjoint S_B) h‖ ^ 2 := sq_nonneg _
  linarith

/--
WD-T14 algebraic signature-shadow inequality:
shrinking the positive-coordinate norm can only strengthen the negative margin.
-/
theorem wd_t14_signature_shadow
    (a qa : K₊)
    (u : K₋)
    (hqa : ‖qa‖ ≤ ‖a‖) :
    ‖u‖ ^ 2 - ‖a‖ ^ 2 ≤ ‖u‖ ^ 2 - ‖qa‖ ^ 2 := by
  have hsquare : ‖qa‖ ^ 2 ≤ ‖a‖ ^ 2 := by
    simpa [pow_two] using mul_self_le_mul_self (norm_nonneg qa) hqa
  linarith

end WeilDefect
