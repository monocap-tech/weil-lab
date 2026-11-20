import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-!
NF735 pure support-geometry and two-block Gram pilot.

These are statements about arbitrary complex-valued functions and real
matrices. No zeta source is imported and no statement of Weil positivity is
assumed or proved. The actual EF / all-divisor identification is a separate
analytical obligation.
-/

/-- The unwindowed *oriented* cross correlation. The first source
occupies a left interval, and the second a right interval. -/
def neutralNF735CrossCorrelation (f g : ℝ → ℂ) (u : ℝ) : ℂ :=
  ∫ x : ℝ, g (x + u) * star (f x)

/-- The exact difference-support window. If f lives in [0,d] and
g in [L-d,L], the cross correlation is identically zero outside
[L-2d,L]. In particular, this gives the *candidate* moving prime
window once the actual Weil prime term has been linked to this
unwindowed correlation by a separate source-specific theorem. -/
theorem neutralNF735CrossCorrelation_zero_outside
    (f g : ℝ → ℂ) (d L u : ℝ)
    (hf : ∀ x, x ∉ Set.Icc (0 : ℝ) d → f x = 0)
    (hg : ∀ y, y ∉ Set.Icc (L - d) L → g y = 0)
    (hu : u < L - 2*d ∨ L < u) :
    neutralNF735CrossCorrelation f g u = 0 := by
  unfold neutralNF735CrossCorrelation
  have hzero : (fun x : ℝ => g (x + u) * star (f x)) =
      (fun _ => (0 : ℂ)) := by
    funext x
    by_cases hx : x ∈ Set.Icc (0 : ℝ) d
    · have hnot : x + u ∉ Set.Icc (L - d) L := by
        intro hy
        rcases hx with ⟨hx0, hxd⟩
        rcases hy with ⟨hy0, hyL⟩
        rcases hu with hleft | hright <;> linarith
      simp [hg (x + u) hnot]
    · simp [hf x hx]
  rw [hzero]
  simp

/-- For EVERY integer n (hence also for prime powers), the oriented
cross correlation at log n is supported on the corresponding moving
logarithmic interval. This is geometry; it does not assert that the
actual Weil prime term equals a sum of these evaluations. -/
theorem neutralNF735CrossCorrelation_log_zero_outside
    (f g : ℝ → ℂ) (d L : ℝ) (n : ℕ)
    (hf : ∀ x, x ∉ Set.Icc (0 : ℝ) d → f x = 0)
    (hg : ∀ y, y ∉ Set.Icc (L - d) L → g y = 0)
    (hn : Real.log (n : ℝ) < L - 2*d ∨ L < Real.log (n : ℝ)) :
    neutralNF735CrossCorrelation f g (Real.log (n : ℝ)) = 0 :=
  neutralNF735CrossCorrelation_zero_outside f g d L _ hf hg hn

/-- A complete real two-block quadratic form is nonnegative when its
diagonal energies are nonnegative and the mixed coefficient obeys the
2x2 Gram determinant bound. This criterion is algebraic only.
Source-specific global Weil use requires proving the Hermitian mixed
pairing and this determinant estimate with *actual* EF entries. -/
theorem neutralNF735RealTwoBlockPSD
    (a b m : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hdet : m^2 ≤ a*b) (u v : ℝ) :
    0 ≤ a*u^2 + 2*m*u*v + b*v^2 := by
  by_cases hzero : a = 0
  · have hm : m = 0 := by
      rw [hzero] at hdet
      nlinarith [sq_nonneg m]
    subst a
    subst m
    simpa using (mul_nonneg hb (sq_nonneg v))
  · have hapos : 0 < a := lt_of_le_of_ne ha (Ne.symm hzero)
    have hs : 0 ≤ (a*u + m*v)^2 + (a*b - m^2)*v^2 :=
      add_nonneg (sq_nonneg _) (mul_nonneg (sub_nonneg.mpr hdet) (sq_nonneg _))
    have he : (a*u + m*v)^2 + (a*b-m^2)*v^2 =
        a*(a*u^2 + 2*m*u*v + b*v^2) := by ring
    rw [he] at hs
    by_contra hneg
    have hq : a*u^2 + 2*m*u*v + b*v^2 < 0 := lt_of_not_ge hneg
    have hm : a*(a*u^2 + 2*m*u*v + b*v^2) < 0 :=
      mul_neg_of_pos_of_neg hapos hq
    linarith

#print axioms neutralNF735CrossCorrelation_zero_outside
#print axioms neutralNF735CrossCorrelation_log_zero_outside
#print axioms neutralNF735RealTwoBlockPSD

end
end WeilDefect
