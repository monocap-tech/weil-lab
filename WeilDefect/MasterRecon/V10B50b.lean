import WeilDefect.MasterRecon.V10B50a

/-! V10B50b: affine physical support substitution and reversible row
operations. The actual polynomial row expansions are a separate input. -/
namespace WeilDefect.MasterRecon.V10B50b
open MeasureTheory Set
open scoped BigOperators

theorem affine_support_integral (F : ℝ → ℂ) :
    (∫ x in Icc (-1/4:ℝ) (1/4), F (2*x+1/2)) =
      (1/2:ℝ) • (∫ z in (0:ℝ)..1, F z) := by
  rw [integral_Icc_eq_integral_Ioc,← intervalIntegral.integral_of_le (by norm_num)]
  let G : ℝ → ℂ := fun y => F (y+1/2)
  change (∫ x in (-1/4:ℝ)..(1/4), G (2*x)) = _
  rw [intervalIntegral.integral_comp_mul_left G (by norm_num : (2:ℝ) ≠ 0)]
  norm_num only [show (2:ℝ)*(-1/4) = -1/2 by norm_num,
    show (2:ℝ)*(1/4) = 1/2 by norm_num,
    show (2:ℝ)⁻¹=1/2 by norm_num]
  unfold G
  rw [intervalIntegral.integral_comp_add_right]
  norm_num

theorem reversible_rows {ι : Type*} [Fintype ι]
    (m l : ι → ℂ) (p q s : ℂ) (T U : ι → ι → ℂ)
    (b : ι → ℂ) (r : ι → ℂ)
    (hT : ∀ i, l i = ∑ j, T i j*m j)
    (hU : ∀ i, m i = ∑ j, U i j*l j)
    (hq : q = s*(p-∑ j, b j*l j))
    (hs : s ≠ 0) (hr : ∀ i, r i ≠ 0) :
    ((∀ i, m i=0) ∧ p=0) ↔ ((∀ i, r i*l i=0) ∧ q=0) := by
  constructor
  · rintro ⟨hm,hp⟩
    have hl : ∀ i, l i=0 := by
      intro i
      simp [hT i,hm]
    simp [hl,hp,hq]
  · rintro ⟨hl,hq0⟩
    have hz : ∀ i, l i=0 := fun i => (mul_eq_zero.mp (hl i)).resolve_left (hr i)
    constructor
    · intro i
      simp [hU i,hz]
    · rw [hq] at hq0
      have h := (mul_eq_zero.mp hq0).resolve_left hs
      simpa [hz] using h

end WeilDefect.MasterRecon.V10B50b

#print axioms WeilDefect.MasterRecon.V10B50b.affine_support_integral
#print axioms WeilDefect.MasterRecon.V10B50b.reversible_rows
