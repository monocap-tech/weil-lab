import WeilDefect.Arithmetic.ActualZetaOriginalJ242RealPhysicalMoments
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
