import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalVariableWidthSignedBudget
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalThreeCellSignedEnvelope
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWiderPrimeFreeBump
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate ENNReal

/-!
IV020: ORIGINAL NF543 strict TWO collar support plus a new DOUBLED
radius 1/500 complex Schwartz interval. Unlike IV019's prospective
measure budget, this module attaches an actual real three-cell source
union E = E_old ∪ [99/500,101/500] and its EXACT Lebesgue
measure 1/125, with genuine source Cauchy–Schwarz L1² ≤ Mass/125.

Original signed Weil 1/10 arithmetic coercivity follows from IV019's
authentic pole+Gamma+vonMangoldt bound provided the ORIGINAL full
n9-prime allowance is verified on the new support; the next file
certifies that additional true-source n9 transfer as a Lean candidate.
Neither module is kernel accepted without a real axiom-audited build.
-/

/-- Literal new physical cell, twice as wide as the IV018 cell. -/
def neutralIV020WidePhysicalInterval : Set ℝ :=
  Set.Icc (99/500:ℝ) (101/500:ℝ)

/-- EXACT real measure of the wider closed physical interval. -/
theorem neutralIV020WidePhysicalInterval_volume :
    volume neutralIV020WidePhysicalInterval =
      ENNReal.ofReal (1/250:ℝ) := by
  unfold neutralIV020WidePhysicalInterval
  rw [Real.volume_Icc]
  norm_num

/-- IV019 real smooth bump's explicit source support is exactly the
new physical interval, using arithmetic equality of endpoints. -/
theorem neutralIV020Wide_support_from_bump
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) → t x = 0) :
    ∀ x : ℝ, x ∉ neutralIV020WidePhysicalInterval → t x = 0 := by
  simpa only [neutralIV020WidePhysicalInterval,
    show (1/5:ℝ)-(1/500:ℝ) = 99/500 by norm_num,
    show (1/5:ℝ)+(1/500:ℝ) = 101/500 by norm_num] using ht

def neutralIV020WideThreeCellSupport : Set ℝ :=
  neutralNF543OriginalCollars ∪ neutralIV020WidePhysicalInterval

/-- All three real cells are physically disjoint by exact
rational endpoints, no approximate support geometry. -/
theorem neutralIV020WideOldNew_disjoint :
    Disjoint neutralNF543OriginalCollars
      neutralIV020WidePhysicalInterval := by
  rw [Set.disjoint_left]
  intro x hx hy
  rcases hx with hL | hR
  · unfold neutralIV020WidePhysicalInterval at hy
    rcases hy with ⟨hyl, _⟩
    linarith [hL.2]
  · unfold neutralIV020WidePhysicalInterval at hy
    rcases hy with ⟨_, hyr⟩
    linarith [hR.1]

/-- Exact UNION measure: old original TWO collars have 1/250
and the newly admitted physical interval has 1/250. -/
theorem neutralIV020WideThreeCell_volume :
    volume neutralIV020WideThreeCellSupport =
      ENNReal.ofReal (1/125:ℝ) := by
  unfold neutralIV020WideThreeCellSupport
  rw [measure_union neutralIV020WideOldNew_disjoint
    (by unfold neutralIV020WidePhysicalInterval; exact measurableSet_Icc),
    neutralNF600Collars_volume,
    neutralIV020WidePhysicalInterval_volume,
    ← ENNReal.ofReal_add (by norm_num) (by norm_num)]
  congr 1
  norm_num

/-- Three-cell-supported tests still fit inside the SAME frozen
original physical window [-11/10,11/10]. Enlarging the source
class does not change the authentic EF physical radius. -/
theorem neutralIV020WideThreeCell_supported_window
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → t x = 0) :
    ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
      t x = 0 := by
  intro x hx
  apply ht x
  intro hnew
  rcases hnew with hold | hnarrow
  · exact hx ⟨by
      rcases hold with hL|hR
      · exact le_of_lt hL.1
      · linarith [hR.1], by
      rcases hold with hL|hR
      · linarith [hL.2]
      · exact le_of_lt hR.2⟩
  · unfold neutralIV020WidePhysicalInterval at hnarrow
    exact hx ⟨by linarith [hnarrow.1],by linarith [hnarrow.2]⟩

/-- Authentic L1/L2 physical support-size estimate for
arbitrary COMPLEX Schwartz input in the full three-cell set.
This is a source-specific Cauchy-Schwarz bound over a real
Lebesgue measurable set of EXACT measure 1/125. -/
theorem neutralIV020WideThreeCell_L1_bound
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → t x = 0) :
    ‖t.toLp 1 volume‖ ≤
      Real.sqrt (neutralNF600Mass t) * Real.sqrt (1/125) := by
  let E := neutralIV020WideThreeCellSupport
  let μ := volume.restrict E
  have hm : volume E < ∞ := by
    rw [show volume E = ENNReal.ofReal (1/125:ℝ)
      from neutralIV020WideThreeCell_volume]
    exact ENNReal.ofReal_lt_top
  letI : IsFiniteMeasure μ := ⟨by simpa [μ] using hm⟩
  have h2 : MemLp (fun x : ℝ => t x)
      (ENNReal.ofReal 2) μ := by
    simpa using (t.memLp 2 volume).mono_measure Measure.restrict_le_self
  have h1 : MemLp (fun _ : ℝ => (1:ℂ))
      (ENNReal.ofReal 2) μ := memLp_const _
  have hh := integral_mul_norm_le_Lp_mul_Lq
    (μ := μ) (p := 2) (q := 2)
    Real.HolderConjugate.two_two h2 h1
  simp only [norm_one, mul_one, Real.rpow_two, one_pow,
    ← Real.sqrt_eq_rpow] at hh
  have hvol : (∫ _ : ℝ, (1:ℝ) ∂μ) = 1/125 := by
    change (∫ _ : ℝ in E, (1:ℝ)) = _
    rw [setIntegral_const]
    simp [measureReal_def,E,neutralIV020WideThreeCell_volume]
  have hE : MeasurableSet E := by
    unfold E neutralIV020WideThreeCellSupport
    exact neutralNF600Collars_measurable.union
      (by unfold neutralIV020WidePhysicalInterval
          exact measurableSet_Icc)
  have hi1 : (∫ x : ℝ, ‖t x‖ ∂μ) =
      ∫ x : ℝ, ‖t x‖ := by
    change (∫ x in E, ‖t x‖) = _
    rw [← integral_indicator hE]
    congr 1
    funext x
    by_cases hx : x ∈ E
    · exact Set.indicator_of_mem hx _
    · rw [Set.indicator_of_notMem hx, ht x hx]
      simp
  have hi2 : (∫ x : ℝ, ‖t x‖^2 ∂μ) =
      neutralNF600Mass t := by
    rw [neutralNF600Mass_eq_integral]
    change (∫ x in E, ‖t x‖^2) = _
    rw [← integral_indicator hE]
    congr 1
    funext x
    by_cases hx : x ∈ E
    · exact Set.indicator_of_mem hx _
    · rw [Set.indicator_of_notMem hx, ht x hx]
      simp
  rw [hi1,hi2,hvol] at hh
  rw [SchwartzMap.norm_toLp_one]
  exact hh

theorem neutralIV020WideThreeCell_L1_sq
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → t x = 0) :
    ‖t.toLp 1 volume‖^2 ≤
      (1/125:ℝ) * neutralNF600Mass t := by
  have h := neutralIV020WideThreeCell_L1_bound t ht
  have hm : 0 ≤ neutralNF600Mass t := by
    unfold neutralNF600Mass
    positivity
  have hsq := pow_le_pow_left₀ (norm_nonneg _) h 2
  calc
    _ ≤ (Real.sqrt (neutralNF600Mass t) *
      Real.sqrt (1/125))^2 := hsq
    _ = _ := by
      rw [mul_pow,Real.sq_sqrt hm,
        Real.sq_sqrt (by norm_num)]
      ring

/-- The EXACT signed original one-tenth Weil margin is now
attached to real L1 support custody of the broader three-cell
class. Only the genuine original n9 prime bound remains an
explicit source hypothesis here; the companion IV020 module
proves it from original finite ±log active-prime correlations. -/
theorem neutralIV020WideThreeCell_oneTenth_of_primeBound
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → f x = 0)
    (hprime :
      |(neutralIV011OriginalMixedPrime
        (11/10:ℝ) f f).re| ≤
        (2/5:ℝ) * neutralNF600Mass f) :
    (1/10:ℝ)*neutralNF600Mass f ≤
      (neutralIV010Diagonal (11/10:ℝ) f).re := by
  exact neutralIV019OriginalOneTenth_of_prime_and_L1 f
    (neutralIV020WideThreeCell_supported_window f hf)
    hprime
    (neutralIV020WideThreeCell_L1_sq f hf)

#print axioms neutralNF600Collars_volume
#print axioms neutralIV019OriginalOneTenth_of_prime_and_L1
#print axioms neutralIV019WideFrozenConcrete_allIntegerGap
#print axioms neutralIV020WidePhysicalInterval_volume
#print axioms neutralIV020Wide_support_from_bump
#print axioms neutralIV020WideOldNew_disjoint
#print axioms neutralIV020WideThreeCell_volume
#print axioms neutralIV020WideThreeCell_supported_window
#print axioms neutralIV020WideThreeCell_L1_bound
#print axioms neutralIV020WideThreeCell_L1_sq
#print axioms neutralIV020WideThreeCell_oneTenth_of_primeBound

end
end WeilDefect
