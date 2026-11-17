import WeilDefect.Arithmetic.ActualZetaOriginalLogDyadicEnvelope
import WeilDefect.Arithmetic.ActualZetaFullSourceLiftOfSquareSummable
import Mathlib.Analysis.Normed.Group.Tannery

namespace WeilDefect
noncomputable section
open Filter InnerProductSpace
open scoped ComplexConjugate ENNReal

/-!
NF574: full actual source graph convergence from a summable
uniform squared envelope and genuine LOG carrier norm convergence.
The endpoint target is not required to have a smooth representative.
No finite-rank or Gram hypotheses are needed for this limit theorem.
-/

/-- Actual multiplicity-aware ℓ² convergence from dominated coordinate
errors; this cannot be replaced by convergence in each fixed band. -/
theorem neutralNF574ActualCoefficients_tendsto_of_domination
    {ι : Type*} {l : Filter ι}
    (u : ι → NeutralActualZetaGreenCoefficients)
    (v : NeutralActualZetaGreenCoefficients)
    (W : NeutralActualZetaDivisorCoordinate → ℝ)
    (hW : Summable W)
    (hcoord : ∀ q, Tendsto (fun i => u i q) l (nhds (v q)))
    (hbound : ∀ᶠ i in l, ∀ q, ‖u i q - v q‖^2 ≤ W q) :
    Tendsto u l (nhds v) := by
  have ht : Tendsto (fun i => ∑' q : NeutralActualZetaDivisorCoordinate,
      ‖u i q - v q‖^2) l (nhds 0) := by
    have hpoint (q : NeutralActualZetaDivisorCoordinate) :
        Tendsto (fun i => ‖u i q - v q‖^2) l (nhds (0 : ℝ)) := by
      have hc : Tendsto (fun _ : ι => v q) l (nhds (v q)) := tendsto_const_nhds
      have h := ((hcoord q).sub hc).norm.pow 2
      simpa using h
    have hd : ∀ᶠ i in l, ∀ q, ‖(‖u i q - v q‖^2 : ℝ)‖ ≤ W q := by
      filter_upwards [hbound] with i hi q
      rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg ‖u i q - v q‖)]
      exact hi q
    simpa only [tsum_zero] using
      (tendsto_tsum_of_dominated_convergence
        (f := fun i q => ‖u i q - v q‖^2)
        (g := fun _ => (0 : ℝ)) hW hpoint hd)
  have hid (i : ι) :
      (∑' q : NeutralActualZetaDivisorCoordinate, ‖u i q - v q‖^2) =
        ‖u i - v‖^2 := by
    have h := (lp.hasSum_norm (by norm_num : 0 < (2:ℝ≥0∞).toReal)
      (u i - v)).tsum_eq
    simpa only [ENNReal.toReal_ofNat, Real.rpow_two, lp.coeFn_sub,
      Pi.sub_apply] using h
  simp_rw [hid] at ht
  apply tendsto_iff_norm_sub_tendsto_zero.mpr
  have hs := Real.continuous_sqrt.continuousAt.tendsto.comp ht
  simpa only [Function.comp_def, Real.sqrt_sq_eq_abs, abs_of_nonneg (norm_nonneg _),
    Real.sqrt_zero] using hs

/-- All positive and negative source samples are actual inner products of
the same physical logarithmic carrier. Uniform bounds on their squared
norms give both exact full-graph membership and the graph limit. -/
theorem neutralNF574ActualFullGraphLimit_of_dyadicDomination
    {ι : Type*} {l : Filter ι}
    (a : ℝ)
    (k : NeutralLogHilbertCarrier a)
    (g : ι → NeutralLogHilbertCarrier a)
    (hg : Tendsto g l (nhds k))
    (C : ℝ) (hC : 0 ≤ C)
    (hkp : ∀ q : NeutralActualZetaDivisorCoordinate,
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) k‖^2
        ≤ C * neutralNF574LogDyadicWeight q)
    (hkn : ∀ q : NeutralActualZetaDivisorCoordinate,
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) k‖^2
        ≤ C * neutralNF574LogDyadicWeight q)
    (hgp : ∀ (i : ι) (q : NeutralActualZetaDivisorCoordinate),
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) (g i)‖^2
        ≤ C * neutralNF574LogDyadicWeight q)
    (hgn : ∀ (i : ι) (q : NeutralActualZetaDivisorCoordinate),
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) (g i)‖^2
        ≤ C * neutralNF574LogDyadicWeight q) :
    ∃ (K : NeutralActualZetaSourceDomain a)
      (G : ι → NeutralActualZetaSourceDomain a),
      neutralActualZetaSourcePhysical a K = k ∧
      (∀ i, neutralActualZetaSourcePhysical a (G i) = g i) ∧
      Tendsto G l (nhds K) := by
  let W := fun q => C * neutralNF574LogDyadicWeight q
  have hW : Summable W := neutralNF574LogDyadicWeight_summable.mul_left C
  have hpK : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) k‖^2) :=
    Summable.of_nonneg_of_le (fun _ => sq_nonneg _) hkp hW
  have hnK : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) k‖^2) :=
    Summable.of_nonneg_of_le (fun _ => sq_nonneg _) hkn hW
  have hpG (i : ι) : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) (g i)‖^2) :=
    Summable.of_nonneg_of_le (fun _ => sq_nonneg _) (hgp i) hW
  have hnG (i : ι) : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) (g i)‖^2) :=
    Summable.of_nonneg_of_le (fun _ => sq_nonneg _) (hgn i) hW
  let K := neutralActualZetaFullSourceLiftOfSquareSummable a k hpK hnK
  let G := fun i => neutralActualZetaFullSourceLiftOfSquareSummable a
    (g i) (hpG i) (hnG i)
  have hK : neutralActualZetaSourcePhysical a K = k := rfl
  have hG (i : ι) : neutralActualZetaSourcePhysical a (G i) = g i := rfl
  have hdiff (x y : ℂ) (w : ℝ) (hx : ‖x‖^2 ≤ w) (hy : ‖y‖^2 ≤ w) :
      ‖x-y‖^2 ≤ 4*w := by
    have hsq := pow_le_pow_left₀ (norm_nonneg (x-y)) (norm_sub_le x y) 2
    nlinarith only [hsq, sq_nonneg (‖x‖-‖y‖), hx, hy]
  have hp : Tendsto (fun i => neutralActualZetaPositiveAnalysis a (G i))
      l (nhds (neutralActualZetaPositiveAnalysis a K)) := by
    apply neutralNF574ActualCoefficients_tendsto_of_domination _ _ (fun q => 4*W q)
      (hW.mul_left 4)
    · intro q
      have h := ((continuous_const : Continuous (fun _ : NeutralLogHilbertCarrier a =>
        neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))).inner
          (𝕜 := ℂ) continuous_id).continuousAt.tendsto.comp hg
      change Tendsto (fun i => inner ℂ
        (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) (g i))
        l (nhds (inner ℂ
          (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) k))
      simpa only [Function.comp_def, id_eq] using h
    · filter_upwards [] with i q
      rw [(neutralActualZetaSourceAnalysis_sampling a (G i) q).1,
        (neutralActualZetaSourceAnalysis_sampling a K q).1, hG i, hK]
      exact hdiff _ _ (W q) (hgp i q) (hkp q)
  have hn : Tendsto (fun i => neutralActualZetaNegativeAnalysis a (G i))
      l (nhds (neutralActualZetaNegativeAnalysis a K)) := by
    apply neutralNF574ActualCoefficients_tendsto_of_domination _ _ (fun q => 4*W q)
      (hW.mul_left 4)
    · intro q
      have h := ((continuous_const : Continuous (fun _ : NeutralLogHilbertCarrier a =>
        neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))).inner
          (𝕜 := ℂ) continuous_id).continuousAt.tendsto.comp hg
      change Tendsto (fun i => inner ℂ
        (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) (g i))
        l (nhds (inner ℂ
          (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) k))
      simpa only [Function.comp_def, id_eq] using h
    · filter_upwards [] with i q
      rw [(neutralActualZetaSourceAnalysis_sampling a (G i) q).2,
        (neutralActualZetaSourceAnalysis_sampling a K q).2, hG i, hK]
      exact hdiff _ _ (W q) (hgn i q) (hkn q)
  refine ⟨K, G, hK, hG, ?_⟩
  apply tendsto_subtype_rng.mpr
  exact hg.prodMk_nhds (hp.prodMk_nhds hn)

end
end WeilDefect
