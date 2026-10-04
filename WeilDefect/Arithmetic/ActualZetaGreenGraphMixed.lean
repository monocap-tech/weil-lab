import WeilDefect.Arithmetic.ActualZetaGreenGraphClosure

namespace WeilDefect
noncomputable section
open ContinuousLinearMap
open scoped InnerProduct ComplexConjugate
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false

/-- The full positive and negative coefficient inner products retain the
actual divisor multiplicities on both unchanged Green vectors. -/
theorem neutralActualZetaGreenSourceLift_mixed_coordinates
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    inner ℂ (neutralActualZetaPositiveAnalysis a (neutralActualZetaGreenSourceLift a ha v))
        (neutralActualZetaPositiveAnalysis a (neutralActualZetaGreenSourceLift a ha w)) =
      neutralActualZetaGreenPositiveForm a ha v w ∧
    inner ℂ (neutralActualZetaNegativeAnalysis a (neutralActualZetaGreenSourceLift a ha v))
        (neutralActualZetaNegativeAnalysis a (neutralActualZetaGreenSourceLift a ha w)) =
      neutralActualZetaGreenNegativeForm a ha v w := by
  constructor <;> rw [lp.inner_eq_tsum] <;>
    apply tsum_congr <;> intro q <;>
    simp only [RCLike.inner_apply', mul_comm] <;> rfl

/-- Normalized Hilbert source covariance agrees with the native mixed form on
two independently chosen Green lifts; the full-divisor factor two cancels. -/
theorem neutralActualZetaGreenHilbertSource_native_operator_mixed
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    inner ℂ (neutralActualZetaGreenHilbertSourceLift a ha v)
      (neutralActualZetaHilbertSourceOperator a
        (neutralActualZetaGreenHilbertSourceLift a ha w)) =
    inner ℂ (neutralActualZetaHilbertSourcePhysical a
        (neutralActualZetaGreenHilbertSourceLift a ha v))
      (neutralActualZetaLogWeilFormOperator a
        (neutralActualZetaHilbertSourcePhysical a
          (neutralActualZetaGreenHilbertSourceLift a ha w))) := by
  have hc : conj neutralActualZetaSourceNormalization *
      neutralActualZetaSourceNormalization = (1 / 2 : ℂ) := by
    rw [← Complex.normSq_eq_conj_mul_self, Complex.normSq_eq_norm_sq]
    exact_mod_cast neutralActualZetaSourceNormalization_norm_sq
  rw [neutralActualZetaHilbertSourceOperator_mixed]
  simp only [neutralActualZetaHilbertPositiveAnalysis,
    neutralActualZetaHilbertNegativeAnalysis, comp_apply,
    neutralActualZetaGreenHilbertSourceLift_custody,
    neutralActualZetaNormalizedPositiveAnalysis,
    neutralActualZetaNormalizedNegativeAnalysis, smul_apply,
    inner_smul_left, inner_smul_right]
  simp only [← mul_assoc, hc]
  rw [(neutralActualZetaGreenSourceLift_mixed_coordinates a ha v w).1,
    (neutralActualZetaGreenSourceLift_mixed_coordinates a ha v w).2,
    ← mul_sub, neutralActualZetaGreenSourceForms_native_operator a ha v w,
    neutralActualZetaGreenHilbertSourcePhysical a ha v,
    neutralActualZetaGreenHilbertSourcePhysical a ha w]
  ring

/-- Both slots extend in the source graph topology. No density in the entire
source graph or physical carrier is required or asserted. -/
theorem neutralActualZetaGreenGraphClosure_mixed
    (a : ℝ) (ha : 0 < a) (f g : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha)
    (hg : g ∈ neutralActualZetaGreenGraphClosure a ha) :
    inner ℂ f (neutralActualZetaHilbertSourceOperator a g) =
      inner ℂ (neutralActualZetaHilbertSourcePhysical a f)
        (neutralActualZetaLogWeilFormOperator a (neutralActualZetaHilbertSourcePhysical a g)) := by
  have hright (v : NeutralActualZetaGreenCoefficients) :
      inner ℂ (neutralActualZetaGreenHilbertSourceLift a ha v)
          (neutralActualZetaHilbertSourceOperator a g) =
        inner ℂ (neutralActualZetaHilbertSourcePhysical a
            (neutralActualZetaGreenHilbertSourceLift a ha v))
          (neutralActualZetaLogWeilFormOperator a (neutralActualZetaHilbertSourcePhysical a g)) := by
    have hs := continuous_const.inner (𝕜 := ℂ)
      (neutralActualZetaHilbertSourceOperator a).continuous
    have hn := continuous_const.inner (𝕜 := ℂ)
      ((neutralActualZetaLogWeilFormOperator a).continuous.comp
        (neutralActualZetaHilbertSourcePhysical a).continuous)
    have hc := isClosed_eq hs hn
    apply closure_minimal (s := Set.range (neutralActualZetaGreenHilbertSourceLift a ha)) ?_ hc hg
    rintro x ⟨w, rfl⟩
    exact neutralActualZetaGreenHilbertSource_native_operator_mixed a ha v w
  have hs := continuous_id.inner (𝕜 := ℂ) continuous_const
  have hn := (neutralActualZetaHilbertSourcePhysical a).continuous.inner (𝕜 := ℂ)
    continuous_const
  have hc := isClosed_eq hs hn
  apply closure_minimal (s := Set.range (neutralActualZetaGreenHilbertSourceLift a ha)) ?_ hc hf
  rintro x ⟨v, rfl⟩
  exact hright v

/-- Mixed native control now holds for the actual source covariance on the
proved closure, measured by the physical logarithmic norms in both slots. -/
theorem neutralActualZetaGreenGraphClosure_mixed_bound
    (a : ℝ) (ha : 0 < a) (f g : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha)
    (hg : g ∈ neutralActualZetaGreenGraphClosure a ha) :
    ‖inner ℂ f (neutralActualZetaHilbertSourceOperator a g)‖ ≤
      ‖neutralActualZetaLogWeilFormOperator a‖ *
        ‖neutralActualZetaHilbertSourcePhysical a f‖ *
        ‖neutralActualZetaHilbertSourcePhysical a g‖ := by
  rw [neutralActualZetaGreenGraphClosure_mixed a ha f g hf hg]
  exact neutralActualZetaLogWeilFormOperator_mixed_bound a _ _

end
end WeilDefect
