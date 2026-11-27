import WeilDefect.MasterRecon.V10B12b

/-! A full-tail enclosure using an approximate action, not a projected
finite residual. A retained subtraction is allowed only if it lies in S. -/
namespace WeilDefect.MasterRecon.V10B14b

open scoped InnerProduct
open V10B12a (energy)

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

theorem action_error (G F : H →L[ℂ] H) (δ : ℝ) (hδ : ‖G-F‖ ≤ δ)
    (v s : H) :
    ‖G v-s‖ ≤ ‖F v-s‖+δ*‖v‖ := by
  have he : G v-s = (F v-s)+(G-F) v := by
    rw [ContinuousLinearMap.sub_apply]
    abel
  rw [he]
  exact (norm_add_le _ _).trans (add_le_add_left
    (((G-F).le_opNorm v).trans (mul_le_mul_of_nonneg_right hδ (norm_nonneg _))) _)

theorem residual_pairing (G : H →L[ℂ] H) (S : Submodule ℂ H)
    (v s : H) (hs : s ∈ S) (w : H) (hw : w ∈ Sᗮ) :
    inner ℂ (G v) w = inner ℂ (G v-s) w := by
  rw [inner_sub_left,show inner ℂ s w = 0 from hw s hs,sub_zero]

theorem approximate_energy (G F : H →L[ℂ] H) (δ : ℝ)
    (hδ : ‖G-F‖ ≤ δ) (v : H) :
    energy F v-δ*‖v‖^2 ≤ energy G v := by
  have hn : ‖(G-F) v‖ ≤ δ*‖v‖ :=
    ((G-F).le_opNorm v).trans (mul_le_mul_of_nonneg_right hδ (norm_nonneg _))
  have h := (Complex.abs_re_le_norm (inner ℂ ((G-F) v) v)).trans
    ((norm_inner_le_norm _ _).trans (mul_le_mul_of_nonneg_right hn (norm_nonneg v)))
  have hl := (abs_le.mp h).1
  rw [ContinuousLinearMap.sub_apply,inner_sub_left,Complex.sub_re] at hl
  unfold energy
  nlinarith only [hl]

theorem residual_reserve (G F : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (S : Submodule ℂ H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ y ∈ Sᗮ, c*‖y‖^2 ≤ energy G y)
    (δ : ℝ) (hδ : ‖G-F‖ ≤ δ)
    (v s w : H) (hs : s ∈ S) (hw : w ∈ Sᗮ) :
    energy F v-δ*‖v‖^2 -
      (2*‖F v-s‖^2+2*δ^2*‖v‖^2)/c ≤ energy G (v+w) := by
  have hδ0 := (norm_nonneg (G-F)).trans hδ
  have ha := action_error G F δ hδ v s
  have hsquare := (sq_le_sq₀ (norm_nonneg _) (by positivity)).mpr ha
  have h2 : ‖G v-s‖^2 ≤ 2*‖F v-s‖^2+2*δ^2*‖v‖^2 := by
    nlinarith only [hsquare,sq_nonneg (‖F v-s‖-δ*‖v‖)]
  have hdiv := div_le_div_of_nonneg_right h2 hc.le
  have hq := approximate_energy G F δ hδ v
  have ht := V10B12b.trial_lower G hG S c hc htail v (G v-s)
    (residual_pairing G S v s hs) w hw
  linarith

theorem approximate_certificate (G F : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (S : Submodule ℂ H) [S.HasOrthogonalProjection]
    (c : ℝ) (hc : 0 < c)
    (htail : ∀ y ∈ Sᗮ, c*‖y‖^2 ≤ energy G y)
    (δ : ℝ) (hδ : ‖G-F‖ ≤ δ)
    (Z : S →L[ℂ] Sᗮ) (Y : S →L[ℂ] S)
    (hfinite : ∀ x : S,
      let v : H := (x:H)-(Z x:H)
      0 ≤ energy F v-δ*‖v‖^2 -
        (2*‖F v-(Y x:H)‖^2+2*δ^2*‖v‖^2)/c) :
    ∀ g : H, 0 ≤ energy G g := by
  intro g
  obtain ⟨x,hx,y,hy,rfl⟩ := S.exists_add_mem_mem_orthogonal g
  let a : S := ⟨x,hx⟩
  let v : H := x-(Z a:H)
  let w : H := y+(Z a:H)
  have hw : w ∈ Sᗮ := Sᗮ.add_mem hy (Z a).property
  have he : v+w = x+y := by dsimp [v,w]; abel
  have h := residual_reserve G F hG S c hc htail δ hδ v (Y a:H) w
    (Y a).property hw
  rw [he] at h
  exact (hfinite a).trans h

end WeilDefect.MasterRecon.V10B14b

#print axioms WeilDefect.MasterRecon.V10B14b.action_error
#print axioms WeilDefect.MasterRecon.V10B14b.residual_pairing
#print axioms WeilDefect.MasterRecon.V10B14b.approximate_energy
#print axioms WeilDefect.MasterRecon.V10B14b.residual_reserve
#print axioms WeilDefect.MasterRecon.V10B14b.approximate_certificate
