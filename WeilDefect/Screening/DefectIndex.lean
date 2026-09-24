import Mathlib

namespace WeilDefect.WDT01

open Filter Set
open scoped InnerProduct Topology
open ContinuousLinearMap
open InnerProductSpace

variable {H Kpos Kneg : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
variable [NormedAddCommGroup Kneg] [InnerProductSpace ℂ Kneg] [CompleteSpace Kneg]

abbrev Coeff := Kpos × Kneg

/-- The coefficient Krein quadratic form. -/
def coeffQ (z : Coeff (Kpos := Kpos) (Kneg := Kneg)) : ℝ :=
  ‖z.1‖ ^ 2 - ‖z.2‖ ^ 2

theorem coeffQ_zero :
    coeffQ (Kpos := Kpos) (Kneg := Kneg) (0 : Coeff (Kpos := Kpos) (Kneg := Kneg)) = 0 := by
  simp [coeffQ]

theorem continuous_coeffQ :
    Continuous (coeffQ (Kpos := Kpos) (Kneg := Kneg)) := by
  unfold coeffQ
  fun_prop

/-- The coefficient analysis map h ↦ (S₊†h,S₋†h). -/
noncomputable def analysisMap
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) :
    H →L[ℂ] Coeff (Kpos := Kpos) (Kneg := Kneg) :=
  (Spos†).prod (Sneg†)

/-- The closed analysis space, represented as a closed set. -/
def analysisSet
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) :
    Set (Coeff (Kpos := Kpos) (Kneg := Kneg)) :=
  closure (Set.range (analysisMap Spos Sneg))

/-- The physical quadratic defect. -/
noncomputable def physicalQ
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (h : H) : ℝ :=
  coeffQ (analysisMap Spos Sneg h)

/-- The physical defect operator S₊S₊† - S₋S₋†. -/
noncomputable def physicalDefect
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) :
    H →L[ℂ] H :=
  Spos ∘L Spos† - Sneg ∘L Sneg†

/-- WD-T01 defect identity in coefficient coordinates. -/
theorem wd_t01_coeff_identity
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (h : H) :
    coeffQ (analysisMap Spos Sneg h) = physicalQ Spos Sneg h := by
  rfl

/-- WD-T01 physical-operator form of the defect identity. -/
theorem wd_t01_defect_inner_identity
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (h : H) :
    inner ℂ (physicalDefect Spos Sneg h) h
      = ((physicalQ Spos Sneg h : ℝ) : ℂ) := by
  simp [physicalDefect, physicalQ, coeffQ, analysisMap,
    ContinuousLinearMap.adjoint_inner_left, inner_self_eq_norm_sq_to_K]

/-- Nonnegativity on the physical carrier. -/
def PhysicalNonnegative
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) : Prop :=
  ∀ h : H, 0 ≤ physicalQ Spos Sneg h

/-- Nonnegativity on the closed analysis space. -/
def AnalysisNonnegative
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) : Prop :=
  ∀ z ∈ analysisSet Spos Sneg, 0 ≤ coeffQ z

/-- WD-T01 nonnegativity transfer between physical and closed analysis spaces. -/
theorem wd_t01_nonnegative_iff
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H) :
    AnalysisNonnegative Spos Sneg ↔ PhysicalNonnegative Spos Sneg := by
  constructor
  · intro hA h
    exact hA (analysisMap Spos Sneg h)
      (subset_closure (Set.mem_range_self h))
  · intro hD
    intro z hz
    let C : Set (Coeff (Kpos := Kpos) (Kneg := Kneg)) :=
      {w | 0 ≤ coeffQ w}
    have hclosed : IsClosed C := isClosed_le continuous_const continuous_coeffQ
    have hrange : Set.range (analysisMap Spos Sneg) ⊆ C := by
      rintro _ ⟨h, rfl⟩
      exact hD h
    exact (closure_minimal hrange hclosed) hz

/--
A finite-rank negative witness is a complex-linear map from ℂⁿ whose image is
strictly negative on the unit sphere and lies in the specified carrier set.
-/
def HasNegativeRank
    {E : Type*}
    [NormedAddCommGroup E] [NormedSpace ℂ E]
    (q : E → ℝ)
    (carrier : Set E)
    (n : ℕ) : Prop :=
  ∃ T : EuclideanSpace ℂ (Fin n) →L[ℂ] E,
    (∀ x, T x ∈ carrier) ∧
    ∀ x, ‖x‖ = 1 → q (T x) < 0

def PhysicalHasNegativeRank
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (n : ℕ) : Prop :=
  HasNegativeRank (physicalQ Spos Sneg) Set.univ n

def AnalysisHasNegativeRank
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (n : ℕ) : Prop :=
  HasNegativeRank
    (coeffQ (Kpos := Kpos) (Kneg := Kneg))
    (analysisSet Spos Sneg) n

/-- Orthonormal coordinate reconstruction from finitely many target vectors. -/
noncomputable def reconstruct
    {E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (n : ℕ)
    (v : Fin n → E) :
    EuclideanSpace ℂ (Fin n) →L[ℂ] E :=
  ∑ i : Fin n,
    rankOne ℂ (v i) (EuclideanSpace.basisFun (Fin n) ℂ i)

theorem reconstruct_basisValues
    {E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (n : ℕ)
    (T : EuclideanSpace ℂ (Fin n) →L[ℂ] E) :
    reconstruct n (fun i => T (EuclideanSpace.basisFun (Fin n) ℂ i)) = T := by
  ext x
  simp only [reconstruct, Finset.sum_apply, rankOne_apply]
  rw [← T.map_sum]
  exact congrArg T ((EuclideanSpace.basisFun (Fin n) ℂ).sum_repr' x)

theorem continuous_reconstruct
    {E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (n : ℕ) :
    Continuous (reconstruct (E := E) n) := by
  unfold reconstruct
  fun_prop

/--
Strict negativity on the unit sphere is stable under small perturbations of a
finite-dimensional continuous linear map.
-/
theorem negativeMap_mem_nhds
    {E : Type*}
    [NormedAddCommGroup E] [NormedSpace ℂ E]
    (n : ℕ)
    (q : E → ℝ)
    (hq : Continuous q)
    (T : EuclideanSpace ℂ (Fin n) →L[ℂ] E)
    (hT : ∀ x, ‖x‖ = 1 → q (T x) < 0) :
    {S : EuclideanSpace ℂ (Fin n) →L[ℂ] E |
      ∀ x, ‖x‖ = 1 → q (S x) < 0} ∈ 𝓝 T := by
  let sphere : Set (EuclideanSpace ℂ (Fin n)) := Metric.sphere 0 1
  have hsphere : IsCompact sphere := isCompact_sphere 0 1
  have hlocal :
      ∀ x ∈ sphere,
        ∀ᶠ z : (EuclideanSpace ℂ (Fin n) →L[ℂ] E) ×
            EuclideanSpace ℂ (Fin n) in 𝓝 (T, x),
          q (z.1 z.2) < 0 := by
    intro x hx
    have hxnorm : ‖x‖ = 1 := by
      simpa [sphere, Metric.mem_sphere, dist_eq_norm] using hx
    have hxneg : q (T x) < 0 := hT x hxnorm
    have hopen :
        IsOpen {z : (EuclideanSpace ℂ (Fin n) →L[ℂ] E) ×
            EuclideanSpace ℂ (Fin n) | q (z.1 z.2) < 0} := by
      exact isOpen_lt (hq.comp (by fun_prop)) continuous_const
    exact hopen.mem_nhds hxneg
  have hunif :=
    hsphere.eventually_forall_of_forall_eventually (x₀ := T) hlocal
  filter_upwards [hunif] with S hS
  intro x hx
  exact hS x (by simpa [sphere, Metric.mem_sphere, dist_eq_norm] using hx)

/--
If every basis value of a finite-dimensional map lies in the closure of a set,
the map can be approximated by a reconstructed map whose basis values lie in
that set.
-/
theorem exists_reconstruct_mem_of_basis_mem_closure
    {E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (n : ℕ)
    (s : Set E)
    (T : EuclideanSpace ℂ (Fin n) →L[ℂ] E)
    (hbasis : ∀ i, T (EuclideanSpace.basisFun (Fin n) ℂ i) ∈ closure s)
    {U : Set (EuclideanSpace ℂ (Fin n) →L[ℂ] E)}
    (hU : U ∈ 𝓝 T) :
    ∃ v : Fin n → E,
      v ∈ Set.univ.pi (fun _ => s) ∧
      reconstruct n v ∈ U := by
  let v0 : Fin n → E := fun i => T (EuclideanSpace.basisFun (Fin n) ℂ i)
  have hv0 :
      v0 ∈ closure (Set.univ.pi (fun _ : Fin n => s)) := by
    rw [mem_closure_pi]
    intro i _
    exact hbasis i
  have hrecon : reconstruct n v0 = T := reconstruct_basisValues n T
  have hpre : reconstruct n ⁻¹' U ∈ 𝓝 v0 := by
    have hU' : U ∈ 𝓝 (reconstruct n v0) := by simpa [hrecon] using hU
    exact (continuous_reconstruct (E := E) n).continuousAt hU'
  obtain ⟨v, hvpre, hvs⟩ :=
    mem_closure_iff_nhds.mp hv0 (reconstruct n ⁻¹' U) hpre
  exact ⟨v, hvs, hvpre⟩

/-- Physical negative rank always gives the same analysis negative rank. -/
theorem wd_t01_physical_to_analysis_rank
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (n : ℕ) :
    PhysicalHasNegativeRank Spos Sneg n →
      AnalysisHasNegativeRank Spos Sneg n := by
  rintro ⟨T, -, hneg⟩
  refine ⟨(analysisMap Spos Sneg) ∘L T, ?_, ?_⟩
  · intro x
    exact subset_closure (Set.mem_range_self (T x))
  · intro x hx
    exact hneg x hx

/-- Reverse finite-rank transfer from the closed analysis space to the physical carrier. -/
theorem wd_t01_analysis_to_physical_rank
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (n : ℕ) :
    AnalysisHasNegativeRank Spos Sneg n →
      PhysicalHasNegativeRank Spos Sneg n := by
  rintro ⟨T, hcarrier, hneg⟩
  let A := analysisMap Spos Sneg
  let R : Set (Coeff (Kpos := Kpos) (Kneg := Kneg)) := Set.range A
  let U : Set (EuclideanSpace ℂ (Fin n) →L[ℂ]
      Coeff (Kpos := Kpos) (Kneg := Kneg)) :=
    {S | ∀ x, ‖x‖ = 1 → coeffQ (S x) < 0}
  have hU : U ∈ 𝓝 T := by
    exact negativeMap_mem_nhds n
      (coeffQ (Kpos := Kpos) (Kneg := Kneg))
      continuous_coeffQ T hneg
  have hbasis :
      ∀ i, T (EuclideanSpace.basisFun (Fin n) ℂ i) ∈ closure R := by
    intro i
    exact hcarrier _
  obtain ⟨v, hvR, hvU⟩ :=
    exists_reconstruct_mem_of_basis_mem_closure n R T hbasis hU
  have hvRange : ∀ i, v i ∈ Set.range A := by
    intro i
    exact hvR i (Set.mem_univ i)
  choose hvec hhvec using hvRange
  let Hmap : EuclideanSpace ℂ (Fin n) →L[ℂ] H :=
    reconstruct n hvec
  have hcomp : A ∘L Hmap = reconstruct n v := by
    ext x
    simp only [Hmap, reconstruct, Finset.sum_apply, rankOne_apply,
      ContinuousLinearMap.comp_apply, map_sum, map_smul]
    apply Finset.sum_congr rfl
    intro i _
    rw [hhvec i]
  refine ⟨Hmap, fun _ => Set.mem_univ _, ?_⟩
  intro x hx
  have hcoeff : coeffQ ((reconstruct n v) x) < 0 := hvU x hx
  rw [← hcomp] at hcoeff
  exact hcoeff

/--
WD-T01 finite-index transfer: the complete set of attainable finite negative
dimensions is identical on the physical and closed analysis sides.
-/
theorem wd_t01_negative_rank_iff
    (Spos : Kpos →L[ℂ] H)
    (Sneg : Kneg →L[ℂ] H)
    (n : ℕ) :
    AnalysisHasNegativeRank Spos Sneg n ↔
      PhysicalHasNegativeRank Spos Sneg n :=
  ⟨wd_t01_analysis_to_physical_rank Spos Sneg n,
    wd_t01_physical_to_analysis_rank Spos Sneg n⟩

end WeilDefect.WDT01
