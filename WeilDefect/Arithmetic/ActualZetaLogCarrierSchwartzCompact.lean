import WeilDefect.Arithmetic.ActualZetaLogCarrierQuadraticMoment
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform SchwartzMap

/-!
NF542: a direct, assumption-free smooth-compact carrier entry for the
genuinely original physical source, using Mathlib's Schwartz/L² Fourier
compatibility. This is intentionally independent of the missing
C²-to-L² derivative-compatibility theorem in NF541.
-/

/-- The same quadratic frequency moment is finite for a Schwartz
function. This uses its genuine Fourier decay, not an assumed
frequency-domain integrability premise. -/
theorem neutralSchwartz_quadraticFourierMoment
    (s : 𝓢(ℝ, ℂ)) :
    Integrable (fun ξ : ℝ =>
      (Real.exp 1 + 1 + ξ ^ 2) * ‖s ξ‖ ^ 2) volume := by
  have h0 : Integrable (fun ξ : ℝ => ‖s ξ‖ ^ 2) volume :=
    (memLp_two_iff_integrable_sq_norm
      s.continuous.aestronglyMeasurable).mp (s.memLp 2 volume)
  have h2 : Integrable (fun ξ : ℝ =>
      ‖ξ‖ ^ 2 * ‖s ξ‖) volume :=
    s.integrable_pow_mul volume 2
  let C : ℝ := (SchwartzMap.seminorm ℝ 0 0) s
  have hC (ξ : ℝ) : ‖s ξ‖ ≤ C := by
    simpa only [C] using SchwartzMap.norm_le_seminorm ℝ s ξ
  have hCpos : 0 ≤ C :=
    (norm_nonneg (s 0)).trans (hC 0)
  have hsq : Integrable (fun ξ : ℝ =>
      ξ ^ 2 * ‖s ξ‖ ^ 2) volume := by
    apply (h2.const_mul C).mono'
    · exact ((continuous_id.pow 2).mul
        (s.continuous.norm.pow 2)).aestronglyMeasurable
    · filter_upwards [] with ξ
      have hx : 0 ≤ ξ ^ 2 := sq_nonneg ξ
      have hn : 0 ≤ ‖s ξ‖ := norm_nonneg _
      have hbound :
          ξ ^ 2 * ‖s ξ‖ ^ 2 ≤ C * (‖ξ‖ ^ 2 * ‖s ξ‖) := by
        calc
          ξ ^ 2 * ‖s ξ‖ ^ 2 =
              (ξ ^ 2 * ‖s ξ‖) * ‖s ξ‖ := by ring
          _ ≤ (ξ ^ 2 * ‖s ξ‖) * C :=
            mul_le_mul_of_nonneg_left (hC ξ) (mul_nonneg hx hn)
          _ = C * (‖ξ‖ ^ 2 * ‖s ξ‖) := by
            rw [Real.norm_eq_abs, sq_abs]
            ring
      simpa only [Real.norm_eq_abs,
        abs_of_nonneg (mul_nonneg hx (sq_nonneg _)),
        abs_of_nonneg (mul_nonneg hCpos
          (mul_nonneg (sq_nonneg _) hn))] using hbound
  have hsum := (h0.const_mul (Real.exp 1 + 1)).add hsq
  have hident :
      (fun ξ : ℝ =>
        (Real.exp 1 + 1 + ξ ^ 2) * ‖s ξ‖ ^ 2) =
      (fun ξ : ℝ =>
        (Real.exp 1 + 1) * ‖s ξ‖ ^ 2 +
          ξ ^ 2 * ‖s ξ‖ ^ 2) := by
    funext ξ
    ring
  rw [hident]
  exact hsum

/-- A Schwartz physical input, mapped into the ACTUAL L² Fourier
transform, automatically has the authentic NF540 quadratic moment.
Crucially, Mathlib already proves exact Fourier compatibility here. -/
theorem neutralSchwartzPhysical_quadraticFourierMoment
    (f : 𝓢(ℝ, ℂ)) :
    Integrable (fun ξ : ℝ =>
      (Real.exp 1 + 1 + ξ ^ 2) *
        ‖(𝓕 (f.toLp 2 volume) : RealComplexL2) ξ‖ ^ 2) volume := by
  have h := neutralSchwartz_quadraticFourierMoment (𝓕 f : 𝓢(ℝ, ℂ))
  rw [SchwartzMap.toLp_fourier_eq f]
  apply h.congr
  filter_upwards [((𝓕 f : 𝓢(ℝ, ℂ)).coeFn_toLp 2 volume)] with ξ hξ
  rw [hξ]

/-- Any ORIGINAL physical compact C∞ test supported in [-a,a]
enters the genuine logarithmic Hilbert carrier with exactly its own
L² equivalence class. No assumed spectral moment, no Fourier
derivative witness and no Green construction. -/
theorem neutralCompactSmoothOriginalLogHilbertCarrier
    (a : ℝ) (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ ∞ ψ) (hc : HasCompactSupport ψ)
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → ψ x = 0) :
    ∃ k : NeutralLogHilbertCarrier a,
      neutralLogPhysical k.val =
        (hc.toSchwartzMap hψ).toLp 2 volume := by
  let s : 𝓢(ℝ, ℂ) := hc.toSchwartzMap hψ
  have hsupport : ∀ᵐ x ∂volume,
      x ∉ Set.Icc (-a) a → (s.toLp 2 volume) x = 0 := by
    filter_upwards [s.coeFn_toLp 2 volume] with x hx hout
    rw [hx]
    exact hs x hout
  exact neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
    a (s.toLp 2 volume) hsupport
      (neutralSchwartzPhysical_quadraticFourierMoment s)

/-- Direct admission for the EXACT original two endpoint collars
B=11/10 and δ=1/500. The compact C∞ test itself, rather than a
surrogate Green packet, is the physical Hilbert-vector representative. -/
theorem neutralOriginalTwoCollarCompactSmoothLogHilbertCarrier
    (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ ∞ ψ) (hc : HasCompactSupport ψ)
    (hs : ∀ x : ℝ,
      x ∉ (Set.Ioo (-(11 / 10 : ℝ)) (-(11 / 10 : ℝ) + 1 / 500) ∪
        Set.Ioo ((11 / 10 : ℝ) - 1 / 500) (11 / 10 : ℝ)) → ψ x = 0) :
    ∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val =
        (hc.toSchwartzMap hψ).toLp 2 volume := by
  apply neutralCompactSmoothOriginalLogHilbertCarrier
    (11 / 10 : ℝ) ψ hψ hc
  intro x hout
  apply hs x
  intro hE
  rcases hE with hleft | hright
  · exact hout ⟨hleft.1.le, by linarith [hleft.2]⟩
  · exact hout ⟨by linarith [hright.1], hright.2.le⟩

end
end WeilDefect
