import WeilDefect.Arithmetic.ActualZetaSourceQuadraticClosure
import WeilDefect.Arithmetic.ActualZetaSmoothLiteralFormulaAutomatic

namespace WeilDefect
noncomputable section
open InnerProductSpace
open scoped ComplexConjugate

/-!
NF538: the authentic complete-source-graph signed quadratic equals
the actual all-multiplicity zero-divisor mixed autocorrelation series.
No Green synthesis, density, oddness, or zero-location hypothesis.

This proof does not assert every physical L² vector is in the graph:
its input is an actual existing closed-graph element, with both l²
source vectors supplied by that graph's membership.
-/

/-- The original raw source normalization has exactly squared scalar
value 1/2 in complex arithmetic (distinct from just its norm squared).
This is required when inverting the genuine two-channel sample pair. -/
private theorem neutralActualZetaSourceNormalization_mul_self :
    neutralActualZetaSourceNormalization *
      neutralActualZetaSourceNormalization = (1 / 2 : ℂ) := by
  have hs : (((Real.sqrt (2 : ℝ)) : ℂ) ^ 2) = (2 : ℂ) := by
    exact_mod_cast Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 2)
  unfold neutralActualZetaSourceNormalization
  calc
    (((Real.sqrt (2 : ℝ)) : ℂ)⁻¹) *
        (((Real.sqrt (2 : ℝ)) : ℂ)⁻¹) =
        (((Real.sqrt (2 : ℝ)) : ℂ) ^ 2)⁻¹ := by
          simp only [inv_pow, pow_two]
    _ = (2 : ℂ)⁻¹ := by rw [hs]
    _ = 1 / 2 := by norm_num

/-- The exact original unnormalized positive/negative source coordinates,
in the actual full divisor, algebraically recover the two raw sample
families by a second 1/sqrt2 mixing. -/
def neutralActualZetaFullGraphRawConjSamples
    (a : ℝ) (h : NeutralActualZetaSourceDomain a) :
    NeutralActualZetaGreenCoefficients :=
  neutralActualZetaSourceNormalization •
    (neutralActualZetaPositiveAnalysis a h + neutralActualZetaNegativeAnalysis a h)

def neutralActualZetaFullGraphRawSamples
    (a : ℝ) (h : NeutralActualZetaSourceDomain a) :
    NeutralActualZetaGreenCoefficients :=
  neutralActualZetaSourceNormalization •
    (neutralActualZetaPositiveAnalysis a h - neutralActualZetaNegativeAnalysis a h)

/-- Full source graph sampling at conjugate complex ordinate, for every
actual zero and integer multiplicity copy, not just Green vectors. -/
theorem neutralActualZetaFullGraphRawConjSamples_apply
    (a : ℝ) (h : NeutralActualZetaSourceDomain a)
    (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaFullGraphRawConjSamples a h q =
      neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val) := by
  let c : ℂ := neutralActualZetaSourceNormalization
  let u : ℂ := neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
      (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)
  let v : ℂ := neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)
  have hp := (neutralActualZetaSourceAnalysis_sampling a h q).1
  have hn := (neutralActualZetaSourceAnalysis_sampling a h q).2
  change (c • (neutralActualZetaPositiveAnalysis a h +
    neutralActualZetaNegativeAnalysis a h)) q = u
  simp only [lp.coeFn_smul, Pi.smul_apply, smul_eq_mul,
    lp.coeFn_add, Pi.add_apply]
  rw [hp, hn, neutralLogPositivePairSource_inner,
    neutralLogNegativePairSource_inner]
  change c * (c * (u + v) + c * (u - v)) = u
  have hc : c * c = (1 / 2 : ℂ) :=
    neutralActualZetaSourceNormalization_mul_self
  calc
    c * (c * (u + v) + c * (u - v)) = (c * c) * (2 * u) := by ring
    _ = u := by rw [hc]; ring

/-- Corresponding actual raw nonconjugate samples, with no assumptions
on where the zero lies or whether any zero is simple. -/
theorem neutralActualZetaFullGraphRawSamples_apply
    (a : ℝ) (h : NeutralActualZetaSourceDomain a)
    (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaFullGraphRawSamples a h q =
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val) := by
  let c : ℂ := neutralActualZetaSourceNormalization
  let u : ℂ := neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
      (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)
  let v : ℂ := neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)
  have hp := (neutralActualZetaSourceAnalysis_sampling a h q).1
  have hn := (neutralActualZetaSourceAnalysis_sampling a h q).2
  change (c • (neutralActualZetaPositiveAnalysis a h -
    neutralActualZetaNegativeAnalysis a h)) q = v
  simp only [lp.coeFn_smul, Pi.smul_apply, smul_eq_mul,
    lp.coeFn_sub, Pi.sub_apply]
  rw [hp, hn, neutralLogPositivePairSource_inner,
    neutralLogNegativePairSource_inner]
  change c * (c * (u + v) - c * (u - v)) = v
  have hc : c * c = (1 / 2 : ℂ) :=
    neutralActualZetaSourceNormalization_mul_self
  calc
    c * (c * (u + v) - c * (u - v)) = (c * c) * (2 * v) := by ring
    _ = v := by rw [hc]; ring

/-- Pure Hilbert polarization for COMPLEX source coefficients.
The identity is valid for any common scalar, and therefore retains
the original two independent sqrt2 normalizations exactly. -/
private theorem neutralActualZetaPN_normalizedEnergy_eq_rawInner
    (P N : NeutralActualZetaGreenCoefficients) (c : ℂ) :
    ‖c • P‖ ^ 2 - ‖c • N‖ ^ 2 =
      (inner ℂ (c • (P + N)) (c • (P - N))).re := by
  have hplus :
      c • (P + N) + c • (P - N) = (2 : ℂ) • (c • P) := by
    simp only [smul_add, smul_sub, two_smul]
    abel
  have hminus :
      c • (P + N) - c • (P - N) = (2 : ℂ) • (c • N) := by
    simp only [smul_add, smul_sub, two_smul]
    abel
  have h := re_inner_eq_norm_add_mul_self_sub_norm_sub_mul_self_div_four
    (c • (P + N)) (c • (P - N))
  rw [hplus, hminus] at h
  have hp : ‖(2 : ℂ) • (c • P)‖ = 2 * ‖c • P‖ := by
    rw [norm_smul]
    norm_num
  have hn : ‖(2 : ℂ) • (c • N)‖ = 2 * ‖c • N‖ := by
    rw [norm_smul]
    norm_num
  rw [hp, hn] at h
  rw [h]
  ring

/-- Full original source signed quadratic equals the Hilbert cross term
of the original raw Fourier sample sequences, no Green restriction. -/
theorem neutralActualZetaSourceQuadratic_fullGraph_rawInner
    (a : ℝ) (h : NeutralActualZetaSourceDomain a) :
    neutralActualZetaSourceQuadratic a h =
      (inner ℂ (neutralActualZetaFullGraphRawConjSamples a h)
        (neutralActualZetaFullGraphRawSamples a h)).re := by
  unfold neutralActualZetaSourceQuadratic
    neutralActualZetaFullGraphRawConjSamples
    neutralActualZetaFullGraphRawSamples
    neutralActualZetaNormalizedPositiveAnalysis
    neutralActualZetaNormalizedNegativeAnalysis
  simp only [ContinuousLinearMap.smul_apply]
  exact neutralActualZetaPN_normalizedEnergy_eq_rawInner
    (neutralActualZetaPositiveAnalysis a h)
    (neutralActualZetaNegativeAnalysis a h)
    neutralActualZetaSourceNormalization

/-- UNIVERSAL source identity: the entire original all-divisor source
quadratic, not only Green packets, equals the real part of the literal
actual zero-side mixed physical correlation sum. The zero series converges
absolutely already from full graph membership via the Hilbert ℓ² pairing. -/
theorem neutralActualZetaSourceQuadratic_fullGraph_rawDivisor
    (a : ℝ) (h : NeutralActualZetaSourceDomain a) :
    neutralActualZetaSourceQuadratic a h =
      (∑' q : NeutralActualZetaDivisorCoordinate,
        conj (neutralWindowEvaluation a
          (conj (neutralActualZetaDivisorOrdinate q))
            (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)) *
          neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
            (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)).re := by
  rw [neutralActualZetaSourceQuadratic_fullGraph_rawInner,
    lp.inner_eq_tsum]
  congr 1
  apply tsum_congr
  intro q
  rw [neutralActualZetaFullGraphRawConjSamples_apply,
    neutralActualZetaFullGraphRawSamples_apply]
  simp only [RCLike.inner_apply']

/-- The full authentic source quadratic equals the real literal zeta
explicit formula on any actual full-graph vector with C² physical
autocorrelation, without RH and without Green packet density. -/
theorem neutralActualZetaSourceQuadratic_fullGraph_literature_of_contDiff
    (a : ℝ) (h : NeutralActualZetaSourceDomain a)
    (hreg : ContDiff ℝ 2
      (neutralWindowCorrelation a
        (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)
        (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val))) :
    neutralActualZetaSourceQuadratic a h =
      (Zeta23.EF.literatureRHS
        (neutralWindowCorrelation a
          (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)
          (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val))).re := by
  rw [neutralActualZetaSourceQuadratic_fullGraph_rawDivisor]
  exact congrArg Complex.re
    (neutralActualZetaWindowCorrelation_literature_of_contDiff a
      (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val)
      (neutralLogPhysical (neutralActualZetaSourcePhysical a h).val) hreg)

end
end WeilDefect
