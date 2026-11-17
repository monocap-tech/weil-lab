import WeilDefect.Arithmetic.ActualZetaOriginalEndpointTwistedPanels
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointLogGeometry
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointMollifier

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped Interval

/-! NF585: attach the full interval calculation to the literal
historical half-carrier, by reflection in B and the exact
exponential phase. All integrals are the original ones. -/

theorem neutralNF585Half_reflection (U : ℝ → ℝ) (d : ℝ) :
    neutralNF575OriginalEndpointHalf U (neutralNF578B-d) =
      (Ioo (0:ℝ) neutralNF578Delta).indicator
        (fun d => neutralNF585TwistedAmplitude U 0 d*
          neutralNF584LogKernel neutralNF578B d) d := by
  have he : neutralNF578B-d ∈ Ioo ((11/10:ℝ)-1/500) (11/10:ℝ) ↔
      d ∈ Ioo (0:ℝ) neutralNF578Delta := by
    simp only [mem_Ioo,neutralNF578B,neutralNF578Delta]
    constructor <;> intro h <;> constructor <;> linarith [h.1,h.2]
  unfold neutralNF575OriginalEndpointHalf
  by_cases hd : d ∈ Ioo (0:ℝ) neutralNF578Delta
  · rw [if_pos (he.mpr hd),indicator_of_mem hd]
    rw [neutralNF584LogKernel_eq_ratio _ _ (by unfold neutralNF578B; norm_num) hd.1]
    unfold neutralNF585TwistedAmplitude neutralNF578B
    rw [sub_sub_cancel]
    simp
  · rw [if_neg (fun h => hd (he.mp h)),indicator_of_notMem hd]

theorem neutralNF585LiteralHalf_integrable (U : ℝ → ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B)) :
    Integrable (neutralNF575OriginalEndpointHalf U) volume := by
  have hδ : 0 ≤ neutralNF578Delta := by unfold neutralNF578Delta; norm_num
  have hA : ContinuousOn (neutralNF585TwistedAmplitude U 0) (uIcc 0 neutralNF578Delta) := by
    rw [uIcc_of_le hδ]
    exact neutralNF585Twisted_continuousOn U 0 hU
  have hl := (neutralNF584LogKernel_intervalIntegrable neutralNF578B 0
    neutralNF578Delta).continuousOn_mul hA
  have hr : Integrable (fun d => neutralNF575OriginalEndpointHalf U
      (neutralNF578B-d)) volume := by
    simp_rw [neutralNF585Half_reflection]
    exact (integrable_indicator_iff measurableSet_Ioo).mpr
      ((intervalIntegrable_iff_integrableOn_Ioo_of_le hδ).mp hl)
  exact (integrable_comp_sub_left _ neutralNF578B).mp hr

/-- Exact entire-frequency identity: the NF584 interval amplitude
is the same physical half integral at the full complex z. -/
theorem neutralNF585LiteralHalf_transform (U : ℝ → ℝ) (z : ℂ) :
    neutralNF579RawTransform (neutralNF575OriginalEndpointHalf U) z =
      Complex.exp (Complex.I*(z.re:ℂ)*(neutralNF578B:ℂ)) *
        (∫ d in (0:ℝ)..neutralNF578Delta,
          neutralNF584Amplitude neutralNF578B (neutralNF585A U z.im) d*
            neutralNF584Phase z.re d) := by
  let B := neutralNF578B
  let δ := neutralNF578Delta
  let K := Complex.exp (Complex.I*(z.re:ℂ)*(B:ℂ))
  let f : ℝ → ℂ := fun x => (neutralNF575OriginalEndpointHalf U x:ℂ)*
    Complex.exp (Complex.I*(z*(x:ℂ)))
  let P : ℝ → ℂ := fun d => neutralNF584Amplitude B (neutralNF585A U z.im) d*
    neutralNF584Phase z.re d
  have he (d : ℝ) : f (B-d) = (Ioo (0:ℝ) δ).indicator (fun d => K*P d) d := by
    dsimp [f]
    rw [neutralNF585Half_reflection U d]
    by_cases hd : d ∈ Ioo (0:ℝ) δ
    · rw [indicator_of_mem hd,indicator_of_mem hd]
      have hz : z = (z.re:ℂ)+Complex.I*(z.im:ℂ) := by
        apply Complex.ext <;> simp [Complex.mul_re,Complex.mul_im]
      have hp : Complex.I*(z*((B-d:ℝ):ℂ)) =
          Complex.I*(z.re:ℂ)*(B:ℂ) +
          ((-z.im*(B-d):ℝ):ℂ) + (-(Complex.I*(z.re:ℂ))*(d:ℂ)) := by
        calc
          _ = Complex.I*(((z.re:ℂ)+Complex.I*(z.im:ℂ))*((B-d:ℝ):ℂ)) :=
            congrArg (fun w : ℂ => Complex.I*(w*((B-d:ℝ):ℂ))) hz
          _ = _ := by
            push_cast
            linear_combination (Complex.I_mul_I)*(z.im:ℂ)*((B:ℂ)-(d:ℂ))
      rw [hp,Complex.exp_add,Complex.exp_add]
      dsimp [K,P,neutralNF584Amplitude,neutralNF585A,
        neutralNF585TwistedAmplitude,neutralNF584Phase]
      simp only [zero_mul,neg_zero,Real.exp_zero,mul_one,Complex.ofReal_mul,
        Complex.ofReal_exp]
      ring
    · rw [indicator_of_notMem hd,indicator_of_notMem hd]
      simp
  have hδ : 0 ≤ δ := by unfold δ neutralNF578Delta; norm_num
  calc
    neutralNF579RawTransform (neutralNF575OriginalEndpointHalf U) z =
        ∫ x : ℝ, f x := rfl
    _ = ∫ d : ℝ, f (B-d) := (integral_sub_left_eq_self f volume B).symm
    _ = ∫ d : ℝ, (Ioo (0:ℝ) δ).indicator (fun d => K*P d) d := by
      apply integral_congr_ae
      filter_upwards [] with d
      exact he d
    _ = ∫ d in Ioo (0:ℝ) δ, K*P d := integral_indicator measurableSet_Ioo
    _ = ∫ d in (0:ℝ)..δ, K*P d := by
      rw [intervalIntegral.integral_of_le hδ,integral_Ioc_eq_integral_Ioo]
    _ = K*(∫ d in (0:ℝ)..δ, P d) := intervalIntegral.integral_const_mul K P

theorem neutralNF585LiteralHalf_strip
    (U U' : ℝ → ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hU' : ContinuousOn U' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hder : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      HasDerivAt U (U' x) x)
    (h0 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U x| ≤ neutralNF578C0)
    (h1 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U' x| ≤ (7/10^4:ℝ))
    (z : ℂ) (hz : |z.im| ≤ 1/2) :
    ‖neutralNF579RawTransform (neutralNF575OriginalEndpointHalf U) z‖ ≤
      (1/40000:ℝ)*neutralNF575StripEnvelope z.re := by
  rw [neutralNF585LiteralHalf_transform,norm_mul]
  have hp : ‖Complex.exp (Complex.I*(z.re:ℂ)*(neutralNF578B:ℂ))‖ = 1 := by
    rw [Complex.norm_exp]
    simp [Complex.mul_re,Complex.mul_im]
  rw [hp,one_mul]
  unfold neutralNF575StripEnvelope
  simpa only [mul_div_assoc] using
    neutralNF585TwistedPanel_strip U U' hU hU' hder h0 h1 z.re z.im hz

end
end WeilDefect
