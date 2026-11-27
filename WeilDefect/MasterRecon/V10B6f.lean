import WeilDefect.MasterRecon.V10B6d
import WeilDefect.MasterRecon.V10B6e
import Mathlib.Topology.Algebra.InfiniteSum.Constructions

/-! V10B6f: split the full strip into the right representatives and
reflections of the strictly off-line representatives. All summations
are transported only after absolute convergence has been established.
Reflection closure and multiplicity equality are explicit inputs. -/
namespace WeilDefect.MasterRecon.V10B6f

open Set
open scoped ENNReal InnerProduct ComplexConjugate
open V10A (Index displacement reflect multiplicity)

abbrev StripIndex := {ρ : ℂ // V09D.stripZero ρ}
abbrev OffIndex := {i : Index // displacement i ≠ 0}

def rightIndex (i : Index) : StripIndex :=
  ⟨i.val,i.property.1⟩

def leftIndex (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ))
    (i : OffIndex) : StripIndex :=
  ⟨reflect i.val.val,hr _ i.val.property.1⟩

theorem rightIndex_re (i : Index) : (1:ℝ)/2 ≤ (rightIndex i : ℂ).re :=
  i.property.2

theorem leftIndex_re
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ))
    (i : OffIndex) : (leftIndex hr i : ℂ).re < 1/2 := by
  change (reflect i.val.val).re < 1/2
  rw [V10A.reflect_re]
  have hi := i.val.property.2
  have hn := i.property
  unfold displacement at hn
  have hp : (1:ℝ)/2 < i.val.val.re := lt_of_le_of_ne hi (fun he => hn (sub_eq_zero.mpr he.symm))
  linarith

theorem splitIndex_bijective
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ)) :
    Function.Bijective (Sum.elim rightIndex (leftIndex hr)) := by
  constructor
  · intro a b h
    cases a with
    | inl i =>
      cases b with
      | inl j =>
        congr 1
        exact Subtype.ext (congrArg Subtype.val h)
      | inr j =>
        have he := congrArg (fun z : StripIndex => z.val.re) h
        exact False.elim (by linarith [rightIndex_re i,leftIndex_re hr j])
    | inr i =>
      cases b with
      | inl j =>
        have he := congrArg (fun z : StripIndex => z.val.re) h
        exact False.elim (by linarith [leftIndex_re hr i,rightIndex_re j])
      | inr j =>
        congr 1
        apply Subtype.ext
        apply Subtype.ext
        have he : reflect i.val.val = reflect j.val.val := congrArg Subtype.val h
        have he' := congrArg reflect he
        simpa only [V10A.reflect_involution] using he'
  · intro z
    by_cases hz : (1:ℝ)/2 ≤ z.val.re
    · exact ⟨Sum.inl ⟨z.val,z.property,hz⟩,rfl⟩
    · have hright : (1:ℝ)/2 ≤ (reflect z.val).re := by
        rw [V10A.reflect_re]
        linarith [lt_of_not_ge hz]
      let i : Index := ⟨reflect z.val,hr _ z.property,hright⟩
      have hi : displacement i ≠ 0 := by
        change (reflect z.val).re-1/2 ≠ 0
        rw [V10A.reflect_re]
        linarith [lt_of_not_ge hz]
      refine ⟨Sum.inr ⟨i,hi⟩,?_⟩
      apply Subtype.ext
      exact V10A.reflect_involution z.val

noncomputable def splitIndex
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ)) :
    Index ⊕ OffIndex ≃ StripIndex :=
  Equiv.ofBijective (Sum.elim rightIndex (leftIndex hr)) (splitIndex_bijective hr)

theorem splitIndex_right
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ)) (i : Index) :
    splitIndex hr (Sum.inl i) = rightIndex i := rfl

theorem splitIndex_left
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ)) (i : OffIndex) :
    splitIndex hr (Sum.inr i) = leftIndex hr i := rfl

noncomputable def zeroTerm (f : ℝ → ℂ) (ρ : ℂ) : ℝ :=
  (V07A.weightedMellin f (V09D.mult ρ) (ρ-1/2) *
    conj (V07A.weightedMellin f (V09D.mult ρ) (reflect ρ-1/2))).re

theorem cross_re_swap (u v : ℂ) : (u * conj v).re = (v * conj u).re := by
  simp only [Complex.mul_re, Complex.conj_re, Complex.conj_im]
  ring

theorem cross_re_self (u : ℂ) : (u * conj u).re = ‖u‖^2 := by
  simp only [Complex.mul_re, Complex.conj_re, Complex.conj_im,
    Complex.sq_norm, Complex.normSq_apply]
  ring

theorem zeroTerm_reflect (f : ℝ → ℂ) (ρ : ℂ)
    (hm : V09D.mult (reflect ρ) = V09D.mult ρ) :
    zeroTerm f (reflect ρ) = zeroTerm f ρ := by
  unfold zeroTerm
  rw [hm,V10A.reflect_involution,cross_re_swap]

theorem fixed_reflect (i : Index) (hi : displacement i = 0) :
    reflect (i : ℂ) = (i : ℂ) :=
  (V10A.reflect_fixed_iff _).2 (sub_eq_zero.mp hi)

theorem orbitTerm_right (f : ℝ → ℂ) (i : Index) :
    V10B6d.orbitTerm f i =
      if displacement i = 0 then zeroTerm f i.val else 2*zeroTerm f i.val := by
  unfold V10B6d.orbitTerm
  by_cases hi : displacement i = 0
  · rw [if_pos hi,if_pos hi]
    unfold zeroTerm
    rw [fixed_reflect i hi,cross_re_self,V10A2.weighted_energy]
    rfl
  · rw [if_neg hi,if_neg hi]
    rfl

theorem zeroTerm_abs_le (f : ℝ → ℂ) (i : Index) :
    |zeroTerm f i.val| ≤ |V10B6d.orbitTerm f i| := by
  rw [orbitTerm_right]
  by_cases hi : displacement i = 0
  · rw [if_pos hi]
  · rw [if_neg hi,abs_mul,abs_of_nonneg (by norm_num : (0:ℝ) ≤ 2)]
    linarith [abs_nonneg (zeroTerm f i.val)]

noncomputable def leftPadded (f : ℝ → ℂ) (i : Index) : ℝ :=
  if displacement i = 0 then 0 else zeroTerm f (reflect i.val)

theorem leftPadded_abs_le (f : ℝ → ℂ) (i : Index)
    (hm : V09D.mult (reflect i.val) = V09D.mult i.val) :
    |leftPadded f i| ≤ |V10B6d.orbitTerm f i| := by
  unfold leftPadded
  by_cases hi : displacement i = 0
  · rw [if_pos hi,abs_zero]
    exact abs_nonneg _
  · rw [if_neg hi,zeroTerm_reflect f i.val hm]
    exact zeroTerm_abs_le f i

theorem orbitTerm_split (f : ℝ → ℂ) (i : Index)
    (hm : V09D.mult (reflect i.val) = V09D.mult i.val) :
    V10B6d.orbitTerm f i = zeroTerm f i.val + leftPadded f i := by
  rw [orbitTerm_right]
  unfold leftPadded
  by_cases hi : displacement i = 0
  · simp [hi]
  · rw [if_neg hi,if_neg hi,zeroTerm_reflect f i.val hm]
    ring

theorem tsum_leftPadded (f : ℝ → ℂ) :
    (∑' i : OffIndex, zeroTerm f (reflect i.val.val)) =
      ∑' i : Index, leftPadded f i := by
  classical
  let s : Set Index := {i | displacement i ≠ 0}
  change (∑' i : s, zeroTerm f (reflect i.val.val)) = _
  rw [tsum_subtype s]
  apply tsum_congr
  intro i
  by_cases hi : displacement i = 0 <;> simp [s,Set.indicator,hi,leftPadded]

/-- An arbitrary absolutely summable orbit bank transports to the
full strip. Absolute convergence of the individual strip terms is
proved before the reindexing equality. -/
theorem full_strip_sum (f : ℝ → ℂ)
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ))
    (hm : ∀ ρ, V09D.stripZero ρ → V09D.mult (reflect ρ) = V09D.mult ρ)
    (hs : Summable (fun i : Index => |V10B6d.orbitTerm f i|)) :
    Summable (fun z : StripIndex => |zeroTerm f z.val|) ∧
      (∑' z : StripIndex, zeroTerm f z.val) =
        ∑' i : Index, V10B6d.orbitTerm f i := by
  classical
  let R : Index → ℝ := fun i => zeroTerm f i.val
  let L : Index → ℝ := leftPadded f
  let E := splitIndex hr
  let Z : StripIndex → ℝ := fun z => zeroTerm f z.val
  have hRa : Summable (fun i => |R i|) := by
    apply Summable.of_norm_bounded hs
    intro i
    rw [Real.norm_eq_abs,abs_abs]
    exact zeroTerm_abs_le f i
  have hLa : Summable (fun i => |L i|) := by
    apply Summable.of_norm_bounded hs
    intro i
    rw [Real.norm_eq_abs,abs_abs]
    exact leftPadded_abs_le f i (hm _ i.property.1)
  have hR : Summable R := by
    apply Summable.of_norm_bounded hRa
    intro i
    rw [Real.norm_eq_abs]
  have hL : Summable L := by
    apply Summable.of_norm_bounded hLa
    intro i
    rw [Real.norm_eq_abs]
  have hLoff : Summable (fun i : OffIndex => Z (E (Sum.inr i))) := by
    have h := hL.subtype (fun i => displacement i ≠ 0)
    apply h.congr
    intro i
    simp [Z,E,splitIndex_left,leftIndex,L,leftPadded,i.property]
  have hLoffa : Summable (fun i : OffIndex => |Z (E (Sum.inr i))|) := by
    have h := hLa.subtype (fun i => displacement i ≠ 0)
    apply h.congr
    intro i
    simp [Z,E,splitIndex_left,leftIndex,L,leftPadded,i.property]
  have hR' : Summable (fun i : Index => Z (E (Sum.inl i))) := hR
  have hR'a : Summable (fun i : Index => |Z (E (Sum.inl i))|) := hRa
  have hsum : Summable ((fun z => |Z z|) ∘ E) :=
    Summable.sum _ hR'a hLoffa
  refine ⟨E.summable_iff.mp hsum,?_⟩
  change (∑' z, Z z) = _
  rw [← E.tsum_eq Z]
  have he : (∑' a : Index ⊕ OffIndex, Z (E a)) =
      (∑' i : Index, R i) + ∑' i : OffIndex, zeroTerm f (reflect i.val.val) := by
    exact hR'.tsum_sum hLoff
  rw [he,tsum_leftPadded f,← hR.tsum_add hL]
  apply tsum_congr
  intro i
  exact (orbitTerm_split f i (hm _ i.property.1)).symm

theorem full_strip_diagonal (t : ℝ)
    (T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index)
    (hT : V10B6d.LiteralCoordinates t T)
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ))
    (hm : ∀ ρ, V09D.stripZero ρ → V09D.mult (reflect ρ) = V09D.mult ρ)
    (g : V08I.logCarrier t) :
    Summable (fun z : StripIndex =>
      |zeroTerm (V08I.physicalInclusion t g : ℝ → ℂ) z.val|) ∧
    (inner ℂ (V10B6c.signedGram T g) g).re =
      ∑' z : StripIndex, zeroTerm (V08I.physicalInclusion t g : ℝ → ℂ) z.val := by
  obtain ⟨ha,he⟩ := full_strip_sum
    (V08I.physicalInclusion t g : ℝ → ℂ) hr hm
    (V10B6d.arithmetic_orbit_abs_summable t T hT g)
  exact ⟨ha,(V10B6d.arithmetic_orbit_diagonal t T hT g).trans he.symm⟩

end WeilDefect.MasterRecon.V10B6f

#print axioms WeilDefect.MasterRecon.V10B6f.rightIndex_re
#print axioms WeilDefect.MasterRecon.V10B6f.leftIndex_re
#print axioms WeilDefect.MasterRecon.V10B6f.splitIndex_bijective
#print axioms WeilDefect.MasterRecon.V10B6f.splitIndex_right
#print axioms WeilDefect.MasterRecon.V10B6f.splitIndex_left
#print axioms WeilDefect.MasterRecon.V10B6f.cross_re_swap
#print axioms WeilDefect.MasterRecon.V10B6f.cross_re_self
#print axioms WeilDefect.MasterRecon.V10B6f.zeroTerm_reflect
#print axioms WeilDefect.MasterRecon.V10B6f.fixed_reflect
#print axioms WeilDefect.MasterRecon.V10B6f.orbitTerm_right
#print axioms WeilDefect.MasterRecon.V10B6f.zeroTerm_abs_le
#print axioms WeilDefect.MasterRecon.V10B6f.leftPadded_abs_le
#print axioms WeilDefect.MasterRecon.V10B6f.orbitTerm_split
#print axioms WeilDefect.MasterRecon.V10B6f.tsum_leftPadded
#print axioms WeilDefect.MasterRecon.V10B6f.full_strip_sum
#print axioms WeilDefect.MasterRecon.V10B6f.full_strip_diagonal
