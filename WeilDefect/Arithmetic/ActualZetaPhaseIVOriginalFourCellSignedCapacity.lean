import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSecondNewCellPrimeGeometry
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWiderThreeCellSourceMeasure
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate ENNReal

/-!
IV022: TRUE original physical FOUR-CELL Lebesgue source capacity.

The ORIGINAL two strict NF543 collars (total width 1/250)
plus IV020's first new [+1/5 ±1/500] (width 1/250)
plus the SECOND prime-separated cell [-1/5 ±1/4000]
(width 1/2000) have exactly total Lebesgue measure 17/2000.

The untouched source physical window b=11/10, signed Gamma
symbol, TWO original poles and all literal von-Mangoldt
arithmetic coefficients are preserved. Exact source
Cauchy–Schwarz gives ||f||_1² ≤ 17/2000 * Mass(f).
Under the GENUINE ORIGINAL prime allowance
 |Re P_original(f,f)| ≤ (2/5)*Mass(f)
the signed IV019 budget gives
 Re W_original(f,f) ≥ (1/16)*Mass(f).

That prime allowance is EXPLICIT in this module. IV022 DOES
NOT claim a complete four-cell prime transfer or unconditional
four-cell Weil positivity: separate authentic source arithmetic
coupling of all four cells remains an open formal obligation.
These are Lean candidates until actual kernel and strict
standard-axiom verification is successful.
-/

/-- The literal physical SECOND new cell; both endpoints fixed
by exact rational arithmetic. -/
def neutralIV022FourthCellInterval : Set ℝ :=
  Set.Icc ((-1/5:ℝ)-(1/4000:ℝ))
    ((-1/5:ℝ)+(1/4000:ℝ))

/-- Actual width 1/2000 of the closed second new interval. -/
theorem neutralIV022FourthCell_volume :
    volume neutralIV022FourthCellInterval =
      ENNReal.ofReal (1/2000:ℝ) := by
  unfold neutralIV022FourthCellInterval
  rw [Real.volume_Icc]
  norm_num

/-- The actual REAL original physical test set with TWO old and
TWO new cells, not a matrix subspace or an artificial support. -/
def neutralIV022FourCellSupport : Set ℝ :=
  neutralIV020WideThreeCellSupport ∪ neutralIV022FourthCellInterval

/-- True physical disjointness of the second added cell from
the historical original two collars AND the first added cell. -/
theorem neutralIV022FourCell_disjoint :
    Disjoint neutralIV020WideThreeCellSupport
      neutralIV022FourthCellInterval := by
  rw [Set.disjoint_left]
  intro x hx hy
  have hFourth :
      (-1/5:ℝ)-(1/4000:ℝ) ≤ x ∧
        x ≤ (-1/5:ℝ)+(1/4000:ℝ) := hy
  change x ∈ neutralNF543OriginalCollars ∪
    neutralIV020WidePhysicalInterval at hx
  rcases hx with hold | hfirst
  · rcases hold with hL | hR
    · linarith [hL.2,hFourth.1]
    · linarith [hR.1,hFourth.2]
  · unfold neutralIV020WidePhysicalInterval at hfirst
    linarith [hfirst.1,hFourth.2]

/-- The authentic whole FOUR-CELL support has exact Lebesgue
measure 1/250+1/250+1/2000=17/2000. -/
theorem neutralIV022FourCell_volume :
    volume neutralIV022FourCellSupport =
      ENNReal.ofReal (17/2000:ℝ) := by
  unfold neutralIV022FourCellSupport
  rw [measure_union neutralIV022FourCell_disjoint
    (by unfold neutralIV022FourthCellInterval; exact measurableSet_Icc),
    neutralIV020WideThreeCell_volume,
    neutralIV022FourthCell_volume,
    ← ENNReal.ofReal_add (by norm_num) (by norm_num)]
  congr 1
  norm_num

/-- Every true physical four-cell complex Schwartz test remains
inside the historical ORIGINAL window [-11/10,11/10];
the literal signed zeta explicit formula cutoff is unchanged. -/
theorem neutralIV022FourCell_supported_window
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x = 0) :
    ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
      f x = 0 := by
  intro x hx
  apply hf x
  intro hcell
  rcases hcell with hthree | hfourth
  · have hwide :
        x ∈ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) := by
      change x∈ neutralNF543OriginalCollars ∪
        neutralIV020WidePhysicalInterval at hthree
      rcases hthree with hold|hfirst
      · rcases hold with hL|hR
        · exact ⟨le_of_lt hL.1,by linarith [hL.2]⟩
        · exact ⟨by linarith [hR.1],le_of_lt hR.2⟩
      · unfold neutralIV020WidePhysicalInterval at hfirst
        exact ⟨by linarith [hfirst.1],by linarith [hfirst.2]⟩
    exact hx hwide
  · unfold neutralIV022FourthCellInterval at hfourth
    exact hx ⟨by linarith [hfourth.1],by linarith [hfourth.2]⟩

theorem neutralIV022FourCell_L1_bound
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → t x = 0) :
    ‖t.toLp 1 volume‖ ≤
      Real.sqrt (neutralNF600Mass t) * Real.sqrt (17/2000) := by
  let E := neutralIV022FourCellSupport
  let μ := volume.restrict E
  have hm : volume E < ∞ := by
    rw [show volume E = ENNReal.ofReal (17/2000:ℝ)
      from neutralIV022FourCell_volume]
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
  have hvol : (∫ _ : ℝ, (1:ℝ) ∂μ) = 17/2000 := by
    change (∫ _ : ℝ in E, (1:ℝ)) = _
    rw [setIntegral_const]
    simp [measureReal_def,E,neutralIV022FourCell_volume]
  have hE : MeasurableSet E := by
    unfold E neutralIV022FourCellSupport
    exact (neutralNF600Collars_measurable.union
      (by unfold neutralIV020WidePhysicalInterval
          exact measurableSet_Icc)).union
      (by unfold neutralIV022FourthCellInterval
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

theorem neutralIV022FourCell_L1_sq
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → t x = 0) :
    ‖t.toLp 1 volume‖^2 ≤
      (17/2000:ℝ) * neutralNF600Mass t := by
  have h := neutralIV022FourCell_L1_bound t ht
  have hm : 0 ≤ neutralNF600Mass t := by
    unfold neutralNF600Mass
    positivity
  have hsq := pow_le_pow_left₀ (norm_nonneg _) h 2
  calc
    _ ≤ (Real.sqrt (neutralNF600Mass t) *
      Real.sqrt (17/2000))^2 := hsq
    _ = _ := by
      rw [mul_pow,Real.sq_sqrt hm,
        Real.sq_sqrt (by norm_num)]
      ring

/-- The complete true original signed zeta Weil conditional
FOUR-CELL capacity theorem. The EXACT original prime allowance
is an EXPLICIT hypothesis; it has not been transferred across all
four physical cells in this stage.

The numerical coefficient 1/16 is a guaranteed candidate only
under the true prime magnitude and compiled Cauchy–Schwarz source
lemmas. No global positivity, equivalence or RH is assumed. -/
theorem neutralIV022FourCell_oneSixteenth_of_originalPrime
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x = 0)
    (hprime :
      |(neutralIV011OriginalMixedPrime
          (11/10:ℝ) f f).re| ≤
        (2/5:ℝ)*neutralNF600Mass f) :
    (1/16:ℝ)*neutralNF600Mass f ≤
      (neutralIV010Diagonal (11/10:ℝ) f).re := by
  have hsource := neutralIV019OriginalSignedWeil_massBudget_of_prime
    f (17/2000:ℝ)
    (neutralIV022FourCell_supported_window f hf)
    hprime (neutralIV022FourCell_L1_sq f hf)
  convert hsource using 1 <;> norm_num

/-- Explicit capacity threshold for ONE additional physical
centered cell of radius r, after the first new radius 1/500:
the coarse ORIGINAL signed estimate is positive exactly when
r < 1/1500. This threshold is not a genuine no-go theorem. -/
theorem neutralIV022AdditionalCell_radiusMargin_iff
    (r : ℝ) :
    (0:ℝ) < (1/10:ℝ)-150*r ↔ r < 1/1500 := by
  constructor <;> intro h <;> linarith

/-- Exact rational signed original capacity after adding the
second cell radius 1/4000: the prospective coercive
margin is 1/16, conditional on the true prime transfer. -/
theorem neutralIV022FourthCell_exactMargin :
    (7/10:ℝ) - 75*(17/2000:ℝ) = 1/16 := by
  norm_num

#print axioms neutralIV020WideThreeCell_volume
#print axioms neutralIV019OriginalSignedWeil_massBudget_of_prime
#print axioms neutralIV021WholeThreeCellOriginalWeil_oneTenth
#print axioms neutralIV022SecondFrozenTwoCollarActiveGap
#print axioms neutralIV022FourthCell_volume
#print axioms neutralIV022FourCell_disjoint
#print axioms neutralIV022FourCell_volume
#print axioms neutralIV022FourCell_supported_window
#print axioms neutralIV022FourCell_L1_bound
#print axioms neutralIV022FourCell_L1_sq
#print axioms neutralIV022FourCell_oneSixteenth_of_originalPrime
#print axioms neutralIV022AdditionalCell_radiusMargin_iff
#print axioms neutralIV022FourthCell_exactMargin

end
end WeilDefect
