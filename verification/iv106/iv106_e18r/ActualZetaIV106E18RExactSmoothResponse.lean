import WeilDefect.Arithmetic.ActualZetaIV106E18QLiteralRank
import WeilDefect.Arithmetic.ActualZetaIV106C3ConstraintDensity

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap

/-- Affine strengthening of C3: any finite-dimensional observation of a
rough vector can be realized exactly in a dense linear core, arbitrarily
close in the original norm. The target need not be zero. -/
theorem neutralIV106E18RAffine_match {E F : Type*}
    [NormedAddCommGroup E] [NormedSpace ℂ E]
    [NormedAddCommGroup F] [NormedSpace ℂ F] [FiniteDimensional ℂ F]
    (D : Submodule ℂ E) (hD : Dense (D : Set E))
    (T : E →L[ℂ] F) (x : E) (ε : ℝ) (hε : 0 < ε) :
    ∃ y ∈ D, T y = T x ∧ dist y x < ε := by
  obtain ⟨d,hd⟩ := neutralIV106C3Range D hD T x
  change T (d:E) = T x at hd
  obtain ⟨R,hR,hfix,hcore⟩ := neutralIV106C3Correction D hD T
  let G : E → E := fun y => (d:E)+R (y-(d:E))
  let S : Set E := {y | y ∈ D ∧ T y = T x}
  have hGc : Continuous G :=
    continuous_const.add (R.continuous.comp (continuous_id.sub continuous_const))
  have hGx : G x = x := by
    have hz : T (x-(d:E)) = 0 := by rw [map_sub,hd,sub_self]
    dsimp [G]
    rw [hfix _ hz]
    abel
  have hsub : (D : Set E) ⊆ G ⁻¹' closure S := by
    intro y hy
    apply subset_closure
    change G y ∈ D ∧ T (G y) = T x
    constructor
    · exact D.add_mem d.property (hcore _ (D.sub_mem hy d.property))
    · dsimp [G]
      rw [map_add,hR,add_zero,hd]
  have hall := closure_minimal hsub (isClosed_closure.preimage hGc)
  rw [hD.closure_eq] at hall
  have hx : G x ∈ closure S := hall (Set.mem_univ x)
  rw [hGx] at hx
  obtain ⟨y,hy,hdy⟩ := Metric.mem_closure_iff.mp hx ε hε
  exact ⟨y,hy.1,hy.2,by simpa [dist_comm] using hdy⟩

/-- Include the zero mean, both pole moments, and every literal IV105C
response coordinate in a single complex-linear observation. -/
def neutralIV106E18RObserve (k : ℕ) (hk : 0 < k) :
    RealComplexL2 →L[ℂ] ((ℂ × ℂ) × (ℂ × (Fin k → ℂ))) :=
  (neutralIV106E18HMoments (11/10:ℝ)).prod
    ((neutralSourceWindowMomentCLM (11/10:ℝ) 0).prod
      (ContinuousLinearMap.pi fun i =>
        InnerProductSpace.toDual ℂ RealComplexL2 (neutralIV105CResponse k hk i)))

theorem neutralIV106E18RObserve_moments (k : ℕ) (hk : 0 < k)
    (u v : RealComplexL2)
    (h : neutralIV106E18RObserve k hk u = neutralIV106E18RObserve k hk v) :
    neutralIV106E18HMoments (11/10:ℝ) u =
      neutralIV106E18HMoments (11/10:ℝ) v ∧
    sourceWindowMoment (11/10:ℝ) 0 u = sourceWindowMoment (11/10:ℝ) 0 v := by
  refine ⟨congrArg Prod.fst h,?_⟩
  simpa [neutralIV106E18RObserve,neutralSourceWindowMomentCLM_eq] using
    congrArg (fun z => z.2.1) h

theorem neutralIV106E18RObserve_row (k : ℕ) (hk : 0 < k)
    (u v : RealComplexL2)
    (h : neutralIV106E18RObserve k hk u = neutralIV106E18RObserve k hk v)
    (i : Fin k) :
    inner ℂ (neutralIV105CResponse k hk i) u =
      inner ℂ (neutralIV105CResponse k hk i) v := by
  simpa [neutralIV106E18RObserve,InnerProductSpace.toDual_apply_apply] using
    congrArg (fun z => z.2.2 i) h

/-- The rough trial need not itself be admitted into the logarithmic
carrier in order to realize its finite response column. The matching
Schwartz vector is a genuine supported original physical test. -/
theorem neutralIV106E18RCell_match (k : ℕ) (hk : 0 < k)
    (j : ℕ) (hj : neutralIV106E18LEligible j)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : 𝓢(ℝ,ℂ),
      (∀ x ∉ closedBall (neutralIV106E18LLeft j+neutralIV106E18LWidth/2)
        (neutralIV106E18LWidth/2+neutralIV106E18LBuffer), s x = 0) ∧
      (∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), s x = 0) ∧
      neutralIV101MassComplement k hk s ∧
      neutralIV106E18HMoments (11/10:ℝ) (s.toLp 2 volume) = 0 ∧
      sourceWindowMoment (11/10:ℝ) 0 (s.toLp 2 volume) = 0 ∧
      dist (s.toLp 2 volume) (neutralIV106E18OTrial j) < ε ∧
      (∀ i : Fin k, inner ℂ (neutralIV105CResponse k hk i) (s.toLp 2 volume) =
        inner ℂ (neutralIV105CResponse k hk i) (neutralIV106E18OTrial j)) := by
  let c := neutralIV106E18LLeft j+neutralIV106E18LWidth/2
  let r := neutralIV106E18LWidth/2+neutralIV106E18LBuffer
  let S := neutralIV106E18JSpace c r
  have hh : 0 < neutralIV106E18LWidth := by norm_num [neutralIV106E18LWidth]
  have hb : 0 < neutralIV106E18LBuffer := by norm_num [neutralIV106E18LBuffer]
  let v : S := ⟨neutralIV106E18OTrial j,
    neutralIV106E18JTrial_closure _ _ _ hh hb⟩
  let T : S →L[ℂ] ((ℂ × ℂ) × (ℂ × (Fin k → ℂ))) :=
    (neutralIV106E18RObserve k hk).domRestrict S
  obtain ⟨w,hw,hT,hdist⟩ := neutralIV106E18RAffine_match
    (neutralIV106E18JLocalCore c r) (neutralIV106E18JLocal_dense c r)
    T v ε hε
  change (w : RealComplexL2) ∈ neutralIV106E18JCore c r at hw
  obtain ⟨s,hs,he⟩ := hw
  have hObs : neutralIV106E18RObserve k hk (s.toLp 2 volume) =
      neutralIV106E18RObserve k hk (neutralIV106E18OTrial j) := by
    change neutralIV106E18RObserve k hk (w : RealComplexL2) =
      neutralIV106E18RObserve k hk (neutralIV106E18OTrial j) at hT
    rwa [he] at hT
  have hclose : dist (s.toLp 2 volume) (neutralIV106E18OTrial j) < ε := by
    change dist (w : RealComplexL2) (neutralIV106E18OTrial j) < ε at hdist
    rwa [he] at hdist
  have hwin : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), s x = 0 :=
    fun x hx => hs x (fun hm => hx (neutralIV106E18LWindow j hj hm))
  have hdis : ∀ x ∈ closedBall c r, x ∉ Set.Icc (4393/4000:ℝ) (4399/4000) := by
    intro x hx hx'
    have h := neutralIV106E18LGap j hj x hx' x hx
    norm_num at h
  have hcell : Set.Icc (neutralIV106E18LLeft j)
      (neutralIV106E18LLeft j+neutralIV106E18LWidth) ⊆
      Set.Icc (-(11/10:ℝ)) (11/10) := by
    intro x hx
    apply neutralIV106E18LWindow j hj
    rw [mem_closedBall,Real.dist_eq,abs_le]
    constructor <;> linarith [hx.1,hx.2]
  obtain ⟨hm,hmean⟩ := neutralIV106E18RObserve_moments k hk _ _ hObs
  refine ⟨s,hs,hwin,neutralIV106E18JPacked_orth k hk s c r hs hdis,
    ?_,?_,hclose,neutralIV106E18RObserve_row k hk _ _ hObs⟩
  · rw [hm]
    exact neutralIV106E18K2Both_moments _ _ _ hh hcell
  · rw [hmean]
    exact neutralIV106E18K2Moment_zero _ _ _ 0 hh hcell (Or.inl rfl)

/-- Exact original arithmetic response and log-carrier admission of the
matching smooth vector. No quantitative log-energy bound is claimed. -/
theorem neutralIV106E18RBank (k : ℕ) (hk : 0 < k) (hk34 : k ≤ 34)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : Fin k → 𝓢(ℝ,ℂ), ∀ j : Fin k,
      (∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), s j x = 0) ∧
      neutralIV101MassComplement k hk (s j) ∧
      neutralIV106E18HMoments (11/10:ℝ) ((s j).toLp 2 volume) = 0 ∧
      sourceWindowMoment (11/10:ℝ) 0 ((s j).toLp 2 volume) = 0 ∧
      dist ((s j).toLp 2 volume) (neutralIV106E18OTrial (j.val+1)) < ε ∧
      (∃ p : NeutralLogHilbertCarrier (11/10:ℝ),
        neutralLogPhysical p.val = (s j).toLp 2 volume) ∧
      (∀ i : Fin k, neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) (s j) =
        (neutralIV106E18OMatrix k hk i j : ℂ)) := by
  classical
  have h j := neutralIV106E18RCell_match k hk (j.val+1)
    (neutralIV106E18OConsecutive k hk34 j) ε hε
  choose s hs using h
  refine ⟨s,?_⟩
  intro j
  obtain ⟨_,hwin,horth,hm,hmean,hd,hrow⟩ := hs j
  refine ⟨hwin,horth,hm,hmean,hd,
    ⟨neutralIV102Lift _ (s j) hwin,neutralIV102Lift_physical _ (s j) hwin⟩,?_⟩
  intro i
  rw [neutralIV105CResponse_pair k hk i (s j) hwin horth,hrow i]
  exact neutralIV106E18OMatrix_literal k hk hk34 i j

#print axioms neutralIV106E18RAffine_match
#print axioms neutralIV106E18RObserve_moments
#print axioms neutralIV106E18RObserve_row
#print axioms neutralIV106E18RCell_match
#print axioms neutralIV106E18RBank
end
end WeilDefect
