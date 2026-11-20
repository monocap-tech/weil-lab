import WeilDefect.Arithmetic.ActualZetaPhaseIVComplexReflection
import WeilDefect.Arithmetic.ActualZetaRawSamplesToFullSourceGraph
import WeilDefect.Arithmetic.ActualZetaLogCarrierSchwartzCompact
import WeilDefect.Arithmetic.ActualZetaSmoothCorrelationRegularity
import WeilDefect.Arithmetic.ActualZetaWeilZeroForm

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
IV005, part 2: **arbitrary complex Schwartz** full actual-zeta divisor
source-graph entry, removing the real-odd hypothesis of NF573.

Key retyping: the REAL-ODD self-correlation trick from NF536 is
unnecessary. For arbitrary complex s, take the mixed correlation of
its conjugate reflection s† with s. Its actual divisor summand is
F_s(z)^2, whose absolute value is |F_s(z)|². The already-accepted
literal zeta explicit formula supplies ABSOLUTE convergence at all
authentic divisor coordinates with multiplicities. The exact divisor
partner equivalence supplies the second raw family. No zeta zero count,
RH, positivity, Green synthesis, or coefficient-box assumptions.

The full source lift uses the existing original physical log Hilbert
carrier and the actual P/N ℓ² source graph, preserving the same
physical vector, not a replacement test.
-/

/-- Literal C² mixed correlation for Schwartz s† and s, using only the
original accepted convolution regularity from the second smooth input. -/
theorem neutralIV005ReflectedMixedCorrelation_C2
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    ContDiff ℝ 2
      (neutralWindowCorrelation a
        ((neutralIV005ConjugateReflection s).toLp 2 volume)
        (s.toLp 2 volume)) := by
  have hc : HasCompactSupport (fun x : ℝ => s x) := by
    apply HasCompactSupport.intro (K := Set.Icc (-a) a) isCompact_Icc
    intro x hx
    exact hs x hx
  exact neutralWindowCorrelation_contDiff_of_ae_smoothSecond a
    ((neutralIV005ConjugateReflection s).toLp 2 volume)
    (s.toLp 2 volume) (fun x => s x)
    (s.smooth 2) hc (neutralIV005WindowSchwartz_ae a s hs)

/-- Main quantitative step: arbitrary COMPLEX compact Schwartz tests
have ℓ² original zeta zero samples, with all multiplicities. We derive
this from the absolute mixed *actual* explicit formula, avoiding a new
uniform zeta zero-count theorem and real-odd symmetry. -/
theorem neutralIV005ComplexWindowSample_sq_summable
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (s.toLp 2 volume)‖^2) := by
  let t := neutralIV005ConjugateReflection s
  have hreg : ContDiff ℝ 2
      (neutralWindowCorrelation a (t.toLp 2 volume) (s.toLp 2 volume)) :=
    neutralIV005ReflectedMixedCorrelation_C2 a s hs
  have hsum : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) (t.toLp 2 volume)) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (s.toLp 2 volume)) := by
    convert neutralActualZetaDivisor_rawTransform_summable_of_contDiff
      (neutralWindowCorrelation a (t.toLp 2 volume) (s.toLp 2 volume))
      hreg (neutralWindowCorrelation_hasCompactSupport a
        (t.toLp 2 volume) (s.toLp 2 volume)) using 1
    funext q
    exact (neutralWindowCorrelation_rawTransform a
      (t.toLp 2 volume) (s.toLp 2 volume)
      (neutralActualZetaDivisorOrdinate q)).symm
  apply hsum.norm.congr
  intro q
  have hm :
      neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q))
        (t.toLp 2 volume) =
      conj (neutralWindowEvaluation a
        (neutralActualZetaDivisorOrdinate q) (s.toLp 2 volume)) := by
    simpa [t] using neutralIV005WindowEvaluation_reflected a s hs
      (conj (neutralActualZetaDivisorOrdinate q))
  rw [norm_mul, Complex.norm_conj, hm, Complex.norm_conj]
  ring

/-- The complementary conjugate-ordinate family is automatically
ℓ² by the true zeta divisor conjugate-partner equivalence.
No real-odd law is used, and every multiplicity copy is retained. -/
theorem neutralIV005ComplexPartnerSample_sq_summable
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q))
        (s.toLp 2 volume)‖^2) := by
  have h := (neutralActualZetaDivisorPairEquiv.summable_iff.mpr
    (neutralIV005ComplexWindowSample_sq_summable a s hs))
  change Summable (fun q : NeutralActualZetaDivisorCoordinate =>
    ‖neutralWindowEvaluation a
      (neutralActualZetaDivisorOrdinate
        (neutralActualZetaDivisorPair q)) (s.toLp 2 volume)‖^2) at h
  simpa only [neutralActualZetaDivisorOrdinate_pair] using h

/-- The decisive arbitrary-complex source lift. Every Schwartz s
supported in the given finite physical window enters the original
complete zeta source graph with *exactly* its own physical L² class.
No reality, oddness, or finite generator source is required. -/
theorem neutralIV005ComplexSchwartz_fullSource
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    ∃ v : NeutralActualZetaSourceDomain a,
      neutralLogPhysical
        (neutralActualZetaSourcePhysical a v).val =
          s.toLp 2 volume := by
  have hsupport : ∀ᵐ x ∂volume,
      x ∉ Set.Icc (-a) a → (s.toLp 2 volume) x = 0 := by
    filter_upwards [s.coeFn_toLp 2 volume] with x hx hout
    rw [hx]
    exact hs x hout
  obtain ⟨k, hk⟩ :=
    neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
      a (s.toLp 2 volume) hsupport
      (neutralSchwartzPhysical_quadraticFourierMoment s)
  have hA : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q))
          (neutralLogPhysical k.val)‖^2) := by
    simpa only [hk] using neutralIV005ComplexPartnerSample_sq_summable a s hs
  have hB : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a
        (neutralActualZetaDivisorOrdinate q)
          (neutralLogPhysical k.val)‖^2) := by
    simpa only [hk] using neutralIV005ComplexWindowSample_sq_summable a s hs
  refine ⟨neutralActualZetaFullSourceLiftOfRawSamples a k hA hB, ?_⟩
  change neutralLogPhysical
    (neutralActualZetaSourcePhysical a
      (neutralActualZetaFullSourceLiftOfRawSamples a k hA hB)).val =
        s.toLp 2 volume
  rw [neutralActualZetaFullSourceLiftOfRawSamples_physical, hk]

/-- User-facing compact C∞ formulation. All complex compact smooth
tests supported in [-a,a] now have an original zeta source lift.
No 'real' or 'odd' restriction survives in the theorem statement. -/
theorem neutralIV005CompactComplexSmooth_fullSource
    (a : ℝ) (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ ∞ ψ)
    (hc : HasCompactSupport ψ)
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → ψ x = 0) :
    ∃ v : NeutralActualZetaSourceDomain a,
      neutralLogPhysical
        (neutralActualZetaSourcePhysical a v).val =
          (hc.toSchwartzMap hψ).toLp 2 volume := by
  apply neutralIV005ComplexSchwartz_fullSource a (hc.toSchwartzMap hψ)
  intro x hx
  exact hs x hx

#print axioms neutralIV005ReflectedMixedCorrelation_C2
#print axioms neutralIV005ComplexWindowSample_sq_summable
#print axioms neutralIV005ComplexPartnerSample_sq_summable
#print axioms neutralIV005ComplexSchwartz_fullSource
#print axioms neutralIV005CompactComplexSmooth_fullSource

end
end WeilDefect
