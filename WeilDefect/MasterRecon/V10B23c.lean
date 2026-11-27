import WeilDefect.MasterRecon.V10B23b

/-! V10B23c: full sesquilinear physical-action attachment to the
logarithmic carrier. This does not require smoothness of the receiving
test vector or any pointwise evaluation of the Bochner integral. -/
namespace WeilDefect.MasterRecon.V10B23c

open MeasureTheory Set Filter Complex
open scoped InnerProduct FourierTransform ComplexConjugate
open V08I (FullL2 logCarrier physicalInclusion logWeight)
open V10B8e (archOperator correction spectralPhysical residual gammaSymbol)
open V10B23b (archAction SeriesSupply)
open V10B22b (U)
open V10B21c (actionTerm)

theorem weighted_cross_ae (t : ℝ) (g h : logCarrier t) :
    (fun u => inner ℂ ((g:FullL2) u) ((h:FullL2) u)) =ᵐ[volume]
      fun u => (logWeight u:ℂ)*inner ℂ ((spectralPhysical t g) u) ((spectralPhysical t h) u) := by
  filter_upwards [V08I.physicalInclusion_fourier_ae t g,
    V08I.physicalInclusion_fourier_ae t h] with u hg hh
  change inner ℂ ((g:FullL2) u) ((h:FullL2) u) =
    (logWeight u:ℂ)*inner ℂ ((𝓕 (physicalInclusion t g):FullL2) u)
      ((𝓕 (physicalInclusion t h):FullL2) u)
  rw [hg,hh]
  simp only [RCLike.inner_apply',map_mul,V08I.inverseWeight,Complex.conj_ofReal]
  have hw := V08I.logWeight_pos u
  have hs := Real.sqrt_pos.2 hw
  have he : (logWeight u:ℂ)*(((Real.sqrt (logWeight u))⁻¹:ℝ):ℂ)^2 = 1 := by
    rw [← Complex.ofReal_pow,← Complex.ofReal_mul]
    congr 1
    rw [inv_pow,Real.sq_sqrt hw.le,mul_inv_cancel₀ hw.ne']
  calc
    _ = 1*(conj ((g:FullL2) u)*((h:FullL2) u)) := by ring
    _ = _ := by rw [← he]; ring

theorem carrier_arch_pairing (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C)
    (g h : logCarrier t)
    (hD : IntegrableOn (actionTerm (physicalInclusion t g)) (Ioi 0))
    (hS : SeriesSupply) :
    inner ℂ (archOperator t hd C hC g) h =
      inner ℂ (archAction (physicalInclusion t g)) (physicalInclusion t h) := by
  let f := physicalInclusion t g
  let k := physicalInclusion t h
  let F := spectralPhysical t g
  let K := spectralPhysical t h
  let R := V10B8e.realMultiplier residual hd C hC F
  have hf : Integrable (fun x : ℝ => f x) :=
    V08K.supported_integrable t _ (V08I.physicalInclusion_support t g)
  have hm := V10B23b.arch_multiplier_ae f hf hD hS
  have hr := V10B8e.realMultiplier_ae residual hd C hC F
  have h₁ : Integrable (fun u => inner ℂ ((g:FullL2) u) ((h:FullL2) u)) :=
    L2.integrable_inner (𝕜 := ℂ) (g:FullL2) (h:FullL2)
  have h₂ : Integrable (fun u => inner ℂ (R u) (K u)) :=
    L2.integrable_inner (𝕜 := ℂ) R K
  have hleft : inner ℂ (archOperator t hd C hC g) h =
      (∫ u, inner ℂ ((g:FullL2) u) ((h:FullL2) u))+
        ∫ u, inner ℂ (R u) (K u) := by
    unfold archOperator correction
    rw [ContinuousLinearMap.add_apply,ContinuousLinearMap.one_apply,inner_add_left]
    simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]
    change inner ℂ (g:FullL2) (h:FullL2)+inner ℂ R K = _
    rw [L2.inner_def,L2.inner_def]
  rw [hleft,← integral_add h₁ h₂]
  change _ = inner ℂ (archAction f) k
  rw [← (Lp.fourierTransformₗᵢ ℝ ℂ).inner_map_map (archAction f) k,L2.inner_def]
  apply integral_congr_ae
  filter_upwards [weighted_cross_ae t g h,hr,hm] with u hw hR hM
  change inner ℂ ((g:FullL2) u) ((h:FullL2) u)+inner ℂ (R u) (K u) =
    inner ℂ ((U (archAction f)) u) (K u)
  rw [hw]
  change R u = (residual u:ℂ)*F u at hR
  change U (archAction f) u = (gammaSymbol u:ℂ)*F u at hM
  rw [hR,hM]
  change (logWeight u:ℂ)*inner ℂ (F u) (K u)+
    inner ℂ ((residual u:ℂ)*F u) (K u) =
      inner ℂ ((gammaSymbol u:ℂ)*F u) (K u)
  simp only [RCLike.inner_apply',map_mul,Complex.conj_ofReal,residual,Complex.ofReal_sub]
  ring

theorem supported_carrier_arch_pairing (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C)
    (g h : logCarrier t) (ht : 0 ≤ t)
    (B K : ℝ) (hB : 0 ≤ B) (hK : 0 ≤ K) (p : ℝ → ℂ)
    (hb : ∀ x ∈ Icc (-t) t, ‖p x‖ ≤ B)
    (hl : ∀ x ∈ Icc (-t) t, ∀ y ∈ Icc (-t) t, ‖p x-p y‖ ≤ K*|x-y|)
    (hf : (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] V10B21b.supported (-t) t p)
    (hS : SeriesSupply) :
    inner ℂ (archOperator t hd C hC g) h =
      inner ℂ (archAction (physicalInclusion t g)) (physicalInclusion t h) :=
  carrier_arch_pairing t hd C hC g h
    (V10B22a.supported_action_integrable (-t) t B K (by linarith) hB hK p hb hl
      (physicalInclusion t g) hf) hS

end WeilDefect.MasterRecon.V10B23c

#print axioms WeilDefect.MasterRecon.V10B23c.weighted_cross_ae
#print axioms WeilDefect.MasterRecon.V10B23c.carrier_arch_pairing
#print axioms WeilDefect.MasterRecon.V10B23c.supported_carrier_arch_pairing
