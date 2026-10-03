import WeilDefect.Morphology.NeutralNativeDirichletSummability

namespace WeilDefect

noncomputable section

open MeasureTheory InnerProductSpace
open scoped BigOperators ENNReal

/-- The actual square-summable native shell coefficient space. -/
abbrev NeutralNativeShellCoefficients (count : ℕ → ℕ) :=
  lp (fun _ : ZetaShellIndex count => ℂ) 2

private theorem native_square_summable_smul
    {ι : Type*} (v : ι → RealComplexL2)
    (hv : Summable (fun i => ‖v i‖ ^ 2))
    (u : lp (fun _ : ι => ℂ) 2) :
    Summable (fun i => u i • v i) := by
  have hu : Summable (fun i => ‖u i‖ ^ 2) := by
    simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
      (lp.hasSum_norm (p := (2 : ℝ≥0∞)) (by norm_num) u).summable
  have hn : Summable (fun i => ‖u i • v i‖) := by
    apply Summable.of_nonneg_of_le (fun i => norm_nonneg _) (fun i => ?_) (hu.add hv)
    rw [norm_smul]
    nlinarith [sq_nonneg (‖u i‖ - ‖v i‖)]
  exact hn.of_norm

/-- Genuine convergence of the full Green-column synthesis. -/
theorem neutralNativeGreenSeries_summable
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (u : NeutralNativeShellCoefficients count) :
    Summable (fun g => u g • neutralDirichletGreenColumnL2 a (data.gamma g)) :=
  native_square_summable_smul _
    (neutralNativeDirichlet_green_square_summable a ha data C hCount) u

/-- Genuine convergence of the compact derivative-column synthesis. -/
theorem neutralNativeGradientSeries_summable
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (u : NeutralNativeShellCoefficients count) :
    Summable (fun g => u g • neutralDirichletGradientColumnL2 a (data.gamma g)) :=
  native_square_summable_smul _
    (neutralNativeDirichlet_gradient_square_summable a ha data C hCount) u

/-- Actual physical vector synthesized from the full native Green columns. -/
def neutralNativeGreenSynthesis
    {count : ℕ → ℕ} (a : ℝ) (data : ActualProblemOneShellData count)
    (u : NeutralNativeShellCoefficients count) : RealComplexL2 :=
  ∑' g, u g • neutralDirichletGreenColumnL2 a (data.gamma g)

/-- Actual physical vector synthesized from the compact derivative columns.
Its weak-derivative relation to the Green synthesis is a separate obligation. -/
def neutralNativeGradientSynthesis
    {count : ℕ → ℕ} (a : ℝ) (data : ActualProblemOneShellData count)
    (u : NeutralNativeShellCoefficients count) : RealComplexL2 :=
  ∑' g, u g • neutralDirichletGradientColumnL2 a (data.gamma g)

theorem neutralNativeGreenSynthesis_hasSum
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (u : NeutralNativeShellCoefficients count) :
    HasSum (fun g => u g • neutralDirichletGreenColumnL2 a (data.gamma g))
      (neutralNativeGreenSynthesis a data u) :=
  (neutralNativeGreenSeries_summable a ha data C hCount u).hasSum

theorem neutralNativeGradientSynthesis_hasSum
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (u : NeutralNativeShellCoefficients count) :
    HasSum (fun g => u g • neutralDirichletGradientColumnL2 a (data.gamma g))
      (neutralNativeGradientSynthesis a data u) :=
  (neutralNativeGradientSeries_summable a ha data C hCount u).hasSum

/-- Same-vector mixed pairing of the actual Green synthesis. -/
theorem neutralNativeGreenSynthesis_inner
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (u : NeutralNativeShellCoefficients count) (f : RealComplexL2) :
    inner ℂ f (neutralNativeGreenSynthesis a data u) =
      ∑' g, u g * inner ℂ f (neutralDirichletGreenColumnL2 a (data.gamma g)) := by
  have h := (neutralNativeGreenSynthesis_hasSum a ha data C hCount u).mapL (innerSL ℂ f)
  simpa only [innerSL_apply_apply, inner_smul_right] using h.tsum_eq.symm

/-- Same-vector mixed pairing of the actual derivative synthesis. -/
theorem neutralNativeGradientSynthesis_inner
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (u : NeutralNativeShellCoefficients count) (f : RealComplexL2) :
    inner ℂ f (neutralNativeGradientSynthesis a data u) =
      ∑' g, u g * inner ℂ f (neutralDirichletGradientColumnL2 a (data.gamma g)) := by
  have h := (neutralNativeGradientSynthesis_hasSum a ha data C hCount u).mapL (innerSL ℂ f)
  simpa only [innerSL_apply_apply, inner_smul_right] using h.tsum_eq.symm

end

end WeilDefect
