import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentRecurrence

namespace WeilDefect
noncomputable section

/-! NF614: a posteriori analytic moment enclosures. An approximate
moment is validated by its exact recurrence residual, without
evaluating the integral or assuming an external inverse. All
norm inequalities here are real premises; rational/ball
certification of those premises remains a separate task. -/

def neutralNF614Boundary (a b : ℝ) (z : ℂ) (n : ℕ) : ℂ :=
  (b:ℂ)^n * Complex.exp (z*(b:ℂ)) -
    (a:ℂ)^n * Complex.exp (z*(a:ℂ))

theorem neutralNF614Norm_from_scaled (z e : ℂ) (δ R : ℝ)
    (hδ : 0 < δ) (hz : δ ≤ ‖z‖)
    (h : ‖z*e‖ ≤ δ*R) : ‖e‖ ≤ R := by
  rw [norm_mul] at h
  have he := (mul_le_mul_of_nonneg_right hz (norm_nonneg e)).trans h
  exact (mul_le_mul_left hδ).mp he

theorem neutralNF614Moment_zero_enclosure (a b : ℝ) (z q : ℂ) (δ R : ℝ)
    (hδ : 0 < δ) (hz : δ ≤ ‖z‖)
    (hres : ‖neutralNF614Boundary a b z 0-z*q‖ ≤ δ*R) :
    ‖neutralNF606ExpMoment a b z 0-q‖ ≤ R := by
  apply neutralNF614Norm_from_scaled z _ δ R hδ hz
  rw [mul_sub,neutralNF606ExpMoment_zero_degree]
  simpa [neutralNF614Boundary] using hres

theorem neutralNF614Moment_succ_enclosure (a b : ℝ) (z q q' : ℂ)
    (n : ℕ) (δ E R S : ℝ)
    (hδ : 0 < δ) (hz : δ ≤ ‖z‖)
    (hprev : ‖neutralNF606ExpMoment a b z n-q‖ ≤ E)
    (hres : ‖neutralNF614Boundary a b z (n+1)-(n+1:ℂ)*q-z*q'‖ ≤ S)
    (hpay : S+(n+1:ℝ)*E ≤ δ*R) :
    ‖neutralNF606ExpMoment a b z (n+1)-q'‖ ≤ R := by
  apply neutralNF614Norm_from_scaled z _ δ R hδ hz
  rw [mul_sub,neutralNF606ExpMoment_succ]
  have he :
      (b:ℂ)^(n+1)*Complex.exp (z*(b:ℂ)) -
      (a:ℂ)^(n+1)*Complex.exp (z*(a:ℂ)) -
      (n+1:ℂ)*neutralNF606ExpMoment a b z n-z*q' =
      (neutralNF614Boundary a b z (n+1)-(n+1:ℂ)*q-z*q') +
        (-(n+1:ℂ))*(neutralNF606ExpMoment a b z n-q) := by
    unfold neutralNF614Boundary
    ring
  rw [he]
  apply (norm_add_le _ _).trans
  rw [norm_mul,norm_neg]
  have hn : ‖(n+1:ℂ)‖ = (n+1:ℝ) := by
    rw [show (n+1:ℂ) = ((n+1:ℝ):ℂ) by push_cast; rfl,
      Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg (by positivity)]
  rw [hn]
  exact (add_le_add hres (mul_le_mul_of_nonneg_left hprev (by positivity))).trans hpay

/-- The zero combined frequency is exact and never requires a
positive lower bound on a complex denominator. -/
theorem neutralNF614Moment_exact_zero (a b : ℝ) (n : ℕ) :
    neutralNF606ExpMoment a b 0 n =
      ((b:ℂ)^(n+1)-(a:ℂ)^(n+1))/(n+1:ℂ) :=
  neutralNF606ExpMoment_zero_frequency a b n

end
end WeilDefect
