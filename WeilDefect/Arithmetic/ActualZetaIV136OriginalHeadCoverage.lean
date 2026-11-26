import WeilDefect.Arithmetic.ActualZetaIV135OriginalMatrixReceiver
import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap BigOperators

/-- Use a finite family of actual complement tests. Coverage is reduced
to spanning the exact cell-constraint image, not all Schwartz tests. -/
theorem neutralIV136Coverage_of_cells {n : ℕ} (k : ℕ) (hk : 0 < k) (N : ℕ)
    (w : Fin n → neutralIV129Complement k hk)
    (hspan : ∀ v : neutralIV129Complement k hk, ∃ c : Fin n → ℂ,
      neutralIV129RestrictedMap k hk N v =
        ∑ i : Fin n, c i • neutralIV129RestrictedMap k hk N (w i)) :
    ∀ v : neutralIV129Complement k hk, ∃ c : Fin n → ℂ,
      ∃ z : neutralIV131Tail k hk N,
        v.val = neutralIV009PhysicalSchwartzSum (fun i => (w i).val) c + z.val := by
  intro v
  obtain ⟨c,hc⟩ := hspan v
  let u : neutralIV129Complement k hk := ∑ i : Fin n, c i • w i
  have hu : neutralIV129RestrictedMap k hk N u =
      neutralIV129RestrictedMap k hk N v := by
    dsimp [u]
    rw [map_sum]
    simp only [map_smul, ← hc]
  let q : neutralIV129Complement k hk := v-u
  have hq : neutralIV129RestrictedMap k hk N q = 0 := by
    change neutralIV129RestrictedMap k hk N (v-u) = 0
    rw [map_sub,hu,sub_self]
  let z : neutralIV131Tail k hk N := ⟨q.val, by
    change q.val ∈ neutralIV129Complement k hk ∧
      q.val ∈ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N)
    exact ⟨q.property,LinearMap.mem_ker.mpr hq⟩⟩
  have hval : u.val = neutralIV009PhysicalSchwartzSum (fun i => (w i).val) c := by
    change (neutralIV129Complement k hk).subtype u = _
    unfold u neutralIV009PhysicalSchwartzSum
    rw [map_sum]
    simp only [map_smul, Submodule.subtype_apply]
  refine ⟨c,z,?_⟩
  change v.val = _ + (v.val-u.val)
  rw [← hval]
  abel

/-- A basis of the actual finite constraint image gives spanning cells
for any exact linear section, after arbitrary tail corrections. -/
theorem neutralIV136Section_basis_spans (k : ℕ) (hk : 0 < k) (N : ℕ)
    (H : LinearMap.range (neutralIV129RestrictedMap k hk N) →ₗ[ℂ]
      neutralIV129Complement k hk)
    (hH : (neutralIV129RestrictedMap k hk N).rangeRestrict.comp H = LinearMap.id)
    (n : ℕ)
    (b : Module.Basis (Fin n) ℂ (LinearMap.range (neutralIV129RestrictedMap k hk N)))
    (t : Fin n → neutralIV131Tail k hk N) :
    ∃ w : Fin n → neutralIV129Complement k hk,
      (∀ i, (w i).val = (H (b i)).val + (t i).val) ∧
      (∀ v : neutralIV129Complement k hk, ∃ c : Fin n → ℂ,
        neutralIV129RestrictedMap k hk N v =
          ∑ i : Fin n, c i • neutralIV129RestrictedMap k hk N (w i)) := by
  let L := neutralIV129RestrictedMap k hk N
  let e : Fin n → neutralIV129Complement k hk := fun i => ⟨(t i).val, (t i).property.1⟩
  let w : Fin n → neutralIV129Complement k hk := fun i => H (b i)+e i
  refine ⟨w,fun i => rfl,?_⟩
  intro v
  let y := L.rangeRestrict v
  let c : Fin n → ℂ := fun i => b.repr y i
  have hb : ∑ i : Fin n, c i • b i = y := b.sum_repr y
  have hw (i : Fin n) : L (w i) = (b i).val := by
    have he : L (e i) = 0 := LinearMap.mem_ker.mp (t i).property.2
    have hB : L.rangeRestrict (H (b i)) = b i :=
      LinearMap.congr_fun hH (b i)
    change L (H (b i)+e i) = _
    rw [map_add,he,add_zero]
    exact congrArg Subtype.val hB
  refine ⟨c,?_⟩
  change L v = ∑ i : Fin n, c i • L (w i)
  simp_rw [hw]
  have hs := congrArg (LinearMap.range L).subtype hb
  rw [map_sum] at hs
  simp only [map_smul,Submodule.subtype_apply] at hs
  exact hs.symm

/-- Noncomputable finite head existence with exact coverage; this does
not supply numerically usable basis functions or an effective cutoff. -/
theorem neutralIV136Finite_cover_exists (k : ℕ) (hk : 0 < k) (N : ℕ) :
    ∃ n : ℕ, n ≤ N ∧ ∃ w : Fin n → neutralIV129Complement k hk,
      ∀ v : neutralIV129Complement k hk, ∃ c : Fin n → ℂ,
        ∃ z : neutralIV131Tail k hk N,
          v.val = neutralIV009PhysicalSchwartzSum (fun i => (w i).val) c + z.val := by
  obtain ⟨H,hH⟩ := neutralIV129Section_exists k hk N
  let Y := LinearMap.range (neutralIV129RestrictedMap k hk N)
  let n := Module.finrank ℂ Y
  let b := Module.finBasis ℂ Y
  obtain ⟨w,_,hw⟩ := neutralIV136Section_basis_spans k hk N H hH n b
    (fun _ => 0)
  exact ⟨n,neutralIV129Head_dim_le k hk N,w,
    neutralIV136Coverage_of_cells k hk N w hw⟩

#print axioms neutralIV136Coverage_of_cells
#print axioms neutralIV136Section_basis_spans
#print axioms neutralIV136Finite_cover_exists

end
end WeilDefect
