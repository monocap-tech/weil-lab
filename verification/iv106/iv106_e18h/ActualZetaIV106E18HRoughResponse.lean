import WeilDefect.Arithmetic.ActualZetaIV106E18GHermitianAttachment
import WeilDefect.Arithmetic.ActualZetaIV106C3ConstraintDensity
import Mathlib.MeasureTheory.Integral.Prod

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate

/-- The signed gap kernel is real and even, with no distributional convention. -/
theorem neutralIV106E18HKernel_symm (δ x y : ℝ) :
    conj (archimedeanGapKernelComplex δ (y-x)) =
      archimedeanGapKernelComplex δ (x-y) := by
  simp only [archimedeanGapKernelComplex, Complex.conj_ofReal, archimedeanGapKernel]
  rw [abs_sub_comm y x]

/-- On the finite window the fixed gap convolution is an actual L2 column. -/
theorem neutralIV106E18HColumn_memLp (a : ℝ) (u : 𝓢(ℝ,ℂ))
    {δ : ℝ} (hδ : 0 < δ) :
    MemLp ((Set.Icc (-a) a).indicator (neutralIV106E18EGap u δ)) 2 volume := by
  have hc := neutralIV106E18EGap_continuous u u.integrable hδ
  have hm : AEStronglyMeasurable ((Set.Icc (-a) a).indicator
      (neutralIV106E18EGap u δ)) volume :=
    hc.aestronglyMeasurable.indicator measurableSet_Icc
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hi : IntegrableOn (fun x => ‖neutralIV106E18EGap u δ x‖^2)
      (Set.Icc (-a) a) volume :=
    (hc.norm.pow 2).integrableOn_Icc
  apply (hi.integrable_indicator measurableSet_Icc).congr
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;> simp [hx]

def neutralIV106E18HColumn (a : ℝ) (u : 𝓢(ℝ,ℂ))
    {δ : ℝ} (hδ : 0 < δ) : RealComplexL2 :=
  (neutralIV106E18HColumn_memLp a u hδ).toLp _

theorem neutralIV106E18HColumn_pair (a : ℝ) (u : 𝓢(ℝ,ℂ))
    {δ : ℝ} (hδ : 0 < δ) (v : RealComplexL2) :
    inner ℂ (neutralIV106E18HColumn a u hδ) v =
      ∫ y in Set.Icc (-a) a, conj (neutralIV106E18EGap u δ y) * v y := by
  rw [L2.inner_def, ← integral_indicator
    (show MeasurableSet (Set.Icc (-a) a) from measurableSet_Icc)]
  apply integral_congr_ae
  filter_upwards [(neutralIV106E18HColumn_memLp a u hδ).coeFn_toLp] with y hy
  change inner ℂ ((neutralIV106E18HColumn_memLp a u hδ).toLp _ y) (v y) = _
  rw [hy]
  by_cases hy' : y ∈ Set.Icc (-a) a <;> simp [hy', RCLike.inner_apply', mul_comm]

/-- Fubini is applied only to the bounded gap kernel and two L1 factors. -/
theorem neutralIV106E18HFubini (u : 𝓢(ℝ,ℂ)) (v : ℝ → ℂ)
    (hv : Integrable v) {δ : ℝ} (hδ : 0 < δ) :
    (∫ x, conj (u x) * (∫ y, v y * archimedeanGapKernelComplex δ (x-y))) =
      ∫ y, conj (neutralIV106E18EGap u δ y) * v y := by
  let F : ℝ × ℝ → ℂ := fun z =>
    conj (u z.1) * (v z.2 * archimedeanGapKernelComplex δ (z.1-z.2))
  let C : ℝ := 1/(1-Real.exp (-2*δ))
  have hk : Continuous (fun z : ℝ × ℝ =>
      archimedeanGapKernelComplex δ (z.1-z.2)) :=
    (archimedeanGapKernelComplex_continuous hδ).comp
      (continuous_fst.sub continuous_snd)
  have hF : Integrable F (volume.prod volume) := by
    apply ((u.integrable.norm.mul_prod hv.norm).mul_const C).mono'
    · exact ((Complex.continuous_conj.comp u.continuous).aestronglyMeasurable.comp_fst.mul
        (hv.aestronglyMeasurable.comp_snd.mul hk.aestronglyMeasurable))
    · filter_upwards [] with z
      dsimp [F]
      simp only [norm_mul, Complex.norm_conj]
      calc
        _ ≤ ‖u z.1‖ * (‖v z.2‖ * C) := by
          gcongr
          exact archimedeanGapKernelComplex_norm_bound hδ _
        _ = _ := by ring
  calc
    _ = ∫ x, ∫ y, F (x,y) := by
      apply integral_congr_ae
      filter_upwards [] with x
      dsimp [F]
      rw [integral_const_mul]
    _ = ∫ y, ∫ x, F (x,y) := integral_integral_swap hF
    _ = _ := by
      apply integral_congr_ae
      filter_upwards [] with y
      unfold neutralIV106E18EGap
      simp only [MeasureTheory.convolution_def, ContinuousLinearMap.mul_apply']
      rw [← integral_conj, ← integral_mul_const]
      apply integral_congr_ae
      filter_upwards [] with x
      dsimp [F]
      rw [map_mul, neutralIV106E18HKernel_symm]
      ring

/-- Positive support gap removes the cutoff only on the nonzero product. -/
theorem neutralIV106E18HUncut (u : 𝓢(ℝ,ℂ)) (v : ℝ → ℂ)
    {δ : ℝ} (hsep : ∀ x y, u x ≠ 0 → v y ≠ 0 → δ ≤ |x-y|) :
    (∫ x, conj (u x) * (∫ y, v y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ))) =
    ∫ x, conj (u x) * (∫ y, v y * archimedeanGapKernelComplex δ (x-y)) := by
  apply integral_congr_ae
  filter_upwards [] with x
  by_cases hx : u x = 0
  · simp [hx]
  congr 1
  apply integral_congr_ae
  filter_upwards [] with y
  by_cases hy : v y = 0
  · simp [hy]
  rw [archimedeanGapKernelComplex_eq_offDiagonal (hsep x y hx hy)]

theorem neutralIV106E18HSchwartz_pair (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    {δ : ℝ} (hδ : 0 < δ)
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0)
    (hsep : ∀ x y, u x ≠ 0 → v y ≠ 0 → δ ≤ |x-y|) :
    (∫ x, conj (u x) * (∫ y, v y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ))) =
      inner ℂ (neutralIV106E18HColumn a u hδ) (v.toLp 2 volume) := by
  rw [neutralIV106E18HUncut u v hsep,
    neutralIV106E18HFubini u v v.integrable hδ,
    neutralIV106E18HColumn_pair]
  symm
  calc
    _ = ∫ y in Set.Icc (-a) a, conj (neutralIV106E18EGap u δ y) * v y := by
      apply integral_congr_ae
      filter_upwards [ae_restrict_of_ae (v.coeFn_toLp 2 volume)] with y hy
      rw [hy]
    _ = _ := by
      apply setIntegral_eq_integral_of_forall_compl_eq_zero
      intro y hy
      simp [hv y hy]

/-- Exact response equality on the Schwartz core, now between two L2 columns. -/
theorem neutralIV106E18HResponse_core (k : ℕ) (hk : 0 < k) (i : Fin k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), v x = 0)
    (horth : neutralIV101MassComplement k hk v)
    {δ : ℝ} (hδ : 0 < δ)
    (hsep : ∀ x y, neutralIV100Carrier k hk i x ≠ 0 → v y ≠ 0 → δ ≤ |x-y|)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset (11/10:ℝ), ∀ x : ℝ, v x ≠ 0 →
      neutralIV100Carrier k hk i (x-Real.log n) = 0 ∧
      neutralIV100Carrier k hk i (x+Real.log n) = 0)
    (hm : sourceWindowMoment (11/10:ℝ) (-(1/2)) (v.toLp 2 volume) = 0)
    (hp : sourceWindowMoment (11/10:ℝ) (1/2) (v.toLp 2 volume) = 0) :
    inner ℂ (neutralIV105CResponse k hk i) (v.toLp 2 volume) =
      inner ℂ (neutralIV106E18HColumn (11/10:ℝ) (neutralIV100Carrier k hk i) hδ)
        (v.toLp 2 volume) := by
  rw [neutralIV106E18GResponse_literal k hk i v hv horth hδ hsep hshift hm hp]
  exact neutralIV106E18HSchwartz_pair _ _ v hδ hv hsep

/-- Exact two pole moments, as a finite-dimensional continuous constraint
on the physical L2 space, not the logarithmic carrier. -/
def neutralIV106E18HMoments (a : ℝ) : RealComplexL2 →L[ℂ] (ℂ × ℂ) :=
  (neutralSourceWindowMomentCLM a (-(1/2))).prod
    (neutralSourceWindowMomentCLM a (1/2))

theorem neutralIV106E18HMoments_zero (a : ℝ) (v : RealComplexL2) :
    neutralIV106E18HMoments a v = 0 ↔
      sourceWindowMoment a (-(1/2)) v = 0 ∧
      sourceWindowMoment a (1/2) v = 0 := by
  simp [neutralIV106E18HMoments, neutralSourceWindowMomentCLM_eq, Prod.ext_iff]

/-- The equality extends to any rough physical vector in the closure of
the eligible core, with no strong spectral action on the rough vector. -/
theorem neutralIV106E18HClosure (r g : RealComplexL2) (A : Set RealComplexL2)
    (hA : ∀ v ∈ A, inner ℂ r v = inner ℂ g v)
    (v : RealComplexL2) (hv : v ∈ closure A) :
    inner ℂ r v = inner ℂ g v := by
  have hc : IsClosed {x : RealComplexL2 | inner ℂ r x = inner ℂ g x} :=
    isClosed_eq ((continuous_const : Continuous (fun _ : RealComplexL2 => r)).inner continuous_id)
      ((continuous_const : Continuous (fun _ : RealComplexL2 => g)).inner continuous_id)
  exact closure_minimal hA hc hv

/-- Local constrained-density transport: S is a physical cell subspace;
D is any dense linear smooth core in S. Density must still be instantiated
on the actual cell. No independence of the two moments is required. -/
theorem neutralIV106E18HConstrained (a : ℝ) (S : Submodule ℂ RealComplexL2)
    (D : Submodule ℂ S) (hd : Dense (D : Set S))
    (r g : RealComplexL2)
    (hcore : ∀ v ∈ D, neutralIV106E18HMoments a (v : RealComplexL2) = 0 →
      inner ℂ r (v : RealComplexL2) = inner ℂ g (v : RealComplexL2))
    (v : S) (hv : neutralIV106E18HMoments a (v : RealComplexL2) = 0) :
    inner ℂ r (v : RealComplexL2) = inner ℂ g (v : RealComplexL2) := by
  let T : S →L[ℂ] (ℂ × ℂ) := (neutralIV106E18HMoments a).domRestrict S
  let A : Set S := (D : Set S) ∩ {x | T x = 0}
  have hc : IsClosed {x : S | inner ℂ r (x : RealComplexL2) =
      inner ℂ g (x : RealComplexL2)} :=
    isClosed_eq ((continuous_const : Continuous (fun _ : S => r)).inner continuous_subtype_val)
      ((continuous_const : Continuous (fun _ : S => g)).inner continuous_subtype_val)
  have hs : A ⊆ {x : S | inner ℂ r (x : RealComplexL2) =
      inner ℂ g (x : RealComplexL2)} := by
    intro x hx
    exact hcore x hx.1 hx.2
  have hh : v ∈ closure A := by
    change v ∈ closure ((D : Set S) ∩ {x | T x = 0})
    rw [neutralIV106C3Closure D hd T]
    exact hv
  exact closure_minimal hs hc hh

/-- The actual IV105C row on a rough representative in a locally dense
physical subspace. The only remaining approximation premise is the local
core density and its stated geometry; no rough strong action is assumed. -/
theorem neutralIV106E18HResponse_rough (k : ℕ) (hk : 0 < k) (i : Fin k)
    {δ : ℝ} (hδ : 0 < δ)
    (S : Submodule ℂ RealComplexL2) (D : Submodule ℂ S)
    (hd : Dense (D : Set S))
    (hD : ∀ q ∈ D, ∃ s : 𝓢(ℝ,ℂ),
      (q : RealComplexL2) = s.toLp 2 volume ∧
      (∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), s x = 0) ∧
      neutralIV101MassComplement k hk s ∧
      (∀ x y, neutralIV100Carrier k hk i x ≠ 0 → s y ≠ 0 → δ ≤ |x-y|) ∧
      (∀ n ∈ rightLimitPrimePowerFinset (11/10:ℝ), ∀ x : ℝ, s x ≠ 0 →
        neutralIV100Carrier k hk i (x-Real.log n) = 0 ∧
        neutralIV100Carrier k hk i (x+Real.log n) = 0))
    (v : S) (hv : neutralIV106E18HMoments (11/10:ℝ) (v : RealComplexL2) = 0)
    (f : ℝ → ℂ) (hf : Integrable f)
    (hrep : ((v : RealComplexL2) : ℝ → ℂ) =ᵐ[volume] f)
    (hwin : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), f x = 0)
    (hsep : ∀ x y, neutralIV100Carrier k hk i x ≠ 0 → f y ≠ 0 → δ ≤ |x-y|) :
    inner ℂ (neutralIV105CResponse k hk i) (v : RealComplexL2) =
    ∫ x, conj (neutralIV100Carrier k hk i x) * (∫ y, f y *
      ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  let u := neutralIV100Carrier k hk i
  have he : inner ℂ (neutralIV105CResponse k hk i) (v : RealComplexL2) =
      inner ℂ (neutralIV106E18HColumn (11/10:ℝ) u hδ) (v : RealComplexL2) := by
    apply neutralIV106E18HConstrained (11/10:ℝ) S D hd _ _ _ v hv
    intro q hq hm
    obtain ⟨s,hs,hswin,hsorth,hssep,hshift⟩ := hD q hq
    rw [hs] at hm ⊢
    obtain ⟨hm,hp⟩ := (neutralIV106E18HMoments_zero _ _).mp hm
    exact neutralIV106E18HResponse_core k hk i s hswin hsorth hδ hssep hshift hm hp
  rw [he, neutralIV106E18HColumn_pair,
    neutralIV106E18HUncut u f hsep, neutralIV106E18HFubini u f hf hδ]
  calc
    _ = ∫ y in Set.Icc (-(11/10:ℝ)) (11/10), conj (neutralIV106E18EGap u δ y) * f y := by
      apply integral_congr_ae
      filter_upwards [ae_restrict_of_ae hrep] with y hy
      rw [hy]
    _ = _ := by
      apply setIntegral_eq_integral_of_forall_compl_eq_zero
      intro y hy
      simp [hwin y hy]

#print axioms neutralIV106E18HResponse_rough
#print axioms neutralIV106E18HKernel_symm
#print axioms neutralIV106E18HColumn_memLp
#print axioms neutralIV106E18HColumn_pair
#print axioms neutralIV106E18HFubini
#print axioms neutralIV106E18HUncut
#print axioms neutralIV106E18HSchwartz_pair
#print axioms neutralIV106E18HResponse_core
#print axioms neutralIV106E18HMoments_zero
#print axioms neutralIV106E18HClosure
#print axioms neutralIV106E18HConstrained
end
end WeilDefect
