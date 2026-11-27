import WeilDefect.MasterRecon.V10B11a

/-! Exact Schur receiver on a finite sector and its Hilbert orthogonal
complement. The tail solve is obtained from coercivity and closed range.
The remaining finite-sector inequality includes the cross response. -/
namespace WeilDefect.MasterRecon.V10B11b

open Set
open scoped InnerProduct NNReal

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

def energy (G : H →L[ℂ] H) (x : H) : ℝ := (inner ℂ (G x) x).re

theorem coercive_norm (G : H →L[ℂ] H) (c : ℝ) (hc : 0 < c)
    (h : ∀ x, c*‖x‖^2 ≤ energy G x) (x : H) : c*‖x‖ ≤ ‖G x‖ := by
  by_cases hx : x = 0
  · simp [hx]
  have hp := norm_pos_iff.mpr hx
  have h₁ := (Complex.re_le_norm (inner ℂ (G x) x)).trans (norm_inner_le_norm _ _)
  have h₂ : (c*‖x‖)*‖x‖ ≤ ‖G x‖*‖x‖ := by
    calc
      _ = c*‖x‖^2 := by ring
      _ ≤ _ := (h x).trans h₁
  exact (mul_le_mul_iff_right₀ hp).mp h₂

theorem coercive_bijective (G : H →L[ℂ] H) (c : ℝ) (hc : 0 < c)
    (h : ∀ x, c*‖x‖^2 ≤ energy G x) : Function.Bijective G := by
  let d : ℝ≥0 := ⟨c⁻¹,by positivity⟩
  have ha : AntilipschitzWith d G := by
    apply AntilipschitzWith.of_le_mul_dist
    intro x y
    rw [dist_eq_norm,dist_eq_norm,← map_sub]
    change ‖x-y‖ ≤ c⁻¹*‖G (x-y)‖
    exact (inv_mul_le_iff₀ hc).mpr (by simpa only [mul_comm] using coercive_norm G c hc h (x-y))
  have hclosed : IsClosed (G.range : Set H) := ha.isClosed_range G.uniformContinuous
  letI : CompleteSpace G.range := hclosed.completeSpace_coe
  have htop : G.range = ⊤ := by
    rw [← G.range.orthogonal_orthogonal,Submodule.eq_top_iff']
    intro v w hw
    have hz : inner ℂ (G w) w = 0 := hw _ ⟨w,rfl⟩
    have hh := h w
    unfold energy at hh
    rw [hz,Complex.zero_re] at hh
    have hnorm : ‖w‖ = 0 := by
      by_contra hn
      have hp := mul_pos hc (sq_pos_of_pos (lt_of_le_of_ne (norm_nonneg w) (Ne.symm hn)))
      linarith
    rw [norm_eq_zero.mp hnorm,inner_zero_left]
  exact ⟨ha.injective,fun y => by
    have hy : y ∈ G.range := by rw [htop]; trivial
    exact hy⟩

variable (S : Submodule ℂ H) [S.HasOrthogonalProjection]

noncomputable def tailBlock (G : H →L[ℂ] H) : Sᗮ →L[ℂ] Sᗮ :=
  Sᗮ.orthogonalProjectionOnto.comp (G.comp Sᗮ.subtypeL)

noncomputable def crossBlock (G : H →L[ℂ] H) : S →L[ℂ] Sᗮ :=
  Sᗮ.orthogonalProjectionOnto.comp (G.comp S.subtypeL)

theorem tail_pairing (G : H →L[ℂ] H) (x y : Sᗮ) :
    inner ℂ (tailBlock S G x) y = inner ℂ (G (x:H)) (y:H) :=
  Sᗮ.inner_orthogonalProjectionOnto_eq_of_mem_right y (G (x:H))

theorem cross_pairing (G : H →L[ℂ] H) (x : S) (y : Sᗮ) :
    inner ℂ (crossBlock S G x) y = inner ℂ (G (x:H)) (y:H) :=
  Sᗮ.inner_orthogonalProjectionOnto_eq_of_mem_right y (G (x:H))

theorem tail_coercive (G : H →L[ℂ] H) (c : ℝ)
    (htail : ∀ x ∈ Sᗮ, c*‖x‖^2 ≤ energy G x) (x : Sᗮ) :
    c*‖x‖^2 ≤ energy (tailBlock S G) x := by
  unfold energy
  rw [tail_pairing]
  exact htail x x.property

noncomputable def tailInverse (G : H →L[ℂ] H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ x ∈ Sᗮ, c*‖x‖^2 ≤ energy G x) : Sᗮ ≃L[ℂ] Sᗮ :=
  ContinuousLinearEquiv.ofBijective (tailBlock S G)
    (LinearMap.ker_eq_bot.mpr (coercive_bijective _ c hc (tail_coercive S G c htail)).1)
    (LinearMap.range_eq_top.mpr (coercive_bijective _ c hc (tail_coercive S G c htail)).2)

noncomputable def response (G : H →L[ℂ] H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ x ∈ Sᗮ, c*‖x‖^2 ≤ energy G x) (x : S) : Sᗮ :=
  (tailInverse S G c hc htail).symm (crossBlock S G x)

theorem response_eq (G : H →L[ℂ] H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ x ∈ Sᗮ, c*‖x‖^2 ≤ energy G x) (x : S) :
    tailBlock S G (response S G c hc htail x) = crossBlock S G x :=
  (tailInverse S G c hc htail).apply_symm_apply _

theorem response_pairing (G : H →L[ℂ] H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ x ∈ Sᗮ, c*‖x‖^2 ≤ energy G x) (x : S) (y : Sᗮ) :
    inner ℂ (G (response S G c hc htail x:H)) (y:H) =
      inner ℂ (G (x:H)) (y:H) := by
  rw [← tail_pairing S G, response_eq S G c hc htail, cross_pairing S G]

theorem energy_add (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y)) (x y : H) :
    energy G (x+y) = energy G x + energy G y + 2*(inner ℂ (G x) y).re := by
  have he : (inner ℂ (G y) x).re = (inner ℂ (G x) y).re := by
    rw [hG y x]
    exact inner_re_symm (𝕜 := ℂ) y (G x)
  unfold energy
  rw [map_add,inner_add_left,inner_add_right,inner_add_right]
  simp only [Complex.add_re]
  linarith

theorem schur_completion (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (c : ℝ) (hc : 0 < c)
    (htail : ∀ x ∈ Sᗮ, c*‖x‖^2 ≤ energy G x) (x : S) (y : Sᗮ) :
    energy G ((x:H)+(y:H)) =
      (energy G (x:H)-energy G (response S G c hc htail x:H)) +
      energy G ((y:H)+(response S G c hc htail x:H)) := by
  rw [energy_add G hG,energy_add G hG]
  have h₁ := response_pairing S G c hc htail x y
  have he : (inner ℂ (G (y:H)) (response S G c hc htail x:H)).re =
      (inner ℂ (G (x:H)) (y:H)).re := by
    rw [hG (y:H) (response S G c hc htail x:H),inner_re_symm (𝕜 := ℂ) (y:H),h₁]
  linarith

theorem positivity_iff_schur (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (c : ℝ) (hc : 0 < c)
    (htail : ∀ x ∈ Sᗮ, c*‖x‖^2 ≤ energy G x) :
    (∀ z : H, 0 ≤ energy G z) ↔
      ∀ x : S, 0 ≤ energy G (x:H)-energy G (response S G c hc htail x:H) := by
  constructor
  · intro h x
    have hh := h ((x:H) + ((-response S G c hc htail x : Sᗮ):H))
    rw [schur_completion S G hG c hc htail x (-response S G c hc htail x)] at hh
    simpa [energy] using hh
  · intro h z
    obtain ⟨x,hx,y,hy,rfl⟩ := S.exists_add_mem_mem_orthogonal z
    let a : S := ⟨x,hx⟩
    let b : Sᗮ := ⟨y,hy⟩
    change 0 ≤ energy G ((a:H)+(b:H))
    rw [schur_completion S G hG c hc htail a b]
    have hh := htail _ (Sᗮ.add_mem b.property (response S G c hc htail a).property)
    exact add_nonneg (h a) (le_trans (by positivity) hh)

end WeilDefect.MasterRecon.V10B11b

#print axioms WeilDefect.MasterRecon.V10B11b.coercive_norm
#print axioms WeilDefect.MasterRecon.V10B11b.coercive_bijective
#print axioms WeilDefect.MasterRecon.V10B11b.tail_pairing
#print axioms WeilDefect.MasterRecon.V10B11b.cross_pairing
#print axioms WeilDefect.MasterRecon.V10B11b.tail_coercive
#print axioms WeilDefect.MasterRecon.V10B11b.response_eq
#print axioms WeilDefect.MasterRecon.V10B11b.response_pairing
#print axioms WeilDefect.MasterRecon.V10B11b.energy_add
#print axioms WeilDefect.MasterRecon.V10B11b.schur_completion
#print axioms WeilDefect.MasterRecon.V10B11b.positivity_iff_schur
