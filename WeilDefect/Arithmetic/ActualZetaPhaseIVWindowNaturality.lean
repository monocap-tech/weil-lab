import WeilDefect.Arithmetic.ActualZetaOriginalRealOddSchwartzFullSource
import WeilDefect.Arithmetic.ActualZetaSmoothCorrelationRegularity
import Mathlib.Analysis.Convolution

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate Convolution

/-!
Canonical NF741 / Phase IV:
Exact naturality of the original *literal* zeta Weil correlation and
explicit-formula functional under enlargement of a window that already
contains the physical supports of TWO arbitrary COMPLEX Schwartz tests.

No real/odd symmetry, no new off-diagonal zeta estimate, no replacement
Weil form, no Phase-III numerical inputs, no global positivity or RH.

This source intentionally uses only previously existing NF573/NF534
source theorems. It does not import the unverified IV003–IV005 modules.
-/

/-- An arbitrary complex Schwartz test supported in a closed physical
window has exactly its own almost-everywhere physical representative
inside that window. This generalizes the E-only NF573 lemma. -/
theorem neutralNF741Schwartz_window_ae
    (a : ℝ) (s : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    neutralWindowRepresentative a (s.toLp 2 volume)
      =ᵐ[volume] (fun x : ℝ => s x) := by
  filter_upwards [s.coeFn_toLp 2 volume] with x hx
  by_cases hw : x ∈ Set.Icc (-a) a
  · simp [neutralWindowRepresentative, hw, hx]
  · simp [neutralWindowRepresentative, hw, hx, hs x hw]

/-- Literal compact-window support inclusion needs no positivity
or sign premise; the narrower interval embeds in the wider one. -/
theorem neutralNF741Schwartz_support_expand
    (a b : ℝ) (hab : a ≤ b) (s : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    ∀ x : ℝ, x ∉ Set.Icc (-b) b → s x = 0 := by
  intro x hx
  apply hs x
  intro hx'
  apply hx
  exact ⟨by linarith [hx'.1], by linarith [hx'.2]⟩

/-- The original positive-exponent complex-frequency sample is exactly
window-independent once the support fits inside both windows. This is
a source-specific statement for the ACTUAL neutralWindowEvaluation. -/
theorem neutralNF741WindowEvaluation_eq_of_support
    (a b : ℝ) (s : 𝓢(ℝ, ℂ))
    (hsa : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (hsb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → s x = 0)
    (z : ℂ) :
    neutralWindowEvaluation a z (s.toLp 2 volume) =
      neutralWindowEvaluation b z (s.toLp 2 volume) := by
  rw [neutralNF573WindowEvaluation_eq_raw_of_ae a _ _
        (neutralNF741Schwartz_window_ae a s hsa),
      neutralNF573WindowEvaluation_eq_raw_of_ae b _ _
        (neutralNF741Schwartz_window_ae b s hsb)]

/-- Conjugate reflection preserves almost-everywhere coincidence of
actual window representatives: negative reflection does not lose null
sets because Lebesgue measure is preserved by x ↦ -x. -/
theorem neutralNF741WindowReflection_ae
    (a b : ℝ) (f : RealComplexL2)
    (hf : neutralWindowRepresentative a f =ᵐ[volume]
      neutralWindowRepresentative b f) :
    (fun x : ℝ => conj (neutralWindowRepresentative a f (-x))) =ᵐ[volume]
      (fun x : ℝ => conj (neutralWindowRepresentative b f (-x))) := by
  have hm :
      neutralWindowRepresentative a f
        =ᵐ[(volume : Measure ℝ).map (fun x : ℝ => -x)]
      neutralWindowRepresentative b f := by
    rw [Measure.map_neg_eq_self (volume : Measure ℝ)]
    exact hf
  have hn := MeasureTheory.ae_of_ae_map
    (f := fun x : ℝ => -x) (μ := (volume : Measure ℝ))
    measurable_neg.aemeasurable hm
  filter_upwards [hn] with x hx
  exact congrArg conj hx

/-- ACTUAL two-argument window correlation is unchanged when two
complex Schwartz tests both fit into either physical window. This is
an equality of the full complex-valued correlation FUNCTIONS. -/
theorem neutralNF741WindowCorrelation_eq_of_support
    (a b : ℝ) (s t : 𝓢(ℝ, ℂ))
    (hsa : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (hsb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → s x = 0)
    (hta : ∀ x : ℝ, x ∉ Set.Icc (-a) a → t x = 0)
    (htb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0) :
    neutralWindowCorrelation a (s.toLp 2 volume) (t.toLp 2 volume) =
      neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume) := by
  have hs :
      neutralWindowRepresentative a (s.toLp 2 volume) =ᵐ[volume]
      neutralWindowRepresentative b (s.toLp 2 volume) :=
    (neutralNF741Schwartz_window_ae a s hsa).trans
      (neutralNF741Schwartz_window_ae b s hsb).symm
  have ht :
      neutralWindowRepresentative a (t.toLp 2 volume) =ᵐ[volume]
      neutralWindowRepresentative b (t.toLp 2 volume) :=
    (neutralNF741Schwartz_window_ae a t hta).trans
      (neutralNF741Schwartz_window_ae b t htb).symm
  have hsn := neutralNF741WindowReflection_ae a b (s.toLp 2 volume) hs
  rw [neutralWindowCorrelation_eq_realBilinearConvolution,
      neutralWindowCorrelation_eq_realBilinearConvolution]
  exact convolution_congr (ContinuousLinearMap.mul ℝ ℂ) ht hsn

/-- The true original zeta explicit-formula RIGHT-HAND SIDE, including
prime, archimedean, and pole terms, is unchanged when the literal
two-argument correlation is unchanged. Nothing is approximated. -/
theorem neutralNF741LiteralMixedEF_eq_of_support
    (a b : ℝ) (s t : 𝓢(ℝ, ℂ))
    (hsa : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (hsb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → s x = 0)
    (hta : ∀ x : ℝ, x ∉ Set.Icc (-a) a → t x = 0)
    (htb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0) :
    Zeta23.EF.literatureRHS
        (neutralWindowCorrelation a
          (s.toLp 2 volume) (t.toLp 2 volume)) =
      Zeta23.EF.literatureRHS
        (neutralWindowCorrelation b
          (s.toLp 2 volume) (t.toLp 2 volume)) := by
  rw [neutralNF741WindowCorrelation_eq_of_support a b s t hsa hsb hta htb]

/-- Source-specific, full-multiplicity mixed ZERO-SIDE series is
window-independent as well: pointwise exact original samples agree for
every original actual divisor copy. No convergence assumption is
needed for equality of the two tsum values (although the existing
NF533 theorem gives convergence for the supported smooth inputs). -/
theorem neutralNF741MixedDivisorSum_eq_of_support
    (a b : ℝ) (s t : 𝓢(ℝ, ℂ))
    (hsa : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (hsb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → s x = 0)
    (hta : ∀ x : ℝ, x ∉ Set.Icc (-a) a → t x = 0)
    (htb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q))
        (s.toLp 2 volume)) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (t.toLp 2 volume)) =
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralWindowEvaluation b
        (conj (neutralActualZetaDivisorOrdinate q))
        (s.toLp 2 volume)) *
        neutralWindowEvaluation b (neutralActualZetaDivisorOrdinate q)
          (t.toLp 2 volume)) := by
  apply tsum_congr
  intro q
  rw [neutralNF741WindowEvaluation_eq_of_support a b s hsa hsb,
      neutralNF741WindowEvaluation_eq_of_support a b t hta htb]

/-- The useful variable-window specialization: arbitrary complex smooth
test supports inside [-a,a] may be carried into ANY larger [-b,b].
The complete literal mixed Weil EF, not just the zero side, is invariant. -/
theorem neutralNF741LiteralMixedEF_natural
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-a) a → t x = 0) :
    Zeta23.EF.literatureRHS
      (neutralWindowCorrelation a (s.toLp 2 volume) (t.toLp 2 volume)) =
    Zeta23.EF.literatureRHS
      (neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)) := by
  exact neutralNF741LiteralMixedEF_eq_of_support a b s t hs
    (neutralNF741Schwartz_support_expand a b hab s hs) ht
    (neutralNF741Schwartz_support_expand a b hab t ht)

/-- Diagonal signed Weil arithmetic value inherits the same naturality.
It is NOT a positivity theorem and does not change the frozen collar. -/
theorem neutralNF741LiteralDiagonalWeil_natural
    (a b : ℝ) (hab : a ≤ b)
    (s : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    (Zeta23.EF.literatureRHS
      (neutralWindowCorrelation a (s.toLp 2 volume) (s.toLp 2 volume))).re =
    (Zeta23.EF.literatureRHS
      (neutralWindowCorrelation b (s.toLp 2 volume) (s.toLp 2 volume))).re := by
  exact congrArg Complex.re
    (neutralNF741LiteralMixedEF_natural a b hab s s hs hs)

#print axioms neutralNF573WindowEvaluation_eq_raw_of_ae
#print axioms neutralWindowCorrelation_eq_realBilinearConvolution
#print axioms neutralActualZetaWindowCorrelation_literature_of_contDiff
#print axioms neutralNF741Schwartz_window_ae
#print axioms neutralNF741Schwartz_support_expand
#print axioms neutralNF741WindowEvaluation_eq_of_support
#print axioms neutralNF741WindowReflection_ae
#print axioms neutralNF741WindowCorrelation_eq_of_support
#print axioms neutralNF741LiteralMixedEF_eq_of_support
#print axioms neutralNF741MixedDivisorSum_eq_of_support
#print axioms neutralNF741LiteralMixedEF_natural
#print axioms neutralNF741LiteralDiagonalWeil_natural

end
end WeilDefect
