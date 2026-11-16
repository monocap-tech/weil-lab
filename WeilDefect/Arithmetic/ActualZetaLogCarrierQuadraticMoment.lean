import WeilDefect.Morphology.NeutralLogHilbertCarrier

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform

/-!
NF540: a concrete sufficient logarithmic-energy carrier criterion for
THE EXISTING ORIGINAL physical L² function. The spectral weight is the
unchanged log(exp 1 + |ξ|), not an invented source/symbol.
-/

/-- The authentic logarithmic Fourier weight is dominated by a
quadratic moment. This uses no zeta-zero data, RH or Green synthesis. -/
theorem neutralLogarithmicFourierWeight_le_quadraticMoment
    (ξ : ℝ) :
    logarithmicFourierWeight ξ ≤ Real.exp 1 + 1 + ξ ^ 2 := by
  unfold logarithmicFourierWeight
  have hx : 0 ≤ Real.exp 1 + |ξ| :=
    le_of_lt (add_pos_of_pos_of_nonneg (Real.exp_pos _) (abs_nonneg _))
  have hlog := Real.log_le_self hx
  have hsquare : |ξ| ^ 2 = ξ ^ 2 := sq_abs ξ
  have hquad := sq_nonneg (|ξ| - 1)
  nlinarith [sq_nonneg ξ]

/-- The complete original log-energy integral is finite whenever
the SAME physical L² vector has a finite quadratic Fourier moment.
This is the relevant regularity gate for smooth original collar tests;
it does not assume weighted carrier membership in its conclusion. -/
theorem neutralFiniteLogFourierEnergy_of_quadraticMoment
    (f : RealComplexL2)
    (hMoment : Integrable (fun ξ : ℝ =>
      (Real.exp 1 + 1 + ξ ^ 2) *
        ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume) :
    Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ *
        ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume := by
  apply hMoment.mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f : RealComplexL2)).norm.pow 2)
  · filter_upwards [] with ξ
    have hlow : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    have hpoly : 0 ≤ Real.exp 1 + 1 + ξ ^ 2 := by positivity
    have hnsq : 0 ≤ ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2 := sq_nonneg _
    simp only [Real.norm_eq_abs]
    rw [abs_of_nonneg (mul_nonneg hlow hnsq)]
    exact mul_le_mul_of_nonneg_right
      (neutralLogarithmicFourierWeight_le_quadraticMoment ξ) hnsq

/-- Full authentic supported logarithmic Hilbert carrier admission,
under the finite quadratic Fourier moment hypothesis for the SAME
physical L² vector. This has no Green span or source interpolation.
The remaining task for compact-smooth collars is to derive hMoment
from the actual smooth test's Fourier derivative regularity. -/
theorem neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
    (a : ℝ) (f : RealComplexL2)
    (hsupport : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0)
    (hMoment : Integrable (fun ξ : ℝ =>
      (Real.exp 1 + 1 + ξ ^ 2) *
        ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume) :
    ∃ k : NeutralLogHilbertCarrier a, neutralLogPhysical k.val = f := by
  let v : neutralCanonicalLogFormDomain a :=
    ⟨f, hsupport, neutralFiniteLogFourierEnergy_of_quadraticMoment f hMoment⟩
  exact ⟨neutralCanonicalToLogHilbert v, neutralLogPhysical_weighted v⟩

end
end WeilDefect
