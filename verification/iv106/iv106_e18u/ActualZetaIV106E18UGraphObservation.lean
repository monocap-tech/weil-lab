import WeilDefect.Arithmetic.ActualZetaIV106E18TConstrainedGraphApprox
import WeilDefect.Arithmetic.ActualZetaIV106E18RExactSmoothResponse

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap

abbrev neutralIV106E18UGraphAmbient := RealComplexL2 × RealComplexL2

/-- Both coordinates come from the SAME supported smooth test.
The second coordinate is the unnormalized physical derivative. -/
def neutralIV106E18UGraphCore (A B : ℝ) :
    Submodule ℂ neutralIV106E18UGraphAmbient where
  carrier := {v | ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
    v = (s.toLp 2 volume, (SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume)}
  zero_mem' := by
    refine ⟨0, fun _ _ => rfl, ?_⟩
    change (0 : neutralIV106E18UGraphAmbient) =
      (SchwartzMap.toLpCLM ℂ ℂ 2 volume 0,
        SchwartzMap.toLpCLM ℂ ℂ 2 volume (SchwartzMap.derivCLM ℂ ℂ 0))
    simp
  add_mem' := by
    rintro v w ⟨s,hs,rfl⟩ ⟨t,ht,rfl⟩
    refine ⟨s+t, ?_, ?_⟩
    · intro x hx
      change s x+t x = 0
      rw [hs x hx,ht x hx,add_zero]
    · change (_,_) =
        (SchwartzMap.toLpCLM ℂ ℂ 2 volume (s+t),
          SchwartzMap.toLpCLM ℂ ℂ 2 volume (SchwartzMap.derivCLM ℂ ℂ (s+t)))
      simp only [map_add] <;> rfl
  smul_mem' := by
    rintro z v ⟨s,hs,rfl⟩
    refine ⟨z • s, ?_, ?_⟩
    · intro x hx
      change z • s x = 0
      rw [hs x hx,smul_zero]
    · change (_,_) =
        (SchwartzMap.toLpCLM ℂ ℂ 2 volume (z • s),
          SchwartzMap.toLpCLM ℂ ℂ 2 volume (SchwartzMap.derivCLM ℂ ℂ (z • s)))
      simp only [map_smul] <;> rfl

abbrev neutralIV106E18UGraphSpace (A B : ℝ) :=
  (neutralIV106E18UGraphCore A B).topologicalClosure

def neutralIV106E18ULocalCore (A B : ℝ) :
    Submodule ℂ (neutralIV106E18UGraphSpace A B) :=
  (neutralIV106E18UGraphCore A B).comap
    (neutralIV106E18UGraphSpace A B).subtype

/-- The dense domain is the closure of graph pairs, not the product of
two separately chosen dense domains. -/
theorem neutralIV106E18ULocal_dense (A B : ℝ) :
    Dense (neutralIV106E18ULocalCore A B : Set (neutralIV106E18UGraphSpace A B)) := by
  intro q
  apply Metric.mem_closure_iff.mpr
  intro ε hε
  have hq : (q : neutralIV106E18UGraphAmbient) ∈
      closure (neutralIV106E18UGraphCore A B : Set neutralIV106E18UGraphAmbient) :=
    q.property
  obtain ⟨v,hv,hd⟩ := Metric.mem_closure_iff.mp hq ε hε
  let w : neutralIV106E18UGraphSpace A B :=
    ⟨v,(neutralIV106E18UGraphCore A B).le_topologicalClosure hv⟩
  exact ⟨w,hv,hd⟩

/-- Lift ANY continuous finite physical observation to the graph space.
C3/E18R then preserves its exact value while controlling both L2 errors.
There is no assumption of independence of its coordinates. -/
theorem neutralIV106E18UGraph_match {F : Type*}
    [NormedAddCommGroup F] [NormedSpace ℂ F] [FiniteDimensional ℂ F]
    (A B : ℝ) (T : RealComplexL2 →L[ℂ] F)
    (f df : RealComplexL2)
    (hf : (f,df) ∈ neutralIV106E18UGraphSpace A B)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
      T (s.toLp 2 volume) = T f ∧
      dist (s.toLp 2 volume) f < ε ∧
      dist ((SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) df < ε := by
  let S := neutralIV106E18UGraphSpace A B
  let v : S := ⟨(f,df),hf⟩
  let U : S →L[ℂ] F :=
    (T.comp (ContinuousLinearMap.fst ℂ RealComplexL2 RealComplexL2)).domRestrict S
  obtain ⟨w,hw,hT,hd⟩ := neutralIV106E18RAffine_match
    (neutralIV106E18ULocalCore A B) (neutralIV106E18ULocal_dense A B) U v ε hε
  change (w : neutralIV106E18UGraphAmbient) ∈ neutralIV106E18UGraphCore A B at hw
  obtain ⟨s,hs,he⟩ := hw
  change T (w : neutralIV106E18UGraphAmbient).1 = T f at hT
  rw [he] at hT
  change dist (w : neutralIV106E18UGraphAmbient) (f,df) < ε at hd
  rw [he] at hd
  change max (dist (s.toLp 2 volume) f)
    (dist ((SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) df) < ε at hd
  exact ⟨s,hs,hT,(max_lt_iff.mp hd).1,(max_lt_iff.mp hd).2⟩

/-- The literal E18R observation is preserved without reducing it to
three derivative moments or silently omitting the ordinary physical mean. -/
theorem neutralIV106E18UObserve_match (k : ℕ) (hk : 0 < k)
    (A B : ℝ) (f df : RealComplexL2)
    (hf : (f,df) ∈ neutralIV106E18UGraphSpace A B)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
      neutralIV106E18HMoments (11/10:ℝ) (s.toLp 2 volume) =
        neutralIV106E18HMoments (11/10:ℝ) f ∧
      sourceWindowMoment (11/10:ℝ) 0 (s.toLp 2 volume) =
        sourceWindowMoment (11/10:ℝ) 0 f ∧
      (∀ i : Fin k, inner ℂ (neutralIV105CResponse k hk i) (s.toLp 2 volume) =
        inner ℂ (neutralIV105CResponse k hk i) f) ∧
      dist (s.toLp 2 volume) f < ε ∧
      dist ((SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) df < ε := by
  obtain ⟨s,hs,ho,hf',hd'⟩ := neutralIV106E18UGraph_match
    A B (neutralIV106E18RObserve k hk) f df hf ε hε
  obtain ⟨hm,hmean⟩ := neutralIV106E18RObserve_moments k hk _ _ ho
  exact ⟨s,hs,hm,hmean,neutralIV106E18RObserve_row k hk _ _ ho,hf',hd'⟩

#print axioms neutralIV106E18ULocal_dense
#print axioms neutralIV106E18UGraph_match
#print axioms neutralIV106E18UObserve_match
end
end WeilDefect
