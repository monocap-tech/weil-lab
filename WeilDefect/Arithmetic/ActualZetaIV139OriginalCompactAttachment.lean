import WeilDefect.Arithmetic.ActualZetaIV138OriginalRadiusCompression
import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap FourierTransform ComplexConjugate BigOperators

/-- The actual signed radius-two multiplier without its pole term.
No identification with a numerical comparison matrix is presumed. -/
def neutralIV139PoleFree (v : 𝓢(ℝ,ℂ)) : ℝ :=
  (∫ ξ : ℝ, conj ((𝓕 (v.toLp 2 volume) : RealComplexL2) ξ) *
    (rightLimitCompactWeilSymbolMathlib 2 ξ : ℂ) *
    (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ).re

theorem neutralIV139PoleFree_eq (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(2:ℝ)) 2 → v x = 0)
    (hp : sourceWindowMoment 2 (1/2) (v.toLp 2 volume) = 0)
    (hm : sourceWindowMoment 2 (-(1/2)) (v.toLp 2 volume) = 0) :
    neutralIV101Q 2 v = neutralIV139PoleFree v := by
  unfold neutralIV101Q neutralIV139PoleFree
  rw [neutralIV123Original_mixed 2 (by norm_num) v v hv hv]
  simp [neutralIV123EvenMoment, neutralIV123OddMoment, hp, hm]

/-- Exact rows for a supplied compact physical bank, both original pole
moments, and the signed packed cross constraints. No cell rows. -/
def neutralIV139Bank {n : ℕ} (k : ℕ) (hk : 0 < k)
    (F : Fin n → RealComplexL2) : (Fin n ⊕ (Fin 2 ⊕ Fin k)) → RealComplexL2 :=
  Sum.elim F (Sum.elim
    (fun j => if j.val = 0 then neutralMomentColumnL2 2 (1/2)
      else neutralMomentColumnL2 2 (-(1/2)))
    (fun i => neutralIV133PhysicalRow (11/10:ℝ) (neutralIV100Carrier k hk i)))

/-- Physical constraint evaluation on the original Schwartz space. -/
def neutralIV139Map {n : ℕ} (k : ℕ) (hk : 0 < k)
    (F : Fin n → RealComplexL2) :
    (𝓢(ℝ,ℂ)) →ₗ[ℂ] ((Fin n ⊕ (Fin 2 ⊕ Fin k)) → ℂ) where
  toFun v i := inner ℂ (neutralIV139Bank k hk F i) (v.toLp 2 volume)
  map_add' := by
    intro u v
    funext i
    change inner ℂ (neutralIV139Bank k hk F i)
      ((SchwartzMap.toLpCLM ℂ ℂ 2 volume) (u+v)) = _
    rw [map_add, inner_add_right]
    rfl
  map_smul' := by
    intro c v
    funext i
    change inner ℂ (neutralIV139Bank k hk F i)
      ((SchwartzMap.toLpCLM ℂ ℂ 2 volume) (c • v)) = _
    rw [map_smul, inner_smul_right]
    rfl

def neutralIV139Tail {n : ℕ} (k : ℕ) (hk : 0 < k)
    (F : Fin n → RealComplexL2) : Submodule ℂ (𝓢(ℝ,ℂ)) :=
  neutralIV129Complement k hk ⊓ LinearMap.ker (neutralIV139Map k hk F)

theorem neutralIV139Constraints {n : ℕ} (k : ℕ) (hk : 0 < k)
    (F : Fin n → RealComplexL2) (z : neutralIV139Tail k hk F) :
    (∀ i : Fin n, inner ℂ (F i) (z.val.toLp 2 volume) = 0) ∧
    sourceWindowMoment 2 (1/2) (z.val.toLp 2 volume) = 0 ∧
    sourceWindowMoment 2 (-(1/2)) (z.val.toLp 2 volume) = 0 ∧
    neutralIV106CrossRHS k hk z.val = 0 := by
  have hz := z.property
  change z.val ∈ neutralIV129Complement k hk ∧
    z.val ∈ LinearMap.ker (neutralIV139Map k hk F) at hz
  have h0 := LinearMap.mem_ker.mp hz.2
  have hp := congrFun h0 (Sum.inr (Sum.inl (0 : Fin 2)))
  have hm := congrFun h0 (Sum.inr (Sum.inl (1 : Fin 2)))
  refine ⟨?_,?_,?_,?_⟩
  · intro i
    exact congrFun h0 (Sum.inl i)
  · simpa [neutralIV139Map, neutralIV139Bank, neutralMomentColumnL2_inner] using hp
  · simpa [neutralIV139Map, neutralIV139Bank, neutralMomentColumnL2_inner] using hm
  · apply (neutralIV138CrossRows_iff k hk z.val hz.1.1).2
    intro i
    exact congrFun h0 (Sum.inr (Sum.inr i))

/-- The supplied compact bank's actual constraint image has dimension
at most n+2+k. This is not a claim of full rank. -/
theorem neutralIV139Head_dim_le {n : ℕ} (k : ℕ) (hk : 0 < k)
    (F : Fin n → RealComplexL2) :
    Module.finrank ℂ (LinearMap.range
      ((neutralIV139Map k hk F).comp (neutralIV129Complement k hk).subtype)) ≤
      n+2+k := by
  calc
    _ ≤ Module.finrank ℂ ((Fin n ⊕ (Fin 2 ⊕ Fin k)) → ℂ) := Submodule.finrank_le _
    _ = n+2+k := by simp [Nat.add_assoc]

/-- Receive an independently proved radius-two compact comparison on
the actual original pole-null tests. The premise is the missing analytic
and numerical attachment, not a theorem proved by this module. -/
theorem neutralIV139Tail_of_compact {n : ℕ} (k : ℕ) (hk : 0 < k)
    (F : Fin n → RealComplexL2) (eta : ℝ)
    (hc : ∀ v : 𝓢(ℝ,ℂ),
      (∀ x : ℝ, x ∉ Set.Icc (-(2:ℝ)) 2 → v x = 0) →
      (∀ i : Fin n, inner ℂ (F i) (v.toLp 2 volume) = 0) →
      sourceWindowMoment 2 (1/2) (v.toLp 2 volume) = 0 →
      sourceWindowMoment 2 (-(1/2)) (v.toLp 2 volume) = 0 →
      eta*‖v.toLp 2 volume‖^2 ≤ neutralIV139PoleFree v)
    (z : neutralIV139Tail k hk F) :
    eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val := by
  have hz := z.property
  change z.val ∈ neutralIV129Complement k hk ∧
    z.val ∈ LinearMap.ker (neutralIV139Map k hk F) at hz
  have hv := hz.1.1
  have hb : ∀ x : ℝ, x ∉ Set.Icc (-(2:ℝ)) 2 → z.val x = 0 := by
    intro x hx
    apply hv x
    intro h
    apply hx
    exact ⟨by linarith [h.1], by linarith [h.2]⟩
  obtain ⟨hF,hp,hm,hcross⟩ := neutralIV139Constraints k hk F z
  rw [neutralIV138Schur_crossNull k hk z.val hcross,
    neutralIV138Q_radius _ 2 (by norm_num) (by norm_num) z.val hv,
    neutralIV139PoleFree_eq z.val hb hp hm]
  exact hc z.val hb hF hp hm

#print axioms neutralIV139PoleFree_eq
#print axioms neutralIV139Constraints
#print axioms neutralIV139Head_dim_le
#print axioms neutralIV139Tail_of_compact

end
end WeilDefect
