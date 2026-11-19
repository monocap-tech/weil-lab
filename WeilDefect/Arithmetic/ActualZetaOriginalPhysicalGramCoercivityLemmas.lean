import Mathlib

namespace WeilDefect

/-! NF658: elementary coercivity inequalities for symmetric physical Gram
blocks. These lemmas are independent of the source archive and will be
used to transport a verified diagonal-dominance margin to a quadratic form. -/

theorem neutralNF658CrossTerm_lower (a u v : ℝ) :
    -|a| * (u^2 + v^2) ≤ 2*a*u*v := by
  rcases le_total 0 a with ha | ha
  · rw [abs_of_nonneg ha]
    have hs : 0 ≤ a * (u+v)^2 :=
      mul_nonneg ha (sq_nonneg _)
    nlinarith
  · rw [abs_of_nonpos ha]
    have hs : 0 ≤ (-a) * (u-v)^2 :=
      mul_nonneg (neg_nonneg.mpr ha) (sq_nonneg _)
    nlinarith

theorem neutralNF658Bilinear_enclosure
    (center radius actual u v : ℝ)
    (h : |actual-center| ≤ radius) :
    center*u*v - radius*|u*v| ≤ actual*u*v := by
  have hp : |(actual-center)*(u*v)| ≤ radius*|u*v| := by
    rw [abs_mul]
    exact mul_le_mul_of_nonneg_right h (abs_nonneg _)
  have hn : -(radius*|u*v|) ≤ (actual-center)*(u*v) :=
    (neg_le_of_abs_le hp)
  nlinarith [hn]

end WeilDefect
