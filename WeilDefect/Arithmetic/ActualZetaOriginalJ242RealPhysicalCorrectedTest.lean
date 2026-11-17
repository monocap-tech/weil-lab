import WeilDefect.Arithmetic.ActualZetaOriginalJ242CanonicalCorrectionReality
import WeilDefect.Arithmetic.ActualZetaOriginalJ242OddParity

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
NF572 — reality of the ORIGINAL physical target moments and
the actual NF543 corrected test. No pointwise representative
of an arbitrary L² equivalence class is assumed canonical.
Reality of the target is an almost-everywhere hypothesis.
Strict positivity is explicitly retained in the conditional
corrected-test theorem.
-/

/-- Extend the exact NF549 Schwartz moment integral to the
genuine arbitrary physical L² target. This is an a.e. L²
identity, not a pointwise equality of equivalence classes. -/
theorem neutralNF572OriginalMoment_eq_physicalIntegral
    (ell : RealComplexL2) (i : Fin 242) :
    neutralNF546OriginalSelectedMoments ell i =
      ∫ x : ℝ, conj (neutralNF546OriginalWindowGenerator i x) *
        ell x ∂volume := by
  change inner ℂ (neutralNF546OriginalSelectedPhysicalL2 i) ell = _
  rw [MeasureTheory.L2.inner_def]
  apply integral_congr_ae
  filter_upwards [neutralNF546OriginalSelectedPhysicalL2_ae i] with x hi
  simp only [hi, RCLike.inner_apply, mul_comm]

/-- Actual real physical L² targets have real original J242
moments. The source window and its original sinh generator
remain unchanged. -/
theorem neutralNF572OriginalRealPhysicalMoments
    (ell : RealComplexL2)
    (hell : ∀ᵐ x ∂volume, conj (ell x) = ell x)
    (i : Fin 242) :
    conj (neutralNF546OriginalSelectedMoments ell i) =
      neutralNF546OriginalSelectedMoments ell i := by
  rw [neutralNF572OriginalMoment_eq_physicalIntegral, ← integral_conj]
  apply integral_congr_ae
  filter_upwards [hell] with x hx
  simp only [map_mul, neutralNF571OriginalWindowGenerator_conj, hx]

/-- Pointwise reality of a smooth test gives real moments,
using its actual a.e. physical representative. -/
theorem neutralNF572OriginalRealSchwartzMoments
    (g : 𝓢(ℝ, ℂ)) (hg : ∀ x : ℝ, conj (g x) = g x)
    (i : Fin 242) :
    conj (neutralNF546OriginalSelectedMoments (g.toLp 2 volume) i) =
      neutralNF546OriginalSelectedMoments (g.toLp 2 volume) i := by
  apply neutralNF572OriginalRealPhysicalMoments
  filter_upwards [g.coeFn_toLp 2 volume] with x hx
  rw [hx, hg x]

/-- The literal NF543 target-minus-test moment defect is real.
This does not require a Gram inverse. -/
theorem neutralNF572OriginalMomentDefect_real
    (ell : RealComplexL2)
    (hell : ∀ᵐ x ∂volume, conj (ell x) = ell x)
    (g : 𝓢(ℝ, ℂ)) (hg : ∀ x : ℝ, conj (g x) = g x)
    (i : Fin 242) :
    conj ((neutralNF546OriginalSelectedMoments ell -
      neutralNF546OriginalSelectedMoments (g.toLp 2 volume)) i) =
    (neutralNF546OriginalSelectedMoments ell -
      neutralNF546OriginalSelectedMoments (g.toLp 2 volume)) i := by
  simp only [Pi.sub_apply, map_sub,
    neutralNF572OriginalRealPhysicalMoments ell hell i,
    neutralNF572OriginalRealSchwartzMoments g hg i]

/-- For an a.e.-real physical target and pointwise-real odd
Schwartz approximation with original collar support, the
unchanged canonical corrected test is simultaneously real,
odd, supported in the same collars, and exactly moment matched.
It is admitted to the authentic original logarithmic carrier.
Only the original finite Gram positivity remains explicit. -/
theorem neutralNF572OriginalCorrectedTest_realOddSupported
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (ell : RealComplexL2)
    (hell : ∀ᵐ x ∂volume, conj (ell x) = ell x)
    (g : 𝓢(ℝ, ℂ))
    (hreal : ∀ x : ℝ, conj (g x) = g x)
    (hodd : ∀ x : ℝ, g (-x) = -g x)
    (hsupp : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0) :
    let f := neutralNF543Correct neutralNF546OriginalSelectedMoments
      (neutralNF548CanonicalRightInverse hpos) ell g
    (∀ x : ℝ, conj (f x) = f x) ∧
    (∀ x : ℝ, f (-x) = -f x) ∧
    (∀ x : ℝ, x ∉ neutralNF543OriginalCollars → f x = 0) ∧
    neutralNF546OriginalSelectedMoments (f.toLp 2 volume) =
      neutralNF546OriginalSelectedMoments ell ∧
    (∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val = f.toLp 2 volume) := by
  let R := neutralNF548CanonicalRightInverse hpos
  let d := neutralNF546OriginalSelectedMoments ell -
    neutralNF546OriginalSelectedMoments (g.toLp 2 volume)
  let f := neutralNF543Correct neutralNF546OriginalSelectedMoments R ell g
  have hf (x : ℝ) : f x = g x + (R d) x := by
    simp [f, d, neutralNF543Correct]
  change (∀ x : ℝ, conj (f x) = f x) ∧
    (∀ x : ℝ, f (-x) = -f x) ∧
    (∀ x : ℝ, x ∉ neutralNF543OriginalCollars → f x = 0) ∧
    neutralNF546OriginalSelectedMoments (f.toLp 2 volume) =
      neutralNF546OriginalSelectedMoments ell ∧
    (∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val = f.toLp 2 volume)
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro x
    rw [hf, map_add, hreal x]
    have hd : ∀ i, conj (d i) = d i :=
      neutralNF572OriginalMomentDefect_real ell hell g hreal
    rw [show conj ((R d) x) = (R d) x from
      neutralNF571CanonicalRightInverse_realData hpos d hd x]
  · intro x
    rw [hf, hf, hodd x]
    rw [show (R d) (-x) = -(R d) x from
      neutralNF551CanonicalRightInverse_odd hpos d x]
    ring
  · exact neutralNF543Correct_supported _ R ell g hsupp
      (neutralNF548CanonicalRightInverse_supported hpos)
  · exact neutralNF543Correct_moments _ R
      (neutralNF548CanonicalRightInverse_correct hpos) ell g
  · obtain ⟨k, hk, _⟩ :=
      neutralNF548OriginalMomentMatchedLogCarrier hpos ell g hsupp
    exact ⟨k, hk⟩

end
end WeilDefect
