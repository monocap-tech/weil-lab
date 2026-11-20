import WeilDefect.Arithmetic.ActualZetaOriginalRealOddSchwartzFullSource
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
IV005, part 1: the exact complex conjugate-reflection involution on
Schwartz tests, their compact windows, and the ORIGINAL raw/window
Fourier convention. No zeta zero-counting, oddness, reality, positivity,
or change to any frozen Phase III object.

The conjugate reflection is s†(x) = conj(s(-x)); its Fourier transform
obeys F[s†](z) = conj(F[s](conj z)), for *every complex* frequency z.
-/

/-- The involution of arbitrary COMPLEX Schwartz tests. Domain negation
is an R-linear continuous equivalence and output conjugation is an
R-linear continuous equivalence, so no false complex-linearity claim is
introduced by the construction. -/
def neutralIV005ConjugateReflection (s : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  ((SchwartzMap.compCLMOfContinuousLinearEquiv ℝ
    (ContinuousLinearEquiv.neg ℝ)) s).postcompCLM
      (Complex.conjCLE.toContinuousLinearMap)

theorem neutralIV005ConjugateReflection_apply
    (s : 𝓢(ℝ,ℂ)) (x : ℝ) :
    neutralIV005ConjugateReflection s x = conj (s (-x)) := by
  rfl

/-- Arbitrary-window compact support is preserved under the actual
anti-linear reflection. We deliberately do not require a > 0. -/
theorem neutralIV005ConjugateReflection_supported
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    ∀ x : ℝ, x ∉ Set.Icc (-a) a →
      neutralIV005ConjugateReflection s x = 0 := by
  intro x hx
  have hn : -x ∉ Set.Icc (-a) a := by
    intro h
    apply hx
    exact ⟨by linarith [h.2], by linarith [h.1]⟩
  rw [neutralIV005ConjugateReflection_apply, hs (-x) hn]
  simp

/-- Windowing a Schwartz test supported in [-a,a] does NOT change
its physical L² representative. Generalizes the older E-only lemma. -/
theorem neutralIV005WindowSchwartz_ae
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    neutralWindowRepresentative a (s.toLp 2 volume) =ᵐ[volume]
      (fun x => s x) := by
  filter_upwards [s.coeFn_toLp 2 volume] with x hx
  by_cases hw : x ∈ Set.Icc (-a) a
  · simp [neutralWindowRepresentative, hw, hx]
  · have hz : s x = 0 := hs x hw
    simp [neutralWindowRepresentative, hw, hx, hz]

/-- The raw transform symmetry is a direct measure-preserving change
of variables, NOT an oddness identity. It holds for any complex input
function as an equality of Bochner integrals. -/
theorem neutralIV005RawTransform_reflected (ψ : ℝ → ℂ) (z : ℂ) :
    neutralRawTransform (fun x => conj (ψ (-x))) z =
      conj (neutralRawTransform ψ (conj z)) := by
  let F : ℝ → ℂ := fun x =>
    conj (ψ (-x)) * Complex.exp (Complex.I * z * (x : ℂ))
  have hemb : MeasurableEmbedding (fun x : ℝ => -x) :=
    (Homeomorph.neg ℝ).isClosedEmbedding.measurableEmbedding
  have hchange := hemb.integral_map (μ := (volume : Measure ℝ)) F
  rw [Measure.map_neg_eq_self (volume : Measure ℝ)] at hchange
  change (∫ x : ℝ, F x) = _ at hchange
  calc
    neutralRawTransform (fun x => conj (ψ (-x))) z =
        ∫ x : ℝ, F x := rfl
    _ = ∫ x : ℝ, F (-x) := hchange
    _ = conj (neutralRawTransform ψ (conj z)) := by
      rw [neutralRawTransform, ← integral_conj]
      apply integral_congr_ae
      filter_upwards [] with x
      have hphase : Complex.I * z * (((-x : ℝ) : ℂ)) =
          conj (Complex.I * conj z * (x : ℂ)) := by
        simp only [Complex.ofReal_neg, map_mul, Complex.conj_I,
          Complex.conj_ofReal]
        ring
      change conj (ψ x) * Complex.exp (Complex.I * z * (((-x : ℝ) : ℂ))) =
        conj (ψ x * Complex.exp (Complex.I * conj z * (x : ℂ)))
      rw [hphase, Complex.exp_conj, map_mul]

/-- Exact authentic window transform reflection for any compactly
supported complex Schwartz test (no real-valued/odd test hypothesis). -/
theorem neutralIV005WindowEvaluation_reflected
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (z : ℂ) :
    neutralWindowEvaluation a z
        ((neutralIV005ConjugateReflection s).toLp 2 volume) =
      conj (neutralWindowEvaluation a (conj z) (s.toLp 2 volume)) := by
  have hR := neutralIV005WindowSchwartz_ae a
    (neutralIV005ConjugateReflection s)
    (neutralIV005ConjugateReflection_supported a s hs)
  have hS := neutralIV005WindowSchwartz_ae a s hs
  rw [neutralNF573WindowEvaluation_eq_raw_of_ae a _ _ hR,
      neutralNF573WindowEvaluation_eq_raw_of_ae a _ _ hS]
  change neutralRawTransform (fun x => conj (s (-x))) z =
    conj (neutralRawTransform (fun x => s x) (conj z))
  exact neutralIV005RawTransform_reflected (fun x => s x) z

#print axioms neutralIV005ConjugateReflection_apply
#print axioms neutralIV005ConjugateReflection_supported
#print axioms neutralIV005WindowSchwartz_ae
#print axioms neutralIV005RawTransform_reflected
#print axioms neutralIV005WindowEvaluation_reflected

end
end WeilDefect
