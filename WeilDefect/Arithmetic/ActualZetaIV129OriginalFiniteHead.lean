import WeilDefect.Arithmetic.ActualZetaIV128OriginalTailCutoffs
import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap BigOperators

/-- The actual supported physical packed complement, not an enlarged
space of arbitrary L2 representatives. -/
def neutralIV129Complement (k : ℕ) (hk : 0 < k) :
    Submodule ℂ (𝓢(ℝ,ℂ)) where
  carrier := {v | (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) ∧
    neutralIV101MassComplement k hk v}
  zero_mem' := by
    constructor
    · intro x hx
      simp
    · intro c
      change inner ℂ ((neutralIV100Packed k hk c).toLp 2 volume)
        ((SchwartzMap.toLpCLM ℂ ℂ 2 volume) 0) = 0
      rw [map_zero, inner_zero_right]
  add_mem' := by
    intro u v hu hv
    constructor
    · intro x hx
      change u x + v x = 0
      rw [hu.1 x hx, hv.1 x hx, add_zero]
    · intro c
      change inner ℂ ((neutralIV100Packed k hk c).toLp 2 volume)
        ((SchwartzMap.toLpCLM ℂ ℂ 2 volume) (u+v)) = 0
      rw [map_add, inner_add_right]
      change inner ℂ ((neutralIV100Packed k hk c).toLp 2 volume) (u.toLp 2 volume) +
        inner ℂ ((neutralIV100Packed k hk c).toLp 2 volume) (v.toLp 2 volume) = 0
      rw [hu.2 c, hv.2 c, add_zero]
  smul_mem' := by
    intro c v hv
    constructor
    · intro x hx
      change c • v x = 0
      rw [hv.1 x hx, smul_zero]
    · intro d
      change inner ℂ ((neutralIV100Packed k hk d).toLp 2 volume)
        ((SchwartzMap.toLpCLM ℂ ℂ 2 volume) (c • v)) = 0
      rw [map_smul, inner_smul_right]
      change c * inner ℂ ((neutralIV100Packed k hk d).toLp 2 volume)
        (v.toLp 2 volume) = 0
      rw [hv.2 d, mul_zero]

/-- Finite coordinate map of literal physical cell means. -/
def neutralIV129CellMap (a : ℝ) (N : ℕ) :
    (𝓢(ℝ,ℂ)) →ₗ[ℂ] (Fin N → ℂ) where
  toFun v j := ∫ x in Set.Ioc (neutralIV126Node (-a) (2*a/(N:ℝ)) j.val)
      (neutralIV126Node (-a) (2*a/(N:ℝ)) (j.val+1)), v x
  map_add' := by
    intro u v
    funext j
    change (∫ x in Set.Ioc (neutralIV126Node (-a) (2*a/(N:ℝ)) j.val)
      (neutralIV126Node (-a) (2*a/(N:ℝ)) (j.val+1)), u x+v x) = _
    exact integral_add u.integrable.integrableOn v.integrable.integrableOn
  map_smul' := by
    intro c v
    funext j
    change (∫ x in Set.Ioc (neutralIV126Node (-a) (2*a/(N:ℝ)) j.val)
      (neutralIV126Node (-a) (2*a/(N:ℝ)) (j.val+1)), c • v x) = _
    exact integral_smul c _

theorem neutralIV129CellMap_zero_iff (a : ℝ) (N : ℕ) (v : 𝓢(ℝ,ℂ)) :
    neutralIV129CellMap a N v = 0 ↔ neutralIV127CellNull a N v := by
  constructor
  · intro h j hj
    exact congrFun h ⟨j,hj⟩
  · intro h
    funext j
    exact h j.val j.isLt

def neutralIV129RestrictedMap (k : ℕ) (hk : 0 < k) (N : ℕ) :
    neutralIV129Complement k hk →ₗ[ℂ] (Fin N → ℂ) :=
  (neutralIV129CellMap (11/10:ℝ) N).comp (neutralIV129Complement k hk).subtype

/-- Use the actual image as head coordinates. No surjectivity onto
all N coordinates or independence of the constraints is presumed. -/
theorem neutralIV129Head_dim_le (k : ℕ) (hk : 0 < k) (N : ℕ) :
    Module.finrank ℂ (LinearMap.range (neutralIV129RestrictedMap k hk N)) ≤ N := by
  calc
    _ ≤ Module.finrank ℂ (Fin N → ℂ) := Submodule.finrank_le _
    _ = N := by simp

/-- A linear section on the actual image always exists. -/
theorem neutralIV129Section_exists (k : ℕ) (hk : 0 < k) (N : ℕ) :
    ∃ H : LinearMap.range (neutralIV129RestrictedMap k hk N) →ₗ[ℂ]
      neutralIV129Complement k hk,
      (neutralIV129RestrictedMap k hk N).rangeRestrict.comp H = LinearMap.id :=
  (neutralIV129RestrictedMap k hk N).rangeRestrict.exists_rightInverse_of_surjective
    (LinearMap.range_rangeRestrict _)

/-- Every original packed-complement vector has a head with its exact
constraints and a cell-null remainder, with both still in the complement. -/
theorem neutralIV129Head_tail (k : ℕ) (hk : 0 < k) (N : ℕ)
    (H : LinearMap.range (neutralIV129RestrictedMap k hk N) →ₗ[ℂ]
      neutralIV129Complement k hk)
    (hH : (neutralIV129RestrictedMap k hk N).rangeRestrict.comp H = LinearMap.id)
    (v : neutralIV129Complement k hk) :
    ∃ z : neutralIV129Complement k hk,
      v = H ((neutralIV129RestrictedMap k hk N).rangeRestrict v) + z ∧
      neutralIV127CellNull (11/10:ℝ) N z.val := by
  let L := neutralIV129RestrictedMap k hk N
  let h := H (L.rangeRestrict v)
  let z := v-h
  have he : L.rangeRestrict h = L.rangeRestrict v := by
    exact LinearMap.congr_fun hH (L.rangeRestrict v)
  have hz : L.rangeRestrict z = 0 := by
    change L.rangeRestrict (v-h) = 0
    rw [map_sub, he, sub_self]
  have hz' : L z = 0 := by
    exact congrArg Subtype.val hz
  refine ⟨z, ?_, (neutralIV129CellMap_zero_iff _ N z.val).1 hz'⟩
  change v = h + (v-h)
  abel

/-- A single finite head and coercive tail work for every vector in the
original supported packed complement, at any prescribed positive margin. -/
theorem neutralIV129Coercive_split (k : ℕ) (hk : 0 < k) (eta : ℝ) :
    ∃ N : ℕ, 0 < N ∧
      ∃ H : LinearMap.range (neutralIV129RestrictedMap k hk N) →ₗ[ℂ]
        neutralIV129Complement k hk,
        (neutralIV129RestrictedMap k hk N).rangeRestrict.comp H = LinearMap.id ∧
        ∀ v : neutralIV129Complement k hk,
          ∃ z : neutralIV129Complement k hk,
            v = H ((neutralIV129RestrictedMap k hk N).rangeRestrict v) + z ∧
            neutralIV127CellNull (11/10:ℝ) N z.val ∧
            eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val := by
  obtain ⟨N,hN,hcoerc⟩ := neutralIV128Schur_coercive_tail_exists k hk eta
  obtain ⟨H,hH⟩ := neutralIV129Section_exists k hk N
  refine ⟨N,hN,H,hH,?_⟩
  intro v
  obtain ⟨z,hz,hnull⟩ := neutralIV129Head_tail k hk N H hH v
  exact ⟨z,hz,hnull,hcoerc z.val z.property.1 hnull⟩

#print axioms neutralIV129CellMap_zero_iff
#print axioms neutralIV129Head_dim_le
#print axioms neutralIV129Section_exists
#print axioms neutralIV129Head_tail
#print axioms neutralIV129Coercive_split

end
end WeilDefect
