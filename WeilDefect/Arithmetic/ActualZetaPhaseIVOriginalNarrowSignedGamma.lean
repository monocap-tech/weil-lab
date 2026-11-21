import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal
import WeilDefect.Arithmetic.ActualZetaOriginalCollarArchLower
import WeilDefect.Arithmetic.ActualZetaOriginalCollarGammaLower
import WeilDefect.Arithmetic.ActualZetaOriginalCollarLiteralArch
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate ENNReal

/-!
IV017, part one. Genuine source-specific narrow-support spectral
concentration and SIGNED original Gamma coercivity.

The frozen new test interval is [199/1000, 201/1000]. The full
width is exactly 1/500; the old historical NF543 collars are
unchanged. This is not an abstract spectral operator or an
assumed Fourier low-band bound: the bounds are derived from the
actual Schwartz physical L¹/L² norms via the existing Mathlib
Fourier transform and Cauchy–Schwarz measure on the real interval.

The original NF599 digamma symbol lower bounds are retained:
gammaBracket(-2*pi*xi) >= -28/5 for all xi, and >= 11/10
whenever |xi|>=5. Hence the precise low-frequency penalty is
67/10, not an unsigned Gamma absolute integral.

Source is a Lean candidate until real independent kernel audit.
-/

def neutralIV017NarrowPhysicalInterval : Set ℝ :=
  Set.Icc (199/1000:ℝ) (201/1000:ℝ)

/-- The original candidate physical interval has EXACT Lebesgue
measure 1/500 (not two collars and not an artificial cutoff). -/
theorem neutralIV017NarrowPhysicalInterval_volume :
    volume neutralIV017NarrowPhysicalInterval =
      ENNReal.ofReal (1/500:ℝ) := by
  unfold neutralIV017NarrowPhysicalInterval
  rw [Real.volume_Icc]
  norm_num

/-- Source-compatible pointwise interval support, exactly the same
candidate around 1/5, radius 1/1000 constructed by IV015. -/
theorem neutralIV017Narrow_support_from_bump
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/1000:ℝ))
        ((1/5:ℝ)+(1/1000:ℝ)) → t x = 0) :
    ∀ x : ℝ, x ∉ neutralIV017NarrowPhysicalInterval → t x = 0 := by
  simpa only [neutralIV017NarrowPhysicalInterval,
    show (1/5:ℝ)-(1/1000:ℝ) = 199/1000 by norm_num,
    show (1/5:ℝ)+(1/1000:ℝ) = 201/1000 by norm_num] using ht

/-- TRUE physical L¹/L² uncertainty charge at width 1/500.
The interval support and exact original Lebesgue measure are used,
rather than importing an NF600 collar-only inequality. -/
theorem neutralIV017NarrowL1_bound
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ, x ∉ neutralIV017NarrowPhysicalInterval → t x = 0) :
    ‖t.toLp 1 volume‖ ≤
      Real.sqrt (neutralNF600Mass t) * Real.sqrt (1/500) := by
  let E := neutralIV017NarrowPhysicalInterval
  let μ := volume.restrict E
  have hm : volume E < ∞ := by
    rw [show volume E = ENNReal.ofReal (1/500:ℝ)
      from neutralIV017NarrowPhysicalInterval_volume]
    exact ENNReal.ofReal_lt_top
  letI : IsFiniteMeasure μ := ⟨by simpa [μ] using hm⟩
  have h2 : MemLp (fun x : ℝ => t x) (ENNReal.ofReal 2) μ := by
    simpa using (t.memLp 2 volume).mono_measure Measure.restrict_le_self
  have h1 : MemLp (fun _ : ℝ => (1:ℂ)) (ENNReal.ofReal 2) μ :=
    memLp_const _
  have hh := integral_mul_norm_le_Lp_mul_Lq
    (μ := μ) (p := 2) (q := 2) Real.HolderConjugate.two_two h2 h1
  simp only [norm_one, mul_one, Real.rpow_two, one_pow,
    ← Real.sqrt_eq_rpow] at hh
  have hvol : (∫ _ : ℝ, (1:ℝ) ∂μ) = 1/500 := by
    change (∫ _ : ℝ in E, (1:ℝ)) = _
    rw [setIntegral_const]
    simp [measureReal_def, E, neutralIV017NarrowPhysicalInterval_volume]
  have hi1 : (∫ x : ℝ, ‖t x‖ ∂μ) = ∫ x : ℝ, ‖t x‖ := by
    change (∫ x in E, ‖t x‖) = _
    rw [← integral_indicator
      (show MeasurableSet E by
        exact measurableSet_Icc)]
    congr 1
    funext x
    by_cases hx : x ∈ E
    · exact Set.indicator_of_mem hx _
    · rw [Set.indicator_of_notMem hx,ht x hx]
      simp
  have hi2 : (∫ x : ℝ, ‖t x‖^2 ∂μ) =
      neutralNF600Mass t := by
    rw [neutralNF600Mass_eq_integral]
    change (∫ x in E, ‖t x‖^2) = _
    rw [← integral_indicator
      (show MeasurableSet E by
        exact measurableSet_Icc)]
    congr 1
    funext x
    by_cases hx : x ∈ E
    · exact Set.indicator_of_mem hx _
    · rw [Set.indicator_of_notMem hx,ht x hx]
      simp
  rw [hi1,hi2,hvol] at hh
  rw [SchwartzMap.norm_toLp_one]
  exact hh

/-- Quantitative physical mass charge, not merely an L¹ bound:
the exact narrow window allows at most 1/500 of the original
L²-mass scale to be paid as squared L¹ norm. -/
theorem neutralIV017NarrowL1_sq_le
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ, x ∉ neutralIV017NarrowPhysicalInterval → t x = 0) :
    ‖t.toLp 1 volume‖^2 ≤ neutralNF600Mass t / 500 := by
  have h := neutralIV017NarrowL1_bound t ht
  have hm : 0 ≤ neutralNF600Mass t := by
    unfold neutralNF600Mass
    positivity
  have hsq := pow_le_pow_left₀ (norm_nonneg _) h 2
  calc
    _ ≤ (Real.sqrt (neutralNF600Mass t) *
          Real.sqrt (1/500))^2 := hsq
    _ = _ := by
      rw [mul_pow,Real.sq_sqrt hm,Real.sq_sqrt (by norm_num)]
      ring

/-- Uniform pointwise spectral density bound, derived from the
actual (unitary) Schwartz Fourier transform and actual L¹ norm. -/
theorem neutralIV017Density_le_L1_sq
    (t : 𝓢(ℝ,ℂ)) (ξ : ℝ) :
    neutralNF600Density t ξ ≤ ‖t.toLp 1 volume‖^2 := by
  have h := SchwartzMap.norm_fourier_apply_le_toLp_one t ξ
  have hsq := pow_le_pow_left₀ (norm_nonneg _) h 2
  simpa only [neutralNF600Density] using hsq

/-- True low-band Fourier mass is at most ten times the original
physical squared L¹ norm, for arbitrary Schwartz input. -/
theorem neutralIV017LowMass_le_tenL1_sq
    (t : 𝓢(ℝ,ℂ)) :
    (∫ ξ in neutralNF600LowBand, neutralNF600Density t ξ) ≤
      10 * ‖t.toLp 1 volume‖^2 := by
  have hm : volume neutralNF600LowBand = 10 := by
    unfold neutralNF600LowBand
    rw [Real.volume_Ioo]
    norm_num
  have hi :
      IntegrableOn (fun _ : ℝ => ‖t.toLp 1 volume‖^2)
        neutralNF600LowBand :=
    integrableOn_const (by rw [hm]; norm_num)
  calc
    _ ≤ ∫ ξ in neutralNF600LowBand,
      ‖t.toLp 1 volume‖^2 :=
      setIntegral_mono_on
        (neutralNF600Density_integrable t).integrableOn
        hi measurableSet_Ioo
        (fun ξ _ => neutralIV017Density_le_L1_sq t ξ)
    _ = _ := by
      rw [setIntegral_const]
      simp [measureReal_def,hm]
      ring

/-- The genuinely narrow physical interval gives a 1/50 upper
bound on low-frequency spectral energy. This is a strict
improvement over NF600's original two-collar 1/25 upper bound. -/
theorem neutralIV017NarrowLowMass_le
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ, x ∉ neutralIV017NarrowPhysicalInterval → t x = 0) :
    (∫ ξ in neutralNF600LowBand, neutralNF600Density t ξ) ≤
      neutralNF600Mass t / 50 := by
  have hten := neutralIV017LowMass_le_tenL1_sq t
  have hphysical := neutralIV017NarrowL1_sq_le t ht
  linarith

/-- UNCONDITIONAL signed genuine Gamma-weight lower bound
for any complex Schwartz input: the exact low-band loss is
67/10 times the ACTUAL low-frequency Fourier mass. No
imaginary-axis zeros, prime or positivity of the Weil form
are assumed. -/
theorem neutralIV017SignedGamma_lower
    (t : 𝓢(ℝ,ℂ)) :
    (11/10:ℝ) * neutralNF600Mass t -
      (67/10:ℝ) *
        (∫ ξ in neutralNF600LowBand, neutralNF600Density t ξ) ≤
      neutralNF600Arch t := by
  let L := neutralNF600LowBand
  let ρ := neutralNF600Density t
  let w := fun ξ : ℝ =>
    Zeta23.EF.gammaBracket (-2*Real.pi*ξ) * ρ ξ
  have hρ := neutralNF600Density_integrable t
  have hw := neutralNF600Arch_integrable t
  have hL : MeasurableSet L := measurableSet_Ioo
  have hlo :
      ∫ ξ in L, (-(28/5:ℝ)) * ρ ξ ≤ ∫ ξ in L, w ξ :=
    setIntegral_mono_on (hρ.const_mul _).integrableOn
      hw.integrableOn hL
      (fun ξ _ =>
        mul_le_mul_of_nonneg_right
          (neutralNF599GammaLower _).le (sq_nonneg _))
  have hhi :
      ∫ ξ in Lᶜ, (11/10:ℝ) * ρ ξ ≤ ∫ ξ in Lᶜ, w ξ :=
    setIntegral_mono_on (hρ.const_mul _).integrableOn
      hw.integrableOn hL.compl
      (fun ξ hξ =>
        mul_le_mul_of_nonneg_right
          (neutralNF599GammaHigh _
            (neutralNF600HighFrequency ξ hξ)).le (sq_nonneg _))
  rw [integral_const_mul] at hlo hhi
  have hm := integral_add_compl hL hρ
  have ha := integral_add_compl hL hw
  change (∫ ξ in L, ρ ξ) +
    (∫ ξ in Lᶜ, ρ ξ) = ∫ ξ, ρ ξ at hm
  rw [neutralNF600Density_mass] at hm
  change (∫ ξ in L, w ξ) +
    (∫ ξ in Lᶜ, w ξ) = ∫ ξ, w ξ at ha
  unfold neutralNF600Arch
  linarith only [hlo,hhi,hm,ha]

/-- Quantitative SIGNED Gamma lower bound from the true width 1/500.
This does not yet include the true pole moments; it is the main
positive contribution needed to sign the new physical diagonal. -/
theorem neutralIV017NarrowGamma_coercive
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ, x ∉ neutralIV017NarrowPhysicalInterval → t x = 0) :
    (483/500:ℝ) * neutralNF600Mass t ≤ neutralNF600Arch t := by
  have hgamma := neutralIV017SignedGamma_lower t
  have hlow := neutralIV017NarrowLowMass_le t ht
  linarith only [hgamma,hlow]

#print axioms neutralNF599GammaLower
#print axioms neutralNF599GammaHigh
#print axioms neutralNF600Density_mass
#print axioms neutralNF600Arch_integrable
#print axioms neutralIV017NarrowPhysicalInterval_volume
#print axioms neutralIV017Narrow_support_from_bump
#print axioms neutralIV017NarrowL1_bound
#print axioms neutralIV017NarrowL1_sq_le
#print axioms neutralIV017Density_le_L1_sq
#print axioms neutralIV017LowMass_le_tenL1_sq
#print axioms neutralIV017NarrowLowMass_le
#print axioms neutralIV017SignedGamma_lower
#print axioms neutralIV017NarrowGamma_coercive

end
end WeilDefect
