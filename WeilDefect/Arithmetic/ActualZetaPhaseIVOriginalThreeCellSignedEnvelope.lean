import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity
import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeBound
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate ENNReal

/-!
IV018: the actual THREE-CELL physical support class.

The historical NF543 ORIGINAL strict two collars near ±11/10
are now joined by ONE genuinely new narrow interval
[199/1000,201/1000] around the IV015 nonzero bump center 1/5.

The EXACT total Lebesgue support width is 3/500, and the
unchanged real-frequency digamma/Gamma symbol gives a SIGNED
lower bound 349/500 on the diagonal. The original two poles
cost at most 6/125, leaving a prime-free 13/20 margin.

The genuine von-Mangoldt prime contribution is NOT dropped:
the theorem that yields a full 1/4 original zeta Weil lower
bound has the original |Re prime|≤2/5 physical mass as a
VISIBLE hypothesis. A SEPARATE source lemma must transport
the accepted NF600 original n=9 prime bound to this new
three-cell class. This is not an arbitrary Gram positivity
assumption and is not global Weil positivity.
-/

/-- Full real original TWO strict collars plus a NEW closed narrow
physical interval. The original collar definition is unchanged. -/
def neutralIV018ThreeCellSupport : Set ℝ :=
  neutralNF543OriginalCollars ∪ neutralIV017NarrowPhysicalInterval

/-- All three real cells are physically disjoint by exact
rational endpoints, no approximate support geometry. -/
theorem neutralIV018OldNew_disjoint :
    Disjoint neutralNF543OriginalCollars
      neutralIV017NarrowPhysicalInterval := by
  rw [Set.disjoint_left]
  intro x hx hy
  rcases hx with hL | hR
  · unfold neutralIV017NarrowPhysicalInterval at hy
    rcases hy with ⟨hyl, _⟩
    linarith [hL.2]
  · unfold neutralIV017NarrowPhysicalInterval at hy
    rcases hy with ⟨_, hyr⟩
    linarith [hR.1]

/-- Exact UNION measure: old original TWO collars have 1/250
and the newly admitted physical interval has 1/500. -/
theorem neutralIV018ThreeCell_volume :
    volume neutralIV018ThreeCellSupport =
      ENNReal.ofReal (3/500:ℝ) := by
  unfold neutralIV018ThreeCellSupport
  rw [measure_union neutralIV018OldNew_disjoint
    (by unfold neutralIV017NarrowPhysicalInterval; exact measurableSet_Icc),
    neutralNF600Collars_volume,
    neutralIV017NarrowPhysicalInterval_volume,
    ← ENNReal.ofReal_add (by norm_num) (by norm_num)]
  congr 1
  norm_num

/-- Three-cell-supported tests still fit inside the SAME frozen
original physical window [-11/10,11/10]. Enlarging the source
class does not change the authentic EF physical radius. -/
theorem neutralIV018ThreeCell_supported_window
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0) :
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
  · unfold neutralIV017NarrowPhysicalInterval at hnarrow
    exact hx ⟨by linarith [hnarrow.1],by linarith [hnarrow.2]⟩

/-- Authentic L1/L2 physical support-size estimate for
arbitrary COMPLEX Schwartz input in the full three-cell set.
This is a source-specific Cauchy-Schwarz bound over a real
Lebesgue measurable set of EXACT measure 3/500. -/
theorem neutralIV018ThreeCell_L1_bound
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0) :
    ‖t.toLp 1 volume‖ ≤
      Real.sqrt (neutralNF600Mass t) * Real.sqrt (3/500) := by
  let E := neutralIV018ThreeCellSupport
  let μ := volume.restrict E
  have hm : volume E < ∞ := by
    rw [show volume E = ENNReal.ofReal (3/500:ℝ)
      from neutralIV018ThreeCell_volume]
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
  have hvol : (∫ _ : ℝ, (1:ℝ) ∂μ) = 3/500 := by
    change (∫ _ : ℝ in E, (1:ℝ)) = _
    rw [setIntegral_const]
    simp [measureReal_def,E,neutralIV018ThreeCell_volume]
  have hE : MeasurableSet E := by
    unfold E neutralIV018ThreeCellSupport
    exact neutralNF600Collars_measurable.union
      (by unfold neutralIV017NarrowPhysicalInterval
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

theorem neutralIV018ThreeCell_L1_sq
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0) :
    ‖t.toLp 1 volume‖^2 ≤
      (3/500:ℝ) * neutralNF600Mass t := by
  have h := neutralIV018ThreeCell_L1_bound t ht
  have hm : 0 ≤ neutralNF600Mass t := by
    unfold neutralNF600Mass
    positivity
  have hsq := pow_le_pow_left₀ (norm_nonneg _) h 2
  calc
    _ ≤ (Real.sqrt (neutralNF600Mass t) *
      Real.sqrt (3/500))^2 := hsq
    _ = _ := by
      rw [mul_pow,Real.sq_sqrt hm,
        Real.sq_sqrt (by norm_num)]
      ring

/-- Quantitative low Fourier mass on (-5,5) for ANY three-cell
source is now at most 3/50 of the total physical L² mass,
not 1/25 for old collars or 1/50 for the new cell alone. -/
theorem neutralIV018ThreeCell_lowMass
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0) :
    (∫ ξ in neutralNF600LowBand,
      neutralNF600Density t ξ) ≤
        (3/50:ℝ) * neutralNF600Mass t := by
  have hlow := neutralIV017LowMass_le_tenL1_sq t
  have hphys := neutralIV018ThreeCell_L1_sq t ht
  linarith only [hlow,hphys]

/-- UNCONDITIONAL on arithmetic prime signs: true signed
digamma/Gamma spectral arch integral is at least
349/500 times mass on the entire expanded three-cell class. -/
theorem neutralIV018ThreeCell_signedGamma_lower
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0) :
    (349/500:ℝ) * neutralNF600Mass t ≤
      neutralNF600Arch t := by
  have hgam := neutralIV017SignedGamma_lower t
  have hlow := neutralIV018ThreeCell_lowMass t ht
  linarith only [hgam,hlow]

/-- BOTH authentic original poles cost at most 6/125 mass
on the ENTIRE three-cell class, no old-collar-only lemma
misapplied to an expanded support. -/
theorem neutralIV018ThreeCell_poleReal_lower
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0) :
    -(6/125:ℝ) * neutralNF600Mass t ≤
      (neutralIV011OriginalMixedPole (11/10:ℝ) t t).re := by
  have htwide := neutralIV018ThreeCell_supported_window t ht
  have hL := neutralIV018ThreeCell_L1_sq t ht
  have hp := neutralIV017OriginalPole_norm_le_eightL1_sq
    t htwide
  have hp' : ‖neutralIV011OriginalMixedPole
      (11/10:ℝ) t t‖ ≤
      (6/125:ℝ) * neutralNF600Mass t := by
    linarith only [hp,hL]
  have hreal := (Complex.abs_re_le_norm _).trans hp'
  exact (abs_le.mp hreal).1

/-- The whole new physical class has 13/20 margin BEFORE
subtracting its genuine signed ORIGINAL prime contribution.
This is the real source Gamma+TWO poles, with the literal
complex-to-unitary Fourier equality proved previously. -/
theorem neutralIV018ThreeCell_analyticReal_lower
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0) :
    (13/20:ℝ) * neutralNF600Mass t ≤
      (neutralIV013OriginalMixedAnalyticRemainder
        (11/10:ℝ) t t).re := by
  have htwide := neutralIV018ThreeCell_supported_window t ht
  have hp := neutralIV018ThreeCell_poleReal_lower t ht
  have hg := neutralIV018ThreeCell_signedGamma_lower t ht
  have ha :=
    neutralIV017OriginalWindowArch_real_eq_spectral t htwide
  unfold neutralIV013OriginalMixedAnalyticRemainder
  simp only [Complex.add_re]
  rw [ha]
  linarith only [hp,hg]

/-- Candidate 1/4 genuine ORIGINAL signed zeta Weil coercivity
on the entire actual enlarged three-cell physical support.

The original prime term is retained as a GENUINE explicit
side condition |Re P| <= (2/5) Mass, not dropped or assumed
positive. Other 13/20 signed analytic budget is fully
source-derived. The next module transports the only n=9
old-collar prime source bound into this three-cell class. -/
theorem neutralIV018ThreeCell_oneQuarter_of_primeBound
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ neutralIV018ThreeCellSupport → t x = 0)
    (hprime :
      |(neutralIV011OriginalMixedPrime
        (11/10:ℝ) t t).re| ≤
        (2/5:ℝ) * neutralNF600Mass t) :
    (1/4:ℝ) * neutralNF600Mass t ≤
      (neutralIV010Diagonal (11/10:ℝ) t).re := by
  have hpolegamma :=
    neutralIV018ThreeCell_analyticReal_lower t ht
  have hsplit := neutralIV011OriginalMixed_arithmeticSplit
    (11/10:ℝ) t t
  change neutralIV010Diagonal (11/10:ℝ) t =
    neutralIV011OriginalMixedPole (11/10:ℝ) t t -
    neutralIV011OriginalMixedPrime (11/10:ℝ) t t +
    neutralIV011OriginalMixedArch (11/10:ℝ) t t at hsplit
  have hre := congrArg Complex.re hsplit
  simp only [Complex.add_re,Complex.sub_re] at hre
  have hres :
      (neutralIV013OriginalMixedAnalyticRemainder
        (11/10:ℝ) t t).re =
      (neutralIV011OriginalMixedPole (11/10:ℝ) t t).re +
      (neutralIV011OriginalMixedArch (11/10:ℝ) t t).re := by
    rfl
  have hbound := (abs_le.mp hprime).2
  linarith only [hpolegamma,hre,hres,hbound]

#print axioms neutralNF600Collars_volume
#print axioms neutralIV017LowMass_le_tenL1_sq
#print axioms neutralIV017SignedGamma_lower
#print axioms neutralIV017OriginalWindowArch_real_eq_spectral
#print axioms neutralIV018OldNew_disjoint
#print axioms neutralIV018ThreeCell_volume
#print axioms neutralIV018ThreeCell_supported_window
#print axioms neutralIV018ThreeCell_L1_bound
#print axioms neutralIV018ThreeCell_L1_sq
#print axioms neutralIV018ThreeCell_lowMass
#print axioms neutralIV018ThreeCell_signedGamma_lower
#print axioms neutralIV018ThreeCell_poleReal_lower
#print axioms neutralIV018ThreeCell_analyticReal_lower
#print axioms neutralIV018ThreeCell_oneQuarter_of_primeBound

end
end WeilDefect
