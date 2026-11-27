import WeilDefect.MasterRecon.V10B12a

/-! V10B12b: certified trial-response lower bound, independent of any
exact inverse construction. The residual is paired on the entire tail.
A negative trial value is also a literal rejection witness. -/
namespace WeilDefect.MasterRecon.V10B12b

open scoped InnerProduct
open V10B12a (energy)

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

theorem energy_add (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y)) (x y : H) :
    energy G (x+y) = energy G x+energy G y+2*(inner ℂ (G x) y).re := by
  have he : (inner ℂ (G y) x).re = (inner ℂ (G x) y).re := by
    rw [hG y x]
    exact inner_re_symm (𝕜 := ℂ) y (G x)
  unfold energy
  simp only [map_add,inner_add_left,inner_add_right,Complex.add_re]
  linarith

theorem square_reserve (c a b : ℝ) (hc : 0 < c) :
    -(a^2/c) ≤ c*b^2-2*a*b := by
  have hs : 0 ≤ (c*b-a)^2 := sq_nonneg _
  have hd : 0 ≤ (c*b-a)^2/c := div_nonneg hs hc.le
  have he : (c*b-a)^2/c = c*b^2-2*a*b+a^2/c := by
    field_simp [hc.ne']
    <;> ring
  rw [he] at hd
  linarith

theorem trial_lower (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (S : Submodule ℂ H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ y ∈ Sᗮ, c*‖y‖^2 ≤ energy G y)
    (v e : H) (he : ∀ y ∈ Sᗮ, inner ℂ (G v) y = inner ℂ e y)
    (w : H) (hw : w ∈ Sᗮ) :
    energy G v-‖e‖^2/c ≤ energy G (v+w) := by
  have hh := htail w hw
  have hn := norm_inner_le_norm (𝕜 := ℂ) e w
  have hr := Complex.abs_re_le_norm (inner ℂ e w)
  have hl := neg_abs_le (inner ℂ e w).re
  have hs := square_reserve c ‖e‖ ‖w‖ hc
  rw [energy_add G hG,he w hw]
  linarith

theorem trial_lower_projection (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (S : Submodule ℂ H) [S.HasOrthogonalProjection]
    (c : ℝ) (hc : 0 < c)
    (htail : ∀ y ∈ Sᗮ, c*‖y‖^2 ≤ energy G y)
    (v w : H) (hw : w ∈ Sᗮ) :
    energy G v-‖Sᗮ.starProjection (G v)‖^2/c ≤ energy G (v+w) := by
  apply trial_lower G hG S c hc htail v (Sᗮ.starProjection (G v)) _ w hw
  intro y hy
  have h := Sᗮ.inner_orthogonalProjectionOnto_eq_of_mem_right (⟨y,hy⟩ : Sᗮ) (G v)
  exact h.symm

theorem trial_certificate (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (S : Submodule ℂ H) [S.HasOrthogonalProjection]
    (c : ℝ) (hc : 0 < c)
    (htail : ∀ y ∈ Sᗮ, c*‖y‖^2 ≤ energy G y)
    (Z : S →L[ℂ] Sᗮ)
    (hfinite : ∀ x : S,
      ‖Sᗮ.starProjection (G ((x:H)-(Z x:H)))‖^2/c ≤
        energy G ((x:H)-(Z x:H))) :
    ∀ g : H, 0 ≤ energy G g := by
  intro g
  obtain ⟨x,hx,y,hy,rfl⟩ := S.exists_add_mem_mem_orthogonal g
  let a : S := ⟨x,hx⟩
  let v : H := x-(Z a:H)
  let w : H := y+(Z a:H)
  have hw : w ∈ Sᗮ := Sᗮ.add_mem hy (Z a).property
  have he : v+w = x+y := by dsimp [v,w]; abel
  have h := trial_lower_projection G hG S c hc htail v w hw
  rw [he] at h
  have hf := hfinite a
  change ‖Sᗮ.starProjection (G v)‖^2/c ≤ energy G v at hf
  linarith

theorem trial_rejection (G : H →L[ℂ] H)
    (S : Submodule ℂ H) (Z : S →L[ℂ] Sᗮ) (x : S)
    (h : energy G ((x:H)-(Z x:H)) < 0) :
    ∃ g : H, energy G g < 0 :=
  ⟨(x:H)-(Z x:H),h⟩

end WeilDefect.MasterRecon.V10B12b

#print axioms WeilDefect.MasterRecon.V10B12b.energy_add
#print axioms WeilDefect.MasterRecon.V10B12b.square_reserve
#print axioms WeilDefect.MasterRecon.V10B12b.trial_lower
#print axioms WeilDefect.MasterRecon.V10B12b.trial_lower_projection
#print axioms WeilDefect.MasterRecon.V10B12b.trial_certificate
#print axioms WeilDefect.MasterRecon.V10B12b.trial_rejection
