import WeilDefect.Arithmetic.ActualZetaIV092OriginalGreenGradientErrorGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-- Lower real enclosure on the original diagonal, without assuming that
the finite complex expression is already real. -/
theorem neutralIV093GreenDiagonal_real_lower
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) :
    (neutralIV086PhysicalWeilFinite M N
      (neutralActualZetaGreenCorrelationInverse a v v)).re -
      ‖neutralActualZetaGradientSynthesis a v‖^2 / ((N : ℝ)+1)^2 ≤
      (neutralActualZetaGreenZeroForm a v v).re := by
  have h := neutralIV092GreenZeroForm_gradient_diagonal_error_bound a ha v M N hM
  have hr := Complex.re_le_norm
    (neutralIV086PhysicalWeilFinite M N
      (neutralActualZetaGreenCorrelationInverse a v v) -
      neutralActualZetaGreenZeroForm a v v)
  rw [norm_sub_rev] at hr
  rw [Complex.sub_re] at hr
  linarith

/-- Upper real enclosure, for an independently certified negative witness. -/
theorem neutralIV093GreenDiagonal_real_upper
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) :
    (neutralActualZetaGreenZeroForm a v v).re ≤
      (neutralIV086PhysicalWeilFinite M N
        (neutralActualZetaGreenCorrelationInverse a v v)).re +
      ‖neutralActualZetaGradientSynthesis a v‖^2 / ((N : ℝ)+1)^2 := by
  have h := neutralIV092GreenZeroForm_gradient_diagonal_error_bound a ha v M N hM
  have hr := Complex.re_le_norm
    (neutralActualZetaGreenZeroForm a v v -
      neutralIV086PhysicalWeilFinite M N
        (neutralActualZetaGreenCorrelationInverse a v v))
  rw [Complex.sub_re] at hr
  linarith

/-- Restricted physical mass coercivity. The gradient-to-mass bound is
a local premise on the actual vector, not a global Gamma form assumption. -/
theorem neutralIV093GreenDiagonal_restricted_coercivity
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) (B μ : ℝ)
    (hgrad : ‖neutralActualZetaGradientSynthesis a v‖^2 ≤
      B * ‖neutralActualZetaGreenSynthesis a v‖^2)
    (hfinite : μ * ‖neutralActualZetaGreenSynthesis a v‖^2 ≤
      (neutralIV086PhysicalWeilFinite M N
        (neutralActualZetaGreenCorrelationInverse a v v)).re) :
    (μ - B / ((N : ℝ)+1)^2) * ‖neutralActualZetaGreenSynthesis a v‖^2 ≤
      (neutralActualZetaGreenZeroForm a v v).re := by
  have h := neutralIV093GreenDiagonal_real_lower a ha v M N hM
  have hg := div_le_div_of_nonneg_right hgrad (sq_nonneg ((N : ℝ)+1))
  calc
    _ = μ * ‖neutralActualZetaGreenSynthesis a v‖^2 -
      (B * ‖neutralActualZetaGreenSynthesis a v‖^2) / ((N : ℝ)+1)^2 := by ring
    _ ≤ _ := by linarith

/-- A uniform sector theorem, with both premises restricted to the same
set of actual coefficients. No claim that this set exhausts the domain. -/
theorem neutralIV093GreenSector_restricted_coercivity
    (a : ℝ) (ha : 0 < a) (S : Set NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) (B μ : ℝ)
    (hgrad : ∀ v ∈ S, ‖neutralActualZetaGradientSynthesis a v‖^2 ≤
      B * ‖neutralActualZetaGreenSynthesis a v‖^2)
    (hfinite : ∀ v ∈ S, μ * ‖neutralActualZetaGreenSynthesis a v‖^2 ≤
      (neutralIV086PhysicalWeilFinite M N
        (neutralActualZetaGreenCorrelationInverse a v v)).re) :
    ∀ v ∈ S, (μ - B / ((N : ℝ)+1)^2) *
      ‖neutralActualZetaGreenSynthesis a v‖^2 ≤
        (neutralActualZetaGreenZeroForm a v v).re := by
  intro v hv
  exact neutralIV093GreenDiagonal_restricted_coercivity a ha v M N hM B μ
    (hgrad v hv) (hfinite v hv)

/-- Strict positivity for a nonzero physical vector when the retained
margin exceeds the entire truncation budget. -/
theorem neutralIV093GreenDiagonal_restricted_positive
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) (B μ : ℝ)
    (hgrad : ‖neutralActualZetaGradientSynthesis a v‖^2 ≤
      B * ‖neutralActualZetaGreenSynthesis a v‖^2)
    (hfinite : μ * ‖neutralActualZetaGreenSynthesis a v‖^2 ≤
      (neutralIV086PhysicalWeilFinite M N
        (neutralActualZetaGreenCorrelationInverse a v v)).re)
    (hmargin : B / ((N : ℝ)+1)^2 < μ)
    (hv : neutralActualZetaGreenSynthesis a v ≠ 0) :
    0 < (neutralActualZetaGreenZeroForm a v v).re := by
  have hn : 0 < ‖neutralActualZetaGreenSynthesis a v‖ := norm_pos_iff.mpr hv
  exact lt_of_lt_of_le
    (mul_pos (sub_pos.mpr hmargin) (pow_pos hn 2))
    (neutralIV093GreenDiagonal_restricted_coercivity a ha v M N hM B μ hgrad hfinite)

/-- A negative finite diagonal with strict error clearance gives a negative
original real diagonal. This is a conditional falsifier, not a found witness. -/
theorem neutralIV093GreenDiagonal_negative_of_finite
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ))
    (hneg : (neutralIV086PhysicalWeilFinite M N
        (neutralActualZetaGreenCorrelationInverse a v v)).re +
      ‖neutralActualZetaGradientSynthesis a v‖^2 / ((N : ℝ)+1)^2 < 0) :
    (neutralActualZetaGreenZeroForm a v v).re < 0 :=
  lt_of_le_of_lt (neutralIV093GreenDiagonal_real_upper a ha v M N hM) hneg

#print axioms neutralIV093GreenDiagonal_real_lower
#print axioms neutralIV093GreenDiagonal_real_upper
#print axioms neutralIV093GreenDiagonal_restricted_coercivity
#print axioms neutralIV093GreenSector_restricted_coercivity
#print axioms neutralIV093GreenDiagonal_restricted_positive
#print axioms neutralIV093GreenDiagonal_negative_of_finite

end
end WeilDefect
