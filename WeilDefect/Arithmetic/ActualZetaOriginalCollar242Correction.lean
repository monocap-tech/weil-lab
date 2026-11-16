import WeilDefect.Arithmetic.ActualZetaLogCarrierSchwartzCompact

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped SchwartzMap FourierTransform

/-!
NF543: finite-dimensional, source-exact 242-moment correction of a
genuine physical Schwartz collar test. All moments act on the ACTUAL
physical L² class; correction coefficients are computed from its
original L² moment defect. No Green span or divisor model enters.

Existence of a supported biorthogonal right inverse from the genuine
NF523 weighted Gram data, and original NF528 approximation convergence,
are separate source-specific obligations.
-/

/-- The unchanged original strict two-collar physical geometry. -/
def neutralNF543OriginalCollars : Set ℝ :=
  Set.Ioo (-(11 / 10 : ℝ)) (-(11 / 10 : ℝ) + 1 / 500) ∪
  Set.Ioo ((11 / 10 : ℝ) - 1 / 500) (11 / 10 : ℝ)

/-- Every Schwartz test vanishing outside the unchanged two collars is
supported in the original physical L² window (almost everywhere). -/
theorem neutralNF543OriginalCollarSchwartz_supported
    (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ) →
      (g.toLp 2 volume) x = 0 := by
  filter_upwards [g.coeFn_toLp 2 volume] with x hx hout
  rw [hx]
  apply hg x
  intro hE
  rcases hE with hleft | hright
  · exact hout ⟨hleft.1.le, by linarith [hleft.2]⟩
  · exact hout ⟨by linarith [hright.1], hright.2.le⟩

/-- Original selected moment map on physical L² vectors. A genuine
weighted 242-dimensional moment system will supply this map; it is
not replaced by numerical or Green data. -/
abbrev NeutralNF543Moments := RealComplexL2 →ₗ[ℂ] (Fin 242 → ℂ)

/-- Supported smooth correction map from the 242 defect coordinates.
The same physical L² moment functionals are applied to the source. -/
abbrev NeutralNF543RightInverse :=
  (Fin 242 → ℂ) →ₗ[ℂ] 𝓢(ℝ, ℂ)

/-- Defect correction of the original same-source L² moment vector
using a Schwartz test and a finite-rank bump operator. -/
def neutralNF543Correct
    (M : NeutralNF543Moments) (R : NeutralNF543RightInverse)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ)) : 𝓢(ℝ, ℂ) :=
  g + R (M ell - M (g.toLp 2 volume))

/-- Provided R is biorthogonal to the true physical source moments,
the corrected test has EXACTLY all 242 original moments. Nothing is
assumed about the numerical coefficients of the original U400 source. -/
theorem neutralNF543Correct_moments
    (M : NeutralNF543Moments) (R : NeutralNF543RightInverse)
    (hR : ∀ d : Fin 242 → ℂ, M ((R d).toLp 2 volume) = d)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ)) :
    M ((neutralNF543Correct M R ell g).toLp 2 volume) = M ell := by
  let d := M ell - M (g.toLp 2 volume)
  have ht :
      (g + R d).toLp 2 volume =
        g.toLp 2 volume + (R d).toLp 2 volume := by
    exact map_add (SchwartzMap.toLpCLM ℂ ℂ 2 volume) g (R d)
  change M ((g + R d).toLp 2 volume) = M ell
  rw [ht, map_add, hR d]
  dsimp [d]
  abel

/-- If every correction direction remains in the original collars,
so does the source-exact 242-moment correction. -/
theorem neutralNF543Correct_supported
    (M : NeutralNF543Moments) (R : NeutralNF543RightInverse)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0)
    (hR : ∀ (d : Fin 242 → ℂ) (x : ℝ),
      x ∉ neutralNF543OriginalCollars → (R d) x = 0) :
    ∀ x : ℝ,
      x ∉ neutralNF543OriginalCollars →
        (neutralNF543Correct M R ell g) x = 0 := by
  intro x hx
  simp [neutralNF543Correct, hg x hx, hR _ x hx]

/-- The full original smooth-test triple gate, with the *genuine*
finite-rank right-inverse and collar-support hypotheses explicit:
(1) strict two-collar support, (2) all original 242 moments identical,
(3) authentic logarithmic Hilbert carrier with exactly the corrected
physical L² test. This does NOT assert ell itself is H¹, or that a
particular NF528 Gram inverse has already been built in Lean. -/
theorem neutralNF543Correct_hasOriginalLogCarrierAnd242Moments
    (M : NeutralNF543Moments) (R : NeutralNF543RightInverse)
    (hRight : ∀ d : Fin 242 → ℂ, M ((R d).toLp 2 volume) = d)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0)
    (hRSupport : ∀ (d : Fin 242 → ℂ) (x : ℝ),
      x ∉ neutralNF543OriginalCollars → (R d) x = 0) :
    ∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val =
          (neutralNF543Correct M R ell g).toLp 2 volume ∧
        M ((neutralNF543Correct M R ell g).toLp 2 volume) = M ell := by
  let f : 𝓢(ℝ, ℂ) := neutralNF543Correct M R ell g
  have hsupport : ∀ᵐ x ∂volume,
      x ∉ Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ) →
      (f.toLp 2 volume) x = 0 :=
    neutralNF543OriginalCollarSchwartz_supported f
      (neutralNF543Correct_supported M R ell g hg hRSupport)
  obtain ⟨k, hk⟩ :=
    neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
      (11 / 10 : ℝ) (f.toLp 2 volume) hsupport
        (neutralSchwartzPhysical_quadraticFourierMoment f)
  exact ⟨k, hk, neutralNF543Correct_moments M R hRight ell g⟩

end
end WeilDefect
