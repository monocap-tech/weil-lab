import WeilDefect.MasterRecon.V07D

/-! V07E: real translation covariance and exact identification with the
V06A positive operator family. The coefficient membership and the
identification of actual zeta samples with the bounded analysis map
remain explicit inputs. -/
namespace WeilDefect.MasterRecon.V07E

open scoped ENNReal InnerProduct
open V07C

variable {ι : Type*}

noncomputable def samplePair (f : ℝ → ℂ) (m : ℕ) (d g : ℝ) : Pair :=
  let u := V07A.weightedMellin f m ((d : ℂ) + (g : ℂ) * Complex.I)
  let v := V07A.weightedMellin f m (-(d : ℂ) + (g : ℂ) * Complex.I)
  WithLp.toLp 2 (V07A.pairPlus u v, V07A.pairMinus u v)

theorem phase_apply (g : ι → ℝ) (a : ℝ) (x : Coeff ι) (i : ι) :
    phase g a x i = ordinatePhase (g i) a • x i := rfl

theorem samplePair_translate (f : ℝ → ℂ) (m : ℕ) (d g a : ℝ) :
    samplePair (V07A.translate a f) m d g =
      ordinatePhase g a •
        NormedSpace.exp ((a : ℂ) • displacementBlock d) (samplePair f m d g) := by
  rw [V07D.local_exp_mix]
  have h := V07A.reflected_mellin_translation f m d g a
  dsimp only at h
  have hz : (a : ℂ) * (d : ℂ) = (d : ℂ) * (a : ℂ) := mul_comm _ _
  rw [hz]
  apply WithLp.ofLp_injective
  apply Prod.ext
  · exact h.1
  · exact h.2

/-- Actual pairwise Mellin sampling covariance, with the square-summable
sample vectors supplied rather than postulated as a new bounded map. -/
theorem sampled_translation (f : ℝ → ℂ) (m : ι → ℕ) (d g : ι → ℝ)
    (hd : ∀ i, |d i| ≤ 1 / 2) (a : ℝ) (x y : Coeff ι)
    (hx : ∀ i, x i = samplePair f (m i) (d i) (g i))
    (hy : ∀ i, y i = samplePair (V07A.translate a f) (m i) (d i) (g i)) :
    y = phase g a (NormedSpace.exp ((a : ℂ) • displacement d hd) x) := by
  apply lp.ext
  funext i
  change y i = phase g a (NormedSpace.exp ((a : ℂ) • displacement d hd) x) i
  rw [hy, phase_apply, V07D.global_exp_coordinate, hx]
  exact samplePair_translate f (m i) (d i) (g i) a

section SelfAdjoint
variable {K : Type*}
variable [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]

theorem real_exp_selfAdjoint (D : K →L[ℂ] K) (hD : D.adjoint = D) (a : ℝ) :
    (NormedSpace.exp ((a : ℂ) • D)).adjoint =
      NormedSpace.exp ((a : ℂ) • D) := by
  change star (NormedSpace.exp ((a : ℂ) • D)) = _
  rw [NormedSpace.star_exp, star_smul, ContinuousLinearMap.star_eq_adjoint, hD]
  simp

end SelfAdjoint

/-- No unbounded ordinate generator occurs in the translated form. -/
theorem translated_pairing (d g : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2)
    (E : ι → Pair →L[ℂ] Pair) (c : ℝ) (hc : 0 ≤ c)
    (hE : ∀ i, ‖E i‖ ≤ c) (a : ℝ) (x y : Coeff ι) :
    let B := NormedSpace.exp ((-(a : ℂ)) • displacement d hd)
    let Q := V07B.blockLift E c hc hE
    inner ℂ (Q (phase g (-a) (B x))) (phase g (-a) (B y)) =
      inner ℂ ((V06A.translatedBlock (displacement d hd) Q (a : ℂ)) x) y := by
  dsimp only
  rw [phase_cancel]
  let B := NormedSpace.exp ((-(a : ℂ)) • displacement d hd)
  let Q := V07B.blockLift E c hc hE
  change inner ℂ (Q (B x)) (B y) = inner ℂ (B (Q (B x))) y
  have hB : B.adjoint = B := by
    unfold B
    rw [← Complex.ofReal_neg]
    exact real_exp_selfAdjoint _ (displacement_selfAdjoint d hd) (-a)
  rw [← ContinuousLinearMap.adjoint_inner_left B y (Q (B x)), hB]

variable {H : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

theorem translated_form_pairing (A : H →L[ℂ] Coeff ι)
    (d g : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2)
    (E : ι → Pair →L[ℂ] Pair) (c : ℝ) (hc : 0 ≤ c)
    (hE : ∀ i, ‖E i‖ ≤ c) (a : ℝ) (x y : H) :
    let B := NormedSpace.exp ((-(a : ℂ)) • displacement d hd)
    let Q := V07B.blockLift E c hc hE
    inner ℂ (Q (phase g (-a) (B (A x)))) (phase g (-a) (B (A y))) =
      inner ℂ ((V06A.translatedForm A (displacement d hd) Q (a : ℂ)) x) y := by
  dsimp only
  rw [translated_pairing]
  change inner ℂ (V06A.translatedBlock (displacement d hd)
    (V07B.blockLift E c hc hE) (a : ℂ) (A x)) (A y) =
      inner ℂ (A.adjoint (V06A.translatedBlock (displacement d hd)
        (V07B.blockLift E c hc hE) (a : ℂ) (A x))) y
  rw [ContinuousLinearMap.adjoint_inner_left]

end WeilDefect.MasterRecon.V07E

#print axioms WeilDefect.MasterRecon.V07E.phase_apply
#print axioms WeilDefect.MasterRecon.V07E.samplePair_translate
#print axioms WeilDefect.MasterRecon.V07E.sampled_translation
#print axioms WeilDefect.MasterRecon.V07E.real_exp_selfAdjoint
#print axioms WeilDefect.MasterRecon.V07E.translated_pairing
#print axioms WeilDefect.MasterRecon.V07E.translated_form_pairing
