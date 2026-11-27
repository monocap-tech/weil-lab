import WeilDefect.MasterRecon.V10B28b
import WeilDefect.MasterRecon.V10B22c

/-! V10B28c: physical Fubini receiver. An explicit measurable
representative of the trial is used, so no L² point evaluation is
interchanged with a Bochner integral. -/
namespace WeilDefect.MasterRecon.V10B28c

open MeasureTheory Set Filter Complex
open scoped InnerProduct ComplexConjugate
open V08I (FullL2)
open V10B21c (actionTerm numerator denominator)
open V10B22b (integratedAction)
open V10B24b (zeroExtend physicalTerm)

noncomputable def trial (t : ℝ) (p : ℝ → ℂ) (x : ℝ) : ℂ :=
  zeroExtend (2*t) p (x+t)

theorem physical_slice (t : ℝ) (p : ℝ → ℂ) (f : FullL2)
    (hf : (f : ℝ → ℂ) =ᵐ[volume] trial t p) (r : ℝ) :
    (actionTerm f r : ℝ → ℂ) =ᵐ[volume]
      fun x => physicalTerm (2*t) p (x+t) r := by
  let a : ℝ := (denominator r)⁻¹
  let c : ℝ := 2*Real.exp (-2*r)
  let d : ℝ := Real.exp (-r/2)
  let u := V10B8d.shift r f
  let v := V10B8d.shift (-r) f
  change ((a • (c • f-d • (u+v)) : FullL2) : ℝ → ℂ) =ᵐ[volume] _
  filter_upwards [Lp.coeFn_smul a (c • f-d • (u+v)),
    Lp.coeFn_sub (c • f) (d • (u+v)),Lp.coeFn_smul c f,
    Lp.coeFn_smul d (u+v),Lp.coeFn_add u v,
    V10B8d.shift_ae r f,V10B8d.shift_ae (-r) f,hf,
    V06D.ae_translate hf r,V06D.ae_translate hf (-r)] with x h₁ h₂ h₃ h₄ h₅ h₆ h₇ h₈ h₉ h₁₀
  rw [h₁,h₂,h₃,h₄,h₅]
  change u x = f (x+r) at h₆
  change v x = f (x+ -r) at h₇
  rw [h₆,h₇,h₈,h₉,h₁₀]
  unfold trial physicalTerm V10B24b.b V10B24b.k
  dsimp only [a,c,d,denominator,V10B24b.den]
  simp only [Complex.real_smul,Complex.ofReal_inv,Complex.ofReal_div,Complex.ofReal_mul]
  rw [show x+r+t=x+t+r by ring,show x+ -r+t=x+t-r by ring]
  ring

theorem physical_measurable (t : ℝ) (p : ℝ → ℂ) (hp : Measurable p) :
    Measurable (fun z : ℝ × ℝ => physicalTerm (2*t) p (z.2+t) z.1) := by
  have hz : Measurable (zeroExtend (2*t) p) := hp.indicator measurableSet_Icc
  have hb : Measurable V10B24b.b := by unfold V10B24b.b V10B24b.den; fun_prop
  have hk : Measurable V10B24b.k := by unfold V10B24b.k V10B24b.den; fun_prop
  unfold physicalTerm
  fun_prop

theorem physical_pairing (t : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (f k : FullL2) (hf : (f : ℝ → ℂ) =ᵐ[volume] trial t p)
    (hD : IntegrableOn (actionTerm f) (Ioi 0))
    (K : ℝ → ℂ) (hK : StronglyMeasurable K)
    (hKa : (k : ℝ → ℂ) =ᵐ[volume] K) :
    inner ℂ k (integratedAction f) =
      ∫ x, conj (K x)*(∫ r in Ioi (0:ℝ), physicalTerm (2*t) p (x+t) r) := by
  let μ := (volume : Measure ℝ).restrict (Ioi 0)
  let A : ℝ → ℝ → ℂ := fun r x => conj (K x)*physicalTerm (2*t) p (x+t) r
  have hs : StronglyMeasurable (Function.uncurry A) :=
    (hK.comp_measurable measurable_snd).conj.mul
      (physical_measurable t p hp).stronglyMeasurable
  have hslice (r : ℝ) : A r =ᵐ[volume] fun x => inner ℂ (k x) (actionTerm f r x) := by
    filter_upwards [hKa,physical_slice t p f hf r] with x h₁ h₂
    dsimp only [A]
    rw [RCLike.inner_apply',h₁,h₂]
  have hi (r : ℝ) : Integrable (A r) :=
    (L2.integrable_inner (𝕜 := ℂ) k (actionTerm f r)).congr (hslice r).symm
  have hn (r : ℝ) : (∫ x, ‖A r x‖) ≤ ‖k‖*‖actionTerm f r‖ := by
    have he : (∫ x, ‖A r x‖) = ∫ x, ‖actionTerm f r x‖*‖k x‖ := by
      apply integral_congr_ae
      filter_upwards [hslice r] with x hx
      rw [hx,RCLike.inner_apply',norm_mul,Complex.norm_conj,mul_comm]
    rw [he,mul_comm ‖k‖]
    exact V10B22c.integral_norm_product (actionTerm f r) k
  have hj : Integrable (Function.uncurry A) (μ.prod volume) := by
    apply (integrable_prod_iff hs.aestronglyMeasurable).mpr
    refine ⟨Eventually.of_forall hi,?_⟩
    apply (hD.norm.const_mul ‖k‖).mono' hs.norm.integral_prod_right.aestronglyMeasurable
    exact Eventually.of_forall fun r => by
      rw [Real.norm_eq_abs,abs_of_nonneg (integral_nonneg fun _ => norm_nonneg _)]
      exact hn r
  calc
    _ = ∫ r ∂μ, inner ℂ k (actionTerm f r) := by
      exact ((innerSL ℂ k).integral_comp_comm hD).symm
    _ = ∫ r ∂μ, ∫ x, A r x := by
      apply integral_congr_ae
      filter_upwards with r
      rw [L2.inner_def]
      exact integral_congr_ae (hslice r).symm
    _ = ∫ x, ∫ r ∂μ, A r x := integral_integral_swap hj
    _ = _ := by
      apply integral_congr_ae
      filter_upwards with x
      dsimp only [A,μ]
      rw [integral_const_mul]

theorem restricted_pairing (t : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (f k : FullL2) (hf : (f : ℝ → ℂ) =ᵐ[volume] trial t p)
    (hD : IntegrableOn (actionTerm f) (Ioi 0))
    (K : ℝ → ℂ) (hK : StronglyMeasurable K)
    (hKa : (k : ℝ → ℂ) =ᵐ[volume] K)
    (hsupp : ∀ᵐ x ∂volume, x+t ∉ Ioo 0 (2*t) → K x = 0)
    (hm : ∀ x ∈ Ioo 0 (2*t),
      (∫ r in Ioi (0:ℝ), physicalTerm (2*t) p x r) = V10B28a.model (2*t) p x) :
    inner ℂ k (integratedAction f) =
      ∫ x, conj (K x)*V10B28a.model (2*t) p (x+t) := by
  rw [physical_pairing t p hp f k hf hD K hK hKa]
  apply integral_congr_ae
  filter_upwards [hsupp] with x hx
  by_cases h : x+t ∈ Ioo 0 (2*t)
  · rw [hm (x+t) h]
  · simp [hx h]

end WeilDefect.MasterRecon.V10B28c

#print axioms WeilDefect.MasterRecon.V10B28c.physical_slice
#print axioms WeilDefect.MasterRecon.V10B28c.physical_measurable
#print axioms WeilDefect.MasterRecon.V10B28c.physical_pairing
#print axioms WeilDefect.MasterRecon.V10B28c.restricted_pairing
