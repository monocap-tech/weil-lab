import WeilDefect.MasterRecon.V10B10b
import WeilDefect.MasterRecon.V10B9c

/-! Arithmetic specialization: exact normalized contraction criterion
and compact-error inequality. No assertion that the criterion holds. -/
namespace WeilDefect.MasterRecon.V10B10c

open Set
open scoped NNReal InnerProduct
open V08I (logCarrier)
open V10B6c (analysisChannel signedGram)
open V10B10a (normalized receiver)

theorem positivity_iff_contraction (t : ℝ)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ g, ‖g‖^2*(b:ℝ) ≤ ‖analysisChannel true T g‖^2) :
    (∀ g, 0 ≤ (inner ℂ (signedGram T g) g).re) ↔
      ‖normalized (analysisChannel true T) (analysisChannel false T) b hb h‖ ≤ 1 := by
  rw [V10B10a.contraction_iff]
  simp only [V10B6c.signedGram_diagonal,sub_nonneg]

theorem positivity_iff_core (t : ℝ)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (hcore : Dense (V10B8h.SmoothCore t)) :
    (∀ g, 0 ≤ (inner ℂ (signedGram T g) g).re) ↔
      ∀ g ∈ V10B8h.SmoothCore t, 0 ≤ (inner ℂ (signedGram T g) g).re := by
  constructor
  · intro h g _
    exact h g
  · intro h g
    have hc : IsClosed {x : logCarrier t | 0 ≤ (inner ℂ (signedGram T x) x).re} :=
      isClosed_le continuous_const
        (Complex.continuous_re.comp ((signedGram T).continuous.inner continuous_id))
    exact closure_minimal h hc (hcore g)

theorem compact_error (t : ℝ)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ g, ‖g‖^2*(b:ℝ) ≤ ‖analysisChannel true T g‖^2)
    (K : logCarrier t →L[ℂ] logCarrier t) (hK : IsCompactOperator K)
    (hG : signedGram T = 1+K) :
    ∃ L : (analysisChannel true T).range →L[ℂ] logCarrier t, IsCompactOperator L ∧
      ∀ y, ‖normalized (analysisChannel true T) (analysisChannel false T) b hb h y‖^2 ≤
        (1-V10B10b.gap (analysisChannel true T))*‖y‖^2 +
          (Real.sqrt (b:ℝ))⁻¹*‖L y‖*‖y‖ := by
  apply V10B10b.compact_normalized_defect _ _ b hb h K hK
  intro g
  rw [← V10B6c.signedGram_diagonal,hG,ContinuousLinearMap.add_apply,
    ContinuousLinearMap.one_apply,inner_add_left,Complex.add_re,
    inner_self_eq_norm_sq_to_K,Complex.ofReal_re]

theorem normalized_arithmetic_receiver (t : ℝ) (ht : 0 < t)
    (hOld : V10B9b.OldApproximation)
    (hStirling : V10B8f.VerticalStirling)
    (hEF : V10B8b.LiteralEF)
    (hSupply : V09C.SuperlinearSupply V09C.CriticalSample) :
    ∃ T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index,
      V10B6d.LiteralCoordinates t T ∧
      ∃ b : ℝ≥0, ∃ hb : 0 < b,
      ∃ h : ∀ g, ‖g‖^2*(b:ℝ) ≤ ‖analysisChannel true T g‖^2,
      (IsClosed ((analysisChannel true T).range :
        Set (V09E.PositiveCoeff V10A.Index))) ∧
      ((∀ g, 0 ≤ (inner ℂ (signedGram T g) g).re) ↔
        ‖normalized (analysisChannel true T) (analysisChannel false T) b hb h‖ ≤ 1) ∧
      ∃ L : (analysisChannel true T).range →L[ℂ] logCarrier t, IsCompactOperator L ∧
        ∀ y, ‖normalized (analysisChannel true T) (analysisChannel false T) b hb h y‖^2 ≤
          (1-V10B10b.gap (analysisChannel true T))*‖y‖^2 +
            (Real.sqrt (b:ℝ))⁻¹*‖L y‖*‖y‖ := by
  obtain ⟨T,hT,⟨K,hK,hG⟩,⟨b,hb,h⟩⟩ :=
    V10B9c.arithmetic_coercivity t ht hOld hStirling hEF hSupply
  exact ⟨T,hT,b,hb,h,V10B10a.positive_range_closed _ b hb h,
    positivity_iff_contraction t T b hb h,compact_error t T b hb h K hK hG⟩

end WeilDefect.MasterRecon.V10B10c

#print axioms WeilDefect.MasterRecon.V10B10c.positivity_iff_contraction
#print axioms WeilDefect.MasterRecon.V10B10c.positivity_iff_core
#print axioms WeilDefect.MasterRecon.V10B10c.compact_error
#print axioms WeilDefect.MasterRecon.V10B10c.normalized_arithmetic_receiver
