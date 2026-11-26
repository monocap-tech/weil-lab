import WeilDefect.Arithmetic.ActualZetaIV105AOriginalPhysicalActionSpectrum

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- Uncut physical inverse action, not an assertion of support. -/
def neutralIV105BInverse (a : ℝ) (u : 𝓢(ℝ,ℂ)) : RealComplexL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).symm (neutralIV105ASpectrum a u)

theorem neutralIV105BInverse_fourier (a : ℝ) (u : 𝓢(ℝ,ℂ)) :
    (𝓕 (neutralIV105BInverse a u) : RealComplexL2) =
      neutralIV105ASpectrum a u :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).apply_symm_apply _

theorem neutralIV105BInverse_pair (a : ℝ) (u v : 𝓢(ℝ,ℂ)) :
    inner ℂ (neutralIV105BInverse a u) (v.toLp 2 volume) =
      inner ℂ (neutralIV105ASpectrum a u) (𝓕 (v.toLp 2 volume) : RealComplexL2) := by
  exact (Lp.fourierTransformₗᵢ ℝ ℂ).symm.inner_map_eq_flip _ _

/-- Both physical moment columns, with original crossed coefficients. -/
def neutralIV105BPole (a : ℝ) (u : 𝓢(ℝ,ℂ)) : RealComplexL2 :=
  sourceWindowMoment a (-(1/2)) (u.toLp 2 volume) • neutralMomentColumnL2 a (1/2) +
    sourceWindowMoment a (1/2) (u.toLp 2 volume) • neutralMomentColumnL2 a (-(1/2))

theorem neutralIV105BPole_pair (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    inner ℂ (neutralIV105BPole a u) (v.toLp 2 volume) =
      inner ℂ (neutralIV102Lift a u hu)
        (neutralLogPoleOperator a (neutralIV102Lift a v hv)) := by
  rw [neutralLogPoleOperator_mixed, neutralIV102Lift_physical,
    neutralIV102Lift_physical]
  simp only [neutralIV105BPole, inner_add_left, inner_smul_left,
    neutralMomentColumnL2_inner]

def neutralIV105BAction (a : ℝ) (u : 𝓢(ℝ,ℂ)) : RealComplexL2 :=
  neutralIV105BInverse a u + neutralIV105BPole a u

/-- Full physical mixed action on supported tests; no cutoff or projection yet. -/
theorem neutralIV105BAction_pair (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Mixed a u v =
      inner ℂ (neutralIV105BAction a u) (v.toLp 2 volume) := by
  rw [neutralIV105AMixed_spectrum_pole a ha u v hu hv,
    neutralIV105BAction, inner_add_left, neutralIV105BInverse_pair,
    neutralIV105BPole_pair a u v hu hv]

#print axioms neutralIV105BInverse_fourier
#print axioms neutralIV105BInverse_pair
#print axioms neutralIV105BPole_pair
#print axioms neutralIV105BAction_pair
end
end WeilDefect
