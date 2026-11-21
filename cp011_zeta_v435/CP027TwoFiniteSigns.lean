module

public import CP026OriginalPointBridge
public import CP027PointwiseBorwein

/-!
CP027 ORIGINAL NARROW ROOT EXISTENCE PAYMENT REDUCTION.

Mathematically and on the original published source definitions,
CP027PointwiseBorwein establishes BOTH source center Borwein bounds
using genuine Zeta/Mathlib only. CP026OriginalPointBridge has an
EXPLICIT four-premise original true HardyZ -> zeta root transport.

This small integration theorem discharges precisely the two
original-point Borwein hypotheses, leaving EXACTLY TWO original
finite-Euler-Maclaurin rational sign proofs unpaid.  It does NOT
assert those two numerical facts; it does NOT assert unconditionally
that the critical-line zero exists and does not identify rank #53.

This local imported bridge will require actual original Lean v4.35
kernels for BOTH its predecessors plus its OWN .olean/axiom receipt.
The separate CP027PointwiseBorwein source leaf imports ONLY
published original Zeta/Mathlib and is independently compillable.
-/

@[expose] public section

namespace CP027TwoFiniteSigns

open CP026OriginalPointBridge

/-- Exactly TWO remaining true original finite-approximant sign
premises for a narrow critical-line zeta zero: all Borwein
hypotheses have been supplied by CP027's genuine-source
pointwise proof candidates, but the Lean kernels are pending. -/
theorem original_narrow_critical_line_zero_of_two_finite_signs
    (hFiniteLeft :
        sourceFiniteZ tLeft + sourcePointError tLeft < 0)
    (hFiniteRight :
        0 < sourceFiniteZ tRight - sourcePointError tRight) :
    ∃ t : ℝ, tLeft < t ∧ t < tRight ∧
      riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0 := by
  exact original_critical_line_zero_in_narrow_bracket
    CP027PointwiseBorwein.original_center_Borwein_left
    CP027PointwiseBorwein.original_center_Borwein_right
    hFiniteLeft hFiniteRight

end CP027TwoFiniteSigns

#print axioms CP027TwoFiniteSigns.original_narrow_critical_line_zero_of_two_finite_signs
