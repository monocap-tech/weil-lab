import WeilDefect.Arithmetic.ActualZetaIV106E18VLiteralMatch
import WeilDefect.Arithmetic.ActualZetaNativeFormOperator

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform InnerProductSpace
open scoped FourierTransform SchwartzMap ComplexConjugate BigOperators

/-- The exact log energy of the PHYSICAL difference is the squared
distance in the original carrier; no comparison to an unrelated norm. -/
theorem neutralIV106E18WNorm_diff (a : ℝ)
    (p q : NeutralLogHilbertCarrier a) :
    ‖p-q‖^2 = ∫ ξ, logarithmicFourierWeight ξ *
      ‖(𝓕 (neutralLogPhysical p.val-neutralLogPhysical q.val) : RealComplexL2) ξ‖^2 := by
  rw [neutralLogHilbertCarrier_norm_sq]
  have he : neutralLogPhysical (p-q).val =
      neutralLogPhysical p.val-neutralLogPhysical q.val := by
    change neutralLogPhysical (p.val-q.val) = _
    exact map_sub _ _ _
  rw [he]

def neutralIV106E18WConstant : ℝ :=
  Real.sqrt (Real.exp 1+1+1/(4*Real.pi^2))

theorem neutralIV106E18WConstant_nonneg : 0 ≤ neutralIV106E18WConstant :=
  Real.sqrt_nonneg _

/-- Same physical representative and same original lift as IV102.
The E18V energy budget now controls the native carrier distance. -/
theorem neutralIV106E18WLift_error (a : ℝ)
    (p : NeutralLogHilbertCarrier a) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x ∉ Set.Icc (-a) a, s x = 0)
    (f : RealComplexL2) (hp : neutralLogPhysical p.val = f)
    (ε : ℝ) (hε : 0 ≤ ε)
    (he : (∫ ξ, logarithmicFourierWeight ξ *
      ‖(𝓕 (s.toLp 2 volume-f) : RealComplexL2) ξ‖^2) ≤
        (Real.exp 1+1+1/(4*Real.pi^2))*ε^2) :
    ‖neutralIV102Lift a s hs-p‖ ≤ neutralIV106E18WConstant*ε := by
  have h := neutralIV106E18WNorm_diff a (neutralIV102Lift a s hs) p
  rw [neutralIV102Lift_physical, hp] at h
  have hsq : ‖neutralIV102Lift a s hs-p‖^2 ≤
      (neutralIV106E18WConstant*ε)^2 := by
    rw [mul_pow,neutralIV106E18WConstant,Real.sq_sqrt (by positivity)]
    rw [h]
    exact he
  have hnon := mul_nonneg neutralIV106E18WConstant_nonneg hε
  nlinarith [norm_nonneg (neutralIV102Lift a s hs-p)]

/-- Actual native form perturbation, not an arbitrary bilinear model.
The source already proves its mixed operator-norm estimate. -/
theorem neutralIV106E18WMixed_error (a : ℝ)
    (p q u v : NeutralLogHilbertCarrier a) :
    ‖inner ℂ u (neutralActualZetaLogWeilFormOperator a v) -
      inner ℂ p (neutralActualZetaLogWeilFormOperator a q)‖ ≤
      ‖neutralActualZetaLogWeilFormOperator a‖ *
        (‖u-p‖*‖q‖+‖p‖*‖v-q‖+‖u-p‖*‖v-q‖) := by
  let W := neutralActualZetaLogWeilFormOperator a
  have he : inner ℂ u (W v)-inner ℂ p (W q) =
      (inner ℂ (u-p) (W q)+inner ℂ p (W (v-q)))+
        inner ℂ (u-p) (W (v-q)) := by
    simp only [map_sub,inner_sub_left,inner_sub_right]
    ring
  change ‖inner ℂ u (W v)-inner ℂ p (W q)‖ ≤ _
  rw [he]
  calc
    _ ≤ ‖inner ℂ (u-p) (W q)+inner ℂ p (W (v-q))‖+
          ‖inner ℂ (u-p) (W (v-q))‖ := norm_add_le _ _
    _ ≤ (‖inner ℂ (u-p) (W q)‖+‖inner ℂ p (W (v-q))‖)+
          ‖inner ℂ (u-p) (W (v-q))‖ :=
      add_le_add_right (norm_add_le _ _) _
    _ ≤ (‖W‖*‖u-p‖*‖q‖+‖W‖*‖p‖*‖v-q‖)+
          ‖W‖*‖u-p‖*‖v-q‖ :=
      add_le_add (add_le_add
        (neutralActualZetaLogWeilFormOperator_mixed_bound a (u-p) q)
        (neutralActualZetaLogWeilFormOperator_mixed_bound a p (v-q)))
        (neutralActualZetaLogWeilFormOperator_mixed_bound a (u-p) (v-q))
    _ = _ := by dsimp [W]; ring

/-- Uniform bound suitable for a finite bank with certified rough-vector
norm and approximation reserves. No positivity is used. -/
theorem neutralIV106E18WUniform (a : ℝ)
    (p q u v : NeutralLogHilbertCarrier a) (K M δ : ℝ)
    (hK : ‖neutralActualZetaLogWeilFormOperator a‖ ≤ K)
    (hM : 0 ≤ M) (hδ : 0 ≤ δ)
    (hp : ‖p‖ ≤ M) (hq : ‖q‖ ≤ M)
    (hu : ‖u-p‖ ≤ δ) (hv : ‖v-q‖ ≤ δ) :
    ‖inner ℂ u (neutralActualZetaLogWeilFormOperator a v) -
      inner ℂ p (neutralActualZetaLogWeilFormOperator a q)‖ ≤
      K*(2*M*δ+δ^2) := by
  have ht : ‖u-p‖*‖q‖+‖p‖*‖v-q‖+‖u-p‖*‖v-q‖ ≤
      δ*M+M*δ+δ*δ :=
    add_le_add (add_le_add
      (mul_le_mul hu hq (norm_nonneg _) hδ)
      (mul_le_mul hp hv (norm_nonneg _) hM))
      (mul_le_mul hu hv (norm_nonneg _) hδ)
  have hnn : 0 ≤ δ*M+M*δ+δ*δ := by positivity
  calc
    _ ≤ ‖neutralActualZetaLogWeilFormOperator a‖ *
        (‖u-p‖*‖q‖+‖p‖*‖v-q‖+‖u-p‖*‖v-q‖) :=
      neutralIV106E18WMixed_error a p q u v
    _ ≤ ‖neutralActualZetaLogWeilFormOperator a‖*(δ*M+M*δ+δ*δ) :=
      mul_le_mul_of_nonneg_left ht (norm_nonneg _)
    _ ≤ K*(δ*M+M*δ+δ*δ) := mul_le_mul_of_nonneg_right hK hnn
    _ = _ := by ring

#print axioms neutralIV106E18WNorm_diff
#print axioms neutralIV106E18WConstant_nonneg
#print axioms neutralIV106E18WLift_error
#print axioms neutralIV106E18WMixed_error
#print axioms neutralIV106E18WUniform
end
end WeilDefect
