import WeilDefect.Arithmetic.ActualZetaIV106E18ILocalSmoothing

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Physical images of Schwartz functions supported in the fixed buffered cell. -/
def neutralIV106E18JCore (c R : ℝ) : Submodule ℂ RealComplexL2 where
  carrier := {v | ∃ s : 𝓢(ℝ,ℂ),
    (∀ x ∉ closedBall c R, s x = 0) ∧ v = s.toLp 2 volume}
  zero_mem' := by
    refine ⟨0, fun _ _ => rfl, ?_⟩
    change 0 = SchwartzMap.toLpCLM ℂ ℂ 2 volume 0
    rw [map_zero]
  add_mem' := by
    rintro v w ⟨s,hs,rfl⟩ ⟨t,ht,rfl⟩
    refine ⟨s+t, ?_, ?_⟩
    · intro x hx
      change s x+t x = 0
      rw [hs x hx,ht x hx,add_zero]
    · change SchwartzMap.toLpCLM ℂ ℂ 2 volume s +
        SchwartzMap.toLpCLM ℂ ℂ 2 volume t =
        SchwartzMap.toLpCLM ℂ ℂ 2 volume (s+t)
      rw [map_add]
  smul_mem' := by
    rintro z v ⟨s,hs,rfl⟩
    refine ⟨z • s, ?_, ?_⟩
    · intro x hx
      change z • s x = 0
      rw [hs x hx,smul_zero]
    · change z • SchwartzMap.toLpCLM ℂ ℂ 2 volume s =
        SchwartzMap.toLpCLM ℂ ℂ 2 volume (z • s)
      rw [map_smul]

abbrev neutralIV106E18JSpace (c R : ℝ) :=
  (neutralIV106E18JCore c R).topologicalClosure

def neutralIV106E18JLocalCore (c R : ℝ) :
    Submodule ℂ (neutralIV106E18JSpace c R) :=
  (neutralIV106E18JCore c R).comap (neutralIV106E18JSpace c R).subtype

/-- Density is internal to the closure; no claim that this is all L2 on the cell. -/
theorem neutralIV106E18JLocal_dense (c R : ℝ) :
    Dense (neutralIV106E18JLocalCore c R : Set (neutralIV106E18JSpace c R)) := by
  intro q
  apply Metric.mem_closure_iff.mpr
  intro ε hε
  have hq : (q : RealComplexL2) ∈ closure (neutralIV106E18JCore c R : Set RealComplexL2) :=
    q.property
  obtain ⟨v,hv,hd⟩ := Metric.mem_closure_iff.mp hq ε hε
  let w : neutralIV106E18JSpace c R :=
    ⟨v,(neutralIV106E18JCore c R).le_topologicalClosure hv⟩
  refine ⟨w,hv,?_⟩
  exact hd

theorem neutralIV106E18JIndicator_memLp (c R : ℝ) :
    MemLp ((closedBall c R).indicator (fun _ : ℝ => (1:ℂ))) 2 volume := by
  have hm : MeasurableSet (closedBall c R) := measurableSet_closedBall
  apply (memLp_two_iff_integrable_sq_norm
    (aestronglyMeasurable_const.indicator hm)).mpr
  have hi : IntegrableOn (fun _ : ℝ => (1:ℝ)) (closedBall c R) volume :=
    continuous_const.integrableOn_isCompact (isCompact_closedBall _ _)
  apply (hi.integrable_indicator hm).congr
  filter_upwards [] with x
  by_cases hx : x ∈ closedBall c R <;> simp [hx]

/-- A compact continuous representative itself belongs to the buffered
Schwartz closure, by the uniform approximation already constructed. -/
theorem neutralIV106E18JClosure_mem (f : ℝ → ℂ) (hf : Continuous f)
    (c r R : ℝ) (hr : 0 < r) (hR : r < R)
    (hs : ∀ x ∉ closedBall c r, f x = 0) (hf2 : MemLp f 2 volume) :
    hf2.toLp f ∈ neutralIV106E18JSpace c R := by
  change hf2.toLp f ∈ closure (neutralIV106E18JCore c R : Set RealComplexL2)
  apply Metric.mem_closure_iff.mpr
  intro ε hε
  let B : RealComplexL2 := (neutralIV106E18JIndicator_memLp c R).toLp _
  let η : ℝ := ε/(‖B‖+1)
  have hη : 0 < η := div_pos hε (by positivity)
  obtain ⟨s,hsout,hsclose⟩ := neutralIV106E18ISmooth_local f hf c r R hr hR hs η hη
  refine ⟨s.toLp 2 volume,⟨s,hsout,rfl⟩,?_⟩
  have hb : ∀ᵐ x ∂volume, ‖s x-f x‖ ≤ η*‖B x‖ := by
    filter_upwards [(neutralIV106E18JIndicator_memLp c R).coeFn_toLp] with x hx
    change ‖s x-f x‖ ≤ η*‖(neutralIV106E18JIndicator_memLp c R).toLp _ x‖
    rw [hx]
    by_cases hmem : x ∈ closedBall c R
    · simpa [hmem] using (hsclose x).le
    · have hsmall : x ∉ closedBall c r := by
        intro h
        exact hmem (closedBall_subset_closedBall hR.le h)
      simp [hsout x hmem,hs x hsmall,hmem]
  have herror := neutralIV106E18IL2_error f hf2 s B η hb
  rw [dist_comm,dist_eq_norm]
  apply herror.trans_lt
  dsimp [η]
  rw [div_mul_eq_mul_div]
  apply (div_lt_iff₀ (by positivity : 0 < ‖B‖+1)).mpr
  nlinarith only [hε]

/-- The genuine IV100 packed carrier is zero outside its narrow right collar,
not just outside the union of the two original collars. -/
theorem neutralIV106E18JCarrier_zero (k : ℕ) (hk : 0 < k) (i : Fin k)
    (x : ℝ) (hx : x ∉ Set.Icc (4393/4000:ℝ) (4399/4000)) :
    neutralIV100Carrier k hk i x = 0 := by
  have hz : (3/4000:ℝ) ≤ |(k:ℝ)*x+neutralIV100PackShift k i.val-1099/1000| := by
    by_contra hn
    obtain ⟨hl,hu⟩ := neutralIV100Pack_containment k i.val hk i.isLt x (lt_of_not_ge hn)
    exact hx ⟨by linarith,by linarith⟩
  change (neutralIV097Plateau ((k:ℝ)*x+neutralIV100PackShift k i.val) : ℂ) = 0
  simp [neutralIV097Plateau_zero _ hz]

/-- Buffered support disjoint from the packed collar automatically gives
orthogonality to the ENTIRE packed sector, not just the chosen response row. -/
theorem neutralIV106E18JPacked_orth (k : ℕ) (hk : 0 < k)
    (s : 𝓢(ℝ,ℂ)) (c R : ℝ)
    (hs : ∀ x ∉ closedBall c R, s x = 0)
    (hdis : ∀ x ∈ closedBall c R, x ∉ Set.Icc (4393/4000:ℝ) (4399/4000)) :
    neutralIV101MassComplement k hk s := by
  intro z
  rw [L2.inner_def]
  have hz : (fun x : ℝ => inner ℂ ((neutralIV100Packed k hk z).toLp 2 volume x)
      (s.toLp 2 volume x)) =ᵐ[volume] (fun _ => 0) := by
    filter_upwards [(neutralIV100Packed k hk z).coeFn_toLp 2 volume,
      s.coeFn_toLp 2 volume] with x hx hy
    rw [hx,hy]
    by_cases h : x ∈ closedBall c R
    · have hp : neutralIV100Packed k hk z x = 0 := by
        unfold neutralIV100Packed
        rw [neutralIV099Sector_apply]
        apply Finset.sum_eq_zero
        intro j hj
        rw [neutralIV106E18JCarrier_zero k hk j x (hdis x h),mul_zero]
      simp [hp]
    · simp [hs x h]
  rw [integral_congr_ae hz]
  simp

/-- Generic buffered geometry is expressed as inequalities between closed
intervals; the finite rational census must still be attached natively. -/
theorem neutralIV106E18JResponse (k : ℕ) (hk : 0 < k) (i : Fin k)
    (f : ℝ → ℂ) (hf : Continuous f)
    (c r R : ℝ) (hr : 0 < r) (hR : r < R)
    (hs : ∀ x ∉ closedBall c r, f x = 0) (hf2 : MemLp f 2 volume)
    (hwin : closedBall c R ⊆ Set.Icc (-(11/10:ℝ)) (11/10))
    {δ : ℝ} (hδ : 0 < δ)
    (hgap : ∀ x ∈ Set.Icc (4393/4000:ℝ) (4399/4000),
      ∀ y ∈ closedBall c R, δ ≤ |x-y|)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset (11/10:ℝ), ∀ x ∈ closedBall c R,
      x-Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000) ∧
      x+Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000))
    (hm : neutralIV106E18HMoments (11/10:ℝ) (hf2.toLp f) = 0) :
    inner ℂ (neutralIV105CResponse k hk i) (hf2.toLp f) =
    ∫ x, conj (neutralIV100Carrier k hk i x) * (∫ y, f y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  let q : neutralIV106E18JSpace c R :=
    ⟨hf2.toLp f,neutralIV106E18JClosure_mem f hf c r R hr hR hs hf2⟩
  have hdis : ∀ x ∈ closedBall c R, x ∉ Set.Icc (4393/4000:ℝ) (4399/4000) := by
    intro x hx hx'
    have hh := hgap x hx' x hx
    simp at hh
    linarith
  have hgeom (s : 𝓢(ℝ,ℂ)) (hs' : ∀ x ∉ closedBall c R, s x = 0) :
      (∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), s x = 0) ∧
      neutralIV101MassComplement k hk s ∧
      (∀ x y, neutralIV100Carrier k hk i x ≠ 0 → s y ≠ 0 → δ ≤ |x-y|) ∧
      (∀ n ∈ rightLimitPrimePowerFinset (11/10:ℝ), ∀ x : ℝ, s x ≠ 0 →
        neutralIV100Carrier k hk i (x-Real.log n) = 0 ∧
        neutralIV100Carrier k hk i (x+Real.log n) = 0) := by
    refine ⟨fun x hx => hs' x (fun h => hx (hwin h)),
      neutralIV106E18JPacked_orth k hk s c R hs' hdis, ?_, ?_⟩
    · intro x y hx hy
      exact hgap x (by_contra fun h => hx (neutralIV106E18JCarrier_zero k hk i x h))
        y (by_contra fun h => hy (hs' y h))
    · intro n hn x hx
      obtain ⟨hl,hr⟩ := hshift n hn x (by_contra fun h => hx (hs' x h))
      exact ⟨neutralIV106E18JCarrier_zero k hk i _ hl,
        neutralIV106E18JCarrier_zero k hk i _ hr⟩
  have hfout : ∀ x ∉ closedBall c R, f x = 0 :=
    fun x hx => hs x (fun h => hx (closedBall_subset_closedBall hR.le h))
  have hfi : Integrable f :=
    hf.integrable_of_hasCompactSupport
      (HasCompactSupport.intro (K := closedBall c r) (isCompact_closedBall _ _) hs)
  change inner ℂ (neutralIV105CResponse k hk i) (q : RealComplexL2) = _
  apply neutralIV106E18HResponse_rough k hk i hδ
    (neutralIV106E18JSpace c R) (neutralIV106E18JLocalCore c R)
    (neutralIV106E18JLocal_dense c R) _ q hm f hfi hf2.coeFn_toLp
  · intro v hv
    obtain ⟨s,hs',he⟩ := hv
    obtain ⟨hw,ho,hg,hp⟩ := hgeom s hs'
    exact ⟨s,he,hw,ho,hg,hp⟩
  · intro x hx
    exact hfout x (fun h => hx (hwin h))
  · intro x y hx hy
    exact hgap x (by_contra fun h => hx (neutralIV106E18JCarrier_zero k hk i x h))
      y (by_contra fun h => hy (hfout y h))

/-- The literal E18A clipped polynomial is square integrable, independently
of any logarithmic or strong-action admission theorem. -/
theorem neutralIV106E18JTrial_memLp (l h : ℝ) (hh : 0 < h) :
    MemLp (neutralIV106E18ITrial l h) 2 volume := by
  have hc := neutralIV106E18ITrial_continuous l h
  have hs := neutralIV106E18ITrial_compact l h hh
  apply (memLp_two_iff_integrable_sq_norm hc.aestronglyMeasurable).mpr
  apply (hc.norm.pow 2).integrable_of_hasCompactSupport
  apply HasCompactSupport.intro (K := Set.Icc l (l+h)) isCompact_Icc
  intro x hx
  simp [neutralIV106E18ITrial_outside l h hh x hx]

theorem neutralIV106E18JTrial_ball (l h : ℝ) (hh : 0 < h) (x : ℝ)
    (hx : x ∉ closedBall (l+h/2) (h/2)) :
    neutralIV106E18ITrial l h x = 0 := by
  apply neutralIV106E18ITrial_outside l h hh x
  intro hx'
  apply hx
  rw [mem_closedBall,Real.dist_eq,abs_le]
  constructor <;> linarith [hx'.1,hx'.2]

/-- The actual polynomial is in the buffered physical closure. -/
theorem neutralIV106E18JTrial_closure (l h ε : ℝ) (hh : 0 < h) (hε : 0 < ε) :
    (neutralIV106E18JTrial_memLp l h hh).toLp _ ∈
      neutralIV106E18JSpace (l+h/2) (h/2+ε) :=
  neutralIV106E18JClosure_mem _ (neutralIV106E18ITrial_continuous l h)
    (l+h/2) (h/2) (h/2+ε) (by positivity) (by linarith)
    (neutralIV106E18JTrial_ball l h hh) (neutralIV106E18JTrial_memLp l h hh)

/-- Actual E18A polynomial response receiver, conditional on the remaining
literal geometry and two exponential moment identities. -/
theorem neutralIV106E18JTrial_response (k : ℕ) (hk : 0 < k) (i : Fin k)
    (l h ε : ℝ) (hh : 0 < h) (hε : 0 < ε)
    (hwin : closedBall (l+h/2) (h/2+ε) ⊆ Set.Icc (-(11/10:ℝ)) (11/10))
    {δ : ℝ} (hδ : 0 < δ)
    (hgap : ∀ x ∈ Set.Icc (4393/4000:ℝ) (4399/4000),
      ∀ y ∈ closedBall (l+h/2) (h/2+ε), δ ≤ |x-y|)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset (11/10:ℝ),
      ∀ x ∈ closedBall (l+h/2) (h/2+ε),
      x-Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000) ∧
      x+Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000))
    (hm : neutralIV106E18HMoments (11/10:ℝ)
      ((neutralIV106E18JTrial_memLp l h hh).toLp _) = 0) :
    inner ℂ (neutralIV105CResponse k hk i)
      ((neutralIV106E18JTrial_memLp l h hh).toLp _) =
    ∫ x, conj (neutralIV100Carrier k hk i x) *
      (∫ y, neutralIV106E18ITrial l h y *
        ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) :=
  neutralIV106E18JResponse k hk i _ (neutralIV106E18ITrial_continuous l h)
    (l+h/2) (h/2) (h/2+ε) (by positivity) (by linarith)
    (neutralIV106E18JTrial_ball l h hh) (neutralIV106E18JTrial_memLp l h hh)
    hwin hδ hgap hshift hm

#print axioms neutralIV106E18JTrial_memLp
#print axioms neutralIV106E18JTrial_ball
#print axioms neutralIV106E18JTrial_closure
#print axioms neutralIV106E18JTrial_response
#print axioms neutralIV106E18JLocal_dense
#print axioms neutralIV106E18JIndicator_memLp
#print axioms neutralIV106E18JClosure_mem
#print axioms neutralIV106E18JCarrier_zero
#print axioms neutralIV106E18JPacked_orth
#print axioms neutralIV106E18JResponse
end
end WeilDefect
