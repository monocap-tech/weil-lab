import WeilDefect.MasterRecon.V10B14c
import WeilDefect.MasterRecon.V10B14e
import WeilDefect.MasterRecon.V10B13b

/-! The finite compressed approximation acts as the identity on its
moment-annihilating tail. A strict margin on the retained bank plus a
global operator-error enclosure suffices; no inverse solve is needed.
This is a sufficient test, not an equivalence for the original operator. -/
namespace WeilDefect.MasterRecon.V10B15c

open scoped InnerProduct
open V10B12a (energy)
open V10B12c (gram matrixForm synth)
open V10B14c (pullback)

variable {H E : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]

theorem compressed_energy (P : H →L[ℂ] E) (B : E →L[ℂ] E) (x : H) :
    energy (1+pullback P B) x = ‖x‖^2+(inner ℂ (B (P x)) (P x)).re := by
  unfold energy pullback
  rw [ContinuousLinearMap.add_apply,ContinuousLinearMap.one_apply,inner_add_left,
    Complex.add_re,inner_self_eq_norm_sq_to_K,Complex.ofReal_re]
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]

theorem compressed_split (P : H →L[ℂ] E) (B : E →L[ℂ] E)
    (S : Submodule ℂ H) (x y : H) (hx : x ∈ S) (hy : y ∈ Sᗮ)
    (hP : P y = 0) :
    energy (1+pullback P B) (x+y) =
      energy (1+pullback P B) x+‖y‖^2 := by
  rw [compressed_energy,compressed_energy,map_add,hP,add_zero]
  have ho : inner ℂ x y = 0 := hy x hx
  rw [norm_add_sq_eq_norm_sq_add_norm_sq_of_inner_eq_zero x y ho]
  ring

theorem direct_certificate (G : H →L[ℂ] H) (P : H →L[ℂ] E)
    (B : E →L[ℂ] E) (S : Submodule ℂ H) [S.HasOrthogonalProjection]
    (δ : ℝ) (hδ : δ ≤ 1) (herr : ‖G-(1+pullback P B)‖ ≤ δ)
    (hP : ∀ y ∈ Sᗮ, P y = 0)
    (hS : ∀ x ∈ S, δ*‖x‖^2 ≤ energy (1+pullback P B) x) :
    ∀ g : H, 0 ≤ energy G g := by
  intro g
  obtain ⟨x,hx,y,hy,rfl⟩ := S.exists_add_mem_mem_orthogonal g
  have h := V10B14b.approximate_energy G (1+pullback P B) δ herr (x+y)
  rw [compressed_split P B S x y hx hy (hP y hy),
    norm_add_sq_eq_norm_sq_add_norm_sq_of_inner_eq_zero x y (hy x hx)] at h
  have hh := mul_nonneg (sub_nonneg.mpr hδ) (sq_nonneg ‖y‖)
  nlinarith only [h,hS x hx,hh]

theorem direct_bank_certificate {ι : Type*} [Fintype ι]
    (G : H →L[ℂ] H) (P : H →L[ℂ] E) (B : E →L[ℂ] E)
    (S : Submodule ℂ H) [S.HasOrthogonalProjection]
    (δ : ℝ) (hδ : δ ≤ 1) (herr : ‖G-(1+pullback P B)‖ ≤ δ)
    (hP : ∀ y ∈ Sᗮ, P y = 0)
    (b : ι → H) (hspan : ∀ x ∈ S, ∃ a : ι → ℂ, synth b a = x)
    (hM : ∀ a : ι → ℂ,
      δ*(matrixForm (gram (1:H →L[ℂ] H) b) a).re ≤
        (matrixForm (gram (1+pullback P B) b) a).re) :
    ∀ g : H, 0 ≤ energy G g := by
  apply direct_certificate G P B S δ hδ herr hP
  intro x hx
  obtain ⟨a,ha⟩ := hspan x hx
  have h := hM a
  rw [V10B14e.norm_gram,V10B12c.matrixForm_gram,ha] at h
  exact h

theorem moment_tail_zero (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (g : V08I.logCarrier t) (hg : g ∈ (V10B13b.retained t ht n)ᗮ) :
    V10B13a.approximation t R ht hR n g = 0 :=
  V10B13a.approximation_zero t R ht hR n g
    (fun j hj => V10B13b.retained_moment_zero t ht n g hg j hj)

end WeilDefect.MasterRecon.V10B15c

#print axioms WeilDefect.MasterRecon.V10B15c.compressed_energy
#print axioms WeilDefect.MasterRecon.V10B15c.compressed_split
#print axioms WeilDefect.MasterRecon.V10B15c.direct_certificate
#print axioms WeilDefect.MasterRecon.V10B15c.direct_bank_certificate
#print axioms WeilDefect.MasterRecon.V10B15c.moment_tail_zero
