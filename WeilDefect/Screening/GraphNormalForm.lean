import WeilDefect.Screening.Douglas
import Mathlib

namespace WeilDefect.WDT03

open scoped InnerProduct
open ContinuousLinearMap
open WeilDefect.WDT01
open WeilDefect.WDT02

variable {H Kpos Kneg : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
variable [NormedAddCommGroup Kneg] [InnerProductSpace ℂ Kneg] [CompleteSpace Kneg]

/-- Synthesis map E(x,u)=Spos x + Sneg u. -/
def synthesisMap
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) :
    (Kpos × Kneg) →L[ℂ] H :=
  Spos.coprod Sneg

/-- The analysis submodule A=(ker E)⊥. -/
def analysisSubmodule
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) :
    Submodule ℂ (Kpos × Kneg) :=
  (synthesisMap Spos Sneg).kerᗮ

/--
Imported Douglas range-inclusion interface used by WD-T03.

It is an explicit theorem premise, not a project axiom.
-/
structure DouglasRangeData
    (A : Kneg →L[ℂ] H)
    (B : Kpos →L[ℂ] H) : Prop where
  reduced_of_range :
    Set.range A ⊆ Set.range B →
      ∃! C : Kneg →L[ℂ] Kpos,
        A = B ∘L C ∧ IsReducedFor B C

/--
Douglas reduced solution transferred to the project's sign convention.
-/
theorem signed_reduced_of_range
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (hDouglas : DouglasRangeData Sneg Spos)
    (hrange : Set.range Sneg ⊆ Set.range Spos) :
    ∃! X : Kneg →L[ℂ] Kpos,
      Sneg = -(Spos ∘L X) ∧ IsReducedFor Spos X := by
  rcases hDouglas.reduced_of_range hrange with ⟨C, hC, huniq⟩
  refine ⟨-C, ?_, ?_⟩
  · constructor
    · rw [ContinuousLinearMap.comp_neg]
      simpa using hC.1
    · exact (reduced_neg_iff Spos C).2 hC.2
  · intro X hX
    have hminusX :
        Sneg = Spos ∘L (-X) ∧ IsReducedFor Spos (-X) := by
      constructor
      · rw [ContinuousLinearMap.comp_neg]
        simpa using hX.1
      · exact (reduced_neg_iff Spos X).2 hX.2
    have hEq : -X = C := huniq (-X) hminusX
    have := congrArg Neg.neg hEq
    simpa using this

/-- Kernel characterization under an exact reduced screening relation. -/
theorem kernel_iff
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (X : Kneg →L[ℂ] Kpos)
    (hfac : Sneg = -(Spos ∘L X))
    (x : Kpos) (u : Kneg) :
    synthesisMap Spos Sneg (x,u) = 0 ↔
      ∃ k : Kpos, Spos k = 0 ∧ x = k + X u := by
  constructor
  · intro h
    refine ⟨x - X u, ?_, ?_⟩
    · have h' := h
      simp [synthesisMap, hfac] at h'
      simpa [map_sub] using h'
    · abel
  · rintro ⟨k, hk, rfl⟩
    simp [synthesisMap, hfac, hk]

/-- The two kernel summands are orthogonal when X is reduced. -/
theorem kernel_summands_orthogonal
    (Spos : Kpos →L[ℂ] H)
    (X : Kneg →L[ℂ] Kpos)
    (hred : IsReducedFor Spos X)
    (k : Kpos) (u : Kneg)
    (hk : Spos k = 0) :
    inner ℂ (k, (0 : Kneg)) (X u, u) = 0 := by
  simpa using hred u k hk

/--
WD-T03 kernel split, expressed pointwise:
every kernel vector decomposes uniquely as a kernel-positive component plus
the graph component (Xu,u).
-/
theorem wd_t03_kernel_decomposition
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (X : Kneg →L[ℂ] Kpos)
    (hfac : Sneg = -(Spos ∘L X))
    (hred : IsReducedFor Spos X)
    (x : Kpos) (u : Kneg) :
    synthesisMap Spos Sneg (x,u) = 0 ↔
      ∃! k : Kpos,
        Spos k = 0 ∧
        (x,u) = (k,0) + (X u,u) ∧
        inner ℂ (k,(0 : Kneg)) (X u,u) = 0 := by
  constructor
  · intro h
    rcases (kernel_iff Spos Sneg X hfac x u).mp h with ⟨k, hk, hx⟩
    refine ⟨k, ?_, ?_⟩
    · refine ⟨hk, ?_, kernel_summands_orthogonal Spos X hred k u hk⟩
      ext <;> simp [hx]
    · intro k' hk'
      have h1 := congrArg Prod.fst hk'.2.1
      have h2 := congrArg Prod.fst (show (x,u) = (k,0) + (X u,u) by
        ext <;> simp [hx])
      simp at h1 h2
      linarith
  · rintro ⟨k, hk, hsplit, -⟩
    apply (kernel_iff Spos Sneg X hfac x u).mpr
    refine ⟨k, hk, ?_⟩
    have := congrArg Prod.fst hsplit
    simpa using this

/-- Membership in ker(Spos)⊥ written pointwise. -/
def PosReducedSpace
    (Spos : Kpos →L[ℂ] H) : Submodule ℂ Kpos :=
  Spos.kerᗮ

/--
WD-T03 graph normal form:
A=(ker E)⊥ is exactly graph(-X†) over ker(Spos)⊥.
-/
theorem wd_t03_analysis_graph_iff
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (X : Kneg →L[ℂ] Kpos)
    (hfac : Sneg = -(Spos ∘L X))
    (hred : IsReducedFor Spos X)
    (a : Kpos) (v : Kneg) :
    (a,v) ∈ analysisSubmodule Spos Sneg ↔
      a ∈ PosReducedSpace Spos ∧ v = -(X†) a := by
  constructor
  · intro hA
    have horth :
        ∀ y ∈ (synthesisMap Spos Sneg).ker,
          inner ℂ (a,v) y = 0 :=
      (Submodule.mem_orthogonal' _ _).mp hA
    have ha : a ∈ PosReducedSpace Spos := by
      rw [PosReducedSpace, Submodule.mem_orthogonal']
      intro k hk
      have hker : (k,(0 : Kneg)) ∈ (synthesisMap Spos Sneg).ker := by
        simp [synthesisMap, hk]
      simpa using horth (k,0) hker
    have hvEq : v = -(X†) a := by
      apply (sub_eq_zero.mp ?_)
      apply (eq_zero_iff_forall_inner_eq_zero).2
      intro u
      have hker : (X u,u) ∈ (synthesisMap Spos Sneg).ker := by
        simp [synthesisMap, hfac]
      have hh := horth (X u,u) hker
      rw [Prod.inner_apply] at hh
      rw [← ContinuousLinearMap.adjoint_inner_left X u a] at hh
      simp only [inner_sub_left, inner_neg_left]
      linarith
    exact ⟨ha, hvEq⟩
  · rintro ⟨ha, rfl⟩
    rw [analysisSubmodule, Submodule.mem_orthogonal']
    intro y hy
    rcases y with ⟨x,u⟩
    have hker :
        synthesisMap Spos Sneg (x,u) = 0 := by
      simpa [LinearMap.mem_ker] using hy
    rcases (kernel_iff Spos Sneg X hfac x u).mp hker with ⟨k, hk, hx⟩
    have hak : inner ℂ a k = 0 := by
      exact (Submodule.mem_orthogonal' _ _).mp ha k hk
    subst x
    rw [Prod.inner_apply]
    rw [inner_add_right, ← ContinuousLinearMap.adjoint_inner_left X u a]
    simp [hak]

/-- WD-T03 signature identity on the graph. -/
theorem wd_t03_graph_signature
    (X : Kneg →L[ℂ] Kpos)
    (a : Kpos) :
    coeffQ (Kpos := Kpos) (Kneg := Kneg) (a, -(X†) a)
      = ‖a‖ ^ 2 - ‖(X†) a‖ ^ 2 := by
  simp [coeffQ]

/--
WD-T03 defect factorization D=Spos(I-XX†)Spos†.
-/
theorem wd_t03_defect_factorization
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (X : Kneg →L[ℂ] Kpos)
    (hfac : Sneg = -(Spos ∘L X)) :
    physicalDefect Spos Sneg
      =
    Spos ∘L
      ((ContinuousLinearMap.id ℂ Kpos - X ∘L X†) ∘L Spos†) := by
  apply ContinuousLinearMap.ext
  intro h
  simp [physicalDefect, hfac]

/--
WD-T03 assembled from the imported Douglas range-inclusion premise.
-/
theorem wd_t03_reduced_graph_normal_form
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (hDouglas : DouglasRangeData Sneg Spos)
    (hrange : Set.range Sneg ⊆ Set.range Spos) :
    ∃! X : Kneg →L[ℂ] Kpos,
      Sneg = -(Spos ∘L X) ∧
      IsReducedFor Spos X ∧
      (∀ a v,
        (a,v) ∈ analysisSubmodule Spos Sneg ↔
          a ∈ PosReducedSpace Spos ∧ v = -(X†) a) ∧
      physicalDefect Spos Sneg
        =
      Spos ∘L
        ((ContinuousLinearMap.id ℂ Kpos - X ∘L X†) ∘L Spos†) := by
  rcases signed_reduced_of_range Spos Sneg hDouglas hrange with
    ⟨X, hX, huniq⟩
  refine ⟨X, ?_, ?_⟩
  · refine ⟨hX.1, hX.2, ?_, ?_⟩
    · intro a v
      exact wd_t03_analysis_graph_iff Spos Sneg X hX.1 hX.2 a v
    · exact wd_t03_defect_factorization Spos Sneg X hX.1
  · intro Y hY
    exact huniq Y ⟨hY.1, hY.2.1⟩

end WeilDefect.WDT03
