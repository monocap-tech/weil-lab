import WeilDefect.MasterRecon.V10B10a

/-! A normalized compact defect is weaker than compactness of the
negative analysis map itself. The strict gap is an inequality modulo
a compact error, not a global contraction certificate. -/
namespace WeilDefect.MasterRecon.V10B10b

open scoped NNReal InnerProduct
open V10B10a (receiver normalized)

variable {H E F : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E]
variable [NormedAddCommGroup F] [InnerProductSpace ℂ F]

noncomputable def gap (A : H →L[ℂ] E) : ℝ := 1/(1+‖A‖^2)

theorem gap_pos (A : H →L[ℂ] E) : 0 < gap A := by
  unfold gap
  positivity

theorem gap_le_one (A : H →L[ℂ] E) : gap A ≤ 1 := by
  unfold gap
  exact (div_le_one (by positivity)).mpr (by nlinarith [sq_nonneg ‖A‖])

theorem gap_energy (A : H →L[ℂ] E) (x : H) :
    gap A*‖A x‖^2 ≤ ‖x‖^2 := by
  have h := (sq_le_sq₀ (norm_nonneg (A x)) (by positivity)).mpr (A.le_opNorm x)
  unfold gap
  rw [div_mul_eq_mul_div,one_mul]
  apply (div_le_iff₀ (by positivity : 0 < 1+‖A‖^2)).mpr
  rw [mul_pow] at h
  nlinarith [sq_nonneg ‖x‖]

theorem normalized_gap (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2)
    (K : H →L[ℂ] H)
    (hdef : ∀ x, ‖A x‖^2-‖B x‖^2 = ‖x‖^2+(inner ℂ (K x) x).re)
    (y : A.range) :
    ‖normalized A B b hb h y‖^2 ≤
      (1-gap A)*‖y‖^2 + ‖K (receiver A b hb h y)‖*‖receiver A b hb h y‖ := by
  let x := receiver A b hb h y
  have he : A.rangeRestrict x = y := V10B10a.receiver_right A b hb h y
  have hy : ‖A x‖ = ‖y‖ := by
    change ‖A.rangeRestrict x‖ = ‖y‖
    rw [he]
  have hn : normalized A B b hb h y = B x := rfl
  have hg := gap_energy A x
  have hd := hdef x
  have hnorm := norm_inner_le_norm (𝕜 := ℂ) (K x) x
  have hre := Complex.abs_re_le_norm (inner ℂ (K x) x)
  have hneg := neg_abs_le (inner ℂ (K x) x).re
  rw [hy] at hg hd
  rw [hn]
  change ‖B x‖^2 ≤ (1-gap A)*‖y‖^2+‖K x‖*‖x‖
  nlinarith only [hg,hd,hnorm,hre,hneg]

theorem compact_normalized_defect (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2)
    (K : H →L[ℂ] H) (hK : IsCompactOperator K)
    (hdef : ∀ x, ‖A x‖^2-‖B x‖^2 = ‖x‖^2+(inner ℂ (K x) x).re) :
    ∃ L : A.range →L[ℂ] H, IsCompactOperator L ∧
      ∀ y : A.range, ‖normalized A B b hb h y‖^2 ≤
        (1-gap A)*‖y‖^2 + (Real.sqrt (b:ℝ))⁻¹*‖L y‖*‖y‖ := by
  let R := receiver A b hb h
  refine ⟨K.comp R,hK.comp_clm R,?_⟩
  intro y
  have hr := R.le_opNorm y
  have hb' := V10B10a.receiver_bound A b hb h
  have hr' : ‖R y‖ ≤ (Real.sqrt (b:ℝ))⁻¹*‖y‖ :=
    hr.trans (mul_le_mul_of_nonneg_right hb' (norm_nonneg _))
  calc
    _ ≤ (1-gap A)*‖y‖^2 + ‖K (R y)‖*‖R y‖ :=
      normalized_gap A B b hb h K hdef y
    _ ≤ _ := by
      have hh := mul_le_mul_of_nonneg_left hr' (norm_nonneg (K (R y)))
      change _ ≤ (1-gap A)*‖y‖^2 + (Real.sqrt (b:ℝ))⁻¹*‖K (R y)‖*‖y‖
      nlinarith only [hh]

theorem normalized_strict_on_defect_kernel (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2)
    (K : H →L[ℂ] H)
    (hdef : ∀ x, ‖A x‖^2-‖B x‖^2 = ‖x‖^2+(inner ℂ (K x) x).re)
    (y : A.range) (hy : y ≠ 0) (hKy : K (receiver A b hb h y) = 0) :
    ‖normalized A B b hb h y‖ < ‖y‖ := by
  have hh := normalized_gap A B b hb h K hdef y
  rw [hKy,norm_zero,zero_mul,add_zero] at hh
  have hp := mul_pos (gap_pos A) (sq_pos_of_pos (norm_pos_iff.mpr hy))
  have hs : ‖normalized A B b hb h y‖^2 < ‖y‖^2 := by
    nlinarith only [hh,hp]
  exact (sq_lt_sq₀ (norm_nonneg _) (norm_nonneg _)).mp hs

end WeilDefect.MasterRecon.V10B10b

#print axioms WeilDefect.MasterRecon.V10B10b.gap_pos
#print axioms WeilDefect.MasterRecon.V10B10b.gap_le_one
#print axioms WeilDefect.MasterRecon.V10B10b.gap_energy
#print axioms WeilDefect.MasterRecon.V10B10b.normalized_gap
#print axioms WeilDefect.MasterRecon.V10B10b.compact_normalized_defect
#print axioms WeilDefect.MasterRecon.V10B10b.normalized_strict_on_defect_kernel
