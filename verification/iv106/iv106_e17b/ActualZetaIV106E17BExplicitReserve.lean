import WeilDefect.Arithmetic.ActualZetaIV106E17AExplicitShift
import WeilDefect.Arithmetic.ActualZetaIV106E16ResidualGram

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate FourierTransform BigOperators

/-- Integrate the explicit one-sided symbol estimate on the actual constrained
carrier. The pole row makes the cross-pole term nonnegative. -/
theorem neutralIV106E17BExplicit_garding (k : ℕ) (hk : 0 < k)
    (q : neutralIV106E13H)
    (hq : neutralIV106C3Constraints 665 k hk q = 0) :
    ‖q‖^2 ≤ neutralIV106E13Energy q + 20*‖neutralLogPhysical q.val‖^2 := by
  let f := neutralLogHilbertToCanonical q
  have hf := neutralActualZetaCanonical_signedEnergy_integrable (11/10) f
  change Integrable (fun ξ => rightLimitCompactWeilSymbolMathlib (11/10) ξ *
    neutralIV106E10Density q ξ) at hf
  have hm := neutralIV106E10Mass q
  have hw : Integrable (fun ξ => logarithmicFourierWeight ξ * neutralIV106E10Density q ξ) :=
    f.property.2
  have hi := integral_mono hw (hf.add (hm.1.const_mul 20)) (fun ξ => by
    have h := mul_le_mul_of_nonneg_right (neutralIV106E17ASymbol_shift ξ)
      (show 0 ≤ neutralIV106E10Density q ξ from sq_nonneg _)
    simpa only [Pi.add_apply,add_mul] using h)
  change (∫ ξ, logarithmicFourierWeight ξ * neutralIV106E10Density q ξ) ≤
    ∫ ξ, rightLimitCompactWeilSymbolMathlib (11/10) ξ * neutralIV106E10Density q ξ +
      20*neutralIV106E10Density q ξ at hi
  rw [integral_add hf (hm.1.const_mul 20), integral_const_mul, hm.2] at hi
  have hn : ‖q‖^2 = ∫ ξ, logarithmicFourierWeight ξ * neutralIV106E10Density q ξ := by
    rw [neutralLogHilbertCarrier_norm_sq]
    rfl
  rw [← hn] at hi
  have hp := neutralIV106E10Pole k hk q hq
  unfold neutralIV106E13Energy
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re]
  unfold neutralActualZetaCanonicalNativeQuadratic
  change ‖q‖^2 ≤ (∫ ξ, rightLimitCompactWeilSymbolMathlib (11/10) ξ *
    neutralIV106E10Density q ξ) + _ + 20*‖neutralLogPhysical q.val‖^2
  linarith only [hi,hp]

/-- A rational coercivity constant sufficient for numerical custody. -/
theorem neutralIV106E17BMargin (k : ℕ) (hk : 0 < k)
    (q : neutralIV106E13H)
    (hq : neutralIV106C3Constraints 665 k hk q = 0) :
    (1/21:ℝ)*‖q‖^2 ≤ neutralIV106E13Energy q := by
  have hm := neutralIV106E11Closed_mass k hk q hq
  change (5003/5000:ℝ)*‖neutralLogPhysical q.val‖^2 ≤ neutralIV106E13Energy q at hm
  have hg := neutralIV106E17BExplicit_garding k hk q hq
  linarith only [hm,hg,sq_nonneg ‖neutralLogPhysical q.val‖]

theorem neutralIV106E17BCompressed_margin (k : ℕ) (hk : 0 < k)
    (x : neutralIV106E12Kernel k hk) :
    (1/21:ℝ)*‖x‖^2 ≤ (inner ℂ x (neutralIV106E12Compressed k hk x)).re := by
  rw [neutralIV106E15Compression_energy]
  exact neutralIV106E17BMargin k hk x.val x.property

theorem neutralIV106E17BInverse21 (k : ℕ) (hk : 0 < k) :
    ∃ e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk,
      e.toContinuousLinearMap = neutralIV106E12Compressed k hk ∧
      ‖e.symm.toContinuousLinearMap‖ ≤ 21 := by
  simpa only [one_div, inv_inv] using
    neutralIV106E12Inverse (neutralIV106E12Compressed k hk) (1/21:ℝ)
      (by norm_num) (neutralIV106E17BCompressed_margin k hk)

/-- Attach the new numerical reserve directly, not via a comparison with
the earlier choice-defined coercivity constant. -/
theorem neutralIV106E17BEnclosure21 (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk) :
    neutralIV106E13Energy (y.val-t.val) -
      21*‖neutralIV106E15Residual k hk y t‖^2 ≤ neutralIV106E13Schur k hk e y := by
  let d := neutralIV106E13Response k hk e y - t
  have hc := neutralIV106E13Actual_completion k hk e he (-t) y
  have hc' : neutralIV106E13Energy (y.val-t.val) =
      neutralIV106E13Energy d.val + neutralIV106E13Schur k hk e y := by
    simpa [d, sub_eq_add_neg, add_comm] using hc
  have h := neutralIV106E15Residual_energy (neutralIV106E12Compressed k hk)
    (1/21:ℝ) (by norm_num) (neutralIV106E17BCompressed_margin k hk) d
  rw [neutralIV106E15Compression_energy, ← neutralIV106E15Residual_eq k hk e he y t] at h
  norm_num at h
  linarith only [hc',h.2]

/-- Concrete rational matrix receiver for numerical trial and residual bounds. -/
theorem neutralIV106E17BInterval21 (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (L R : neutralIV106E16Index k → neutralIV106E16Index k → ℂ)
    (hL : ∀ c, neutralIV106E16Quadratic L c ≤
      neutralIV106E16Quadratic (neutralIV106E16TrialGram k hk t) c)
    (hR : ∀ c, neutralIV106E16Quadratic
      (neutralIV106E16ResidualGram k hk t) c ≤ neutralIV106E16Quadratic R c)
    (hcert : ∀ c, 21*neutralIV106E16Quadratic R c ≤ neutralIV106E16Quadratic L c) :
    ∀ q : neutralIV106E13H, 0 ≤ neutralIV106E13Energy q := by
  obtain ⟨e,he,_⟩ := neutralIV106E17BInverse21 k hk
  apply (neutralIV106E13Nonnegative_iff k hk e he).mpr
  intro y
  obtain ⟨c,hc⟩ := neutralIV106E14Synthesis k hk y
  have hb := neutralIV106E17BEnclosure21 k hk e he
    (∑ j, c j • neutralIV106E14LiftedRow k hk j) (∑ j, c j • t j)
  rw [neutralIV106E16Trial_energy, neutralIV106E16Residual_energy, hc] at hb
  have h := mul_le_mul_of_nonneg_left (hR c) (by norm_num : (0:ℝ) ≤ 21)
  linarith only [hb,h,hcert c,hL c]

#print axioms neutralIV106E17BExplicit_garding
#print axioms neutralIV106E17BMargin
#print axioms neutralIV106E17BCompressed_margin
#print axioms neutralIV106E17BInverse21
#print axioms neutralIV106E17BEnclosure21
#print axioms neutralIV106E17BInterval21
end
end WeilDefect
