import WeilDefect.Morphology.NeutralNativeDirichletCoordinates

namespace WeilDefect

noncomputable section

open MeasureTheory

/-- The retained actual shell energy is the energy of the two concrete
physical L2 coordinates of the full endpoint-corrected Green column. -/
theorem neutralNativeDirichlet_energy_coordinates
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (g : ZetaShellIndex count) :
    problemOneDirichletEnergy a (data.gamma g) =
      ‖neutralDirichletGradientColumnL2 a (data.gamma g)‖ ^ 2 +
        (1 / 4 : ℝ) * ‖neutralDirichletGreenColumnL2 a (data.gamma g)‖ ^ 2 := by
  rw [← problemOneColumnEnergySq_eq_dirichletEnergy a (data.gamma g) ha
    (actualProblemOneGreenDenom_ne_zero data g)]
  exact neutralDirichletGreen_nativeL2_energy a (data.gamma g) ha
    (actualProblemOneGreenDenom_ne_zero data g)

/-- WD-T28 square summability now has an actual physical coordinate witness. -/
theorem neutralNativeDirichlet_coordinates_summable
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C) :
    Summable (fun g : ZetaShellIndex count =>
      ‖neutralDirichletGradientColumnL2 a (data.gamma g)‖ ^ 2 +
        (1 / 4 : ℝ) * ‖neutralDirichletGreenColumnL2 a (data.gamma g)‖ ^ 2) := by
  have hs := wd_t28_actual_dirichlet_energy_summable a ha data C hCount
  have heq : (fun g : ZetaShellIndex count =>
      problemOneDirichletEnergy a (data.gamma g)) =
      (fun g : ZetaShellIndex count =>
        ‖neutralDirichletGradientColumnL2 a (data.gamma g)‖ ^ 2 +
          (1 / 4 : ℝ) * ‖neutralDirichletGreenColumnL2 a (data.gamma g)‖ ^ 2) := by
    funext g
    exact neutralNativeDirichlet_energy_coordinates a ha data g
  rwa [heq] at hs

/-- The compact derivative columns are genuinely square summable. -/
theorem neutralNativeDirichlet_gradient_square_summable
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C) :
    Summable (fun g : ZetaShellIndex count =>
      ‖neutralDirichletGradientColumnL2 a (data.gamma g)‖ ^ 2) := by
  apply Summable.of_nonneg_of_le (fun g => sq_nonneg _)
    (fun g => ?_) (wd_t28_actual_dirichlet_energy_summable a ha data C hCount)
  rw [neutralNativeDirichlet_energy_coordinates a ha data g]
  have hm := sq_nonneg ‖neutralDirichletGreenColumnL2 a (data.gamma g)‖
  linarith

/-- The full endpoint-corrected Green columns are genuinely square summable. -/
theorem neutralNativeDirichlet_green_square_summable
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C) :
    Summable (fun g : ZetaShellIndex count =>
      ‖neutralDirichletGreenColumnL2 a (data.gamma g)‖ ^ 2) := by
  have hs := (wd_t28_actual_dirichlet_energy_summable a ha data C hCount).mul_left 4
  apply Summable.of_nonneg_of_le (fun g => sq_nonneg _) (fun g => ?_) hs
  rw [neutralNativeDirichlet_energy_coordinates a ha data g]
  have hd := sq_nonneg ‖neutralDirichletGradientColumnL2 a (data.gamma g)‖
  linarith

end

end WeilDefect
