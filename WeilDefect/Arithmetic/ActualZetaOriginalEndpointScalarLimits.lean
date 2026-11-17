import Mathlib.Analysis.Calculus.BumpFunction.Convolution
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped Convolution

/-!
NF580: scalar fixed-frequency limits for normalized smooth
mollification and real Fourier evaluation. Independent of the
pending physical graph and source-specific endpoint estimates.

We use Mathlib's normalized-bump convolution limit only on the
continuous exponential, not on the singular physical carrier.
-/

theorem neutralNF580RealPhase_norm (t x : ℝ) :
    ‖Complex.exp (Complex.I * ((t : ℂ) * (x : ℂ)))‖ = 1 := by
  rw [Complex.norm_exp]
  simp [Complex.mul_re, Complex.mul_im]

/-- At any fixed real frequency a positive normalized bump of
shrinking radius has complex Fourier mass tending to one. -/
theorem neutralNF580NormalizedBump_sampleLimit
    {ι : Type*} {l : Filter ι}
    (φ : ι → ContDiffBump (0 : ℝ))
    (hφ : Tendsto (fun i => (φ i).rOut) l (nhds 0))
    (t : ℝ) :
    Tendsto (fun i => ∫ x : ℝ, ((φ i).normed volume x : ℂ) *
      Complex.exp (Complex.I * ((t : ℂ) * (x : ℂ)))) l (nhds (1 : ℂ)) := by
  let g : ℝ → ℂ := fun x => Complex.exp (Complex.I * ((t : ℂ) * (-(x : ℂ))))
  have hg : Continuous g := by
    dsimp [g]
    fun_prop
  have h := ContDiffBump.convolution_tendsto_right_of_continuous
    (μ := (volume : Measure ℝ)) hφ hg (0 : ℝ)
  have he (i : ι) :
      (((φ i).normed volume) ⋆[ContinuousLinearMap.lsmul ℝ ℝ, volume] g) 0 =
      ∫ x : ℝ, ((φ i).normed volume x : ℂ) *
        Complex.exp (Complex.I * ((t : ℂ) * (x : ℂ))) := by
    rw [convolution_lsmul]
    apply integral_congr_ae
    filter_upwards [] with x
    simp [g, Complex.real_smul]
  have hzero : g 0 = 1 := by simp [g]
  simpa only [he, hzero] using h

/-- Ordinary integrability of the unchanged half-carrier suffices
for the real-frequency limit. No L² dilation limit is assumed. -/
theorem neutralNF580RealTransform_sampleLimit
    (h : ℝ → ℝ) (hh : Integrable h volume)
    (u : ℕ → ℝ) (t : ℝ)
    (hu : Tendsto u atTop (nhds t)) :
    Tendsto (fun n => ∫ x : ℝ, (h x : ℂ) *
      Complex.exp (Complex.I * ((u n : ℂ) * (x : ℂ)))) atTop
      (nhds (∫ x : ℝ, (h x : ℂ) *
        Complex.exp (Complex.I * ((t : ℂ) * (x : ℂ))))) := by
  let F : ℝ → ℝ → ℂ := fun a x => (h x : ℂ) *
    Complex.exp (Complex.I * ((a : ℂ) * (x : ℂ)))
  have hm (a : ℝ) : AEStronglyMeasurable (F a) volume := by
    have hcast : AEStronglyMeasurable (fun x => (h x : ℂ)) volume :=
      Complex.continuous_ofReal.comp_aestronglyMeasurable hh.aestronglyMeasurable
    have hp : Continuous (fun x : ℝ =>
        Complex.exp (Complex.I * ((a : ℂ) * (x : ℂ)))) := by fun_prop
    exact hcast.mul hp.aestronglyMeasurable
  have hb (a x : ℝ) : ‖F a x‖ = ‖h x‖ := by
    simp only [F, norm_mul, neutralNF580RealPhase_norm, mul_one, Complex.norm_real]
  have hpoint (x : ℝ) : Tendsto (fun n => F (u n) x) atTop (nhds (F t x)) := by
    have hc : Continuous (fun a => F a x) := by
      dsimp [F]
      fun_prop
    exact hc.continuousAt.tendsto.comp hu
  exact tendsto_integral_of_dominated_convergence (fun x => ‖h x‖)
    (fun n => hm (u n)) hh.norm
    (fun n => Eventually.of_forall fun x => (hb (u n) x).le)
    (Eventually.of_forall hpoint)

/-- Compact physical support and integrability pay the complex
exponential twist at any fixed z, including off-axis samples. -/
theorem neutralNF580Twisted_integrable
    (h : ℝ → ℝ) (hh : Integrable h volume)
    (A : ℝ) (hA : 0 ≤ A)
    (hsupp : ∀ x, A < |x| → h x = 0)
    (z : ℂ) :
    Integrable (fun x : ℝ => (h x : ℂ) *
      Complex.exp (Complex.I * (z * (x : ℂ)))) volume := by
  let f : ℝ → ℂ := fun x => (h x : ℂ) *
    Complex.exp (Complex.I * (z * (x : ℂ)))
  let C := Real.exp (|z.im| * A)
  have hcast : AEStronglyMeasurable (fun x => (h x : ℂ)) volume :=
    Complex.continuous_ofReal.comp_aestronglyMeasurable hh.aestronglyMeasurable
  have hp : Continuous (fun x : ℝ =>
      Complex.exp (Complex.I * (z * (x : ℂ)))) := by fun_prop
  have hf : AEStronglyMeasurable f volume := hcast.mul hp.aestronglyMeasurable
  have hmajor : Integrable (fun x => C * ‖h x‖) volume := hh.norm.const_mul C
  apply hmajor.mono' hf
  filter_upwards [] with x
  by_cases hx : |x| ≤ A
  · have hb : -(z.im*x) ≤ |z.im| * A := by
      calc
        _ ≤ |z.im*x| := neg_le_abs _
        _ = |z.im| * |x| := abs_mul _ _
        _ ≤ _ := mul_le_mul_of_nonneg_left hx (abs_nonneg _)
    have hr : (Complex.I * (z * (x : ℂ))).re = -(z.im*x) := by
      simp [Complex.mul_re, Complex.mul_im]
    change ‖(h x : ℂ) * Complex.exp (Complex.I * (z * (x : ℂ)))‖ ≤ C * ‖h x‖
    rw [norm_mul, Complex.norm_real, Complex.norm_exp, hr, mul_comm C]
    exact mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hb) (norm_nonneg _)
  · have hz : h x = 0 := hsupp x (lt_of_not_ge hx)
    simp [f, hz]

end
end WeilDefect
