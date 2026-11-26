import WeilDefect.Arithmetic.ActualZetaIV131OriginalVariationalSchur
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

theorem neutralIV132Tail_supported (k : ℕ) (hk : 0 < k) (N : ℕ)
    (z : neutralIV131Tail k hk N) :
    ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z.val x = 0 := by
  have hz := z.property
  change z.val ∈ neutralIV129Complement k hk ∧
    z.val ∈ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N) at hz
  exact hz.1.1

/-- Exact all-fibre sign criterion on the finite constraint image.
No claim that the variational penalty has already been evaluated. -/
theorem neutralIV132Head_iff (k : ℕ) (hk : 0 < k) (N : ℕ)
    (H : LinearMap.range (neutralIV129RestrictedMap k hk N) →ₗ[ℂ]
      neutralIV129Complement k hk)
    (hH : (neutralIV129RestrictedMap k hk N).rangeRestrict.comp H = LinearMap.id)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : neutralIV131Tail k hk N,
      eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val) :
    (∀ v : neutralIV129Complement k hk, 0 ≤ neutralIV107SchurEnergy k hk v.val) ↔
    (∀ y : LinearMap.range (neutralIV129RestrictedMap k hk N),
      neutralIV131Penalty k hk (neutralIV131Tail k hk N) (H y).val ≤
        neutralIV107SchurEnergy k hk (H y).val) := by
  constructor
  · intro hp y
    apply (neutralIV131Fibre_iff k hk (neutralIV131Tail k hk N)
      (H y).val (H y).property.1 (neutralIV132Tail_supported k hk N) eta he hc).1
    intro z
    have hz := z.property
    change z.val ∈ neutralIV129Complement k hk ∧
      z.val ∈ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N) at hz
    exact hp ⟨(H y).val+z.val, (neutralIV129Complement k hk).add_mem
      (H y).property hz.1⟩
  · intro hp v
    obtain ⟨z,hz,hn⟩ := neutralIV129Head_tail k hk N H hH v
    let t : neutralIV131Tail k hk N := ⟨z.val, by
      change z.val ∈ neutralIV129Complement k hk ∧
        z.val ∈ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N)
      exact ⟨z.property, LinearMap.mem_ker.mpr
        ((neutralIV129CellMap_zero_iff _ N z.val).2 hn)⟩⟩
    let y := (neutralIV129RestrictedMap k hk N).rangeRestrict v
    have hs := (neutralIV131Fibre_iff k hk (neutralIV131Tail k hk N)
      (H y).val (H y).property.1 (neutralIV132Tail_supported k hk N) eta he hc).2
      (hp y) t
    have hv : v.val = (H y).val + t.val := congrArg Subtype.val hz
    rw [hv]
    exact hs

/-- Receive the finite-image comparison into literal original window positivity. -/
theorem neutralIV132Window_of_head (k : ℕ) (hk : 0 < k) (N : ℕ)
    (H : LinearMap.range (neutralIV129RestrictedMap k hk N) →ₗ[ℂ]
      neutralIV129Complement k hk)
    (hH : (neutralIV129RestrictedMap k hk N).rangeRestrict.comp H = LinearMap.id)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : neutralIV131Tail k hk N,
      eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val)
    (hp : ∀ y : LinearMap.range (neutralIV129RestrictedMap k hk N),
      neutralIV131Penalty k hk (neutralIV131Tail k hk N) (H y).val ≤
        neutralIV107SchurEnergy k hk (H y).val)
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) :
    0 ≤ neutralIV101Q (11/10:ℝ) s := by
  apply neutralIV107Window_nonneg_of_schur k hk _ s hs
  intro v horth hv
  exact (neutralIV132Head_iff k hk N H hH eta he hc).2 hp ⟨v,hv,horth⟩

/-- Corrected rows are additive in the second slot. -/
theorem neutralIV132Mixed_add_right (k : ℕ) (hk : 0 < k) (h y z : 𝓢(ℝ,ℂ))
    (hy : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → y x = 0)
    (hz : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z x = 0) :
    neutralIV130Mixed k hk h (y+z) =
      neutralIV130Mixed k hk h y + neutralIV130Mixed k hk h z := by
  have hsum : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → (y+z) x = 0 := by
    intro x hx
    change y x+z x = 0
    rw [hy x hx,hz x hx,add_zero]
  rw [neutralIV130Mixed_row k hk h (y+z) hsum,
    neutralIV130Mixed_row k hk h y hy, neutralIV130Mixed_row k hk h z hz,
    neutralIV130Mixed_add_right _ _ y z hy hz]

/-- Corrected first-slot additivity from Hermitian symmetry and right additivity. -/
theorem neutralIV132Mixed_hermitian (k : ℕ) (hk : 0 < k) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    star (neutralIV130Mixed k hk u v) = neutralIV130Mixed k hk v u := by
  unfold neutralIV130Mixed
  change conj (neutralIV101Mixed (11/10:ℝ) u v -
    neutralIV101Mixed (11/10:ℝ) (neutralIV130ResponseVector k hk u)
      (neutralIV130ResponseVector k hk v)) = _
  rw [map_sub, neutralIV130Mixed_hermitian _ u v hu hv,
    neutralIV130Mixed_hermitian _ _ _
      (neutralIV130Response_supported k hk u) (neutralIV130Response_supported k hk v)]

theorem neutralIV132Mixed_add_left (k : ℕ) (hk : 0 < k) (h y z : 𝓢(ℝ,ℂ))
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hy : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → y x = 0)
    (hz : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z x = 0) :
    neutralIV130Mixed k hk (h+y) z =
      neutralIV130Mixed k hk h z + neutralIV130Mixed k hk y z := by
  have hsum : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → (h+y) x = 0 := by
    intro x hx
    change h x+y x = 0
    rw [hh x hx,hy x hx,add_zero]
  rw [← neutralIV132Mixed_hermitian k hk z (h+y) hz hsum,
    neutralIV132Mixed_add_right k hk z h y hh hy, star_add,
    neutralIV132Mixed_hermitian k hk z h hz hh,
    neutralIV132Mixed_hermitian k hk z y hz hy]

/-- Shift a trial response in the genuine tail; exact loss identity. -/
theorem neutralIV132Loss_shift (k : ℕ) (hk : 0 < k) (h y z : 𝓢(ℝ,ℂ))
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hy : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → y x = 0)
    (hz : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z x = 0) :
    neutralIV131Loss k hk h (y+z) =
      neutralIV131Loss k hk h y + neutralIV131Loss k hk (h+y) z := by
  unfold neutralIV131Loss
  have h1 := neutralIV132Mixed_add_right k hk h y z hy hz
  have h2 := neutralIV132Mixed_add_left k hk h y z hh hy hz
  have h3 := neutralIV130Schur_add k hk y z hy hz
  rw [h1,h2,h3]
  simp only [Complex.add_re]
  ring

/-- Rigorous trial-response upper bound for the exact penalty.
The residual row is evaluated at h+y, not the uncorrected h. -/
theorem neutralIV132Penalty_trial_le (k : ℕ) (hk : 0 < k)
    (Z : Submodule ℂ (𝓢(ℝ,ℂ))) (h : 𝓢(ℝ,ℂ)) (y : Z)
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hz : ∀ z : Z, ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z.val x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : Z, eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val) :
    neutralIV131Penalty k hk Z h ≤ neutralIV131Loss k hk h y.val +
      (neutralIV109RowConstant (11/10:ℝ)
        ((h+y.val)-neutralIV130ResponseVector k hk (h+y.val)))^2/eta := by
  have hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → (h+y.val) x = 0 := by
    intro x hx
    change h x+y.val x = 0
    rw [hh x hx,hz y x hx,add_zero]
  unfold neutralIV131Penalty
  apply csSup_le
  · exact ⟨neutralIV131Loss k hk h (0 : Z).val, ⟨0,rfl⟩⟩
  · rintro r ⟨z,rfl⟩
    let w : Z := z-y
    have hw : z.val = y.val+w.val := by
      change z.val = y.val+(z.val-y.val)
      abel
    change neutralIV131Loss k hk h z.val ≤ _
    rw [hw, neutralIV132Loss_shift k hk h y.val w.val hh (hz y) (hz w)]
    have hp := neutralIV131Loss_le k hk (h+y.val) w.val hs (hz w) eta he (hc w)
    linarith only [hp]

#print axioms neutralIV132Tail_supported
#print axioms neutralIV132Head_iff
#print axioms neutralIV132Window_of_head
#print axioms neutralIV132Mixed_add_right
#print axioms neutralIV132Mixed_hermitian
#print axioms neutralIV132Mixed_add_left
#print axioms neutralIV132Loss_shift
#print axioms neutralIV132Penalty_trial_le

end
end WeilDefect
