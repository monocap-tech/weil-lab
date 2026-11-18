import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBoundaryReceipts

namespace WeilDefect
noncomputable section

/-! NF615: prefer a rectangular norm upper bound whose certificate
is a single rational comparison. It is deliberately independent
of the external midpoint generator. -/

def neutralNF615RectNormUpper (a : NF591Rect) : ℚ :=
  |a.re.mid| + a.re.rad + (|a.im.mid| + a.im.rad)

theorem neutralNF615RectNormUpper_sound (a : NF591Rect) (z : ℂ)
    (hz : a.Contains z) :
    ‖z‖ ≤ (neutralNF615RectNormUpper a:ℝ) := by
  have h1 := NF591Ball.contains_abs_bound hz.1
  have h2 := NF591Ball.contains_abs_bound hz.2
  calc
    ‖z‖ = ‖(z.re:ℂ)+(z.im:ℂ)*Complex.I‖ := by rw [Complex.re_add_im]
    _ ≤ ‖(z.re:ℂ)‖+‖(z.im:ℂ)*Complex.I‖ := norm_add_le _ _
    _ = |z.re|+|z.im| := by
      simp [norm_mul,Complex.norm_real,Real.norm_eq_abs]
    _ ≤ _ := by
      unfold neutralNF615RectNormUpper
      push_cast at h1 h2 ⊢
      linarith

def neutralNF615RectBelow (a : NF591Rect) (r : ℚ) : Bool :=
  decide (neutralNF615RectNormUpper a ≤ r)

theorem neutralNF615RectBelow_sound (a : NF591Rect) (z : ℂ) (r : ℚ)
    (hz : a.Contains z) (hc : neutralNF615RectBelow a r = true) :
    ‖z‖ ≤ (r:ℝ) :=
  (neutralNF615RectNormUpper_sound a z hz).trans
    (by exact_mod_cast (of_decide_eq_true hc : neutralNF615RectNormUpper a ≤ r))

def neutralNF615ResidualRect (B Z q q' : NF591Rect) (Q n : ℕ) : NF591Rect :=
  (B.add (((NF591Rect.realQ (n+1:ℚ) Q).mulQ q Q).neg)).add
    ((Z.mulQ q' Q).neg)

theorem neutralNF615ResidualRect_sound (B Z q q' : NF591Rect)
    (b z u v : ℂ) (Q n : ℕ) (hQ : 0<Q)
    (hb : B.Contains b) (hz : Z.Contains z)
    (hu : q.Contains u) (hv : q'.Contains v) :
    (neutralNF615ResidualRect B Z q q' Q n).Contains
      (b-(n+1:ℂ)*u-z*v) := by
  have h1 := NF591Rect.contains_mulQ (NF591Rect.contains_realQ (n+1:ℚ) Q hQ) hu Q hQ
  have h2 := NF591Rect.contains_mulQ hz hv Q hQ
  simpa only [neutralNF615ResidualRect,sub_eq_add_neg,Rat.cast_add,Rat.cast_natCast,
    Rat.cast_one] using
    NF591Rect.contains_add (NF591Rect.contains_add hb (NF591Rect.contains_neg h1))
      (NF591Rect.contains_neg h2)

/-- A checked complex rectangle residual supplies the real bound
required by the analytic recurrence. Previous enclosure and radius
payment remain explicit and may be checked independently. -/
theorem neutralNF615Moment_succ_of_rect (p : NF591Ball) (hp : p.Contains Real.pi)
    (h f : ℚ) (hh : |h|≤1)
    (q q' : NF591Rect) (u v : ℂ) (hu : q.Contains u) (hv : q'.Contains v)
    (Q N n : ℕ) (hQ : 0<Q) (hN : 1≤N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ))
    (δ E R : ℝ) (S : ℚ)
    (hδ : 0<δ) (hz : δ ≤ ‖neutralNF615Lambda h f‖)
    (hprev : ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ)
      (neutralNF615Lambda h f) n-u‖ ≤ E)
    (hcheck : neutralNF615RectBelow
      (neutralNF615ResidualRect (neutralNF615BoundaryRect p h f Q N (n+1))
        (neutralNF615LambdaRect p h f Q) q q' Q n) S = true)
    (hpay : (S:ℝ)+(n+1:ℝ)*E ≤ δ*R) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ)
      (neutralNF615Lambda h f) (n+1)-v‖ ≤ R := by
  have hb := neutralNF615BoundaryRect_sound p hp h f hh Q N (n+1) hQ hN hfee
  have hZ := neutralNF615LambdaRect_sound p hp h f Q hQ
  have hres := neutralNF615ResidualRect_sound _ _ q q' _ _ u v Q n hQ hb hZ hu hv
  exact neutralNF614Moment_succ_enclosure _ _ _ u v n δ E R (S:ℝ) hδ hz hprev
    (neutralNF615RectBelow_sound _ _ S hres hcheck) hpay

end
end WeilDefect
