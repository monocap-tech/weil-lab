import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentEnclosure

namespace WeilDefect
noncomputable section

/-! NF620: full-degree sign symmetry on the actual physical window.
This justifies the candidate schedule's sign quotient; no
approximate equality or frequency rounding is permitted. -/

def neutralNF620J (z : ℂ) (n : ℕ) : ℂ :=
  neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) z n

theorem neutralNF620J_neg (z : ℂ) (n : ℕ) :
    neutralNF620J (-z) n = (-1:ℂ)^n * neutralNF620J z n := by
  by_cases hz : z=0
  · subst z
    have h := neutralNF606ExpMoment_zero_frequency (-(11/10:ℝ)) (11/10:ℝ) n
    have he : neutralNF620J 0 n =
        ((11/10:ℂ)^(n+1)-(-(11/10:ℂ))^(n+1))/(n+1:ℂ) := by
      simpa [neutralNF620J] using h
    let p : ℂ := (-1:ℂ)^n
    have hs : p*p = 1 := by
      dsimp [p]
      rw [← mul_pow]
      norm_num
    have hb : (-(11/10:ℂ))^(n+1) = -p*(11/10:ℂ)^(n+1) := by
      rw [show -(11/10:ℂ)=(-1:ℂ)*(11/10) by ring,mul_pow,pow_succ]
      dsimp [p]
      ring
    rw [neg_zero,he,hb]
    change ((11/10:ℂ)^(n+1)- -p*(11/10:ℂ)^(n+1))/(n+1:ℂ) =
      p*(((11/10:ℂ)^(n+1)- -p*(11/10:ℂ)^(n+1))/(n+1:ℂ))
    have hnum : (11/10:ℂ)^(n+1)- -p*(11/10:ℂ)^(n+1) =
      p*((11/10:ℂ)^(n+1)- -p*(11/10:ℂ)^(n+1)) := by
      linear_combination -((11/10:ℂ)^(n+1))*hs
    rw [← mul_div_assoc,← hnum]
  · induction n with
    | zero =>
      have hp : z*neutralNF620J z 0 =
          Complex.exp (z*(11/10:ℂ))-Complex.exp (z*(-(11/10:ℂ))) := by
        simpa [neutralNF620J] using
          neutralNF606ExpMoment_zero_degree (-(11/10:ℝ)) (11/10:ℝ) z
      have hm : (-z)*neutralNF620J (-z) 0 =
          Complex.exp ((-z)*(11/10:ℂ))-Complex.exp ((-z)*(-(11/10:ℂ))) := by
        simpa [neutralNF620J] using
          neutralNF606ExpMoment_zero_degree (-(11/10:ℝ)) (11/10:ℝ) (-z)
      rw [show (-z)*(11/10:ℂ) = z*(-(11/10:ℂ)) by ring,
        show (-z)*(-(11/10:ℂ)) = z*(11/10:ℂ) by ring] at hm
      have he : z*(neutralNF620J (-z) 0-neutralNF620J z 0)=0 := by
        linear_combination -hm-hp
      simpa using sub_eq_zero.mp ((mul_eq_zero.mp he).resolve_left hz)
    | succ n ih =>
      let B : ℂ := 11/10
      let p : ℂ := (-1:ℂ)^n
      have hs : p*p=1 := by dsimp [p]; rw [← mul_pow]; norm_num
      have hb : (-B)^(n+1) = -p*B^(n+1) := by
        rw [show -B=(-1:ℂ)*B by ring,mul_pow,pow_succ]
        dsimp [p]
        ring
      have hrec (w : ℂ) : w*neutralNF620J w (n+1) =
          B^(n+1)*Complex.exp (w*B)-(-B)^(n+1)*Complex.exp (w*(-B))-
            (n+1:ℂ)*neutralNF620J w n := by
        simpa [neutralNF620J,B] using
          neutralNF606ExpMoment_succ (-(11/10:ℝ)) (11/10:ℝ) w n
      have hp := hrec z
      have hm := hrec (-z)
      rw [hb] at hp hm
      rw [show (-z)*B=z*(-B) by ring,show (-z)*(-B)=z*B by ring,ih] at hm
      change (-z)*neutralNF620J (-z) (n+1) =
        B^(n+1)*Complex.exp (z*(-B))-(-p*B^(n+1))*Complex.exp (z*B)-
          (n+1:ℂ)*(p*neutralNF620J z n) at hm
      have he : z*(neutralNF620J (-z) (n+1)+p*neutralNF620J z (n+1))=0 := by
        linear_combination -hm+p*hp+
          B^(n+1)*Complex.exp (z*(-B))*hs
      have h := (mul_eq_zero.mp he).resolve_left hz
      rw [pow_succ]
      change neutralNF620J (-z) (n+1)=p*(-1)*neutralNF620J z (n+1)
      linear_combination h

end
end WeilDefect
