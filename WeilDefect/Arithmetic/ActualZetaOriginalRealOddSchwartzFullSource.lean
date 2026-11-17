import WeilDefect.Arithmetic.ActualZetaRawSamplesToFullSourceGraph
import WeilDefect.Arithmetic.ActualZetaOriginalCollar242Correction
import WeilDefect.Arithmetic.ActualZetaSmoothCorrelationRegularity
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate ContDiff

/-!
NF573: real odd compact Schwartz tests enter the actual full divisor
source graph. The reflection identity is for the literal positive-
exponent window transform, not a critical-line assumption. Absolute
convergence of the C² autocorrelation gives both complete ℓ² vectors
through NF537. No uniform approximation or source density is inferred.
-/

/-- Real odd tests obey the genuine off-real-axis sample reflection
law, at every complex frequency, prior to taking the divisor. -/
theorem neutralNF573RawTransform_realOdd_conj
    (psi : ℝ → ℂ) (hreal : ∀ x, conj (psi x) = psi x)
    (hodd : ∀ x, psi (-x) = -psi x) (z : ℂ) :
    neutralRawTransform psi (conj z) =
      -conj (neutralRawTransform psi z) := by
  let F : ℝ → ℂ := fun x =>
    psi x * Complex.exp (Complex.I * conj z * (x : ℂ))
  have hemb : MeasurableEmbedding (fun x : ℝ => -x) :=
    (Homeomorph.neg ℝ).isClosedEmbedding.measurableEmbedding
  have hchange := hemb.integral_map (μ := (volume : Measure ℝ)) F
  rw [Measure.map_neg_eq_self (volume : Measure ℝ)] at hchange
  change (∫ x : ℝ, F x) = _
    at hchange
  calc
    neutralRawTransform psi (conj z) = ∫ x : ℝ,
        psi (-x) * Complex.exp (Complex.I * conj z * ((-x : ℝ) : ℂ)) := hchange
    _ = -conj (neutralRawTransform psi z) := by
      rw [neutralRawTransform, ← integral_conj, ← integral_neg]
      apply integral_congr_ae
      filter_upwards [] with x
      have hphase :
          Complex.I * conj z * ((-x : ℝ) : ℂ) =
            conj (Complex.I * z * (x : ℂ)) := by
        simp only [Complex.ofReal_neg, map_mul, Complex.conj_I,
          Complex.conj_ofReal]
        ring
      rw [hodd x, hphase, Complex.exp_conj, map_mul, hreal x]
      ring

/-- The actual full-window Fourier observation equals the raw
transform of any a.e. identical representative. -/
theorem neutralNF573WindowEvaluation_eq_raw_of_ae
    (a : ℝ) (f : RealComplexL2) (psi : ℝ → ℂ)
    (hpsi : neutralWindowRepresentative a f =ᵐ[volume] psi)
    (z : ℂ) :
    neutralWindowEvaluation a z f = neutralRawTransform psi z := by
  unfold neutralWindowEvaluation neutralRawTransform
  rw [← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [hpsi] with x hx
  by_cases hw : x ∈ Set.Icc (-a) a
  · simpa [neutralWindowRepresentative, hw] using
      congrArg (fun v : ℂ => v * Complex.exp
        (Complex.I * z * (x : ℂ))) hx
  · simpa [neutralWindowRepresentative, hw] using
      congrArg (fun v : ℂ => v * Complex.exp
        (Complex.I * z * (x : ℂ))) hx

/-- The actual physical window of a supported Schwartz input
agrees a.e. with the exact same smooth test. -/
theorem neutralNF573OriginalCollar_window_ae
    (s : 𝓢(ℝ, ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    neutralWindowRepresentative (11 / 10 : ℝ) (s.toLp 2 volume)
      =ᵐ[volume] (fun x => s x) := by
  filter_upwards [s.coeFn_toLp 2 volume,
    neutralNF543OriginalCollarSchwartz_supported s hs] with x hx hzero
  by_cases hw : x ∈ Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ)
  · simp [neutralWindowRepresentative, hw, hx]
  · have hz : s x = 0 := hx ▸ hzero hw
    simp [neutralWindowRepresentative, hw, hz]

/-- A single originally supported real odd Schwartz test has an
actual full-divisor graph lift with EXACT physical realization.
All multiplicity copies and both P/N vectors are retained. -/
theorem neutralNF573OriginalRealOddSchwartz_fullSource
    (s : 𝓢(ℝ, ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (hr : ∀ x, conj (s x) = s x)
    (ho : ∀ x, s (-x) = -s x) :
    ∃ v : NeutralActualZetaSourceDomain (11 / 10 : ℝ),
      neutralLogPhysical
        (neutralActualZetaSourcePhysical (11 / 10 : ℝ) v).val =
          s.toLp 2 volume := by
  let B : ℝ := 11 / 10
  obtain ⟨k, hk⟩ :=
    neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
      B (s.toLp 2 volume)
      (neutralNF543OriginalCollarSchwartz_supported s hs)
      (neutralSchwartzPhysical_quadraticFourierMoment s)
  have hae : neutralWindowRepresentative B (neutralLogPhysical k.val)
      =ᵐ[volume] (fun x => s x) := by
    rw [hk]
    exact neutralNF573OriginalCollar_window_ae s hs
  have hc : HasCompactSupport (fun x : ℝ => s x) := by
    apply HasCompactSupport.intro (K := Set.Icc (-B) B) isCompact_Icc
    intro x hx
    apply hs x
    intro hE
    apply hx
    rcases hE with hl | hh
    · exact ⟨hl.1.le, by dsimp [B]; linarith [hl.2]⟩
    · exact ⟨by dsimp [B]; linarith [hh.1], hh.2.le⟩
  have hreg : ContDiff ℝ 2
      (neutralWindowCorrelation B (neutralLogPhysical k.val)
        (neutralLogPhysical k.val)) :=
    neutralWindowCorrelation_contDiff_of_ae_smoothSecond B
      (neutralLogPhysical k.val) (neutralLogPhysical k.val)
      (fun x => s x) (s.smooth.of_le (by norm_num)) hc hae
  have hsym : ∀ q : NeutralActualZetaDivisorCoordinate,
      neutralWindowEvaluation B (conj (neutralActualZetaDivisorOrdinate q))
          (neutralLogPhysical k.val) =
        -conj (neutralWindowEvaluation B (neutralActualZetaDivisorOrdinate q)
          (neutralLogPhysical k.val)) := by
    intro q
    rw [neutralNF573WindowEvaluation_eq_raw_of_ae B _ _ hae,
      neutralNF573WindowEvaluation_eq_raw_of_ae B _ _ hae]
    exact neutralNF573RawTransform_realOdd_conj (fun x => s x)
      hr ho (neutralActualZetaDivisorOrdinate q)
  refine ⟨neutralActualZetaRealOddSmoothLogFullSourceLift B k hreg hsym, ?_⟩
  rw [neutralActualZetaRealOddSmoothLogFullSourceLift_physical]
  exact hk

end
end WeilDefect
