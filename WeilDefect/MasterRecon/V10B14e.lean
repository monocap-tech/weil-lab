import WeilDefect.MasterRecon.V10B14b
import WeilDefect.MasterRecon.V10B12c

/-! Finite bank receiver with no linear-independence assumption.
Coverage, tail membership, and retained subtraction are explicit.
The error reserve is for the full Hilbert norm of the approximate action. -/
namespace WeilDefect.MasterRecon.V10B14e

open scoped InnerProduct BigOperators
open V10B12a (energy)
open V10B12c (synth gram matrixForm)

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable {ι : Type*} [Fintype ι]

theorem synth_mem (S : Submodule ℂ H) (b : ι → H)
    (hb : ∀ i, b i ∈ S) (a : ι → ℂ) : synth b a ∈ S := by
  unfold synth
  exact S.sum_mem fun i _ => S.smul_mem _ (hb i)

theorem synth_sub (b z : ι → H) (a : ι → ℂ) :
    synth (fun i => b i-z i) a = synth b a-synth z a := by
  unfold synth
  simp only [smul_sub,Finset.sum_sub_distrib]

theorem synth_action (F : H →L[ℂ] H) (v : ι → H) (a : ι → ℂ) :
    synth (fun i => F (v i)) a = F (synth v a) := by
  unfold synth
  simp only [map_sum,map_smul]

theorem norm_gram (v : ι → H) (a : ι → ℂ) :
    (matrixForm (gram (1:H →L[ℂ] H) v) a).re = ‖synth v a‖^2 := by
  rw [V10B12c.matrixForm_gram,ContinuousLinearMap.one_apply,
    inner_self_eq_norm_sq_to_K,Complex.ofReal_re]

theorem spanning_bank_certificate (G F : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (S : Submodule ℂ H) [S.HasOrthogonalProjection]
    (c : ℝ) (hc : 0 < c)
    (htail : ∀ y ∈ Sᗮ, c*‖y‖^2 ≤ energy G y)
    (δ : ℝ) (hδ : ‖G-F‖ ≤ δ)
    (b z s : ι → H)
    (hz : ∀ i, z i ∈ Sᗮ) (hs : ∀ i, s i ∈ S)
    (hspan : ∀ x ∈ S, ∃ a : ι → ℂ, synth b a = x)
    (hM : ∀ a : ι → ℂ,
      let v : ι → H := fun i => b i-z i
      let r : ι → H := fun i => F (v i)-s i
      0 ≤ (matrixForm (gram F v) a).re -
        δ*(matrixForm (gram (1:H →L[ℂ] H) v) a).re -
        (2*(matrixForm (gram (1:H →L[ℂ] H) r) a).re +
          2*δ^2*(matrixForm (gram (1:H →L[ℂ] H) v) a).re)/c) :
    ∀ g : H, 0 ≤ energy G g := by
  intro g
  obtain ⟨x,hx,y,hy,rfl⟩ := S.exists_add_mem_mem_orthogonal g
  obtain ⟨a,ha⟩ := hspan x hx
  let v := synth (fun i => b i-z i) a
  let w := y+synth z a
  let q := synth s a
  have hw : w ∈ Sᗮ := Sᗮ.add_mem hy (synth_mem Sᗮ z hz a)
  have hq : q ∈ S := synth_mem S s hs a
  have he : v+w = x+y := by
    dsimp [v,w]
    rw [synth_sub,ha]
    abel
  have h := V10B14b.residual_reserve G F hG S c hc htail δ hδ v q w hq hw
  rw [he] at h
  have hm := hM a
  dsimp only at hm
  rw [V10B12c.matrixForm_gram,norm_gram,norm_gram,norm_gram,
    synth_sub (fun i => F (b i-z i)) s a,synth_action] at hm
  exact hm.trans h

end WeilDefect.MasterRecon.V10B14e

#print axioms WeilDefect.MasterRecon.V10B14e.synth_mem
#print axioms WeilDefect.MasterRecon.V10B14e.synth_sub
#print axioms WeilDefect.MasterRecon.V10B14e.synth_action
#print axioms WeilDefect.MasterRecon.V10B14e.norm_gram
#print axioms WeilDefect.MasterRecon.V10B14e.spanning_bank_certificate
