import WeilDefect.MasterRecon.V08C
import Mathlib.Analysis.Complex.Exponential

/-! V08D: bounded rectangle Fourier kernel approximation and compact
rank-one moment sums. No actual L² moment identification is asserted
until the supported physical and frequency carriers are attached. -/
namespace WeilDefect.MasterRecon.V08D

open Filter Finset
open scoped Topology BigOperators

noncomputable def fourierKernel (u x : ℝ) : ℂ :=
  Complex.exp (-Complex.I * (u : ℂ) * (x : ℂ))

noncomputable def kernelPolynomial (n : ℕ) (u x : ℝ) : ℂ :=
  ∑ j ∈ Finset.range n, (-Complex.I * (u : ℂ) * (x : ℂ)) ^ j / (j.factorial : ℂ)

theorem kernelPolynomial_separated (n : ℕ) (u x : ℝ) :
    kernelPolynomial n u x =
      ∑ j ∈ Finset.range n,
        ((-Complex.I * (u : ℂ)) ^ j / (j.factorial : ℂ)) * (x : ℂ) ^ j := by
  unfold kernelPolynomial
  apply Finset.sum_congr rfl
  intro j _
  rw [mul_pow]
  ring

/-- A uniform remainder for a genuine bounded Fourier rectangle.
The Taylor polynomial uses n terms, starting at degree zero. -/
theorem kernel_remainder (n : ℕ) (R t u x : ℝ)
    (hu : |u| ≤ R) (hx : |x| ≤ t)
    (hn : R * t / ((n : ℝ) + 1) ≤ 1 / 2) :
    ‖fourierKernel u x - kernelPolynomial n u x‖ ≤
      (R * t) ^ n / (n.factorial : ℝ) * 2 := by
  let z : ℂ := -Complex.I * (u : ℂ) * (x : ℂ)
  have hR : 0 ≤ R := (abs_nonneg u).trans hu
  have ht : 0 ≤ t := (abs_nonneg x).trans hx
  have hz : ‖z‖ ≤ R * t := by
    have he : ‖z‖ = |u| * |x| := by
      simp [z, norm_mul, Complex.norm_real, Real.norm_eq_abs]
    rw [he]
    exact mul_le_mul hu hx (abs_nonneg x) hR
  have hsmall : ‖z‖ / (n.succ : ℝ) ≤ 1 / 2 := by
    push_cast
    exact (div_le_div_of_nonneg_right hz (by positivity)).trans hn
  have h := Complex.exp_bound' (n := n) hsmall
  change ‖fourierKernel u x - kernelPolynomial n u x‖ ≤ _ at h
  refine h.trans ?_
  have hp : ‖z‖ ^ n ≤ (R * t) ^ n := by
    gcongr
  exact mul_le_mul_of_nonneg_right
    (div_le_div_of_nonneg_right hp (by positivity)) (by norm_num)

variable {H L : Type*}
variable [NormedAddCommGroup H] [NormedSpace ℂ H]
variable [NormedAddCommGroup L] [NormedSpace ℂ L] [CompleteSpace L]

theorem moment_rank_one_compact (f : H →L[ℂ] ℂ) (v : L) :
    IsCompactOperator (f.smulRight v) := by
  let g : ℂ →L[ℂ] L := (1 : ℂ →L[ℂ] ℂ).smulRight v
  have hg : IsCompactOperator g := isCompactOperator_of_locallyCompactSpace_rng g
  have he : g.comp f = f.smulRight v := by
    ext x
    rfl
  rw [← he]
  exact hg.comp_clm f

theorem moment_rank_one_norm (f : H →L[ℂ] ℂ) (v : L) :
    ‖f.smulRight v‖ ≤ ‖f‖ * ‖v‖ := by
  apply ContinuousLinearMap.opNorm_le_bound _ (by positivity)
  intro x
  rw [ContinuousLinearMap.smulRight_apply, norm_smul]
  calc
    ‖f x‖ * ‖v‖ ≤ (‖f‖ * ‖x‖) * ‖v‖ :=
      mul_le_mul_of_nonneg_right (f.le_opNorm x) (norm_nonneg v)
    _ = _ := by ring

theorem moment_partial_sum_compact (f : ℕ → H →L[ℂ] ℂ) (v : ℕ → L)
    (s : Finset ℕ) :
    IsCompactOperator (↑(∑ j ∈ s, (f j).smulRight (v j) : H →L[ℂ] L) : H → L) := by
  classical
  induction s using Finset.induction_on with
  | empty =>
    simpa only [Finset.sum_empty] using
      (isCompactOperator_zero : IsCompactOperator (0 : H →L[ℂ] L))
  | insert j s hj ih =>
    rw [Finset.sum_insert hj]
    exact (moment_rank_one_compact (f j) (v j)).add ih

/-- The limit of norm-summable separated moment operators is compact.
This is the bounded-band Fourier compactness receiver. -/
theorem moment_series_compact (f : ℕ → H →L[ℂ] ℂ) (v : ℕ → L)
    (C : H →L[ℂ] L)
    (hs : HasSum (fun j => (f j).smulRight (v j)) C) :
    IsCompactOperator C := by
  apply isCompactOperator_of_tendsto hs
  exact Eventually.of_forall (fun s => moment_partial_sum_compact f v s)

theorem factorial_moment_series_compact
    (f : ℕ → H →L[ℂ] ℂ) (v : ℕ → L) (B r : ℝ)
    (hB : 0 ≤ B) (hr : 0 ≤ r)
    (hbound : ∀ j, ‖f j‖ * ‖v j‖ ≤ B * (r ^ j / (j.factorial : ℝ))) :
    Summable (fun j => (f j).smulRight (v j)) ∧
      IsCompactOperator (↑(∑' j, (f j).smulRight (v j) : H →L[ℂ] L) : H → L) := by
  have hs : Summable (fun j : ℕ => r ^ j / (j.factorial : ℝ)) := by
    have h := NormedSpace.norm_expSeries_div_summable r
    convert h using 1
    funext j
    rw [Real.norm_of_nonneg (by positivity)]
  have hnorm : Summable (fun j => ‖(f j).smulRight (v j)‖) :=
    Summable.of_nonneg_of_le (fun j => norm_nonneg _)
      (fun j => (moment_rank_one_norm (f j) (v j)).trans (hbound j))
      (hs.mul_left B)
  have h := hnorm.of_norm
  exact ⟨h, moment_series_compact f v _ h.hasSum⟩

end WeilDefect.MasterRecon.V08D

#print axioms WeilDefect.MasterRecon.V08D.kernelPolynomial_separated
#print axioms WeilDefect.MasterRecon.V08D.kernel_remainder
#print axioms WeilDefect.MasterRecon.V08D.moment_rank_one_compact
#print axioms WeilDefect.MasterRecon.V08D.moment_rank_one_norm
#print axioms WeilDefect.MasterRecon.V08D.moment_partial_sum_compact
#print axioms WeilDefect.MasterRecon.V08D.moment_series_compact
#print axioms WeilDefect.MasterRecon.V08D.factorial_moment_series_compact
