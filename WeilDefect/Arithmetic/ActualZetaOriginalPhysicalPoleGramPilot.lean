import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramTerms
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointExpRecurrence

namespace WeilDefect
noncomputable section

/-! NF617: a deliberately small, genuine physical entry pilot.
The retained last selected generator is sinh(x/2), not an artificial
test mode. This module does not depend on the new NF615-616 proofs. -/

theorem neutralNF617PoleGram_exact :
    (neutralNF606PhysicalH (241:Fin 242) (241:Fin 242):ℂ) =
      (Complex.exp (11/10)-Complex.exp (-(11/10)))/2-(11/10) := by
  let J := fun z : ℂ => neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) z 0
  have hp : J 1 = Complex.exp (11/10)-Complex.exp (-(11/10)) := by
    have h := neutralNF606ExpMoment_zero_degree (-(11/10:ℝ)) (11/10:ℝ) (1:ℂ)
    simpa [J] using h
  have hm : J (-1) = Complex.exp (11/10)-Complex.exp (-(11/10)) := by
    have h := neutralNF606ExpMoment_zero_degree (-(11/10:ℝ)) (11/10:ℝ) (-1:ℂ)
    have h' : -J (-1) = Complex.exp (-(11/10))-Complex.exp (11/10) := by
      simpa [J] using h
    linear_combination -h'
  have hz : J 0 = (11/5:ℂ) := by
    have h := neutralNF606ExpMoment_zero_frequency (-(11/10:ℝ)) (11/10:ℝ) 0
    norm_num [J] at h ⊢ <;> assumption
  rw [← neutralNF607SelectedH_eq]
  unfold neutralNF607SelectedH neutralNF607SelectedTerm
  have hlast : ¬(241:Fin 242).val < 241 := by decide
  simp only [dif_neg hlast,neutralNF607Pair,neutralNF607SinhTerm,
    if_true,if_false,Bool.false_eq_true]
  change (1/2:ℂ)*(1/2)*J (1/2+1/2) +
      (1/2)*(-1/2)*J (1/2+ -1/2) +
      (-1/2)*(1/2)*J (-1/2+1/2) +
      (-1/2)*(-1/2)*J (-1/2+ -1/2) = _
  rw [show (1/2:ℂ)+1/2=1 by norm_num,
    show (1/2:ℂ)+ -1/2=0 by ring,
    show (-1/2:ℂ)+1/2=0 by ring,
    show (-1/2:ℂ)+ -1/2= -1 by norm_num,hp,hm,hz]
  ring

def neutralNF617Q : ℕ := 10^40
def neutralNF617N : ℕ := 48

theorem neutralNF617Q_pos : 0<neutralNF617Q := by norm_num [neutralNF617Q]

theorem neutralNF617ExpFee :
    2/(Nat.factorial neutralNF617N:ℝ) ≤ 1/(neutralNF617Q:ℝ) := by
  have h : 2*neutralNF617Q ≤ Nat.factorial neutralNF617N := by decide +kernel
  apply (div_le_div_iff₀ (by positivity : (0:ℝ)<Nat.factorial neutralNF617N)
    (by exact_mod_cast neutralNF617Q_pos : (0:ℝ)<neutralNF617Q)).mpr
  have h' : (2:ℝ)*(neutralNF617Q:ℝ) ≤ (Nat.factorial neutralNF617N:ℝ) := by exact_mod_cast h
  simpa using h'

def neutralNF617Small (h : ℚ) : NF591Rect :=
  neutralNF592SmallExpBall (NF591Rect.realQ h neutralNF617Q) neutralNF617Q neutralNF617N

def neutralNF617SquareExp (h : ℚ) : NF591Rect :=
  let a := neutralNF617Small h
  a.mulQ a neutralNF617Q

theorem neutralNF617SquareExp_sound (h : ℚ) (hh : |h|≤1) :
    (neutralNF617SquareExp h).Contains (Complex.exp ((h:ℂ)+(h:ℂ))) := by
  have hn : ‖(h:ℂ)‖≤1 := by
    rw [← Complex.ofReal_ratCast,Complex.norm_real,Real.norm_eq_abs]
    exact_mod_cast hh
  have ha := neutralNF592SmallExpBall_sound _ (h:ℂ) neutralNF617Q neutralNF617N
    neutralNF617Q_pos (by decide)
    (NF591Rect.contains_realQ h neutralNF617Q neutralNF617Q_pos) hn neutralNF617ExpFee
  rw [Complex.exp_add]
  exact NF591Rect.contains_mulQ ha ha neutralNF617Q neutralNF617Q_pos

def neutralNF617PoleGramBall : NF591Ball :=
  ((((neutralNF617SquareExp (11/20)).re.add
    (neutralNF617SquareExp (-11/20)).re.neg).divPos 2).round neutralNF617Q).add
    (NF591Ball.exactQ (-11/10) neutralNF617Q)

theorem neutralNF617PoleGramBall_sound :
    neutralNF617PoleGramBall.Contains (neutralNF606PhysicalH (241:Fin 242) (241:Fin 242)) := by
  have hp := (neutralNF617SquareExp_sound (11/20) (by norm_num)).1
  have hm := (neutralNF617SquareExp_sound (-11/20) (by norm_num)).1
  have hp' : (neutralNF617SquareExp (11/20)).re.Contains (Complex.exp (11/10)).re := by
    convert hp using 1 <;> norm_num
  have hm' : (neutralNF617SquareExp (-11/20)).re.Contains (Complex.exp (-(11/10))).re := by
    convert hm using 1 <;> norm_num
  have hs := NF591Ball.contains_add hp' (NF591Ball.contains_neg hm')
  have hd := NF591Ball.contains_round (NF591Ball.contains_divPos hs (by norm_num : (0:ℚ)<2))
    neutralNF617Q neutralNF617Q_pos
  have h := NF591Ball.contains_add hd
    (NF591Ball.contains_exactQ (-11/10) neutralNF617Q neutralNF617Q_pos)
  have he := congrArg Complex.re neutralNF617PoleGram_exact
  have hx : neutralNF606PhysicalH (241:Fin 242) (241:Fin 242) =
      ((Complex.exp (11/10)).re - (Complex.exp (-(11/10))).re)/2-11/10 := by
    norm_num [Complex.div_re,Complex.sub_re] at he ⊢ <;> linarith
  rw [hx]
  unfold neutralNF617PoleGramBall
  convert h using 1 <;> ring

def neutralNF617PoleTarget : NF591Ball :=
  ⟨2356474701241767793847805235787/10^31,1/10^30⟩

def neutralNF617PoleCheck : Bool :=
  decide (|neutralNF617PoleGramBall.mid-neutralNF617PoleTarget.mid| +
    neutralNF617PoleGramBall.rad ≤ neutralNF617PoleTarget.rad)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 10000000 in
theorem neutralNF617PoleCheck_true : neutralNF617PoleCheck = true := by
  decide +kernel

theorem neutralNF617PoleGram_certified :
    neutralNF617PoleTarget.Contains (neutralNF606PhysicalH (241:Fin 242) (241:Fin 242)) := by
  apply NF591Ball.contains_widen neutralNF617PoleGramBall_sound
  unfold NF591Ball.Widens
  exact of_decide_eq_true neutralNF617PoleCheck_true

end
end WeilDefect
