import WeilDefect.DirichletResolvent
import Mathlib.NumberTheory.LSeries.ZetaZeros

namespace WeilDefect

noncomputable section

/-- Actual nontrivial zeta zero points in the open critical strip.
This is a point carrier, not a multiplicity-weighted divisor enumeration. -/
def NeutralActualZetaZeroPoint :=
  {ρ : ℂ // riemannZeta ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1}

/-- Bombieri ordinate convention: rho = 1/2 + I gamma. -/
def neutralActualZetaOrdinate (ρ : NeutralActualZetaZeroPoint) : ℂ :=
  -Complex.I * (ρ.val - 1 / 2)

theorem neutralActualZetaOrdinate_re (ρ : NeutralActualZetaZeroPoint) :
    (neutralActualZetaOrdinate ρ).re = ρ.val.im := by
  simp [neutralActualZetaOrdinate, Complex.mul_re]

theorem neutralActualZetaOrdinate_im (ρ : NeutralActualZetaZeroPoint) :
    (neutralActualZetaOrdinate ρ).im = 1 / 2 - ρ.val.re := by
  simp [neutralActualZetaOrdinate, Complex.mul_im]
  ring

/-- The actual source argument reconstructs the same zeta zero exactly. -/
theorem neutralActualZetaOrdinate_source (ρ : NeutralActualZetaZeroPoint) :
    (1 / 2 : ℂ) + Complex.I * neutralActualZetaOrdinate ρ = ρ.val := by
  unfold neutralActualZetaOrdinate
  simp only [neg_mul, mul_neg, ← mul_assoc, Complex.I_sq]
  ring

theorem neutralActualZetaOrdinate_zeta (ρ : NeutralActualZetaZeroPoint) :
    riemannZeta ((1 / 2 : ℂ) + Complex.I * neutralActualZetaOrdinate ρ) = 0 := by
  rw [neutralActualZetaOrdinate_source]
  exact ρ.property.1

/-- Open-strip membership yields a strict ordinate strip without RH. -/
theorem neutralActualZetaOrdinate_strictStrip (ρ : NeutralActualZetaZeroPoint) :
    |(neutralActualZetaOrdinate ρ).im| < 1 / 2 := by
  rw [neutralActualZetaOrdinate_im, abs_lt]
  constructor <;> linarith [ρ.property.2.1, ρ.property.2.2]

/-- The actual functional equation carries an open-strip zero to 1-rho. -/
def neutralActualZetaZeroReflect (ρ : NeutralActualZetaZeroPoint) :
    NeutralActualZetaZeroPoint := by
  refine ⟨1 - ρ.val, ?_, ?_, ?_⟩
  · have hn : ∀ n : ℕ, ρ.val ≠ -(n : ℂ) := by
      intro n h
      have hr := congrArg Complex.re h
      simp only [Complex.neg_re, Complex.natCast_re] at hr
      have hnat : 0 ≤ (n : ℝ) := by positivity
      linarith [ρ.property.2.1]
    have hone : ρ.val ≠ 1 := by
      intro h
      have hr := congrArg Complex.re h
      simp only [Complex.one_re] at hr
      linarith [ρ.property.2.2]
    rw [riemannZeta_one_sub hn hone, ρ.property.1, mul_zero]
  · simp only [Complex.sub_re, Complex.one_re]
    linarith [ρ.property.2.2]
  · simp only [Complex.sub_re, Complex.one_re]
    linarith [ρ.property.2.1]

theorem neutralActualZetaZeroReflect_involutive :
    Function.Involutive neutralActualZetaZeroReflect := by
  intro ρ
  apply Subtype.ext
  change 1 - (1 - ρ.val) = ρ.val
  ring

/-- Functional-equation reflection is gamma -> -gamma in this convention.
It is distinct from conjugate-ordinate pair reflection. -/
theorem neutralActualZetaOrdinate_reflect (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaOrdinate (neutralActualZetaZeroReflect ρ) =
      -neutralActualZetaOrdinate ρ := by
  change -Complex.I * ((1 - ρ.val) - 1 / 2) =
    -(-Complex.I * (ρ.val - 1 / 2))
  ring

/-- Every actual open-strip zero has a lawful nonzero Green denominator;
no shell-height lower bound or spectral L2 assumption is required. -/
theorem neutralActualZetaOrdinate_greenDenom_ne_zero
    (ρ : NeutralActualZetaZeroPoint) :
    problemOneGreenDenom (neutralActualZetaOrdinate ρ) ≠ 0 := by
  have hs := neutralActualZetaOrdinate_strictStrip ρ
  have hab := abs_lt.mp hs
  have hsq : (neutralActualZetaOrdinate ρ).im ^ 2 < 1 / 4 := by
    nlinarith [mul_pos (by linarith : 0 < 1 / 2 - (neutralActualZetaOrdinate ρ).im)
      (by linarith : 0 < 1 / 2 + (neutralActualZetaOrdinate ρ).im)]
  have hr : 0 < (problemOneGreenDenom (neutralActualZetaOrdinate ρ)).re := by
    simp only [problemOneGreenDenom, pow_two, Complex.add_re, Complex.mul_re]
    norm_num
    nlinarith [sq_nonneg (neutralActualZetaOrdinate ρ).re]
  intro hz
  have hzero := congrArg Complex.re hz
  simp only [Complex.zero_re] at hzero
  linarith

end

end WeilDefect
