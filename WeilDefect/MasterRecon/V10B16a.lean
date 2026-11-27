import WeilDefect.MasterRecon.V10B15b

/-! Signed symbol split. Instead of a uniform absolute residual budget,
retain the positive high-frequency contribution and localize the
negative defect to a measurable low-frequency region. -/
namespace WeilDefect.MasterRecon.V10B16a

open MeasureTheory Set Filter
open scoped FourierTransform InnerProduct

theorem signed_split (a w : ℝ → ℝ) (f : ℝ → ℂ) (S : Set ℝ)
    (hS : MeasurableSet S) (c D : ℝ)
    (ha : Integrable (fun u => a u * ‖f u‖^2))
    (hw : Integrable (fun u => w u * ‖f u‖^2))
    (hf : Integrable (fun u => ‖f u‖^2))
    (hlo : ∀ u ∈ S, c*w u-D ≤ a u)
    (hhi : ∀ u ∉ S, c*w u ≤ a u) :
    c*(∫ u, w u*‖f u‖^2)-D*(∫ u in S, ‖f u‖^2) ≤
      ∫ u, a u*‖f u‖^2 := by
  have hI : Integrable (S.indicator (fun u => ‖f u‖^2)) := hf.indicator hS
  have h := integral_mono ((hw.const_mul c).sub (hI.const_mul D)) ha (fun u => by
    change c*(w u*‖f u‖^2)-D*S.indicator (fun u => ‖f u‖^2) u ≤ _
    by_cases hu : u ∈ S
    · rw [Set.indicator_of_mem hu]
      have hh := mul_le_mul_of_nonneg_right (hlo u hu) (sq_nonneg ‖f u‖)
      nlinarith only [hh]
    · rw [Set.indicator_of_notMem hu,mul_zero,sub_zero]
      have hh := mul_le_mul_of_nonneg_right (hhi u hu) (sq_nonneg ‖f u‖)
      nlinarith only [hh])
  change (∫ u, c*(w u*‖f u‖^2)-D*S.indicator (fun u => ‖f u‖^2) u) ≤ _ at h
  rw [integral_sub (hw.const_mul c) (hI.const_mul D),
    integral_const_mul,integral_const_mul,integral_indicator hS] at h
  exact h

theorem localized_coercivity {H : Type*} [NormedAddCommGroup H]
    (Q mass : H → ℝ) (c D ε : ℝ) (hD : 0 ≤ D)
    (hQ : ∀ g, c*‖g‖^2-D*mass g ≤ Q g)
    (g : H) (hm : mass g ≤ ε^2*‖g‖^2) :
    (c-D*ε^2)*‖g‖^2 ≤ Q g := by
  have h := mul_le_mul_of_nonneg_left hm hD
  nlinarith only [h,hQ g]

end WeilDefect.MasterRecon.V10B16a

#print axioms WeilDefect.MasterRecon.V10B16a.signed_split
#print axioms WeilDefect.MasterRecon.V10B16a.localized_coercivity
