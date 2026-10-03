import WeilDefect.Morphology.NeutralNativeWeakDerivative

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped BigOperators

/-- The full actual compact Green column is supported in the retained window. -/
theorem neutralNativeGreenColumn_supported (a : ℝ) (z : ℂ) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a →
      neutralDirichletGreenColumnL2 a z x = 0 := by
  filter_upwards [(neutralDirichletGreenColumn_memLp a z).coeFn_toLp] with x hx
  intro hout
  change (neutralDirichletGreenColumn_memLp a z).toLp
    (neutralDirichletGreenColumn a z) x = 0
  rw [hx]
  simp [neutralDirichletGreenColumn, hout]

/-- The actual compact derivative column has the same support. -/
theorem neutralNativeGradientColumn_supported (a : ℝ) (z : ℂ) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a →
      neutralDirichletGradientColumnL2 a z x = 0 := by
  filter_upwards [(neutralDirichletGradientColumn_memLp a z).coeFn_toLp] with x hx
  intro hout
  change (neutralDirichletGradientColumn_memLp a z).toLp
    (neutralDirichletGradientColumn a z) x = 0
  rw [hx]
  simp [neutralDirichletGradientColumn, hout]

/-- Compact support survives the actual L2 Green synthesis, by continuity
of the existing physical outside-restriction map. -/
theorem neutralNativeGreenSynthesis_supported
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a →
      neutralNativeGreenSynthesis a data v x = 0 := by
  apply (neutralOutsideRestriction_zero_iff a _).mp
  have h := (neutralNativeGreenSynthesis_hasSum a ha data C hCount v).mapL
    (neutralOutsideRestriction a)
  have hz (g : ZetaShellIndex count) :
      neutralOutsideRestriction a
        (v g • neutralDirichletGreenColumnL2 a (data.gamma g)) = 0 := by
    rw [map_smul]
    have hc := (neutralOutsideRestriction_zero_iff a _).mpr
      (neutralNativeGreenColumn_supported a (data.gamma g))
    rw [hc, smul_zero]
  have ht := h.tsum_eq.symm
  simpa only [hz, tsum_zero] using ht

/-- Compact support survives the actual L2 derivative synthesis. Combined
with its global weak derivative identity, both spatial witnesses are attached. -/
theorem neutralNativeGradientSynthesis_supported
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a →
      neutralNativeGradientSynthesis a data v x = 0 := by
  apply (neutralOutsideRestriction_zero_iff a _).mp
  have h := (neutralNativeGradientSynthesis_hasSum a ha data C hCount v).mapL
    (neutralOutsideRestriction a)
  have hz (g : ZetaShellIndex count) :
      neutralOutsideRestriction a
        (v g • neutralDirichletGradientColumnL2 a (data.gamma g)) = 0 := by
    rw [map_smul]
    have hc := (neutralOutsideRestriction_zero_iff a _).mpr
      (neutralNativeGradientColumn_supported a (data.gamma g))
    rw [hc, smul_zero]
  have ht := h.tsum_eq.symm
  simpa only [hz, tsum_zero] using ht

end

end WeilDefect
