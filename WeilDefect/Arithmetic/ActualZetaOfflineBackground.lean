import WeilDefect.Arithmetic.ActualZetaDistinctObservationRigidity

namespace WeilDefect
noncomputable section
set_option backward.isDefEq.respectTransparency false
open ContinuousLinearMap
open scoped ComplexConjugate

theorem neutralActualZetaOrdinate_conj_eq_of_critical
    (ρ : NeutralActualZetaZeroPoint) (hρ : ρ.val.re = 1 / 2) :
    conj (neutralActualZetaOrdinate ρ) = neutralActualZetaOrdinate ρ := by
  apply Complex.ext
  · simp only [Complex.conj_re]
  · rw [Complex.conj_im, neutralActualZetaOrdinate_im, hρ]
    ring

/-- Critical-line points carry no actual negative source. -/
theorem neutralActualZetaNegativeSource_zero_of_critical
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) (hρ : ρ.val.re = 1 / 2) :
    neutralLogNegativePairSource a (neutralActualZetaOrdinate ρ) = 0 := by
  simp only [neutralLogNegativePairSource,
    neutralActualZetaOrdinate_conj_eq_of_critical ρ hρ, sub_self, smul_zero]

theorem neutralActualZetaNegativeAnalysis_zero_of_critical
    (a : ℝ) (f : NeutralActualZetaSourceDomain a)
    (q : NeutralActualZetaDivisorCoordinate) (hq : q.1.val.re = 1 / 2) :
    neutralActualZetaNegativeAnalysis a f q = 0 := by
  rw [(neutralActualZetaSourceAnalysis_sampling a f q).2]
  simp only [neutralActualZetaDivisorOrdinate,
    neutralActualZetaNegativeSource_zero_of_critical a q.1 hq, inner_zero_left]

/-- Exact unselected normalized negative coordinate on the same source vector. -/
theorem neutralActualZetaBackgroundNegative_coordinate
    (a : ℝ) (s : Finset NeutralActualZetaDivisorCoordinate)
    (f : NeutralActualZetaSourceDomain a) (q : NeutralActualZetaDivisorCoordinate)
    (hq : q ∉ s) :
    neutralActualZetaBackgroundNegativeAnalysis a s f q =
      neutralActualZetaSourceNormalization * ((Real.sqrt 2)⁻¹ : ℂ) *
        (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
          (neutralLogPhysical (neutralActualZetaSourcePhysical a f).val) -
         neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralLogPhysical (neutralActualZetaSourcePhysical a f).val)) := by
  change (neutralActualZetaNormalizedNegativeAnalysis a f -
    neutralActualZetaSelectedProjection s
      (neutralActualZetaNormalizedNegativeAnalysis a f)) q = _
  rw [lp.coeFn_sub, Pi.sub_apply, neutralActualZetaSelectedProjection_coordinate]
  simp only [hq, ite_false, sub_zero]
  rw [neutralActualZetaNormalizedNegativeAnalysis, ContinuousLinearMap.smul_apply,
    lp.coeFn_smul]
  simp only [Pi.smul_apply, smul_eq_mul]
  rw [(neutralActualZetaSourceAnalysis_sampling a f q).2,
    neutralLogNegativePairSource_inner]
  ring

/-- Removing critical-line coordinates from the zero-background test loses
no negative energy. Off-line evaluation differences remain actual input. -/
theorem neutralActualZetaBackgroundNegative_zero_iff_offline
    (a : ℝ) (s : Finset NeutralActualZetaDivisorCoordinate)
    (f : NeutralActualZetaSourceDomain a) :
    neutralActualZetaBackgroundNegativeAnalysis a s f = 0 ↔
      ∀ q : NeutralActualZetaDivisorCoordinate, q ∉ s →
        q.1.val.re ≠ 1 / 2 →
        neutralActualZetaNormalizedNegativeAnalysis a f q = 0 := by
  constructor
  · intro h q hq _
    have hv := congrArg (fun v : NeutralActualZetaGreenCoefficients => v q) h
    change (neutralActualZetaNormalizedNegativeAnalysis a f -
      neutralActualZetaSelectedProjection s
        (neutralActualZetaNormalizedNegativeAnalysis a f)) q = (0 : NeutralActualZetaGreenCoefficients) q at hv
    rw [lp.coeFn_sub, Pi.sub_apply, neutralActualZetaSelectedProjection_coordinate] at hv
    simpa [hq] using hv
  · intro h
    apply lp.ext
    funext q
    change (neutralActualZetaNormalizedNegativeAnalysis a f -
      neutralActualZetaSelectedProjection s
        (neutralActualZetaNormalizedNegativeAnalysis a f)) q = (0 : NeutralActualZetaGreenCoefficients) q
    rw [lp.coeFn_sub, Pi.sub_apply, neutralActualZetaSelectedProjection_coordinate]
    by_cases hq : q ∈ s
    · simp [hq]
    · by_cases hc : q.1.val.re = 1 / 2
      · have hn := neutralActualZetaNegativeAnalysis_zero_of_critical a f q hc
        simp [hq, neutralActualZetaNormalizedNegativeAnalysis,
          ContinuousLinearMap.smul_apply, lp.coeFn_smul, hn]
      · simp [hq, h q hq hc]

end
end WeilDefect
