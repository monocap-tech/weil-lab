import WeilDefect.MasterRecon.V10B22b

/-! V10B22c: Fubini attachment using full L² Cauchy-Schwarz slice
bounds. The scalar symbol integral and local measurability are explicit
inputs, not evaluation of an L² equivalence class at a point. -/
namespace WeilDefect.MasterRecon.V10B22c

open MeasureTheory Set Filter Complex
open scoped InnerProduct FourierTransform ComplexConjugate ENNReal
open V08I (FullL2)
open V10B22b (U symbol integratedAction)
open V10B21c (actionTerm)

theorem integral_norm_product (v k : FullL2) :
    (∫ u, ‖v u‖*‖k u‖) ≤ ‖v‖*‖k‖ := by
  have h := integral_mul_norm_le_Lp_mul_Lq (μ := volume)
    (p := (2:ℝ)) (q := (2:ℝ)) Real.HolderConjugate.two_two
    (by simpa using Lp.memLp v) (by simpa using Lp.memLp k)
  rw [← Real.sqrt_eq_rpow,← Real.sqrt_eq_rpow] at h
  have hv : (∫ u, ‖v u‖^(2:ℝ)) = ‖v‖^2 := by
    simp only [show (2:ℝ)=(↑(2:ℕ):ℝ) by norm_num,Real.rpow_natCast]
    exact (V08G.l2_norm_sq_integral volume v).symm
  have hk : (∫ u, ‖k u‖^(2:ℝ)) = ‖k‖^2 := by
    simp only [show (2:ℝ)=(↑(2:ℕ):ℝ) by norm_num,Real.rpow_natCast]
    exact (V08G.l2_norm_sq_integral volume k).symm
  rw [hv,hk,Real.sqrt_sq (norm_nonneg v),Real.sqrt_sq (norm_nonneg k)] at h
  exact h

theorem spectral_pairing_fubini (f k : FullL2)
    (hf : Integrable (fun x : ℝ => f x))
    (hD : IntegrableOn (actionTerm f) (Ioi 0))
    (F K : ℝ → ℂ) (hF : StronglyMeasurable F) (hK : StronglyMeasurable K)
    (hFa : (U f : ℝ → ℂ) =ᵐ[volume] F)
    (hKa : (k : ℝ → ℂ) =ᵐ[volume] K)
    (hsm : StronglyMeasurable (fun z : ℝ × ℝ => symbol z.1 z.2))
    (m : ℝ → ℂ)
    (hm : ∀ u, (∫ r in Ioi (0:ℝ), symbol r u) = m u) :
    inner ℂ k (U (integratedAction f)) = ∫ u, conj (K u)*(m u*F u) := by
  let μ := (volume : Measure ℝ).restrict (Ioi 0)
  let A : ℝ → ℝ → ℂ := fun r u => conj (K u)*(symbol r u*F u)
  have hs : StronglyMeasurable (Function.uncurry A) :=
    (hK.comp_measurable measurable_snd).conj.mul
      (hsm.mul (hF.comp_measurable measurable_snd))
  have hslice (r : ℝ) : A r =ᵐ[volume] fun u =>
      inner ℂ (k u) (U (actionTerm f r) u) := by
    filter_upwards [hFa,hKa,V10B22b.symbol_fourier_ae f hf r] with u h₁ h₂ h₃
    dsimp [A]
    rw [RCLike.inner_apply',h₃,h₁,h₂]
  have hi (r : ℝ) : Integrable (A r) :=
    (L2.integrable_inner (𝕜 := ℂ) k (U (actionTerm f r))).congr (hslice r).symm
  have hn (r : ℝ) : (∫ u, ‖A r u‖) ≤ ‖k‖*‖actionTerm f r‖ := by
    have he : (∫ u, ‖A r u‖) = ∫ u, ‖U (actionTerm f r) u‖*‖k u‖ := by
      apply integral_congr_ae
      filter_upwards [hslice r] with u hu
      rw [hu,RCLike.inner_apply',norm_mul,Complex.norm_conj,mul_comm]
    rw [he]
    have h := integral_norm_product (U (actionTerm f r)) k
    change (∫ u, ‖U (actionTerm f r) u‖*‖k u‖) ≤ ‖U (actionTerm f r)‖*‖k‖ at h
    rw [show ‖U (actionTerm f r)‖=‖actionTerm f r‖ from
      (Lp.fourierTransformₗᵢ ℝ ℂ).norm_map _,mul_comm] at h
    exact h
  have hj : Integrable (Function.uncurry A) (μ.prod volume) := by
    apply (integrable_prod_iff hs.aestronglyMeasurable).mpr
    refine ⟨Eventually.of_forall hi,?_⟩
    apply (hD.norm.const_mul ‖k‖).mono' hs.norm.integral_prod_right.aestronglyMeasurable
    exact Eventually.of_forall fun r => by
      rw [Real.norm_eq_abs,abs_of_nonneg (integral_nonneg fun _ => norm_nonneg _)]
      exact hn r
  rw [V10B22b.fourier_pairing_comm f k hD]
  calc
    _ = ∫ r ∂μ, ∫ u, A r u := by
      apply integral_congr_ae
      filter_upwards with r
      rw [L2.inner_def]
      exact integral_congr_ae (hslice r).symm
    _ = ∫ u, ∫ r ∂μ, A r u := integral_integral_swap hj
    _ = _ := by
      apply integral_congr_ae
      filter_upwards with u
      dsimp [A]
      simp only [integral_const_mul,integral_mul_const,μ,hm]

theorem multiplier_eq_of_pairings (f v : FullL2)
    (h : ∀ k : FullL2, inner ℂ k (U (integratedAction f)) = inner ℂ k v) :
    U (integratedAction f) = v :=
  ext_inner_left ℂ (fun k => h k)

end WeilDefect.MasterRecon.V10B22c

#print axioms WeilDefect.MasterRecon.V10B22c.integral_norm_product
#print axioms WeilDefect.MasterRecon.V10B22c.spectral_pairing_fubini
#print axioms WeilDefect.MasterRecon.V10B22c.multiplier_eq_of_pairings
