module

public import CP027TwoFiniteSigns

/-!
CP028 — COARSE, INDEPENDENTLY FALSIFIABLE FINITE A6,256 BOX
interface for the TRUE original Hardy-Z strict narrow root.

CP027PointwiseBorwein proposes the two actual original
critical-line pointwise Borwein bounds (new kernel PENDING).
CP026OriginalPointBridge and CP027TwoFiniteSigns supply the
source-faithful HardyZ -> zeta IVT with exactly two original
finite numerical sign premises (kernels PENDING).

This CP028 module proves, in ordinary exact ℝ inequalities,
that each complicated sign premise follows from TWO MUCH
LOOSER finite-source interval goals:
  ‖original A6,256(s_left/right)‖ <= 1/1000
  sourceFiniteZ(left) < -1/10^7
  sourceFiniteZ(right) > 1/10^7.

The published original Hardy theta-error is 12/t^4,
so at t>=150 and ‖A‖<=1/1000
  sourcePointError < 1/10^10,
with >1000x slack for each sign. No finite numerical value is
assumed as a new global axiom: all four simple goals are
EXPLICIT HYPOTHESES and await source-bound kernel interval
certificates. No use of an untrusted JSON/Python boolean.

SOURCE PROOF CANDIDATES only. This Lean file has NOT been
compiled and has NO new v4.35 kernel receipt. Even a standard
axiom audit of the conditional theorem would NOT pay the
four coarse finite arithmetic premise instances.
-/

@[expose] public section

namespace CP028CoarseFiniteBoxes

open CP026OriginalPointBridge

/-- The TWO common source numerical approximation targets form
a deliberately coarse finite complex box at a single exact height. -/
def FiniteLeftBox : Prop :=
  ‖sourceA tLeft‖ ≤ (1 : ℝ) / 1000 ∧
  sourceFiniteZ tLeft < -((1 : ℝ) / (10 : ℝ) ^ 7)

def FiniteRightBox : Prop :=
  ‖sourceA tRight‖ ≤ (1 : ℝ) / 1000 ∧
  ((1 : ℝ) / (10 : ℝ) ^ 7) < sourceFiniteZ tRight

/-- The original published theta error makes the source
finite pointwise Hardy-Z error strictly smaller than 10^-10,
once t≥150 and ‖A6,256‖≤10^-3. This is a PURE EXACT
RATIONAL COMPARISON; no numerically evaluated special
function appears in the proof. -/
theorem sourcePointError_lt_ten_billionth
    (t : ℝ) (ht : (150 : ℝ) ≤ t)
    (hA : ‖sourceA t‖ ≤ (1 : ℝ) / 1000) :
    sourcePointError t < (1 : ℝ) / (10 : ℝ) ^ 10 := by
  have hpow : (150 : ℝ) ^ 4 ≤ t ^ 4 :=
    pow_le_pow_left₀ (by norm_num) ht 4
  have hdiv : (12 : ℝ) / t ^ 4 ≤ (12 : ℝ) / 150 ^ 4 :=
    div_le_div_of_nonneg_left (by norm_num) (by norm_num) hpow
  have hproduct :
      (12 : ℝ) / t ^ 4 * ‖sourceA t‖
          ≤ (12 : ℝ) / 150 ^ 4 * ((1 : ℝ) / 1000) :=
    mul_le_mul hdiv hA (norm_nonneg _) (by norm_num)
  change (12 : ℝ) / t ^ 4 * ‖sourceA t‖
      + (3 : ℝ) / (10 : ℝ) ^ 13 < (1 : ℝ) / (10 : ℝ) ^ 10
  calc
    _ ≤ (12 : ℝ) / 150 ^ 4 * ((1 : ℝ) / 1000)
          + 3 / (10 : ℝ) ^ 13 := add_le_add_right hproduct _
    _ < (1 : ℝ) / (10 : ℝ) ^ 10 := by norm_num

theorem original_left_finite_sign_of_coarse_box
    (h : FiniteLeftBox) :
    sourceFiniteZ tLeft + sourcePointError tLeft < 0 := by
  obtain ⟨hA, hF⟩ := h
  have ht : (150 : ℝ) ≤ tLeft := by norm_num [tLeft]
  have he := sourcePointError_lt_ten_billionth tLeft ht hA
  linarith

theorem original_right_finite_sign_of_coarse_box
    (h : FiniteRightBox) :
    0 < sourceFiniteZ tRight - sourcePointError tRight := by
  obtain ⟨hA, hF⟩ := h
  have ht : (150 : ℝ) ≤ tRight := by norm_num [tRight]
  have he := sourcePointError_lt_ten_billionth tRight ht hA
  linarith

/-- For the ORIGINAL zeta/HardyZ definitions, the two whole
CP025 complicated finite analytic sign obligations can be paid
by TWO deliberately broad endpoint finite-complex boxes.
Neither box is kernel-paid here, and every imported local
CP026/27 source module also needs a genuine Lean kernel.
There is NO assertion about the ordinal #53 or RH. -/
theorem original_narrow_zero_of_two_coarse_boxes
    (hLeft : FiniteLeftBox)
    (hRight : FiniteRightBox) :
    ∃ t : ℝ, tLeft < t ∧ t < tRight ∧
      riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0 := by
  exact CP027TwoFiniteSigns.original_narrow_critical_line_zero_of_two_finite_signs
    (original_left_finite_sign_of_coarse_box hLeft)
    (original_right_finite_sign_of_coarse_box hRight)

end CP028CoarseFiniteBoxes

#print axioms CP028CoarseFiniteBoxes.sourcePointError_lt_ten_billionth
#print axioms CP028CoarseFiniteBoxes.original_left_finite_sign_of_coarse_box
#print axioms CP028CoarseFiniteBoxes.original_right_finite_sign_of_coarse_box
#print axioms CP028CoarseFiniteBoxes.original_narrow_zero_of_two_coarse_boxes
