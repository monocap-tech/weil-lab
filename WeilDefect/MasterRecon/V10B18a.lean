import WeilDefect.MasterRecon.V10B12b
import WeilDefect.MasterRecon.V10B12c

/-! Constraint-coordinate certificate. Exact Riesz representers and
orthogonal trial corrections are unnecessary if the constraint map has
a certified finite right section. Residuals are measured in the physical
norm on the entire support, via their exact pairing with all tail tests. -/
namespace WeilDefect.MasterRecon.V10B18a

open scoped InnerProduct BigOperators
open V10B12a (energy)
open V10B12c (synth gram matrixForm)

variable {H E F : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E]
variable [NormedAddCommGroup F] [NormedSpace ℂ F]
variable {ι : Type*} [Fintype ι]

theorem constraint_coverage (L : H →L[ℂ] F) (v : ι → H)
    (hcover : ∀ g : H, ∃ a : ι → ℂ, L (synth v a) = L g) :
    ∀ g : H, ∃ a : ι → ℂ, g-synth v a ∈ L.ker := by
  intro g
  obtain ⟨a,ha⟩ := hcover g
  refine ⟨a,?_⟩
  change L (g-synth v a) = 0
  rw [map_sub,ha,sub_self]

theorem physical_trial_lower (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (T : Submodule ℂ H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ w ∈ T, c*‖w‖^2 ≤ energy G w)
    (J : H →L[ℂ] E) (d : ℝ) (hd : 0 ≤ d)
    (hJ : ∀ w, ‖J w‖ ≤ d*‖w‖)
    (v : H) (r : E)
    (hpair : ∀ w ∈ T, inner ℂ (G v) w = inner ℂ r (J w))
    (w : H) (hw : w ∈ T) :
    energy G v-(d*‖r‖)^2/c ≤ energy G (v+w) := by
  have hn := (norm_inner_le_norm (𝕜 := ℂ) r (J w)).trans
    (mul_le_mul_of_nonneg_left (hJ w) (norm_nonneg r))
  have hr := Complex.abs_re_le_norm (inner ℂ r (J w))
  have hl := neg_abs_le (inner ℂ r (J w)).re
  have hs := V10B12b.square_reserve c (d*‖r‖) ‖w‖ hc
  rw [V10B12b.energy_add G hG,hpair w hw]
  nlinarith only [hn,hr,hl,hs,htail w hw]

theorem physical_bank_certificate (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (T : Submodule ℂ H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ w ∈ T, c*‖w‖^2 ≤ energy G w)
    (J : H →L[ℂ] E) (d : ℝ) (hd : 0 ≤ d)
    (hJ : ∀ w, ‖J w‖ ≤ d*‖w‖)
    (v : ι → H) (r : ι → E)
    (hcover : ∀ g : H, ∃ a : ι → ℂ, g-synth v a ∈ T)
    (hpair : ∀ i w, w ∈ T → inner ℂ (G (v i)) w = inner ℂ (r i) (J w))
    (hM : ∀ a : ι → ℂ, (d*‖synth r a‖)^2/c ≤ energy G (synth v a)) :
    ∀ g : H, 0 ≤ energy G g := by
  intro g
  obtain ⟨a,ha⟩ := hcover g
  let z := synth v a
  have hp : ∀ w ∈ T, inner ℂ (G z) w = inner ℂ (synth r a) (J w) := by
    intro w hw
    dsimp [z,synth]
    simp only [map_sum,map_smul,sum_inner,inner_smul_left,hpair _ w hw]
  have hh := physical_trial_lower G hG T c hc htail J d hd hJ z (synth r a)
    hp (g-z) ha
  rw [show z+(g-z)=g by abel] at hh
  exact (sub_nonneg.mpr (hM a)).trans hh

theorem physical_matrix_certificate (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (T : Submodule ℂ H) (c : ℝ) (hc : 0 < c)
    (htail : ∀ w ∈ T, c*‖w‖^2 ≤ energy G w)
    (J : H →L[ℂ] E) (d : ℝ) (hd : 0 ≤ d)
    (hJ : ∀ w, ‖J w‖ ≤ d*‖w‖)
    (v : ι → H) (r : ι → E)
    (hcover : ∀ g : H, ∃ a : ι → ℂ, g-synth v a ∈ T)
    (hpair : ∀ i w, w ∈ T → inner ℂ (G (v i)) w = inner ℂ (r i) (J w))
    (hM : ∀ a : ι → ℂ,
      (d^2/c)*(matrixForm (gram (1:E →L[ℂ] E) r) a).re ≤
        (matrixForm (gram G v) a).re) :
    ∀ g : H, 0 ≤ energy G g := by
  apply physical_bank_certificate G hG T c hc htail J d hd hJ v r hcover hpair
  intro a
  have h := hM a
  rw [V10B12c.matrixForm_gram,V10B12c.matrixForm_gram,
    ContinuousLinearMap.one_apply] at h
  have hn : (inner ℂ (synth r a) (synth r a)).re = ‖synth r a‖^2 :=
    inner_self_eq_norm_sq (𝕜 := ℂ) _
  rw [hn] at h
  unfold energy
  calc
    _ = (d^2/c)*‖synth r a‖^2 := by ring
    _ ≤ _ := h

end WeilDefect.MasterRecon.V10B18a

#print axioms WeilDefect.MasterRecon.V10B18a.constraint_coverage
#print axioms WeilDefect.MasterRecon.V10B18a.physical_trial_lower
#print axioms WeilDefect.MasterRecon.V10B18a.physical_bank_certificate
#print axioms WeilDefect.MasterRecon.V10B18a.physical_matrix_certificate
