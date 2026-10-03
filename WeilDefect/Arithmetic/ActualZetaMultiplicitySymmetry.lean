import WeilDefect.Arithmetic.ActualZetaMultiplicity
import Mathlib.Analysis.Calculus.Deriv.Star
import Mathlib.Analysis.Complex.CauchyIntegral

namespace WeilDefect

noncomputable section

open scoped ENat Topology ComplexConjugate
open Filter

/-- Actual zeta conjugation preserves all derivatives, including their junk
values. The analytic-order application below separately supplies analyticity. -/
theorem neutralActualZetaIteratedDeriv_conjugate (n : ℕ) (z : ℂ) :
    iteratedDeriv n riemannZeta (conj z) =
      conj (iteratedDeriv n riemannZeta z) := by
  have hzero : conj ∘ riemannZeta ∘ conj = riemannZeta := by
    funext w
    simp only [Function.comp_apply, riemannZeta_conj, starRingEnd_apply, star_star]
  have hall : ∀ k : ℕ, conj ∘ iteratedDeriv k riemannZeta ∘ conj =
      iteratedDeriv k riemannZeta := by
    intro k
    induction k with
    | zero => simpa only [iteratedDeriv_zero] using hzero
    | succ k ih =>
      rw [iteratedDeriv_succ, ← deriv_conj_conj, ih]
  simpa only [Function.comp_apply, starRingEnd_apply, star_star] using
    (congrFun (hall n) (conj z)).symm

theorem neutralActualZetaOrder_conjugate (ρ : NeutralActualZetaZeroPoint) :
    analyticOrderAt riemannZeta (neutralActualZetaZeroConjugate ρ).val =
      analyticOrderAt riemannZeta ρ.val := by
  have hdata := (analyticOrderAt_eq_nat_iff_iteratedDeriv_eq_zero
    (hf := neutralActualZetaZeroPoint_analytic ρ)).mp
      (neutralActualZetaMultiplicity_order ρ).symm
  rw [← neutralActualZetaMultiplicity_order ρ]
  apply (analyticOrderAt_eq_nat_iff_iteratedDeriv_eq_zero
    (hf := neutralActualZetaZeroPoint_analytic
      (neutralActualZetaZeroConjugate ρ))).mpr
  constructor
  · intro k hk
    change iteratedDeriv k riemannZeta (conj ρ.val) = 0
    rw [neutralActualZetaIteratedDeriv_conjugate, hdata.1 k hk, map_zero]
  · change iteratedDeriv (neutralActualZetaMultiplicity ρ) riemannZeta (conj ρ.val) ≠ 0
    rw [neutralActualZetaIteratedDeriv_conjugate]
    intro h
    apply hdata.2
    simpa only [starRingEnd_apply, star_star, map_zero] using
      congrArg (starRingEnd ℂ) h

theorem neutralActualZetaMultiplicity_conjugate (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaMultiplicity (neutralActualZetaZeroConjugate ρ) =
      neutralActualZetaMultiplicity ρ :=
  congrArg ENat.toNat (neutralActualZetaOrder_conjugate ρ)

theorem neutralActualZetaZeroPoint_ne_zero (ρ : NeutralActualZetaZeroPoint) :
    ρ.val ≠ 0 := by
  intro h
  have hre := congrArg Complex.re h
  simp only [Complex.zero_re] at hre
  linarith [ρ.property.2.1]

/-- Actual completed zeta is analytic at every open-strip zero point. -/
theorem neutralActualZetaCompleted_analytic (ρ : NeutralActualZetaZeroPoint) :
    AnalyticAt ℂ completedRiemannZeta ρ.val := by
  apply analyticAt_iff_eventually_differentiableAt.mpr
  have hzero : {0}ᶜ ∈ 𝓝 ρ.val :=
    isOpen_compl_singleton.mem_nhds
      (by simpa using neutralActualZetaZeroPoint_ne_zero ρ)
  have hone : {1}ᶜ ∈ 𝓝 ρ.val :=
    isOpen_compl_singleton.mem_nhds
      (by simpa using neutralActualZetaZeroPoint_ne_one ρ)
  filter_upwards [hzero, hone] with z hz0 hz1
  exact differentiableAt_completedZeta (by simpa using hz0) (by simpa using hz1)

/-- Removing the actual nonvanishing Gamma factor preserves analytic order.
The globally analytic reciprocal avoids assuming analyticity at a Gamma pole. -/
theorem neutralActualZetaOrder_completed (ρ : NeutralActualZetaZeroPoint) :
    analyticOrderAt completedRiemannZeta ρ.val =
      analyticOrderAt riemannZeta ρ.val := by
  have heq : riemannZeta =ᶠ[𝓝 ρ.val]
      fun z => completedRiemannZeta z * (Complex.Gammaℝ z)⁻¹ := by
    have hzero : {0}ᶜ ∈ 𝓝 ρ.val :=
      isOpen_compl_singleton.mem_nhds
        (by simpa using neutralActualZetaZeroPoint_ne_zero ρ)
    filter_upwards [hzero] with z hz
    simpa only [div_eq_mul_inv] using
      riemannZeta_def_of_ne_zero (by simpa using hz)
  rw [analyticOrderAt_congr heq,
    analyticOrderAt_mul (neutralActualZetaCompleted_analytic ρ)
      (Complex.differentiable_Gammaℝ_inv.analyticAt ρ.val),
    analyticOrderAt_eq_zero.mpr
      (.inr (inv_ne_zero (Complex.Gammaℝ_ne_zero_of_re_pos ρ.property.2.1))),
    add_zero]

/-- The actual functional equation preserves analytic multiplicity:
its completed form is invariant under the affine map with derivative -1. -/
theorem neutralActualZetaOrder_reflect (ρ : NeutralActualZetaZeroPoint) :
    analyticOrderAt riemannZeta (neutralActualZetaZeroReflect ρ).val =
      analyticOrderAt riemannZeta ρ.val := by
  rw [← neutralActualZetaOrder_completed (neutralActualZetaZeroReflect ρ),
    ← neutralActualZetaOrder_completed ρ]
  have heq : completedRiemannZeta ∘ (fun z : ℂ => 1 - z) =
      completedRiemannZeta :=
    funext completedRiemannZeta_one_sub
  have horder := analyticOrderAt_comp_of_deriv_ne_zero
    (f := completedRiemannZeta) (g := fun z : ℂ => 1 - z) (z₀ := ρ.val)
    (by fun_prop) (by simp)
  rw [heq] at horder
  exact horder.symm

theorem neutralActualZetaMultiplicity_reflect (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaMultiplicity (neutralActualZetaZeroReflect ρ) =
      neutralActualZetaMultiplicity ρ :=
  congrArg ENat.toNat (neutralActualZetaOrder_reflect ρ)

theorem neutralActualZetaMultiplicity_pair (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaMultiplicity (neutralActualZetaZeroPair ρ) =
      neutralActualZetaMultiplicity ρ := by
  unfold neutralActualZetaZeroPair
  rw [neutralActualZetaMultiplicity_reflect, neutralActualZetaMultiplicity_conjugate]

/-- The actual point pair lifts to divisor copies with the same copy label. -/
def neutralActualZetaDivisorPair (q : NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaDivisorCoordinate :=
  ⟨neutralActualZetaZeroPair q.1,
    ⟨q.2.val, by rw [neutralActualZetaMultiplicity_pair]; exact q.2.isLt⟩⟩

theorem neutralActualZetaDivisorPair_involutive :
    Function.Involutive neutralActualZetaDivisorPair := by
  intro q
  apply Sigma.ext (neutralActualZetaZeroPair_involutive q.1)
  exact (Fin.heq_ext_iff
    (congrArg neutralActualZetaMultiplicity
      (neutralActualZetaZeroPair_involutive q.1))).mpr rfl

theorem neutralActualZetaDivisorOrdinate_pair (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaDivisorOrdinate (neutralActualZetaDivisorPair q) =
      conj (neutralActualZetaDivisorOrdinate q) :=
  neutralActualZetaOrdinate_pair q.1

/-- Actual multiplicity weight on the existing normalized negative pair column. -/
def neutralActualZetaWeightedNegativeSource (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    NeutralLogHilbertCarrier a :=
  ((Real.sqrt (neutralActualZetaMultiplicity ρ : ℝ)) : ℂ) •
    neutralLogNegativePairSource a (neutralActualZetaOrdinate ρ)

theorem neutralActualZetaWeightedNegativeSource_pair
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaWeightedNegativeSource a (neutralActualZetaZeroPair ρ) =
      -neutralActualZetaWeightedNegativeSource a ρ := by
  unfold neutralActualZetaWeightedNegativeSource
  rw [neutralActualZetaMultiplicity_pair, neutralActualZetaPair_negativeSource, smul_neg]

/-- Actual integer multiplicity weight on the existing selected rank-one. -/
def neutralActualZetaWeightedSelectedOperator (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :=
  (neutralActualZetaMultiplicity ρ : ℂ) •
    neutralLogSelectedPairOperator a (neutralActualZetaOrdinate ρ)

theorem neutralActualZetaWeightedSelectedOperator_pair
    (a : ℝ) (ρ : NeutralActualZetaZeroPoint) :
    neutralActualZetaWeightedSelectedOperator a (neutralActualZetaZeroPair ρ) =
      neutralActualZetaWeightedSelectedOperator a ρ := by
  unfold neutralActualZetaWeightedSelectedOperator
  rw [neutralActualZetaMultiplicity_pair, neutralActualZetaPair_selectedOperator]

end

end WeilDefect
