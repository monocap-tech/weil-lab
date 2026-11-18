import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramTerms

namespace WeilDefect
noncomputable section

/-! NF619: assemble complete physical matrix entries from the
original moment pilots, using exact evenness of the degree-zero
symmetric interval primitive. No independent negative-exponent
quadrature is required. -/

def neutralNF619J (z : ℂ) : ℂ :=
  neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) z 0

theorem neutralNF619J_neg (z : ℂ) :
    neutralNF619J (-z) = neutralNF619J z := by
  by_cases hz : z=0
  · simp [hz]
  · have hp : z*neutralNF619J z =
      Complex.exp (z*(11/10:ℂ))-Complex.exp (z*(-(11/10:ℂ))) := by
      simpa [neutralNF619J] using
        neutralNF606ExpMoment_zero_degree (-(11/10:ℝ)) (11/10:ℝ) z
    have hm : (-z)*neutralNF619J (-z) =
      Complex.exp ((-z)*(11/10:ℂ))-Complex.exp ((-z)*(-(11/10:ℂ))) := by
      simpa [neutralNF619J] using
        neutralNF606ExpMoment_zero_degree (-(11/10:ℝ)) (11/10:ℝ) (-z)
    rw [show (-z)*(11/10:ℂ) = z*(-(11/10:ℂ)) by ring,
      show (-z)*(-(11/10:ℂ)) = z*(11/10:ℂ) by ring] at hm
    have he : z*(neutralNF619J (-z)-neutralNF619J z)=0 := by
      linear_combination -hm-hp
    exact sub_eq_zero.mp ((mul_eq_zero.mp he).resolve_left hz)

theorem neutralNF619J_zero : neutralNF619J 0 = (11/5:ℂ) := by
  have h := neutralNF606ExpMoment_zero_frequency (-(11/10:ℝ)) (11/10:ℝ) 0
  norm_num [neutralNF619J] at h ⊢ <;> assumption

def neutralNF619W : ℂ := 2*(Real.pi:ℂ)*(37/64)
def neutralNF619Z : ℂ := Complex.I*neutralNF619W

theorem neutralNF619FirstTerm (s : Bool) :
    neutralNF607SelectedTerm (0:Fin 242) s = neutralNF607SinTerm neutralNF619W 0 s := by
  have hn : nf545OriginalOscillatorNodeAt (0:Fin 241) = (37/64,0) := by decide +kernel
  unfold neutralNF607SelectedTerm
  simp [hn,neutralNF619W]

theorem neutralNF619LastTerm (s : Bool) :
    neutralNF607SelectedTerm (241:Fin 242) s = neutralNF607SinhTerm s := by
  simp [neutralNF607SelectedTerm]

theorem neutralNF619SinCoeff :
    (1:ℂ)/(2*Complex.I) = -Complex.I/2 := by
  apply (div_eq_iff (by exact mul_ne_zero (by norm_num) Complex.I_ne_zero)).2
  calc
    (1:ℂ) = -(Complex.I*Complex.I) := by rw [Complex.I_mul_I]; ring
    _ = (-Complex.I/2)*(2*Complex.I) := by ring

theorem neutralNF619OscGram_exact :
    (neutralNF606PhysicalH (0:Fin 242) (0:Fin 242):ℂ) =
      (11/10:ℂ)-neutralNF619J (2*neutralNF619Z)/2 := by
  rw [← neutralNF607SelectedH_eq]
  unfold neutralNF607SelectedH
  simp only [neutralNF619FirstTerm,neutralNF607Pair,neutralNF607SinTerm,
    if_true,if_false,Bool.false_eq_true]
  change (1/(2*Complex.I))*(1/(2*Complex.I))*neutralNF619J (neutralNF619Z+neutralNF619Z) +
    (1/(2*Complex.I))*(-1/(2*Complex.I))*neutralNF619J (neutralNF619Z+ -neutralNF619Z) +
    (-1/(2*Complex.I))*(1/(2*Complex.I))*neutralNF619J (-neutralNF619Z+neutralNF619Z) +
    (-1/(2*Complex.I))*(-1/(2*Complex.I))*neutralNF619J (-neutralNF619Z+ -neutralNF619Z) = _
  rw [show neutralNF619Z+neutralNF619Z=2*neutralNF619Z by ring,
    show neutralNF619Z+ -neutralNF619Z=0 by ring,
    show -neutralNF619Z+neutralNF619Z=0 by ring,
    show -neutralNF619Z+ -neutralNF619Z=-(2*neutralNF619Z) by ring,
    neutralNF619J_neg,neutralNF619J_zero]
  simp only [neg_div,neutralNF619SinCoeff]
  have hi : Complex.I^2 = -1 := by rw [pow_two,Complex.I_mul_I]
  ring_nf
  simp only [hi]
  ring

theorem neutralNF619MixedGram_exact :
    (neutralNF606PhysicalH (0:Fin 242) (241:Fin 242):ℂ) =
      (-Complex.I/2)*(neutralNF619J (neutralNF619Z+1/2)-
        neutralNF619J (neutralNF619Z-1/2)) := by
  rw [← neutralNF607SelectedH_eq]
  unfold neutralNF607SelectedH
  simp only [neutralNF619FirstTerm,neutralNF619LastTerm,neutralNF607Pair,
    neutralNF607SinTerm,neutralNF607SinhTerm,if_true,if_false,Bool.false_eq_true]
  change (1/(2*Complex.I))*(1/2)*neutralNF619J (neutralNF619Z+1/2) +
    (1/(2*Complex.I))*(-1/2)*neutralNF619J (neutralNF619Z+ -1/2) +
    (-1/(2*Complex.I))*(1/2)*neutralNF619J (-neutralNF619Z+1/2) +
    (-1/(2*Complex.I))*(-1/2)*neutralNF619J (-neutralNF619Z+ -1/2) = _
  rw [show neutralNF619Z+ -1/2=neutralNF619Z-1/2 by ring,
    show -neutralNF619Z+1/2=-(neutralNF619Z-1/2) by ring,
    show -neutralNF619Z+ -1/2=-(neutralNF619Z+1/2) by ring,
    neutralNF619J_neg,neutralNF619J_neg]
  simp only [neg_div,neutralNF619SinCoeff]
  ring

/-- Real projection of the complex norm enclosure, with no
assumption that the proposed midpoint is an exact real moment. -/
theorem neutralNF619OscGram_of_moment (q : ℂ) (r : ℝ)
    (h : ‖neutralNF619J (2*neutralNF619Z)-q‖ ≤ r) :
    |neutralNF606PhysicalH (0:Fin 242) (0:Fin 242)-(11/10-q.re/2)| ≤ r/2 := by
  have he := congrArg Complex.re neutralNF619OscGram_exact
  have hp := (Complex.abs_re_le_norm (neutralNF619J (2*neutralNF619Z)-q)).trans h
  simp only [Complex.sub_re] at hp
  have hr : neutralNF606PhysicalH (0:Fin 242) (0:Fin 242) =
      11/10-(neutralNF619J (2*neutralNF619Z)).re/2 := by
    norm_num [Complex.sub_re,Complex.div_re] at he ⊢ <;> linarith
  rw [hr,show (11/10:ℝ)-(neutralNF619J (2*neutralNF619Z)).re/2-(11/10-q.re/2) =
    -((neutralNF619J (2*neutralNF619Z)).re-q.re)/2 by ring,abs_div,abs_neg]
  norm_num only [abs_of_pos (by norm_num : (0:ℝ)<2)]
  linarith

theorem neutralNF619MixedGram_of_moments (p q : ℂ) (r s : ℝ)
    (hp : ‖neutralNF619J (neutralNF619Z+1/2)-p‖ ≤ r)
    (hq : ‖neutralNF619J (neutralNF619Z-1/2)-q‖ ≤ s) :
    |neutralNF606PhysicalH (0:Fin 242) (241:Fin 242)-(p.im-q.im)/2| ≤ (r+s)/2 := by
  have he := congrArg Complex.re neutralNF619MixedGram_exact
  have hr : neutralNF606PhysicalH (0:Fin 242) (241:Fin 242) =
      ((neutralNF619J (neutralNF619Z+1/2)).im-
        (neutralNF619J (neutralNF619Z-1/2)).im)/2 := by
    norm_num [Complex.mul_re,Complex.sub_re,Complex.sub_im,Complex.div_re,
      Complex.div_im] at he ⊢ <;> linarith
  have e1 := (Complex.abs_im_le_norm (neutralNF619J (neutralNF619Z+1/2)-p)).trans hp
  have e2 := (Complex.abs_im_le_norm (neutralNF619J (neutralNF619Z-1/2)-q)).trans hq
  simp only [Complex.sub_im] at e1 e2
  rw [hr,show _ = (((neutralNF619J (neutralNF619Z+1/2)).im-p.im)-
    ((neutralNF619J (neutralNF619Z-1/2)).im-q.im))/2 by ring,abs_div]
  have hab (x y : ℝ) : |x-y| ≤ |x|+|y| := by
    simpa only [sub_eq_add_neg,abs_neg] using abs_add_le x (-y)
  norm_num only [abs_of_pos (by norm_num : (0:ℝ)<2)]
  linarith [hab ((neutralNF619J (neutralNF619Z+1/2)).im-p.im)
    ((neutralNF619J (neutralNF619Z-1/2)).im-q.im)]

end
end WeilDefect
